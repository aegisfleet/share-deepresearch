---
layout: topic
title: "AWS CodePipelineとCodeBuildにおける一般的な問題と高度なトラブルシューシューティングガイド"
date: 2025-06-02
prompt: "AWS CodePipelineとCodeBuildで発生する問題をまとめたい。エンジニアが良く陥るあるあるネタや、発生頻度は低いが解決に時間が掛かる問題などを集めて欲しい。"
category: "engineering"
tags: ["AWS","CI/CD","DevOps","自動化"]
audio: "/share-deepresearch/assets/audio/aws-codepipeline.mp3"
supplementary_materials:
  - title: "AWS CI/CDインフォグラフィック：CodePipeline & CodeBuild 問題解決ガイド"
    url: "/share-deepresearch/topics/aws-codepipeline/infographic.html"
---

# **AWS CodePipelineとCodeBuildにおける一般的な問題と高度なトラブルシューシューティングガイド**

## **1\. はじめに**

AWS CodePipelineおよびAWS CodeBuildは、AWS上でCI/CD（継続的インテグレーション/継続的デリバリー）ワークフローを構築するための基本的なコンポーネントです。これらのサービスは、ソフトウェアのリリースプロセスを自動化し、開発チームが迅速かつ確実にアプリケーションをデプロイできるよう支援します 1。

現代のソフトウェア開発において、信頼性が高く効率的なCI/CDパイプラインは不可欠です。これにより、開発速度の向上、品質の確保、そして開発者の生産性向上が期待できます 2。しかし、これらの強力なサービスを効果的に活用するには、その設定や運用における特有の課題を理解し、対処する能力が求められます。

本レポートは、エンジニアがAWS CodePipelineおよびCodeBuildを使用する際に直面する可能性のある、一般的な落とし穴（いわゆる「あるあるネタ」）から、発生頻度は低いものの解決に時間を要する複雑な問題までを網羅的に解説することを目的としています。具体的な診断ガイダンス、解決策、そして予防的なベストプラクティスを提供することで、エンジニアがこれらの課題に効果的に対処できるよう支援します。

本レポートは、これらのAWSサービスを利用している、または利用を検討しているエンジニアおよび技術リーダーを対象としています。AWSおよびCI/CDの基本的な概念についての知識があることを前提としています。

AWS CodePipelineとCodeBuildは非常に強力なサービスですが、その多機能性と柔軟性の裏返しとして、設定や運用の複雑さが存在します。公式ドキュメント 4、コミュニティフォーラム 6、技術ブログ 1 など、問題解決のための情報源が多岐にわたることは、これらのサービスを習熟する上での学習曲線と、潜在的な問題の多様性を示唆しています。エンジニアが直面する可能性のある問題を事前に把握し、体系的な知識を身につけることは、安定したCI/CD環境を構築・維持する上で極めて重要です。

## **2\. 一般的な落とし穴（「あるあるネタ」）**

このセクションでは、エンジニアが頻繁に遭遇する問題、特に単純な見落とし、デフォルト設定の誤解、または複数のサービス連携の複雑さに起因する一般的な課題について解説します。

### **2.1. 設定の罠：よくある原因**

多くの設定関連の問題は、開発者のローカル環境や前提と、CodeBuild/CodePipelineの実際の実行環境との間の差異から生じます。ファイルパス、利用可能なツール、環境変数、ネットワークアクセスなどの不一致が、「手元の環境では動作するのに」という典型的な状況を引き起こす主要な要因です。

* **buildspec.yml の設定ミス**  
  * **詳細:** buildspec.yml のエラーは、ビルド失敗の主要な原因の一つです。YAMLの構文エラー、コマンドシーケンスの間違い、ビルドフェーズ（install、pre\_build、build、post\_build）の誤解、buildspec 内での環境変数のスコープに関する問題などが含まれます 1。  
  * 典型的な落とし穴として、CodeBuildプロジェクト設定でのパス指定の誤りや、ソースアーティファクトのパッケージ化方法のエラー（例えば、予期しないディレクトリ構造でzip化されている）により、buildspec.yml が見つからないという問題があります 7。  
  * buildspec.yml で version: 0.2 を使用することは非常に重要です。これにより、コマンドが同じシェルインスタンスで実行され、フェーズ内のコマンド間で状態（あるコマンドで設定された環境変数を別のコマンドで使用するなど）が保持されるようになります。古いバージョンには、ユーザーを混乱させがちな制限がありました 9。  
  * **関連資料:** 1  
* **ソースステージのトリガー設定ミス**  
  * **詳細:** CodePipelineがソースの変更をどのように検出するかを誤って設定することは、頻繁に見られる「あるあるネタ」です。これには、監視対象の正しいブランチ（例：main 対 master 対フィーチャーブランチ）の指定ミスが含まれます 11。  
  * 一般的な問題点として、CodePipelineのソースアクション（特に CodeStarSourceConnection を使用する場合）が特定の BranchName を要求するデフォルトの動作があり、一時的なフィーチャーブランチやプルリクエストから直接CIをトリガーするにはカスタムの回避策が必要になる点が挙げられます 11。  
  * S3ソーストリガーの場合、S3バケットのCloudTrailデータイベントの有効化を忘れることは、パイプラインがトリガーされない原因となる簡単な見落としです 7。  
  * **関連資料:** 5  
* **環境変数エラー**  
  * **詳細:** 環境変数の設定や使用における間違いは一般的です。変数名の単純なタイプミス、不正な値（例：問題を引き起こす場所に / を含める 7）、CodePipelineとCodeBuild間、あるいはCodeBuildフェーズ内での変数の渡し方の問題などがあります 7。  
  * CodeBuildで環境変数として設定する際に、シークレット値（例：AWS\_ACCESS\_KEY\_ID、AWS\_SECRET\_ACCESS\_KEY）に末尾のスペースのような余分な文字を含めてしまうことは、デバッグが困難な認証失敗につながる、微妙ながらも重大なエラーです 12。  
  * **関連資料:** 7  
* **アーティファクト処理の問題**  
  * **詳細:** 入出力アーティファクトに関する問題は頻繁に発生します。これには、アーティファクト名の誤り（CodePipelineは名前を切り詰めるため、混乱を招くことがありますが、これは仕様です 5）、buildspec.yml の artifacts セクションにおける files のパス設定ミス、またはCodePipeline/CodeBuildロールがアーティファクトを読み書きするためのS3バケット権限の不足などが含まれます 1。  
  * CodeDeployToECS アクションのアーティファクトとしてタスク定義ファイルを含めるのを忘れたり、3MBのサイズ制限を超えたりすることは、特定の落とし穴です 5。  
  * **関連資料:** 1

### **2.2. IAMの迷路：権限関連の失敗**

最小権限の原則はセキュリティのベストプラクティスですが、複数のサービスや潜在的なクロスアカウントアクセスが絡む複雑なCI/CDワークフローにおいて、エンジニアがこれを正しく実装することはしばしば困難です。この結果、過度に制限的な権限が失敗を引き起こし、その迅速な修正として過度に広範な権限が付与され、セキュリティリスクが増大するという一般的なサイクルが生じがちです。

* **サービスロールの権限不足**  
  * **詳細:** 非常に一般的なエラーカテゴリです。CodePipelineおよびCodeBuildに関連付けられたIAMロールには、他のAWSサービス（例：アーティファクト用のS3、ソース用のCodeCommit/GitHub、イメージ用のECR、ロギング用のCloudWatch Logs、暗号化用のKMS、デプロイ用のECS/Elastic Beanstalk）と連携するために必要な権限が不足していることがよくあります 1。  
  * CodeBuildでの DOWNLOAD\_SOURCE\_FAILED エラーは典型的な例で、通常、ソースリポジトリ（例：CodeCommit、GitHub、BitBucket）へのアクセスに関するIAMロールの権限問題や、リポジトリ接続設定の誤りを指します 8。  
  * 特定の日付より前に作成されたCodePipelineロールは、新しい統合（例：Elastic Beanstalkの DescribeEvents やCodeCommitアクセス）に対する権限が不足している場合があります 5。  
  * ベストプラクティスではありませんが、権限問題を迅速に解決するためにCodeBuildロールに IAMFullAccess のような過度に広範な権限を付与することは一般的であり、これは権限を正しくスコープすることの難しさを示しています 13。  
  * **関連資料:** 1  
