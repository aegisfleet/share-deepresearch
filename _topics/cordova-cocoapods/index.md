---
layout: topic
title: "CordovaとiOSにおけるCocoaPodsとfastlaneを用いた堅牢なビルド・署名パイプラインの構築"
date: 2025-06-18
prompt: "iOSのアプリをCordovaで作成する際、CocoaPodsによりライブラリの管理を行いたい。fastlaneで署名の設定を行う想定なのだが、ビルド環境の構成について調査を行い、署名のやり方など注意すべきポイントをまとめて欲しい。"
category: "engineering"
tags: [開発環境]
audio: "/share-deepresearch/assets/audio/cordova-cocoapods.mp3"
supplementary_materials:
  - title: "Cordova iOS: 堅牢なビルド・署名パイプラインの構築"
    url: "/share-deepresearch/topics/cordova-cocoapods/infographic.html"
  - title: "Cordova iOS開発の完全自動化ガイド"
    url: "/share-deepresearch/topics/cordova-cocoapods/reveal.html"
---

# **CordovaとiOSにおけるCocoaPodsとfastlaneを用いた堅牢なビルド・署名パイプラインの構築**

## **導入**

### **目的**

本レポートは、CordovaベースのiOSアプリケーション向けに、堅牢かつ自動化されたビルドおよびリリースパイプラインを確立するための、専門家レベルの包括的なガイドを提供することを目的とします。本稿では、Cordova、依存関係管理のためのCocoaPods、そしてビルドとコード署名自動化のためのfastlaneの統合について詳述します。

### **対象読者**

本レポートは、プロフェッショナルなビルドインフラの構築または最適化を担うモバイルアプリケーション開発者およびDevOpsエンジニアを対象としています。

### **基本理念**

本レポートは、手動介入を最小限に抑え、platformsディレクトリの一時的な性質といったCordova開発における一般的な落とし穴に耐性を持つ、宣言的でバージョン管理された、回復力のあるアーキテクチャを推奨します。

---

## **第1部 基盤となる構成：宣言的なプロジェクトコア**

このパートでは、プロジェクト構成の「信頼できる唯一の情報源（Single Source of Truth）」を確立し、config.xmlに焦点を当てます。目標は、プラットフォームの再構築後も存続する方法で、プロジェクトの構造と依存関係を可能な限り定義することです。

### **1.1. config.xmlの中心的な役割**

config.xmlはCordovaアプリケーションの設計図です。メタデータだけでなく、プラットフォーム固有の重要な動作も制御します 。堅牢なパイプラインのためには、これがアイデンティティとコア設定の決定的な情報源でなければなりません。

#### **主な構成要素**

* **アプリケーションID:** プライマリのidとversionを定義します。iOSに特化して上書きするためにios-CFBundleIdentifierとios-CFBundleVersionを使用し、Androidのパッケージ名が異なる場合にクリーンな分離を確保します 。これは、バンドルIDによってアプリを識別するfastlane matchにとって極めて重要です。  
* **iOSデプロイメントターゲット:** サポートする最小のiOSバージョンを\<preference name="deployment-target" value="12.0" /\>を使用して設定します。これはCocoaPodsの依存関係解決に直接影響を与える重要な設定です 2。

config.xmlをIDとプラットフォームターゲットに関する揺るぎない情報源として扱うことは、回復力のあるビルドシステムに向けた第一歩です。Xcodeプロジェクトでの逸脱や手動変更は、一時的なアンチパターンと見なすべきであり、config.xml内の宣言的な解決策またはフックに置き換えられるべきです。このアプローチの背景には、ビルドの失敗がしばしば下流の構成不一致に起因するという事実があります。例えば、あるCocoaPodsライブラリがプロジェクトで設定されたバージョンよりも高いiOSバージョンを要求した場合、ビルドは失敗します 2。この問題の根本的な解決策は、Xcodeプロジェクトを直接編集するのではなく、

config.xmlでデプロイメントターゲットを引き上げることです。これにより、cordova prepareが実行されるたびに、常に正しい設定を持つXcodeプロジェクトが生成されることが保証されます。

### **1.2. cordova-plugin-cocoapod-supportxによるCocoaPodsの統合**

Cordovaは、cordova platform rm iosコマンドの実行後も存続する方法でCocoaPodsの依存関係をネイティブに管理しません。platforms/ios内のPodfileを手動で編集する方法は非常に脆弱です。このギャップを埋めるためにはプラグインが必要です。

