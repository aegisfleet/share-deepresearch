---
audio: /share-deepresearch/assets/audio/spec-kit-practical-guide.m4a
category: engineering
date: 2025-09-03
description: GitHubのSpec Kitを活用したAI駆動開発の実践的なガイドです。セットアップから具体的な使用例まで、詳細に解説します。
ga4_metrics:
  avgSessionDuration: 596.9091618
  pageViews: 5
  users: 3
layout: topic
prompt: GitHubのSpec Kitのハンズオン資料を作成したい。セットアップから実際の使用例を丁寧に解説して欲しい。
tags:
- AIツール
- 開発手法
title: AI駆動開発ハンズオンガイド：GitHub Spec Kitの徹底活用
video: /share-deepresearch/assets/video/spec-kit-practical-guide.mp4
---

# **AI駆動開発ハンズオンガイド：GitHub Spec Kitの徹底活用**

## **第1部 仕様駆動開発へのパラダイムシフト**

本章では、このガイド全体の概念的基盤を構築します。単なる定義を超えて、生成AI時代における開発者の役割の根本的な変化とソフトウェア制作の進化を探求します。

### **1.1 コードファーストから意図ファーストへ：Spec Kitの哲学**

仕様駆動開発（Spec-Driven Development, SDD）は、従来の開発ワークフローの限界と、初期のAIコード生成が持つ非構造的な性質への直接的なアンサーとして登場しました 1。その中核となるコンセプトは、これまでの常識を覆すものです。すなわち、仕様はもはや使い捨ての足場ではなく、実行可能な成果物となり、コードを生成、テスト、検証するための信頼できる唯一の情報源（Source of Truth）へと昇華します 1。

このアプローチは、従来の開発プロセスにおける非効率性を解消する試みです。多くの場合、仕様書はコーディングが始まるとすぐに陳腐化し、ドキュメントと実装の乖離がプロジェクト後半で大きな手戻りを生む原因となっていました。Spec Kitは、この問題を根本から解決するため、仕様そのものを開発プロセスの中心に据えます。

Spec Kitの哲学は、4つの主要な柱に基づいています 1。

* **意図駆動開発（Intent-driven development）:** 「どのように（How）」を実装する前に、「何を（What）」そして「なぜ（Why）」を定義することに重点を置きます。  
* **豊富な仕様作成（Rich specification creation）:** ガードレールと組織的な原則を用いて、曖昧さを排除した詳細かつ構造化された仕様を作成します。  
* **多段階の洗練（Multi-step refinement）:** プロンプト一発でのコード生成（ワンショット生成）がもたらす予測不能性を排し、意図的な反復プロセスを採用します。  
* **AIによる高度な解釈（AI-enhanced interpretation）:** 複雑な仕様を理解し、それに基づいて行動するために、高度なAIモデルの能力に大きく依存します。

この哲学は、生成AIの確率的で時に予測不可能な性質に対して、工学的な規律を課すための意図的な試みと解釈できます。Specify、Plan、Tasksという多段階のプロセスは、単なるワークフローではなく、AIが要件から逸脱したり、「ハルシネーション」を起こしたりするのを防ぐためのリスク管理戦略です。開発者は各チェックポイントでAIの解釈を検証し、次のステップに進む許可を与えます。これは、AI向けに最適化された古典的な品質ゲートプロセスと言えるでしょう。

### **1.2 AIディレクターとしての開発者：新たな役割**

SDDは、開発者のワークフローに大きな変化をもたらします。主な役割は、一行ずつコードを書くことから、AIエージェントを重要なチェックポイントで導く（steer）ことへとシフトします 2。このプロセスは、人間のアーキテクトとAIの実装者の間で行われる、構造化された対話として捉えることができます。そこでは、明確でコンテキストの豊富なコミュニケーション（プロンプト）が極めて重要になります。

Spec Kitは開発者を代替するものではなく、むしろ強力な「フォースマルチプライヤ（能力増幅器）」として位置づけられています。これにより、開発者はアーキテクチャ、ユーザーエクスペリエンス、ビジネスロジックといった、より高次の関心事に集中できるようになります 1。AIに定型的な実装作業を委任することで、人間は創造的かつ戦略的な意思決定に注力できるのです。