* **クロスアカウント権限の複雑さ**  
  * **詳細:** パイプラインが複数のAWSアカウント間で動作する場合（例：開発アカウントからソースを取得し、本番アカウントにデプロイする）、IAM設定は著しく複雑になります。これには、クロスアカウントロール、信頼ポリシーの設定、およびリソースポリシー（S3バケットポリシーやKMSキーポリシーなど）が別のアカウントのパイプライン実行ロールからのアクセスを許可することを確認することが含まれます 5。  
  * 特定の落とし穴として、AWSコンソールを介してCodePipelineのソースステージで別のアカウントのリポジトリやブランチを指定することは多くの場合不可能であり、CLIやIaCが必要となる点があります 15。  
  * KMSキーポリシーは、クロスアカウントシナリオでは特に厄介です。あるアカウントのデフォルトのAWSマネージドキーで暗号化されたアーティファクトは、別のアカウントのCodePipeline/CodeBuildでは復号できない可能性があり、適切なクロスアカウント権限を持つカスタマーマネージドキー（CMK）の使用が必要になります 14。  
  * **関連資料:** 5

### **2.3. ビルドステージの崩壊：コンパイルとテストが失敗する時**

CodeBuild環境の一時的かつコンテナ化された性質は、一貫性を提供する一方で、開発者がローカルでの開発やテスト時にその特性を完全に理解または再現しない場合、「あるある」問題の原因ともなり得ます。これは特に、依存関係、システムツール、Dockerイメージの相互作用に関して当てはまります。

* **COMMAND\_EXECUTION\_ERROR とスクリプトの失敗**  
  * **詳細:** この一般的なエラーは、buildspec.yml 内のコマンドが失敗したことを示します。原因は、コマンドのタイプミス、不正なパス、依存関係の欠落から、スクリプトが実行不可能であることやロジックエラーによる失敗まで多岐にわたります 8。  
  * デバッグには、多くの場合、ビルドログを綿密に調査して、失敗したコマンドとその出力を特定する必要があります 8。  
  * **関連資料:** 8  
* **依存関係解決の問題（「依存関係地獄」）**  
  * **詳細:** 特に複雑なプロジェクトでは、依存関係の管理が悪夢となることがあります。これには、競合する依存関係のバージョン、CodeBuild環境での依存関係の欠落、またはパッケージマネージャー（npm、pip、Maven、Gradleなど）の問題が含まれます 1。  
  * buildspec.yml の install フェーズは、依存関係を正しく設定するために不可欠です 1。  
  * 依存関係のキャッシュ（例：CodeBuildのローカルキャッシュやS3キャッシュの使用）はビルドを高速化できますが、キャッシュが古くなったり破損したりすると問題を引き起こす可能性もあります 2。  
  * **関連資料:** 1  
* **Dockerイメージの問題**  
  * **詳細:** CodeBuildでカスタムDockerイメージを使用する場合、またはCodeBuild内でDockerイメージをビルドする場合：  
    * **非互換性:** カスタムイメージに必要なツールやライブラリが不足していたり、CodeBuildの期待やアプリケーションのニーズと完全には互換性のないOSバージョンであったりする可能性があります 4。  
    * **アーキテクチャの不一致:** ローカル（例：M1/M2 Mac）でARMイメージをビルドし、CodeBuild経由でデプロイされたx86 Fargateタスクで実行しようとすると（またはその逆）、失敗を引き起こす可能性があります 7。  
    * **特権モード:** 一部のDocker操作（Docker-in-DockerやDockerレイヤーキャッシュなど）では、CodeBuildプロジェクトを特権モードで実行する必要があります 18。  
    * **ビルド時間:** CodeBuild内でDockerイメージをビルドすると時間がかかり、パイプライン全体の遅延の一因となることがあります 3。  
  * **関連資料:** 3  
* **CodeBuildのVPCネットワーキング問題**  
  * **詳細:** CodeBuildプロジェクトがVPC内で実行されるように設定されている場合（例：プライベートリソースへのアクセス）、依存関係のダウンロードやベースDockerイメージのプルに必要なインターネット接続の欠如といった一般的な問題が発生します。これは多くの場合、NATゲートウェイ、ルートテーブル、セキュリティグループ、またはネットワークACLの設定ミスに関連しています 22。  
  * CodeBuildのサービスロールにVPCとの連携に必要なEC2権限がない場合、Unexpected EC2 error: UnauthorizedOperation が発生することがあります 22。  
  * **関連資料:** 22

**表1：一般的なCodePipelineおよびCodeBuildのエラーシナリオと初期チェック**

| エラーメッセージ/症状 | 考えられる原因 | 主な調査領域 | 関連資料 |
| :---- | :---- | :---- | :---- |
| DOWNLOAD\_SOURCE\_FAILED | IAMロールの権限不足、ソースリポジトリへの接続設定ミス | サービスロールのポリシー、CodeStar接続ステータス、リポジトリの認証情報 | 8 |
| COMMAND\_EXECUTION\_ERROR | buildspec.yml の構文エラー、コマンド実行失敗、スクリプトエラー | buildspec.yml のコマンド、ビルドログの詳細 | 8 |
| ログ内の AccessDenied | IAMロールの権限不足（S3、KMS、ECRなどへのアクセス） | サービスロールのポリシー、リソースポリシー（S3バケットポリシー、KMSキーポリシー） | 5 |
| パイプラインがトリガーされない (S3ソース) | S3バケットのCloudTrailデータイベントが無効、EventBridgeルールの設定ミス | CloudTrailの設定、EventBridgeルールの設定とイベントパターン、IAM権限 | 7 |
| パイプラインがトリガーされない (CodeCommitソース) | CodeCommitのブランチ名指定ミス、EventBridgeルールの設定ミス、CodeStar接続の問題 | CodePipelineソースステージ設定、EventBridgeルールの設定、CodeStar接続ステータス | 11 |
| ビルドがハングする | VPCネットワーク設定ミス（インターネットアクセスなし）、リソース不足、長時間実行されるコマンド | CodeBuildプロジェクトのVPC設定（NATゲートウェイ、ルートテーブル、SG、NACL）、ビルドログ、リソース使用状況 | 22 |
| CodeDeployToECS アクションでのタスク定義ファイルエラー | タスク定義ファイルがアーティファクトに含まれていない、アーティファクトのZIPサイズが3MBを超過 | buildspec.yml の artifacts セクション、出力アーティファクトの内容とサイズ | 5 |
| 環境変数が正しく渡されない/機能しない | 環境変数のタイプミス、値のフォーマットエラー（例：末尾スペース、不正文字）、スコープの問題 | CodePipelineおよびCodeBuildの環境変数設定、buildspec.yml での参照方法、ビルドログでの環境変数確認 | 7 |
| クロスアカウントでのアーティファクトアクセス失敗 (KMS暗号化) | AWSマネージドKMSキーの使用、KMSキーポリシーの権限不足 | アーティファクトストアの暗号化設定、KMSキーポリシー、カスタマーマネージドキー（CMK）の使用検討 | 14 |
| ローカルとCodeBuild環境でのアーキテクチャ不一致によるECS起動失敗 | ローカルビルドイメージ（例：ARM）とFargateタスク（例：x86）のアーキテクチャのミスマッチ | CodeBuildの実行環境イメージのアーキテクチャ、ターゲットECSタスク定義のアーキテクチャ設定 | 7 |

この表は、エンジニアが最も頻繁に遭遇する問題の初期対応チェックリストとして機能し、迅速な原因特定と診断時間の節約に貢献します。

## **3\. 発生頻度は低いが解決困難な問題**

このセクションでは、日常的に発生するわけではないものの、発生した際には診断と解決に特に時間と深い理解を要する問題について掘り下げます。これらの問題は、サービス間の複雑な相互作用や、システムの潜在的な限界に関連していることが多いです。

### **3.1. 捉えどころのない断続的な失敗と競合状態**