#### **プラグイン選定の論理的根拠**

調査からはcordova-plugin-cocoapods-support 3 とそのフォークである

cordova-plugin-cocoapod-supportx 6 が候補として挙がります。後者のフォークは積極的にメンテナンスされており、オリジナルや新しいバージョンのCocoaPodsに存在するバグを修正しているため 6、現代的なビルド環境において推奨される選択肢となります。

#### **インストール**

cordova plugin add cordova-plugin-cocoapod-supportx \--save

#### **動作メカニズム**

このプラグインはCordovaのビルドプロセスにフックし、config.xmlやplugin.xmlファイルからカスタムタグを読み取り、pod installを実行する前にplatforms/ios/Podfileを動的に生成します 3。これにより、ネイティブの依存関係定義が宣言的かつ回復力のあるものになります。

#### **config.xmlにおける詳細な\<pod\>タグ設定**

config.xml内の\<platform name="ios"\>ブロックが、すべてのCocoaPods定義の置き場所となります。

* **基本的なPod:** \<pod name="Alamofire" version="\~\> 5.0" /\> 3  
* **GitベースのPod:** \<pod name="GitPod1" git="https://github.com/blakgeek/something" tag="v1.0.1" /\> (branchやcommitもサポート) 3  
* **ビルド構成固有のPod:** \<pod name="Foobar" configurations="release,debug" /\> 3  
* **Podspecベース:** \<pod name="JSONKit" podspec="https://example.com/JSONKit.podspec" /\> 3  
* **CordovaライクなSpec:** \<pod name="JustLikeCordova" spec="\~\> 2.0.0"/\> 3  
* **トラブルシューティング用属性:** \<pod name="Lock" fix-bundle-path="Lock/Auth0.bundle"/\> は、新しいCocoaPodsバージョンで発生するリソースバンドルパスの問題を解決します 5。

#### **\<pods-config\>によるグローバルなPod設定**

\<platform name="ios"\>内に配置されるこのタグは、生成されるPodfileのグローバル設定を制御します。

* ios-min-version="12.0": Podfileにplatform :ios, '12.0'を設定します 3。  
* use-frameworks="true": Podfileにuse\_frameworks\!を追加します。これはSwiftベースのPodに不可欠です 3。注意点として、これはブリッジングヘッダーを無効にするため、一部のプロジェクトで問題を引き起こす可能性があります 6。  
* \<source url="..."/\>: プライベートなPodスペックリポジトリを追加します 3。

このアプローチの核心は、宣言的な定義によって命令的なプロセスを制御することにあります。Cordovaの根本的な課題は、cordova platform add iosのような命令的なコマンドが、手動での変更が失われやすい一時的なプロジェクトを生成する点にあります。cordova-plugin-cocoapod-supportxを使用することで、config.xmlがネイティブの依存関係が「どうあるべきか」を宣言する、宣言的なレイヤーを導入します。プラグインのフックは、その宣言に一致するようにPodfileを命令的に作成します。このパターンこそが安定性の鍵です。これにより、開発者はリポジトリをクローンし、npm installとcordova prepareを実行するだけで、Xcodeを一度も開くことなく、完全に構成されたネイティブプロジェクトを手に入れることができるのです。

---

## **第2部 fastlane matchによるコード署名の自動化**

このパートでは、プロジェクトの定義から、複雑でしばしば苦痛を伴うiOSのコード署名プロセスへと移行し、matchを決定的な解決策として提示します。

### **2.1. matchの哲学：中央集権的な署名機関**

手動でのコード署名は、CI/CD失敗の主要な原因です。証明書は失効し、秘密鍵は失われ、プロビジョニングプロファイルは同期が取れなくなります。fastlane matchは、署名IDをコードとして扱うことでこの問題を解決します 8。

matchは、必要なすべての証明書とプロビジョニングプロファイルを作成・維持し、それらを中央のプライベートGitリポジトリ（またはS3/Google Cloud）に暗号化して保存します 8。チームメンバーとCIサーバーはこの単一の情報源から情報を引き出すため、「私のマシンでは動作する」という問題が解消されます。

### **2.2. 初期セットアップとリポジトリ構成**

