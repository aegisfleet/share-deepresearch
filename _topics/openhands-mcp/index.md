---
layout: topic
title: "OpenHands、GitHub Actions、Playwright-MCPを活用したブラウザ操作自動化ワークフローの実現可能性調査と実践ガイド"
date: 2025-05-27
prompt: "OpenHandsとGitHub ActionsとPlaywright-MCPを使って、ワークフローの中でブラウザ操作の自動化を行いたい。実現可能か調査し、可能であれば具体的な使用例をまとめて欲しい。"
category: "ai"
tags: [OpenHands,GitHub Actions,Playwright-MCP]
audio: "/share-deepresearch/assets/audio/openhands-mcp.mp3"
supplementary_materials:
  - title: "AI駆動型開発自動化の最前線：市場トレンド分析"
    url: "/share-deepresearch/topics/openhands-mcp/infographic.html"
---

# **OpenHands、GitHub Actions、Playwright-MCPを活用したブラウザ操作自動化ワークフローの実現可能性調査と実践ガイド**

## **1\. はじめに**

本レポートは、OpenHands、GitHub Actions、およびPlaywright-MCP（Model Context Protocol）を組み合わせ、ワークフロー内でのブラウザ操作の自動化を実現する可能性について調査し、具体的な使用例を提示することを目的としています。現代のソフトウェア開発において、反復的なブラウザ操作タスクの自動化は、テストの効率化、デプロイメントプロセスの迅速化、そして開発者の生産性向上に不可欠です。OpenHandsのようなAIエージェントプラットフォーム、GitHub ActionsのようなCI/CDツール、そしてPlaywright-MCPのような高度なブラウザ制御プロトコルを連携させることで、これまで手動で行っていた、あるいは限定的なスクリプトで対応していたブラウザ操作を、よりインテリジェントかつ柔軟に自動化できる可能性があります。

本調査では、これらの技術要素の概要、連携アプローチ、具体的な設定方法、そして実際のユースケースを詳細に解説します。これにより、開発者は本技術の導入検討に必要な知見を得るとともに、実践的な導入ステップを理解することができます。

## **2\. OpenHandsとPlaywright-MCPの概要**

### **2.1. OpenHands**

OpenHands（旧OpenDevin）は、AIエージェントが人間開発者と同様の方法でタスクを実行できるオープンソースプラットフォームです 1。エージェントは、コードの読み取り、理解、変更、シェルコマンドの実行、Webブラウジング、API操作、ファイルシステム管理といった包括的な能力を備えています 1。これらの操作は、通常Dockerコンテナとして実装される保護されたサンドボックス環境内で安全に実行されます 1。

OpenHandsのアーキテクチャは主に、エージェントの抽象化、アクションと観察の履歴を追跡するイベントストリーム、そしてアクションを実行して観察結果に変換するランタイムの3つのコンポーネントで構成されています 2。特にブラウザ操作に関しては、OpenHandsはBrowserGym（ServiceNowによって開発されたPlaywrightベースのChromiumブラウザ環境）を利用して、ナビゲーション、クリック、タイピング、スクロールなどのアクションプリミティブを提供します 2。エージェントはこれらのプリミティブを通じてウェブサイトと対話し、情報を収集したりタスクを実行したりします 2。OpenHandsは、WebArenaのようなベンチマークでの評価も行われており、そのWebブラウジング能力が検証されています 2。

OpenHandsエージェントは、自然言語による指示に基づいてタスクを計画し実行します。例えば、「特定のウェブサイトから情報を抽出する」「フォームにデータを入力して送信する」といった指示を解釈し、必要なブラウザ操作を自律的に行います 1。

### **2.2. Playwright-MCP**

Playwright-MCP (Model Context Protocol) は、Playwrightのブラウザ自動化能力を大規模言語モデル（LLM）やその他のAIエージェントが利用できるように設計されたサーバーです 6。従来のスクリーンショットや視覚ベースのモデルに依存するのではなく、主にブラウザのアクセシビリティツリーを通じて構造化されたデータに基づいてウェブページと対話します 6。これにより、高速かつ軽量で、LLMにとって親和性の高い、決定論的なツール適用が可能になります 6。

Playwright-MCPはクライアントサーバーアーキテクチャを採用しており、Playwright MCPサーバーがPlaywrightが管理するブラウザインスタンスへのアクセスを提供し、クライアント（AIエージェントなど）がMCPサーバーに接続してブラウザ操作を指示します 8。主な操作モードとして、アクセシビリティツリーを利用する「スナップショットモード」（デフォルト）と、スクリーンショットを利用する「ビジョンモード」があります 6。スナップショットモードは、構造化されたテキストデータに基づいて動作するため高速かつ信頼性が高い一方、ビジョンモードはアクセシビリティ情報が不十分なカスタムUI要素などに対応できる可能性があります 7。

Playwright-MCPは、ナビゲーション、クリック、入力、スクリーンショット取得、要素の待機など、多岐にわたるブラウザ操作ツールを提供します 6。これらのツールは、AIエージェントがより複雑なテストフローや自動化ワークフローを編成するのに役立ちます 8。特に、VS CodeのGitHub CopilotエージェントやCursor、Claude DesktopといったAI支援開発ツールとの連携が考慮されています 6。

## **3\. 連携アプローチの比較**

OpenHands、GitHub Actions、Playwright-MCPを連携させてブラウザ操作を自動化するアプローチは、主に2つのシナリオが考えられます。1つはOpenHandsの標準的なブラウザ操作機能（BrowserGymベース）をGitHub Actions内で利用するアプローチ、もう1つはOpenHandsのカスタムサンドボックス内にPlaywright-MCPサーバーを導入し、OpenHandsエージェントがMCPクライアントとして動作するより高度なアプローチです。

これらのアプローチは、セットアップの複雑さ、制御の粒度、そして対応可能なユースケースにおいてそれぞれ特徴があります。以下の表に、各アプローチの比較を示します。

**Table 1: 連携アプローチの比較**

| 特徴項目 (Feature) | OpenHands標準機能 (BrowserGym) | OpenHands \+ Playwright-MCP連携 |
| :---- | :---- | :---- |
| **主要なブラウザ制御方法** | OpenHandsエージェントがLLMを通じてBrowserGymのアクションプリミティブを解釈・実行 2。 | OpenHandsエージェントがLLMを通じてPlaywright-MCPサーバーの提供するツール（コマンド）を解釈・実行 6。エージェントはMCPクライアントとして振る舞う必要がある。 |
| **制御の粒度** | BrowserGymが提供するアクションセットに依存。比較的抽象度が高い場合がある 13。 | Playwright-MCPが提供する詳細なツールセットにより、より細かいブラウザ操作が可能 6。アクセシビリティツリーのrefを利用した精密な要素指定など。 |
| **セットアップの複雑性** | 比較的容易。OpenHandsの標準インストールとGitHub Actionsの設定で実現可能 1。 | 高い。OpenHandsカスタムサンドボックスの構築、Playwright-MCPサーバーの導入と設定、エージェントのMCPクライアント機能の実装（またはそのための指示）が必要 6。 |
| **利点 (Pros)** | 導入が容易。OpenHandsエージェントの汎用的なタスク解決能力を活用しやすい。 | 高度なブラウザ制御、アクセシビリティ情報に基づく堅牢な要素特定、Playwrightの豊富な機能を間接的に利用可能 6。 |
| **欠点 (Cons)** | 複雑な動的コンテンツや特殊なUI要素への対応が限定的である可能性。BrowserGymのアクションスペースに制約される。 | セットアップと設定が複雑。OpenHandsエージェントがPlaywright-MCPツールを適切に利用するためのプロンプト設計がより重要になる。 |
| **推奨ユースケース** | 簡単なWebスクレイピング、基本的なフォーム入力、E2Eテストの補助、OpenHandsエージェントによる一般的なWebタスクの自動化。 | 複雑なWebアプリケーションの精密なテスト、動的コンテンツへの高度な対応、アクセシビリティを重視したテスト、Playwrightの知見を活かした自動化。 |
| **データソース** | 1 | 6 |

