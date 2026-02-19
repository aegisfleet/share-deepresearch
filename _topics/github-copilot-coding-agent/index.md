---
audio: /share-deepresearch/assets/audio/github-copilot-coding-agent.m4a
category: ai
date: 2025-10-30
description: GitHub Copilot Coding Agentで他のリポジトリやAWS・Jenkinsなど外部サービスへの権限付きアクセスを実現するためのセキュリティアーキテクチャと実装方法を解説
ga4_metrics:
  avgSessionDuration: 220.52094714285712
  pageViews: 7
  users: 4
layout: topic
prompt: GitHub Copilot Coding Agentの使い方を調査したい。特に他のリポジトリのファイルを参照したり、AWSやJenkinsといった他のサービスからログを取得するなど、権限が必要な作業をどのようにすれば行えるのかが知りたい。
tags:
- AI Agent
title: 'GitHub Copilot Coding Agent: 外部リソースアクセスのための高度なインテグレーションとセキュリティアーキテクチャ'
video: /share-deepresearch/assets/video/github-copilot-coding-agent.mp4
---

# **GitHub Copilot Coding Agent: 外部リソースアクセスのための高度なインテグレーションとセキュリティアーキテクチャ**

## **1. 分析: GitHub Copilot Agent アーキテクチャの定義**

### **1.1. 序論: 自律型エージェントという新しいクラス**

GitHub Copilot Coding Agentは、開発者支援AIの進化における重要なパラダイムシフトを提示します 1。従来のIDEベースのコード補完とは異なり、Coding Agentは**自律型（Autonomous）**かつ**タスク駆動型（Task-driven）**のエンティティとして設計されています。これは、GitHub Issuesやチャットプロンプトを通じて割り当てられた開発タスク（バグ修正、機能実装、テストカバレッジ向上など）を、バックグラウンドで独立して完了させることができるエージェントです 3。

この自律性を実現する中核的なメカニズムは、その実行環境にあります。Copilot Coding Agentは、**GitHub Actionsを搭載した環境（GitHub Actions-powered environment）**内で動作します 1。このアーキテクチャ上の選択は、エージェントの能力、制限、そして本レポートの主題である「権限が必要な作業」を実行するためのセキュリティモデルを理解する上で、最も決定的な要因となります。

### **1.2. 決定的な区別: Copilotエコシステムにおける3つの「エージェント」**

ユーザーの要求（特にローカルリソースへのアクセス）を正確に分析するためには、現在「エージェント」と呼ばれる主要な3つのCopilot製品を明確に区別する必要があります。これらは根本的に異なる実行環境と権限モデルを持っています 1。

1. **Copilot Coding Agent (クラウド実行型):**  
   * **環境:** GitHubホストの分離された（Sandboxed）GitHub Actionsランナー（VM） 5。  
   * **アクセス:** ローカルマシンへのアクセス権は一切持ちません。リポジトリのコード（クローンされたもの）と、明示的に許可されたネットワークエンドポイントにのみアクセス可能です 5。  
2. **Copilot "Agent Mode" (IDE実行型):**  
   * **環境:** ユーザーのローカルIDE（VS Codeなど）のプロセス内で実行されます 1。  
   * **アクセス:** IDEが開いているワークスペース内のファイルにアクセスできますが、その権限はIDEのプロセスに限定されます。  
3. **Copilot CLI (ターミナル実行型):**  
   * **環境:** ユーザーのローカルターミナルセッション内で実行されます 7。  
   * **アクセス:** ターミナルを実行しているユーザーと**全く同じ権限**を持ちます。これには、カレントディレクトリのファイル操作、シェルコマンドの実行、そして（ここが重要ですが）~/.aws/configや~/.aws/credentialsのようなローカルの認証情報ファイルへの暗黙的なアクセスが含まれます 8。

ユーザーの「AWSからログを取得する」という要求は、ローカルのAWS認証情報を利用するシナリオを示唆しています。このタスクは、**Copilot CLI**にとっては自明です（ローカルのAWS CLIを実行するだけ）。しかし、ユーザーが名指しした**Copilot Coding Agent**にとっては、ローカル認証情報へのアクセスは不可能であり、根本的に異なる（ネットワークと認証を中心とした）ソリューションが必要となります。

このアーキテクチャの違いを明確にすることが、正確なソリューションを提供する第一歩です。

### **1.3. 比較分析: Copilot エージェント・モダリティ**

以下の表は、これら3つのエージェントの主な違いをまとめたものです。