1. **セキュアなリポジトリの作成:** GitHubやBitbucket上のプライベートGitリポジトリが標準的な選択肢です 11。  
2. **matchの初期化:** プロジェクトのルートでfastlane match initを実行します。ストレージモードとしてgitを選択し、プライベートリポジトリのSSH URLを提供します 8。  
3. **fastlane/Matchfileの設定:** initコマンドによって生成されるこのファイルに構成を保存します 11。  
   * git\_url: 証明書リポジトリのURL。  
   * type: デフォルトのプロファイルタイプ（例: appstore, development）。  
   * app\_identifier: アプリケーションのバンドルID。config.xmlと一致する必要があります。  
   * username: Apple Developerアカウントのメールアドレス。  
4. **（任意だが推奨）既存プロファイルのクリーンアップ:** クリーンな状態から始めるために、fastlane match nuke distributionおよびfastlane match nuke developmentを使用して、Apple Developer Portalから既存の証明書とプロファイルをすべて失効させることができます 13。これは強力なコマンドであり注意が必要ですが、  
   matchが完全に管理下におけることを保証します。

### **2.3. 実践におけるmatchワークフロー**

* **認証情報（Credentials）の生成:** fastlane match appstoreとfastlane match developmentを実行します。これにより以下の処理が行われます。  
  1. リポジトリに存在しない場合、新しい配布用および開発用の証明書を作成します。  
  2. 指定されたapp\_identifier用の新しいプロビジョニングプロファイルを作成します。  
  3. これらすべてのアセットを暗号化し、Gitリポジトリにプッシュします 8。  
  4. ローカルのキーチェーンと\~/Library/MobileDevice/Provisioning Profilesにインストールします。  
* **新しいマシン/CIサーバーでの利用:** fastlane match appstore \--readonlyを実行するだけで、リポジトリから既存の証明書とプロファイルをフェッチしてインストールし、数秒でビルド用のマシン構成が完了します 8。

### **2.4. 高度な設定：App IDケーパビリティの同期**

プッシュ通知やSign in with Appleのようなサービスを追加すると、Developer Portal上のApp IDを更新する必要があります。これにより、そのIDに関連する既存のすべてのプロビジョニングプロファイルが無効になります 16。

この問題を解決するには、単にmatchを再実行するだけでは不十分です。明確な複数ステップのプロセスが必要です。

1. **サービスの有効化:** produceアクションを使用して、App IDのケーパビリティをプログラムで有効にします。これは、Webポータルでの手動クリックよりも優れており、Fastfileでスクリプト化できます。  
   * fastlane produce enable\_services \--apple-pay \--push-notification \-a "com.your.app.id" 17  
2. **無効化の確認:** このアクションがDeveloper Portal上の古いプロファイルを無効にしたことを理解します。  
3. **matchによるプロファイルの再生成:** ここでmatchを再度実行しますが、新しく有効化されたケーパビリティを含む新しいプロファイルを確実に作成するためにforceフラグを使用します。  
   * fastlane match appstore \--force 8。  
     forceパラメータは、有効なプロファイルが既に存在する場合でも、新しいプロビジョニングプロファイルを作成するようmatchに指示します。これが新しいケーパビリティを取り込む鍵となります。

このワークフローは、専門家レベルのガイダンスを必要とする重要な注意点であり、本レポートの核心的な価値の一つです。

---

## **第3部 Fastfileにおける自動ビルドパイプラインの構築**

このセクションでは、前述の基礎的な要素を、fastlane/Fastfileで定義された実用的な自動パイプラインに統合します。

### **3.1. Cordovaビルドの実行戦略**

パイプラインの中核はCordovaビルドコマンドの実行です。fastlaneはこれを実現するためにいくつかの方法を提供しますが、それぞれに重要なアーキテクチャ上のトレードオフが存在します。

単純なsh 'cordova build ios' 19 は機能しますが、fastlaneにとってはブラックボックスです。署名情報をどう渡し、ビルドされた

.ipaファイルのパスをどう受け取るかといった問題は、脆弱なカスタムスクリプトにつながります。gym 20 のようなネイティブアクションはXcodeと深く統合されていますが、Cordovaが生成したプロジェクト向けには設計されておらず、プロジェクトファイルのアップグレードが必要になるなどの摩擦を生みます 22。

