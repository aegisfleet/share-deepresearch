---
layout: topic
title: "Cordova iOSアプリケーションにおけるCocoaPods依存関係管理と自動署名の包括的ガイド"
date: 2025-06-18
prompt: "iOSのアプリをCordovaで作成する際、CocoaPodsによりライブラリの管理を行いたい。ビルド環境の構成について調査を行い、署名のやり方など注意すべきポイントをまとめて欲しい。"
category: "engineering"
tags: [開発環境]
audio: "/share-deepresearch/assets/audio/cordova-cocoapods.mp3"
supplementary_materials:
  - title: "Cordova iOS ビルド & 署名 自動化インフォグラフィック"
    url: "/share-deepresearch/topics/cordova-cocoapods/infographic.html"
  - title: "Cordova iOS開発の完全自動化ガイド"
    url: "/share-deepresearch/topics/cordova-cocoapods/reveal.html"
---

# **Cordova iOSアプリケーションにおけるCocoaPods依存関係管理と自動署名の包括的ガイド**

## **Part 1: 基礎概念：CordovaとCocoaPodsのシナジー**

本レポートは、Apache Cordovaフレームワークを使用してiOSアプリケーションを開発する際に、CocoaPodsを介してネイティブライブラリを統合し、ビルドプロセス全体を自動化するための包括的な技術ガイドである。環境構築の基本から、依存関係管理の高度な戦略、そしてCI/CDパイプラインに不可欠なコード署名の自動化まで、専門的かつ実践的な知見を提供する。

### **1.1. Apache Cordovaフレームワーク：ネイティブへの架け橋**

Apache Cordovaは、HTML、CSS、JavaScriptといった標準的なWeb技術を用いて、単一のコードベースから複数のプラットフォーム（iOS、Androidなど）向けのモバイルアプリケーションを構築するためのオープンソースフレームワークである 1。このアプローチは一般的に「ハイブリッドアプリケーション」開発として知られている 3。

#### **コアアーキテクチャ**

Cordovaの核心は、ネイティブアプリケーションのコンテナ内にWebコンテンツをパッケージ化する点にある 4。具体的には、アプリケーションはプラットフォーム固有のラッパーアプリケーションとして構築され、その内部に

WebViewと呼ばれるコンポーネントが配置される 1。この

WebViewが、アプリケーションのUIとロジックを担うWebコンテンツ（HTML、CSS、JavaScript）の実行環境として機能する 5。この構造により、Web開発者は既存のスキルセットを活用して、ネイティブアプリケーションを開発することが可能になる 3。

#### **WebViewコンポーネント**

WebViewは、アプリケーション内に組み込まれたブラウザエンジンであり、Webページを表示するためのネイティブUIコンポーネントである 3。Cordovaは、この

WebViewをフルスクリーンで表示し、アプリケーションの主要なインターフェースとして利用する。近年のCordovaでは、パフォーマンスと機能性が向上したWKWebViewをcordova-plugin-wkwebview-engineのようなプラグインを通じて利用することが推奨されている 6。これにより、より高速でモダンなWeb標準に準拠したアプリケーション体験を提供できる。

#### **プラグインエコシステム**

Cordovaの真の力は、その広範なプラグインエコシステムにある。Webアプリケーションは通常、セキュリティ上の理由からデバイスのネイティブ機能（カメラ、GPS、ファイルシステム、連絡先など）に直接アクセスすることができない 2。Cordovaプラグインは、このギャップを埋める「橋渡し」の役割を果たす 3。プラグインは、JavaScriptインターフェースと、各プラットフォームに対応するネイティブコード（iOSではObjective-CまたはSwift）のセットで構成される 7。開発者はJavaScriptからプラグインのAPIを呼び出すことで、間接的にネイティブ機能を実行できる 1。この仕組みにより、ハイブリッドアプリでありながら、プッシュ通知やデバイスハードウェアの操作といったネイティブアプリ同等の機能を実現できる 5。

#### **開発ワークフロー**

Cordova開発の典型的なワークフローは、Cordova CLI（Command-Line Interface）を中心に展開される 1。CLIは、プロジェクトの作成、プラットフォームの追加、プラグインの管理、ビルド、エミュレータでの実行といった一連のタスクを抽象化し、クロスプラットフォーム開発の複雑さを大幅に軽減する。開発者は主に

wwwディレクトリ内のWebコンテンツに集中し、プラットフォーム固有の実装の多くをCordovaとプラグインに委ねることができる 10。

### **1.2. CocoaPods：iOSにおけるデファクトスタンダードの依存関係マネージャー**

CocoaPodsは、SwiftおよびObjective-Cで記述されたiOS（およびmacOS）プロジェクトのための依存関係管理ツールである 11。Node.jsにおけるnpmやPythonにおけるpipと同様の役割を果たし 13、iOS開発コミュニティにおいて広く受け入れられているデファクトスタンダードとなっている。10万を超えるライブラリが利用可能で、300万以上のアプリケーションで使用されている実績がある 14。

#### **主要な成果物とその機能**

CocoaPodsのワークフローは、いくつかの重要なファイル（アーティファクト）によって支えられている。これらを理解することは、Cordovaとの連携を成功させる上で不可欠である。

* **Podfile**: プロジェクトが依存するライブラリ（Pod）を定義するための仕様ファイルである 11。開発者はこの平文テキストファイルに、使用したいライブラリの名前と、必要に応じてバージョン制約を記述する。これにより、プロジェクトの依存関係が明示的に管理される。  
* **Podfile.lock**: pod installコマンドを初めて実行した際に生成されるロックファイルである 11。このファイルには、  
  Podfileの定義に基づいて実際にインストールされた各Podの**正確なバージョン**が記録される。このPodfile.lockをバージョン管理システム（Gitなど）に含めることで、チーム内の全開発者やCI/CDサーバーが全く同じバージョンのライブラリを使用することが保証され、環境差異による「私の環境では動いたのに」という問題を防止する。これは再現可能なビルドを実現するための最も重要なファイルである。  
* **.xcworkspace**: pod installを実行すると、従来の.xcodeprojファイルに加えて、.xcworkspaceというXcodeワークスペースファイルが生成される 15。これ以降、開発者はXcodeでプロジェクトを開く際に、  
  .xcodeprojではなく、この.xcworkspaceファイルを開く必要がある 17。このワークスペースは、元のアプリケーションプロジェクトと、CocoaPodsが管理する依存ライブラリを含んだ  
  Podsプロジェクトを統合する役割を持つ。

### **1.3. 連携の戦略的意義：両者の長所を活かす**

CordovaとCocoaPodsを連携させることは、単なる技術的な選択肢ではなく、現代のハイブリッドアプリ開発における戦略的な決定である。

