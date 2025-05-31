---
layout: topic
title: "GitHub Copilot Spaces 最新情報と具体的な活用事例"
date: 2025-05-31
prompt: "GitHub Copilot Spacesについて最新情報を調査し、具体的な活用事例をまとめて欲しい。"
category: "ai"
tags: [GitHub,GitHub Copilot]
audio: "/share-deepresearch/assets/audio/github-copilot-spaces.mp3"
supplementary_materials:
  - title: "GitHub Copilot Spaces 活用事例 インフォグラフィック"
    url: "/share-deepresearch/topics/github-copilot-spaces/infographic.html"
---

# **GitHub Copilot Spaces 最新情報と具体的な活用事例**

## **1\. はじめに (Introduction to GitHub Copilot Spaces)**

### **GitHub Copilotの進化とCopilot Spacesの位置づけ (Evolution of GitHub Copilot and the Role of Copilot Spaces)**

GitHub Copilotは、開発者の生産性向上を目的としたAIペアプログラマーとして登場して以来、単なるコード補完ツールを超えた進化を遂げてきました。初期のリアルタイムコード提案から、Copilot Chatによる対話型支援、Copilot Coding Agentによるタスク自動化の試み、さらにはコードレビュー機能の搭載など、その機能は開発ライフサイクルの多岐にわたる局面をカバーするように拡張されています 1。開発者はこれらの機能を通じて、コーディングの効率化だけでなく、問題解決やコラボレーションの質の向上を期待できるようになりました。

このようなGitHub Copilotの進化の過程で登場したのが「Copilot Spaces」です。Copilot Spacesは、特定のタスクやプロジェクト遂行に必要な「コンテキスト」をAIに集中的に提供することで、より精度の高い、タスクに特化した支援を実現することを目的としています 1。現代の開発現場では、プロジェクト情報がコード、ドキュメント、コミュニケーションツールなど様々な場所に散在し、「情報の断片化」が課題となることが少なくありません。Copilot Spacesは、この課題に対する一つの解決策として、関連情報を一元化し、それを基盤としたAI支援を提供することを目指しています 12。

Copilot Spacesの登場は、GitHubがAIによる開発支援において、従来の広範な知識に基づく「汎用性」だけでなく、特定の文脈に深く根差した「特化性」の追求、あるいはその両立を目指す戦略の現れと解釈できます。初期のGitHub Copilotは、膨大な公開コードを学習データとし、広範なプログラミング言語や状況に対応できる汎用的なコード補完能力を提供することに主眼が置かれていました。その後、Copilot Chatが導入され、開発者が自然言語でAIと対話し、より具体的な指示や質問を通じてコンテキストを伝えられるようになりましたが、そのコンテキストは対話のセッションに依存する一時的なものが中心でした。Copilot Spacesは、この点をさらに一歩進め、ユーザーが能動的に、かつ永続的にコンテキストの集合（コード、ドキュメント、指示など）を定義し、AIの知識を特定のドメインやタスクに「グラウンディング」させることを可能にします。これは、より複雑で専門性の高い開発業務においてAIの真価を発揮させるための、必然的な進化のステップと言えるでしょう。つまり、汎用的な大規模言語モデルの能力を維持しつつ、その限界をユーザー定義の特化されたコンテキストによって補い、具体的なタスクにおけるAIのパフォーマンスを最大限に引き出すアプローチと言えます。

### **本レポートの目的と構成 (Purpose and Structure of this Report)**

本レポートは、GitHub Copilot Spacesに関する最新情報を網羅的に調査し、その中核的なコンセプト、主要な機能、提供状況、料金体系、そして具体的な活用事例を詳細に解説することを目的としています。

開発者がCopilot Spacesを効果的に理解し、日々の開発業務やチームプロジェクトにおいてその能力を最大限に活用することで、生産性の向上、知識共有の促進、そしてコラボレーションの深化に繋げるための一助となるような、実践的な情報を提供することを目指します。レポートは、Copilot Spacesの基本的な概要から始まり、機能の詳細、利用シナリオ、他のCopilot機能との比較、そして現状の課題と将来展望に至るまで、段階的に掘り下げていきます。

## **2\. GitHub Copilot Spacesとは何か？ (What is GitHub Copilot Spaces?)**

### **定義と中核的なコンセプト (Definition and Core Concept)**

GitHub Copilot Spacesは、特定の開発タスクやプロジェクトに関連する多様な情報資源（ソースコード、技術ドキュメント、設計メモ、さらにはCopilotへのカスタム指示など）を一元的に集約し、その整理されたコンテキストに基づいてCopilotがより的確で、状況に応じたパーソナライズされた回答や開発支援を提供するための機能です 1。この機能は、github.com/copilot/spaces という専用のURLからアクセスし、ユーザーが独自の「Space（スペース）」を作成・管理することが可能です 1。

現代のソフトウェア開発チームが直面する大きな課題の一つに「知識の断片化」があります。プロジェクトに関する重要なコンテキストが、コードベース、複数のドキュメント、そしてチームメンバー個々の頭の中に散在している状況は、新しい領域へのキャッチアップや効率的なタスク遂行を困難にします。Copilot Spacesは、この問題に対処するために、プロジェクトのコンテキストを集約し、Copilotをその特定の主題に関する専門家（Subject Matter Expert）へと変貌させることを目指しています 12。

### **主な提供価値と利点 (Key Value Proposition and Benefits)**

Copilot Spacesは、開発者個人およびチームに対して、以下のような主要な価値と利点を提供します。

* コンテキスト集約による回答精度の向上 (Improved Answer Accuracy through Context Aggregation):  
  厳選された特定のコード、ドキュメント、指示といったコンテキストにAIの知識を「グラウンディング」させる（深く関連付ける）ことにより、一般的なCopilot Chatの応答と比較して、よりタスクに関連性が高く、具体的な回答や提案を得ることが可能になります 11。特に注目すべきは、「限定されたサイズのコンテキスト」という設計思想です。これは、無制限にコンテキストを広げるのではなく、意図的に範囲を絞ることで、ノイズを減らし、AIが集中して高品質な応答を生成できるようにするための戦略的な選択と言えます 11。  
* 開発フローの維持と効率化 (Maintaining Development Flow and Efficiency):  
  特定のタスク遂行に必要な情報を一箇所に集約することで、開発者は複数のツール間を頻繁に移動したり、他のチームメンバーに背景情報を繰り返し問い合わせたりする手間を削減できます。これにより、集中状態（フロー状態）を維持しやすくなり、開発作業の効率化が期待できます 11。GitHub自身の調査によれば、GitHub Copilotの利用者はタスク完了速度が最大55%向上し、仕事に対する満足度が最大75%向上すると報告されており 3、Copilot Spacesはこの効果をさらに増幅させる可能性を秘めています。  
* チーム内の知識共有とコラボレーション促進 (Promoting Knowledge Sharing and Collaboration within Teams):  
  作成したSpaceを組織内で共有することにより、チームメンバーは特定のプロジェクトや技術に関する専門知識に容易にアクセスできるようになります。これにより、同じ質問が繰り返されたり、特定の人に知識が集中したりする状況を緩和し、チーム全体の知識レベルの向上と効率的なコラボレーションを促進します 11。具体的な活用例としては、新規メンバーのオンボーディング資料の集約、複雑なシステムの構造理解、共通のスタイルガイドやレビューチェックリストの共有などが挙げられます 14。

Copilot Spacesは、単なるQ\&Aツールや情報検索ツールに留まらず、「生きたドキュメント」兼「タスク特化型AIアシスタント」としての役割を担う可能性を秘めていると言えます。従来のプロジェクトドキュメントは静的であり、更新が滞ったり、必要な情報を見つけ出すのに手間がかかったりすることがありました。これに対し、Copilot Spacesは、ソースコード、公式ドキュメント、チーム内の議事録、さらにはSlackの会話履歴 1 といった、より多様で動的な情報を集約し、それらに対して自然言語で対話形式でアクセスすることを可能にします。さらに重要な点として、Spaceに追加されたリポジトリ内のコードは、常にそのリポジトリのmainブランチの最新バージョンを参照するため 1、情報が陳腐化しにくいという大きな利点があります。これにより、Space自体がプロジェクトの「現在の状態」を反映した動的な知識ベースとして機能し、チームメンバーは常に最新かつ正確な情報に基づいてCopilotの支援を受けながら作業を進められるようになるでしょう。

## **3\. 主な機能詳解 (Detailed Key Features)**

### **スペースの作成と管理 (Creating and Managing Spaces)**

Copilot Spacesの利用は、専用のウェブインターフェース https://github.com/copilot/spaces から始まります。ユーザーはここから「Create space」ボタンをクリックすることで、新しいSpaceの作成プロセスを開始できます 1。

作成時には、以下の情報を設定します。

* **スペース名 (Name):** Spaceを識別するための名前。  
* **オーナー (Owner):** Spaceを個人アカウントで所有するか、所属するGitHub Organizationで所有するかを選択します。OrganizationがオーナーとなるSpaceは、後述する共有機能を利用してチームメンバーと連携することが可能です 1。  
* **説明 (Description):** (任意) Spaceの目的や内容を他のユーザーが理解しやすくするための説明文。