fastlane-plugin-cordova 19 のような専用プラグインが理想的な中間地点です。これはCordovaの規約を理解する高レベルAPIを提供しつつ、fastlaneのコンテキストと統合された（例：

matchの出力を読み取り、レーン変数を設定する）ファーストクラスのfastlaneアクションです。

**表1：Cordova向けfastlaneビルド戦略の比較**

| 戦略 | 利点 | 欠点 | 推奨度 |
| :---- | :---- | :---- | :---- |
| **fastlane-plugin-cordova** | Cordova向けに最適化。署名とビルドパラメータを抽象化。出力パスを環境変数で提供 23。 | プラグインへの依存が発生。 | **最高** |
| **ネイティブツール (gym)** | Xcodeビルドプロセスを詳細に制御可能 20。 | Cordovaが生成したプロジェクトとの互換性の問題（例：プロジェクトのアップグレードが必要）22。 | 中 |
| **シェルコマンド (sh)** | シンプルで直接的。 | fastlaneのコンテキスト（署名情報、出力パス）と統合されていないため、脆弱なスクリプトが必要 19。 | 低 |

### **3.2. 完全なFastfileのウォークスルー**

このセクションでは、ユーザーのテンプレートとして機能する、完全に注釈付きの本番環境対応のFastfileを提供します。これは、前述のすべての概念を組み合わせたものです。fastlane initが実行され、Appfileがapp\_identifier、apple\_id、team\_idで構成されていることを前提としています 23。

```Ruby
# fastlane/Fastfile

# 使用するfastlaneのバージョンを固定  
fastlane_version "2.210.0"   
default_platform :ios

platform :ios do  
  before_all do  
    # Rubyの依存関係がインストールされていることを確認  
    sh "bundle install"  
    # CocoaPodsが最新であることを確認  
    cocoapods(repo_update: true) # [26]  
  end

  desc "新しいベータ版をビルドし、TestFlightにアップロードします"  
  lane :beta do  
    # 1. セキュアなリポジトリから証明書とプロファイルを同期  
    # CI環境ではreadonlyを推奨  
    match(type: "appstore", readonly: is_ci) 

    # 2. ネイティブの依存関係がインストールされていることを確認  
    # これは 'cordova platform rm/add' の後に特に重要  
    cocoapods(  
      podfile: "./platforms/ios/Podfile"  
    )

    # 3. プラグインを使用してCordovaプロジェクトをビルド  
    # プラグインが署名情報をxcodebuildに渡す処理を担う  
    cordova(  
      platform: 'ios',  
      release: true,  
      device: true,  
      build_config_file: 'build.json' # オプション: カスタムビルドフラグ用  
      # プラグインは ENV を設定する [23]  
    )

    # 4. TestFlightへのアップロード  
    pilot(  
      ipa: ENV,  
      skip_waiting_for_build_processing: true  
    )  
  end

  #... App Store用の :release のような他のレーン  
end
```

Fastfile内の各ステップは、関連する情報源（例：match 8、

cordovaプラグイン 23、

cocoapodsアクション 26、

pilot 27）を参照しながら詳細に説明されます。

joshstrangeによる実例 28 は、構造の良い、ただし複雑な現実世界の参照となります。

---

## **第4部 堅牢なパイプラインのための重要な考慮事項とベストプラクティス**

この最終パートでは、基本的なスクリプトを、回復力のある本番グレードのパイプラインから区別する高度なトピックと一般的な障害モードについて説明します。

### **4.1. プラットフォームの揮発性の克服：Cordovaフックの役割**

Cordova自動化における最大の障害点は、platforms/iosディレクトリがビルド成果物と見なされるという事実にあります。これは、プラグインの問題を解決する一般的な修正方法であるcordova platform rm ios && cordova platform add iosによって削除および再生成される可能性があり、このディレクトリ内で行われた手動の変更はすべて失われます。

この問題に対する公式に認められた解決策がCordovaフックです。フックは、Cordova CLIのライフサイクルの特定の時点で実行されるスクリプトであり 29、ネイティブプロジェクトをプログラムで変更するための唯一の堅牢な方法です。

#### **実用例：構成ファイルのコピー**

特定のGoogleService-Info.plistや他の環境固有の構成ファイルを、プラットフォームが追加された後にXcodeプロジェクト構造にコピーする必要があるとします。