この比較から、プロジェクトの要件や開発チームのスキルセットに応じて適切なアプローチを選択することが重要であると理解できます。単純なタスクであればOpenHandsの標準機能で十分対応可能ですが、より高度で精密なブラウザ制御が求められる場合は、Playwright-MCPとの連携が有力な選択肢となります。ただし、後者はその分、導入と運用のコストが高くなることを考慮に入れる必要があります。

## **4\. 具体的な使用例**

ここでは、前述の2つの連携アプローチに基づいた具体的な使用例を、GitHub Actionsワークフローの設定、OpenHandsへのタスク定義（プロンプト）、期待される出力と成果物の観点から解説します。

### **4.1. シナリオ1：OpenHands標準機能とGitHub Actionsの連携**

このシナリオでは、OpenHandsが標準で備えるBrowserGymベースのブラウザ操作機能をGitHub Actionsワークフロー内で活用します。

#### **4.1.1. GitHub Actionsワークフローの設定**

OpenHands Resolver（openhands-resolver.yml）を利用して、GitHubのIssueやPull RequestのイベントをトリガーにOpenHandsエージェントを起動します 14。ワークフローファイルはリポジトリの .github/workflows/ ディレクトリに配置します。

**YAML記述例 (.github/workflows/openhands-browser-task.yml):**

YAML

name: OpenHands Browser Automation Task

on:  
  issue_comment:  
    types: \[created\]

jobs:  
  run_openhands_browser_task:  
    \# コメントが特定のキーワード（例: @openhands-agent fix-me）で始まる場合にのみ実行  
    if: github.event.issue.pull_request && startsWith(github.event.comment.body, '@openhands-agent fix-me')  
    runs-on: ubuntu-latest  
    steps:  
      \- name: Checkout Repository  
        uses: actions/checkout@v4

      \- name: Run OpenHands Resolver  
        \# 公式のOpenHands Resolver Actionまたは互換性のあるActionを指定  
        \# 例: All-Hands-AI/OpenHands/.github/actions/openhands-resolver@main  
        \# または xinbenlv/openhands-ai-action@v1.0.1-rc3 (プロンプトを直接渡す場合)  
        uses: All-Hands-AI/OpenHands/.github/actions/openhands-resolver@main \# または適切な参照  
        with:  
          issue-number: ${{ github.event.issue.number }}  
          \# LLM_API_KEY, PAT_TOKENなどはsecrets経由で渡される想定 \[14\]

このワークフローは、Issueへのコメントが @openhands-agent fix-me で始まる場合にトリガーされます。All-Hands-AI/OpenHands/.github/actions/openhands-resolver@main の部分は、公式の openhands-resolver.yml 14 を参照して適切に設定するか、xinbenlv/openhands-ai-action 18 を使用します。後者の場合、prompt 入力で直接タスクを渡すことが可能です。

#### **4.1.2. OpenHandsへのタスク定義 (プロンプト)**

タスクは、GitHubのIssueコメントやPull Requestコメント内で、自然言語プロンプトとしてOpenHandsエージェントに与えられます 16。

プロンプト例1 (情報収集):  
@openhands-agent fix-me 「https://www.example.com」にアクセスし、ページタイトルと主要な見出し（H1タグの内容）を抽出して、結果をこのIssueにコメントしてください。  
OpenHandsエージェントは、この指示に基づき、指定されたURLにアクセスし、要求された情報を取得するためのブラウザ操作（ナビゲーション、DOM解析など）を計画・実行します 1。  
プロンプト例2 (フォーム入力と送信):  
@openhands-agent fix-me 「https://example.com/login」にアクセスし、ユーザー名入力フィールド（name="username"）に「testuser」、パスワード入力フィールド（name="password"）に「testpass」と入力し、ログインボタン（type="submit"）をクリックしてください。ログイン後のページのURLを報告してください。  
このプロンプトでは、フォーム要素の特定（例: name属性）、テキスト入力、ボタンクリックといった一連の操作が指示されています。OpenHandsはBrowserGymの機能を利用してこれらの操作を試みます 1。  
プロンプト例3 (特定要素のテキスト抽出):  
@openhands-agent fix-me 「https://example.com/products/123」にアクセスし、価格情報が表示されている要素（例：id="product-price"）のテキストを抽出してください。  
特定の要素をターゲットとした情報抽出も可能です。プロンプトで要素の特定方法に関するヒント（例: id属性）を与えることで、エージェントの精度向上が期待できます。

#### **4.1.3. 期待される出力と成果物**

OpenHandsエージェントは、実行計画、実際に行ったアクション、そして観測結果（ブラウザの表示内容やエラーメッセージなど）を、トリガーとなったGitHub IssueやPull Requestにコメントとして投稿します 14。抽出されたデータや操作結果も同様にコメントで報告されます。

スクリーンショットのようなバイナリファイルや、抽出されたデータをまとめたテキストファイルなどは、GitHub Actionsの成果物（artifacts）としてアップロード・保存することが可能です 20。これには、OpenHandsエージェントに特定のパス（例: ${{ github.workspace }}/openhands_output/screenshots/）にファイルを保存するよう指示し、ワークフローの後続ステップで actions/upload-artifact アクションを使用してそのパスを指定します。OpenHandsのGitHub Issue \#8372 21 では、エージェントがスクリーンショットをワークスペースに保存する機能に関する議論と実装が進められており、将来的にはよりスムーズな成果物連携が期待されます。

**YAML例 (成果物アップロードステップ):**

YAML

      \# (OpenHands実行ステップの後に追加)  
      \- name: Upload Browser Automation Artifacts  
        uses: actions/upload-artifact@v4  
        with:  
          name: browser-output  
          path: |  
            ${{ github.workspace }}/openhands_output/screenshots/ \# OpenHandsがスクリーンショットを保存する想定パス  
            ${{ github.workspace }}/openhands_output/extracted_data.txt \# OpenHandsが抽出データを保存する想定パス

### **4.2. シナリオ2：Playwright-MCPとの連携**

このシナリオでは、OpenHandsのカスタムサンドボックス内にPlaywright-MCPサーバーをセットアップし、OpenHandsエージェントがPlaywright-MCPの提供するツールを利用してブラウザ操作を行います。

#### **4.2.1. Playwright-MCPサーバーのセットアップ**

Playwright-MCPサーバーをOpenHandsのカスタムDockerイメージ内にインストールし、コンテナ起動時に実行されるように設定します。サーバーは npx @playwright/mcp@latest コマンドで起動できます 6。ポート番号や許可するオリジンなどの設定は、コマンドライン引数または config.json 設定ファイルで行います 6。

**Dockerfile内での起動例 (概念):**

Dockerfile

\# ベースイメージの指定 (例: Node.jsとPythonが利用可能なイメージ)  
FROM nikolaik/python-nodejs:python3.12\-nodejs22

\# Playwrightとその依存関係のインストール  
RUN npx playwright install \--with-deps

\# Playwright-MCPのインストール  
RUN npm install \-g @playwright/mcp@latest

\# OpenHandsのアプリケーションコードや依存関係のコピーとセットアップ  
\# (省略)

\# コンテナ起動時にMCPサーバーとOpenHandsアプリケーションを起動するスクリプト  
COPY start-services.sh /app/start-services.sh  
RUN chmod \+x /app/start-services.sh

CMD \["/app/start-services.sh"\]