これらの情報を入力し、「Create」ボタンを押すことでSpaceが作成されます。

### **コンテキストの追加：インストラクションとリファレンス (Adding Context: Instructions and References)**

作成されたSpaceには、Copilotの応答を方向付けるための主要なコンテキストとして、「インストラクション」と「リファレンス」の2種類を追加できます 1。

* インストラクション (Instructions):  
  これは、そのSpace内でCopilotがどのような役割を担い、何に焦点を当てるべきかを自由記述のテキスト形式で指示するものです。具体的には、Copilotの専門分野、支援すべきタスクの種類、逆に避けるべき応答や行動などを定義します 1。このインストラクションにより、ユーザーの意図に沿った、より関連性の高いCopilotからの応答を引き出すことが期待できます。  
  公式ドキュメントで提示されている例としては、「あなたはSQLジェネレーターです。添付ファイルで定義されたサンプルクエリとデータスキーマを基に、ユーザーの目標に応じたSQLクエリを生成することがあなたの仕事です。」といった具体的な指示が挙げられます 1。  
  この「インストラクション」機能は、単にAIに指示を与えるだけでなく、高度なプロンプトエンジニアリングの知識やノウハウをSpace単位でカプセル化し、チーム内で再利用可能にする手段と捉えることができます。効果的なAIの活用には、質の高いプロンプトが不可欠であることは広く認識されていますが 25、全ての開発者がプロンプトエンジニアリングに長けているわけではありません。「インストラクション」は、Spaceの作成者がAIの振る舞いを定義する一種の「マスタープロンプト」や「システムプロンプト」のような役割を果たします。Spaceの利用者は、この事前に最適化された「インストラクション」によって方向付けられた環境でCopilotと対話するため、個々の質問プロンプトが多少洗練されていなくても、Space全体のコンテキストと指示によって応答の品質が向上する可能性があります。これは、チーム内でのAI活用スキルの平準化や、専門家が設計した高度なAI支援をより多くのメンバーが享受できるようにするための重要な仕組みと言えるでしょう。  
* リファレンス (References):  
  リファレンスとしては、GitHubリポジトリ（パブリックおよびプライベート双方を含む）内のソースコードや、プロジェクトに関連する様々なテキストベースのコンテンツを追加できます 1。特筆すべきは、公式な技術ドキュメントや設計書だけでなく、よりインフォーマルな情報源、例えばSlackの議論スレッドのコピー、ビデオ会議の議事録の要約、箇条書きのメモなども有効なコンテキストとして活用できる点です 1。これは、Copilot Spacesが情報の形式にとらわれず、実際の開発現場で生まれる実用的な知識を柔軟に集約できる能力を持っていることを示しています。  
  さらに重要な点として、Spaceに追加されたリポジトリは、常にそのリポジトリのmainブランチ（またはデフォルトブランチ）の最新バージョンのコードを参照します 1。これにより、Space内のコードコンテキストが常に最新の状態に保たれ、古い情報に基づく不正確な応答が生成されるリスクを低減します。

### **チームでの共有とアクセス権管理 (Team Sharing and Permission Management)**

Copilot Spacesは、個人利用だけでなく、チームでのコラボレーションを強力にサポートするように設計されています。

* **組織オーナーのSpace:** Organizationが所有者として設定されたSpaceは、そのOrganizationに所属する他のメンバーと共有することが可能です。共有設定では、通常、Organizationメンバーに対して読み取り専用のアクセス権が付与されます 1。  
* **個人オーナーのSpace:** 個人アカウントで作成されたSpaceは、現時点では他者と共有する機能は提供されていません 24。  
* **共有されたSpaceの利用:** 共有されたSpaceにアクセス権を持つチームメンバーは、そのSpaceに集約されたコンテキスト（インストラクションやリファレンス）を閲覧し、そのコンテキストに基づいてSpace内のCopilot Chatインターフェースを通じて質問や指示を行うことができます 24。

### **対応AIモデルの選択 (Selecting Compatible AI Models)**

Copilot Spacesでは、応答を生成するために使用する大規模言語モデル（LLM）をユーザーが選択し、変更することが可能です。Space内のチャットインターフェースに設けられたドロップダウンメニューから、利用したいAIモデルを選ぶことができます 1。

現在、GitHub Copilot全体で利用可能なモデルとしては、Anthropic社のClaudeシリーズ、Google社のGeminiシリーズ、そしてOpenAI社のGPT-4.1、o3、o4-miniなどが挙げられており、Spacesでもこれらのモデル、あるいはそのサブセットが利用できると考えられます 1。GitHubは、タスクの性質に応じて最適なAIモデルを選択するためのガイドも提供しています 1。

モデル選択の自由度は、開発者にとって大きなメリットをもたらします。タスクの特性、例えば高度な推論や創造性が求められるのか、応答速度が重視されるのか、あるいは特定の知識領域に特化した能力が必要なのかといった要件に応じて、最も適したAIモデルをSpaceごとに割り当てることができるからです。例えば、複雑なアルゴリズムの設計やリファクタリング案の検討を行うSpaceでは高性能なフラッグシップモデルを選択し、既存ドキュメントの内容に関する単純なQ\&Aを行うSpaceではより軽量で高速なモデルを選択する、といった使い分けが考えられます。

しかし、この柔軟性は同時に、ユーザーに対して各AIモデルの特性（得意なタスク、応答スタイル、処理速度、トークン消費量、そして場合によってはコストなど）をある程度理解し、適切に選択する能力を求めることにもなります。Spaceの目的と提供コンテキストに合致したモデルを選択することが、Copilot Spacesの価値を最大限に引き出すための鍵となるでしょう。

## **4\. 提供状況と料金体系 (Availability and Pricing)**

### **現在の提供ステータス (Current Availability Status)**

GitHub Copilot Spacesは、本レポート執筆時点（2025年5月以降の情報に基づく）において、**パブリックプレビュー版**として提供されています 1。これは、機能がまだ開発途上にあり、今後変更される可能性があることを意味します。ユーザーからのフィードバックを積極的に収集し、製品改善に役立てる段階です。

公式な発表としては、GitHub Changelogにおいて2025年5月29日に「Introducing Copilot Spaces: A new way to work with code and context」というタイトルでその登場が告知されました 12。

### **利用可能なGitHub CopilotプランとSpacesの関連性 (Applicable GitHub Copilot Plans and Relation to Spaces)**

Copilot Spacesの利用資格は、基本的にGitHub Copilotの有効なライセンスを保有している全てのユーザーに開かれています。これには、個人向けのCopilot Free、Copilot Pro、Copilot Pro+プランの利用者、および組織向けのCopilot Business、Copilot Enterpriseプランの利用者が含まれます 1。

ただし、Copilot BusinessまたはCopilot Enterpriseプランを通じてSpacesを利用する場合、所属する組織の管理者が、GitHub Copilotのプレビュー機能を組織レベルでオプトイン（有効化）している必要があります 11。この設定は、通常、組織のCopilotポリシー管理画面 (Managing policies for Copilot in your organization) から行います 11。

### **Spaces利用時の課金モデル（2025年6月4日以降の予定を含む）(Billing Model for Spaces Usage, including plans from June 4th, 2025\)**

GitHubは、Copilot Spacesの課金モデルについて、2025年6月4日以降、既存のCopilot Chatと同じ体系に従うと発表しています 11。具体的な内容は以下の通りです。

* Copilot Pro, Pro+, Business, Enterprise プランの利用者:  
  これらの有料プランのサブスクライバーがSpaces内でプレミアムAIモデル（例: GPT-4.5, Claude Opus 4など、より高性能だがリクエストあたりのコストが高いモデル）を使用してチャット（質問や指示）を行った場合、そのチャットリクエスト1回につき、各プランに割り当てられている「プレミアムリクエスト」の許容量を1回消費します。一方、ベースAIモデル（例: GPT-4.1, Claude 3.7/4 Sonnetなど、標準的な性能のモデル）を使用した場合のチャットリクエストは、プレミアムリクエストの許容量を消費しません（つまり、ベースモデルでの利用は実質的に無制限に近い形となりますが、プランごとの全体的な利用規約に従います）3。  
* Copilot Free プランの利用者:  
  Copilot FreeプランのユーザーがSpaces内でチャットを行った場合、そのリクエストは、プランに設定されている月間50回のCopilot Chat利用上限にカウントされます 3。

また、全てのプランにおいて、特に需要が集中する期間には、サービスの安定性を保つためにレート制限（一定時間内のリクエスト数上限）が適用される可能性があると言及されています 11。