### **1.3 仕様駆動開発が特に有効な主要シナリオ**

SDDは、特に以下の3つの主要なユースケースで最大の価値を提供します。

* **0-to-1（「グリーンフィールド」）開発:** 高レベルのコンセプトから新しいプロジェクトを開始し、AIを使って本番環境に対応可能なアプリケーションをゼロから構築するシナリオです 1。  
* **反復的強化（「ブラウンフィールド」）開発:** 既存のシステムに複雑な機能を追加するシナリオです。これは特に、企業の環境において強力かつ実用的な応用例として注目されています 1。  
* **創造的探索とモダナイゼーション:** 安定した一つの仕様を基に、異なる技術スタックで複数の実装を並行して生成したり、ビジネスロジック（「What」）を時代遅れの実装（「How」）から分離してレガシーシステムを近代化したりするシナリオです 1。

特に「ブラウンフィールド」開発への注力は、Spec Kitの設計思想が単なる新規アプリ開発だけでなく、大企業が抱える既存システムの複雑性や技術的負債という根深い問題に取り組むことを示唆しています。ソフトウェアエンジニアリングにおいて、真にコストと時間がかかるのは、大規模なレガシーコードベースの維持と拡張です。Spec Kitをこの難題に対するソリューションとして位置づけることで、このツールは単なる技術デモから、企業のアーキテクチャを支える本格的なユーティリティへと昇華します。これは、AIを管理されたモダナイゼーションのためのツールとして活用する、未来のエンタープライズソフトウェア保守への道筋を示すものです。

## **第2部 統合開発環境のセットアップ**

このセクションでは、開発環境を準備するための、コピー＆ペーストで実行可能な詳細な手順を提供します。これは重要かつ複雑になりがちなステップであるため、最大限の明確さを目指します。

### **2.1 基本的な前提条件**

Spec Kitを利用するには、いくつかの基本的なツールが必要です。以下の手順に従って、GitとPythonをインストールし、バージョンを確認してください。

* **Git:** バージョン管理システム。macOS、Linux、Windows（WSL2経由）にインストールされている必要があります 1。  
* **Python:** Python 3.11以降が必要です 1。これは、Spec Kitが依存するライブラリとの互換性を確保するためです。各OSの公式パッケージマネージャ（  
  apt、yum、brewなど）やインストーラを使用してインストールしてください。

### **2.2 高性能パッケージマネージャ uv のインストール**

Spec Kitは、Pythonのパッケージ管理にuvの使用を推奨しています。uvは、その高速性とモダンな機能で注目されているツールです 1。

以下のプラットフォーム別コマンドを実行してuvをインストールします 6。

* **macOS / Linux:**  

  ```Bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

* **Windows (PowerShell):**  

  ```PowerShell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

インストール後、uv \--versionコマンドで正しくインストールされたことを確認します 8。

uv venv（仮想環境の作成）やuv pip install \<package\>（パッケージのインストール）といった基本的なコマンドに慣れておくと、後の作業がスムーズに進みます 6。

### **2.3 AIコーディングエージェントの設定**

Spec Kitは、複数のAIコーディングエージェントに対応しています。使用するエージェントのセクションのみに従って設定を進めてください。

#### **2.3.1 Claude Code CLI のセットアップ**

* **前提条件:** Node.js 18以降がインストールされている必要があります 10。  
* **インストール:** npm（推奨）またはネイティブインストーラを使用してインストールします 10。  

  ```Bash
  npm install -g @anthropic-ai/claude-code
  ```

* **認証:** ターミナルでclaudeコマンドを初めて実行すると、ブラウザが開き認証が求められます。Claude.ai（サブスクリプション）またはAnthropic Console（APIクレジット）アカウントでログインします 10。  
* **検証:** claude doctorコマンドを実行し、セットアップが正常に完了したことを確認します 12。

#### **2.3.2 GitHub Copilot CLI のセットアップ**

* **前提条件:** 有効なGitHub Copilotサブスクリプションと、GitHub CLI (gh) がインストールされている必要があります 13。  
* **GitHub CLIの認証:** ghをインストールした後、以下のコマンドでGitHubアカウントにログインします 13。  

  ```Bash
  gh auth login
  ```

