---
layout: topic
title: "n8nとAWSを活用したSlackリアクションからのGitHub Issue自動作成ガイド"
date: 2025-06-03
prompt: "n8nを使ってSlackとGitHubの連携を行いたい。特にSlackのリアク字に反応してIssueを作成したいので、その方法をまとめて欲しい。AWSでホストする前提となる。"
category: "engineering"
tags: [n8n,CI/CD,GitHub]
audio: "/share-deepresearch/assets/audio/connect-n8n-to-slack.mp3"
supplementary_materials:
  - title: "ワークフロー自動化市場の動向とインサイト 2025"
    url: "/share-deepresearch/topics/connect-n8n-to-slack/infographic.html"
  - title: "環境構成図：Slack・AWS(n8n)・GitHub連携"
    url: "/share-deepresearch/topics/connect-n8n-to-slack/diagram.html"
---

# **n8nとAWSを活用したSlackリアクションからのGitHub Issue自動作成ガイド**

## **1\. はじめに**

### **目的**

本レポートの目的は、AWS上にセルフホストされたn8nを利用し、特定のSlackメッセージリアクションに応じてGitHubのIssueを自動的に作成する、堅牢な自動化パイプラインを構築することです。この自動化は、共同作業環境から直接バグ報告、タスク作成、またはフィードバック収集を効率化するという一般的なニーズに対応します。

### **ソリューション概要**

このソリューションは、AWS上にホストされたn8nインスタンス、Slackのreaction\_addedイベントをリッスンする設定済みのSlackアプリケーション、Issue作成のためのGitHub連携、そしてこれらの要素を連携させるn8nワークフローから構成されます。この自動化により、手作業の削減、効率の向上、そしてSlackでの議論から発生する実行可能なアイテムの追跡改善といった利点が得られます。

## **2\. Part 1: AWSでのn8n環境準備**

### **AWSホスティング戦略の選択**

AWSでn8nをセルフホストする際の主要な選択肢はいくつか存在します。それぞれの方法は、スケーラビリティ、管理オーバーヘッド、初期設定の複雑さにおいて異なる特性を持ちます。

* **EC2への直接インストール**: n8nとその依存関係（Node.js、npmなど）をEC2インスタンスに直接インストールする方法です 1。コンテナ化に不慣れなユーザーにとっては最もシンプルですが、依存関係の管理やスケーリングが難しくなる可能性があります。  
* **EC2上のDocker**: EC2インスタンス上でn8nをDockerコンテナとして実行する方法です 1。環境の分離性、更新の容易さ、移植性に優れています。本ガイドでは、管理性と制御のバランスが良いこのアプローチを推奨します。  
* **AWS ECS (FargateまたはEC2)**: Amazon Elastic Container Serviceを使用して、n8nをコンテナ化されたサービスとしてデプロイする方法です 3。Fargateはサーバーレスなコンテナ実行を提供し、インフラ管理を削減します。一方、ECS on EC2は基盤となるインスタンスに対するより詳細な制御を可能にします。これはより複雑ですが、本番ワークロードに対して高いスケーラビリティと耐障害性を提供します。

ホスティング方法の選択は、将来のメンテナンスやスケーリング戦略に直接影響します。例えば、小規模チームはEC2上のDockerから始めるかもしれませんが、大企業はECSを選択する可能性があります。

また、n8nをスケーリングする場合、特に複数のインスタンス（例：ECSでdesired\_count \> 1など）を実行する際には、Webhookの登録と配信が正しく処理されないと問題が発生する可能性があります 5。SlackトリガーはWebhookに依存するため、最初はシンプルな単一インスタンス構成（EC2上のDockerやWebhookを処理する単一タスクのECSなど）の方が信頼性が高い場合があります。あるいは、スケーリングされたセットアップでは、ロードバランサーの適切な設定（スティッキーセッション 7）やn8nのキューモードが必要になります。

**表1: n8nのためのAWSホスティング方法比較**

| ホスティング方法 | 設定の容易さ | スケーラビリティ | 管理オーバーヘッド | コスト影響 | 最適なユースケース |
| :---- | :---- | :---- | :---- | :---- | :---- |
| EC2直接インストール | 高い | 低い | 中程度 | EC2インスタンス費用 | 小規模、テスト、コンテナ未経験者 |
| EC2上のDocker | 中程度 | 中程度 | 中程度 | EC2インスタンス費用 | 中規模、開発・本番環境、移植性重視 |
| ECS Fargate | 低い | 高い | 低い | Fargate費用（vCPU、メモリ）、データ転送費用など | 大規模、スケーラビリティ重視、サーバーレス志向 |

### **推奨アプローチ: AWS EC2インスタンスでのDockerによるn8nデプロイ**

#### **EC2インスタンスのセットアップ**

EC2インスタンスの起動手順は以下の通りです 1。