この課金モデルは、GitHubが一貫して進めているAIサービス戦略を反映していると考えられます。Copilot Chatという既存の主要な対話型インターフェースとSpacesの課金体系を統一することで、ユーザーが複数の機能間で異なる料金ルールに混乱することを避け、シンプルな利用体験を提供しようとしています。同時に、計算資源をより多く消費するプレミアムAIモデルの利用に対しては、その対価としてプレミアムリクエスト数を消費させることで、サービスの持続可能性と公平性を担保する狙いがあるでしょう。Copilot Freeユーザーにとっては、Spacesの利用も貴重な月間チャット許容量を消費するため、どのタスクにSpacesを活用するかを計画的に判断するか、あるいはより多くの機能と利用枠を求めてCopilot Pro以上の有料プランへのアップグレードを検討する動機付けとなる可能性があります。

### **表: GitHub Copilotプラン比較とSpaces利用**

| プラン名 | 月額料金（個人） | Spaces利用可否 | Spacesチャット(ベースモデル) | Spacesチャット(プレミアムモデル) | 主な対象ユーザー |
| :---- | :---- | :---- | :---- | :---- | :---- |
| GitHub Copilot Free | 無料 | 可 | 月間チャット上限50回にカウント 12 | 月間チャット上限50回にカウント (プレミアムモデル利用制限あり) 12 | Copilotの基本機能を試したい個人開発者 |
| GitHub Copilot Pro | $10 USD/月 または $100 USD/年 29 | 可 | プレミアムリクエスト消費なし (チャット自体は無制限) 12 | プレミアムリクエストを1回消費 (月間300回まで、超過分は追加購入) 12 | より柔軟なAI支援を求める個人開発者、学生、教師、OSSメンテナー (無料枠あり) 29 |
| GitHub Copilot Pro+ | $39 USD/月 または $390 USD/年 29 | 可 | プレミアムリクエスト消費なし (チャット自体は無制限) 12 | プレミアムリクエストを1回消費 (月間1500回まで、超過分は追加購入) 12 | 最新・最上位モデルへのフルアクセスを求めるAIパワーユーザー 29 |
| GitHub Copilot Business | シートあたり $19 USD/月 30 | 可 | プレミアムリクエスト消費なし (チャット自体は無制限) 12 | プレミアムリクエストを1回消費 (ユーザーあたり月間300回まで) 12 | GitHub Free/Teamプランの組織、GitHub Enterprise Cloudのエンタープライズ 30 |
| GitHub Copilot Enterprise | シートあたり $39 USD/月 29 | 可 | プレミアムリクエスト消費なし (チャット自体は無制限) 12 | プレミアムリクエストを1回消費 (ユーザーあたり月間1000回まで) 12 | GitHub Enterprise Cloudを利用する大規模エンタープライズ 30 |

*注: 上記のプレミアムリクエスト消費に関する記述は、2025年6月4日以降の課金モデルに基づきます。料金や内容は変更される可能性がありますので、常に最新の公式情報をご確認ください。*

この表は、ユーザーが自身の利用状況や予算に最適なプランを選択し、Copilot Spacesをどのように利用できるかを明確に理解するのに役立ちます。特に、Spacesの利用がプランごとのチャット回数制限やプレミアムリクエストの消費にどのように影響するのかを把握することが重要です。

## **5\. 具体的な活用事例 (Specific Use Cases)**

GitHub Copilot Spacesは、そのコンテキスト集約能力と対話型インターフェースにより、個人開発からチーム開発まで、多岐にわたるシナリオでの活用が期待されます。

### **個人開発における活用シナリオ (Use Case Scenarios in Individual Development)**

* 新機能開発の迅速化と品質向上 (Accelerating New Feature Development and Improving Quality):  
  個人開発者が新しい機能に取り組む際、関連する既存コードの断片、自身でまとめた製品仕様メモ、参考にしたデザインレビューの記録、あるいはUIモックアップの画像とその説明などをSpaceに集約します 16。このコンテキストに基づき、Copilotは以下のような支援を提供できます。  
  * 現在の実装がどのように機能しているかの要約。  
  * 集約された仕様書やメモに基づいて、必要な変更や追加機能の提案。  
  * 新機能の初期実装のドラフトコード作成、または開発を進めるための具体的な次のステップの概説。  
  * 仕様に対して実装が不足している要素や、設計との間に矛盾点が存在する場合の指摘。 例えば、公式ドキュメントでは、「このSpaceには、低コストの検査を提供するヘルスケアNPOのための新しいユーザー登録フォームが含まれています。これはReactとTailwind CSSを使用して構築されています」といったインストラクションを設定した上で、「このフォームに2要素認証（2FA）のサポートを追加するにはどうすればよいですか？」とCopilotに質問するシナリオが紹介されています 16。  
* 定型的なタスクや小規模ロジックの定義 (Defining Logic for Repetitive or Small-Scale Tasks):  
  テレメトリイベントの追跡、特定イベント発生時の処理、APIからのデータ取得と整形など、開発プロジェクトには定型的・反復的な小規模タスクが数多く存在します。これらのタスクのロジックを一度Spaceに文書化し、関連コードスニペットと共に集約しておくことで、同様のタスクが発生した際に一貫性を保ちつつ、迅速に処理できるようになります 16。Copilotは以下の点で支援します。  
  * 過去の類似作業やSpace内の情報に基づいて、効率的な実装パターンを提案。  
  * 再利用可能な関数やテンプレートコードの作成支援。  
  * 定義したロジックが、プロジェクト全体の標準やベストプラクティス（Space内で定義されていればそれも含む）に準拠しているかのレビュー。  
  * コードベース内で類似のタスクが過去にどのように処理されてきたかの具体例の提示。 インストラクションの例として、「あなたは開発者がテレメトリーイベントを実装するのを支援します。(1) イベントに対するユーザーの目標を検証し、(2) 既存のイベントの例に基づいて新しいイベント構造を提案し（共通のテレメトリースキーマを使用）、(3) テレメトリー設定ファイルの新しいバージョンを作成する必要があります」といった役割定義が挙げられています。これに対し、ユーザーは「ユーザーがアプリ内通知をクリックしたときにログを記録するのを手伝ってください」といった具体的なプロンプトで依頼できます 16。  
* 既存コードベース・エラー内容の深い理解 (Deeper Understanding of Existing Codebases and Errors):  
  個人開発では、自身が過去に書いたコードや、利用しているオープンソースライブラリの内部構造を深く理解する必要が生じることがあります。Fintan.jpが報告した学生向けイベントでのCopilot Chatの活用事例（これはCopilot Spacesのコンセプトと非常に近いものです）では、既存コードの説明やエラーメッセージの解説に大きな効果があったとされています 32。Copilot Spacesに該当するソースコードや関連ドキュメントを投入し、適切なインストラクションを与えることで、同様の利用が可能です。  
  例えば、特定のコードブロックを選択し「これを説明して (Explain this)」と指示したり、発生したエラーメッセージを提示して「このエラーを説明して (Explain using Copilot)」と依頼することで、一般的な検索エンジンで情報を探すよりも迅速かつ的確に、問題の核心やコードの意図を理解する助けとなります 32。  
  個人開発者にとって、Copilot Spacesは、いわば「自己完結型の仮想的な専門家チーム」を構築する手段となり得ます。開発者は、特定の技術スタック（例: Python/Django, React/Node.js）、デザインパターン、利用しているライブラリのAPI仕様、プロジェクト固有のアーキテクチャや設計思想などをSpaceに集約し、インストラクションを通じてCopilotにそのSpace内での役割（例: 「Djangoエキスパートとして質問に答える」「Reactのベストプラクティスに基づいてコードレビューを行う」など）を定義することができます。これにより、開発者は必要な時にいつでも、まるでその分野の専門家と対話しているかのように、Space内のCopilotから具体的なアドバイス、コード例、トラブルシューティングのヒントなどを引き出せるようになります。これは、特に新しい技術を学習しながら開発を進める場合や、ニッチな技術領域、あるいは大規模で複雑なオープンソースプロジェクトを利用する際に、非常に強力なサポートとなるでしょう。

### **チーム開発における活用シナリオ (Use Case Scenarios in Team Development)**

Copilot Spacesの真価は、チームでの知識共有とコラボレーションの促進において、より顕著に現れると考えられます。

* 新規メンバーのオンボーディング支援 (Supporting Onboarding of New Team Members):  
  新しい開発者がチームに参加した際、プロジェクトの概要、主要なコードコンポーネント、開発環境のセットアップ手順、コーディング規約、重要なドキュメントへのリンク、よくある質問とその回答などを集約したSpaceを共有することで、オンボーディングプロセスを大幅に効率化し、新規メンバーが迅速にプロジェクトに貢献できるよう支援します 14。Copilotは、このSpace内の最新情報に基づいて新規メンバーからの質問に答えたり、プロジェクトのベストプラクティスを具体的に指導したりする役割を担うことができます 16。  