* **インストール:** 次のコマンドでCopilot拡張機能をインストールします 13。  

  ```Bash
  gh extension install github/gh-copilot
  ```

* **検証:** gh copilot suggest "list all files"のようなコマンドを実行して、機能が有効になっていることを確認します 14。

#### **2.3.3 Gemini CLI のセットアップ**

* **前提条件:** Node.js 20以降と、課金が有効なGoogle Cloudプロジェクトが必要です 16。  
* **インストール:** npm（グローバルインストール）またはnpx（都度実行）を使用してインストールします 17。  

  ```Bash
  npm install -g @google/gemini-cli
  ```

* **認証:** 認証には複数の選択肢があります。個人のGoogleアカウントを使用するOAuth、Gemini APIキー、またはエンタープライズ向けのVertex AIです。多くの場合、GOOGLE\_CLOUD\_PROJECT環境変数の設定が必要です 17。  
* **検証:** gemini \--versionコマンドでバージョンを確認します。初回実行時には、テーマの選択や認証方法の選択など、対話的なセットアップが行われます 16。

セットアッププロセスは、ユーザーが最初に直面する大きなハードルです。以下の表は、各エージェントのセットアッププロセスを要約したもので、使用するエージェントの選択や、特定のコマンドを素早く思い出すのに役立ちます。

| 機能 | Claude Code | GitHub Copilot | Gemini CLI |
| :---- | :---- | :---- | :---- |
| **主要な前提条件** | Node.js 18+ | GitHub CLI (gh), Copilotサブスクリプション | Node.js 20+, Google Cloudプロジェクト |
| **インストールコマンド** | npm install \-g @anthropic-ai/claude-code | gh extension install github/gh-copilot | npm install \-g @google/gemini-cli |
| **認証方法** | ブラウザ経由のOAuth | gh auth login | OAuth, APIキー, またはVertex AI |
| **検証コマンド** | claude doctor | gh copilot suggest 'prompt' | gemini \--version |
| **主要な環境変数** | (特になし) | (特になし) | GOOGLE\_CLOUD\_PROJECT |

## **第3部 「Taskify」構築：Spec Kitウォークスルー**

このセクションは本ガイドの中核をなすチュートリアルです。Spec Kitのドキュメントに記載されているプロンプトとワークフローを正確に用いながら、各ステップでの分析と解説を交え、アプリケーションをゼロから構築するプロセスを案内します。

### **3.1 ステップ1：プロジェクトの初期化とスキャフォールディング**

まず、Spec Kitプロジェクトの基本的な骨格を作成します。ターミナルで以下のコマンドを実行してください 1。

```Bash
uvx --from git+https://github.com/github/spec-kit.git specify init Taskify
```

このコマンドは、Taskifyという名前の新しいディレクトリを作成し、Spec Kitのワークフローに必要なファイル構造を生成します。生成されるディレクトリ構造は以下の通りです 1。

* memory/: このディレクトリにはconstitution.mdなどが含まれます。これはAIエージェントの基本的な「ルール」や行動指針を定義するファイルで、セッションを跨いで一貫性を保つ役割を果たします。これは、人間向けのCONTRIBUTING.mdファイルに相当する、AI向けのガイドラインと考えることができます 20。  
* scripts/: ユーザーコマンド（/specifyなど）と、ファイルシステムの操作やAIとの対話を結びつけるシェルスクリプト群が格納されています。これらはSpec Kitの運用を支えるバックボーンです。  
* specs/: AIによって生成されるすべての仕様書や計画書が保存される場所です。  
* templates/: spec-template.mdやplan-template.mdといったテンプレートファイルが含まれています。これらはAIが成果物を構造化するための設計図として機能し、生成されるすべてのドキュメントが一貫したフォーマットを持つことを保証します。これはソフトウェア開発におけるテンプレートファイルの概念を応用したものです 21。

### **3.2 ステップ2：/specifyフェーズ \- 意図の明確化**

プロジェクトの骨格ができたので、次に対話型のAIエージェント（例：claude）をプロジェクトのルートディレクトリで起動します。そして、/specifyコマンドを使って、これから構築するアプリケーションの要件を自然言語で伝えます。