1. **AMIの選択**: Ubuntu Server 22.04 LTSやAmazon Linux 2などのAMIを選択します。  
2. **インスタンスタイプの選択**: パフォーマンスとコストのバランスが良いt3.medium 1、または基本的なワークロード向けのt2.micro 1 などを選択します。  
3. **セキュリティグループの設定**: n8nのデフォルトポートである5678番ポートへのインバウンドトラフィックを許可します。アクセス元は、管理アクセス用の自分のIPアドレスや、ALBなしでWebhookを直接使用する場合はSlackのIPレンジなどに制限することが重要です。また、SSH用に22番ポートも許可します 1。単にポート5678を0.0.0.0/0に開放するのはセキュリティリスクがあるため、アクセス元を既知のIPに制限するか、ALBとWAFを使用することが推奨されます。

#### **Dockerのインストールとn8nコンテナのデプロイ**

EC2インスタンスにDockerおよびDocker Composeをインストールするためのコマンドを実行します 1。  
公式n8n Dockerイメージを実行します。データ永続化のための-vフラグの重要性を強調します。  
例: docker run \-it \--rm \--name n8n \-p 5678:5678 \-v \~/.n8n:/home/node/.n8n n8nio/n8n 1

#### **データ永続性の確保**

/home/node/.n8nディレクトリの永続化は非常に重要です。ここにはワークフローデータ、暗号化された認証情報、そしてユニークな暗号化キーが保存されます 2。Dockerの-vフラグを使用して、ホストディレクトリ（例：ホスト上の/opt/n8n\_dataや\~/.n8n）をコンテナ内の/home/node/.n8nにマウントします 1。  
代替手段として、ホストボリュームの永続化を異なる方法で管理する場合、環境変数N8N\_ENCRYPTION\_KEYを提供する方法もありますが、一般的には直接的なボリュームマウントが推奨されます 2。EFSとECSのようなより複雑なストレージソリューションを選択する場合や、特定のバックアップ・リストア戦略がある場合、N8N\_ENCRYPTION\_KEYを（おそらくAWS Secrets Managerに保存して）明示的に管理することが、認証情報リカバリのために重要になります。

#### **パブリックアクセス設定（Webhook用）**

* **Elastic IPアドレス**: EC2インスタンスにElastic IPを割り当て、静的なパブリックIPを確保します 1。SlackのRequest URLがEC2インスタンスを直接指す場合に不可欠です。  
* **(推奨) Application Load Balancer (ALB)**: n8nインスタンスの前面にALBを設置します。これにより、HTTPS終端、カスタムドメイン名、そして将来的なスケーリングやインスタンス交換が容易になります 1。  
* **AWS Certificate Manager (ACM)によるHTTPS化**: ALBとACMを統合し、安全なWebhook通信のための無料SSL/TLS証明書を提供します 1。SlackはRequest URLにHTTPSを要求することを説明します。

### **(任意だが推奨) AWS Secrets Managerによる認証情報の保護**

AWS Secrets Managerは、n8n自体の設定やワークフロー内で使用するAPIトークンなどの機密データを保存するための優れたサービスです 10。

#### **n8nのためのIAM権限**

EC2インスタンス（またはECSタスクロール）がAWS Secrets Managerからシークレットにアクセスするために必要なIAMロールとポリシーを詳述します。これには通常、secretsmanager:GetSecretValueのような権限が含まれます 12。IAMポリシーの例を示します 12。  
n8nはデフォルトで認証情報を暗号化しますが、AWS Secrets Managerを使用することで、一元管理、ローテーション、IAMベースのアクセス制御が可能になり、特にAWSエコシステム内で運用するユーザーにとってはAWSのベストプラクティスに沿った形となります。

#### **n8nでの外部シークレットの使用設定**

n8nが実行時にAWS Secrets Managerから認証情報を取得するように設定する方法を説明します（環境変数またはUI経由）12。  
{{ $secrets.awsSecretsManager.\<secret-name\> }}のような式を使用して、n8nの認証情報フィールドでこれらのシークレットを参照する方法を示します 12。  
関連するAWSサービスとして、SSM Parameter Storeも設定/シークレット管理のための選択肢として存在します。n8nが公式にサポートを追加した場合、一部のユーザーにとっては費用対効果の高い選択となる可能性があります 11。

## **3\. Part 2: n8n連携のためのSlack設定**

### **Slackアプリの作成**

api.slack.com/appsにアクセスし、「From scratch」で新しいアプリを作成します 14。アプリ名とワークスペースを選択します。

### **認証: Bot User OAuth Tokenの生成**

Slackアプリ設定の「OAuth & Permissions」に移動します 14。Slack TriggerノードはAPIアクセストークン（Bot User OAuth Token、xoxb-で始まる）を必要とします 14。OAuth2は通常、Slackの*アクション*ノード用であり、トリガー用ではありません 14。アプリをワークスペースにインストールした後、「Bot User OAuth Token」をコピーします 14。

### **必須スコープ (Bot Token Scopes)**

適切なスコープの設定は、ワークフローが期待通りに機能するために不可欠です。