start-services.sh の内容例:

Bash

\#\!/bin/sh  
\# Playwright-MCPサーバーをバックグラウンドで起動  
npx @playwright/mcp@latest \--port 8931 \--host 0.0.0.0 &  
\# OpenHandsアプリケーションをフォアグラウンドで起動 (実際の起動コマンドに置き換えてください)  
exec python \-m openhands.app.main

実際の起動方法は、OpenHandsのカスタムサンドボックスのアーキテクチャやエントリーポイントの設計に依存します。OpenHandsの runtime_extra_deps 15 やカスタム setup.sh 22 を利用して、サンドボックス初期化時にPlaywright-MCPサーバーをセットアップ・起動することも考えられます。

#### **4.2.2. OpenHandsカスタムサンドボックスの設定**

GitHub Actionsワークフローにおいて、OpenHands Resolverまたは関連アクションの OPENHANDS_BASE_CONTAINER_IMAGE 環境変数（または相当する入力）に、上記で作成したPlaywright-MCPを含むカスタムDockerイメージ名を指定します 15。

#### **4.2.3. OpenHandsへのタスク定義 (Playwright-MCPツール利用の指示)**

OpenHandsエージェントに対し、ローカル（サンドボックス内）で実行されているPlaywright-MCPサーバーのツールを使用するよう自然言語で指示します。これには、エージェントがMCPクライアントとして動作し、適切なHTTPリクエスト（JSON-RPC形式など）を localhost:PORT（MCPサーバーがリッスンしているポート）に送信するコードを生成・実行することが含まれます。

プロンプトは、達成したい高レベルのブラウザ操作目標（例: 「ウェブサイトにログインする」）を記述するとともに、その達成のためにPlaywright-MCPの特定のツール（例: browser_type でユーザー名を入力）を利用するようエージェントを誘導する必要があります。これは、OpenHandsを支えるLLMが、ウェブ操作を理解するだけでなく、特定のツールセット（この場合はMCPツール）の存在とそれらの適切な順序付けを理解する必要があることを意味します。このアプローチは、エージェントがツールの説明に基づいて任意のAPIやツールキットを活用できるようになるための一歩と言えます。

プロンプト例1 (MCPツールでのナビゲーションとスナップショット):  
@openhands-agent fix-me Playwright-MCPサーバーの browser_navigate ツールを使い「https://www.example.com」にアクセスし、その後 browser_snapshot ツールでアクセシビリティスナップショットを取得してください。取得したスナップショットの内容を要約して報告してください。MCPサーバーはlocalhost:8931で動作しています。  
このプロンプトでは、エージェントにPlaywright-MCPの具体的なツール名 (browser_navigate, browser_snapshot) と、それらが動作するエンドポイント (localhost:8931) を指示しています 6。  
プロンプト例2 (MCPツールでの要素クリックと入力):  
@openhands-agent fix-me Playwright-MCPサーバー（localhost:8931）を使い、「https://example.com/login」に移動してください。次に、要素「username-input」のrefを持つ要素に browser_type ツールで「mcp_user」と入力し、要素「password-input」のrefを持つ要素に「mcp_pass」と入力してください。最後に要素「login-button」のrefを持つ要素を browser_click ツールでクリックし、結果を報告してください。  
ここでは、要素の ref (アクセシビリティスナップショットから得られる一意な参照ID) を利用した精密な要素操作を指示しています。これにより、視覚的な曖昧さを排除した確実なインタラクションが期待できます 6。

#### **4.2.4. ワークフロー例**

基本的なワークフロー構造はシナリオ1と類似しますが、OPENHANDS_BASE_CONTAINER_IMAGE でPlaywright-MCPを含むカスタムイメージを指定する点が主な違いとなります。

**YAML例 (一部抜粋):**

YAML

jobs:  
  run_openhands_mcp_task:  
    \#... (if, runs-on, checkout steps はシナリオ1と同様)...  
    env:  
      OPENHANDS_BASE_CONTAINER_IMAGE: "my-registry/my-openhands-with-mcp:latest" \# カスタムイメージ  
      LLM_API_KEY: ${{ secrets.LLM_API_KEY }}  
      \#... (その他のOpenHands Resolverに必要な環境変数)  
    steps:  
      \#... (Checkout step)...  
      \- name: Run OpenHands Resolver with Custom Sandbox  
        uses: All-Hands-AI/OpenHands/.github/actions/openhands-resolver@main \# または適切な参照  
        with:  
          issue-number: ${{ github.event.issue.number }}  
      \#... (成果物アップロードステップはシナリオ1と同様)...

### **4.3. Playwright-MCPブラウザ操作ツール一覧**

Playwright-MCPは、ブラウザ操作のための多様なツールを提供します。これらのツールを理解することは、OpenHandsエージェントに適切な指示を与える上で非常に重要です。以下に主要なツールを示します。

**Table 2: Playwright-MCPブラウザ操作ツール例**

| ツール名 (Tool Name) | 説明 (Description) | 主要パラメータ (Key Parameters) | 利用モード (Mode) | 読取専用 (Read-only) |
| :---- | :---- | :---- | :---- | :---- |
| browser_navigate | 指定されたURLにナビゲートします。 | url (string): ナビゲート先のURL。 | Snapshot/Vision | False |
| browser_click | ウェブページ上の要素をクリックします。 | element (string): 要素の人間可読な説明。\<br\>ref (string): ページスナップショットからの正確なターゲット要素参照。 | Snapshot | False |
| browser_type | 編集可能な要素にテキストを入力します。 | element (string): 要素の説明。\<br\>ref (string): 要素参照。\<br\>text (string): 入力するテキスト。\<br\>submit (boolean, optional): 入力後にEnterキーを押すか。\<br\>slowly (boolean, optional): 1文字ずつ入力するか。 | Snapshot | False |
| browser_select_option | ドロップダウンでオプションを選択します。 | element (string): 要素の説明。\<br\>ref (string): 要素参照。\<br\>values (array): 選択する値の配列。 | Snapshot | False |
| browser_snapshot | 現在のページのアクセシビリティスナップショットを取得します。 | なし | Snapshot | True |
| browser_take_screenshot | 現在のページまたは特定要素のスクリーンショットを撮ります。 | raw (boolean, optional): 非圧縮PNGで返すか。\<br\>filename (string, optional): 保存ファイル名。\<br\>element (string, optional): 要素の説明。\<br\>ref (string, optional): 要素参照。 | Snapshot/Vision | True |
| browser_wait_for | 指定したテキストが出現または消失するのを待つか、指定時間待機します。 | time (number, optional): 待機時間(秒)。\<br\>text (string, optional): 出現を待つテキスト。\<br\>textGone (string, optional): 消失を待つテキスト。 | Snapshot/Vision | True |
| browser_screen_click | 指定されたX,Y座標でマウスクリックを実行します（ビジョンモード）。 | element (string): 要素の説明。\<br\>x (number): X座標。\<br\>y (number): Y座標。 | Vision | False |
| browser_file_upload | ファイルをアップロードします。 | files (array): アップロードするファイルの絶対パスの配列。 | Snapshot/Vision | False |

*データソース: 6*

この表は、Playwright-MCPが提供するコマンドセットの一部を示しており、ユーザーがブラウザをどの程度の粒度で制御できるかを理解するのに役立ちます。これにより、より効果的なタスク定義（プロンプト作成）が可能になります。

ブラウザ操作の自動化において、テキストベースのログだけでは不十分な場合が多く、視覚的なフィードバック（スクリーンショットなど）や構造化されたデータ出力が不可欠です。GitHub Actionsの成果物管理機能 20 を活用し、これらの情報をPRコメントにリンクするなどして、エージェントの作業内容をデバッグし検証可能にすることが、自動化の実用性を高める上で極めて重要となります。OpenHandsのIssue 21で議論されているスクリーンショット保存機能は、まさにこのニーズに応えるものです。