以下は、ドキュメントで提示されている「Taskify」アプリケーションのための詳細なプロンプトです 1。

```text
/specify Develop Taskify, a team productivity platform. It should allow users to create projects, add team members, assign tasks, comment and move tasks between boards in Kanban style. In this initial phase for this feature, let's call it "Create Taskify," let's have multiple users but the users will be declared ahead of time, predefined. I want five users in two different categories, one product manager and four engineers. Let's create three different sample projects. Let's have the standard Kanban columns for the status of each task, such as "To Do," "In Progress," "In Review," and "Done." There will be no login for this application as this is just the very first testing thing to ensure that our basic features are set up. For each task in the UI for a task card, you should be able to change the current status of the task between the different columns in the Kanban work board. You should be able to leave an unlimited number of comments for a particular card. You should be able to, from that task card, assign one of the valid users. When you first launch Taskify, it's going to give you a list of the five users to pick from. There will be no password required. When you click on a user, you go into the main view, which displays the list of projects. When you click on a project, you open the Kanban board for that project. You're going to see the columns. You'll be able to drag and drop cards back and forth between different columns. You will see any cards that are assigned to you, the currently logged in user, in a different color from all the other ones, so you can quickly see yours. You can edit any comments that you make, but you can't edit comments that other people made. You can delete any comments that you made, but you can't delete comments anybody else made.
```

このプロンプトが効果的である理由は、ユーザーの体験、機能、制約（「What」と「Why」）に完全に焦点を当て、技術的な実装（「How」）については一切言及していない点にあります。

AIエージェントはこのプロンプトを受け取ると、specs/001-create-taskify/spec.mdというファイルを生成します。このファイルには、ユーザーストーリーや機能要件が構造化された形式で記述されています 1。

プロセスはここで終わりではありません。次のように追加のプロンプトを与えて、仕様をさらに洗練させることができます 1。

```text
For each sample project or project that you create there should be a variable number of tasks between 5 and 15 tasks for each one randomly distributed into different states of completion. Make sure that there's at least one task in each stage of completion.
```

さらに、AIに自身の生成物を自己評価させることも可能です。これは重要な品質管理ステップです 1。

```text
Read the review and acceptance checklist, and check off each item in the checklist if the feature spec meets the criteria. Leave it empty if it does not.
```

### **3.3 ステップ3：/planフェーズ \- ソリューションの設計**

機能要件が固まったら、/planコマンドを使って技術的な設計図を作成します。このフェーズでは、開発者はアーキテクトとして、技術スタックや設計に関する決定を下します。

以下のプロンプトは、Taskifyアプリケーションを.NET Aspire、Postgres、Blazorで構築するようAIに指示する例です 1。

```text
/plan We are going to generate this using.NET Aspire, using Postgres as the database. The frontend should use Blazor server with drag-and-drop task boards, real-time updates. There should be a REST API created with a projects API, tasks API, and a notifications API.
```

このコマンドの実行後、specs/001-create-taskify/ディレクトリには、contracts/（API仕様）、data-model.md、plan.md（実装計画）、quickstart.md、research.mdといった、より詳細な技術ドキュメントが生成されます 1。

このプロセスは、Spec Kitが単にコードを生成するだけでなく、プロジェクトの包括的なドキュメンテーションスイートを同時に生成していることを示しています。これにより、プロジェクトは「生まれたときからドキュメント化されている」状態になります。これは、ドキュメントが後回しにされがちな従来の開発モデルを覆すものであり、長期的な保守性や新規開発者のオンボーディングにおいて大きな利点となります。

また、AIの調査プロセスを導くことも可能です。例えば、AIが「.NET Aspireを調査する」といった広範なタスクを立てた場合、以下のようにプロンプトを与えて、より具体的で実装に役立つ調査へと方向修正させることができます 1。

```text
I think we need to break this down into a series of steps. First, identify a list of tasks that you would need to do during implementation that you're not sure of or would benefit from further research. Write down a list of those tasks. And then for each one of these tasks, I want you to spin up a separate research task...
```

このような対話的なプロセスは、一種の「ライブ」なアーキテクチャ設計と言えます。開発者は単に計画を指示するだけでなく、AIを対話的な相談相手兼リサーチアシスタントとして活用し、コードを一行も書く前に技術的なトレードオフを検討しているのです。