| 機能 | Copilot Coding Agent | Copilot "Agent Mode" (IDE内) | Copilot CLI |
| :---- | :---- | :---- | :---- |
| **実行環境** | クラウド (分離されたGitHub Actionsランナー) | ローカル (IDEプロセス内) | ローカル (ターミナルセッション内) |
| **主な用途** | 自律的なバックグラウンドタスク (PR作成、バグ修正) | 対話的なリアルタイムのコーディング、リファクタリング | 自律的なローカルタスク (テスト実行、ビルド、スクリプト実行) |
| **ローカルファイルへのアクセス** | 不可 (クローンされたリポジトリのみ) | 可能 (IDEのワークスペース内) | 可能 (カレントディレクトリとユーザーのファイルシステム) |
| **ローカル認証情報 (例: ~/.aws/config) へのアクセス** | **不可 (絶対不可能)** | 限定的 (IDEプロセス経由) | **可能 (完全なアクセス)** |
| **主な連携モデル** | 環境カスタマイズ (.yml), MCP, OIDC | VS Code拡張機能, MCP | MCP, シェルコマンド |
| **ネットワークアクセス** | **厳しく制限** (ファイアウォールによる許可リスト制) | ローカルユーザーのマシンと同様 | ローカルユーザーのマシンと同様 |

データソース: 1

### **1.4. Actions環境が権限に与える影響**

本レポートの以降のセクションでは、主に**Coding Agent**と**CLI Agent**に焦点を当てます。Coding AgentがGitHub Actions環境で実行されるという事実は、以下の3つの重要な運用上の影響をもたらします 6。

1. **短命性 (Ephemeral):** エージェントの環境はタスクごとに作成・破棄されます。AWS CLIのような追加ツールは、実行のたびにインストールする必要があります。  
2. **分離性 (Sandboxed):** デフォルトでは、エージェントは外部システム（AWS, Jenkins）からネットワーク的に隔離されています。アクセスには、ファイアウォールの明示的な設定と、OIDCやSecretsによる認証が必須です。  
3. **拡張性 (Customizable):** この環境は、CI/CDで使い慣れたメカニズム（ワークフローYAML）によってカスタマイズ可能です 12。これが、ユーザーの要求を実現するための技術的な鍵となります。

## **2. 解決モデル I: 複数リポジトリおよびコードベースへのアクセス**

### **2.1. 標準的な制限の分析: 分離によるセキュリティ**

Copilot Coding Agentは、デフォルトで厳格なセキュリティ境界内で動作します。割り当てられたタスクが存在する**単一のリポジトリ**のコンテキストにのみアクセスが許可されています 1。

これは技術的な制約ではなく、意図的な**セキュリティ設計**です。もしエージェントが侵害されたり、巧妙なプロンプトインジェクション攻撃を受けたりした場合、攻撃者が組織全体のコードベースを横断的に偵察し、機密情報を持ち出すことを防ぐための重要なセーフガードです。したがって、この制限を回避する行為は、権限の意図的な昇格であり、慎重なリスク分析を伴う必要があります。

### **2.2. アプローチ 1 (RAG/コンテキスト): "Knowledge Bases" による知識集約**

これは、Copilot Enterpriseで利用可能な、最も安全なマルチリポジトリ・コンテキストの提供方法です 14。

* **機能:** 組織のオーナーは、複数のリポジトリから**Markdownドキュメント**を集約した「Knowledge Base（ナレッジベース）」を作成できます 15。  
* **用途:** このナレッジベースは、Copilot Chatのコンテキストとして使用できます 15。  
* **分析:** このアプローチは、Retrieval-Augmented Generation (RAG) の一種です。エージェントに、共有ライブラリのAPI仕様、全社的なアーキテクチャガイドライン、デザインシステムのドキュメントなど、別リポジトリに保存されている**ドキュメント**を参照させるのに最適です。  
* **制限:** ソース 15 は「Markdownドキュメント」と明記しており、別リポジトリの**ソースコード**そのものを直接参照する必要がある場合、この方法では不十分な可能性があります。

### **2.3. アプローチ 2 (対話型): コンテキストツール (@workspace と #githubRepo)**

IDE内のCopilot Chat（Agent Mode）では、ユーザーが明示的にコンテキストを追加できます。

* @workspace: IDEで現在開いているワークスペース全体のコードベースに関する質問に答えるために使用されます 17。  
* #githubRepo: Copilot Chatが、現在のワークスペースに**含まれていない**他のリポジトリを横断的に検索できるようにするツールです 19。  
* **分析:** これらは、開発者が介在する**対話型セッション**において非常に強力なツールです。しかし、自律的にバックグラウンドで実行されるCoding Agentが、これらのツールをどのように指示されて使用するかは不明確です。このアプローチは、人間がループ（human-in-the-loop）にいる場合に限定される可能性が高いです。

### **2.4. アプローチ 3 (高度/自律型): Model Context Protocol (MCP) によるアクセス拡張**

これは、自律型エージェントにとって最も強力かつ高度なソリューションです。