## **5\. 詳細設定ガイド**

OpenHandsとPlaywright-MCPを連携させるための詳細な設定項目について解説します。設定は、GitHub Actionsワークフローレベル、OpenHandsアプリケーションレベル、カスタムDockerイメージレベル、そしてPlaywright-MCPサーバーレベルと多岐にわたります。これらの設定レイヤーがどのように相互作用するかを理解することが、安定した自動化環境を構築する鍵となります。

### **5.1. OpenHands GitHub Actionの設定**

OpenHands Resolverや xinbenlv/openhands-ai-action を使用する際の主要な設定項目です。

* **認証情報 (Secrets):** GitHubリポジトリの Settings \> Secrets and variables \> Actions で設定します。  
  * LLM_API_KEY: 使用するLLMプロバイダー（Anthropic Claude, OpenAI GPTなど）のAPIキー。必須項目です 14。  
  * PAT_USERNAME (オプション): GitHubパーソナルアクセストークン（PAT）に関連付けられたユーザー名 14。  
  * PAT_TOKEN (オプション): OpenHandsがリポジトリにアクセスし、ブランチ作成やPR作成を行うために必要なGitHub PAT。contents, issues, pull_requests, workflows のスコープが必要です 14。  
* **環境変数と入力 (Environment Variables and Inputs):** ワークフローファイル内で env: ブロックや with: ブロックを使用して設定します。  
  * LLM_MODEL: OpenHandsエージェントが使用する具体的なLLMモデル名（例: anthropic/claude-3-5-sonnet-20240620, openai/gpt-4o）。プロバイダーとモデルの組み合わせを指定します 16。  
  * OPENHANDS_MAX_ITER: エージェントが一つのタスクに対して実行する思考とアクションの最大回数。無限ループを防ぐために設定します 16。  
  * OPENHANDS_BASE_CONTAINER_IMAGE: OpenHandsエージェントが動作するサンドボックスのベースとなるDockerイメージ。Playwright-MCPを導入する場合など、カスタムイメージを指定する際に使用します 15。  
  * TARGET_BRANCH: OpenHandsが作成した変更をマージするためのPRのターゲットブランチ。デフォルトはリポジトリのメインブランチです 16。  
  * xinbenlv/openhands-ai-action を使用する場合の主な入力:  
    * prompt (必須): エージェントに実行させたいタスクを自然言語で記述します 18。  
    * runtime_image: OpenHandsランタイム用のDockerイメージを指定します 18。  
    * openhands_image: OpenHands本体のサービス用Dockerイメージを指定します 18。  
    * additional_env: JSON形式で追加の環境変数をコンテナに渡すことができます 18。  
* **ワークフロー権限 (Workflow Permissions):** リポジトリの Settings \> Actions \> General で設定します。  
  * Workflow permissions: 「Read and write permissions」を選択します。  
  * 「Allow GitHub Actions to create and approve pull requests」を有効化します。これにより、OpenHandsが自動でPRを作成できるようになります 14。  
* **カスタム指示 (.openhands/microagents/repo.md):** リポジトリのルートディレクトリに .openhands/microagents/repo.md というマークダウンファイルを配置することで、そのリポジトリでOpenHandsエージェントが動作する際の共通の指示やコンテキスト（例: プロジェクトの概要、主要なファイル構造、コーディング規約など）を提供できます。これにより、エージェントの行動をよりリポジトリに適したものに調整できます 14。

### **5.2. Playwright-MCPサーバーの設定**

Playwright-MCPサーバーは、コマンドライン引数またはJSON設定ファイルで詳細な動作を制御できます。

* **コマンドライン引数 (Command-Line Arguments):** npx @playwright/mcp@latest \--help で利用可能な全引数を確認できます 6。  
  * \--browser \<browser_name\>: 使用するブラウザを指定します（例: chromium, firefox, webkit, または msedge, chrome などのチャンネル名）23。  
  * \--port \<port_number\>: MCPサーバーがリッスンするポート番号を指定します。デフォルト以外を使用する場合に設定します 23。  
  * \--host \<ip_address\>: サーバーがバインドするホストアドレス。デフォルトは localhost ですが、コンテナ環境などでは 0.0.0.0 を指定して全てのインターフェースでリッスンさせることが一般的です 6。  
  * \--headless: ブラウザをヘッドレスモードで起動します。CI環境では通常有効にします 23。  
  * \--allowed-origins \<origins\>: ブラウザからのリクエストを許可するオリジンのリストをセミコロン区切りで指定します。デフォルトは全て許可です 6。  
  * \--vision: スクリーンショットベースのビジョンモードを有効にします。デフォルトはアクセシビリティスナップショットモードです 6。  
  * \--config \<path/to/config.json\>: 設定ファイルへのパスを指定します 6。  
* **JSON設定ファイル (JSON Configuration File):** コマンドライン引数よりも詳細な設定が可能です。--config オプションでこのファイルを指定します。スキーマの詳細はPlaywright-MCPのドキュメントやソースコードで確認できますが、主要な設定項目には以下のようなものがあります 6。  
  * browser: ブラウザ関連の設定 (browserName, launchOptions (例: headless: true), contextOptions (例: viewport) など)。  
  * server: サーバー関連の設定 (port, host など)。  
  * capabilities: 有効にする機能のリスト（例: core, tabs, pdf, history, wait, files）。  
  * vision: ビジョンモードの有効/無効。  
  * outputDir: スクリーンショットなどの出力先ディレクトリ。  
  * **設定例 (サーバー直接設定ファイル):**  
    JSON  
    {  
      "server": {  
        "port": 8931,  
        "host": "0.0.0.0"  
      },  
      "browser": {  
        "browserName": "chromium",  
        "headless": true,  
        "launchOptions": {},  
        "contextOptions": {  
          "viewport": { "width": 1280, "height": 720 }  
        }  
      },  
      "capabilities": \["core", "tabs", "pdf", "history", "wait", "files"\],  
      "vision": false,  
      "outputDir": "/tmp/playwright_mcp_output"  
    }

### **5.3. Dockerによるカスタム環境構築**

Playwright-MCPをOpenHandsのサンドボックス内で利用するためには、カスタムDockerイメージの構築が必要です。

* **Dockerfileの作成:**  
  1. **ベースイメージの選択:** OpenHandsが推奨するサンドボックスのベースイメージ（Debianベースであることが多い 15）や、Node.jsとPython環境がプリインストールされたイメージ（例: nikolaik/python-nodejs:python3.12-nodejs22 15）を選択します。  
  2. **Playwrightのインストール:** npx playwright install \--with-deps コマンドを実行し、指定ブラウザのエンジンと必要なOS依存関係をインストールします 15。  
  3. **Playwright-MCPのインストール:** npm install \-g @playwright/mcp@latest コマンドでPlaywright-MCPサーバーをグローバルにインストールします 6。  
  4. **その他の依存関係:** OpenHandsエージェントが必要とするその他のライブラリやツールをインストールします。  
  5. **起動スクリプトの設定:** コンテナ起動時にOpenHandsアプリケーションとPlaywright-MCPサーバーの両方を起動するスクリプト（例: start-services.sh）を用意し、CMD または ENTRYPOINT で指定します。  
  * Dockerfileの一般的な作成方法については 24 が参考になります。  