* 複雑なシステムやワークフローの知識集約 (Knowledge Aggregation for Complex Systems or Workflows):  
  大規模なシステムにおける認証フロー、複雑なビジネスロジックを持つモジュール、CI/CDパイプラインの全体像など、理解に時間のかかるシステムやワークフローに関する情報をSpaceに集約します。これには、関連するソースコード、アーキテクチャ図、シーケンス図、設計ドキュメント、過去のトラブルシューティング記録などが含まれます 24。チームメンバーは、このSpaceを参照することで、システムの詳細について自己学習したり、Copilotに質問して理解を深めたりすることができます。例えば、「あなたはこの認証システムに関連するコードとドキュメントを含んでいます」というインストラクションを持つSpaceに対し、「このシステムにおけるSSO（シングルサインオン）はどのように機能しますか？」と質問することで、具体的な説明を得ることが期待できます 16。  
* コーディング規約、レビュースタイルガイドの共有と徹底 (Sharing and Enforcing Coding Standards and Review Style Guides):  
  チームで定めたコーディング規約、API設計ガイドライン、コードレビューの観点やチェックリスト、UIコンポーネントのデザイントークンなどをSpaceに文書化し、実例と共に集約します 24。開発者は、新しいコードを書いたり既存コードをリファクタリングしたりする際に、このSpace内のCopilotに「このコードは規約に準拠していますか？」と尋ねたり、Copilotが変更を提案する際にこれらの規約を参照させたりすることができます。  
  公式ドキュメントでは、ある分野の専門家（Subject Matter Expert）が、チームの内部アクセシビリティチェックリスト、製品ガイドライン、およびWCAG（Web Content Accessibility Guidelines）ドキュメントを含む「アクセシビリティレビュー」という名前のSpaceを作成する例が挙げられています。開発者は、このSpace内で直接Copilotに質問することで、自身が実装している機能が最新のアクセシビリティガイドラインに従っているかを確認できます 24。  
* **日本国内企業・コミュニティでの事例紹介 (Introduction to Use Cases in Japanese Companies/Communities):**  
  * **TIS株式会社 / Fintan.jpの事例:** 学生向けの技術イベントにおいて、GitHub Copilot Chat（Copilot Spacesのコンセプトと類似）を導入し、参加者が開発中のアプリケーションに関するプロジェクト固有情報（ワークスペース内のコード構造の説明、特定の機能の実装方法など）についてAIに質問できる環境を提供しました 32。この事例で特筆すべきは、AIがより正確で有用な回答を生成できるように、README.mdなどのドキュメントの記述方法をAIが理解しやすいように工夫・調整した点です。例えば、ディレクトリ構造を説明する際に、人間には理解しやすいtreeコマンドの出力形式よりも、AIが構造を把握しやすいシンプルなテーブル形式で記述し直すといった対応が行われました。これは、Copilot Spacesの「リファレンス」としてどのような情報をどのように提供するか、そして「インストラクション」でAIの解釈をどう導くか、という観点から非常に示唆に富む知見です。  
  * **株式会社L\&E Groupの事例:** 「コードレビュー\&AI駆動開発ミーティング」を定期的に開催し、GitHub Copilotを用いたコードレビューのあり方や、AIを活用した効率的な実装・レビュー方法の確立についてチーム内で議論・検討を進めていると報告されています 34。このような取り組みにおいて、Copilot Spacesは、議論されたベストプラクティスやノウハウ、具体的なレビュー観点などを集約・共有するための知識基盤として貢献できる可能性があります。  
  * **ZennやQiitaでの個人の試み:** 日本の開発者コミュニティにおいても、Copilot Spacesの可能性を模索する動きが見られます。例えば、あるZennの記事 35 では、複数のオープンソースソフトウェア（OSS）のリポジトリをCopilot Spacesのコンテキストとして追加し、それらのOSS間の機能や特徴を比較分析させるという試みが紹介されています。これは、特定の技術選定や競合製品分析などにおいて、Copilot Spacesが強力なリサーチツールとなり得ることを示す興味深いユースケースです。

### **GitHubチームによる活用例 (Examples from the GitHub Team)**

GitHub自身の開発チームも、Copilot Spacesを積極的にドッグフーディング（自社製品を自ら日常的に使用すること）し、その有効性を検証しています。GitHub Communityのディスカッションで紹介されたいくつかの活用例は、実用的な示唆に富んでいます 15。

* **コードに関する質問応答:** Copilot Spaces開発チームのあるエンジニアは、Spaces機能に関連する全てのソースコードと、過去に行われたSpacesに関するセッションのビデオトランスクリプト（文字起こし）をまとめたSpaceを作成しました。このSpaceは、チーム内でSpacesの内部構造や動作原理に関する質問に答えるために活用されているとのことです（非常にメタな活用例と言えます）。  
* **コーディング標準とベストプラクティスの標準化:** 別のチームでは、エンジニアに対してセキュアコーディングのプラクティスをアドバイスする役割を担うメンバーが、標準的な認証モデルのドキュメント、暗号化技術の正しい使い方、セキュリティレビュープロセスの進め方に関する指示などを集約したSpaceをセットアップしました。これにより、Slackなどで頻繁に繰り返されていた同様の質問への対応負荷を軽減しています。  
* **SQL/KQLクエリ作成支援:** あるプロダクトマネージャーは、自身が得意とするSQL（Structured Query Language）やKQL（Kusto Query Language）のクエリ作成スキルをチームメンバーがセルフサービスで活用できるように、テレメトリデータのスキーマ定義コードや優れたサンプルクエリを含むSpaceを作成しました。これにより、他のメンバーがデータに基づいた意思決定を行うためのクエリ作成やダッシュボード構築を支援しています。  
* **ドキュメント更新作業の効率化:** 課金・ライセンス関連のプロダクトマネージャーは、顧客サポートチャネルやコミュニティのディスカッション投稿を通じて寄せられる質問に基づき、既存のGitHubドキュメントをよりユーザーフレンドリーに更新する作業を行っています。その際、更新対象となるドキュメントのバッチごとにSpaceを作成し、関連する既存コードやGitHub上でホストされているドキュメントをリンクし、さらにインストラクションや頻出する質問とその回答（FAQ）をコンテキストとして追加しています。このSpaceを利用することで、Copilotが更新版ドキュメントの草案を生成し、それをドキュメントリポジトリに簡単にコピーして反映できるようになったと報告されています。

これらのGitHub内部での活用例は、Copilot Spacesが単なるコードの理解や生成を助けるツールに留まらず、チーム内に分散しがちな専門知識をスケールさせ、ドキュメントの作成・維持といった周辺業務を効率化し、さらには組織横断的なナレッジ共有プラットフォームとしての大きな可能性を秘めていることを具体的に示しています。

特に、プロダクトマネージャーがSQL/KQLクエリ作成支援のためのSpaceを構築したり、ドキュメント更新作業にSpaceを活用したりする例は重要です。これは、直接コードを書かない職種のメンバーもCopilot Spacesを有効に活用し、チーム全体の生産性向上や知識共有に貢献できることを示唆しています。技術的なコンテキストだけでなく、プロジェクトの仕様、顧客からのフィードバック、マーケティング資料、営業戦略など、プロジェクト運営に関わる多様な情報をSpacesに集約することで、部門を超えた「集合知」を形成し、それをAIを通じて効率的に活用する新たな働き方が生まれるかもしれません。

## **6\. 他のCopilot機能との比較と連携 (Comparison and Synergy with Other Copilot Features)**

GitHub Copilotは多機能なAI開発支援プラットフォームであり、Copilot Spacesはそのエコシステムの一部です。Spacesの価値を最大限に引き出すためには、他のCopilot機能、特にCopilot Chatやナレッジベース、カスタムインストラクションとの違いを理解し、効果的に連携させることが重要です。

### **Copilot Chatとの違いと効果的な使い分け (Differences from Copilot Chat and Effective Differentiation)**

Copilot Chatは、IDE（統合開発環境）内やGitHub.com上で利用可能な、汎用性の高い対話型AIアシスタントです。開いているファイル、選択範囲、ユーザーからの自然言語による指示など、その時々の状況に応じて動的にコンテキストを解釈し、コードの提案、説明、デバッグ支援などを行います 1。

一方、Copilot Spacesは、特定のタスクやプロジェクトのために、**ユーザーが事前にキュレーションし、永続的に保持されるコンテキストの集合**をCopilot Chatの基盤として提供する、より特化された環境です。Space内でCopilot Chatを利用する場合、その応答はSpaceに定義された情報（関連コード、ドキュメント、インストラクションなど）に強く基づくため、一般的なCopilot Chatよりも専門性が高く、一貫性のある、そしてより深い洞察に基づいた支援が期待できます 1。

両者の効果的な使い分けとしては、以下のようなシナリオが考えられます。

* **Copilot Chat (単独での利用):**  
  * IDEで開いているファイルに関する一時的なコードの疑問点の解消。  
  * 特定のアルゴリズムやプログラミング言語の構文に関する一般的な質問。  
  * 小規模なコードスニペットの生成や、簡単なリファクタリングの提案依頼。  
  * エラーメッセージの簡単な解説依頼。  