最後に、AI自身に計画全体を監査させ、抜け漏れがないかを確認させます。これにより、実装計画の精度がさらに高まります 1。

### **3.4 ステップ4：/tasksフェーズ \- 計画から実行可能なステップへ**

/tasksコマンドの目的は、高レベルなplan.mdを、AIが実行できる細分化されたステップのチェックリストに分解することです 1。これにより、大規模な実装計画が、検証可能で管理しやすい小さなタスク群に変換されます。これは、アジャイル開発におけるタスク分割の考え方に似ています 23。

例えば、以下のようなコマンドを実行します。

```text
/tasks for specs/001-create-taskify/plan.md
```

このコマンドの出力は、AIがこれから実行する具体的な作業項目（例：「データベーススキーマを作成する」「ユーザー選択画面のUIコンポーネントを実装する」など）のリストになります。

### **3.5 ステップ5：AIによる実装とデバッグ**

すべての準備が整ったら、いよいよ実装を開始します。以下のコマンドでAIにコーディングを指示します 1。

```text
implement specs/001-create-taskify/plan.md
```

このコマンドを受け取ると、AIは生成されたタスクリストに従って、ローカル環境でCLIコマンド（例：dotnet new、npm install）を実行し、コードを記述し始めます。このため、/planフェーズで指定した技術スタック（この例では.NET SDK）がローカルマシンにインストールされている必要があります 1。

実装が完了したら、デバッグのループに入ります。まずAIにアプリケーションのビルドと実行を指示します。ビルドエラーが発生した場合、AIはターミナルの出力を読み取って自己修正を試みます。アプリケーションは起動するものの、ブラウザのコンソールにランタイムエラーが表示されるような場合は、そのエラーメッセージをコピーしてAIにフィードバックすることで、修正を促すことができます 1。

この対話的なデバッグプロセスを経て、最終的に人間の指示のもとでAIによってほぼ完全に構築された、動作するアプリケーションが完成します。

## **第4部 高度なワークフローとベストプラクティス**

ここまでのチュートリアルで「グリーンフィールド」開発のプロセスを学びました。このセクションでは、Spec Kitのより広範で戦略的な応用方法を探り、そのポテンシャルを最大限に引き出すための知識を深めます。

### **4.1 反復的強化：「ブラウンフィールド」ワークフロー**

ソフトウェア開発における「ブラウンフィールド」とは、大規模で複雑な既存のコードベースに新しい機能を追加することを指します 1。Spec Kitは、この困難なタスクを体系化し、安全かつ効率的に進めるための強力なワークフローを提供します。

ブラウンフィールド開発の概念的な流れは以下の通りです。

1. **コンテキストの読み込み:** AIに既存システムのアーキテクチャ、主要なコードファイル、コーディング規約など、必要なコンテキストを提供します。これにより、AIは既存の設計思想を理解します。  
2. **仕様の作成:** /specifyコマンドを使い、*新しい機能*に限定した仕様を作成します。この際、既存システムとのインタラクションを明確に定義することが重要です。  
3. **制約付き計画:** /planコマンドで、既存のアーキテクチャ、ライブラリ、設計パターンを尊重した実装計画を生成させます。これにより、新しいコードがシステムに自然に統合されるよう設計されます。  
4. **ターゲットを絞った実装:** AIは、後付け感のあるコードではなく、既存のコードベースに馴染むように設計された、クリーンに統合可能なコードを生成します 2。

このアプローチにより、複雑なシステムへの機能追加が高速化され、デグレードのリスクも低減します。

### **4.2 創造的探索：並行実装の生成**

Spec Kitの強力な応用例の一つが、単一のspec.mdを信頼できる情報源として、複数の異なる実装を並行して生成する「創造的探索」です 1。

例えば、以下のようなシナリオが考えられます。

1. 「Taskify」プロジェクトで作成したspec.mdを用意します。  
2. チュートリアルと同様に、.NETベースの実装を要求する/planコマンドを実行します。  
3. 次に、全く新しいセッションを開始し、\*同じspec.md\*をコンテキストとして提供した上で、全く異なる技術スタックを要求する/planコマンドを実行します。  

   ```text
   /plan Use Vite with React for the frontend and a Node.js/Express backend with a local SQLite database.
   ```