* **config.xmlでのフック定義:** \<hook src="scripts/copy\_ios\_config.js" type="after\_prepare" /\> 13  
* **Node.jsフックスクリプト (scripts/copy\_ios\_config.js):**  

  ```JavaScript
  #!/usr/bin/env node

  const fs = require('fs');  
  const path = require('path');

  module.exports = function(context) {  
      // このフックはiOSプラットフォームに対してのみ実行  
      if (!context.opts.platforms.includes('ios')) {  
          return;  
      }

      console.log('Executing after_prepare hook to copy iOS configuration files...');

      const projectRoot = context.opts.projectRoot;  
      const platformRoot = path.join(projectRoot, 'platforms/ios');

      // コピー元とコピー先のファイルを定義  
      const filesToCopy = {  
          'config/ios/GoogleService-Info.plist': 'AppName/Resources/GoogleService-Info.plist' // 'AppName'は実際のプロジェクト名に置き換える  
      };

      // プロジェクト名を取得 (config.xmlから)  
      const configXml = fs.readFileSync(path.join(projectRoot, 'config.xml'), 'utf-8');  
      const appName = /<name>(.*?)</name>/.exec(configXml);

      for (const srcFile in filesToCopy) {  
          const destFileRelative = filesToCopy[srcFile].replace('AppName', appName);  
          const srcPath = path.join(projectRoot, srcFile);  
          const destPath = path.join(platformRoot, destFileRelative);

          if (fs.existsSync(srcPath)) {  
              const destDir = path.dirname(destPath);  
              if (!fs.existsSync(destDir)) {  
                  fs.mkdirSync(destDir, { recursive: true });  
              }  
              fs.copyFileSync(srcPath, destPath);  
              console.log(`Copied ${srcPath} to ${destPath}`);  
          } else {  
              console.error(`Source file not found: ${srcPath}`);  
          }  
      }  
  };
  ```

  このスクリプトは、バージョン管理された場所（例：/config/ios）からplatforms/ios内の適切な場所へファイルをコピーする、堅牢で再現可能な方法を示しています 32。

### **4.2. バージョンマトリックスの航行**

このツールチェーンには、cordova-ios、node、npm、CocoaPods、Ruby、fastlane、および様々なプラグインといった複数の可動部分が含まれます。これらのいずれか一つにおけるバージョンの不一致が、パイプライン全体を破壊する可能性があります 2。

#### **解決策：バージョン管理の徹底**

* **GemfileとBundler:** Ruby環境にとってこれは交渉の余地がありません。fastlaneとそのすべてのプラグイン（fastlane-plugin-cordovaなど）のバージョンを固定するためにGemfileを作成する必要があります。すべてのfastlaneコマンドはbundle exec fastlane...で実行されるべきです 39。これにより、すべての開発者とCIサーバーが全く同じRuby gemバージョンを使用することが保証されます。  
* **package.json:** cordova、プラグイン、およびNode.jsベースのフックの依存関係を固定します。  
* **CocoaPods:** platforms/iosで生成されるPodfile.lockは.gitignoreに追加すべきです。信頼できる唯一の情報源はconfig.xml内の\<pod\>タグです。もしPodfile.lockをコミットする場合は、CIサーバー上のCocoaPodsのバージョンがそれを生成したものと一致することを確認し、警告やエラーを回避してください 36。推奨されるアプローチは、  
  cordova-plugin-cocoapod-supportxに各ビルドで新しく管理させることです。

### **4.3. 一般的なビルドエラーとトラブルシューティング**

このセクションは、パイプラインが失敗した際にユーザーが最初に対応するための実践的なガイドとして機能します。調査から得られた様々なエラー報告を構造化された形式で統合します。

**表2：一般的なCordova/CocoaPods/fastlaneビルドエラー**