断続的な失敗は、多くの場合、リソースの競合、API制限、または不適切なリトライロジックといった根本的なシステム的問題の兆候であり、単発のバグではありません。これらの問題を解決するには、即時の失敗だけでなく、より広範なシステムの動作と相互作用パターンを分析する必要があります。

* **不安定なビルド/一時的なエラーの特定とトラブルシューティング**  
  * **詳細:** 明確な設定変更がないにもかかわらず、散発的に失敗するビルドやパイプラインステージは、デバッグが非常に困難です。これらは、一時的なネットワーク問題、依存サービスの瞬間的な利用不能、APIスロットリング、あるいはスクリプトやインフラストラクチャ内の微妙な競合状態に起因する可能性があります 25。  
  * 例：CodeBuildで rake assets:precompile が断続的に失敗する 25。  
  * 例：AWS SAM CodeDeploy Lambdaデプロイメントが「InternalFailure」で断続的に失敗し、同時デプロイ中のLambda APIリクエスト制限超過に関連することがある 26。  
  * **トラブルシューティング:** 綿密なログ分析（CloudWatch、CodeBuildログ、CloudTrail）、より詳細なロギングの有効化、そしてエクスポネンシャルバックオフとジッターを伴う堅牢なリトライメカニズムの実装が必要になる場合があります 29。  
  * **関連資料:** 25  
* **潜在的な競合状態**  
  * **詳細:** 資料にはCodePipeline/CodeBuildの競合状態に関する具体的な例は詳述されていませんが、複数の同時ビルド/アクションが共有リソース（例：適切なロック/バージョニングなしの共有データベースやS3内のファイル）を変更しようとしたり、ビルドスクリプトに内部的な競合状態があったりする場合に発生する可能性があります。  
  * **トラブルシューティング:** これには多くの場合、ビルドスクリプトの慎重なコードレビュー、リソースアクセスパターンの理解、そして共有の可変状態が避けられない場合の特定の操作の直列化やロックメカニズムの実装が必要になります。

### **3.2. 複雑なロールバックシナリオ：元に戻す処理が失敗する時**

CodePipelineにおける効果的なロールバック戦略、特にCloudFormationを使用する場合、組み込みのロールバックメカニズムだけに頼るのではなく、最初から障害を想定した設計（冪等性、モジュール性、DependsOnによる依存関係の管理）に大きく依存します。組み込みメカニズムは、複雑なステートフルな変更に対して信頼性が低いか、不十分な場合があります。

* **CloudFormationロールバックの課題**  
  * **詳細:** CodePipelineはインフラデプロイにCloudFormationをよく使用します。CloudFormationのロールバックは複雑で、様々な理由で失敗する可能性があります。  
    * **スタックタイムアウト:** スタック操作（作成、更新、削除）に時間がかかりすぎ、タイムアウトが発生し、その後のロールバック試行自体も失敗することがあります 32。  
    * **リソース安定化の問題:** 更新中またはロールバック中にリソースが安定化しなかったり、成功シグナルを送信しなかったりする 33。  
    * **CloudFormation外部での変更:** CloudFormationで管理されているリソースがスタック外部で手動で変更された場合、実際の状態がテンプレートの期待と一致しないため、CloudFormationが正しくロールバックできないことがあります 33。  
    * **APIスロットリングエラー:** CloudFormationによる多数のリソースの同時デプロイはAPIスロットリングを引き起こし、失敗とロールバックの原因となることがあります 34。  
    * **ロールバックのための権限不足:** IAMロールには作成/更新の権限はあるものの、ロールバック中のリソース削除や適切な変更の権限がない場合があります 33。  
    * **カスタムリソースの失敗:** Lambdaバックのカスタムリソースが作成中または更新中に失敗すると、Lambdaが成功/失敗シグナルを正しく送信しなかったりタイムアウトしたりした場合、ロールバック失敗につながることがあります 33。  
  * **解決策:** 多くの場合、DependsOn 属性を使用してデプロイを直列化する 34、リソースを手動で同期する、またはロールバック中に問題のあるリソースをスキップする 33 といった手動介入が必要です。  
  * **関連資料:** 6  
* **特定のデプロイタイプに対する直接的なロールバックの欠如**  
  * **詳細:** 一部のユーザーは、CodePipelineがすべてのデプロイタイプ、特にCloudFormationに対して単純で直接的なロールバックメカニズムを提供していないことに不満を表明しています。緊急時には、パイプライン全体を通して「ロールバックコミット」をプッシュする必要があり、これが遅い場合があります 6。  
  * **関連資料:** 6

### **3.3. 大規模プロジェクトの課題：タイムアウト、同時実行性、パフォーマンスのナビゲート**

CI/CDの利用が拡大するにつれて（プロジェクト数の増加、コードベースの巨大化、ビルド頻度の増加）、問題は個々のビルドの正しさから、スループット、リソース競合（同時実行制限、APIスロットリング）、コスト管理といったシステム的な問題へと移行します。解決には、パイプライン設計とリソース最適化に対するよりアーキテクチャ的なアプローチが必要です。

* **ビルド時間の最適化**  
  * **詳細:** 広範なコードベースや複雑なビルド（例：大規模アプリケーションのコンパイル、長時間のE2Eテストの実行）の場合、ビルド時間が大きなボトルネックとなり、開発者の生産性やCI/CDサイクルタイムに影響を与える可能性があります 2。  
  * 戦略には、キャッシュ（依存関係、Dockerレイヤー）、ビルドおよびテストアクションの並列化、CodeBuildインスタンスタイプの最適化、そして潜在的には大規模ビルドをより小さな並列パイプラインに分割することが含まれます 2。  
  * **関連資料:** 2  
* **タイムアウトの管理（ビルド対キュー）**  
  * **詳細:** CodeBuildにはビルド実行タイムアウト（デフォルト1時間、最大36時間まで延長可能 36）とキュータイムアウト（デフォルト8時間 18）があります。この違いを理解することが不可欠です。  
  * **ビルドタイムアウト:** 単一のビルド実行が可能な最大時間。  
  * **キュータイムアウト:** 同時ビルド制限に達した場合にビルドが破棄されるまでにキューで待機できる最大時間。  
  * 同時実行制限によるキュータイムアウトが問題である場合、ビルドタイムアウトを延長しても解決しません 36。  
  * **関連資料:** 18  
* **同時ビルド制限とキューイングの処理**  
  * **詳細:** AWSアカウントおよびCodeBuildプロジェクトには、同時ビルド数に制限があります。これらの制限を超えると、ビルドはキューに入れられるか失敗します 18。  
  * キューに入れられたビルドの最大数は、通常、同時ビルド制限の5倍です 18。  
  * キューに入れられたビルドの実行順序は予測できません 18。  
  * これらの制限を効果的に管理するには、特に多くのプロジェクトを抱える大規模な組織では、慎重な計画、潜在的にはプロジェクトレベルの同時実行制限の使用、またはビルド期間を最適化してスロットをより迅速に解放する必要があります。  
  * **関連資料:** 18

### **3.4. 高度な統合と運用上の頭痛の種**

CodePipeline/CodeBuildの信頼性は、それらが統合する多数のAWS（およびサードパーティ）サービスの正しい設定と動作に深く関連しています。障害は多くの場合、CodePipeline/CodeBuild自体ではなく、それらが状態遷移を管理する方法や、これらの外部依存関係（IAM、S3、KMS、EventBridge、CloudFormation、ECS、Jenkinsなど）とどのように相互作用するかに起因します。

* **クロスアカウントアーティファクト暗号化におけるKMSキーの問題**  
  * **詳細:** CodePipelineアーティファクトがS3に保存され暗号化される際、AWSマネージドKMSキーを使用すると、クロスアカウントシナリオで復号失敗を引き起こす可能性があります。コンシューマーアカウントのCodeBuildロールが、ソースアカウントのデフォルトKMSキーを使用する権限を持っていない場合があるためです。  
  * **解決策:** 明示的にカスタマーマネージドKMSキー（CMK）を使用し、キーポリシーがアーティファクトにアクセスする必要のあるクロスアカウントIAMロールに必要な kms:Decrypt （およびその他の関連）権限を付与することを確認します 14。  
  * **関連資料:** 14  