このプロセスは、SDDがビジネス要件（What）と技術実装（How）をいかに見事に分離しているかを示しています。これにより、技術選定のための迅速なプロトタイピング、パフォーマンス比較、アーキテクチャの実験などを、非常に低いコストで実現できます 1。

### **4.3 プロンプトの技術：AIディレクションのベストプラクティス**

「Taskify」のウォークスルーから得られた教訓を、実践的なベストプラクティスとして以下にまとめます。

* **/specifyコマンド向け:**  
  * ユーザーペルソナ、ユーザーストーリー、受け入れ基準に焦点を当てます。  
  * 曖昧さを避け、冗長であっても明示的に記述します。  
  * 制約条件やエッジケースを具体的に列挙します。  
* **/planコマンド向け:**  
  * 技術スタック、アーキテクチャパターン、設計上の制約（例：「最小限のライブラリを使用する」「企業の設計システムに準拠する」）について、明確な意思決定を伝えます。  
* **すべての対話において:**  
  * 反復的な洗練を心がけます。最初の出力を最終版と見なさず、AIに明確化を求める質問を投げかけ、その仮定に挑戦し、自己監査ツールとして活用します。

Spec Kitを最も効果的に使いこなすのは、最高の初期プロンプトを書ける開発者ではなく、この反復的な洗練と検証のループを通じてAIを巧みに導くことができる、戦略的なAIディレクターとしてのスキルを持つ開発者です。

## **第5部 結論：AIネイティブなソフトウェア開発の未来**

### **5.1 Spec Kitがもたらす優位性の再確認**

本ガイドで詳述したように、GitHubのSpec Kitは、単なるコード生成ツールではなく、ソフトウェア開発のプロセスそのものを再定義するフレームワークです。その利点は多岐にわたります。

* **開発速度の向上:** AIが定型的な実装作業を担うことで、開発者はより高次のタスクに集中でき、プロジェクト全体のベロシティが向上します。  
* **品質と一貫性の確保:** 仕様に基づいた体系的なアプローチにより、生成されるコードの一貫性が保たれ、属人性が排除されます。  
* **生きたドキュメント:** 開発プロセスと同時にAPI仕様やデータモデルなどのドキュメントが生成されるため、ドキュメントは常に最新の状態に保たれます。  
* **開発者の役割の昇華:** 開発者は単なるコーダーから、ビジネス要件と技術実装を繋ぐ戦略的な「AIディレクター」へと進化します。

### **5.2 今後の展望**

Spec Kitのような構造化され、プロセス指向のツールキットの登場は、ソフトウェア開発におけるAI技術が成熟期に入ったことを示しています。初期の「プロンプト一発」でのコード生成がもたらした混沌から、予測可能で信頼性の高いエンジニアリングプロセスへと移行しつつあります。

今後、このような方法論を習得し、AIを共同作業者として効果的に活用する能力は、高いパフォーマンスを発揮するエンジニアリングチームを定義する重要な差別化要因となるでしょう。Spec Kitは、その未来に向けた具体的な一歩であり、AIネイティブなソフトウェア開発の時代の到来を告げるものです 1。

#### **引用文献**