* **Copilot Spaces (その中でのCopilot Chat利用):**  
  * 特定のプロジェクト全体のアーキテクチャや、複雑なモジュールの動作原理に関する深い理解が必要なQ\&A。  
  * チーム内で共有された設計思想やコーディング規約に基づいた開発支援。  
  * プロジェクトの仕様書や設計ドキュメントを参照しながらの機能実装に関する相談。  
  * 新規参加メンバーに対する、プロジェクト固有の知識や開発手順に関するオンボーディング支援。  
  * 特定のドメイン知識（例: 金融、医療、ゲーム開発など）を学習させたSpace内での専門的なアドバイス。

日本の開発者によるZennの記事 35 では、通常のCopilot Chat（IDEやGitHub.com上のもの）でも、複数のリポジトリをコンテキストとして選択できる機能が追加されたとの報告があります。これは一見、Copilot Spacesの機能と重複するように見えるかもしれません。しかし、Copilot Spacesの独自の価値は、単に複数の情報源を一時的に参照できる点にあるのではなく、「**永続的で、チームで共有可能、かつ専門家によって意図的にキュレーション（収集・整理）されたコンテキストハブ**」を構築できる点にあると考えられます。つまり、その場限りのコンテキスト指定ではなく、特定の目的のために最適化された知識空間を事前に定義し、それを繰り返し利用したりチームで共有したりできる点が、Spacesの大きな特徴と言えるでしょう。

### **ナレッジベースとの違いとそれぞれの最適な用途 (Differences from Knowledge Bases and Optimal Use Cases for Each)**

GitHub Copilot Enterpriseプランの機能として提供されている「ナレッジベース」も、Copilotに特定のコンテキストを提供するための仕組みですが、Copilot Spacesとは対象ユーザー、扱えるコンテンツの種類、コンテキストの管理方法においていくつかの重要な違いがあります。

**表: Copilot Spaces vs. ナレッジベース比較**

| 項目 | Copilot Spaces | ナレッジベース (Copilot Enterprise) |
| :---- | :---- | :---- |
| **作成権限** | Copilotライセンスを持つ全てのユーザー 11 | 組織オーナーのみ 4 |
| **所有者** | 個人アカウント または 組織 1 | 組織のみ 4 |
| **コンテンツタイプ** | リポジトリ内のコード、自由記述テキスト（議事録、Slackスレッド、ノートなど多様） 1 | GitHub上でホストされたMarkdownファイル形式のドキュメント 4 |
| **コンテキストの扱い** | サイズ制限あり（高品質な応答を優先するため、意図的に絞り込まれる）11 | サイズ制限なし（ただし、コンテキストが広大すぎると応答品質が低下する可能性）11 |
| **最適な用途の例** | 特定タスクへの集中、プロジェクト固有の動的な情報共有、チーム内での非公式な知識集約、オンボーディング支援 | 組織全体の公式ドキュメントに基づくQ\&A、社内規定や標準プロセスの参照、大規模な静的ドキュメント群の検索 |

この比較から、Copilot Spacesとナレッジベースは競合するものではなく、むしろ補完関係にあると理解できます。\*\*Copilot Spacesは、より動的でタスク指向の「作業場」や「プロジェクトルーム」\*\*のような役割を担い、進行中のプロジェクトに関連する多様な情報をリアルタイムに近い形で扱います。一方、\*\*ナレッジベースは、より静的で公式な「参照図書館」や「アーカイブ」\*\*として機能し、組織として確立された情報や規定を参照するのに適しています。

例えば、「当社の公式APIドキュメントの最新版について知りたい」といった場合は、ナレッジベースが適切な情報源となるでしょう。それに対し、「現在開発中の新機能Xの仕様と、それに関連する未マージのブランチYのコードについて議論し、実装方針を検討したい」といった場合は、Copilot Spacesがそのための最適な環境を提供します。また、Spacesの「インストラクション」機能は、ナレッジベースには見られない、その場その場のAIの振る舞いをより細かく制御する能力を提供し、タスク特化性を高めます。

### **カスタムインストラクション（リポジトリ、パーソナル、オーガニゼーション）との関係性 (Relationship with Custom Instructions \- Repository, Personal, Organization)**

GitHub Copilotは、ユーザーやプロジェクトの特性に合わせて応答を調整するために、複数の階層からなるカスタムインストラクションの仕組みを提供しています 1。これらは、Copilot Spacesの「インストラクション」機能と密接に関連し、連携して動作すると考えられます。

既存のカスタムインストラクションの階層は以下の通りです。

1. **パーソナルカスタムインストラクション:** GitHubウェブサイト上の全てのCopilot Chat会話に適用され、個々のユーザーの好み（例えば、優先的に使用するプログラミング言語、応答のトーンや詳細度など）を反映します 43。  
2. **リポジトリカスタムインストラクション:** 特定のGitHubリポジトリ内に .github/copilot-instructions.md というファイル名で配置され、そのリポジトリをコンテキストとした会話に適用されます。プロジェクト固有のコーディング標準、使用フレームワーク、ライブラリのバージョン情報などを定義するのに役立ちます 41。  
3. **オーガニゼーションカスタムインストラクション:** (パブリックプレビュー、Copilot Enterprise限定機能) GitHub Organization全体に適用され、組織としての方針（例えば、全社共通のセキュリティガイドライン、特定の技術スタックの推奨など）をCopilotの応答に反映させるために使用されます 43。

これらのカスタムインストラクションは、**パーソナル \> リポジトリ \> オーガニゼーション** の順で優先度が高いとされています。ただし、これは単純な上書き関係ではなく、関連する全ての階層の指示セットが結合されてCopilot Chatにコンテキストとして提供されると説明されています 43。

Copilot Spacesの「インストラクション」機能は、この既存の階層にさらに細かい粒度での制御を加えるものと位置づけられます。公式ドキュメント 1 やGitHubブログ 12 では、Spaceごとに独自の「インストラクション」を設定できることが明記されており、「Space内のカスタムCopilotインストラクション」という表現も用いられています。

これらの情報から、Spacesの「インストラクション」は、そのSpace内での対話において、最も特異性の高い（つまり、そのSpaceの目的に最も強く関連づけられた）指示として機能すると考えられます。既存のグローバルなカスタムインストラクション階層（パーソナル、リポジトリ、オーガニゼーション）とSpacesのインストラクションが具体的にどのように相互作用するか、例えば、Spaceの指示がパーソナル指示を完全に上書きするのか、あるいは補完的に働くのかといった詳細な動作については、さらなる公式情報や実証的な検証が待たれるところです。しかし、論理的には、よりスコープの狭いSpace固有の指示が、そのSpace内でのAIの振る舞いに対して最も強い影響力を持つか、少なくとも非常に優先的に考慮されると推測するのが自然でしょう。

この多層的な指示システムは、Copilot Spacesを既存のカスタムインストラクションシステムをさらに細分化し、特定の「作業空間」や「タスクコンテキスト」に最適化されたAIの振る舞いを定義するための強力なツールとします。これにより、グローバルな設定（例：個人として常に丁寧語で回答してほしい）と、よりローカルなSpace固有の設定（例：このSpaceでは特定のAPIドキュメントのスタイルで技術的な解説をしてほしい）を組み合わせることで、より洗練され、状況に応じたコンテキスト制御が可能になります。

例えば、あるリポジトリのカスタムインストラクションで「常にPythonで回答するように」と設定されていたとしても、そのリポジトリのコードを参照しつつ特定のJavaScriptフロントエンド機能について議論するために作成されたSpaceでは、「このSpace内ではJavaScriptのフロントエンド開発に関する質問が主なので、JavaScriptのコード例を中心に、Reactのベストプラクティスを交えて回答してください」といったインストラクションを与えることで、Space内ではJavaScript中心の、より目的に合致した応答が期待できるようになります。

ただし、このような多層的な指示システムは強力である反面、複数の指示が複雑に絡み合うことによる意図しないAIの挙動や、設定管理の煩雑化といった新たな課題を生じさせる可能性も考慮に入れる必要があります。ユーザーは、各階層の指示が最終的なAIの応答にどのように影響を与えるかを理解し、意図しない指示の競合を避けるよう注意深く設計・管理することが求められるでしょう。

**表: 各種カスタムインストラクションの優先順位と適用範囲（Spacesインストラクションの位置づけは現時点での考察を含む）**

| インストラクション種別 | 適用範囲 | 設定場所 | 主な目的 | 優先順位 (高い順) |
| :---- | :---- | :---- | :---- | :---- |
| **Spaces内インストラクション** | 特定のCopilot Space内での対話 | 各Spaceの設定画面内 | Space固有のタスク、役割、応答スタイルを定義 | 1 (最優先と推測) |
| パーソナルカスタムインストラクション | GitHub.com上の全てのCopilot Chat会話 | GitHub.comのCopilot設定 | 個人の応答スタイル、言語設定など | 2 |
| リポジトリカスタムインストラクション | 特定のリポジトリをコンテキストとする会話 | リポジトリ内の .github/copilot-instructions.md ファイル | プロジェクト固有のコーディング規約、技術スタック、参照すべきドキュメントの指示 | 3 |
| オーガニゼーションカスタムインストラクション | (Copilot Enterprise) 組織全体のCopilot Chat会話 | Organization設定 (GitHub.com) | 組織全体の標準、セキュリティポリシー、推奨事項の指示 | 4 |