* **GitHub Actionsでのカスタムイメージ利用:**  
  1. 作成したDockerfileを使用してDockerイメージをビルドします (docker build \-t my-registry/my-openhands-with-mcp:latest.)。  
  2. ビルドしたイメージをDocker HubやGitHub Container Registry (GHCR) などのコンテナレジストリにプッシュします。  
  3. GitHub Actionsワークフローファイル内で、OpenHands Resolverを使用する場合は OPENHANDS_BASE_CONTAINER_IMAGE 環境変数にプッシュしたイメージ名（例: my-registry/my-openhands-with-mcp:latest）を指定します 16。  
  4. xinbenlv/openhands-ai-action を使用する場合は、runtime_image や openhands_image 入力にカスタムイメージ名を指定できます 18。  
  5. 一般的なDockerコンテナアクションとして実行する場合は、ジョブの container ディレクティブでイメージを指定することも可能です 24。

### **5.4. 設定パラメータ一覧表**

以下に、OpenHands GitHub ActionとPlaywright-MCPサーバーの主要な設定パラメータをまとめます。

**Table 3: 主要設定パラメータ**

| ツール (Tool) | パラメータ名 (Parameter Name) | 説明 (Description) | 設定方法 (How to Set) | 使用例 (Example Value) |
| :---- | :---- | :---- | :---- | :---- |
| OpenHands GitHub Action (Resolver) | LLM_API_KEY | LLMサービスのAPIキー。 | Workflow Secret | ${{ secrets.LLM_API_KEY }} |
| OpenHands GitHub Action (Resolver) | LLM_MODEL | 使用するLLMモデル。 | Workflow Env Var / Secret | anthropic/claude-3-5-sonnet-20240620 |
| OpenHands GitHub Action (Resolver) | OPENHANDS_BASE_CONTAINER_IMAGE | カスタムサンドボックスイメージ。 | Workflow Env Var / Secret | my-registry/my-openhands-with-mcp:latest |
| OpenHands GitHub Action (Resolver) | PAT_TOKEN | GitHubリポジトリアクセス用PAT。 | Workflow Secret | ${{ secrets.GH_PAT }} |
| xinbenlv/openhands-ai-action | prompt | エージェントへの自然言語タスク指示。 | Workflow Input | "「example.com」から価格情報を抽出してください。" |
| Playwright-MCP Server | \--port \<number\> | サーバーがリッスンするポート。 | MCP CLI Arg / MCP JSON Key (server.port) | 8931 |
| Playwright-MCP Server | \--browser \<name\> | 使用するブラウザ。 | MCP CLI Arg / MCP JSON Key (browser.browserName) | chromium |
| Playwright-MCP Server | \--headless | ヘッドレスモードで起動。 | MCP CLI Arg / MCP JSON Key (browser.headless) | (引数のみ、または true) |
| Playwright-MCP Server | \--allowed-origins \<origins\> | 許可するオリジン。 | MCP CLI Arg / MCP JSON Key (network.allowedOrigins) | \* または https://example.com |
| Playwright-MCP Server | \--vision | ビジョンモードを有効化。 | MCP CLI Arg / MCP JSON Key (vision) | (引数のみ、または true) |
| Playwright-MCP Server | \--config \<path\> | 設定ファイルパス。 | MCP CLI Arg | config/mcp_server_config.json |

CI/CDパイプラインにおける自動化では、セキュリティが最優先事項です。APIキーやパーソナルアクセストークンなどの機密情報は、必ずGitHub Secretsのような安全な場所に保管し、ワークフローからは参照する形でのみ利用してください 14。また、サンドボックス環境（Docker）の利用 1 や、ワークフローの実行権限の適切な管理 14 も、意図しない副作用やセキュリティリスクを低減するために不可欠です。特に、コンテナ内からホストOS上のサービス（例: ローカルで実行中のLLMサーバー）にアクセスするために host.docker.internal 27 を利用する際は、ネットワークの露出範囲に十分注意する必要があります。

## **6\. 高度な考慮事項**

OpenHands、GitHub Actions、Playwright-MCPを用いたブラウザ操作自動化を実践する上で、エラーハンドリング、セキュリティ、動的コンテンツへの対応、そしてパフォーマンスといった高度な側面を考慮することが、より堅牢で実用的なシステムを構築するために重要となります。

### **6.1. エラーハンドリングとデバッグ戦略**

AIエージェントが関与する自動化システムのデバッグは、従来のコードデバッグとは異なる側面を持ちます。エージェントの「思考プロセス」（LLMへのプロンプトとLLMからの応答）、実行したアクション、環境の状態（ブラウザのDOM、スクリーンショットなど）、そして最終的な結果を総合的に把握する必要があります。

* **OpenHands:** エージェントの思考過程、実行アクション、発生したエラーは、OpenHandsのWeb UI（利用可能な場合）やコンソールログで確認できます 1。GitHub Actionsの実行ログも、特にセットアップや連携部分の問題解決に不可欠です。LOG_ALL_EVENTS=true のような環境変数を設定することで、より詳細なイベントログを取得できます 1。  
* **Playwright-MCP:** Playwright-MCPサーバー自体のログを確認し、起動時オプションや設定ファイルに誤りがないかを確認します。OpenHandsエージェントが生成したMCPクライアントコード側では、MCPサーバーからのレスポンスコードをチェックし、エラーメッセージを適切に処理するロジックを組み込むようエージェントに指示する必要があります。  
* **GitHub Actions:** ワークフローの各ステップの実行ログは、GitHubのActionsタブから詳細に確認できます。actions/upload-artifact 20 を利用して、デバッグに有用な詳細ログファイル、Playwrightのトレースファイル、エラー発生時のスクリーンショットなどを成果物として保存し、後から分析できるようにすることが推奨されます。OpenHandsのIssue \#8372 21 で議論されているように、エージェントが取得したスクリーンショットを成果物としてアップロードする仕組みは、デバッグ効率を大幅に向上させます。  
* **一般的な戦略:**  
  * **段階的アプローチ:** 最初は単純なタスク（例: 特定の静的ページへのアクセスとタイトル取得）から始め、成功を確認しながら徐々に複雑なタスク（例: 複数ページ遷移、フォーム入力、動的コンテンツ操作）へと移行します。  
  * **タイムアウト設定:** 外部サービスへのアクセスや時間のかかるブラウザ操作には、適切なタイムアウト値を設定し、無限待機を防ぎます。  
  * **リトライメカニズム:** ネットワークの一時的な不安定さや、要素の読み込み遅延などによる失敗を許容するため、限定的なリトライ処理を組み込むことを検討します。OpenHands自体にもLLM呼び出しのリトライ機構があります 29。  
  * **明確なプロンプト:** エラー発生時には、エージェントがエラーメッセージを正確に解釈し、適切な修正行動を取れるよう、具体的で明確なプロンプトを与えることが重要です。

### **6.2. セキュリティに関する考慮事項**

自動化ワークフロー、特にCI/CDパイプラインに組み込む場合、セキュリティは最優先で考慮すべき事項です。

* **APIキーとトークンの管理:** LLMのAPIキーやGitHubのパーソナルアクセストークン（PAT）などの機密情報は、必ずGitHub Secretsに保存し、ワークフロー内では ${{ secrets.MY_API_KEY }} のように参照します 14。ハードコーディングは絶対に避けてください。PATに付与するスコープは、OpenHandsが必要とする最小限（例: contents, issues, pull_requests, workflows 14）に限定します。  
* **サンドボックス環境の徹底:** OpenHandsは、エージェントの操作をDockerコンテナ内のサンドボックス環境に隔離することで、ホストシステムへの意図しない影響を防ぎます 1。Playwright-MCPを導入するためにカスタムサンドボックスイメージを構築する場合も、ベースイメージの選択や追加するソフトウェアに関してセキュリティを十分に考慮し、不要な権限を与えないようにします。  
* **ワークフローの実行権限:** GitHub Actionsのワークフローが必要とする権限（リポジトリへの書き込み、PR作成など）は、リポジトリ設定で適切に管理します 14。特に、外部コントリビューターからのPull Requestによってトリガーされるワークフローの実行は、セキュリティリスクを伴うため、手動承認を必須にするなどの対策を検討します 26。  
* **ネットワークアクセス制御:** Playwright-MCPサーバーをコンテナ内で実行し、OpenHandsエージェントがそのコンテナ内のサーバーにアクセスする場合、通常は localhost またはコンテナネットワーク内のアドレスで通信が完結します。もし何らかの理由でPlaywright-MCPサーバーをホストOSや外部ネットワークに公開する必要がある場合は、ファイアウォール設定や認証・認可メカニズムを慎重に検討し、不正アクセスを防ぐ必要があります。