1. github/spec-kit: Toolkit to help you get started with Spec-Driven Development, 9月 3, 2025にアクセス、 [https://github.com/github/spec-kit](https://github.com/github/spec-kit)  
2. Spec-driven development with AI: Get started with a new open source toolkit, 9月 3, 2025にアクセス、 [https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/](https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/)  
3. Let it Cook \- Introducing Spec Kit for Spec-Driven Development\! \- Episode 13 \- YouTube, 9月 3, 2025にアクセス、 [https://www.youtube.com/watch?v=DTw9X7MtU5s](https://www.youtube.com/watch?v=DTw9X7MtU5s)  
4. Spec-Kit Jimmy Song, 9月 3, 2025にアクセス、 [https://jimmysong.io/en/ai/spec-kit/](https://jimmysong.io/en/ai/spec-kit/)  
5. github/spec-kit: Toolkit to help you get started with Spec-Driven Development \- YouTube, 9月 3, 2025にアクセス、 [https://www.youtube.com/watch?v=bEhzouDE-y0](https://www.youtube.com/watch?v=bEhzouDE-y0)  
6. astral-sh/uv: An extremely fast Python package and project manager, written in Rust. \- GitHub, 9月 3, 2025にアクセス、 [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)  
7. Installation uv \- Astral Docs, 9月 3, 2025にアクセス、 [https://docs.astral.sh/uv/getting-started/installation/](https://docs.astral.sh/uv/getting-started/installation/)  
8. Python UV: The Ultimate Guide to the Fastest Python Package Manager \- DataCamp, 9月 3, 2025にアクセス、 [https://www.datacamp.com/tutorial/python-uv](https://www.datacamp.com/tutorial/python-uv)  
9. Managing packages uv \- Astral Docs, 9月 3, 2025にアクセス、 [https://docs.astral.sh/uv/pip/packages/](https://docs.astral.sh/uv/pip/packages/)  
10. Quickstart \- Anthropic API, 9月 3, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/quickstart](https://docs.anthropic.com/en/docs/claude-code/quickstart)  
11. Set up Claude Code \- Anthropic API, 9月 3, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/setup](https://docs.anthropic.com/en/docs/claude-code/setup)  
12. How to Install Claude Code CLI – Bind AI IDE, 9月 3, 2025にアクセス、 [https://blog.getbind.co/2025/08/26/how-to-install-claude-code-cli/](https://blog.getbind.co/2025/08/26/how-to-install-claude-code-cli/)  
13. Installing GitHub Copilot in the CLI, 9月 3, 2025にアクセス、 [https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-in-the-cli](https://docs.github.com/en/copilot/how-tos/set-up/install-copilot-in-the-cli)  
14. Getting Started with GitHub Copilot in the CLI \- DEV Community, 9月 3, 2025にアクセス、 [https://dev.to/github/stop-struggling-with-terminal-commands-github-copilot-in-the-cli-is-here-to-help-4pnb](https://dev.to/github/stop-struggling-with-terminal-commands-github-copilot-in-the-cli-is-here-to-help-4pnb)  
15. Installing GitHub Copilot in the CLI \- GitHub Enterprise Cloud Docs, 9月 3, 2025にアクセス、 [https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli](https://docs.github.com/en/enterprise-cloud@latest/copilot/managing-copilot/configure-personal-settings/installing-github-copilot-in-the-cli)  
16. Hands-on with Gemini CLI \- Codelabs, 9月 3, 2025にアクセス、 [https://codelabs.developers.google.com/gemini-cli-hands-on](https://codelabs.developers.google.com/gemini-cli-hands-on)  
17. google-gemini/gemini-cli: An open-source AI agent that brings the power of Gemini directly into your terminal. \- GitHub, 9月 3, 2025にアクセス、 [https://github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)  
18. How do I install Gemini CLI? \- Milvus, 9月 3, 2025にアクセス、 [https://milvus.io/ai-quick-reference/how-do-i-install-gemini-cli](https://milvus.io/ai-quick-reference/how-do-i-install-gemini-cli)  
19. Gemini CLI Tutorial Series \- Google Cloud \- Medium, 9月 3, 2025にアクセス、 [https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718](https://medium.com/google-cloud/gemini-cli-tutorial-series-77da7d494718)  
20. Setting guidelines for repository contributors \- GitHub Docs, 9月 3, 2025にアクセス、 [https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/setting-guidelines-for-repository-contributors)  
21. Creating a template repository \- GitHub Docs, 9月 3, 2025にアクセス、 [https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)  
22. Configuring issue templates for your repository \- GitHub Docs, 9月 3, 2025にアクセス、 [https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)  
23. shellspec/shellspec: A full-featured BDD unit testing framework for bash, ksh, zsh, dash and all POSIX shells \- GitHub, 9月 3, 2025にアクセス、 [https://github.com/shellspec/shellspec](https://github.com/shellspec/shellspec)  
24. sagiegurari/cargo-make: Rust task runner and build tool. \- GitHub, 9月 3, 2025にアクセス、 [https://github.com/sagiegurari/cargo-make](https://github.com/sagiegurari/cargo-make)