| エラーメッセージ（または症状） | 考えられる原因 | 解決戦略 | 関連情報源 |
| :---- | :---- | :---- | :---- |
| The 'Pods-App' target overrides the LD\_RUNPATH\_SEARCH\_PATHS... | Xcodeプロジェクトのビルド設定がCocoaPodsによって設定された値を上書きしている。多くの場合、プラグインまたはbuild.jsonが原因。 | Xcodeプロジェクトのビルド設定でLD\_RUNPATH\_SEARCH\_PATHSに$(inherited)フラグを追加する。原因となっているプラグインを特定し修正するか、Cordovaフックで修正する。 | 2 |
| CocoaPods could not find compatible versions for pod... | Podが要求する最小デプロイメントターゲットが、プロジェクトで設定されているものより高い。 | config.xmlで\<preference name="deployment-target" value="..."/\>をPodが要求するバージョン以上に設定する。 | 2 |
| No such module 'ModuleName' (Swift Podの場合) | use\_frameworks\!がPodfileに設定されていないか、ブリッジングヘッダーの設定に問題がある。 | config.xmlで\<pods-config use-frameworks="true" /\>を設定する。Xcodeプロジェクトを開く際は.xcodeprojではなく.xcworkspaceを開く。 | 42 |
| fastlane matchが失敗 / Xcodeがプロファイルを見つけられない | 1\. App IDのケーパビリティが変更され、プロファイルが無効になった。 2\. 証明書がローカルのキーチェーンに正しくインストールされていない。 | 1\. produce enable\_servicesでケーパビリティを更新後、match \--forceでプロファイルを再生成する。 2\. matchを再実行して証明書をインストールする。 | 9 |
| 'GoogleCloudMessaging.h' file not found または他のPodヘッダーの問題 | CocoaPodsのインストールが不完全、またはXcodeのヘッダー検索パスが正しくない。 | platforms/iosからPods/と.xcworkspaceを削除し、cordova prepare iosを再実行してpod installをトリガーする。 | 44 |
| CocoaPodsのインストールが壊れている（Rubyバージョンの問題） | システムにインストールされているRubyのバージョンとCocoaPodsの互換性がない。 | rbenvやrvmを使用して、CocoaPodsがサポートする安定したRubyバージョン（例: macOSのシステムRuby）に切り替える。sudo gem install cocoapodsを再試行する。 | 37 |

---

## **結論と最終的な推奨事項**

### **推奨アーキテクチャの要約**

本レポートで概説したコア原則を再確認します。それは、cordova-plugin-cocoapod-supportxを使用した宣言的なconfig.xml、fastlane matchによる中央集権的な署名管理、そしてバージョン管理された環境（Gemfile、package.json）内でのfastlane-plugin-cordovaを介したビルド自動化です。

### **最終チェックリスト**

開発者が自身のセットアップを本レポートで概説されたベストプラクティスと照らし合わせて検証するための箇条書きリストです。

* config.xmlは、IDとPod依存関係の信頼できる唯一の情報源ですか？  
* cordova-plugin-cocoapod-supportxはインストールされていますか？  
* fastlane matchはセキュアなリポジトリで構成されていますか？  
* fastlaneとプラグインのバージョンを固定するためにGemfileが使用されていますか？  
* すべてのfastlaneコマンドはbundle execで実行されていますか？  
* プロジェクト固有の変更は、手動編集ではなくCordovaフックによって処理されていますか？  
* App IDのケーパビリティを更新するための明確なワークフローが存在しますか？

#### **引用文献**