* **EventBridge/CloudTrail統合の設定ミス**  
  * **詳細:** S3ソース変更またはEventBridgeを使用したCodeCommit変更によってトリガーされるパイプラインでは、設定ミスが一般的です。  
    * S3の場合、ソースバケットのCloudTrailデータイベントを有効にしないと、EventBridgeがイベントを受信できなくなります 7。  
    * 同じパイプラインを指す重複したEventBridgeルールがあると、単一のコミットが複数のパイプライン実行を引き起こし、ビルドフェーズがより早期の、より高速な実行からのデプロイフェーズに追い越されるといった予期しない動作を引き起こす可能性があります 23。これは、ルールが手動（またはCodePipelineによって自動的に）とIaCの両方で作成された場合に発生する可能性があります。  
    * IaC（例：Terraform）でEventBridgeルールを管理する場合、初期ルールがCodePipelineによって自動作成されたものであれば、Terraformでブランチを変更しても実際のEventBridgeルールが更新されず、パイプラインが新しいブランチに対してトリガーされなくなる可能性があります 24。  
  * **解決策:** S3に対してCloudTrailが正しく設定されていることを確認します。EventBridgeルールを慎重に管理し、できればIaCを介して行い、自動作成されたルールに注意します 5。  
  * **関連資料:** 5  
* **CloudFormationにおけるカスタムリソースのタイムアウト（CodePipelineによるオーケストレーション）**  
  * **詳細:** CodePipelineがLambdaバックのカスタムリソースを含むCloudFormationスタックをデプロイする場合、Lambda関数が実行に時間がかかりすぎる（Lambdaの最大15分）か、CloudFormationに成功/失敗シグナルを正しく送信しないと、これらのカスタムリソースがタイムアウトする可能性があります。これにより、CloudFormationスタックの更新が失敗し、潜在的にロールバックされます 33。  
  * デバッグにはLambda CloudWatchログの確認が必要です。ログがない場合（ロールバック時に削除された場合）、ロールバックを無効にして再デプロイします 35。  
  * Lambdaがシグナルを送信しない原因：cfn-response モジュールの不正な使用、コードエラー、Lambdaタイムアウト、VPCからのシグナル送信のためのS3エンドポイントアクセス欠如 35。  
  * **関連資料:** 33  
* **手動介入を必要とするパイプラインのスタック状態**  
  * **詳細:** パイプラインは様々なステージで「スタック」することがあります（例：応答のない手動承認ステップ、基盤となるリソースの問題によるデプロイアクションのハング、または「進行中」でスタックしたCodeDeploy ECSデプロイメント）5。  
  * Jenkins統合の場合、Jenkinsアクションがハングすると、Jenkinsサーバー/EC2インスタンスの認証情報/権限の問題が原因である可能性があります 5。  
  * CodeDeployを使用しないECSデプロイメントは、新しいタスクが安定化に失敗すると「進行中」でスタックすることがあります。解決策には、新しい動作するタスク定義をデプロイするか、以前のバージョンに戻すことが含まれます 41。  
  * Step FunctionsがFargateタスクを呼び出す場合：Step Functionがタイムアウトすると、Fargateタスクが自動的に強制終了されず、「ゾンビコンテナ」が発生する可能性があります。解決策には、タイムアウトをキャッチし、Lambdaを介してFargateタスクを明示的に停止することが含まれます 43。  
  * **関連資料:** 5

**表2：発生頻度は低いが複雑な問題のトラブルシューティングガイド**

| 問題カテゴリ | 一般的な症状 | 高度な診断ステップ | 潜在的な解決策/回避策 | 関連資料 |
| :---- | :---- | :---- | :---- | :---- |
| 断続的なビルド失敗 | 不安定なテスト結果、時折発生するCOMMAND\_EXECUTION\_ERROR | 詳細ログの有効化、CloudTrailでのAPI呼び出しパターンの分析、リソース競合の調査、Session Managerでのビルドコンテナ調査 | ジッター付きエクスポネンシャルバックオフによるリトライ実装、テスト環境の安定化、リソース制限の確認 | 25 |
| CloudFormationロールバックループ | UPDATE\_ROLLBACK\_FAILED状態、スタックが長時間ロールバック試行を繰り返す | CloudFormationイベントの詳細確認、関連リソース（カスタムリソースLambdaログなど）のログ調査、手動変更の有無確認 | CloudFormationテンプレートでのDependsOn属性の使用、手動でのリソース同期、ロールバック時の問題リソースのスキップ、APIスロットリング対策 | 33 |
| クロスアカウントKMS復号エラー | 別アカウントのS3アーティファクトへのアクセス時にAccessDenied | KMSキーポリシーとグラントの確認、CloudTrailでのKMS API呼び出しエラーの特定 | カスタマーマネージドキー（CMK）の作成とクロスアカウント権限付与、アーティファクトストアでの正しいKMSキー指定 | 14 |
| パイプラインが承認/デプロイでスタック | パイプラインが長時間In Progress状態、手動承認通知が来ない、デプロイが進まない | CodePipeline実行履歴の詳細確認、関連サービス（SNS、ECS、CodeDeployなど）のログとステータス確認 | 手動でのスタックアクションの停止/再試行、通知設定の確認、基盤リソースの問題解決（例：ECSタスクのヘルスチェック失敗） | 6 |
| EventBridgeトリガーが発火しない | CodeCommitへのプッシュやS3へのオブジェクト配置でパイプラインが開始されない | EventBridgeルールの設定（イベントパターン、ターゲット）確認、CloudTrailでのイベント配信状況の確認、IAM権限確認 | EventBridgeルールのIaCによる管理、CloudTrailデータイベントの有効化（S3ソースの場合）、重複ルールの削除 | 7 |
| CodeDeploy ECSデプロイのハング | ECSデプロイメントが長時間「In progress」、新しいタスクが起動しない、またはヘルスチェックに失敗する | CodeDeployデプロイメントログ、ECSサービスイベント、タスクのCloudWatchログ、ALBターゲットグループのヘルスチェックステータス確認 | 新しい正常なタスク定義での再デプロイ、以前の正常なバージョンへのロールバック、ECSサーキットブレーカーやCloudWatchアラームの設定見直し | 41 |
| Step Functions連携Fargateタスクのゾンビ化 | Step FunctionsがタイムアウトしてもFargateタスクが停止しない | Step Functionsの実行履歴、Fargateタスクのステータス、CloudWatchログ | Step FunctionsのCatchブロックでタイムアウトを捕捉し、Lambda関数で対象Fargateタスクを明示的に停止する | 43 |

この表は、一般的ではないものの非常に混乱を招く可能性のある問題の診断をエンジニアに案内します。これらの「ブラックボックス」的な状況に対して構造化されたアプローチを提供します。

## **4\. 高度なトラブルシューティングとデバッグ戦略**

このセクションでは、エンジニアが問題をより効果的に診断し解決するために使用できる実践的なテクニックとツールに焦点を当てます。CodePipeline/CodeBuildにおけるトラブルシューティングと最適化は、障害発生後の単なるログの精査から、ローカルテスト/デバッグ、クラウドでのインタラクティブセッション、詳細なパフォーマンス分析といった、より積極的で開発者中心のアプローチへと移行しています。

### **4.1. ログの効果的な活用：基本的なチェックを超えて**

* **CloudWatch Logsの詳細分析**  
  * **詳細:** 単に「エラー」メッセージを探すだけでなく、さらに踏み込むことを強調します。CodePipeline、CodeBuild、Lambda、CloudFormation、ECSなど、異なるサービス間でログを関連付ける方法を説明します。  
  * ビルドログやパイプライン実行ログの強力なクエリと分析のために、CloudWatch Logs Insightsを使用します 2。  
  * CodeBuildログ（フェーズ遷移、コマンド出力）とCodePipeline実行履歴の構造を理解します 1。  
  * **関連資料:** 1  
* **API監査のためのCloudTrail**  
  * **詳細:** CodePipelineおよびCodeBuildサービスロールによって行われたAPI呼び出しを追跡するために、CloudTrailログを使用します。これは、どのAPI呼び出しが失敗し、なぜ失敗したのかを正確に把握することで、権限問題（AccessDeniedエラー）をデバッグするのに非常に役立ちます。  
  * イベント駆動トリガーの問題（例：S3イベントがEventBridgeに到達しているか、EventBridgeがCodePipelineを呼び出しているか）を理解するのにも役立ちます 7。  
  * **関連資料:** 7