* reactions:read: reaction\_addedイベントを受信するために絶対的に必要です 16。  
* channels:history: リアクションが追加された元のメッセージのコンテンツを取得する必要がある場合に必須です 16。トリガーペイロードには完全なメッセージテキストが含まれていない可能性があるためです。このスコープの必要性は、GitHub Issueを元のメッセージ内容で充実させたいという二次的な要件から生じます。  
* groups:history, im:history, mpim:history: グループDM、DM、または複数人DMでリアクションが発生し、メッセージ内容の取得が必要な場合に潜在的に必要です。  
* users:read または users.profile:read: ユーザー情報（リアクションした人の名前など）をID以外で解決する必要がある場合や、n8nによる認証情報検証のために必要になることがあります 20。  
* chat:write: ワークフローがSlackにメッセージを投稿する場合（例：Issue作成の確認）に必要です 16。  
* Slack Triggerノードのドキュメント 18 には、UIピッカーや内部検証のために、conversations.listとusers.listが最低限の要件として記載されています。  
* 包括的なリストについては、18 や 15 からリンクされている「Scopes | Slack credentials」のページを参照してください。

**表2: Slackアプリ設定概要**

| 設定項目 | 設定値/スコープ | 目的 | 参照 |
| :---- | :---- | :---- | :---- |
| アプリ作成 | api.slack.com/appsにて「From scratch」 | n8n連携用Slackアプリの作成 | 14 |
| Bot Token | 「OAuth & Permissions」で生成されるxoxb-で始まるトークン | n8n Slack Triggerノードの認証用 | 14 |
| スコープ (Bot) | reactions:read, channels:history, users:read (推奨), chat:write (任意) | イベント受信、メッセージ取得、ユーザー情報取得、メッセージ送信のための権限付与 | 16 |
| イベントサブスクリプション | reaction\_added (Bot Event) | 指定リアクションイベントの購読 | 14 |

### **イベントサブスクリプション**

Slackアプリ設定の「Event Subscriptions」に移動します 14。  
「Enable Events」をオンにします 14。

* **Request URL**:  
  * n8nのSlack TriggerノードからWebhook URL（Production URL）をコピーし、Slackアプリの「Request URL」フィールドに貼り付けます 14。SlackはこのURLにチャレンジリクエストを送信し、n8nは検証のためにこれを正しく処理する必要があります。この検証プロセスとn8nのテスト/本番URLの区別は、失敗の多いポイントであるため、慎重なガイドが必要です。  
  * n8nのテストURLと本番URLの違い、そしてSlackアプリごとに許可されるRequest URLは1つだけであることを説明します 14。テストURLでテストする場合、ワークフローをアクティブ化する際に本番URLに更新する必要があります。一部のコミュニティ投稿 22 では、n8nワークフローをアクティブ化した後にSlackのURLを更新し忘れ、トリガーが発火しない問題が報告されています。  
* **ボットイベントの購読**:  
  * 「Subscribe to bot events」でreaction\_addedイベントを選択します 14。これにより、ボットが存在する、またはアクセス権を持つメッセージへのユーザーによるリアクションをアプリがリッスンするようになります。

### **n8nでのSlack認証情報の設定**

n8nで「Credentials」に移動し、新しいSlack認証情報を追加します。  
「API Access Token」方式を使用します 14。  
Slackアプリ設定から取得した「Bot User OAuth Token」（xoxb-で始まる）をn8nの「Access Token」フィールドに貼り付けます 14。

### **代替案: Slack Socket Modeの使用（概要）**

パブリックなWebhook URLを公開できない環境（ローカル開発、制限されたネットワークなど）の代替案としてSlack Socket Modeに言及します 16。  
@mbakgun/n8n-nodes-slack-socket-modeのようなコミュニティノードが必要です 16。  
これには異なるSlackアプリ設定が必要です（Socket Modeの有効化、App-Level Token（xapp-）の生成、異なるスコープ/イベント購読方法）16。これは高度な代替案であり、本ガイドの主要な焦点ではありませんが、完全性のために言及する価値があります。

## **4\. Part 3: n8n連携のためのGitHub設定**

### **GitHub Personal Access Token (Classic)の生成**

GitHubプロファイルの Settings \> Developer settings \> Personal access tokens \> Tokens (classic) にユーザーを誘導します 23。  
n8nは、ベータ版でありエンドポイントの制限がある可能性があるため、fine-grained PATよりも「personal access token (classic)」を推奨していることを強調します 23。  
手順: Generate new token (classic)を選択し、説明的なノート（例: "n8n-slack-integration"）を追加し、有効期限を設定します（セキュリティプラクティスとして有効期限設定を推奨 24）。

### **repoスコープの割り当て**

repoスコープを選択します。このスコープはプライベートリポジトリの完全な制御を許可し、通常、Issueの作成やコンテンツの読み取りなどに必要です 23。スコープなしのトークンはパブリック情報にしかアクセスできないことを説明します。repoスコープは強力であるため、このトークンがリポジトリへの広範なアクセス権を持つことをユーザーは認識すべきです。生成されたトークンは再度表示されないため、すぐにコピーします。

**表3: GitHub PAT設定概要**