この表は、ユーザーがCopilotの応答をカスタマイズするための多様な方法を理解し、それぞれの特性に応じて使い分けるための指針となります。特に、Copilot Spacesのインストラクションが既存の階層とどのように連携し、影響し合うのかを明確に把握することが、Spacesを効果的に活用する上で重要となります。

## **7\. 現状の課題、制限事項と今後の展望 (Current Challenges, Limitations, and Future Outlook)**

Copilot Spacesは革新的な機能である一方、パブリックプレビュー段階であるため、いくつかの留意点や制限事項が存在し、また今後の発展も期待されます。

### **パブリックプレビュー版としての留意点とフィードバックの重要性 (Considerations for the Public Preview and Importance of Feedback)**

Copilot Spacesは現在パブリックプレビューとして提供されており、これは機能がまだ完全には安定しておらず、今後ユーザーからのフィードバックを元に変更・改善されていく段階であることを意味します 1。したがって、利用者は予期せぬ動作や機能不足に遭遇する可能性があります。

GitHubは、このプレビュー期間中のユーザーからの積極的なフィードバックを重視しており、製品改善のための貴重な情報源と位置付けています。ユーザーは、GitHub Communityの関連ディスカッションフォーラム 15 や、Copilot Spacesインターフェース内に設けられているインラインフィードバックボタンを通じて、使用感、バグ報告、機能要望などを送信することが推奨されています。

### **コンテキストサイズに関する制限（判明している範囲）と対策 (Context Size Limitations (as known) and Potential Workarounds)**

Copilot Spacesの大きな特徴の一つは、厳選されたコンテキストに基づいて高品質な応答を目指す点であり、そのためにコンテキストサイズが「限定されている」と公式に述べられています 11。これは、無制限に情報を扱えるが応答品質が低下する可能性があるナレッジベースとの明確な違いとして強調されています 11。しかし、現時点の公開情報では、この「限定されたサイズ」が具体的なトークン数やファイル数としてどの程度なのかは明示されていません 13。

* **影響:** この制限により、非常に大規模なリポジトリ全体や、膨大な量のドキュメント群を単一のSpaceに一度にコンテキストとして含めようとすると、上限に達してしまい、期待した情報すべてをAIが参照できない可能性があります。  
* **対策・ベストプラクティス:**  
  1. **タスクの細分化とSpaceの分割:** 複雑なプロジェクトや広範な知識領域を扱う場合、全体を一つの巨大なSpaceでカバーしようとするのではなく、より小さなサブタスクや特定の目的に特化した複数のSpaceに分割することを検討します。これは、GitHub Copilot全般における効果的なプロンプト戦略としても推奨されているアプローチです 25。  
  2. **コンテキストの戦略的な厳選:** Spaceに追加するリファレンス（コード、ドキュメント）やインストラクションは、そのSpaceの目的にとって真に関連性が高く、かつAIが効果的に解釈できるものに絞り込むことが重要です。TIS/Fintan.jpの事例 32 で見られたように、単に情報を投入するだけでなく、AIが理解しやすいようにドキュメントの形式を調整したり、冗長な情報を削除したりするキュレーション作業が有効です。  
  3. **段階的な情報提供と対話の活用:** 一度に全ての情報をAIに与えようとするのではなく、初期コンテキストを基に対話を開始し、必要に応じて追加の情報をチャットで提供したり、リファレンスを更新したりするなど、段階的にコンテキストを構築していくアプローチも考えられます。  
  4. **LLMのトークン制限への一般的な留意:** GitHub Copilot for Azureのトークン管理に関する議論 50 や、RStudio環境でのGitHub Copilot利用時におけるトークン上限への言及 52 は、大規模言語モデル（LLM）を利用するシステムに共通の課題としてトークン制限が存在することを示唆しています。Copilot SpacesもLLMを基盤としている以上、同様の制約を意識した利用が求められるでしょう。  
  5. **過去の類似機能からの学び:** かつて提供されていたCopilot Workspaceの既知の問題として、大きなファイルの書き換え処理に時間がかかったり、非常に巨大なリポジトリの解析に課題があったりしたこと 53 も、コンテキストサイズがパフォーマンスや実用性に影響を与える可能性を示唆しています。

コンテキストサイズの制限は、Copilot Spacesが高品質な応答を提供するための設計思想と表裏一体の関係にあります。ユーザーは「何でもSpaceに入れれば良い」というわけではなく、「何を、どのようにSpaceに含め、AIに解釈させるべきか」という戦略的なキュレーション能力が求められます。これがCopilot Spacesを効果的に使いこなす上での鍵となり、今後、コミュニティやGitHub自身から、より具体的なベストプラクティスやノウハウが共有されていくことが期待されます。LLMは一般的に入力トークン数に上限があり 54、この上限を超えると情報を処理できません。また、仮に処理できたとしても、コンテキストが過大になると、関連性の低い情報にAIの注意が分散し、応答の焦点がぼやけたり、不正確になったりする「干し草の中の針を探す」ような問題が発生しやすくなります。Spacesが「限定されたサイズ」というアプローチを採用したのは、まさにこの応答品質の低下を避けるためと考えられます。したがって、ユーザーはSpaceの明確な目的に合わせて含める情報を厳選し、さらに「インストラクション」機能を用いてAIの注意を適切に誘導する必要があります。将来的には、Space内でさらにコンテキスト要素の優先度付けを行ったり、対話の流れに応じて動的に参照するコンテキストを選択したりするような、より高度なコンテキスト管理機能が導入されることも期待されるかもしれません。

### **ロードマップと期待される新機能（例：Issueのコンテキスト追加）(Roadmap and Anticipated New Features \- e.g., adding Issues to context)**

Copilot Spacesはまだ開発の初期段階にあり、今後の機能拡張が期待されます。

* **GitHub Issuesのコンテキストとしての統合:** GitHub Communityの公式なディスカッションにおいて、将来的にはGitHub IssuesをCopilot Spacesのコンテキストとして追加する予定であると言及されています 15。これが実現すれば、Issueに記述されたバグ報告の詳細、機能要求の背景、関連する議論の経緯などをCopilotが直接参照しながら、開発者と対話し、解決策を共に検討できるようになります。  
* **Copilot Workspaceとの関連性:** 2025年5月30日に技術プレビューが終了したCopilot Workspace 56 は、GitHub Issueを起点として、AIが開発計画を立案し、コードを生成・テストし、プルリクエストを作成するまでの一連のタスクを支援することを目的としていました 56。Copilot SpacesがIssueをコンテキストとして取り込めるようになれば、かつてのCopilot Workspaceが目指したタスク中心の開発支援の思想を、より柔軟な形で一部継承し、発展させる可能性があります。  
* **GitHub Nextからの示唆:** GitHubが将来的な技術や実験的なプロジェクトを紹介するGitHub Nextのページ 58 は、Copilotチームが現在検討しているベータレベルのプロジェクトやコンセプトの概要を示しており、Copilot Spacesのさらなる進化の方向性を示唆する情報が含まれているかもしれません。

GitHub Issuesのコンテキスト統合は、Copilot Spacesを単なる情報参照やコード理解のためのツールから、より能動的な開発タスク実行支援ツールへと進化させるための重要な一歩と言えるでしょう。これにより、開発プロセスの初期段階であるIssueの正確な理解から、具体的な実装、そしてテストに至るまで、一貫したコンテキストの下でAIの支援を途切れることなく受けられるようになることが期待されます。例えば、「このIssueで報告されているバグの最も可能性の高い原因箇所を、Space内の関連コードファイルから特定し、修正案を提示してください」といった、より具体的で実践的な指示がCopilotに対して可能になるかもしれません。これは、GitHub Copilot Coding Agent 1 との連携を深め、Issueに基づいたタスクの自動化や半自動化が、よりスムーズかつ効果的に進む未来を示唆しています。

## **8\. まとめ (Conclusion)**

### **GitHub Copilot Spacesの総括と開発者への推奨事項 (Summary of GitHub Copilot Spaces and Recommendations for Developers)**

GitHub Copilot Spacesは、GitHub Copilotの進化における新たなマイルストーンであり、開発者が直面する情報の断片化という課題に対応し、AIによる開発支援を次のレベルへと引き上げる可能性を秘めた機能です。特定のタスクやプロジェクトに必要なコード、ドキュメント、メモ、そしてAIへの指示（インストラクション）を一元的に集約し、その厳選されたコンテキストに基づいてCopilotがより的確で質の高い応答を提供することを可能にします。これにより、開発者はコーディングの効率化だけでなく、複雑な問題の理解、チーム内での知識共有、そして新規メンバーのオンボーディングといった多様な側面で恩恵を受けることが期待できます。

Copilot Spacesは、単に情報を集める場所ではなく、AIを特定の主題に関する「専門家」へと育成し、その専門知識をチーム全体で活用するためのプラットフォームとしての役割を担います。特に、インストラクション機能によるAIの振る舞いのカスタマイズや、リポジトリの最新コードを常に参照する動的なコンテキスト維持は、これまでのAI支援ツールにはないユニークな価値を提供します。