### **4.2. インタラクティブデバッグ：実践的なアプローチ**

* **ライブデバッグのためのAWS Systems Manager Session Manager**  
  * **詳細:** CodeBuildとSession Managerの統合により、エンジニアは実行中のビルドコンテナに直接接続できます。これは、複雑なビルドスクリプトの問題、環境問題、または依存関係の競合をリアルタイムでデバッグするための画期的な機能です 19。  
  * 有効化方法：「高度なビルドの上書き」で「セッション接続の有効化」をチェックします。  
  * 使用方法：buildspec.yml に codebuild-breakpoint を挿入してビルドを一時停止し、CodeBuildコンソールのリンク経由で接続します。続行するには codebuild-resume を使用します 44。  
  * **注意:** CodeBuildはビルド環境が実行されている時間（一時停止時間を含む）に対して課金されるため、請求に注意してください 44。  
  * **関連資料:** 19  
* **事前チェックのためのローカルCodeBuildエージェント**  
  * **詳細:** CodeBuildエージェントを使用すると、CodeBuild環境をシミュレートするDockerコンテナでビルドをローカル実行できます。これは以下に優れています：  
    * コミット前に buildspec.yml の構文とコマンドを検証する。  
    * 各イテレーションでAWSコストを発生させることなくビルドスクリプトをデバッグする。  
    * ビルド変更テストのための不要なコミットを削減する 45。  
  * **セットアップ:** ローカルにDockerとGitが必要です。CodeBuildエージェントイメージと目的のビルドイメージをプルします 45。  
  * **関連資料:** 45  
* **CodeBuild Sandbox（新機能）**  
  * **詳細:** CodeBuild Sandboxは、AWS Management ConsoleまたはAWS CLIを介して直接、安全で隔離された環境でのインタラクティブなデバッグセッションを提供します。コマンドを実行し、ビルドプロセスを段階的に検証できます 19。  
  * **注意:** Sandboxの使用には料金が発生します 19。  
  * **関連資料:** 19

### **4.3. ビルドパフォーマンスの最適化とボトルネックの特定**

* **キャッシュ戦略**  
  * **詳細:** 効果的なキャッシュはビルド時間短縮に不可欠です。CodeBuildは以下をサポートします：  
    * **ローカルキャッシュ:** ソース（Gitメタデータ）、Dockerレイヤー（特権モードが必要、Linuxのみ）、カスタムパス（例：node\_modules、\~/.m2のような依存関係）2。  
    * **S3キャッシュ:** より大きなキャッシュの保存やビルドプロジェクト間でのキャッシュ共有（ただし、典型的な依存関係キャッシュにはあまり一般的ではありません）2。  
  * **落とし穴:** キャッシュの無効化/一貫性が問題になることがあります。古いキャッシュは予期しないビルド動作や失敗につながる可能性があります。  
  * **関連資料:** 2  
* **並列化テクニック**  
  * **詳細:**  
    * **CodePipelineステージ:** 同じCodePipelineステージ内で独立したアクションを並列実行するには、それらの RunOrder を同じ値に設定します 2。  
    * **CodeBuildバッチビルド:** 依存ビルドには build-graph を、単一のCodeBuildプロジェクト実行内での同時独立ビルドには build-list または build-matrix を使用します 18。  
    * **CodeBuild並列テスト:** CodeBuildは、テストシャーディングとレポート集約のために codebuild-tests-run CLIを使用して、バッチビルド内の複数の環境にテストを分散できます 18。  
  * **利点:** パイプライン全体の実行時間を短縮します。  
  * **関連資料:** 2  
* **CodeBuild設定の最適化**  
  * **詳細:**  
    * **インスタンスタイプ:** ビルドワークロードを適切なCPUとメモリを持つインスタンスタイプ（例：コンピューティング最適化C5/M5、コスト/パフォーマンスのためのGraviton2）に合わせます 2。  
    * **コンピューティングモード:** EC2またはLambdaコンピューティングを選択します（Lambdaは起動が速く、短いビルドではコストが低い可能性があります）2。  
    * **カスタムDockerイメージ:** 依存関係をカスタムDockerイメージにプリインストールして、install フェーズを高速化します 2。  
  * **関連資料:** 2  
* **ボトルネックの特定**  
  * **詳細:** パイプライン実行履歴（ステージ期間、待機時間）、CodeBuildログ（フェーズ期間）、CloudWatchメトリクスを分析します 2。  
  * CodeGuru Profilerのようなツールは、CodeBuildプロジェクト内のコードレベルのパフォーマンス問題を特定するのに役立ちます 2。  
  * 遅いビルドの一般的な原因：大規模なコードベース、非効率なビルドスクリプト、リソース不足 2。  
  * **関連資料:** 2

**表3：デバッグテクニックとツールマトリックス**

| テクニック/ツール | 主なユースケース | 主な利点 | セットアップ/使用ポインタ | 関連資料 |
| :---- | :---- | :---- | :---- | :---- |
| CloudWatch Logs Insights | 大量のログ分析、複雑なクエリ実行 | 強力なクエリ言語、迅速なログ調査 | クエリ構文の学習、ロググループの選択 | 2 |
| CloudTrail分析 | IAM/APIエラーの追跡、イベントトリガーのデバッグ | API呼び出しの監査証跡、権限問題の根本原因特定 | イベント名/ロールでフィルタリング、エラーコード確認 | 7 |
| Session Managerデバッグ | インタラクティブなスクリプトデバッグ、環境問題のリアルタイム調査 | リアルタイムフィードバック、コンテナ内での直接コマンド実行 | セッション接続の有効化、codebuild-breakpoint の使用 | 19 |
| ローカルCodeBuildエージェント | コミット前のbuildspec検証、ローカルでのビルドスクリプトデバッグ | コスト削減、迅速なイテレーション、不要なコミット削減 | Dockerセットアップ、エージェントスクリプトの実行 | 45 |
| CodeBuild Sandbox | インタラクティブな環境検証、分離された安全なデバッグ | コンソール/CLIからの直接アクセス、段階的なプロセス検証 | AWSコンソールからのアクセス、価格確認 | 19 |
| キャッシュ分析 | ビルド時間短縮のためのキャッシュ効果測定、キャッシュ問題の特定 | ビルド時間の大幅短縮の可能性 | プロジェクト設定でのキャッシュモード設定、キャッシュヒット率の確認 | 2 |
| ビルド並列化レビュー | パイプラインレイテンシ削減、スループット向上 | エンドツーエンドのデリバリ時間短縮 | CodePipelineステージでのRunOrder設定、CodeBuildバッチビルドの活用 | 2 |
| CodeGuru Profiler | コードレベルのボトルネック特定、パフォーマンス最適化 | アプリケーションコード内の非効率な部分の特定 | CodeBuildプロジェクトとの統合、プロファイリング結果の分析 | 2 |

この表は、エンジニアが利用可能なデバッグおよび最適化ツール/テクニックの概要を迅速に比較検討するのに役立ち、特定の問​​題や目標に最も適したものを選択するのに役立ちます。

## **5\. レジリエントで効率的なCI/CDパイプライン構築のためのベストプラクティス**

このセクションでは、調査から得られたベストプラクティスを統合し、問題を予防し、堅牢で保守可能かつ安全なパイプラインを構築するための積極的な対策に焦点を当てます。「解決困難な問題」や一般的な落とし穴の多くは、最初から積極的な設計原則を採用することで軽減または完全に回避できます。これには、冪等性のための設計、IaCの厳格な使用、堅牢なリトライとエラー処理の実装、設定の保護、スケーラビリティと保守性の計画が含まれます。

### **5.1. 堅牢なエラー処理とリトライメカニズム**