#### **根本的な課題**

Cordovaプラグインはネイティブコードをバンドルできるが、サードパーティ製の複雑なネイティブiOS SDK（例えば、Firebase、Stripe決済、高度な分析ツールなど）を導入する際、手動でのフレームワーク追加やプロジェクト設定の変更は非常に煩雑で、間違いが発生しやすい。さらに、多くの先進的なiOS SDKは、現在ではCocoaPodsを介してのみ配布されているのが実情である 11。

#### **解決策としての連携**

Cordovaプロジェクト内でCocoaPodsを利用することで、開発者はCocoaPodsエコシステムで利用可能な**あらゆるネイティブiOSライブラリ**をシームレスに統合できるようになる。これにより、標準的なCordovaプラグインだけでは実現が難しい高度な機能を、Cordovaアプリケーションに組み込むことが可能になる 11。

この連携は、Cordova自体がネイティブにサポートしている機能ではない。その代わりに、この自動化を実現するために専用のCordovaプラグイン（例：cordova-plugin-cocoapod-support）が利用される 16。このプラグインは、Cordovaのビルドプロセスに介入し、

config.xmlや各プラグインのplugin.xmlから依存関係を読み取り、動的にPodfileを生成してpod installコマンドを実行する。

この構造は、いわば「橋の上の橋」とも言える多層的な抽象化を実現している。CordovaがWebとネイティブの橋渡しをするのに対し 5、連携プラグインはCordovaとCocoaPodsエコシステムの橋渡しをする。この一連の自動化チェーン（

cordova prepare → プラグインフック実行 → Podfile生成 → pod install実行 → .xcworkspace生成 → Xcodeビルド）を理解することは、ビルドプロセスで問題が発生した際のトラブルシューティングにおいて極めて重要である。Xcodeでのビルドエラーが、実はその数ステップ前のPodfile生成の不備に起因することも少なくない。したがって、このプロセス全体を安定させ、デバッグ可能な状態に保つことが、堅牢な開発パイプラインを構築する鍵となる。

#### **連携によるメリット**

このアプローチは、依存関係の解決を自動化し、プロジェクト設定を簡素化するだけでなく、Cordovaプロジェクトを標準的なネイティブiOS開発の実践に近づける 11。これにより、プロジェクトのスケーラビリティと保守性が向上し、Web技術に精通した開発者とネイティブiOS開発に精通した開発者との協業も円滑になる 20。

## **Part 2: 開発・ビルド環境の構築**

安定したビルド環境の構築は、CordovaとCocoaPodsを連携させる上で最も重要なステップの一つである。ツールのバージョン間の互換性は、しばしば予期せぬビルドエラーの原因となるため、細心の注意を払う必要がある。

### **2.1. システムとツールチェーンの前提条件**

iOSアプリケーションをビルドするには、以下のツールチェーンを正確にセットアップする必要がある。

* **macOS**: iOSアプリの開発とビルドは、AppleのmacOS上でのみ可能である 21。  
* **Node.js**: Cordova CLIおよび関連するnpmパッケージの実行に必須である。要求されるバージョンは、使用するcordova-iosのバージョンに依存する 22。  
* **Ruby**: CocoaPodsはRubyで実装されたライブラリ（gem）であるため、Rubyの実行環境が必要である 11。macOSにはシステムRubyがプリインストールされているが、特にApple Silicon搭載Macでは、パーミッションの問題（  
  sudoの必要性）や互換性の問題を避けるため、rbenvやRVMといったバージョンマネージャーを用いて、ユーザー環境に別途Rubyをインストールすることが強く推奨される 26。  
* **Homebrew**: macOS用の推奨パッケージマネージャーであり、ios-deployやcocoapodsといった開発ツールのインストールに利用する 22。  
* **XcodeとXcode Command Line Tools**:  
  * **Xcode**: iOS SDKを含む統合開発環境（IDE）であり、iOS開発の根幹をなす 21。App StoreまたはApple DeveloperのWebサイトからダウンロードできる 22。App Storeへアプリを提出するには、最新バージョンのXcodeを使用する必要がある 23。  
  * **Xcode Command Line Tools**: Cordova CLIなどのコマンドラインツールがXcodeのビルドシステムと連携するために不可欠なコンポーネント群である 22。ターミナルで  
    xcode-select \--installを実行することでインストールが促される 24。このコマンドは、インストールを要求するGUIダイアログを起動する 30。  
* **デプロイおよび依存関係ツール**:  
  * **ios-deploy**: コマンドラインから物理iOSデバイスへアプリケーションをデプロイするためのユーティリティ。Homebrewを用いてbrew install ios-deployでインストールする 22。  
  * **cocoapods**: 依存関係マネージャー本体。RubyGemsを介してインストールされるが、依存関係の管理を確実にするため、Homebrew経由でのインストール（brew install cocoapods）が推奨される 22。

#### **表1: ツールとバージョンの互換性マトリクス**

開発を始める前に、使用するcordova-iosのバージョンと、それに対応する各ツールのバージョン要件を確認することが不可欠である。以下の表は、Cordovaの公式ドキュメントに基づいた互換性の概要を示す 24。

| Cordova-iOSバージョン | 最小iOSサポート | 要求Node.jsバージョン | 要求Xcodeバージョン | 要求CocoaPodsバージョン |
| :---- | :---- | :---- | :---- | :---- |
| 8.x | 13.0 | \>= 20.5.0 | \>= 15.x | \>= 1.8.0 |
| 7.x | 11.0 | \>= 16.13.0 | \>= 11.0.0 | \>= 1.8.0 |
| 6.x | 11.0 | \>= 10.0.0 | \>= 11.0.0 | \>= 1.8.0 |
| 5.x | 10.0 | \>= 6.0.0 | \>= 10.0.0 | \>= 1.0.1 |

出典: 24

この表は、安定した開発環境を構築するための基礎となる。特にNode.jsとXcodeのバージョンは、ビルドの成否に直接影響するため、プロジェクト開始時にチーム全体で統一することが重要である。

### **2.2. Cordovaプロジェクトの初期化とプラットフォーム統合**

開発環境が整ったら、Cordovaプロジェクトを作成し、iOSプラットフォームを追加する。

1. Cordova CLIのインストール:  
   ターミナルを開き、npmを使用してCordova CLIをグローバルにインストールする 33。  
   Bash  
   npm install \-g cordova

2. 新規プロジェクトの作成:  
   cordova createコマンドを使用して、新しいプロジェクトを生成する 8。  
   Bash  
   cordova create my-app com.example.myapp MyApp

   このコマンドの引数は、左から順に「プロジェクトフォルダ名」「アプリケーションID（iOSのBundle Identifier）」「アプリケーション表示名（Xcodeプロジェクト名）」を意味する 8。  