標準のMCP統合では、エージェントのアクセスは一度に一つのリポジトリに制限されています 1。しかし、ドキュメントは明確に「**ただし、Model Context Protocol (MCP) でエージェントを拡張することにより、より広範なアクセスを設定できます**」と述べています 5。

この広範なアクセスを設定するための実装ガイドは以下の通りです 5:

1. Personal Access Token (PAT) の作成:  
   エージェントにアクセスさせたい全てのリポジトリに対する読み取りアクセス権を持つPAT（理想的には、権限を細かく設定したFine-grained PAT）を作成します。  
2. GitHub Environment の作成:  
   リポジトリの Settings > Environments で、copilot という名前の新しい環境を作成します。  
3. 環境シークレットとしてPATを追加:  
   作成した copilot 環境に、新しいシークレットを追加します。シークレット名は、必ず COPILOT_MCP_ というプレフィックスで始める必要があります（例: COPILOT_MCP_SHARED_READ_PAT）。値には、ステップ1で作成したPATを設定します。  
4. MCPサーバーの設定:  
   リポジトリの Settings > Copilot > Coding agent にあるMCP設定（JSON形式）を編集し、組み込みのGitHub MCPサーバーがこの新しいシークレット（PAT）を使用するよう指示します。

**セキュリティ分析:** このアプローチは非常に強力ですが、多くのリポジトリへのアクセス権を単一のトークンに集約することになります。このPATは高度な権限を持つシークレットとなり、最小権限の原則（読み取り専用など）を徹底し、定期的にローテーションするなど、最大限の注意を払って管理する必要があります。

## **3. 解決モデル II: 外部サービスとの連携 (AWS と Jenkins)**

### **3.1. アーキテクチャの基礎: 直接カスタマイズ vs 抽象化された連携**

ユーザーの要求（「ログの取得」）は、根本的に異なる2つのアーキテクチャ・パターンで解決できます。これは、「戦術的アプローチ」と「戦略的アプローチ」の分岐点を表しています。

* 戦術的アプローチ (直接的):  
  最も迅速な解決策は、Coding AgentのActions環境を標準的なCIジョブとして扱うことです。copilot-setup-steps.yml 12 を使用して apt-get install awscli や curl を実行させます。次に、エージェントに対して「aws logs... を実行せよ」または「curl -u $USER:$TOKEN... を実行せよ」といった具体的なコマンドを含むプロンプトを与えます。この方法は迅速ですが、エージェントが特定のコマンドを知っている必要があり、実行コンテキストに認証情報が直接混在するため、脆弱で保守性に欠けます。  
* 戦略的アプローチ (抽象化):  
  より堅牢で、スケーラブルかつ安全な方法は、Model Context Protocol (MCP) を活用することです 20。このモデルでは、我々は「アダプタ」として機能するMCPサーバーを構築（または利用）します。エージェントは curl や awscli の存在を知る必要はありません。その代わり、get_jenkins_log や get_aws_cloudwatch_log といった新しい「ツール」を利用できるようになります。エージェントは「'deploy-prod'ジョブのログを取得して」と高レベルで判断するだけで、リクエストを受け取ったMCPサーバーが（安全な場所で）認証やAPI呼び出しを処理し、ログデータのみをエージェントに返します。

**結論:** 戦術的アプローチはプロトタイピングに適しています。しかし、エンタープライズ環境での本番運用には、複雑さを抽象化し、ロジックを一元管理し、エージェントによる生の認証情報へのアクセスを制限する**戦略的MCPアプローチ**が、アーキテクチャとして正しい選択です。

### **3.2. 戦術的アプローチ: copilot-setup-steps.yml によるエージェント環境のカスタマイズ**

このアプローチは、標準的なActionsのメカニズムを使用して、エージェントの実行環境を直接構成するものです。リポジトリの .github/workflows/copilot-setup-steps.yml という特別なファイルは、エージェントがタスクを開始する**前**に実行されます 12。

実装ガイド 12:

* **ツールのインストール:** run ステップを追加し、AWS CLIやjqなどの必要な依存関係をインストールします。  

  ```YAML
  jobs:
    copilot-setup-steps:
      runs-on: ubuntu-latest
      steps:
        - name: Install AWS CLI and jq
          run: |
            sudo apt-get update  
            sudo apt-get install -y awscli jq
  ```

* 認証情報の安全な注入 (Jenkinsの場合):  
  JenkinsのAPIトークンを、まずGitHubの Settings > Secrets に（例: JENKINS_API_TOKENとして）保存します 22。次に、このシークレットをエージェントの環境変数として利用可能にします。  

  ```YAML  
  # (上記YAMLの続き)  
        - name: Set Jenkins Env Variables  
          env:  
            # GitHub Secretsから一時的に読み込む  
            JENKINS_TOKEN_FROM_SECRETS: ${{ secrets.JENKINS_API_TOKEN }}  
          run: |  
            # エージェントのメインプロセスからアクセスできるよう、GITHUB_ENVに書き出す  
            echo "JENKINS_API_TOKEN=${JENKINS_TOKEN_FROM_SECRETS}" >> $GITHUB_ENV
  ```