| 設定項目 | 設定値 | 目的 | 参照 |
| :---- | :---- | :---- | :---- |
| トークンタイプ | Personal Access Token (Classic) | n8nからのGitHub API認証用 | 23 |
| ノート | 例: "n8n-slack-integration" | トークンの識別 | 23 |
| 有効期限 | 推奨: 設定する (例: 90日) | セキュリティ向上のため | 24 |
| スコープ | repo | Issue作成を含むリポジトリ操作のための権限付与 | 23 |
| n8n認証情報設定 | GitHubユーザー名と生成されたアクセストークン | n8nワークフローからGitHub APIを利用可能にする | 23 |

### **n8nでのGitHub認証情報の設定**

n8nで「Credentials」に移動し、新しいGitHub認証情報を追加します。  
認証方法は「API Access Token」になります 23。  
GitHubユーザー名を入力し、生成されたPersonal Access Tokenを「Access Token」フィールドに貼り付けます 23。  
GitHub Enterprise Serverを使用していない限り、「GitHub Server URL」はデフォルトのままにします 23。  
n8nの汎用認証（Bearer認証、ヘッダー認証）がヘッダーを正しく送信しなかったり、値がリセットされたりする潜在的な問題 25 がありますが、GitHubノードは事前定義された認証情報タイプを使用するため、専用のGitHub認証情報タイプとPAT 23 を使用することが最も信頼性の高い方法です。

## **5\. Part 4: n8nワークフローの構築: SlackリアクションからGitHub Issueへ**

### **ワークフロー設計概要**

ノードフローの概念図: Slack Trigger \-\> (任意 IF) \-\> (任意 Slack Nodeでメッセージコンテキスト取得) \-\> GitHub Node。  
データフローの説明: リアクションイベントがワークフローをトリガーし、データは任意でフィルタリングおよびエンリッチされ、GitHub Issueの作成に使用されます。

### **Node 1: Slack Trigger**

* **イベント**: イベントリストからReaction Addedを選択します 18。  
* **認証**: Part 2で設定したSlack認証情報を選択します。  
* **パラメータ** 18:  
  * Watch Whole Workspace: デフォルトはオフ。オンにした場合の影響を説明します（ボットがいる*すべて*のチャンネルのイベントごとに1実行を使用するため注意が必要）。このユースケースでは通常オフにし、特定のチャンネルのみが関連する場合はChannel to Watchを指定します。ただし、ボットが認識する場所であればどこでもリアクションを拾う一般的な設定では、これを広範にトリガーさせ、後でフィルタリングすることもあります。  
  * Channel to Watch: ワークスペース全体を監視しない場合にチャンネルを指定します。  
  * Usernames or IDs to ignore: ボットが自身の行動や他のボットに反応するのを防ぐのに役立ちます 18。27では、無視リストがボットIDに対して機能しない場合のバグ/回避策としてフィルターノードが必要になる可能性が示唆されています。  
* **出力: reaction\_addedイベントペイロードの理解** 17:  
  * ペイロードからの主要フィールド:  
    * event.type: "reaction\_added"  
    * event.user: リアクションを追加した人のユーザーID。  
    * event.reaction: 絵文字の名前（例: "bug", "task"）。Slack APIペイロードの絵文字名は通常コロンなしのショートコード（例: "thumbsup" であり ":thumbsup:" ではない）であるため、IFノードでの正確なフィルタリングにはこの詳細が重要です。  
    * event.item.type: 通常は "message"。  
    * event.item.channel: メッセージが存在するチャンネルID。  
    * event.item.ts: リアクションされたメッセージのタイムスタンプ。これは元のメッセージを取得するために不可欠です。  
    * event.item\_user: 元のメッセージを投稿した人のユーザーID。  
  * このペイロードは後続ノードの主要なデータソースとなります。reaction\_addedペイロードにはリアクションとリアクションされたアイテムに関するメタデータが含まれますが、元のメッセージの*内容*は含まれません。これが、GitHub Issueにメッセージテキストが必要な場合にオプションの「メッセージ内容の取得」ステップを必要とする直接的な理由です。  
* **表4: n8n Slack Triggerノード設定**

| パラメータ | 値/設定 | 説明 |
| :---- | :---- | :---- |
| 認証情報 | 作成済みのSlack認証情報 | Slack APIへのアクセスに使用 |
| イベント | Reaction Added | このイベント発生時にワークフローをトリガー |
| Watch Whole Workspace | 推奨: オフ (ユースケースによる) | オンにすると全チャンネルの全リアクションでトリガーされるため注意が必要 |
| Channel to Watch | (Watch Whole Workspaceがオフの場合) 特定のチャンネルID | リアクションを監視するチャンネルを指定 |
| Usernames or IDs to ignore | (任意) ボットのユーザーIDなど | 特定ユーザーからのイベントを無視 |

### **(任意) Node 2: IF Node (リアクションのフィルタリング)**