開発者がCopilot Spacesを最大限に活用するためには、以下の点が推奨されます。

1. 積極的な試用とフィードバック:  
   Copilot Spacesは現在パブリックプレビュー段階です。この期間を捉え、自身の開発ワークフローやチームのプロジェクトに積極的に導入し、どのようなユースケースで効果を発揮するのかを実体験を通じて評価することが重要です。その過程で得られた知見や改善要望は、GitHub Communityやフィードバックチャネルを通じて提供することで、製品のさらなる発展に貢献できます。  
2. コンテキストの質と量の最適化:  
   「Garbage In, Garbage Out」の原則はAI支援ツールにも当てはまります。Spaceに追加する情報は、量よりも質を重視し、そのSpaceの目的にとって真に関連性の高いものに厳選する必要があります。また、インストラクション機能を効果的に活用し、AIの役割、応答スタイル、注意すべき点などを明確に指示することで、期待する応答を得やすくなります。AIが理解しやすいようにドキュメントの形式を工夫することも有効な戦略です。  
3. チームでの戦略的な活用検討:  
   個人での利用も有効ですが、Copilot Spacesの真価はチームでの知識共有とコラボレーション促進において発揮されやすいと考えられます。新規メンバーのオンボーディング資料の集約とQ\&A対応、複雑なシステムアーキテクチャやドメイン知識の共有リポジトリとしての活用、チーム共通のコーディング規約やデザインパターンの参照・徹底など、チーム内に散在しがちな「暗黙知」を形式知化し、専門知識をスケールさせる手段として戦略的に活用を検討すべきです。  
4. 他のCopilot機能との連携の模索:  
   Copilot Spacesは、GitHub Copilotエコシステムの一部です。IDE内でのCopilot Chat、リポジトリカスタムインストラクションやパーソナルカスタムインストラクション、そして将来的にはCopilot Coding Agentなど、他のCopilot機能とSpacesを組み合わせることで、より包括的で高度なAI開発支援環境を構築できる可能性があります。それぞれの機能の特性を理解し、タスクに応じて最適なツールや設定を選択することが求められます。  
5. 継続的な最新情報のキャッチアップ:  
   パブリックプレビューであるCopilot Spacesの機能や仕様は、今後も継続的に変化・進化していくことが予想されます。GitHub BlogのChangelog 12 や公式ドキュメント 1 を定期的に確認し、最新の機能やベストプラクティスを把握し続けることが、Copilot Spacesを効果的に活用し続ける上で不可欠です。

GitHub Copilot Spacesは、開発のあり方を大きく変える可能性を秘めたツールです。その能力を理解し、賢明に活用することで、開発者はより創造的で価値の高い作業に集中し、ソフトウェア開発の生産性と質を新たな次元へと高めることができるでしょう。

#### **引用文献**