### **6.3. 動的コンテンツと複雑なインタラクションへの対応**

現代のWebアプリケーションは動的なコンテンツが多く、ユーザーインタラクションも複雑化しています。これらに対応するためには、自動化ツールとエージェントの双方が高度な能力を持つ必要があります。

* **OpenHands (BrowserGymベース):** OpenHandsが内部的に利用するBrowserGymはPlaywrightを基盤としているため、Playwright自体が持つ動的コンテンツへの対応能力（例: Auto-wait機能）をある程度継承しています 2。しかし、エージェントがLLMを介してこれらの機能を間接的に利用するため、プロンプトの工夫が重要になります。例えば、「ボタンが表示されるまで待ってからクリックしてください」といった明示的な待機指示や、要素の特定が難しい場合にはXPathやCSSセレクタのヒントをプロンプトに含めることが有効です。  
* **Playwright-MCP:**  
  * browser_wait_for ツールを使用することで、特定のテキストや要素が出現するまで、または消えるまで待機させることができます 6。これは、非同期に読み込まれるコンテンツへの対応に役立ちます。  
  * **スナップショットモード** 6 は、アクセシビリティツリーに依存するため、このツリーが頻繁かつ大幅に変更されるような高度にインタラクティブなサイト（例: シングルページアプリケーションの一部）では、要素の参照 (ref) が不安定になる可能性があります。  
  * **ビジョンモード** 6 は、スクリーンショットに基づいて操作を行うため、アクセシビリティ情報が不十分なカスタムUI要素やグラフィカルな要素の操作には有効な場合があります。しかし、レイアウトの僅かな変更で座標がずれやすく、一般にスナップショットモードよりも信頼性が低下する傾向があります。  
* **対応戦略:**  
  * **適切な待機処理の組み込み:** 要素の存在確認、表示確認、操作可能状態の確認など、適切な待機処理をエージェントの行動計画に含めるよう指示します。  
  * **複数のセレクタ戦略:** 一つのセレクタで要素を特定できない場合に備え、代替となるセレクタ（ID、name属性、クラス名、テキスト内容、XPathなど）をエージェントが試行できるよう、プロンプトで柔軟性を持たせることが考えられます。  
  * **状態変化の監視:** 特定のアクション後に期待される状態変化（例: URLの変更、特定テキストの表示）を確認するステップを指示に含めます。  
  * **タスクの分割:** 非常に複雑なインタラクションは、複数の小さなステップに分割し、各ステップの成功を確認しながら進めるようエージェントに指示します。

自動化の粒度と堅牢性の間にはトレードオフが存在します。Playwright-MCPは ref を用いた要素指定など、非常に細かい粒度での制御を提供し、これはUIが安定している場合には強力です 6。一方で、UIが頻繁に変更される環境では、このような精密な指定が逆に自動化を脆くする可能性があります。LLMを活用するOpenHandsのようなエージェントに対して、より高レベルで目標指向の指示を与えることで、LLMが多少のUI変更に適応し、より堅牢な自動化が実現できるかもしれません。これは、各操作を直接制御する代わりに、エージェントの適応能力に期待するアプローチです。

### **6.4. パフォーマンスとスケーラビリティ**

* **GitHub Actionsランナー:** ワークフローの実行速度は、GitHub Actionsが提供するランナーの性能に依存します。より高性能なランナーを選択することで改善が見込める場合があります。  
* **LLMの応答速度:** OpenHandsエージェントの思考プロセスはLLMへの複数回の問い合わせを伴うため、LLMの応答速度が全体のパフォーマンスに大きく影響します。  
* **Playwright-MCPサーバー:** ローカルまたはコンテナ内で単一のエージェントから利用する場合は通常問題になりませんが、もし複数のクライアントからの同時接続を想定するような構成（本レポートの主眼ではありませんが、Playwright-MCPの一般的な議論として 31 で言及あり）では、サーバーリソースや処理能力がボトルネックになる可能性があります。  
* **タスクの複雑性:** 多数のブラウザ操作を伴う複雑なタスクや、多数のページ遷移を含むタスクは、必然的に実行時間が長くなります。タスクのスコープを適切に設定することが重要です。

Playwright-MCPのようなエージェントとツール間の対話プロトコルの標準化は、今後のAIエージェント開発において重要なテーマです 8。OpenHandsとPlaywright-MCPの連携は、AIエージェントが様々なツールやAPIを発見し、理解し、利用するための標準化された方法への需要を示唆しています。今後、このようなプロトコルがさらに発展・普及し、AIが活用できるツールやサービスのエコシステムが拡大していくことが期待されます。

## **7\. 結論と推奨事項**

### **7.1. 総括**

本調査の結果、OpenHands、GitHub Actions、およびPlaywright-MCPを連携させることによるワークフロー内でのブラウザ操作自動化は、技術的に実現可能であることが確認されました。  
OpenHandsの標準的なブラウザ操作機能（BrowserGymベース）でも、GitHub Actionsを介して基本的なWebタスクを実行できます 1。これは比較的導入が容易なアプローチです。  
一方、OpenHandsのカスタムサンドボックス内にPlaywright-MCPサーバーを導入し、OpenHandsエージェントをMCPクライアントとして機能させることで、より詳細かつ堅牢なブラウザ制御が期待できます 6。このアプローチはセットアップの複雑性が増しますが、アクセシビリティツリーを活用した精密な要素特定や、Playwrightの豊富な機能を間接的に利用できるメリットがあります。

### **7.2. 各アプローチの推奨利用シナリオ**

* **OpenHands標準機能 (BrowserGymベース) の利用:**  
  * 比較的単純な情報収集（例: 特定ページのタイトル取得、特定要素のテキスト抽出）。  
  * 基本的なフォーム入力と送信。  
  * E2Eテストの簡単な補助タスク。  
  * 迅速に導入し、OpenHandsエージェントの汎用的な自然言語理解能力とタスク解決能力をWebブラウジングに応用したい場合に適しています。  
* **OpenHandsとPlaywright-MCPの連携:**  
  * 複雑なWebアプリケーションにおける精密な操作シーケンスの自動化。  
  * JavaScriptによって動的に変化するコンテンツへのより高度な対応。  
  * アクセシビリティツリー情報（要素の ref など）を活用した、CSSセレクタやXPathの変更に強い堅牢な要素特定が求められるテストや自動化タスク。  
  * 既存のPlaywrightの知見やテスト資産を活かしつつ、LLMによる柔軟なタスク指示を組み合わせたい場合に有効です。

### **7.3. 今後の展望と発展可能性**