* 目的: 特定の事前定義された絵文字リアクション（例: :bug:, :ticket:, :task:）に対してのみGitHub Issueが作成されるようにします。これによりノイズを防ぎ、意図を明確にします。  
* 設定:  
  * 入力: Slack Triggerノードからのデータ。  
  * 条件: {{ $json.event.reaction }}を目的の絵文字名のリストと比較します。  
  * 例: {{ $json.event.reaction \=== "bug" | | $json.event.reaction \=== "task\_to\_do" }} (実際の絵文字名は異なる場合があり、SlackはAPIイベントでコロンなしのショートコードを使用します。例: "bug", "task\_to\_do")。

### **(任意) Node 3: Slack Node (メッセージ内容の取得)**

* 目的: リアクションを受け取った元のSlackメッセージの内容を取得します。トリガーペイロード自体には含まれていないためです。  
* **認証**: 同じSlack認証情報を選択します。  
* **リソース & オペレーション**: Channel \-\> History 19。これはSlack APIメソッドconversations.history 28 にマッピングされます。  
* **パラメータ** 19:  
  * Channel ID: Slack Triggerの出力からマッピング: {{ $json.event.item.channel }}。  
  * Latest: Slack Triggerの出力からマッピング: {{ $json.event.item.ts }}。これは取得するメッセージのタイムスタンプです。  
  * Oldest: Slack Triggerの出力からマッピング: {{ $json.event.item.ts }}。(単一メッセージを取得するため、latestとoldestは同じです)。  
  * Inclusive: trueに設定します（指定されたtsのメッセージを含めるため）。  
  * Limit: 1に設定します（その単一メッセージのみを取得するため）。  
  * Return All: limitを使用する場合はオフにする必要があります。  
  * conversations.historyをメッセージのtsに設定したlatest、oldest、inclusive: true、limit: 1と共に使用することは、特定のメッセージの内容を取得する標準的な方法です 19。  
* 出力: ノードはメッセージオブジェクトを含む配列を出力します。メッセージテキストは通常messages.textにあります。その他の有用なフィールドにはmessages.user（元の投稿者）、messages.permalinkがあります。  
* conversations.historyはTier 3メソッド（50+/分）ですが、非Marketplaceアプリの場合、Tier 1（1+/分）に変更され、リクエストあたり15オブジェクトの制限があります 29。単一メッセージの取得（limit=1）は問題ありませんが、頻繁なトリガーはこの低いレート制限に達する可能性があります。

### **Node 4: GitHub Node**

* **認証**: Part 3で設定したGitHub認証情報を選択します。  
* **リソース & オペレーション**: Issue \-\> Create 31。  
* **パラメータ** (31でオペレーション、32でRedmineからのフィールド例、Issueフィールドに関する一般的なGitHub API知識を参照):  
  * Owner/Organization: リポジトリが存在するGitHubユーザー名または組織名。(例: {{ $env.GITHUB\_REPO\_OWNER }} またはハードコード)。  
  * Repository Name: リポジトリの名前。(例: {{ $env.GITHUB\_REPO\_NAME }} またはハードコード)。  
  * Title: 意味のあるタイトルを作成します。  
    * 例: Slack Reaction: {{ $json.event.reaction }} on message by {{ $node.json.event.item\_user }}  
    * または、メッセージ内容が取得された場合: Bug: {{ $node.json.messages.text.substring(0, 50\) }}...  
  * Body: Issueの主要な内容。以下を含めます:  
    * 元のSlackメッセージ内容（取得された場合）: {{ $node.json.messages.text }}。  
    * Slackメッセージへのパーマリンク: {{ $node.json.messages.permalink }} (取得された場合。それ以外の場合はteam\_id, channel\_id, message\_tsを使用して構築)。  
    * リアクションしたユーザー: User {{ $json.event.user }} reacted with :{{ $json.event.reaction }}:  
    * リアクションのタイムスタンプ。  
    * GitHub Issueの品質は、Slackからのデータがタイトルと本文にどのようにマッピングされ、フォーマットされるかに大きく依存します。パーマリンク、ユーザーID、元のメッセージの断片を含めるための式を使用することが、Issueを実行可能にする鍵です。  
  * Labels (任意): ラベルのコンマ区切り文字列 (例: "bug", "slack-reported", {{ $json.event.reaction }}など)。  
  * Assignees (任意): GitHubユーザー名のコンマ区切り文字列。  
* **表5: n8n GitHubノード (Issue作成) 設定**

| パラメータ | 値/式 | 説明 |
| :---- | :---- | :---- |
| 認証情報 | 作成済みのGitHub認証情報 | GitHub APIへのアクセスに使用 |
| Owner/Organization | (必須) リポジトリ所有者のユーザー名または組織名 | Issueを作成するリポジトリの所有者を指定 |
| Repository | (必須) リポジトリ名 | Issueを作成するリポジトリを指定 |
| Title | (必須) 例: Slackリアクション: {{ $json.event.reaction }} | GitHub Issueのタイトル。Slackイベントデータから動的に生成可能 |
| Body | (任意) 例: Slackメッセージへのリンク: {{ $node.json.messages.permalink }}\\n\\n内容:\\n{{ $node.json.messages.text }} | GitHub Issueの本文。メッセージ内容やパーマリンクを含めることを推奨 |
| Labels | (任意) 例: bug,from-slack,{{ $json.event.reaction }} | Issueに付与するラベルをコンマ区切りで指定 |
| Assignees | (任意) GitHubユーザー名をコンマ区切りで指定 | Issueの担当者を指定 |