1. Config.xml API \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x-2025.01/config\_ref/](https://cordova.apache.org/docs/en/12.x-2025.01/config_ref/)  
2. Help\! Cordova fails building iOS game · apache cordova ... \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/apache/cordova/discussions/441](https://github.com/apache/cordova/discussions/441)  
3. cordova-plugin-cocoapods-support/README.md at master \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/blakgeek/cordova-plugin-cocoapods-support/blob/master/README.md](https://github.com/blakgeek/cordova-plugin-cocoapods-support/blob/master/README.md)  
4. blakgeek/cordova-plugin-cocoapods-support: A Cordova ... \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/blakgeek/cordova-plugin-cocoapods-support](https://github.com/blakgeek/cordova-plugin-cocoapods-support)  
5. cordova-plugin-cocoapod-support \- NPM, 6月 18, 2025にアクセス、 [https://www.npmjs.com/package/cordova-plugin-cocoapod-support](https://www.npmjs.com/package/cordova-plugin-cocoapod-support)  
6. cordova-plugin-cocoapod-supportx Yarn, 6月 18, 2025にアクセス、 [https://classic.yarnpkg.com/en/package/cordova-plugin-cocoapod-supportx](https://classic.yarnpkg.com/en/package/cordova-plugin-cocoapod-supportx)  
7. cordova-plugin-cocoapod-supportx CDN by jsDelivr \- A CDN for npm and GitHub, 6月 18, 2025にアクセス、 [https://www.jsdelivr.com/package/npm/cordova-plugin-cocoapod-supportx](https://www.jsdelivr.com/package/npm/cordova-plugin-cocoapod-supportx)  
8. match \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/match/](https://docs.fastlane.tools/actions/match/)  
9. Codesigning concepts \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/codesigning/getting-started/](https://docs.fastlane.tools/codesigning/getting-started/)  
10. Tutorial: Apple code signing with Fastlane in CodeBuild using S3 for certificate storage, 6月 18, 2025にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/sample-fastlane.html](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-fastlane.html)  
11. Use case: fastlane and fastlane Match on Bitrise \- Bitrise Blog, 6月 18, 2025にアクセス、 [https://bitrise.io/blog/post/use-case-fastlane-and-fastlane-match](https://bitrise.io/blog/post/use-case-fastlane-and-fastlane-match)  
12. How to setup Fastlane and Match to release iOS apps automatically on CI/CD server, 6月 18, 2025にアクセス、 [https://www.revelo.com/blog/how-to-setup-fastlane-and-match-to-release-ios-apps-automatically-on-ci-cd-server](https://www.revelo.com/blog/how-to-setup-fastlane-and-match-to-release-ios-apps-automatically-on-ci-cd-server)  
13. Setting up Fastlane with Ionic/Cordova apps \- Josh Strange, 6月 18, 2025にアクセス、 [https://joshstrange.com/2017/10/14/setting-up-fastlane-with-ionic-cordova-apps/](https://joshstrange.com/2017/10/14/setting-up-fastlane-with-ionic-cordova-apps/)  
14. match\_nuke \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/match\_nuke/](https://docs.fastlane.tools/actions/match_nuke/)  
15. fastlane Tips and Tricks: Top fastlane Actions and How to Use Them \- Runway, 6月 18, 2025にアクセス、 [https://www.runway.team/blog/fastlane-tips-and-tricks-top-fastlane-actions-and-how-to-use-them](https://www.runway.team/blog/fastlane-tips-and-tricks-top-fastlane-actions-and-how-to-use-them)  
16. Enable app capabilities \- Identifiers \- Account \- Help \- Apple Developer, 6月 18, 2025にアクセス、 [https://developer.apple.com/help/account/identifiers/enable-app-capabilities/](https://developer.apple.com/help/account/identifiers/enable-app-capabilities/)  
17. produce \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/produce/](https://docs.fastlane.tools/actions/produce/)  
18. How to use Fastlane to enable capabilities in provision profile ..., 6月 18, 2025にアクセス、 [https://github.com/fastlane/fastlane/discussions/19280](https://github.com/fastlane/fastlane/discussions/19280)  
19. Build your Ionic or Cordova app with the cordova Fastlane plugin, 6月 18, 2025にアクセス、 [https://ionic.zone/fastlane/build-your-project-with-cordova-plugin](https://ionic.zone/fastlane/build-your-project-with-cordova-plugin)  
20. gym \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/gym/](https://docs.fastlane.tools/actions/gym/)  
21. xcodebuild \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/xcodebuild/](https://docs.fastlane.tools/actions/xcodebuild/)  
22. Build your Ionic or Cordova app with native tooling in Fastlane, 6月 18, 2025にアクセス、 [https://ionic.zone/fastlane/build-your-project-with-native-tooling](https://ionic.zone/fastlane/build-your-project-with-native-tooling)  
23. bamlab/fastlane-plugin-cordova \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/bamlab/fastlane-plugin-cordova](https://github.com/bamlab/fastlane-plugin-cordova)  
24. why fastlane working directory different than what I set \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/42426612/why-fastlane-working-directory-different-than-what-i-set](https://stackoverflow.com/questions/42426612/why-fastlane-working-directory-different-than-what-i-set)  
25. Initialize Fastlane for your Cordova iOS and Android apps \- ionic.zone, 6月 18, 2025にアクセス、 [https://ionic.zone/fastlane/initialize-fastlane-for-your-cordova-ios-and-android-apps](https://ionic.zone/fastlane/initialize-fastlane-for-your-cordova-ios-and-android-apps)  
26. cocoapods \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/actions/cocoapods/](https://docs.fastlane.tools/actions/cocoapods/)  
27. Ionic and Fastlane, 6月 18, 2025にアクセス、 [https://ionic.zone/fastlane](https://ionic.zone/fastlane)  
28. Fastfile for iOS/Android \- GitHub Gist, 6月 18, 2025にアクセス、 [https://gist.github.com/joshstrange/a3da9901cc84ae7f5d0b1b40dd110e0f](https://gist.github.com/joshstrange/a3da9901cc84ae7f5d0b1b40dd110e0f)  
29. Leveraging Cordova Hooks for Custom Build Automation Tasks Reintech media, 6月 18, 2025にアクセス、 [https://reintech.io/blog/leveraging-cordova-hooks-custom-build-automation](https://reintech.io/blog/leveraging-cordova-hooks-custom-build-automation)  
30. Hooks Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x-2025.01/guide/appdev/hooks/](https://cordova.apache.org/docs/en/12.x-2025.01/guide/appdev/hooks/)  
31. cordova-wrapper/hooks/README.md at master \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/frappe/cordova-wrapper/blob/master/hooks/README.md](https://github.com/frappe/cordova-wrapper/blob/master/hooks/README.md)  
32. Hooks Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/6.x/guide/appdev/hooks/](https://cordova.apache.org/docs/en/6.x/guide/appdev/hooks/)  
33. Hooks Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x/guide/appdev/hooks/](https://cordova.apache.org/docs/en/12.x/guide/appdev/hooks/)  
34. Using npm scripts for Cordova \- Josh Bavari's Thoughts, 6月 18, 2025にアクセス、 [http://jbavari.github.io/blog/2014/06/19/using-npm-scripts-for-cordova/](http://jbavari.github.io/blog/2014/06/19/using-npm-scripts-for-cordova/)  
35. Cordova hooks to copy file to specific platform using node. \- GitHub Gist, 6月 18, 2025にアクセス、 [https://gist.github.com/2804699db0cad824fa73](https://gist.github.com/2804699db0cad824fa73)  
36. The version of CocoaPods used to generate the lockfile (X.X.X) is higher than the version of the current executable (X.X.X) \- Ionic, 6月 18, 2025にアクセス、 [https://ionic.zendesk.com/hc/en-us/articles/14658104488343-The-version-of-CocoaPods-used-to-generate-the-lockfile-X-X-X-is-higher-than-the-version-of-the-current-executable-X-X-X](https://ionic.zendesk.com/hc/en-us/articles/14658104488343-The-version-of-CocoaPods-used-to-generate-the-lockfile-X-X-X-is-higher-than-the-version-of-the-current-executable-X-X-X)  
37. ios \- CocoaPods not installed or not in valid state \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/62593939/cocoapods-not-installed-or-not-in-valid-state](https://stackoverflow.com/questions/62593939/cocoapods-not-installed-or-not-in-valid-state)  
38. Cordova ios build failed caused by GooglePlus Plugin \- Ionic Forum, 6月 18, 2025にアクセス、 [https://forum.ionicframework.com/t/cordova-ios-build-failed-caused-by-googleplus-plugin/233695](https://forum.ionicframework.com/t/cordova-ios-build-failed-caused-by-googleplus-plugin/233695)  
39. Setup \- fastlane docs, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/getting-started/ios/setup/](https://docs.fastlane.tools/getting-started/ios/setup/)  
40. Getting started with fastlane for Android, 6月 18, 2025にアクセス、 [https://docs.fastlane.tools/getting-started/android/setup/](https://docs.fastlane.tools/getting-started/android/setup/)  
41. \[Camera Plugin\] Swift Language Version not compatible \- OutSystems, 6月 18, 2025にアクセス、 [https://www.outsystems.com/forums/discussion/99228/camera-plugin-swift-language-version-not-compatible/](https://www.outsystems.com/forums/discussion/99228/camera-plugin-swift-language-version-not-compatible/)  
42. Cordova plugin with Cocoapod dependency is not working properly \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/48098166/cordova-plugin-with-cocoapod-dependency-is-not-working-properly](https://stackoverflow.com/questions/48098166/cordova-plugin-with-cocoapod-dependency-is-not-working-properly)  
43. How to use Fastlane to enable capabilities in provision profile? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/68913813/how-to-use-fastlane-to-enable-capabilities-in-provision-profile](https://stackoverflow.com/questions/68913813/how-to-use-fastlane-to-enable-capabilities-in-provision-profile)  