* 実行:  
  この設定により、エージェントは curl... -H "Authorization: Bearer $JENKINS_API_TOKEN"... や aws... といったコマンドを実行するよう指示できます（AWSの認証はセクション4.1で詳述）。

### **3.3. 戦略的アプローチ: Model Context Protocol (MCP) による連携**

MCPは、AIエージェントが外部のツールやコンテキストを発見し、利用するためのオープンプロトコルであり 20、GitHubが推奨するスケーラブルな連携ソリューションです 25。

**Jenkins向けソリューション: Jenkins MCP Server Plugin**

* **概要:** Jenkinsには「**MCP Server Plugin**」と呼ばれる、まさにこの目的のためのプラグインが存在します 26。  
* **機能:** このプラグインをインストールすると、Jenkinsインスタンス自体がMCPサーバーとして機能するようになります。  
* **ワークフロー:**  
  1. 開発者がJenkinsマスターにこのプラグインをインストールします 26。  
  2. Copilot側（IDEまたはエージェントのMCP設定）で、このJenkins MCPサーバーのエンドポイントと、認証用のJenkins APIトークン（Basic認証）を設定します 26。  
  3. Copilotは、list_jenkins_job や get_last_build_status といった新しい「ツール」セットを認識します 26。  
  4. 開発者（またはエージェント）は、「'deploy-prod'の最後の失敗ビルドのログを見せて」といった自然言語で指示を出せるようになります。CopilotはこれをMCP呼び出しに変換し、Jenkinsサーバーがログテキストを返します。  
* **分析:** この方法は、エージェントにcurlコマンドを教え込む「戦術的アプローチ」よりもはるかに優れており、セマンティックで堅牢な連携を実現します。

**AWS向けソリューション: カスタムAWS MCPサーバーの設計パターン**

* **概要:** （調査時点では）AWS用の公式MCPサーバーは存在しないため、構築する必要があります。  
* **アーキテクチャ:**  
  1. AWS LambdaやAzure App Service 27 などで、MCPプロトコルを実装した軽量なWebサービスをホストします 24。  
  2. このサービスは、get_cloudwatch_logs(log_group, stream) のような「ツール」を外部に公開します。  
  3. サービス自体は、安全な**IAMロール**を使用してCloudWatchへの問い合わせを実行します。  
  4. Copilot Agentは、この新しいカスタムMCPサーバーを利用するよう設定されます。  
* **分析:** これにより、Copilot Agentは awscli やIAMの存在を一切知ることなく、AWSのログを取得する「能力」を手に入れることができます。

## **4. コア・フレームワーク: 認証と権限の管理**

ユーザーの要求の核心は「権限」の扱いです。AWSとJenkinsという2つの主要なシナリオは、それぞれ異なるベストプラクティスのセキュリティパターンを必要とします。

### **4.1. シナリオ 1: AWSへのセキュアなアクセス (シークレットレス・パターン)**

* **課題:** Coding AgentのActions環境 6 が、AWS APIを呼び出す必要がある。  
* **アンチパターン:** 長期的な AWS_ACCESS_KEY_ID と AWS_SECRET_ACCESS_KEY をGitHub Secretsに保存すること 22。これは漏洩のリスクがあり、ローテーションも手動となるため、重大なセキュリティリスクです。  
* ベストプラクティス (OIDC):  
  正しい方法は、OpenID Connect (OIDC) を使用したIDフェデレーションです 29。GitHub ActionsはOIDC IDプロバイダーとして機能し、AWSに一時的な認証情報を動的に要求できます。

実装ガイド 30:

1. AWS側 (IAM):  
   IAMダッシュボードで、新しいIDプロバイダーを作成します。プロバイダーURLに <https://token.actions.githubusercontent.com>、対象者（Audience）に sts.amazonaws.com を指定します。  
2. AWS側 (IAM):  
   新しいIAMロールを作成します（例: GitHubCopilotAgentRole）。このロールに、必要なAWS権限（例: CloudWatchLogsReadOnlyAccess）をアタッチします。  
3. AWS側 (IAM):  
   作成したロールの「信頼関係」ポリシーを編集し、GitHub OIDCプロバイダーからの sts:AssumeRoleWithWebIdentity アクションを許可します。セキュリティを強化するため、Condition 句を使用して、特定のGitHubリポジトリ（例: repo:your-org/your-repo:ref:refs/heads/main）からのみロールを引き受けられるように厳格にスコープを設定します。  