## **6\. Part 5: テスト、デプロイ、ベストプラクティス**

### **ワークフローの有効化とエンドツーエンドテスト**

ワークフローを保存し、その後有効化することを強調します。  
ボットが存在するSlackチャンネルのメッセージに指定されたリアクションを追加してテストします。  
n8nの「Executions」リストを確認し、ワークフローがトリガーされ、正常に完了したかを確認します。  
GitHubでIssueが正しい詳細で作成されたことを確認します。

### **n8nでのエラー処理の実装**

堅牢なソリューションには、エラー処理が不可欠です。

* **ノードレベルのエラー処理**: 重要なノード（GitHub Create Issueなど）では、「Settings」タブ \-\> 「Continue on Fail」を使用し、エラー出力を選択します。これにより、ワークフローを分岐させてエラーを適切に処理できます（例: 管理者に通知を送信）33。  
* **ワークフローレベルのエラー処理**: 別のワークフローで「Error Trigger」ノードを設定し、任意のワークフローからのエラーをキャッチします 34。このグローバルエラーハンドラは、詳細をログに記録したり、アラートを送信したりできます。  
* デバッグを容易にするためにノードを明確に命名することの重要性について説明します 35。 ノードレベルの「Continue on Fail」は既知の潜在的な障害点に対して事前対応的であり、グローバルなError Triggerワークフローは予期しない障害に対して事後対応的です。堅牢なソリューションは両方を使用します。

### **APIレート制限の認識**

* **Slack APIレート制限** 29:  
  * 一般的な制限（例: chat.postMessage 1件/秒/チャンネル、Events API 30,000件/時/ワークスペース）。  
  * conversations.historyに特に注意（Tier 3だが、新規/非MarketplaceアプリではTier 1: 1件/分、15アイテム/リクエスト）。ワークフローが非常に頻繁にトリガーされ、その都度メッセージ履歴を取得する場合、これが問題になる可能性があります。  
  * 使用するメソッドの最新のレート制限については、SlackのAPIドキュメントを確認するよう助言します。  
* **GitHub APIレート制限** 36:  
  * 認証済みユーザー（PAT）の場合: 5,000リクエスト/時。Enterprise Cloud上のGitHub Appsの場合はさらに高い。  
  * 同時リクエストや単一エンドポイントへの過多なリクエストに対するセカンダリレート制限。  
  * APIレスポンスヘッダー（X-RateLimit-Remaining）を介してレート制限のステータスを確認する方法を説明します。  
  * 一般的に、この特定のワークフロー（リアクションごとに1つのIssue作成）では、リアクションの量が極端に多くない限り、主要なGitHubレート制限が問題になる可能性は低いです。  
* **緩和策**: IFノードを使用してトリガーをフィルタリングし、必要に応じて遅延を追加し（ただし、リアルタイムトリガーにはあまり理想的ではありません）、ワークフローが実行される頻度に注意します。 あるサービス（例: Slack conversations.history）でレート制限に達すると、そのステップが失敗し、GitHub Issueが作成される前にワークフロー全体が停止する可能性があります。これは、自動化におけるサービスの相互関連性を示しています。

### **一般的な問題のトラブルシューティング**

* **Slackトリガーが発火しない**:  
  * Slackアプリ設定のRequest URLが間違っているか、URLが検証されていない 14。  
  * n8nでワークフローがアクティブになっていない。  
  * SlackアプリのBot Token ScopeまたはEvent Subscriptionが正しくない 14。  
  * Slackアプリが関連チャンネルに追加されていない。  
  * Slackトリガーが断続的に応答しなくなり、ワークフローの無効化/再有効化で解決することがある 37。これは既知の、厄介な問題のようです。  
* **GitHubノードエラー**:  
  * PATが間違っているか、スコープが不十分（例: repoスコープがない）23。  
  * リポジトリの所有者/名前が無効。  
  * 認証の問題（専用のGitHubノードでは可能性は低いが、25は一般的な警告）。  
  * Issueフィールドのデータが無効（例: 存在しないユーザーを割り当てようとしている）。  
* **データマッピングの問題**: 式を使用して以前のノードからのデータを誤って参照している。式エディタを使用し、ステップを個別にテストするよう助言します。  
* **EC2上のDockerボリュームに関する権限の問題**: Dockerデーモンを実行しているユーザー（またはユーザー再マッピングが行われている場合はコンテナ内のnodeユーザー）が、マウントされたホストディレクトリに対して正しい権限を持っていることを確認します 9。ホストディレクトリに対するchownまたはchmodが必要になる場合があります。

## **7\. 結論**

### **自動化されたワークフローの要約**