* **OpenHandsエージェントのMCPクライアント機能の標準サポート:** 現在はカスタムセットアップが必要ですが、将来的にはOpenHandsエージェントが標準でMCPクライアントとして動作し、Playwright-MCPサーバーなどの外部ツールと容易に連携できるようになることが期待されます。  
* **高度なビジュアルベースブラウザ操作の統合:** OpenHandsの VisualBrowsingAgent 12 やPlaywright-MCPのビジョンモード 6 がさらに進化し、アクセシビリティ情報だけでは対応が難しいUI要素の操作や、視覚的な確認タスクの自動化精度が向上する可能性があります。  
* **GitHub Actionsマーケットプレイスの充実:** より洗練されたOpenHands連携GitHub Actionが登場し、ワークフローへの組み込みや設定がさらに簡素化される可能性があります。  
* **AIエージェントによるテスト自動化の進化:** ブラウザ操作自動化技術とLLMの組み合わせは、テストケースの自動生成、実行結果に基づく自己修復型テスト、自然言語によるテストシナリオ記述など、テスト自動化の分野に大きな変革をもたらす可能性があります。

### **7.4. 最終的な推奨事項**

1. **段階的アプローチの採用:** まずはOpenHandsの標準機能とGitHub Actionsの連携から始め、基本的なブラウザ操作タスクの自動化を試みることを推奨します。これにより、セットアップのハードルを低く抑えつつ、OpenHandsエージェントの能力と限界を把握できます。その上で、より高度な制御や堅牢性が求められる特定のユースケースに対して、Playwright-MCPの導入を検討するのが現実的です。この段階的な導入は、新しい技術をスムーズに組織に取り込む上で効果的です。  
2. **プロンプトエンジニアリングへの注力:** OpenHandsエージェントの性能は、与えられる自然言語プロンプトの質に大きく依存します 19。タスクの目的、操作対象、期待する結果を具体的かつ明確に記述することが、自動化の成功率を高める鍵となります。特にPlaywright-MCPのツールを利用させる場合は、どのツールをどのように使うべきかまで示唆するような、より詳細なプロンプト設計が求められます。プロンプトエンジニアリングは、LLMを活用した高度な自動化システムを使いこなす上で中心的なスキルとなります。  
3. **セキュリティ対策の徹底:** APIキーやパーソナルアクセストークンの安全な管理（GitHub Secretsの利用 14）、サンドボックス環境（Docker 1）の適切な運用、ワークフロー実行権限の最小化 14 など、セキュリティ対策は常に最優先事項としてください。自動化ワークフローがアクセスできる範囲や権限を慎重に検討し、潜在的なリスクを低減するための措置を講じることが不可欠です。

これらの推奨事項に従うことで、OpenHands、GitHub Actions、Playwright-MCPを活用したブラウザ操作自動化の導入を、より安全かつ効果的に進めることができるでしょう。

## **8\. 付録**

### **A. BrowserGymアクションスペース詳細**

OpenHandsが内部的にブラウザ操作を行う際に利用するBrowserGymは、Playwrightをベースとしたアクションセットを提供します。これらのアクションは、OpenHandsエージェントがLLMを通じて解釈し、実行する基本的なブラウザ操作コマンドとなります。以下に、BrowserGymの主要なアクションとその概要、一般的なパラメータ、そして対応するPlaywrightの機能を示します。この情報は、OpenHandsの標準機能でブラウザ操作を行う際のプロンプト作成や、エージェントの動作理解の助けとなります。

**Table 4: BrowserGym主要アクションとPlaywrightマッピング例**

| BrowserGymアクション (Action) | 説明 (Description) | パラメータ例 (Example Parameters) | Playwright機能例 (Corresponding Playwright Function(s)) |
| :---- | :---- | :---- | :---- |
| goto | 指定されたURLに移動します。 | url (string) | page.goto() |
| click | 指定された要素をクリックします。 | bid (string, 要素ID), button (string, "left"/"right"/"middle"), modifiers (list,) | element.click() |
| fill / type | 指定された入力フィールドにテキストを入力します。 | bid (string, 要素ID), text (string) | element.fill(), element.type() |
| select_option | ドロップダウンリストからオプションを選択します。 | bid (string, 要素ID), options (string or list) | element.select_option() |
| press | 指定されたキーまたはキーの組み合わせを押します。 | bid (string, 要素ID), key_comb (string, 例: "Enter", "Control+C") | element.press() |
| focus | 指定された要素にフォーカスします。 | bid (string, 要素ID) | element.focus() |
| clear | 入力フィールドの内容をクリアします。 | bid (string, 要素ID) | element.clear() |
| scroll | ページを指定された量だけスクロールします。 | delta_x (float), delta_y (float) | page.mouse.wheel() |
| mouse_move | マウスカーソルを指定された座標に移動します。 | x (float), y (float) | page.mouse.move() |
| mouse_down / mouse_up | マウスボタンを押す/離す操作。 | x (float), y (float), button (string) | page.mouse.down(), page.mouse.up() |
| drag_and_drop | ある要素から別の要素へドラッグ＆ドロップします。 | from_bid (string), to_bid (string) | element.drag_to() (または mouse.down/move/up の組み合わせ) |
| go_back | ブラウザの履歴を一つ戻ります。 | なし | page.go_back() |
| go_forward | ブラウザの履歴を一つ進みます。 | なし | page.go_forward() |
| take_screenshot | 現在のページのスクリーンショットを撮ります。 | (パラメータはBrowserGymの実装による) | page.screenshot() |
| send_msg_to_user | ユーザーにメッセージを送信します（エージェントからの情報提供用）。 | text (string) | (BrowserGym内部機能) |

データソース: 13 (BrowserGymのアクション関数の定義を参照)  
注: bid はBrowserGym内部で要素を識別するためのID（BrowserGym ID）を指すことが一般的です。パラメータの詳細はBrowserGymの具体的な実装やバージョンによって異なる場合があります。

### **B. 参考資料とリンク集**