4. GitHub側 (copilot-setup-steps.yml):  
   エージェントのセットアップワークフローで aws-actions/configure-aws-credentials アクションを使用し、OIDC認証を実行します。  

  ```YAML  
   jobs:  
     copilot-setup-steps:  
       runs-on: ubuntu-latest  
       # OIDC認証には id-token: write 権限が必須  
       permissions:  
         id-token: write  
         contents: read  
       steps:  
         - name: Configure AWS Credentials via OIDC  
           uses: aws-actions/configure-aws-credentials@main  
           with:  
             role-to-assume: arn:aws:iam::YOUR_ACCOUNT_ID:role/GitHubCopilotAgentRole  
             aws-region: us-east-1

         # (awscli のインストールなど、他のセットアップステップ)
  ```

* **結果:** この構成により、エージェントの環境には、GitHub Actionsによって動的に発行された**短命（Short-lived）**なAWS認証情報が設定されます。一切のシークレットを保存することなく、安全に aws コマンドが実行可能になります。

### **4.2. シナリオ 2: Jenkinsへのセキュアなアクセス (トークンベース・パターン)**

* **課題:** Jenkinsは通常、OIDCフェデレーションをサポートしておらず、APIトークンによる認証が必要です 32。  
* ベストプラクティス (Secrets):  
  この回避不可能なシークレットを取り扱う正しい方法は、GitHubの暗号化されたシークレットストアを利用することです。

実装ガイド 12:

1. GitHub側 (Secrets):  
   リポジトリの Settings > Secrets and variables > Actions で、JENKINS_API_TOKEN という名前のシークレットを作成します（よりセキュアにするには、セクション2.4で作成した copilot 環境専用の環境シークレットとして作成します）。  
2. GitHub側 (copilot-setup-steps.yml):  
   セクション3.2で示したように、このシークレットをエージェントの環境変数に注入します。  

  ```YAML  
   jobs:  
     copilot-setup-steps:  
       runs-on: ubuntu-latest  
       steps:  
         - name: Inject Jenkins API Token  
           run: echo "JENKINS_API_TOKEN=${{ secrets.JENKINS_API_TOKEN }}" >> $GITHUB_ENV
  ```

* **結果:** エージェントのプロセスは JENKINS_API_TOKEN 環境変数を読み込めるようになり、curl コマンドや、この環境変数を読み取るように設定されたJenkins MCPプラグイン 26 で使用できます。

### **4.3. 見落とされがちな必須要件: エージェント・ファイアウォールの設定**

上記の4.1（OIDC）と4.2（Secrets）のソリューションは、デフォルトのCopilot Coding Agent環境では**両方とも失敗します**。

* **理由:** Coding Agentのデフォルトのセキュリティ態勢は「高」であり、その「**インターネットアクセスは、カスタマイズ可能な信頼できる宛先のリストに厳しく制限されています**」6。  
* **影響:** つまり、AWS STSエンドポイント（sts.amazonaws.com）へのOIDCコールや、社内のJenkinsマスター（jenkins.my-company.com）へのAPIコールは、デフォルトで**ファイアウォールによってブロック**されます。  
* 解決策:  
  これらの外部連携を機能させるための絶対的な前提条件として、リポジトリ管理者は Settings > Copilot > Coding agent に移動し、「Custom allowlist（カスタム許可リスト）」に、必要な外部エンドポイント（例: *.amazonaws.com や jenkins.my-company.com）を明示的に追加する必要があります 9。

このファイアウォール設定は、見落とされがちですが、外部サービス連携を成功させるための最も重要なステップの一つです。

## **5. セキュリティとガバナンスの設計図**

### **5.1. 組み込みのセキュリティメカニズム: エージェントの「免疫システム」**

Coding Agentは、単なるLLMのラッパーではありません。GitHubの堅牢なセキュリティプラットフォームに深く統合されています。

* **自動検証:** エージェントが生成した新しいコードは、**自動的に**分析されます。これには、CodeQLによる潜在的なセキュリティ脆弱性のスキャン、GitHub Advisory Databaseによる新規依存関係のチェック、およびSecret Scanningによる偶発的な機密情報（APIキーなど）の混入検知が含まれます 5。  
* **セキュアなワークフロー:** エージェントは、自身が作成したプルリクエスト（PR）を自己承認したりマージしたりすることはできません 5。コードが本番環境にマージされる前に、必ず書き込み権限を持つ**人間によるレビューと承認**が必要です 6。これにより、開発ライフサイクルにおける「Human-in-the-Loop（人間参加型）」の原則が強制されます。

### **5.2. カスタムMCPサーバーのセキュリティ・ベストプラクティス**

セクション3.3で推奨したカスタムMCPサーバー（例: AWS用）の構築は、新たな攻撃対象領域を生み出します。