1. Creating and using Copilot Spaces \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/creating-and-using-copilot-spaces)  
2. Copilot Spaces \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces)  
3. GitHub Copilot · Your AI pair programmer, 5月 31, 2025にアクセス、 [https://github.com/features/copilot](https://github.com/features/copilot)  
4. GitHub Copilot features, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features](https://docs.github.com/en/copilot/about-github-copilot/github-copilot-features)  
5. What is GitHub Copilot?, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot](https://docs.github.com/en/copilot/about-github-copilot/what-is-github-copilot)  
6. Visual Studio With GitHub Copilot \- AI Pair Programming \- Microsoft, 5月 31, 2025にアクセス、 [https://visualstudio.microsoft.com/github-copilot/](https://visualstudio.microsoft.com/github-copilot/)  
7. 8 things you didn't know you could do with GitHub Copilot, 5月 31, 2025にアクセス、 [https://github.blog/developer-skills/github/8-things-you-didnt-know-you-could-do-with-github-copilot/](https://github.blog/developer-skills/github/8-things-you-didnt-know-you-could-do-with-github-copilot/)  
8. GitHub Copilot Pros and Cons, 5月 31, 2025にアクセス、 [https://www.netguru.com/blog/github-copilot](https://www.netguru.com/blog/github-copilot)  
9. The Ultimate Guide to Using Github Copilot \- Hatica, 5月 31, 2025にアクセス、 [https://www.hatica.io/blog/how-to-use-github-copilot/](https://www.hatica.io/blog/how-to-use-github-copilot/)  
10. Measuring Impact of GitHub Copilot, 5月 31, 2025にアクセス、 [https://resources.github.com/learn/pathways/copilot/essentials/measuring-the-impact-of-github-copilot/](https://resources.github.com/learn/pathways/copilot/essentials/measuring-the-impact-of-github-copilot/)  
11. About organizing and sharing context with Copilot Spaces \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/copilot/using-github-copilot/copilot-spaces/about-organizing-and-sharing-context-with-copilot-spaces](https://docs.github.com/copilot/using-github-copilot/copilot-spaces/about-organizing-and-sharing-context-with-copilot-spaces)  
12. Introducing Copilot Spaces: A new way to work with code and context \- GitHub Changelog, 5月 31, 2025にアクセス、 [https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/](https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context/)  
13. About organizing and sharing context with Copilot Spaces \- GitHub ..., 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/about-organizing-and-sharing-context-with-copilot-spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/about-organizing-and-sharing-context-with-copilot-spaces)  
14. Introducing Copilot Spaces: A new way to work with code and context \- GitHub Changelog, 5月 31, 2025にアクセス、 [https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context](https://github.blog/changelog/2025-05-29-introducing-copilot-spaces-a-new-way-to-work-with-code-and-context)  
15. Introducing Copilot Spaces: A new way to work with context \#160840 \- GitHub, 5月 31, 2025にアクセス、 [https://github.com/orgs/community/discussions/160840](https://github.com/orgs/community/discussions/160840)  
16. Speeding up development work with Copilot Spaces \- GitHub ..., 5月 31, 2025にアクセス、 [https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces](https://docs.github.com/en/enterprise-cloud@latest/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces)  
17. Speeding up development work with Copilot Spaces \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/speeding-up-development-work-with-copilot-spaces)  
18. How to measure GitHub Copilot's impact on productivity \- Plandek, 5月 31, 2025にアクセス、 [https://plandek.com/blog/copilot-on-engineering-productivity/](https://plandek.com/blog/copilot-on-engineering-productivity/)  
19. GitHub Copilot Review with Practical Examples \- Apriorit, 5月 31, 2025にアクセス、 [https://www.apriorit.com/dev-blog/github-copilot-review](https://www.apriorit.com/dev-blog/github-copilot-review)  
20. Experience with GitHub Copilot for Developer Productivity at Zoominfo \- arXiv, 5月 31, 2025にアクセス、 [https://arxiv.org/html/2501.13282v1](https://arxiv.org/html/2501.13282v1)  
21. How To Use GitHub Copilot With Python | Guide by Hostman, 5月 31, 2025にアクセス、 [https://hostman.com/tutorials/how-to-use-github-copilot-with-python/](https://hostman.com/tutorials/how-to-use-github-copilot-with-python/)  
22. Measuring GitHub Copilot's Impact on Productivity \- Communications of the ACM, 5月 31, 2025にアクセス、 [https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/](https://cacm.acm.org/research/measuring-github-copilots-impact-on-productivity/)  
23. Is GitHub Copilot Worth It? Expert Opinions and Real-World Application, 5月 31, 2025にアクセス、 [https://flyaps.com/blog/is-github-copilot-worth-it-expert-opinions-and-real-world-application/](https://flyaps.com/blog/is-github-copilot-worth-it-expert-opinions-and-real-world-application/)  
24. Collaborating with your team using Copilot Spaces \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/collaborating-with-your-team-using-copilot-spaces](https://docs.github.com/en/copilot/using-github-copilot/copilot-spaces/collaborating-with-your-team-using-copilot-spaces)  
25. Best practices for using GitHub Copilot, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot](https://docs.github.com/en/copilot/using-github-copilot/best-practices-for-using-github-copilot)  
26. Multiple new models are now generally available in GitHub Copilot ..., 5月 31, 2025にアクセス、 [https://github.blog/changelog/2025-04-04-multiple-new-models-are-now-generally-available-in-github-copilot/](https://github.blog/changelog/2025-04-04-multiple-new-models-are-now-generally-available-in-github-copilot/)  
27. GitHub Copilot app modernization \- upgrade for .NET now in public preview, 5月 31, 2025にアクセス、 [https://github.blog/changelog/2025-05-19-github-copilot-app-modernization-upgrade-for-net-now-in-public-preview/](https://github.blog/changelog/2025-05-19-github-copilot-app-modernization-upgrade-for-net-now-in-public-preview/)  
28. Copilot code review: Better coverage and more control \- GitHub Changelog, 5月 31, 2025にアクセス、 [https://github.blog/changelog/2025-05-28-copilot-code-review-better-coverage-and-more-control/](https://github.blog/changelog/2025-05-28-copilot-code-review-better-coverage-and-more-control/)  
29. About individual Copilot plans and benefits \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-started-with-copilot-on-your-personal-account/about-individual-copilot-plans-and-benefits](https://docs.github.com/en/copilot/managing-copilot/managing-copilot-as-an-individual-subscriber/getting-started-with-copilot-on-your-personal-account/about-individual-copilot-plans-and-benefits)  
30. Plans for GitHub Copilot \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot](https://docs.github.com/en/copilot/about-github-copilot/plans-for-github-copilot)  
31. Managing policies for Copilot in your organization \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization](https://docs.github.com/en/copilot/managing-copilot/managing-github-copilot-in-your-organization/managing-policies-for-copilot-in-your-organization)  
32. AI初学者向けGitHub Copilot導入事例 \- Fintan, 5月 31, 2025にアクセス、 [https://fintan.jp/page/13367/](https://fintan.jp/page/13367/)  
33. Training and onboarding developers on GitHub Copilot, 5月 31, 2025にアクセス、 [https://github.com/resources/whitepapers/training-and-onboarding-developers-on-github-copilot](https://github.com/resources/whitepapers/training-and-onboarding-developers-on-github-copilot)  
34. 「GitHub Copilot」「Devin」などAIを活用した開発とコードレビューへの取り組み【第1回コードレビュー\&AI駆動開発ミーティング】 \- 株式会社L\&E Group, 5月 31, 2025にアクセス、 [https://legrp.co.jp/media20250430/](https://legrp.co.jp/media20250430/)  
35. GitHub Copilot Spacesの使い道を考えたい \- Zenn, 5月 31, 2025にアクセス、 [https://zenn.dev/kesin11/articles/20250530\_copilot\_spaces](https://zenn.dev/kesin11/articles/20250530_copilot_spaces)  
36. Responsible use of GitHub Copilot Chat in your IDE, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-chat-in-your-ide](https://docs.github.com/en/copilot/responsible-use-of-github-copilot-features/responsible-use-of-github-copilot-chat-in-your-ide)  
37. How to use GitHub Copilot: What it can do and real-world examples, 5月 31, 2025にアクセス、 [https://github.blog/ai-and-ml/github-copilot/what-can-github-copilot-do-examples/](https://github.blog/ai-and-ml/github-copilot/what-can-github-copilot-do-examples/)  
38. GitHub Copilot vs. ChatGPT: Developer AI Tools Comparison \- Spacelift, 5月 31, 2025にアクセス、 [https://spacelift.io/blog/github-copilot-vs-chatgpt](https://spacelift.io/blog/github-copilot-vs-chatgpt)  
39. What's The Difference Between GitHub Copilot Chat and GitHub Copilot ? : r/GithubCopilot \- Reddit, 5月 31, 2025にアクセス、 [https://www.reddit.com/r/GithubCopilot/comments/1j0opec/whats\_the\_difference\_between\_github\_copilot\_chat/](https://www.reddit.com/r/GithubCopilot/comments/1j0opec/whats_the_difference_between_github_copilot_chat/)  
40. Asking GitHub Copilot questions in your IDE \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/asking-github-copilot-questions-in-your-ide](https://docs.github.com/en/copilot/using-github-copilot/copilot-chat/asking-github-copilot-questions-in-your-ide)  
41. Tips and tricks for Copilot in VS Code, 5月 31, 2025にアクセス、 [https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks](https://code.visualstudio.com/docs/copilot/copilot-tips-and-tricks)  
42. Managing Copilot knowledge bases \- GitHub Enterprise Cloud Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/enterprise-cloud@latest/copilot/customizing-copilot/managing-copilot-knowledge-bases](https://docs.github.com/en/enterprise-cloud@latest/copilot/customizing-copilot/managing-copilot-knowledge-bases)  
43. Adding personal custom instructions for GitHub Copilot \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-personal-custom-instructions-for-github-copilot)  
44. Adding repository custom instructions for GitHub Copilot \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot](https://docs.github.com/en/copilot/customizing-copilot/adding-repository-custom-instructions-for-github-copilot)  
45. About customizing GitHub Copilot Chat responses, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses](https://docs.github.com/en/copilot/customizing-copilot/about-customizing-github-copilot-chat-responses)  
46. GitHub Copilot Features Explained \- Nathan Nellans, 5月 31, 2025にアクセス、 [https://www.nathannellans.com/post/github-copilot-features-explained](https://www.nathannellans.com/post/github-copilot-features-explained)  
47. Master React Coding with GitHub Copilot: A Simple Guide to ..., 5月 31, 2025にアクセス、 [https://dev.to/vigneshiyergithub/master-react-coding-with-github-copilot-a-simple-guide-to-custom-instructions-e38](https://dev.to/vigneshiyergithub/master-react-coding-with-github-copilot-a-simple-guide-to-custom-instructions-e38)  
48. Context is all you need: Better AI results with custom instructions \- Visual Studio Code, 5月 31, 2025にアクセス、 [https://code.visualstudio.com/blogs/2025/03/26/custom-instructions](https://code.visualstudio.com/blogs/2025/03/26/custom-instructions)  
49. VS Code 1.10 Showcases New, Detailed Markdown Copilot Prompting \- Visual Studio Magazine, 5月 31, 2025にアクセス、 [https://visualstudiomagazine.com/articles/2025/05/12/vs-code-1-10-showcases-detailed-markdown-copilot-prompting.aspx](https://visualstudiomagazine.com/articles/2025/05/12/vs-code-1-10-showcases-detailed-markdown-copilot-prompting.aspx)  
50. Managing Token Consumption with GitHub Copilot for Azure | Microsoft Community Hub, 5月 31, 2025にアクセス、 [https://techcommunity.microsoft.com/blog/azuredevcommunityblog/managing-token-consumption-with-github-copilot-for-azure/4397885](https://techcommunity.microsoft.com/blog/azuredevcommunityblog/managing-token-consumption-with-github-copilot-for-azure/4397885)  
51. GitHub Copilot for Azure: Set token limits for your GenAI APIs \- YouTube, 5月 31, 2025にアクセス、 [https://www.youtube.com/watch?v=B7w9WW1gaYM](https://www.youtube.com/watch?v=B7w9WW1gaYM)  
52. GitHub Copilot – RStudio User Guide \- Posit Docs, 5月 31, 2025にアクセス、 [https://docs.posit.co/ide/user/ide/guide/tools/copilot.html](https://docs.posit.co/ide/user/ide/guide/tools/copilot.html)  
53. copilot-workspace-user-manual/known-issues.md at main \- GitHub, 5月 31, 2025にアクセス、 [https://github.com/githubnext/copilot-workspace-user-manual/blob/main/known-issues.md](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/known-issues.md)  
54. YAML完全活用マニュアル AIエージェント開発とプロンプト工学の次世代標準｜hirokaji \- note, 5月 31, 2025にアクセス、 [https://note.com/tasty\_dunlin998/n/nd350adfaa0e8](https://note.com/tasty_dunlin998/n/nd350adfaa0e8)  
55. 大規模言語モデルを自作しよう！(Transformers+DeepSpeed+torch.compile+flash\_attn2）, 5月 31, 2025にアクセス、 [https://zenn.dev/selllous/articles/transformers\_pretrain\_to\_ft](https://zenn.dev/selllous/articles/transformers_pretrain_to_ft)  
56. Copilot Workspace \- GitHub Next, 5月 31, 2025にアクセス、 [https://githubnext.com/projects/copilot-workspace](https://githubnext.com/projects/copilot-workspace)  
57. GitHub Copilot Workspace: Welcome to the Copilot-native developer environment, 5月 31, 2025にアクセス、 [https://github.blog/news-insights/product-news/github-copilot-workspace/](https://github.blog/news-insights/product-news/github-copilot-workspace/)  
58. Is there a copilot roadmap anywhere? Or an insider that knows things :) : r/GithubCopilot, 5月 31, 2025にアクセス、 [https://www.reddit.com/r/GithubCopilot/comments/11ts97l/is\_there\_a\_copilot\_roadmap\_anywhere\_or\_an\_insider/](https://www.reddit.com/r/GithubCopilot/comments/11ts97l/is_there_a_copilot_roadmap_anywhere_or_an_insider/)  
59. Best practices for using Copilot to work on tasks \- GitHub Docs, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks](https://docs.github.com/en/copilot/using-github-copilot/coding-agent/best-practices-for-using-copilot-to-work-on-tasks)  
60. Modernizing legacy code with GitHub Copilot, 5月 31, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/modernizing-legacy-code-with-github-copilot](https://docs.github.com/en/copilot/using-github-copilot/guides-on-using-github-copilot/modernizing-legacy-code-with-github-copilot)  
61. copilot-workspace-user-manual/troubleshooting.md at main \- GitHub, 5月 31, 2025にアクセス、 [https://github.com/githubnext/copilot-workspace-user-manual/blob/main/troubleshooting.md](https://github.com/githubnext/copilot-workspace-user-manual/blob/main/troubleshooting.md)