3. iOSプラットフォームの追加:  
   作成したプロジェクトディレクトリに移動し、cordova platform addコマンドでiOSプラットフォームを追加する 21。  
   Bash  
   cd my-app  
   cordova platform add ios

   このコマンドは、cordova-iosプラットフォームライブラリをダウンロードし、プロジェクト内にplatforms/iosディレクトリを生成する。このディレクトリには、ネイティブのXcodeプロジェクトファイル群が格納される 8。  
4. **ビルドと実行**:  
   * **ビルド**: cordova build iosコマンドでプロジェクトをコンパイルする 10。  
   * **シミュレータでの実行**: ios-simがインストールされていれば、cordova emulate iosコマンドでiOSシミュレータ上でアプリを起動できる 8。  
   * **Xcodeでのプロジェクト開封**: CocoaPodsによる依存関係の統合後、platforms/iosディレクトリ内に.xcworkspaceファイルが生成される。デバッグやプロファイリングのためにXcodeを使用する場合は、必ずこの.xcworkspaceファイルを開く必要がある 17。  
     .xcodeprojファイルを開くと、Podライブラリがリンクされず、コンパイルエラーが発生する。

## **Part 3: CocoaPods依存関係の統合と管理**

CordovaプロジェクトにネイティブのiOSライブラリを組み込むプロセスは、専用のプラグインによって自動化される。このセクションでは、その仕組みと具体的な依存関係の宣言方法、そしてビルドプロセスの流れを詳述する。

### **3.1. 自動化エンジン：cordova-plugin-cocoapod-support**

CordovaとCocoaPodsの連携を円滑に行うための鍵となるのが、cordova-plugin-cocoapod-support（またはそのフォークであるcordova-plugin-cocoapod-supportxなど）である 16。このプラグインはCordovaの標準機能ではなく、追加でインストールする必要がある。

* **目的**: このプラグインは、Cordovaのビルドプロセスにフックし、プロジェクト内の依存関係定義を基にPodfileを自動生成し、pod installを実行することで、手動でのXcodeプロジェクト編集を不要にする 19。AndroidにおけるGradleでの依存関係管理が標準でサポートされているのに対し、iOSではこの種のプラグインがその役割を担う 16。  
* **インストール**: Cordova CLIを使用してプラグインをプロジェクトに追加する。  
  Bash  
  cordova plugin add cordova-plugin-cocoapod-supportx

  注: cordova-plugin-cocoapod-supportは長期間更新されていないため、バグ修正や新機能が追加されているフォーク版（例: cordova-plugin-cocoapod-supportx）の使用が推奨される 16。  
* **動作メカニズム**: プラグインは、Cordovaのフックスクリプトを利用して動作する。具体的には、config.xml（アプリケーション全体）と、インストールされている全プラグインのplugin.xmlファイルをスキャンし、\<pod\>というXMLタグで宣言された依存関係をすべて収集する。その後、これらの情報を基にplatforms/ios/Podfileを動的に生成し、pod install（またはpod update）コマンドを内部で実行する 19。

### **3.2. 依存関係の宣言：config.xmlとplugin.xml**

CocoaPodsの依存関係は、その利用目的に応じて2つの異なるXMLファイルで宣言される。

* 再利用可能なプラグインの場合 (plugin.xml):  
  特定のネイティブSDKをラップするような再利用可能なCordovaプラグインを作成する場合、その依存関係はプラグイン自身のplugin.xmlファイル内で宣言する 16。これにより、プラグインは自己完結型となり、他のプロジェクトへの導入が容易になる。宣言は  
  \<platform name="ios"\>タグ内で行う。  
  **plugin.xmlでの記述例:**  
  XML  
  \<?xml version='1.0' encoding='UTF-8'?\>  
  \<plugin id\="cordova-plugin-my-custom-sdk" version\="1.0.0" xmlns\="http://apache.org/cordova/ns/plugins/1.0"\>  
      \<name\>My Custom SDK Plugin\</name\>  
      \<dependency id\="cordova-plugin-cocoapod-supportx"/\>  
      \<platform name\="ios"\>  
          \<pod name\="AFNetworking" spec\="\~\> 3.0" /\>  
      \</platform\>  
  \</plugin\>

* プロジェクト固有の要求の場合 (config.xml):  
  特定のアプリケーションでのみ使用するライブラリを追加する場合や、プラグイン間の依存関係の競合を解決する場合には、プロジェクトルートにあるconfig.xmlファイルに直接\<pod\>タグを記述する 16。  
  config.xmlでの宣言は、各plugin.xmlでの宣言よりも優先されるため、バージョン競合の解決に特に有効である 16。  
  **config.xmlでの記述例:**  
  XML  
  \<?xml version='1.0' encoding='utf-8'?\>  
  \<widget id\="com.example.myapp" version\="1.0.0" xmlns\="http://www.w3.org/ns/widgets" xmlns:cdv\="http://cordova.apache.org/ns/1.0"\>  
      \<name\>MyApp\</name\>  
     ...  
      \<platform name\="ios"\>  
         ...  
          \<pod name\="Alamofire" version\="5.4.0" /\>  
          \<pod name\="MyPrivatePod" git\="https://github.com/my-company/my-private-pod.git" tag\="v1.2.3" /\>  
          \<pod name\="DebugUtility" configuration\="debug" /\>  
      \</platform\>  
  \</widget\>

  このプラグインは、バージョン指定、Gitリポジトリからの直接取得（ブランチ、タグ、コミットハッシュ指定も可能）、ビルド構成ごとの依存関係指定など、CocoaPodsのPodfileがサポートする多様な宣言方法に対応している 16。

### **3.3. ビルドプロセスの解明：Cordovaフックの役割**

cordova-plugin-cocoapod-supportによる自動化は、Cordovaのフックシステムによって実現されている。

* **after\_prepareフック**: このプロセスで最も一般的に使用されるのがafter\_prepareフックである 19。このフックは、  
  cordova prepareコマンドが実行され、wwwディレクトリのWebアセットがplatforms/ios/wwwにコピーされ、ネイティブプロジェクトの基本的な構造が準備された**後**、かつXcodeによるコンパイルが開始される**前**に実行される。このタイミングは、ネイティブプロジェクト（Podfileの生成やpod installの実行など）に変更を加えるのに最適である。  