* **リスク:** MCPサーバーはAI（Copilot）とバックエンドサービス（Jenkins, AWS）の「橋渡し」をします。攻撃者は以下のような攻撃を試みる可能性があります。  
  * **Confused Deputy（混乱した代理人）攻撃:** 攻撃者がCopilotに巧妙なプロンプトを送り、MCPサーバーを呼び出させます。このとき、Copilotエージェントはアクセスできるが、プロンプトを入力した**元のユーザー**はアクセスできないはずのプロジェクトのログを要求させる可能性があります 36。  
  * **Token Passthrough（トークン・パススルー）脆弱性:** Copilotとの通信に使用されるトークンが、MCPサーバーへの直接攻撃に再利用される危険性です 36。  
* 対策 (MCP仕様のベストプラクティス) 36:  
  1. **厳格な認証 (OAuth 2.1):** MCPサーバーは、受信したすべてのリクエストのトークンを厳格に検証する必要があります。  
  2. **リソース・インジケータ (RFC 8707) の使用:** トークンが特定の「対象者（Audience）」、すなわちそのMCPサーバー自身のためだけに発行されたものであることを保証し、トークンの再利用攻撃を防ぎます。  
  3. **データ分離の強制:** MCPサーバーは、トークンを検証した後、そこに含まれる**元のユーザー**のIDを抽出し、そのユーザーがバックエンドシステム（例: Jenkins）において**本当にそのデータ（ログ）へのアクセス権を持っているか**を再検証する必要があります。AIエージェントを盲目的に信頼してはなりません。

### **5.3. 責任ある運用: 人間というファイアウォール**

最終的な防衛線は、コードをレビューする開発者自身です。コードが新人の開発者から来たものであれ、AIエージェントから来たものであれ、すべての提案は精査されなければなりません 37。

LLMベースのツールには、脆弱なコードの出力、機密データの漏洩、プロンプトインジェクション攻撃への耐性といった固有のリスクが常につきまといます 40。組織は、AIが生成したPRに対して厳格なコードレビュー・ポリシーを施行し、エージェントの出力を盲信しない文化を醸成する必要があります。

## **6. 結論: 戦略的実装ロードマップ**

### **6.1. 解決パターンの総括**

本分析により、Copilot Coding Agentに権限が必要なタスクを実行させるための、明確なアーキテクチャ・パターンが明らかになりました。

1. **複数リポジトリへのアクセス:**  
   * **推奨 (RAG):** **Knowledge Bases** 15 を使用し、ドキュメント・コンテキストを安全に集約します。  
   * **高度 (直接):** ソースコードへのプログラム的アクセスが必須の場合のみ、**MCPによる広範なPAT** 5 を使用し、関連するセキュリティリスクを許容します。  
2. **Jenkinsへのアクセス:**  
   * **戦略的推奨:** **Jenkins MCP Server Plugin** 26 をインストールし、セマンティックでリッチな連携を実現します。  
   * **戦術的代替:** **環境カスタマイズ** 12 と **GitHub Secrets** 22 を使用し、curl コマンドを直接実行させます。  
3. **AWSへのアクセス:**  
   * **必須プラクティス:** **OIDCフェデレーション** 30 を使用します。エンタープライズ環境において、静的なAPIキーをSecretsに保存する選択肢は取るべきではありません。  
4. **普遍的な前提条件:**  
   * 上記のどの外部連携も、リポジトリ設定で**エージェントのファイアウォール** 9 を設定し、AWSおよびJenkinsのエンドポイントへのアウトバウンド通信を許可しない限り、機能しません。

### **6.2. 戦略的導入ロードマップ**

Copilot Agentの高度な機能を組織に安全に導入するため、以下の段階的なアプローチを推奨します。

* **フェーズ 1 (評価 - 戦術的アプローチ):**  
  * copilot-setup-steps.yml 12 を使用した「直接的アプローチ」で、概念実証（PoC）を実施します。  
  * AWS CLIとcurlをインストールし、OIDC 31 とSecrets 22 を設定します。  
  * ファイアウォールを構成 9 し、エージェントが実際にAWSとJenkinsから単一のログファイルを取得できることを実証します。  
* **フェーズ 2 (統合 - 戦略的アプローチ):**  
  * 本番環境への展開にあたり、「戦略的MCPアプローチ」にリファクタリングします。  
  * Jenkins MCP Server Plugin 26 をインストールし、設定します。  
  * MCPセキュリティ・ベストプラクティス 36 に準拠した、軽量で安全なカスタムAWS MCPサーバーを設計・構築します 28。  
* **フェーズ 3 (ガバナンス):**  
  * エージェントが生成したすべてのPRに対し、厳格な人間によるレビューを必須とするポリシーを適用します 6。  
  * OIDCおよびMCPサーバーに付与されたIAMロールの権限を定期的に監査し、最小権限の原則が維持されていることを確認します。

#### **引用文献**