* **OpenHands:**  
  * 公式ドキュメント: [https://docs.all-hands.dev/](https://docs.all-hands.dev/) 32  
  * GitHubリポジトリ: [https://github.com/All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) 33  
  * OpenHands Resolver README:(https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/resolver/README.md) 14  
* **Playwright-MCP:**  
  * GitHubリポジトリ: [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) 6  
* **BrowserGym:**  
  * 公式ドキュメント: [https://browsergym.readthedocs.io/](https://browsergym.readthedocs.io/) 34  
  * GitHubリポジトリ:(https://github.com/ServiceNow/BrowserGym) 35  
* **GitHub Actions:**  
  * 公式ドキュメント: [https://docs.github.com/actions](https://docs.github.com/actions) 30  
  * Dockerコンテナアクションの作成: [https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action) 24  
  * 成果物の保存: [https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts](https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts) 20  
* **その他関連資料:**  
  * OpenHandsの概要とインストール (apidog.com): [https://apidog.com/blog/openhands-the-open-source-devin-ai-alternative/](https://apidog.com/blog/openhands-the-open-source-devin-ai-alternative/) 1  
  * Playwright-MCPの解説 (codoid.com): [https://codoid.com/automation-testing/playwright-mcp-expert-strategies-for-success/](https://codoid.com/automation-testing/playwright-mcp-expert-strategies-for-success/) 8  
  * Playwright-MCPのモード解説 (huggingface.co): [https://huggingface.co/blog/lynn-mikami/microsoft-playwright-mcp](https://huggingface.co/blog/lynn-mikami/microsoft-playwright-mcp) 7

#### **引用文献**

1. OpenHands: The Open Source Devin AI Alternative \- Apidog, 5月 27, 2025にアクセス、 [https://apidog.com/blog/openhands-the-open-source-devin-ai-alternative/](https://apidog.com/blog/openhands-the-open-source-devin-ai-alternative/)  
2. openreview.net, 5月 27, 2025にアクセス、 [https://openreview.net/pdf/95990590797cff8b93c33af989ecf4ac58bde9bb.pdf](https://openreview.net/pdf/95990590797cff8b93c33af989ecf4ac58bde9bb.pdf)  
3. open-operator/open/openhands.md at main · All-Hands-AI/open-operator \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/All-Hands-AI/open-operator/blob/main/open/openhands.md](https://github.com/All-Hands-AI/open-operator/blob/main/open/openhands.md)  
4. System Architecture | OpenHands, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/architecture/backend](https://docs.all-hands.dev/modules/usage/architecture/backend)  
5. OpenHands : An Open Platform for AI Software Developers as Generalist Agents | PDF, 5月 27, 2025にアクセス、 [https://www.slideshare.net/slideshow/openhands-an-open-platform-for-ai-software-developers-as-generalist-agents/274830722](https://www.slideshare.net/slideshow/openhands-an-open-platform-for-ai-software-developers-as-generalist-agents/274830722)  
6. microsoft/playwright-mcp: Playwright MCP server \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)  
7. Microsoft Playwright MCP: Tutorial for Beginners \- Hugging Face, 5月 27, 2025にアクセス、 [https://huggingface.co/blog/lynn-mikami/microsoft-playwright-mcp](https://huggingface.co/blog/lynn-mikami/microsoft-playwright-mcp)  
8. Playwright MCP: Expert Strategies for Success \- Codoid Innovations, 5月 27, 2025にアクセス、 [https://codoid.com/automation-testing/playwright-mcp-expert-strategies-for-success/](https://codoid.com/automation-testing/playwright-mcp-expert-strategies-for-success/)  
9. Modern Test Automation With AI (LLM) and Playwright MCP \- DZone, 5月 27, 2025にアクセス、 [https://dzone.com/articles/modern-test-automation-ai-llm-playwright-mcp](https://dzone.com/articles/modern-test-automation-ai-llm-playwright-mcp)  
10. Playwright MCP \- Scraping Smithery MCP database Tutorial with Cursor \- ScrapingBee, 5月 27, 2025にアクセス、 [https://www.scrapingbee.com/blog/playwright-mcp-web-scraping-smithery-tutorial-cursor/](https://www.scrapingbee.com/blog/playwright-mcp-web-scraping-smithery-tutorial-cursor/)  
11. Using an MCP Server in GitHub Copilot, 5月 27, 2025にアクセス、 [https://markheath.net/post/2025/4/10/mcp-playwright](https://markheath.net/post/2025/4/10/mcp-playwright)  
12. openhands.agenthub.browsing_agent \- All Hands AI, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/python/openhands/agenthub/browsing_agent](https://docs.all-hands.dev/modules/python/openhands/agenthub/browsing_agent)  
13. BrowserGym/browsergym/core/src/browsergym/core/action/functions.py at main · ServiceNow/BrowserGym \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/ServiceNow/BrowserGym/blob/main/browsergym/core/src/browsergym/core/action/functions.py](https://github.com/ServiceNow/BrowserGym/blob/main/browsergym/core/src/browsergym/core/action/functions.py)  
14. OpenHands/openhands/resolver/README.md at main · All-Hands ..., 5月 27, 2025にアクセス、 [https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/resolver/README.md](https://github.com/All-Hands-AI/OpenHands/blob/main/openhands/resolver/README.md)  
15. Custom Sandbox | OpenHands, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide](https://docs.all-hands.dev/modules/usage/how-to/custom-sandbox-guide)  
16. Using the OpenHands GitHub Action \- All Hands AI, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/how-to/github-action](https://docs.all-hands.dev/modules/usage/how-to/github-action)  
17. OpenHands/.github/workflows/openhands-resolver.yml at main · All ..., 5月 27, 2025にアクセス、 [https://github.com/All-Hands-AI/OpenHands/blob/main/.github/workflows/openhands-resolver.yml](https://github.com/All-Hands-AI/OpenHands/blob/main/.github/workflows/openhands-resolver.yml)  
18. OpenHands AI Action \- GitHub Marketplace, 5月 27, 2025にアクセス、 [https://github.com/marketplace/actions/openhands-ai-action](https://github.com/marketplace/actions/openhands-ai-action)  
19. Prompting Best Practices | OpenHands, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/prompting/prompting-best-practices](https://docs.all-hands.dev/modules/usage/prompting/prompting-best-practices)  
20. Storing and sharing data from a workflow \- GitHub Docs, 5月 27, 2025にアクセス、 [https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts](https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts)  
21. Allow the agent to save a browser screenshot as an image · Issue \#8372 · All-Hands-AI/OpenHands \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/All-Hands-AI/OpenHands/issues/8372](https://github.com/All-Hands-AI/OpenHands/issues/8372)  
22. Repository Customization \- OpenHands \- All Hands AI, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/customization/repository](https://docs.all-hands.dev/modules/usage/customization/repository)  
23. Playwright Browser Automation \- MCP Server \- Magic Slides, 5月 27, 2025にアクセス、 [https://www.magicslides.app/mcps/microsoft-playwright-browser-automation](https://www.magicslides.app/mcps/microsoft-playwright-browser-automation)  
24. Creating a Docker container action \- GitHub Docs, 5月 27, 2025にアクセス、 [https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action](https://docs.github.com/en/actions/sharing-automations/creating-actions/creating-a-docker-container-action)  
25. Docker Container Action \- GitHub Marketplace, 5月 27, 2025にアクセス、 [https://github.com/marketplace/actions/docker-container-action](https://github.com/marketplace/actions/docker-container-action)  
26. How can a GitHub owner run and external PR through GitHub Actions? \- Stack Overflow, 5月 27, 2025にアクセス、 [https://stackoverflow.com/questions/77894343/how-can-a-github-owner-run-and-external-pr-through-github-actions](https://stackoverflow.com/questions/77894343/how-can-a-github-owner-run-and-external-pr-through-github-actions)  
27. \[Bug\]: LLM Connection Fails for Dockerized OpenHands to Host Ollama \- UI Settings Override \`host.docker.internal\` · Issue \#8318 \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/All-Hands-AI/OpenHands/issues/8318](https://github.com/All-Hands-AI/OpenHands/issues/8318)  
28. OpenHands Feature Overview \- All Hands AI, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/key-features](https://docs.all-hands.dev/modules/usage/key-features)  
29. Configuration Options \- OpenHands \- All Hands AI, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/modules/usage/configuration-options](https://docs.all-hands.dev/modules/usage/configuration-options)  
30. Understanding GitHub Actions, 5月 27, 2025にアクセス、 [https://docs.github.com/articles/getting-started-with-github-actions](https://docs.github.com/articles/getting-started-with-github-actions)  
31. Playwright MCP Server Explained: A Guide to Multi-Client Browser Automation \- QA Touch, 5月 27, 2025にアクセス、 [https://www.qatouch.com/blog/playwright-mcp-server/](https://www.qatouch.com/blog/playwright-mcp-server/)  
32. OpenHands | OpenHands, 5月 27, 2025にアクセス、 [https://docs.all-hands.dev/](https://docs.all-hands.dev/)  
33. Fullstack Open Source Projects That Will Help You Become AI Devs (Python, JavaScript, AI), 5月 27, 2025にアクセス、 [https://dev.to/fast/fullstack-open-source-projects-that-will-help-you-become-ai-devs-python-javascript-ai-4m9a](https://dev.to/fast/fullstack-open-source-projects-that-will-help-you-become-ai-devs-python-javascript-ai-4m9a)  
34. Welcome to BrowserGym's documentation\! \- Read the Docs, 5月 27, 2025にアクセス、 [https://browsergym.readthedocs.io/latest/](https://browsergym.readthedocs.io/latest/)  
35. BrowserGym, a Gym environment for web task automation \- GitHub, 5月 27, 2025にアクセス、 [https://github.com/ServiceNow/BrowserGym](https://github.com/ServiceNow/BrowserGym)