* **ステップ・バイ・ステップのフロー**:  
  1. 開発者がcordova build iosまたはcordova prepare iosコマンドを実行する。  
  2. Cordova CLIがplatforms/iosディレクトリを準備し、Webアセットをコピーする。  
  3. after\_prepareイベントが発火し、cordova-plugin-cocoapod-supportに登録されたフックスクリプトが呼び出される。  
  4. フックスクリプトがプロジェクトのconfig.xmlとpluginsディレクトリ内の全plugin.xmlを解析し、\<pod\>タグを収集する。  
  5. 収集した情報に基づき、platforms/ios/Podfileを生成または上書きする。  
  6. platforms/iosディレクトリ内でpod install \--verboseコマンドを実行する。  
  7. CocoaPodsが依存関係を解決し、必要なライブラリをダウンロードし、Podfile.lockと.xcworkspaceファイルを生成・更新する。  
  8. Cordovaのビルドプロセスが続行され、Xcodeのビルドツール（xcodebuild）が、新しく生成された.xcworkspaceを使用してアプリケーション本体とPodライブラリをコンパイルする。

### **3.4. 高度なPodfileのカスタマイズ（手動介入）**

プラグインによるPodfileの自動生成は強力だが、時にはそれだけでは不十分な場合がある。例えば、特定のPodライブラリが要求するビルド設定を適用するために、Podfileにpost\_installフックを追記する必要があるケースなどである 39。

* **課題**: cordova prepareが実行されるたびにPodfileが自動生成・上書きされるため、手動でPodfileに加えた変更は失われてしまう。  
* **解決策（ワークアラウンド）**: この問題を解決するには、独自のCordovaフックを利用する。具体的には、cordova-plugin-cocoapod-supportのフックが実行された**後**に実行される、自前のafter\_prepareフックを定義する。  
  1. プロジェクトルートにscriptsディレクトリを作成し、その中にカスタムフックスクリプト（例: scripts/customize\_podfile.js）を配置する。  
  2. config.xmlに、このカスタムフックを登録する。  
     XML  
     \<hook type\="after\_prepare" src\="scripts/customize\_podfile.js" /\>

  3. customize\_podfile.jsスクリプト内で、Node.jsのfsモジュールを使い、platforms/ios/Podfileを読み込む。  
  4. 読み込んだ内容の末尾に、必要なカスタムロジック（例: post\_installブロック）を追記する。  
  5. 変更した内容でPodfileを上書き保存する。

この手法により、自動生成の利便性を享受しつつ、プロジェクト固有の高度な要求にも対応できる柔軟性が得られる 39。これは、宣言的なXMLだけでは対応できない複雑なシナリオのための高度なテクニックである。

## **Part 4: CordovaにおけるiOSコード署名の完全ガイド**

iOSアプリのビルドプロセスにおいて、コード署名は最も複雑でつまずきやすい部分の一つである。特にCI/CD環境でのビルドを自動化するためには、手動でのXcode操作を排除し、コマンドラインから署名プロセスを完結させることが不可欠である。このセクションでは、Appleのコード署名の仕組みを解き明かし、Cordovaのbuild.jsonファイルを用いた自動化手法を詳細に解説する。

### **4.1. Appleのコード署名の解明**

iOSのコード署名は、アプリケーションが信頼できる開発元から提供され、改ざんされていないことを保証するための仕組みである。このプロセスは、いくつかの主要な要素から構成される。

* **署名証明書 (Signing Certificate)**: 開発者または開発チームを識別するための暗号鍵ペア（公開鍵と秘密鍵）。macOSのキーチェーンに保存される。主に「Development（開発用）」と「Distribution（配布用）」の2種類が存在する 22。  
* **App ID**: アプリケーションを一意に識別するためのID（例: com.mycompany.myapp）。プロビジョニングポータルで登録する 8。  
* **プロビジョニングプロファイル (Provisioning Profile)**: 署名証明書、App ID、そして（開発・アドホック配布の場合は）許可されたデバイスリストを紐付けるファイル。このファイルによって、特定のアプリが特定のデバイスにインストールされる権限が与えられる 22。

これらの要素を手動でXcodeプロジェクトに設定するのは、特にチーム開発や自動ビルドの文脈では非効率かつエラーの温床となる。目標は、これらの設定をすべてコマンドラインから注入し、ビルドプロセスを完全に自動化することである 40。

### **4.2. 自動化の鍵：build.json設定ファイル**

Cordovaは、この署名の自動化のためにbuild.jsonという設定ファイルを提供する。

* **目的**: build.jsonは、プロジェクトのルートディレクトリに配置するJSONファイルで、Cordova CLIに対して署名情報やビルド設定を提供する 41。このファイルを使用することで、Xcodeを一切開くことなく、コマンドラインからデバッグビルドやリリースビルドの署名が可能になる。  
* **使用方法**: cordova buildまたはcordova runコマンドに--buildConfigフラグを付けてbuild.jsonファイルのパスを指定する。  
  Bash  
  cordova build ios \--release \--device \--buildConfig=build.json

* **構造**: ファイルはトップレベルにiosキーを持ち、その下にdebugとreleaseのオブジェクトを配置して、それぞれのビルドタイプに応じた設定を記述する 41。

#### **表2: build.json iOS設定パラメータ詳解**

build.jsonを正しく構成するためには、各キーの意味と、その値の取得方法を正確に理解する必要がある。

| キー | 型 | 説明 | 値の取得方法 |
| :---- | :---- | :---- | :---- |
| codeSignIdentity | String | macOSのキーチェーンにインストールされているコード署名証明書の名前。一般的にデバッグ用は"iPhone Developer"、リリース用は"iPhone Distribution"または"Apple Distribution"といった文字列を含む。 | ターミナルでsecurity find-identity \-v \-p codesigningを実行。出力されたリストから適切な証明書の**引用符を含む完全な名前**をコピーする（例: "Apple Distribution: My Company Inc. (ABCDE12345)"） 45。 |
| developmentTeam | String | Apple Developerアカウントの10桁のチームID。Xcode 8以降の署名プロセスで必須。 | Apple Developerポータルにログインし、「Membership」セクションで確認できる 45。 |
| provisioningProfile | String | 使用するプロビジョニングプロファイルのUUID（Universally Unique Identifier）。手動署名に必須。 | Apple Developerポータルから.mobileprovisionファイルをダウンロードし、TextEditなどのテキストエディタで開く（Sublime Textなど一部のエディタでは正しく表示されない場合がある）。ファイル内の\<key\>UUID\</key\>を探し、その直後にある\<string\>タグ内の36文字のUUIDをコピーする 42。 |
| packageType | String | 生成するビルドアーカイブの種類を指定する。有効な値はdevelopment、ad-hoc、app-store、enterprise。 | 使用するプロビジョニングプロファイルの種別と一致させる必要がある 43。 |
| automaticProvisioning | Boolean | Xcodeの自動プロビジョニング機能を有効にする（主にCapacitorなどのエコシステムで見られるが、CordovaでもdevelopmentTeamを指定しprovisioningProfileを省略することで同様の挙動を促せる）。 | 純粋なCordovaでは直接的なフラグではないが、自動管理を行いたい場合はdevelopmentTeamのみを指定するアプローチを取る 43。 |