1. About GitHub Copilot coding agent - GitHub Enterprise Cloud Docs, 10月 30, 2025にアクセス、 [https://docs.github.com/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent)  
2. Piloting GitHub Copilot coding agent in your organization, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/tutorials/coding-agent/pilot-coding-agent](https://docs.github.com/en/copilot/tutorials/coding-agent/pilot-coding-agent)  
3. GitHub Copilot · Your AI pair programmer, 10月 30, 2025にアクセス、 [https://github.com/features/copilot](https://github.com/features/copilot)  
4. GitHub Copilot coding agent 101: Getting started with agentic workflows on GitHub, 10月 30, 2025にアクセス、 [https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/](https://github.blog/ai-and-ml/github-copilot/github-copilot-coding-agent-101-getting-started-with-agentic-workflows-on-github/)  
5. About GitHub Copilot coding agent, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent](https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-coding-agent)  
6. GitHub Copilot: Meet the new coding agent, 10月 30, 2025にアクセス、 [https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/](https://github.blog/news-insights/product-news/github-copilot-meet-the-new-coding-agent/)  
7. About GitHub Copilot CLI, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli](https://docs.github.com/en/copilot/concepts/agents/about-copilot-cli)  
8. Responsible use of GitHub Copilot CLI, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/responsible-use/copilot-cli](https://docs.github.com/en/copilot/responsible-use/copilot-cli)  
9. Customizing or disabling the firewall for GitHub Copilot coding agent ..., 10月 30, 2025にアクセス、 [https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/customizing-or-disabling-the-firewall-for-copilot-coding-agent](https://docs.github.com/copilot/how-tos/agents/copilot-coding-agent/customizing-or-disabling-the-firewall-for-copilot-coding-agent)  
10. Credentials - AWS Copilot CLI, 10月 30, 2025にアクセス、 [https://aws.github.io/copilot-cli/docs/credentials/](https://aws.github.io/copilot-cli/docs/credentials/)  
11. How to set up development and production environments using AWS Copilot: Example using a `plumber` API. R-bloggers, 10月 30, 2025にアクセス、 [https://www.r-bloggers.com/2024/02/how-to-set-up-development-and-production-environments-using-aws-copilot-example-using-a-plumber-api/](https://www.r-bloggers.com/2024/02/how-to-set-up-development-and-production-environments-using-aws-copilot-example-using-a-plumber-api/)  
12. Customizing the development environment for GitHub Copilot ..., 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment)  
13. 10月 30, 2025にアクセス、 [https://docs.github.com/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent#:~:text=In%20addition%2C%20Copilot%20cannot%20make,%2C%20however%2C%20configure%20broader%20access.](https://docs.github.com/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent#:~:text=In%20addition%2C%20Copilot%20cannot%20make,%2C%20however%2C%20configure%20broader%20access.)  
14. GitHub Copilot features, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/get-started/features](https://docs.github.com/en/copilot/get-started/features)  
15. GitHub Copilot knowledge bases - GitHub Enterprise Cloud Docs, 10月 30, 2025にアクセス、 [https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/context/knowledge-bases](https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/context/knowledge-bases)  
16. Creating and managing GitHub Copilot knowledge bases, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/how-tos/provide-context/create-knowledge-bases](https://docs.github.com/en/copilot/how-tos/provide-context/create-knowledge-bases)  
17. visual studio code - How to use GitHub Copilot for multiple files? - Stack Overflow, 10月 30, 2025にアクセス、 [https://stackoverflow.com/questions/76509513/how-to-use-github-copilot-for-multiple-files](https://stackoverflow.com/questions/76509513/how-to-use-github-copilot-for-multiple-files)  
18. Can copilot analyse your entire repo, or just one file at a time? : r/vscode - Reddit, 10月 30, 2025にアクセス、 [https://www.reddit.com/r/vscode/comments/1cc9yed/can_copilot_analyse_your_entire_repo_or_just_one/](https://www.reddit.com/r/vscode/comments/1cc9yed/can_copilot_analyse_your_entire_repo_or_just_one/)  
19. GitHub Copilot Cross Repo Magic: Reference Any Repository - YouTube, 10月 30, 2025にアクセス、 [https://www.youtube.com/watch?v=TFD4BR-7X9Y](https://www.youtube.com/watch?v=TFD4BR-7X9Y)  
20. Enhancing GitHub Copilot agent mode with MCP, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp](https://docs.github.com/en/copilot/tutorials/enhance-agent-mode-with-mcp)  
21. Using Model Context Protocol - GitHub Docs, 10月 30, 2025にアクセス、 [https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol](https://docs.github.com/copilot/customizing-copilot/using-model-context-protocol)  
22. Using secrets in GitHub Actions - GitHub Docs, 10月 30, 2025にアクセス、 [https://docs.github.com/actions/security-guides/using-secrets-in-github-actions](https://docs.github.com/actions/security-guides/using-secrets-in-github-actions)  
23. Meet the GitHub MCP Registry: The fastest way to discover MCP Servers - The GitHub Blog, 10月 30, 2025にアクセス、 [https://github.blog/ai-and-ml/github-copilot/meet-the-github-mcp-registry-the-fastest-way-to-discover-mcp-servers/](https://github.blog/ai-and-ml/github-copilot/meet-the-github-mcp-registry-the-fastest-way-to-discover-mcp-servers/)  
24. Use MCP servers in VS Code, 10月 30, 2025にアクセス、 [https://code.visualstudio.com/docs/copilot/customization/mcp-servers](https://code.visualstudio.com/docs/copilot/customization/mcp-servers)  
25. GitHub Copilot CLI, 10月 30, 2025にアクセス、 [https://github.com/features/copilot/cli](https://github.com/features/copilot/cli)  
26. MCP Server Jenkins plugin, 10月 30, 2025にアクセス、 [https://plugins.jenkins.io/mcp-server/](https://plugins.jenkins.io/mcp-server/)  
27. Web app as MCP server in GitHub Copilot Chat agent mode (Python) - Microsoft Learn, 10月 30, 2025にアクセス、 [https://learn.microsoft.com/en-us/azure/app-service/tutorial-ai-model-context-protocol-server-python](https://learn.microsoft.com/en-us/azure/app-service/tutorial-ai-model-context-protocol-server-python)  
28. Building your first MCP server: How to extend AI tools with custom capabilities, 10月 30, 2025にアクセス、 [https://github.blog/ai-and-ml/github-copilot/building-your-first-mcp-server-how-to-extend-ai-tools-with-custom-capabilities/](https://github.blog/ai-and-ml/github-copilot/building-your-first-mcp-server-how-to-extend-ai-tools-with-custom-capabilities/)  
29. OpenID Connect (OIDC) for GitHub Copilot Extensions, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/concepts/extensions/openid-connect](https://docs.github.com/en/copilot/concepts/extensions/openid-connect)  
30. Configuring OpenID Connect in Amazon Web Services - GitHub Docs, 10月 30, 2025にアクセス、 [https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/configuring-openid-connect-in-amazon-web-services)  
31. Configure AWS credential environment variables for use in other GitHub Actions., 10月 30, 2025にアクセス、 [https://github.com/aws-actions/configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials)  
32. How to use Github Personal Access Token in Jenkins - Stack Overflow, 10月 30, 2025にアクセス、 [https://stackoverflow.com/questions/61105368/how-to-use-github-personal-access-token-in-jenkins](https://stackoverflow.com/questions/61105368/how-to-use-github-personal-access-token-in-jenkins)  
33. jenkinsci/github-oauth-plugin: Jenkins authentication plugin using GitHub OAuth as the source. - GitHub, 10月 30, 2025にアクセス、 [https://github.com/jenkinsci/github-oauth-plugin](https://github.com/jenkinsci/github-oauth-plugin)  
34. Configuring Jenkins with GitHub (Authorization) - Stack Overflow, 10月 30, 2025にアクセス、 [https://stackoverflow.com/questions/60559456/configuring-jenkins-with-github-authorization](https://stackoverflow.com/questions/60559456/configuring-jenkins-with-github-authorization)  
35. Copilot coding agent now automatically validates code security and quality, 10月 30, 2025にアクセス、 [https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality/](https://github.blog/changelog/2025-10-28-copilot-coding-agent-now-automatically-validates-code-security-and-quality/)  
36. How to build secure and scalable remote MCP servers - The GitHub ..., 10月 30, 2025にアクセス、 [https://github.blog/ai-and-ml/generative-ai/how-to-build-secure-and-scalable-remote-mcp-servers/](https://github.blog/ai-and-ml/generative-ai/how-to-build-secure-and-scalable-remote-mcp-servers/)  
37. Trust Center - github.com - GitHub Copilot Trust Center, 10月 30, 2025にアクセス、 [https://copilot.github.trust.page/faq](https://copilot.github.trust.page/faq)  
38. Best practices for using GitHub Copilot, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/get-started/best-practices](https://docs.github.com/en/copilot/get-started/best-practices)  
39. Responsible use of GitHub Copilot coding agent on GitHub.com, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent](https://docs.github.com/en/copilot/responsible-use/copilot-coding-agent)  
40. Responsible use of GitHub Copilot Chat in your IDE, 10月 30, 2025にアクセス、 [https://docs.github.com/en/copilot/responsible-use/chat-in-your-ide](https://docs.github.com/en/copilot/responsible-use/chat-in-your-ide)  
41. GitHub Copilot Security Risks and How to Mitigate Them, 10月 30, 2025にアクセス、 [https://www.prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities](https://www.prompt.security/blog/securing-enterprise-data-in-the-face-of-github-copilot-vulnerabilities)