* **一時的なエラーに対するリトライロジックの実装**  
  * **詳細:** 一時的な障害（ネットワークの不具合、スロットリング）が発生する可能性のあるAWSサービスやその他の外部依存関係との対話には、リトライロジックを実装します。  
  * **ベストプラクティス:** エクスポネンシャルバックオフとジッターを使用します。これにより、サンダリングハード問題を防ぎ、サービスが回復する時間を確保できます 29。  
  * AWS SDK（CodeBuildスクリプトやCodePipelineのLambda関数で使用）には、多くの場合、設定可能なリトライメカニズム（Boto3のレガシー、標準、アダプティブモードなど）が組み込まれています 29。  
  * CodePipeline自体にもアクションに対するいくつかのリトライ機能があります 5。  
  * より複雑なシナリオでは、Step Functionsを使用して、高度なバックオフとジッターロジック（例：cdk-stepfunctions-patterns の RetryWithJitterTask）でリトライをオーケストレーションできます 31。  
  * **関連資料:** 5  
* **冪等性のための設計**  
  * **詳細:** パイプラインステージとビルドステップが冪等であることを確認します。つまり、同じ入力で複数回実行しても、意図しない副作用なしに同じ結果を生成できるようにします。これは、安全なリトライと障害からの回復に不可欠です 10。  
  * **テクニック:** 操作に一意の識別子を使用し、条件付き更新を行い、アトミックな操作を設計します。CloudFormationは大部分が設計上冪等です 30。  
  * CodeBuild buildspec.yml バージョン0.2は、コマンドを同じシェルで実行することで、ビルド内の冪等性のための状態管理を容易にします 9。  
  * **関連資料:** 9

### **5.2. CI/CDにおけるセキュリティベストプラクティス**

* **シークレットの安全な管理**  
  * **詳細:** APIキー、パスワード、トークンなどのシークレットを buildspec.yml やパイプライン定義にハードコードしないでください。  
  * **ベストプラクティス:** AWS Secrets ManagerまたはAWS Systems Manager Parameter Store（SecureStringタイプ）を使用してシークレットを保存し、CodeBuildプロジェクト設定または buildspec.yml （env/parameter-store または env/secrets-manager セクションを使用）で安全に参照します 9。  
  * CodeBuildのIAMロールがこれらのシークレットを取得するために必要な最小限の権限を持っていることを確認します。  
  * **関連資料:** 9  
* **脆弱性スキャンの統合**  
  * **詳細:** CI/CDパイプラインに自動セキュリティスキャンを統合して、脆弱性を早期に検出します。  
  * **ツール:** ソースコードの依存関係（例：Snyk 52 やOWASP Dependency-Checkを使用）、コンテナイメージ（例：Trivy、Amazon ECRスキャン、Clair）、Infrastructure as Codeテンプレートをスキャンします。  
  * これらのスキャンをCodePipeline/CodeBuildのビルドまたはテストステップとして組み込みます。  
  * **関連資料:** 52  
* **プライベート依存関係管理のためのAWS CodeArtifactの使用**  
  * **詳細:** プライベートパッケージを管理したり、パブリックパッケージリポジトリへのアクセスを制御したりする必要がある組織向けに、AWS CodeArtifactは安全で管理されたアーティファクトリポジトリを提供します。  
  * CodeBuildをCodeArtifactと統合して、パッケージを安全に取得および公開します。これには、CodeArtifactで認証するように buildspec.yml を設定することが含まれます 53。  
  * **利点:** 一元管理、パブリックリポジトリへの直接依存を減らすことによるセキュリティ向上、監査。  
  * **関連資料:** 53  
* **IAMロールに対する最小権限の原則**  
  * **詳細:** CodePipelineおよびCodeBuildで使用されるすべてのIAMロールに、最小権限の原則を一貫して適用します。IAMFullAccess 13 のような過度に広範な権限を避けます。  
  * パイプライン要件の変更に応じて、権限を定期的に確認し、調整します。  
  * **関連資料:** 1

### **5.3. 保守性と効率性のためのパイプライン設計と管理**

* **ベストプラクティスとしてのイベント駆動トリガー**  
  * **詳細:** パイプラインを開始するために、ポーリングよりもイベント駆動トリガー（例：CodeCommit、S3、ECRとのEventBridge統合）を優先します。これは、より効率的で応答性が高く、コスト効率に優れています 5。  
  * AWSの試験やベストプラクティスでは、イベント駆動アーキテクチャが強調されています 37。  
  * **関連資料:** 5  
* **パイプラインのためのInfrastructure as Code (IaC)**  
  * **詳細:** AWS CloudFormationやAWS CDKのようなIaCツールを使用して、CodePipelineおよびCodeBuildリソースを定義および管理します 6。  
  * **利点:** バージョン管理、再現性、プロビジョニングと更新の自動化、災害復旧、およびより良い変更管理。  
  * これにより、手動のコンソール変更で発生する可能性のある設定のドリフトを回避できます 23。  
  * **関連資料:** 6  
* **モジュラーパイプライン設計**  
  * **詳細:** 複雑なリリースプロセスを、より小さく、管理しやすく、潜在的に再利用可能なパイプラインステージ、あるいは相互に接続された個別のパイプラインに分割します。  
  * 適切な場合は「1つのAWS CodePipelineに1つのAWS CodeDeploy」の原則に従います。同じアプリケーションコンポーネントに対して複数のパイプラインを使用するのではなく、その構造内で並列デプロイのためにCodeDeployデプロイメントグループを使用します 37。  
  * 明確さのために、ビルド、テスト、デプロイの懸念事項を個別のステージに分離することを検討します。  
  * **関連資料:** 37  
* **効果的な通知戦略**  
  * **詳細:** 主要なパイプラインイベント（開始、成功、失敗、手動承認が必要）に対する通知を実装して、関係者に情報を提供し、問題への迅速な対応を可能にします。  
  * Amazon SNSと統合して、メール、SMS、またはチャット通知（例：Slack、Chime）を行います 37。  
  * エンジニアが常にコンソールを監視することに依存しないようにします 37。  
  * **関連資料:** 37  
* **AWS Well-Architected Frameworkの遵守**  
  * **詳細:** AWS Well-Architected Framework（オペレーショナルエクセレンス、セキュリティ、信頼性、パフォーマンス効率、コスト最適化）の原則をCI/CDインフラストラクチャに適用します 50。  
  * これらの柱に対してパイプラインアーキテクチャを定期的にレビューします。  
  * **関連資料:** 50  
* **ビルド環境と再現性の管理**  
  * **詳細:** CodeBuildにバージョン管理されたカスタムDockerイメージを使用して、一貫性のある再現可能なビルド環境を確保します。これらのイメージにツールや依存関係をプリインストールすることで、ビルドも高速化できます 2。  
  * セキュリティのためにカスタムイメージを定期的に更新し、パッチを適用します 21。  
  * **関連資料:** 2

## **6\. まとめ**

AWS CodePipelineとCodeBuildは、強力なCI/CDパイプラインを構築するための基盤ですが、その設定や運用には様々な課題が伴います。本レポートでは、設定ミス、権限問題、ビルドやデプロイの失敗、さらには断続的なエラーや大規模プロジェクト特有の複雑な運用上の問題など、エンジニアが直面しうる多岐にわたる課題を解説しました。

これらの問題の多くは、ローカル環境とクラウド環境の差異、IAMの複雑さ、ビルド環境の特性の誤解、そして多数の連携サービスとの相互作用に起因します。トラブルシューティングは不可欠ですが、最終的な目標は、設計、セキュリティ、運用のベストプラクティスを適用することにより、回復力があり効率的なパイプラインを構築することです。具体的には、冪等性の確保、IaCの徹底、堅牢なエラー処理とリトライ戦略の導入、セキュアな設定管理、そしてスケーラビリティと保守性を見据えた計画が重要となります。

CI/CDは反復的なプロセスであり、パイプラインは継続的に監視、改良、改善されるべきです。AWSのサービスは絶えず進化しているため、エンジニアは新しい機能やベストプラクティスを常に把握し続けることが求められます。本レポートで提供された知識が、エンジニアの皆様がより良く、より信頼性の高いCI/CDワークフローをAWS上で構築するための一助となることを願っています。

#### **引用文献**