出典: 41

### **4.3. 実践的ウォークスルー：署名アセットの特定とbuild.jsonの作成**

以下に、build.jsonを作成するために必要な情報を特定する具体的な手順を示す。

**ステップ1: codeSignIdentityの特定**

1. macOSでターミナルを開く。  
2. security find-identity \-v \-p codesigningコマンドを実行する。  
3. 出力結果から、ビルドに必要な証明書（開発用または配布用）を見つけ、その行の"..."で囲まれた部分を完全にコピーする 45。

**ステップ2: developmentTeamの特定**

1. Webブラウザで([https://developer.apple.com/account)にログインする](https://www.google.com/search?q=https://developer.apple.com/account)%E3%81%AB%E3%83%AD%E3%82%B0%E3%82%A4%E3%83%B3%E3%81%99%E3%82%8B)。  
2. 「Membership」セクションに移動する。  
3. 表示される「Team ID」の10桁の英数字をコピーする 45。

**ステップ3: provisioningProfile UUIDの特定**

1. Apple Developer Portalの「Certificates, Identifiers & Profiles」セクションに移動する。  
2. 「Profiles」で、対象のApp IDに紐づくプロビジョニングプロファイル（開発用または配布用）を生成または選択し、ダウンロードする。  
3. ダウンロードした.mobileprovisionファイルを、macOSのTextEditアプリケーションで開く。  
4. ファイル内で文字列UUIDを検索する。\<key\>UUID\</key\>という行のすぐ下にある\<string\>...\</string\>タグに囲まれたUUID（例: 926c2bd6-8de9-4c2f-8407-1016d2d12954）をコピーする 42。

build.jsonの組み立て例  
上記で特定した情報を基に、プロジェクトのルートディレクトリにbuild.jsonファイルを作成する。

JSON

{  
    "ios": {  
        "debug": {  
            "codeSignIdentity": "Apple Development: John Appleseed (ABCDE12345)",  
            "provisioningProfile": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",  
            "developmentTeam": "A1B2C3D4E5",  
            "packageType": "development"  
        },  
        "release": {  
            "codeSignIdentity": "Apple Distribution: My Company Inc. (A1B2C3D4E5)",  
            "provisioningProfile": "yyyyyyyy-yyyy-yyyy-yyyy-yyyyyyyyyyyy",  
            "developmentTeam": "A1B2C3D4E5",  
            "packageType": "app-store"  
        }  
    }  
}

このファイルを適切に設定することで、cordova build ios \--release \--device \--buildConfig=build.jsonのような単一のコマンドで、署名済みのリリースビルドを生成することが可能になる。

## **Part 5: ベストプラクティスと高度なトラブルシューティング**

プロジェクトを健全に維持し、開発プロセスを円滑に進めるためには、いくつかのベストプラクティスと高度な問題解決策を理解しておくことが重要である。

### **5.1. バージョン管理戦略：platformsディレクトリのジレンマ**

Cordovaプロジェクトにおけるバージョン管理、特に.gitignoreの扱いは、議論の的となりやすい。

* **標準的なプラクティス**: Cordovaプロジェクトを新規作成すると、デフォルトで生成される.gitignoreファイルにはplatforms/およびplugins/ディレクトリが含まれている 52。この背景にある考え方は、これらのディレクトリの内容は  
  config.xmlとpackage.jsonからcordova prepareコマンドによっていつでも再生成できる「ビルド成果物」であるというものである 54。  
* **CocoaPodsがもたらす複雑性**: この標準的なプラクティスは、CocoaPodsを多用するプロジェクトにおいては問題を引き起こす可能性がある。platforms/iosディレクトリには、自動生成されたXcodeプロジェクトファイル群に加え、Podfile、そして最も重要なPodfile.lockファイルが含まれる。Podfile.lockは、すべての依存ライブラリの正確なバージョンを固定し、ビルドの再現性を保証する上で不可欠なファイルである 11。このファイルをバージョン管理から除外すると、開発者ごと、あるいはCIサーバーごとに  
  pod installが実行され、異なるバージョンのライブラリがインストールされてしまう危険性がある。これは、ビルドの失敗や実行時の予期せぬ不具合の直接的な原因となりうる。  
* 構成ドリフト問題と推奨される解決策:  
  再現性の高いビルドは、プロフェッショナルなソフトウェア開発における絶対的な要件である。Podfile.lockの主な目的は、チーム全体で依存関係のツリーを完全に一致させることにあるが 11、このファイルがGitで管理されていなければ、その目的は達成されない。このため、CocoaPodsに強く依存するCordovaプロジェクトにおいては、従来の「  
  platformsディレクトリを無視する」というアドバイスは、むしろアンチパターンとなり得る。  
  したがって、本レポートでは\*\*platforms/ディレクトリを.gitignoreから削除し、platforms/iosディレクトリ全体をバージョン管理下に置くこと\*\*を強く推奨する。これにより、Xcodeプロジェクトの設定、Podfile、そして決定的に重要なPodfile.lockがすべてバージョン管理され、チーム全体でのビルドの一貫性と再現性が保証される。リポジトリサイズが大きくなるというトレードオフは存在するが、ビルドの安定性というメリットはそれを十分に上回る。Git submodulesを利用するような代替戦略も存在するが 56、多くのチームにとっては過度に複雑であり、直接コミットするアプローチが最も堅牢かつシンプルである。

### **5.2. 依存関係地獄の解決：CocoaPodsバージョン競合への対応策**

複数のCordovaプラグインが、同じネイティブPodライブラリの異なる、互換性のないバージョンに依存している場合、ビルド時にバージョン競合エラーが発生する。これはCordovaとCocoaPodsを連携させる上で最も一般的な問題の一つである。

* 典型的なエラーメッセージ:  
  \[\!\] CocoaPods could not find compatible versions for pod "SomePod"  
  このエラーは、CocoaPodsが全プラグインの要求を同時に満たす単一のバージョンを見つけられないことを示している 55。  
* 依存関係解決の階層的アプローチ:  
  これらの競合を解決するためには、体系的なアプローチが必要である。様々な解決策が存在するが、それらは影響の大きさや介入の度合いに応じて階層的に適用することができる。最も侵襲性の低い方法から試し、段階的に強力な手段に移行するのが効果的である。  
* **競合解決プレイブック**:  
  1. **エラーの分析**: まず、CocoaPodsが出力するエラーメッセージを注意深く読む。どのPodが競合しているのか、そしてどのプラグインがどのバージョンを要求しているのかを正確に特定する。  
  2. 戦略1: config.xmlでのプラグイン順序の変更（最も低リスク）:  
     config.xml内の\<plugin\>タグの記述順序が、依存関係の解決に影響を与えることがある。より厳格なバージョン要件を持つ、あるいはより重要なプラグインをリストの最後に移動させることで、単純な競合が解決する場合がある 57。  
  3. 戦略2: config.xmlでのバージョン上書き（推奨される明示的解決策）:  
     cordova-plugin-cocoapod-supportの仕様により、プロジェクトのconfig.xmlで宣言された\<pod\>は、各プラグインのplugin.xml内の宣言よりも優先される 16。この仕組みを利用して、競合しているPodのバージョンを、すべてのプラグインの要求を満たす特定のバージョンに固定する。  
     XML  
     \<pod name\="GoogleUserMessagingPlatform" spec\="2.1.0" /\>

  4. 戦略3: プラグイン変数の利用:  
     競合しているプラグインのドキュメントを確認する。一部のプラグインは、インストール時に変数を渡すことで、依存するSDKのバージョンを指定できる機能を提供していることがある 61。  
     Bash  
     \# 例: firebasexプラグインでiOS Firebase SDKのバージョンを指定  
     cordova plugin add cordova-plugin-firebasex \--variable IOS\_FIREBASE\_SDK\_VERSION=8.13.0

  5. 戦略4: クリーン＆リビルド:  
     プロジェクトの状態が破損している可能性もある。完全なクリーンアップが問題を解決することがある。  
     Bash  
     cordova platform rm ios  
     \# 必要に応じてnode\_modules, plugins, Podfile.lockを削除  
     rm \-rf node\_modules/ plugins/ platforms/  
     npm install  
     cordova platform add ios  
     cordova build ios

  6. 戦略5: プラグインのフォーク（最終手段）:  
     上記のいずれの方法でも解決できない場合、問題を引き起こしているプラグインをフォーク（複製）し、そのplugin.xmlを直接編集して互換性のある依存関係バージョンを指定する。その後、ローカルまたはGitリポジトリからフォークしたプラグインをインストールする 57。これは最も手間がかかるが、完全な制御を可能にする最終手段である。

## **Part 6: 結論と戦略的提言**

本レポートでは、Apache CordovaとCocoaPodsを統合し、iOSアプリケーションを構築するための包括的な手法を詳述した。この連携は、Web技術の生産性とネイティブiOSエコシステムの強力なライブラリ群を組み合わせることで、高機能なハイブリッドアプリケーション開発を可能にする。

### **統合ワークフローの要約**

成功への道筋は、以下の3つの核心的な柱に基づいている。

1. **安定した環境の構築**: cordova-ios、Node.js、Xcode、CocoaPodsのバージョン互換性を確保し、rbenvなどを用いてクリーンなRuby環境を維持することが、すべての基本となる。  
2. **宣言的な依存関係管理**: cordova-plugin-cocoapod-supportのようなプラグインを活用し、config.xmlやplugin.xmlを通じてネイティブ依存関係を宣言的に管理する。これにより、手動でのXcodeプロジェクト編集を排除し、プロセスの自動化と再現性を高める。  
3. **完全自動化されたコード署名**: build.jsonファイルを用いて署名情報を外部化し、コマンドラインからビルドプロセスを完結させる。これは、継続的インテグレーション（CI）と継続的デプロイメント（CD）パイプラインを構築する上で不可欠である。

### **自動化の重要性**

本レポートで提示された個々のツールやテクニック（build.jsonの利用、platformsディレクトリのバージョン管理、依存関係解決プラグインなど）は、単なる便利な機能ではない。これらは、プロフェッショナルで、スケーラブルで、保守可能なハイブリッドアプリケーション開発パイプラインを構築するための必須コンポーネントである。

手動での作業、例えばXcodeを開いて署名設定を行うようなプロセス 22 は、自動化を妨げ、ヒューマンエラーを誘発する。開発者ごとに異なる環境は、予測不能なビルド失敗の温床となる。本レポートで概説した自動化戦略を組み合わせることによって初めて、Cordovaプロジェクトは単なる実験的な試みから、エンタープライズレベルの品質を持つ製品へと昇華する。

最終的な目標は、cordova build ios \--release \--buildConfig=build.jsonのような**単一のコマンド**によって、どの開発者のマシンでも、どのCIサーバー上でも、一貫して信頼性の高いビルド成果物を生成できる状態を実現することである。本レポートで詳述した戦略は、その目標を達成するための実践的なロードマップを提供するものである。このアプローチを採用することで、開発チームは複雑なビルド管理から解放され、アプリケーションの価値創造という本質的なタスクに集中することが可能となる。

#### **引用文献**

1. 【OSS情報アーカイブ】Apache Cordova \- マジセミ, 6月 18, 2025にアクセス、 [https://majisemi.com/topics/oss/4871/](https://majisemi.com/topics/oss/4871/)  
2. Apache Cordovaの完全ガイド：ハイブリッドアプリ開発を簡単に \- Capgo, 6月 18, 2025にアクセス、 [https://capgo.app/ja/blog/cordova-hybrid-app-development/](https://capgo.app/ja/blog/cordova-hybrid-app-development/)  
3. ブラウザの機能向上が後押しに――Web技術でスマホアプリを開発するハイブリッドアプリの強みとは \- CodeZine, 6月 18, 2025にアクセス、 [https://codezine.jp/article/detail/10464](https://codezine.jp/article/detail/10464)  
4. ハイブリッドアプリが開発できる「Apache Cordova」の紹介とAndroidアプリの作成手順 |, 6月 18, 2025にアクセス、 [https://vintage.ne.jp/blog/2014/11/354](https://vintage.ne.jp/blog/2014/11/354)  
5. Cordovaの使用方法を解説！React Nativeとの違いは？ \- toiroフリーランス, 6月 18, 2025にアクセス、 [https://freelance.shiftinc.jp/column/cordova](https://freelance.shiftinc.jp/column/cordova)  
6. cordova-plugin-wkwebview-engine on CocoaPods.org, 6月 18, 2025にアクセス、 [https://cocoapods.org/pods/cordova-plugin-wkwebview-engine](https://cocoapods.org/pods/cordova-plugin-wkwebview-engine)  
7. Plugin Development Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/10.x/guide/hybrid/plugins/](https://cordova.apache.org/docs/en/10.x/guide/hybrid/plugins/)  
8. Cordovaの環境構築をしてみる \#iOS \- Qiita, 6月 18, 2025にアクセス、 [https://qiita.com/katsu\_suzuki/items/2a9251f8a13812b03664](https://qiita.com/katsu_suzuki/items/2a9251f8a13812b03664)  
9. Apache Cordova 詳細情報 | OSSサポートのOpenStandia™【NRI】, 6月 18, 2025にアクセス、 [https://openstandia.jp/oss\_info/cordova/](https://openstandia.jp/oss_info/cordova/)  
10. Cordova Guide \- Evothings, 6月 18, 2025にアクセス、 [http://evothings.com/doc/build/cordova-guide.html](http://evothings.com/doc/build/cordova-guide.html)  
11. 【iOS開発】 CocoaPodsとは何なのか〜導入〜使い方まで徹底解説 ..., 6月 18, 2025にアクセス、 [https://tech-begin.com/programming-coding/ios/about-cocoapods/](https://tech-begin.com/programming-coding/ios/about-cocoapods/)  
12. Cocoapodsの使いかた \- Zenn, 6月 18, 2025にアクセス、 [https://zenn.dev/snake12379/articles/80583127601ceb](https://zenn.dev/snake12379/articles/80583127601ceb)  
13. podfileは何してるの？ \- Zenn, 6月 18, 2025にアクセス、 [https://zenn.dev/hikarugp24/articles/75e524f03a2595](https://zenn.dev/hikarugp24/articles/75e524f03a2595)  
14. CocoaPods, 6月 18, 2025にアクセス、 [https://cocoapods.org/](https://cocoapods.org/)  
15. Getting Started \- CocoaPods Guides, 6月 18, 2025にアクセス、 [https://guides.cocoapods.org/using/getting-started.html](https://guides.cocoapods.org/using/getting-started.html)  
16. cordova-plugin-cocoapod-supportx | Yarn, 6月 18, 2025にアクセス、 [https://classic.yarnpkg.com/en/package/cordova-plugin-cocoapod-supportx](https://classic.yarnpkg.com/en/package/cordova-plugin-cocoapod-supportx)  
17. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/10.x/guide/platforms/ios/](https://cordova.apache.org/docs/en/10.x/guide/platforms/ios/)  
18. iOSプロジェクトにおけるCocoaPodsとCarthageについて \- Zenn, 6月 18, 2025にアクセス、 [https://zenn.dev/kueharx/articles/40d66aad9afd5c](https://zenn.dev/kueharx/articles/40d66aad9afd5c)  
19. cordova-plugin-cocoapods-support/README.md at master \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/blakgeek/cordova-plugin-cocoapods-support/blob/master/README.md](https://github.com/blakgeek/cordova-plugin-cocoapods-support/blob/master/README.md)  
20. Kotlin Multiplatform Mobile（KMM）およびCompose Multiplatformを使用したモバイルアプリケーションの開発 | KINTO Tech Blog, 6月 18, 2025にアクセス、 [https://blog.kinto-technologies.com/posts/2023-08-15-kmm-compose-multiplatform/](https://blog.kinto-technologies.com/posts/2023-08-15-kmm-compose-multiplatform/)  
21. Apache Cordova | PlayCanvas Developer Site, 6月 18, 2025にアクセス、 [https://developer.playcanvas.com/ja/user-manual/publishing/mobile/cordova/](https://developer.playcanvas.com/ja/user-manual/publishing/mobile/cordova/)  
22. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x-2025.01/guide/platforms/ios/](https://cordova.apache.org/docs/en/12.x-2025.01/guide/platforms/ios/)  
23. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/11.x/guide/platforms/ios/](https://cordova.apache.org/docs/en/11.x/guide/platforms/ios/)  
24. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x/guide/platforms/ios/](https://cordova.apache.org/docs/en/12.x/guide/platforms/ios/)  
25. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/12.x/guide/platforms/ios/index.html](https://cordova.apache.org/docs/en/12.x/guide/platforms/ios/index.html)  
26. CocoaPods overview and setup | Kotlin Multiplatform Documentation \- JetBrains, 6月 18, 2025にアクセス、 [https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-cocoapods-overview.html](https://www.jetbrains.com/help/kotlin-multiplatform-dev/multiplatform-cocoapods-overview.html)  
27. Getting Started with iOS \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/2.5.0/guide/getting-started/ios/](https://cordova.apache.org/docs/en/2.5.0/guide/getting-started/ios/)  
28. Use xcode-select to Install Xcode Command Line Tools, 6月 18, 2025にアクセス、 [https://mac.install.guide/commandlinetools/4](https://mac.install.guide/commandlinetools/4)  
29. Xcode CLT Installation Guide \- CSCI 1230, 6月 18, 2025にアクセス、 [https://cs1230.graphics/website-fall-22/docs/xcode-CLT-installation-guide/](https://cs1230.graphics/website-fall-22/docs/xcode-CLT-installation-guide/)  
30. How can I install the Command Line Tools completely from the command line?, 6月 18, 2025にアクセス、 [https://apple.stackexchange.com/questions/107307/how-can-i-install-the-command-line-tools-completely-from-the-command-line](https://apple.stackexchange.com/questions/107307/how-can-i-install-the-command-line-tools-completely-from-the-command-line)  
31. Apache Cordova iOS \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/apache/cordova-ios](https://github.com/apache/cordova-ios)  
32. Upgrading Plugins to Cordova iOS 8.x | Documentation, 6月 18, 2025にアクセス、 [https://apache.github.io/cordova-ios/documentation/cordova/upgrading-8/?language=objc](https://apache.github.io/cordova-ios/documentation/cordova/upgrading-8/?language=objc)  
33. Cordovaアプリ開発の備忘録 \#JavaScript \- Qiita, 6月 18, 2025にアクセス、 [https://qiita.com/poruruba/items/f03b1691fd0f113735b3](https://qiita.com/poruruba/items/f03b1691fd0f113735b3)  
34. Prepare for Cordova (iOS and Android) Development on Mac, 6月 18, 2025にアクセス、 [https://developers.blackberry.com/us/en/resources/developer-summit/readiness/ios-cordova-dev-ios.html](https://developers.blackberry.com/us/en/resources/developer-summit/readiness/ios-cordova-dev-ios.html)  
35. MacでCordovaのインストール・実行・ビルドまで (iOS, Android, Web) \- 株式会社TKS2, 6月 18, 2025にアクセス、 [https://tks2.co.jp/2020/02/17/apache-cordova/](https://tks2.co.jp/2020/02/17/apache-cordova/)  
36. iOS App Development Using Cordova \- Adafruit, 6月 18, 2025にアクセス、 [https://cdn-learn.adafruit.com/downloads/pdf/ios-app-development-using-cordova.pdf](https://cdn-learn.adafruit.com/downloads/pdf/ios-app-development-using-cordova.pdf)  
37. cordova-plugin-cocoapod-support \- NPM, 6月 18, 2025にアクセス、 [https://www.npmjs.com/package/cordova-plugin-cocoapod-support](https://www.npmjs.com/package/cordova-plugin-cocoapod-support)  
38. blakgeek/cordova-plugin-cocoapods-support: A Cordova ... \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/blakgeek/cordova-plugin-cocoapods-support](https://github.com/blakgeek/cordova-plugin-cocoapods-support)  
39. Customization of Podfile generated by cordova-ios · Issue \#1512 \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/apache/cordova-ios/issues/1512](https://github.com/apache/cordova-ios/issues/1512)  
40. Generate Cordova build configuration | Bitrise Integration Steps, 6月 18, 2025にアクセス、 [https://bitrise.io/integrations/steps/generate-cordova-build-configuration](https://bitrise.io/integrations/steps/generate-cordova-build-configuration)  
41. How to automatically set the Signing Team on IOS cordova project? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/44367628/how-to-automatically-set-the-signing-team-on-ios-cordova-project](https://stackoverflow.com/questions/44367628/how-to-automatically-set-the-signing-team-on-ios-cordova-project)  
42. iOS Shell Tool Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/5.4.0/guide/platforms/ios/tools.html](https://cordova.apache.org/docs/en/5.4.0/guide/platforms/ios/tools.html)  
43. iOS Platform Guide \- Apache Cordova, 6月 18, 2025にアクセス、 [https://cordova.apache.org/docs/en/9.x/guide/platforms/ios/](https://cordova.apache.org/docs/en/9.x/guide/platforms/ios/)  
44. ionic cordova xcode 9 build development team and conflicting provisionning profiles, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/48748900/ionic-cordova-xcode-9-build-development-team-and-conflicting-provisionning-profi](https://stackoverflow.com/questions/48748900/ionic-cordova-xcode-9-build-development-team-and-conflicting-provisionning-profi)  
45. Phonegap IOS Signing with build.json \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/41248908/phonegap-ios-signing-with-build-json](https://stackoverflow.com/questions/41248908/phonegap-ios-signing-with-build-json)  
46. How can I find exactly what my codesign identity is? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/16576537/how-can-i-find-exactly-what-my-codesign-identity-is](https://stackoverflow.com/questions/16576537/how-can-i-find-exactly-what-my-codesign-identity-is)  
47. Code Signing Error \- Ionic Forum, 6月 18, 2025にアクセス、 [https://forum.ionicframework.com/t/code-signing-error/112564](https://forum.ionicframework.com/t/code-signing-error/112564)  
48. Cordova \- NSB App Studio, 6月 18, 2025にアクセス、 [https://wiki.appstudio.dev/Cordova](https://wiki.appstudio.dev/Cordova)  
49. build.json not working with 5.0.0 · Issue \#625 · apache/cordova-ios \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/apache/cordova-ios/issues/625](https://github.com/apache/cordova-ios/issues/625)  
50. Cordova iOS what is the value for provisioningProfile value for both debug and release, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/41547666/cordova-ios-what-is-the-value-for-provisioningprofile-value-for-both-debug-and-r](https://stackoverflow.com/questions/41547666/cordova-ios-what-is-the-value-for-provisioningprofile-value-for-both-debug-and-r)  
51. (ios) where to enable codeSignIdentity/developmentTeam, previously set in cordova build.json \- Capacitor \- Ionic Forum, 6月 18, 2025にアクセス、 [https://forum.ionicframework.com/t/ios-where-to-enable-codesignidentity-developmentteam-previously-set-in-cordova-build-json/230416](https://forum.ionicframework.com/t/ios-where-to-enable-codesignidentity-developmentteam-previously-set-in-cordova-build-json/230416)  
52. Best Practices for Version Control in Apache Cordova Apps \- Optimize Your Workflow, 6月 18, 2025にアクセス、 [https://moldstud.com/articles/p-best-practices-for-version-control-in-apache-cordova-apps-optimize-your-workflow](https://moldstud.com/articles/p-best-practices-for-version-control-in-apache-cordova-apps-optimize-your-workflow)  
53. git \- .gitignore for PhoneGap/Cordova 3.0 projects \- what should I commit? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/17911204/gitignore-for-phonegap-cordova-3-0-projects-what-should-i-commit](https://stackoverflow.com/questions/17911204/gitignore-for-phonegap-cordova-3-0-projects-what-should-i-commit)  
54. Exclude platforms folder in .gitignore \- Ionic Forum, 6月 18, 2025にアクセス、 [https://forum.ionicframework.com/t/exclude-platforms-folder-in-gitignore/102007](https://forum.ionicframework.com/t/exclude-platforms-folder-in-gitignore/102007)  
55. \[\!\] CocoaPods could not find compatible versions for pod \- DEV Community, 6月 18, 2025にアクセス、 [https://dev.to/matthewzruiz/-cocoapods-could-not-find-compatible-versions-for-pod-27g](https://dev.to/matthewzruiz/-cocoapods-could-not-find-compatible-versions-for-pod-27g)  
56. Maintaining plugins and packages \- best practice? \- Ionic Forum, 6月 18, 2025にアクセス、 [https://forum.ionicframework.com/t/maintaining-plugins-and-packages-best-practice/134789](https://forum.ionicframework.com/t/maintaining-plugins-and-packages-best-practice/134789)  
57. CocoaPods is conflicting \- VoltBuilder, 6月 18, 2025にアクセス、 [https://forum.volt.build/t/cocoapods-is-conflicting/1564](https://forum.volt.build/t/cocoapods-is-conflicting/1564)  
58. bug?: Cocoa Pods Conflict? · Issue \#373 · dpa99c/cordova-plugin-firebasex \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/dpa99c/cordova-plugin-firebasex/issues/373](https://github.com/dpa99c/cordova-plugin-firebasex/issues/373)  
59. CocoaPods is conflicting when installed cordova-plugin-consent · Issue \#624 \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/admob-plus/admob-plus/issues/624](https://github.com/admob-plus/admob-plus/issues/624)  
60. CocoaPods is conflicting \- \#7 by havenht \- VoltBuilder, 6月 18, 2025にアクセス、 [https://forum.volt.build/t/cocoapods-is-conflicting/1564/7](https://forum.volt.build/t/cocoapods-is-conflicting/1564/7)  
61. repeated issue with Cocoa Pods Conflict · Issue \#699 · dpa99c/cordova-plugin-firebasex, 6月 18, 2025にアクセス、 [https://github.com/dpa99c/cordova-plugin-firebasex/issues/699](https://github.com/dpa99c/cordova-plugin-firebasex/issues/699)