本レポートでは、SlackのリアクションからGitHubのIssueを構造化して作成するシームレスなフローを、自己管理型のAWS n8nインスタンス上で実現する自動化について概説しました。

### **実現されるメリット**

効率性、コラボレーション、タスク追跡の改善が期待できます。

### **今後の拡張可能性**

* 新しく作成されたGitHub Issueへのリンクを含む確認メッセージをSlackチャンネル（またはスレッドの返信として）に送信する。  
* 複雑な本文フォーマットのためにn8nのCodeノードを使用して、より高度なIssueテンプレートを作成する。  
* より多くのフィルターを追加する（例: 特定のスレッド内のメッセージ、または特定のユーザーロールによるメッセージのみに反応する）。  
* ワークフロー設定（ターゲットリポジトリ、特定の絵文字など）を外部ソース（Google Sheets、データベースなど）に保存し、ワークフローを直接編集せずに簡単に管理できるようにする。  
* n8nの標準ノードを超える複雑なロジックが必要な場合、AWS Lambdaと統合して前処理/後処理タスクを実行する。

#### **引用文献**

1. Efficient n8n Hosting on AWS EC2 | Scalable Cloud Automation, 6月 3, 2025にアクセス、 [https://www.oneclickitsolution.com/centerofexcellence/aiml/n8n-hosting-on-aws-ec2](https://www.oneclickitsolution.com/centerofexcellence/aiml/n8n-hosting-on-aws-ec2)  
2. Docker | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/hosting/installation/docker/](https://docs.n8n.io/hosting/installation/docker/)  
3. AWS Fargate: Serverless Compute Engine for ECS and EKS Workloads \- NareshIT, 6月 3, 2025にアクセス、 [https://nareshit.com/blogs/aws-fargate-a-compute-engine-for-ecs-and-eks](https://nareshit.com/blogs/aws-fargate-a-compute-engine-for-ecs-and-eks)  
4. Run n8n docker hub image on AWS ECS Fargate with EFS \- Questions, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/run-n8n-docker-hub-image-on-aws-ecs-fargate-with-efs/96530](https://community.n8n.io/t/run-n8n-docker-hub-image-on-aws-ecs-fargate-with-efs/96530)  
5. elasticscale/terraform-aws-n8n: Run N8n on AWS ECS Fargate \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/elasticscale/terraform-aws-n8n](https://github.com/elasticscale/terraform-aws-n8n)  
6. Best pattern for a highly reliable AWS host? \- Questions \- n8n Community, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/best-pattern-for-a-highly-reliable-aws-host/6848](https://community.n8n.io/t/best-pattern-for-a-highly-reliable-aws-host/6848)  
7. How to run n8n on AWS cheaper per month \- ElasticScale, 6月 3, 2025にアクセス、 [https://elasticscale.com/blog/run-n8n-on-aws-for-less-than-a-cup-of-coffee-per-month/](https://elasticscale.com/blog/run-n8n-on-aws-for-less-than-a-cup-of-coffee-per-month/)  
8. build-a-slack-bot-with-n8n-webhooks-node-and-github-api.mdx, 6月 3, 2025にアクセス、 [https://github.com/hacktivist123/sheddy-xyz-new/blob/main/data/blog/build-a-slack-bot-with-n8n-webhooks-node-and-github-api.mdx](https://github.com/hacktivist123/sheddy-xyz-new/blob/main/data/blog/build-a-slack-bot-with-n8n-webhooks-node-and-github-api.mdx)  
9. How to troubleshoot n8n container issues in GitHub Actions? \- Latenode community, 6月 3, 2025にアクセス、 [https://community.latenode.com/t/how-to-troubleshoot-n8n-container-issues-in-github-actions/9859](https://community.latenode.com/t/how-to-troubleshoot-n8n-container-issues-in-github-actions/9859)  
10. Help connecting to an AWS RDS postgres database using either N8N hosted or N8N cloud self hosted on Hostinger, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/help-connecting-to-an-aws-rds-postgres-database-using-either-n8n-hosted-or-n8n-cloud-self-hosted-on-hostinger/109423](https://community.n8n.io/t/help-connecting-to-an-aws-rds-postgres-database-using-either-n8n-hosted-or-n8n-cloud-self-hosted-on-hostinger/109423)  
11. Support For SSM Parameter Store as an External Secrets Provider \- n8n Community, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/support-for-ssm-parameter-store-as-an-external-secrets-provider/111759](https://community.n8n.io/t/support-for-ssm-parameter-store-as-an-external-secrets-provider/111759)  
12. External secrets | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/external-secrets/](https://docs.n8n.io/external-secrets/)  
13. Using Secrets Manager environment variables in AWS ECS \- tsmx, 6月 3, 2025にアクセス、 [https://tsmx.net/using-secrets-manager-environment-variables-in-aws-ecs/](https://tsmx.net/using-secrets-manager-environment-variables-in-aws-ecs/)  
14. n8n-docs/docs/integrations/builtin/credentials/slack.md at main · n8n ..., 6月 3, 2025にアクセス、 [https://github.com/n8n-io/n8n-docs/blob/main/docs/integrations/builtin/credentials/slack.md](https://github.com/n8n-io/n8n-docs/blob/main/docs/integrations/builtin/credentials/slack.md)  
15. Slack credentials \- n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/integrations/builtin/credentials/slack/](https://docs.n8n.io/integrations/builtin/credentials/slack/)  
16. This is an n8n community node that lets you use Slack Socket Mode in your n8n workflow \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/mbakgun/n8n-slack-socket-mode](https://github.com/mbakgun/n8n-slack-socket-mode)  
17. Events API | Slack, 6月 3, 2025にアクセス、 [https://api.slack.com/events-api](https://api.slack.com/events-api)  
18. Slack Trigger node documentation | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/](https://docs.n8n.io/integrations/builtin/trigger-nodes/n8n-nodes-base.slacktrigger/)  
19. Slack node documentation | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.slack/)  
20. Slack \- Scope required \- Docs & Tutorials \- n8n Community, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/slack-scope-required/8704](https://community.n8n.io/t/slack-scope-required/8704)  
21. How to Connect Slack to n8n (2025) (Step-by-Step) \- YouTube, 6月 3, 2025にアクセス、 [https://www.youtube.com/watch?v=qk5JH6ImK0I\&pp=0gcJCdgAo7VqN5tD](https://www.youtube.com/watch?v=qk5JH6ImK0I&pp=0gcJCdgAo7VqN5tD)  
22. Slack Trigger node not responding to events \- Questions \- n8n Community, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/slack-trigger-node-not-responding-to-events/80009](https://community.n8n.io/t/slack-trigger-node-not-responding-to-events/80009)  
23. GitHub credentials | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/integrations/builtin/credentials/github/](https://docs.n8n.io/integrations/builtin/credentials/github/)  
24. Managing your personal access tokens \- GitHub Docs, 6月 3, 2025にアクセス、 [https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)  
25. "Bearer Auth" Generic Authentication on the HTTP Request node does not work · Issue \#15261 · n8n-io/n8n \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/n8n-io/n8n/issues/15261](https://github.com/n8n-io/n8n/issues/15261)  
26. Authentication Credentials Reset Automatically in Header Auth Configurations in n8n · Issue \#12596 \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/n8n-io/n8n/issues/12596](https://github.com/n8n-io/n8n/issues/12596)  
27. Slack trigger doesn't ignore · Issue \#13758 · n8n-io/n8n \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/n8n-io/n8n/issues/13758](https://github.com/n8n-io/n8n/issues/13758)  
28. conversations.history method \- Slack API, 6月 3, 2025にアクセス、 [https://api.slack.com/methods/conversations.history](https://api.slack.com/methods/conversations.history)  
29. Rate Limits \- Slack API, 6月 3, 2025にアクセス、 [https://api.slack.com/apis/rate-limits](https://api.slack.com/apis/rate-limits)  
30. Rate limit changes for non-Marketplace apps \- Slack API, 6月 3, 2025にアクセス、 [https://api.slack.com/changelog/2025-05-terms-rate-limit-update-and-faq](https://api.slack.com/changelog/2025-05-terms-rate-limit-update-and-faq)  
31. GitHub node documentation | n8n Docs, 6月 3, 2025にアクセス、 [https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-base.github/)  
32. N8N community node that integrates with Redmine \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/jonathanferreyra/n8n-nodes-redmine](https://github.com/jonathanferreyra/n8n-nodes-redmine)  
33. Are there any generic try/catch n8n nodes that can do error handing for my nodes?, 6月 3, 2025にアクセス、 [https://community.n8n.io/t/are-there-any-generic-try-catch-n8n-nodes-that-can-do-error-handing-for-my-nodes/101677](https://community.n8n.io/t/are-there-any-generic-try-catch-n8n-nodes-that-can-do-error-handing-for-my-nodes/101677)  
34. How To Handle Errors In Your N8N Workflows \- Reddit, 6月 3, 2025にアクセス、 [https://www.reddit.com/r/n8n/comments/1kqz2pm/how\_to\_handle\_errors\_in\_your\_n8n\_workflows/](https://www.reddit.com/r/n8n/comments/1kqz2pm/how_to_handle_errors_in_your_n8n_workflows/)  
35. n8n Best Practices for Clean, Profitable Automations (Or, How to Stop Making Dumb Mistakes) \- Reddit, 6月 3, 2025にアクセス、 [https://www.reddit.com/r/n8n/comments/1k47ats/n8n\_best\_practices\_for\_clean\_profitable/](https://www.reddit.com/r/n8n/comments/1k47ats/n8n_best_practices_for_clean_profitable/)  
36. Rate limits for the REST API \- GitHub Docs, 6月 3, 2025にアクセス、 [https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)  
37. Workflow with Slack trigger becomes unresponsive. · Issue \#13435 · n8n-io/n8n \- GitHub, 6月 3, 2025にアクセス、 [https://github.com/n8n-io/n8n/issues/13435](https://github.com/n8n-io/n8n/issues/13435)