1. Troubleshooting Common AWS CodePipeline Failures Reintech media, 6月 2, 2025にアクセス、 [https://reintech.io/blog/troubleshooting-common-aws-codepipeline-failures](https://reintech.io/blog/troubleshooting-common-aws-codepipeline-failures)  
2. Optimize Your AWS CodePipeline Build Speed, 6月 2, 2025にアクセス、 [https://cloud.folio3.com/blog/optimizing-aws-codepipeline-workflows/](https://cloud.folio3.com/blog/optimizing-aws-codepipeline-workflows/)  
3. AWS CodeBuild と Docker Build Cloud を使用して Docker ビルドを高速化, 6月 2, 2025にアクセス、 [https://www.docker.com/ja-jp/blog/accelerate-your-docker-builds-using-aws-codebuild-and-docker-build-cloud/](https://www.docker.com/ja-jp/blog/accelerate-your-docker-builds-using-aws-codebuild-and-docker-build-cloud/)  
4. トラブルシューティング AWS CodeBuild, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/ja\_jp/codebuild/latest/userguide/troubleshooting.html](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/troubleshooting.html)  
5. Troubleshooting CodePipeline \- AWS CodePipeline, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/codepipeline/latest/userguide/troubleshooting.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/troubleshooting.html)  
6. what has been your experience using codebuild, codepipeline and ..., 6月 2, 2025にアクセス、 [https://www.reddit.com/r/aws/comments/wivg4p/what\_has\_been\_your\_experience\_using\_codebuild/](https://www.reddit.com/r/aws/comments/wivg4p/what_has_been_your_experience_using_codebuild/)  
7. 【Tips寄り】S3に配置したJavaのソースコードをCodePipelineで ..., 6月 2, 2025にアクセス、 [https://dev.classmethod.jp/articles/tips-s3-java-codepipeline-ecs/](https://dev.classmethod.jp/articles/tips-s3-java-codepipeline-ecs/)  
8. AWS CodeBuildの完全ガイド：失敗しない導入と運用のための7つの ..., 6月 2, 2025にアクセス、 [https://dexall.co.jp/articles/?p=2244](https://dexall.co.jp/articles/?p=2244)  
9. Build specification reference for CodeBuild \- AWS CodeBuild, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html)  
10. CodeBuild のビルド仕様に関するリファレンス \- AWS Documentation, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/ja\_jp/codebuild/latest/userguide/build-spec-ref.html](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/build-spec-ref.html)  
11. CodePipeline のトリガーで不便なポイントは？｜CTC Build ... \- note, 6月 2, 2025にアクセス、 [https://note.com/build\_service/n/n470bd565e918](https://note.com/build_service/n/n470bd565e918)  
12. CodeBuildが正常に動くまでにしたことリスト \#AWS \- Qiita, 6月 2, 2025にアクセス、 [https://qiita.com/matsuda-hiroki/items/39188d52a002b5461d6f](https://qiita.com/matsuda-hiroki/items/39188d52a002b5461d6f)  
13. 【AWS】CFn用CI/CD環境の作り方(単一リポジトリに複数ファイルが存在する場合) \- Qiita, 6月 2, 2025にアクセス、 [https://qiita.com/kaburagi\_/items/28fcc41160d4aa4ecfd6](https://qiita.com/kaburagi_/items/28fcc41160d4aa4ecfd6)  
14. CodePipeline を使用してクロスアカウントで CodeCommit から S3 ..., 6月 2, 2025にアクセス、 [https://zenn.dev/mn87/articles/f772875c974a2d](https://zenn.dev/mn87/articles/f772875c974a2d)  
15. AWS CodePipelineをクロスアカウントで作成する際の権限図 \- Zenn, 6月 2, 2025にアクセス、 [https://zenn.dev/takamin55/articles/66ea83a47f7c08](https://zenn.dev/takamin55/articles/66ea83a47f7c08)  
16. An Overview and Catalogue of Dependency Challenges in Open Source Software Package Registries \- arXiv, 6月 2, 2025にアクセス、 [https://arxiv.org/html/2409.18884v3](https://arxiv.org/html/2409.18884v3)  
17. Classification of Detected Dependency Issues Download Scientific Diagram \- ResearchGate, 6月 2, 2025にアクセス、 [https://www.researchgate.net/figure/Classification-of-Detected-Dependency-Issues\_tbl1\_343048136](https://www.researchgate.net/figure/Classification-of-Detected-Dependency-Issues_tbl1_343048136)  
18. でのビルド AWS CodeBuild \- AWS CodeBuild \- AWS Documentation, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/ja\_jp/codebuild/latest/userguide/builds-working.html](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/builds-working.html)  
19. Debug builds in AWS CodeBuild, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/debug-builds.html](https://docs.aws.amazon.com/codebuild/latest/userguide/debug-builds.html)  
20. CodeBuild に用意されている Docker イメージ \- AWS Documentation, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/ja\_jp/codebuild/latest/userguide/build-env-ref-available.html](https://docs.aws.amazon.com/ja_jp/codebuild/latest/userguide/build-env-ref-available.html)  
21. 1月 1, 1970にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/custom-images.html](https://docs.aws.amazon.com/codebuild/latest/userguide/custom-images.html)  
22. Troubleshoot your VPC setup \- AWS CodeBuild, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting-vpc.html](https://docs.aws.amazon.com/codebuild/latest/userguide/troubleshooting-vpc.html)  
23. CodePipelineの同じパイプラインを呼び出すEventBridgeのルールが ..., 6月 2, 2025にアクセス、 [https://dev.classmethod.jp/articles/duplicate-rules-for-eventbridge-that-invoke-codepipeline/](https://dev.classmethod.jp/articles/duplicate-rules-for-eventbridge-that-invoke-codepipeline/)  
24. \[CodePipeline\] 検出オプションをEventBridgeにした時の注意点 iret ..., 6月 2, 2025にアクセス、 [https://iret.media/88518](https://iret.media/88518)  
25. Unanswered 'aws-codebuild' Questions \- Page 5 \- Stack Overflow, 6月 2, 2025にアクセス、 [https://stackoverflow.com/questions/tagged/aws-codebuild?tab=unanswered\&page=5](https://stackoverflow.com/questions/tagged/aws-codebuild?tab=unanswered&page=5)  
26. AWS SAM CodeDeploy Lambda deployment failure ... \- AWS re:Post, 6月 2, 2025にアクセス、 [https://repost.aws/questions/QUcI10rP\_xSvqNY\_0bBhwQyw/aws-sam-codedeploy-lambda-deployment-failure-codedeployservicerole-awslambda-request-limit-exceeded](https://repost.aws/questions/QUcI10rP_xSvqNY_0bBhwQyw/aws-sam-codedeploy-lambda-deployment-failure-codedeployservicerole-awslambda-request-limit-exceeded)  
27. amazon web services \- Implementing multiple builds with AWS ..., 6月 2, 2025にアクセス、 [https://stackoverflow.com/questions/65159839/implementing-multiple-builds-with-aws-codebuild-with-dependant-artifacts](https://stackoverflow.com/questions/65159839/implementing-multiple-builds-with-aws-codebuild-with-dependant-artifacts)  
28. landing-zone-accelerator-on-aws/CHANGELOG.md at release/v1 ..., 6月 2, 2025にアクセス、 [https://github.com/awslabs/landing-zone-accelerator-on-aws/blob/release/v1.12.0/CHANGELOG.md](https://github.com/awslabs/landing-zone-accelerator-on-aws/blob/release/v1.12.0/CHANGELOG.md)  
29. Retries \- Boto3 1.38.26 documentation \- AWS, 6月 2, 2025にアクセス、 [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/retries.html)  
30. Exponential Backoff And Jitter AWS Architecture Blog, 6月 2, 2025にアクセス、 [https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/)  
31. cdk-stepfunctions-patterns Yarn, 6月 2, 2025にアクセス、 [https://classic.yarnpkg.com/en/package/cdk-stepfunctions-patterns](https://classic.yarnpkg.com/en/package/cdk-stepfunctions-patterns)  
32. CloudFormationの全てを味わいつくせ！「AWSの全てをコードで ..., 6月 2, 2025にアクセス、 [https://dev.classmethod.jp/articles/aws-all-iac/](https://dev.classmethod.jp/articles/aws-all-iac/)  
33. Troubleshooting CloudFormation \- AWS CloudFormation, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html)  
34. AWSのCodeシリーズの運用で躓いたお話 コラム クラウド ..., 6月 2, 2025にアクセス、 [https://business.ntt-east.co.jp/content/cloudsolution/ih\_column-153.html](https://business.ntt-east.co.jp/content/cloudsolution/ih_column-153.html)  
35. How do I troubleshoot custom resource failures in ... \- AWS re:Post, 6月 2, 2025にアクセス、 [https://repost.aws/knowledge-center/cfn-troubleshoot-custom-resource-failures](https://repost.aws/knowledge-center/cfn-troubleshoot-custom-resource-failures)  
36. \[アップデート\] AWS CodeBuild プロジェクトの最大タイムアウトが ..., 6月 2, 2025にアクセス、 [https://dev.classmethod.jp/articles/codebuild-timeout-36/](https://dev.classmethod.jp/articles/codebuild-timeout-36/)  
37. AWS CodePipelineの超詳細解説 \#AWS認定試験 \- Qiita, 6月 2, 2025にアクセス、 [https://qiita.com/tech4anyone/items/6353b5ca379b18301b4f](https://qiita.com/tech4anyone/items/6353b5ca379b18301b4f)  
38. jeroendesloovere/amazon-web-services-guide \- GitHub, 6月 2, 2025にアクセス、 [https://github.com/jeroendesloovere/amazon-web-services-guide](https://github.com/jeroendesloovere/amazon-web-services-guide)  
39. Public Cloud Records \- Exploratory, 6月 2, 2025にアクセス、 [https://ja.exploratory.io/viz/PQd2wHB2BZ/Public-Cloud-Records-viy6NIA6GV](https://ja.exploratory.io/viz/PQd2wHB2BZ/Public-Cloud-Records-viy6NIA6GV)  
40. AWS Blu Age Devops Pipeline : Failed AWS re:Post, 6月 2, 2025にアクセス、 [https://repost.aws/questions/QU8tZLkvjnQwG7cvSSeo2UCA/aws-blu-age-devops-pipeline-failed](https://repost.aws/questions/QU8tZLkvjnQwG7cvSSeo2UCA/aws-blu-age-devops-pipeline-failed)  
41. How do I stop an ECS deployment that does not use CodeDeploy ..., 6月 2, 2025にアクセス、 [https://repost.aws/questions/QUpswRAHByToG\_Fq-Xj8kEDQ/how-do-i-stop-an-ecs-deployment-that-does-not-use-codedeploy-the-ecs-deployment-is-stuck-in-in-progress](https://repost.aws/questions/QUpswRAHByToG_Fq-Xj8kEDQ/how-do-i-stop-an-ecs-deployment-that-does-not-use-codedeploy-the-ecs-deployment-is-stuck-in-in-progress)  
42. Elastic Beanstalk Blue Green Deployment Without Approval Step \- Stack Overflow, 6月 2, 2025にアクセス、 [https://stackoverflow.com/questions/52879812/elastic-beanstalk-blue-green-deployment-without-approval-step](https://stackoverflow.com/questions/52879812/elastic-beanstalk-blue-green-deployment-without-approval-step)  
43. amazon web services \- AWS Steps Function: timed out Fargate task ..., 6月 2, 2025にアクセス、 [https://stackoverflow.com/questions/73734329/aws-steps-function-timed-out-fargate-task-not-automatically-killed](https://stackoverflow.com/questions/73734329/aws-steps-function-timed-out-fargate-task-not-automatically-killed)  
44. \[アップデート\] デバッグ作業が捗る！AWS CodeBuild で一時停止 ..., 6月 2, 2025にアクセス、 [https://dev.classmethod.jp/articles/codebuild-supports-accessing-build-environments-with-aws-session-manager/](https://dev.classmethod.jp/articles/codebuild-supports-accessing-build-environments-with-aws-session-manager/)  
45. ローカル環境でCodeBuildを爆速実行！テスト・デバッグも楽々！, 6月 2, 2025にアクセス、 [https://zenn.dev/secondselection/articles/codebuild\_agent](https://zenn.dev/secondselection/articles/codebuild_agent)  
46. 1月 1, 1970にアクセス、 [https://docs.aws.amazon.com/codebuild/latest/userguide/caching.html](https://docs.aws.amazon.com/codebuild/latest/userguide/caching.html)  
47. Infrastructure as Code (IaC) vs. Traditional Infrastructure Management \- AutoMQ, 6月 2, 2025にアクセス、 [https://www.automq.com/blog/infrastructure-as-code-iac-vs-traditional-infrastructure-management](https://www.automq.com/blog/infrastructure-as-code-iac-vs-traditional-infrastructure-management)  
48. Pipeline Comparison: How to Compare and Contrast Different Pipeline Development Approaches and Tools \- FasterCapital, 6月 2, 2025にアクセス、 [https://fastercapital.com/content/Pipeline-Comparison--How-to-Compare-and-Contrast-Different-Pipeline-Development-Approaches-and-Tools.html](https://fastercapital.com/content/Pipeline-Comparison--How-to-Compare-and-Contrast-Different-Pipeline-Development-Approaches-and-Tools.html)  
49. AWS Certified Developer \- Associate (DVA-C02) Exam Book, 6月 2, 2025にアクセス、 [https://interview.quicktechie.com/books/book/53?chapterId=7\&sessionId=2](https://interview.quicktechie.com/books/book/53?chapterId=7&sessionId=2)  
50. AWS Certified Solutions Architect – Associate (SAA-C02) 2020 ..., 6月 2, 2025にアクセス、 [https://www.examcollection.com/blog/aws-certified-solutions-architect-associate-saa-c02-2020-exam-study-guide-and-updated-preparation-materials/](https://www.examcollection.com/blog/aws-certified-solutions-architect-associate-saa-c02-2020-exam-study-guide-and-updated-preparation-materials/)  
51. AWS DevOps & Developer Productivity Blog \- Amazon.com, 6月 2, 2025にアクセス、 [https://aws.amazon.com/blogs/devops/](https://aws.amazon.com/blogs/devops/)  
52. 1月 1, 1970にアクセス、 [https://aws.amazon.com/blogs/devops/integrating-snyk-into-an-aws-codepipeline-to-secure-your-application-delivery/](https://aws.amazon.com/blogs/devops/integrating-snyk-into-an-aws-codepipeline-to-secure-your-application-delivery/)  
53. 1月 1, 1970にアクセス、 [https://aws.amazon.com/blogs/devops/using-aws-codeartifact-with-aws-codebuild-to-securely-store-and-share-packages/](https://aws.amazon.com/blogs/devops/using-aws-codeartifact-with-aws-codebuild-to-securely-store-and-share-packages/)  
54. AWS CodePipeline および AWS CodeBuild を使用して、スタックセットデプロイを自動化 \- Amazon.com, 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/ja\_jp/prescriptive-guidance/latest/patterns/automate-stack-set-deployment-by-using-aws-codepipeline-and-aws-codebuild.html](https://docs.aws.amazon.com/ja_jp/prescriptive-guidance/latest/patterns/automate-stack-set-deployment-by-using-aws-codepipeline-and-aws-codebuild.html)  
55. 【AWS CodePipeline】GitHubソースのVersion 1→ 2移行は大事故が起こる可能性があるため注意 \- Zenn, 6月 2, 2025にアクセス、 [https://zenn.dev/bm\_sms/articles/b80b6670c04263](https://zenn.dev/bm_sms/articles/b80b6670c04263)  
56. Add a manual approval action to a pipeline in CodePipeline \- AWS ..., 6月 2, 2025にアクセス、 [https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-action-add.html](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals-action-add.html)  
57. Amazon Aurora Noise Page 3, 6月 2, 2025にアクセス、 [https://noise.getoto.net/tag/amazon-aurora/page/3/](https://noise.getoto.net/tag/amazon-aurora/page/3/)  
58. AWS Cloud Operations Blog, 6月 2, 2025にアクセス、 [https://aws.amazon.com/blogs/mt/](https://aws.amazon.com/blogs/mt/)  
