---
layout: topic
title: "Anthropic Claude Code 詳細調査報告：VSCode及びGitHub Actions連携の深掘り"
date: 2025-05-25
tags: [Anthropic,Claude Code,VSCode,GitHub Actions]
audio: "/share-deepresearch/assets/audio/claude-code-research.mp3"
---

# **Anthropic Claude Code 詳細調査報告：VSCode及びGitHub Actions連携の深掘り**

## **1\. はじめに**

本報告書は、Anthropicによって開発されたエージェント型コーディングツール「Claude Code」に関する詳細な調査結果をまとめたものです。Claude Codeは、開発者のターミナル内で動作し、コードベース全体を理解し、自然言語コマンドを通じてコーディング作業を高速化することを目的としています 1。特に本報告書では、Visual Studio Code (VSCode) とGitHub Actionsとの連携に焦点を当て、その機能、設定方法、具体的な使用例、そして開発ワークフローへの影響について深掘りします。

Claude Codeは、単なるコード生成ツールを超え、コードの編集、バグ修正、テスト実行、Git操作の自動化など、多岐にわたる開発タスクを支援する能力を有しています 1。このツールが開発者の生産性向上にどのように貢献しうるのか、また、既存の開発エコシステムとどのように統合されるのかを明らかにすることが、本報告書の目的です。

## **2\. Anthropic Claude Codeの概要**

### **2.1. コア機能と特徴**

Claude Codeは、開発者のターミナルに常駐し、自然言語による指示を通じてコーディングプロセスを支援するエージェント型ツールです 1。その中核的な機能は以下の通りです。

* **コード編集とバグ修正**: コードベース全体にわたるファイルの編集やバグの修正を実行します 1。  
* **コード理解**: コードのアーキテクチャやロジックに関する質問に回答します 1。  
* **テストとコマンド実行**: テストの実行と修正、リンティング、その他のコマンド操作をサポートします 1。  
* **Git操作**: Git履歴の検索、マージコンフリクトの解決、コミットやプルリクエスト（PR）の作成を自動化します 1。  
* **Web検索によるドキュメント参照**: Web検索を用いてドキュメントやリソースを閲覧します 1。  
* **エンタープライズ統合**: Amazon BedrockやGoogle Vertex AIとの連携により、エンタープライズレベルのセキュアなデプロイメントが可能です 1。  
* **コンテキスト理解と自律的行動**: プロジェクトのコンテキストを理解し、手動でファイルコンテキストを追加する必要なく、必要に応じてコードベースを探索し、実際の操作（ファイル編集やコミット作成など）を実行します 1。

これらの機能は、開発者が反復的なタスクから解放され、より複雑で創造的な問題解決に集中できるよう支援することを目的としています。特に、コードベース全体を自律的に探索し、コンテキストを把握する能力は、大規模プロジェクトや馴染みのないコードベースを扱う際に大きな利点となります。

### **2.2. 対応モデルとパフォーマンス**

Claude Codeは、Anthropicの強力な基盤モデルを活用しており、特にコーディングタスクに最適化されたモデルが利用可能です。主に以下のモデルが使用されます。

* **Claude Opus 4**: 最も高性能なモデルであり、複雑な分析、多数のステップを伴うタスク、高度な数学的およびコーディングタスクに対応します 2。Claude Codeに組み込まれ、深いコードベース認識と直接的なファイル編集・コマンド実行能力を提供します 3。GitHubのCEOであるThomas Dohmke氏は、Claude Opus 4が他のモデルでは解決できない複雑な課題を解決し、以前のモデルが見逃していた重要なアクションを成功裏に処理する能力は、開発ワークフローにとって変革的であると評価しています 3。  
* **Claude Sonnet 4**: インテリジェンス、コスト、速度の最適なバランスを提供し、効率的で高スループットなタスクに適しています 2。SWE-bench Verifiedで72.7%のスコアを記録し、コーディング能力の高さが示されています 3。GitHub Copilotの初期内部評価では、適応的なツール使用、正確な指示追従、強力なコーディング直感により、前世代のSonnetと比較して最大10%の改善を示しました 3。  
* **Claude Haiku 3.5**: 最速かつ最もコスト効率の高いモデルで、軽量なアクションの実行に適しています 2。

これらのモデルは、タスクの複雑性や要求されるパフォーマンスに応じて選択的に利用され、Claude Codeの多様なユースケースを支えています。エンタープライズユーザーは、既存のAmazon BedrockやGoogle Cloud Vertex AIインスタンス内のモデルを利用するオプションも持っています 4。

### **2.3. インタラクションモデル：CLIとスラッシュコマンド**

Claude Codeとのインタラクションは、主にコマンドラインインターフェース（CLI）を通じて行われます 1。ユーザーは自然言語でプロンプトを入力し、Claude Codeに応答させます。例えば、「claude \> how does our authentication system work?」（認証システムの仕組みは？）や「claude commit」（コミットして）といった具体的な指示が可能です 1。

さらに、特定の操作を迅速に実行するために「スラッシュコマンド」が用意されています 5。これらのコマンドは、会話履歴のクリア（/clear）、設定の表示・変更（/config）、ヘルプの表示（/help）、プロジェクトの初期化（/init）など、多岐にわたります 5。例えば、/initコマンドは、コードベースのドキュメントを含むCLAUDE.mdファイルを生成します 5。

VSCodeなどのIDEとの連携時には、キーボードショートカットも利用可能です。例えば、Cmd+Esc（Mac）またはCtrl+Esc（Windows/Linux）でClaude Codeを起動したり 7、@でファイルパスを、\#で情報を記憶させるなどのショートカットが提供されています 8。

このような構造化されたコマンドと柔軟な自然言語の組み合わせにより、開発者はClaude Codeに対して正確な制御と表現力豊かなタスク委任の両方を行うことができます。

#### **2.3.1. コンテキストインタラクションにおけるCLAUDE.mdの重要性**

Claude Codeのインタラクションにおいて、CLAUDE.mdファイルは極めて重要な役割を果たします。自然言語プロンプトだけでは、AIが特定のプロジェクト規約を遵守したり、カスタムツールを効果的に利用したりするためのコンテキストが不足する可能性があります。CLAUDE.mdは、Claude Codeが自動的に読み込む、プロジェクト固有の永続的な指示セットとして機能します 9。

このファイルを通じて、開発者はプロジェクト特有の側面（コーディング標準、レビュー基準、使用するシェルコマンド、テスト手順など）をClaudeに「教える」ことができます 6。これにより、Claude Codeは汎用的なコーディングアシスタントから、特定のプロジェクトに特化したアシスタントへと変化し、より正確で文脈に適したインタラクションと出力が期待できます。CLAUDE.mdは、プロジェクトのルートディレクトリ、サブディレクトリ、さらにはユーザーのホームディレクトリなど、様々な場所に配置でき、コンテキストの粒度を細かく制御することが可能です 9。これは特にチームでの共同作業において、AIの振る舞いをプロジェクト全体で一貫させるために不可欠です。

### **2.4. Claude Code SDK：プログラムによる統合**

Claude Code SDKは、開発者がClaude Codeをサブプロセスとして実行することにより、自身のアプリケーションにプログラム的に統合することを可能にします 14。これにより、Claudeの能力を活用したAI搭載のコーディングアシスタントやカスタムツールの構築が実現します。

現在、SDKはコマンドラインでの使用をサポートしており、将来的にはTypeScriptおよびPythonのSDKが提供される予定です 14。このSDKは、Claude Code GitHub Actionsのような統合機能の基盤となっています 11。

SDKの主な使用例としては、非インタラクティブモードでの実行（-pフラグ）、JSON形式での出力（--output-format json）、JSON出力のストリーミング、複数ターンにわたる会話の継続（--continue、--resume）、カスタムシステムプロンプトの設定、Model Context Protocol (MCP) の設定などが挙げられます 14。

#### **2.4.1. スケーラブルな自動化の基盤としてのSDK**

インタラクティブなCLIの使用は個々の開発者にとって強力ですが、真の自動化にはプログラムによる制御が不可欠です。Claude Code SDKはまさにこの制御を提供し、スクリプト、CI/CDパイプライン、または他のアプリケーションからClaude Codeを呼び出すことを可能にします。特に、JSON出力や非インタラクティブモードといった機能は、このようなプログラム的な使用を念頭に設計されています 6。

これにより、例えば、自動コードレビュー、issueトリガーに基づくPR生成、あるいはClaudeのインテリジェンスを活用したカスタムpre-commitフックといったシナリオが実現可能になります 9。SDKは、Claude Codeを自動化された無人プロセスに統合するためのゲートウェイと言えます。カスタム開発者ツールを構築したり、AI支援をDevOpsプラクティスに深く組み込んだりすることを検討している開発者にとって、SDKの能力を活用することは非常に重要です。今後予定されているPythonおよびTypeScript SDKのリリースは、このような統合への障壁をさらに下げるでしょう。

## **3\. 深掘り：Claude CodeとVSCodeの連携**

Visual Studio Code (VSCode) は、現代の開発者にとって主要な開発環境の一つであり、Claude Codeとの連携は生産性向上に大きく寄与する可能性があります。

### **3.1. Anthropic公式VSCode連携機能**

Anthropicは、Claude CodeをVSCode内でシームレスに利用するための公式な連携機能を提供しています。

#### **3.1.1. インストールとセットアップ**

公式連携機能のインストールは非常に簡単で、VSCodeの統合ターミナル内でclaudeコマンドを実行すると、関連する拡張機能が自動的にインストールされます 7。このプロセスを成功させるためには、VSCodeのコマンドラインインターフェース（codeコマンド、またはCursorやWindsurfのようなフォークの場合はそれぞれの対応コマンド）がシステムのPATHに設定されている必要があります 7。また、外部ターミナルセッションからIDEに接続したい場合は、/ideコマンドを使用できます 7。

インストールに関する一般的なトラブルシューティングとしては、統合ターミナルから実行しているか、code CLIがインストールされているか、VSCodeが拡張機能をインストールする権限を持っているかなどを確認することが挙げられます 7。GitHubのissueトラッカーには、「Claude Code Extension Not Detected in VSCode Terminal」といった問題も報告されています 17。

#### **3.1.2. 主要機能**

公式連携は、Claude Codeの能力をエディタ内に深く統合するための様々な機能を提供します。

* **クイック起動**: Cmd+Esc（Mac）またはCtrl+Esc（Windows/Linux）のショートカットキー、あるいはUI上のボタンクリックでClaude Codeを直接起動できます 7。  
* **IDE内での差分表示**: コードの変更点は、ターミナル出力ではなく、VSCodeの差分ビューアで直接表示されます 7。  
* **選択コンテキスト共有**: IDEで現在選択されている範囲やアクティブなタブの情報が自動的にClaude Codeと共有され、コンテキストに基づいた指示が可能になります 7。  
* **ファイル参照ショートカット**: Cmd+Option+K（Mac）またはAlt+Ctrl+K（Windows/Linux）を使用して、@File\#L1-99のような形式でファイル参照を挿入できます 7。  
* **診断情報共有**: リンティングエラーや構文エラーなど、IDEからの診断情報が作業中に自動的にClaudeと共有されます 7。  
* **インライン編集**: Claudeによって提案された編集内容は、ファイル内に直接インラインで表示され、レビューと追跡が容易になります 15。

これらの機能は、Claude Codeを単なる外部ツールとしてではなく、エディタと一体化した「ペアプログラマー」 15 として活用することを目指しています。特にインライン編集機能は、ターミナルとエディタ間の頻繁な切り替えを減らし、よりスムーズな開発フローを実現する上で重要です。デモンストレーションビデオ 18 では、Claudeが変更を加え、テストを実行する様子が示されており、これらの変更がIDE内で視覚的に表示されることが示唆されています。また、Anthropicの発表 15 でも、VSCode拡張機能がベータ版として提供され、IDEのターミナルからclaudeを実行することでインストールできること、そして「Claudeの提案する編集がファイル内にインラインで表示される」ことが明記されています。

#### **3.1.3. 設定**

Claude CodeのVSCode連携に関する設定は、Claude Code内で/configコマンドを実行することで行えます 7。特に、差分表示ツールをautoに設定することで、IDEが自動的に検出され、適切なビューアが使用されるようになります 7。これにより、ユーザーは好みに応じて、変更点がどのように提示されるかを調整できます。

#### **3.1.4. 公式連携の焦点：「エディタ内エクスペリエンス」と「リアルタイム補完」の不在**

公式ドキュメントや発表 7 を見ると、公式連携は差分表示、選択範囲の共有、そして提案された変更に対する*インライン編集*といった機能に重点を置いていることがわかります。これは、Claude Codeの主要なインタラクションモデルが、IDE内であっても会話型かつコマンド駆動型であるためです 1。開発者はClaudeにタスク実行を*依頼*します。

「インライン編集」機能 15 は、Claudeがコマンドに応じてコードを生成または変更した際に、それらの変更がターミナルに出力されるだけでなく、エディタのファイル内に直接表示されることを意味します。これは純粋なCLIツールと比較して大きな進歩です。

しかしながら、これは開発者がタイプ入力するそばからAIが次の数トークンを予測するような、GitHub Copilotの中核機能であるリアルタイムのコード補完やスニペット生成とは異なります。チュートリアル 20 でも、テスト生成やリファクタリングといったタスクはコマンドベースのインタラクションで行われており、継続的な補完機能については言及されていません。

したがって、Claude Codeの公式VSCode連携にGitHub Copilotのようなリアルタイム自動補完機能を期待するユーザーは、異なるパラダイムのツールであることを理解する必要があります。VSCode内のClaude Codeは、指示を与えてタスクを実行させ、その結果（編集内容や差分）をエディタ内で視覚的に確認する「エディタ内のエージェント」として機能します。「ペアプログラミング」15 という表現は、この反復的なコマンド発行とClaudeの作業結果のインラインレビューというプロセスを指していると考えられます。

### **3.2. 一般的なサードパーティ製VSCode拡張機能**

Anthropic公式連携以外にも、コミュニティによって開発されたClaudeを利用するためのVSCode拡張機能がいくつか存在します。

* **kodu-ai製「Claude Coder」** 21:  
  * 機能：アイデアから実装まで、デザインから実体化、直感的なデバッグ、Web検索、デプロイ支援などをAnthropicのClaudeを活用して提供します 21。  
  * インストール：VSCode Marketplaceまたはクイックオープンコマンド経由 21。  
  * ユーザーエクスペリエンス：スキルレベルに適応する24時間稼働のAIソフトウェア開発者を目指し、無料クレジットも提供されます 21。  
  * 特記事項：「Claude Dev」に触発されたとされています 21。Redditでの「Claude Dev」（前身または関連プロジェクトの可能性）に関するユーザーレビューは賛否両論で、エンドツーエンドの生成能力を称賛する声 22 がある一方、APIコストやトークン消費量の高さを指摘する声 22 もあります。58のビデオでは、「Root Code」（Claude Coderまたは類似ツールと思われる）で「Claude 3.7」を使用してアプリを約$1.45で構築する様子が紹介されています。  
* **CodeFlow Studio製「Claude Code Assistant for VSCode」** 23:  
  * 機能：Claude Code CLIの非公式連携。サイドバーアクセス、永続セッション、ワークスペース/ファイルコンテキスト認識、画像のドラッグ＆ドロップ/ペースト対応、問題点/ターミナル出力への@メンション、スラッシュコマンド、Markdownサポート、Claude風UIなどを提供します 23。  
  * 前提条件：VSCode 1.70.0以降、Claude Code CLIのインストール、アクティブなClaudeアカウント 23。  
  * インストール：MarketplaceまたはVSIXファイルから 23。  
* **rexdotsh製「ClaudeSync」** 24:  
  * 機能：コードをClaude.aiのプロジェクトと同期します。自動同期、ファイルの除外/含入、プロジェクト指示の管理などが可能です 24。  
  * 前提条件：Claude.ai Proプラン、セッショントークン 24。  
  * 特記事項：Anthropicとは非公式。Claude.aiの「プロジェクト」機能を活用します。  
* **Claudeモデルを利用したGitHub Copilot** 25:  
  * 機能：VSCode内のGitHub Copilot Chatは、デフォルトのGitHubモデルの代わりに、Claude Opus 4、Sonnet 4、Sonnet 3.5、Sonnet 3.7といったAnthropicモデルを使用するように設定できます 25。  
  * 解説：これはClaude Code自体ではなく、GitHub Copilotのフレームワーク内でClaudeの*モデル*を利用するものです。Copilotのチャットインターフェース内でClaudeの推論能力を活用できます。

#### **3.2.1. サードパーティ拡張機能における多様なアプローチ**

サードパーティ製の拡張機能は、それぞれ異なる機能を提供しています。一部はVSCode内でCLI体験を再現・強化しようとするもの（CodeFlow Studio製）、その他は特定のClaude.aiウェブ機能に焦点を当てたもの（ClaudeSync製）、さらに一般的なAIアシスタント体験を提供しようとするもの（kodu-ai製）など様々です。

公式連携がCLIのエージェント能力をエディタ内に視覚的なフィードバック（インライン編集、差分表示）と共に持ち込むことに焦点を当てているのに対し、サードパーティ開発者は、より伝統的なチャットインターフェース、画像サポート 23、あるいはウェブプラットフォーム機能との同期 24 など、ClaudeモデルやClaude Codeツールを活用する他の方法を模索しています。

これは活気あるエコシステムを示していますが、同時に機能の断片化や品質・コスト面でのばらつきの可能性も示唆しています（22の「Claude Dev」に関するレビューで見られるように）。したがって、ユーザーは選択肢がある一方で、自身のワークフロー、求める機能、コスト考慮事項に最も適したVSCode拡張機能（公式かサードパーティか）を慎重に評価する必要があります。公式ルートは特定の種類の統合を提供し、サードパーティのオプションは公式ツールにはない異なるインタラクションパラダイムや機能を提供する可能性があります。

### **3.3. VSCodeでの実用的な使用法とユーザーエクスペリエンス**

チュートリアルでは、ターミナル内でClaude Codeを使用してコードを生成したり、ファイルを操作したりし、それをVSCodeで開くといった使い方が示されています 27。

実際にVSCodeプラグイン（「Claude Dev」など）を使用したユーザーからは、エンドツーエンドのコード生成に関して他のツールよりも優れているとの評価がある一方で 22、APIコストとトークン消費量の高さが懸念点として挙げられています。特に多数のファイルや広範なコンテキストを扱う場合に顕著で、あるユーザーは初期呼び出しで13万5千トークン以上を消費したと報告し、別のユーザーは簡単な変更で1ドルかかったと述べています 22。

VSCodeのターミナルは長いペースト内容を切り詰めることがあるため、Claude Codeを使用する際はファイルベースのワークフローが推奨されます 28。また、59では、Cursorのような差分表示やファイル指定の改善をVSCode連携に求める声も上がっています。

#### **3.3.1. APIを利用するVSCode拡張機能におけるコスト管理の重要性**

複数のユーザー報告 22 は、Claudeを使用する際（特に最適化が不十分であったり、大規模なコンテキストを渡したりする可能性のあるサードパーティ製VSCode拡張機能経由の場合）に、APIコストが潜在的に高くなることを強調しています。

VSCode拡張機能が深いコードベース認識を提供する場合、大量のファイルコンテンツをClaudeに送信する誘惑に駆られるかもしれません。しかし、スマートなコンテキスト選択、差分処理、あるいはClaude自身の持つエージェント検索能力に頼るなど、慎重に管理されなければ、インタラクションごとのトークン消費量が高騰する可能性があります。AnthropicのAPIはトークンごとに課金されるため 29、非効率的なトークン使用は直接的にコスト増につながります。公式連携機能である「選択コンテキスト共有」7 やClaude Code固有のコードベース探索能力 1 は、一部のサードパーティ製アプローチよりも最適化されている可能性があります。

したがって、ユーザーは、選択したVSCode拡張機能（公式かサードパーティかを問わず）がどのようにコンテキストを管理し、Claude APIとインタラクトするかを意識し、予期せぬコストを避ける必要があります。コンテキストを賢く制限したり、Claudeに組み込まれたコンテキスト認識機能を活用したりする機能が望ましいです。Anthropicコンソールを通じたトークン使用量の監視は不可欠です。

### **3.4. Claude Code VSCode連携機能の比較**

以下の表は、VSCodeでClaudeを利用するための主要な連携オプションを比較したものです。

| 機能 | Anthropic公式連携 | Claude Coder (kodu-ai) | Claude Code Assistant (CodeFlow Studio) | ClaudeSync (rexdotsh) | GitHub Copilot (Claudeモデル使用) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **インストール方法** | 統合ターミナルでclaude実行 | VSCode Marketplace | VSCode Marketplace / VSIX | VSCode Marketplace | GitHub Copilot拡張機能 |
| **主要インタラクション** | CLIエージェント型 (会話形式) | AIアシスタント型 (タスク指示) | CLIラッパー型 (サイドバーチャット) | Claude.aiプロジェクト同期 | チャットベース (Copilotインターフェース) |
| **インライン編集** | あり (提案された変更) 15 | 不明 (コード生成が主) | 不明 (CLIの出力を表示) | なし (同期が主) | なし (Copilotの補完とは異なる) |
| **差分表示** | IDEビューア 7 | 不明 | 不明 | なし | なし |
| **コンテキスト管理** | 自動共有 (選択範囲/タブ) 7 | ユーザー指示/Web検索 21 | ワークスペース/ファイル認識 23 | ファイル同期 24 | Copilotのコンテキスト管理 |
| **画像サポート** | CLI経由で可能 (拡張機能での直接サポートは不明) 20 | 不明 | あり (ドラッグ&ドロップ/ペースト) 23 | なし | なし |
| **Web検索** | CLI経由で可能 (拡張機能での直接サポートは不明) 1 | あり 21 | 不明 | なし | あり (Copilotの機能として) |
| **前提条件** | Claude Code CLI, Anthropicアカウント | Anthropic Claudeモデルアクセス (無料クレジットあり) 21 | Claude Code CLI, Anthropicアカウント 23 | Claude.ai Proプラン, セッショントークン 24 | GitHub Copilotサブスクリプション, Anthropicモデルアクセス承認 25 |
| **コスト** | MaxプランまたはAPIトークン 4 | APIトークン (無料クレジット後) 21 | APIトークン | Claude.ai Proプランの費用 | GitHub Copilot費用 \+ AnthropicモデルAPIトークン (設定による) |

この表は、ユーザーがVSCodeでClaudeを利用する際の様々な選択肢を明確に区別し、それぞれの特徴、前提条件、コスト構造を理解するのに役立ちます。これにより、個々のニーズやワークフローに最適な統合方法を選択するための判断材料となります。

## **4\. 深掘り：Claude CodeとGitHub Actionsの連携**

GitHub Actionsは、ソフトウェア開発ワークフローを自動化するための強力なプラットフォームであり、Claude Codeとの連携により、AIを活用した高度な自動化が実現します。

### **4.1. GitHub ActionsにおけるClaude Codeのセットアップと設定**

Claude CodeをGitHub Actionsで利用するためのセットアップ方法は、主に2通りあります。

* **クイックスタート**: Claude Codeのターミナルで/install-github-appコマンドを実行します。これにより、GitHub Appのセットアップと必要なシークレット（主にANTHROPIC\_API\_KEY）の作成がガイドされます 11。この方法は、Anthropic APIを直接利用するユーザー向けで、リポジトリの管理者権限が必要です 11。  
* **手動セットアップ**:  
  1. リポジトリにClaude GitHub App ([https://github.com/apps/claude](https://github.com/apps/claude)) をインストールします 11。  
  2. ANTHROPIC\_API\_KEYをリポジトリのシークレットとして追加します 11。  
  3. 提供されているサンプルワークフローYAMLファイル（例：claude.yml）をリポジトリの.github/workflows/ディレクトリにコピーします 11。 この手動セットアップは、クイックスタートが失敗した場合や、AWS Bedrock/Google Vertex AIを利用する場合に必要です 11。

ワークフローYAMLファイルでは、anthropics/claude-code-action@betaまたはanthropics/claude-code-base-action@betaアクションを使用します 11。主要な入力パラメータには、prompt（Claudeへの指示）、allowed\_tools（Claudeが使用できるツール）、anthropic\_api\_key、trigger\_phrase（Claudeを起動するフレーズ、例：@claude）、direct\_prompt（トリガーなしで自動実行するプロンプト）、model（使用するモデル）、use\_bedrock、use\_vertex、custom\_instructionsなどがあります 11。ワークフローは、issue\_comment、pull\_request、pull\_request\_review\_commentといったGitHubイベントによってトリガーされます 32。

以下は、issueコメントで@claudeがメンションされた際にPRを作成する基本的なワークフローの例です 11。

YAML

name: Claude PR Creation  
on:  
  issue\_comment:  
    types: \[created\]  
jobs:  
  create-pr:  
    if: contains(github.event.comment.body, '@claude')  
    runs-on: ubuntu-latest  
    steps:  
      \- uses: anthropics/claude-code-action@beta  
        with:  
          prompt: "${{ github.event.comment.body }}"  
          anthropic\_api\_key: ${{ secrets.ANTHROPIC\_API\_KEY }}  
          \# allowed\_tools: \# 必要に応じて許可するツールを指定

#### **4.1.1. GitHub Actionsの2つの階層：claude-code-action vs. claude-code-base-action**

Anthropicは、claude-code-action 11 と claude-code-base-action 34 という2つの異なるGitHub Actionを提供しています。

claude-code-actionは、issueやPRでの@claudeメンションへの応答といった、一般的なインタラクティブなユースケース向けに設計された、より高レベルで意見の強いアクションのようです 11。これはコメントからのトリガーやコンテキスト処理を扱います。

一方、claude-code-base-actionは、「汎用的な」アクション 34 とされており、*あらゆるカスタムワークフロー*内でClaude Codeを実行できます。これは、より基本的なビルディングブロックとして機能するようです 34。特定のユーザーメンションなしで特定のイベントに基づいてClaudeを自動的に実行させたい場合や、より複雑でスクリプト化されたインタラクションのためには、claude-code-base-actionが適しています。

したがって、ユーザーはニーズに応じてアクションを選択すべきです。単純な@claudeトリガータスクにはclaude-code-actionで十分でしょう。より複雑なカスタムオートメーションや非インタラクティブなワークフローを構築する場合には、claude-code-base-actionがより多くの柔軟性を提供します。

### **4.2. Claude Code Actionsによる開発ワークフローの自動化**

Claude Code GitHub Actionsは、開発ワークフローの様々な側面を自動化する能力を持っています。

* **IssueからPRへの変換**: Issue内で「@claude implement this feature...」のようにメンションすることで、ClaudeがIssueを分析し、コードを記述し、レビューのためのPRを作成します 4。  
* **自動コードレビュー**: pull\_requestイベントでトリガーされ、Claudeが変更点をレビューし、品質、バグ、パフォーマンスに焦点を当てて改善を提案します 11。レビュープロンプトの例：「Review the PR changes. Focus on code quality, potential bugs, and performance issues.」11。  
* **PR管理と実装支援**: レビュアーのフィードバックへの対応、PR内のコード修正、コメントを通じた実装アドバイスの取得などが可能です 11。  
* **迅速なバグ修正**: Issue内で「@claude fix the TypeError...」とメンションすることで、Claudeがバグを特定し、修正を実装し、PRを作成します 11。  
* **スマートなブランチ処理**: Issueに対しては新しいブランチを作成し、オープンなPRに対しては既存のPRブランチに直接プッシュし、クローズされたPRに対しては新しいブランチを作成します 32。

これらのユースケースを具体的に示すために、以下の表に主要なGitHub Actionsの活用例をまとめます。

| ユースケース | トリガーイベント/コメント例 | @claudeプロンプトまたはdirect\_prompt例 | 主要なallowed\_tools (該当する場合) | 期待される結果 |
| :---- | :---- | :---- | :---- | :---- |
| **IssueからPRへの変換** | issue\_comment (例: @claude implement feature X) | implement feature X based on the issue description | View, GlobTool, GrepTool, Bash(git commands), FileEditTool, FileWriteTool | Claudeがコードを記述し、新しいブランチにコミットし、PRを作成する。 |
| **自動コードレビュー** | pull\_request (opened, synchronize) | direct\_prompt: "Review this PR for code quality, bugs, and adherence to CLAUDE.md guidelines." | View, GrepTool, Bash(git diff) | ClaudeがPRにレビューコメントを投稿する。 |
| **PRフィードバックへの対応** | pull\_request\_review\_comment (例: @claude address this feedback) | address the reviewer's feedback: \[feedback text\] | View, FileEditTool, Bash(git commit) | Claudeがフィードバックに基づいてコードを修正し、PRブランチにコミットする。 |
| **Issueからのバグ修正** | issue\_comment (例: @claude fix bug described in issue \#123) | fix the bug described in issue \#123. The error message is: \[error message\] | View, GrepTool, FileEditTool, Bash(git commands) | Claudeがバグを修正し、新しいブランチにコミットし、PRを作成する。 |
| **カスタム自動タスク** (direct\_prompt) | schedule, workflow\_dispatchなど | direct\_prompt: "Refactor all services in the /services directory to use the new Logger interface." | View, GlobTool, FileEditTool, FileWriteTool, Bash(git commands) | Claudeが指定されたリファクタリングを実行し、変更をコミット/PRする（設定による）。 |

この表は、Claude CodeをGitHub Actionsで活用する際の具体的な方法を示しており、一般的な開発タスクに対してどのような自動化が可能か、またそのためにどのようにプロンプトやワークフローを設定すればよいかを理解するのに役立ちます。

### **4.3. GitHub Actionsの高度な使用例とベストプラクティス**

#### **4.3.1. CLAUDE.mdによる振る舞いの誘導**

リポジトリのルートにCLAUDE.mdファイルを作成することで、コーディング標準、レビュー基準、プロジェクト固有のルール、優先されるパターンなどを定義できます。Claude Codeはこのガイドラインに従います 9。これは、直接的なインタラクションが制限される自動化ワークフローにおいて、Claudeの行動をプロジェクトの規約に整合させる上で極めて重要です 9。より詳細なコンテキストを提供するために、コードベース全体に複数のCLAUDE.mdファイルを使用することも可能です 10。

#### **4.3.2. AWS BedrockおよびGoogle Vertex AIとの統合**

エンタープライズ環境向けにサポートされており、データの保存場所や請求に関する管理が可能です 11。セットアップには、各クラウドプロバイダーとのOIDC設定、IAMロール、そしてトークン生成のためのカスタムGitHub Appが必要になる場合があります 11。YAML入力では、use\_bedrock: "true"またはuse\_vertex: "true"を使用し、プロバイダー固有の形式でモデルを指定します 32。

#### **4.3.3. テストケースの生成とデプロイ前チェック**

* **テストケースの生成**: GitHub Actionsに特化したドキュメントでは主要なユースケースとして明記されていませんが、Claude Code自体は「テストの実行と修正」が可能であり 1、チュートリアルではインタラクティブに未テストコードを特定し、テストのひな形を生成する様子が示されています 20。GitHub Actionは「機能の実装」や「バグ修正」が可能であるため 11、適切にプロンプトを与えれば論理的にテスト生成にも拡張できると考えられます。13は、ユニットテストと統合テストのための「テストのベストプラクティス」を含むCLAUDE.mdの例を提供しており、Claudeがこれらを扱えるように誘導できることを示唆しています。  
* **デプロイ前チェック**: GitHub Actionsのドキュメント 11 は、コードレビュー、PR作成、バグ修正に焦点を当てており、「デプロイ前チェック」は機能として明示されていません。しかし、Claude Codeはコマンドを実行でき 1、ヘッドレスモードで「主観的なリンティング、issue分類、静的コード解析」を実行できるため 9、特定の解析スクリプトやリンターを実行し、その結果を報告するようClaudeに指示することで、特定のデプロイ前チェックを実行するカスタムワークフローを設計できる可能性があります。6は、非インタラクティブモードを使用したCI/インフラワークフローの自動化について言及しています。

これらの高度なユースケースを実現するための直接的なYAMLの例は提供されていませんが、Claude Codeの基本的な能力（コマンド実行、コード解析、CLAUDE.mdへの準拠）とSDK/ベースアクションの柔軟性 14 を考慮すると、カスタムプロンプトとワークフロー設計によってこれらが*可能である*と考えられます。

**テストケース生成の概念的な例:**

YAML

\#...  
\# issueコメントまたはdirect\_prompt内:  
\# "@claude このPRの変更点を分析し、モジュールXの新しい関数に対するユニットテストをCLAUDE.mdに記載されたテストのベストプラクティスに従って生成してください。"  
\#...

**デプロイ前チェックの概念的な例:**

YAML

\#...  
\# direct\_prompt: "コミットされたコード変更のセキュリティレビューを実施してください。CLAUDE.mdのセキュリティガイドラインに従い、潜在的なXSS脆弱性と安全でないAPI呼び出しに焦点を当ててください。発見事項を報告してください。"  
\# allowed\_tools: \# カスタムスキャナを許可  
\#...

#### **4.3.4. コスト最適化とセキュリティ**

* **コスト**: GitHub Actionsの実行時間（分）とAPIコストに注意が必要です 11。特定の@claudeコマンドの使用、適切なmax\_turnsの設定、コンテキスト提供のためのissueテンプレートの活用、簡潔なCLAUDE.mdによって最適化を図ります 11。より高速で安価な実行のために、Depot GitHub Actionsランナーが提案されています 35。  
* **セキュリティ**: APIキー（ANTHROPIC\_API\_KEY）には常にGitHub Secretsを使用します 11。アクションの権限を制限し、マージ前にClaudeの提案をレビューします 11。カスタムツールやbashコマンドには、allowed\_toolsを使用して必要な操作のみを明示的に許可します 6。

CIでAIエージェントを実行することは、管理しなければコストやセキュリティリスクを伴う可能性があります。ドキュメントには明確なベストプラクティスが提供されています。

#### **4.3.5. 一般的な問題とコミュニティでの議論**

claude-code-actionに関するGitHub Issues 40 では、コミットツールの失敗、古いClaude Codeバージョンのインストール、PR作成に関する問題、MCPファイルが認識されない、APIエラー、認証問題などが報告されています。

Claude Code CLI全般（GitHub Actionsに間接的に影響する可能性のある問題を含む）に関するGitHub Issues 17 では、動作の遅延、過剰なAPI呼び出し、モデル設定の無視、VSCode連携の問題などが挙げられています。

Redditでの議論 43 では、Claude Code（暗黙的にActionsでの使用も含む）とCursorのような他のツールとの比較が行われ、コストの違いが指摘されています。Coder.comのブログ記事 44 では、Claude Code（エージェント）が複雑な推論やドキュメントが不十分なAPIの扱いに苦戦する一方で、より単純なタスクでは良好な結果を示したと報告されています。

#### **4.3.6. 効果的かつ安全なGitHub Actions自動化におけるCLAUDE.mdの最重要性**

複数の情報源が、Claudeの振る舞いを導き、標準を定義し、さらには許可されたツールやコマンドをリストアップするためにCLAUDE.mdを強調しています 9。

自動化されたGitHub Actionでは、曖昧さを明確にしたり、誤解をリアルタイムで修正したりするインタラクティブなユーザーは存在しません。CLAUDE.mdは、AIエージェントのための永続的な指示とコンテキストのセットとして機能します。これにより、コーディングスタイルだけでなく、PRのレビュー基準、特定の種類のバグを修正する手順、あるいは実行しても安全な特定のシェルコマンドまで定義できます 9。これにより、Claudeの振る舞いがより予測可能になり、プロジェクトの要件と整合性が取れるようになります。これは、信頼性の高い自動化に不可欠です。また、プロジェクトにとって標準的な操作を（暗黙的または明示的に文書化されていれば）導くことで、セキュリティ上の役割も果たします。

したがって、包括的なCLAUDE.mdの作成に時間を投資することは、Claude Code GitHub Actionsの使用を計画しているチームにとって重要なベストプラクティスです。これは、自動化されたCI/CD環境でAIの振る舞いをカスタマイズし、制御するための主要なメカニズムです。13のテストに関するCLAUDE.mdの例の詳細は、このガイダンスがいかに具体的であるかを示しています。

## **5\. 言語サポート、価格設定、ライセンス、データに関する考慮事項**

### **5.1. 対応コーディング言語と自然言語インタラクション**

* **コーディング言語**: Claudeは主要なプログラミング言語すべてに習熟しており、特にPythonを得意としています 45。  
* **自然言語**: Claudeは堅牢な多言語能力を示し、多くの言語でゼロショットタスクにおいて高いパフォーマンスを発揮します 46。日本語に関して、Claude Opus 4のパフォーマンスは英語を100%とした場合に96.2%、Sonnet 4では95.6%です 46。 これは、ユーザーがClaude Codeと日本語でインタラクション（プロンプト記述など）を行い、高いレベルの理解を期待できること、そして様々なプログラミング言語で書かれたコードベースを扱えることを意味します。多言語コンテンツを扱う際のベストプラクティスとしては、明確な言語コンテキストを提供し、ネイティブスクリプトを使用することが推奨されます 46。

### **5.2. 価格モデル：Maxサブスクリプション vs. APIトークン消費**

Claude Codeへのアクセスは、主に以下の2つの方法で提供されます。

* **Maxサブスクリプション**: 月額$100（Pro使用量の5倍）または月額$200（Pro使用量の20倍）のプランがあります。Claude Codeの使用量は、Maxプランの共有レート制限に対してカウントされます 4。  
* **Anthropic API（トークンベース）**: 標準のAPI価格でAPIトークンを消費します。従量課金制です 4。

ユーザーには柔軟性があり、Maxプランは一般的な使用量に対して予測可能な月額コストを提供し、APIアクセスは時折の使用や実験的な使用、あるいは組織内での無制限の開発者展開に適しています 4。Maxプランの制限に達した場合、ユーザーは従量課金制のAPIクレジットに切り替えるオプションがあります 31。APIクレジットの自動リロードは、Claude Code自体ではなくAPIコンソールで管理されます 31。

モデルの価格は大幅に異なり（例：Opus 4入力$15/MTok、Sonnet 4入力$3/MTok、Haiku 3.5入力$0.80/MTok）、バッチ処理では50%の割引が適用されます 29。

#### **5.2.1. 管理不行き届きによるコスト超過の可能性**

ユーザーレビュー 22 やバグレポート 42 でさえ、特に非効率的なキャッシュ管理やClaudeが最適でないモデルにデフォルト設定された場合に、高いトークン消費量とコストが言及されています。

Claude Codeのエージェント的な性質は、ファイルやコンテキストの読み取りを伴います。もし過剰または冗長な読み取り（例：マイナーなインタラクションごとに大規模なコンテキストを再読み取りする）が発生すると、トークン使用量が急増する可能性があります（42では、API呼び出しごとに約5万トークンのキャッシュ読み取りが強調されています）。モデルの選択（Opus vs. Sonnet vs. Haiku）は、コストに直接的かつ大きな影響を与えます 29。Maxプランはある程度の予測可能性を提供しますが、ヘビーユーザーや制限に達してAPIクレジットに切り替えるユーザーは、使用状況を監視しなければ相当な請求に直面する可能性があります。

したがって、特にAPI課金を利用しているユーザーやMaxプランの限界に挑戦しているユーザーは、Anthropicコンソール 4 を通じてトークン消費量を積極的に監視する必要があります。モデルの設定方法 28、CLAUDE.mdを使用してコンテキストを効率的に提供する方法 9、/compactのようなコマンドの使用方法 5 を理解することは、コスト管理にとって極めて重要です。

### **5.3. AI生成コードの所有権と商用利用**

Anthropicは、同社の規約を遵守することを条件として、「出力」（例：生成されたコード）に関するすべての権利、権原、利益（もしあれば）をユーザーに譲渡します 47。ユーザーとAnthropicの間では、ユーザーが出力を所有します 47。

ただし、純粋にAIによって生成されたコンテンツ（十分な人間の著作性が認められないもの）の著作権は複雑であり、認められない場合があります。人間の貢献が多ければ多いほど、著作権の主張は強くなります 47。Anthropicの商用規約（2025年5月版）には、ビジネスユーザー向けの著作権補償が含まれており、Claudeとその出力の承認された使用から生じる第三者の著作権侵害の申し立てに対してAnthropicが防御します 47。これは標準的な消費者向け規約には適用されません。

制限事項として、ユーザーは出力を別のAIのトレーニングに使用したり、Claudeのコアサービスを再販または再配布したり、モデルスクレイピングに従事したりすることはできません 47。ある開発者が、制限的な商用ライセンス下にあるClaude Code自体のソースコードを逆難読化して公開したためにDMCAテイクダウンに直面した事例がありますが 48、これはClaude Code *ツール自体*に関するものであり、ユーザーが生成したコードに関するものではありません。

要約すると、ユーザーは通常、Claudeが生成を支援したコードを商用目的で所有しますが、Anthropicの規約に従う必要があります。補償は企業にとって大きな利点です。*出力*の所有権と*ツール*のライセンスの区別は重要です。

#### **5.3.1. 強固なIP権のための人間とAIの協調の重要性**

Anthropicが出力に対する権利を譲渡する一方で、実際の著作権性は人間の関与にかかっています 47。

世界の著作権法（例：米国著作権局のガイダンス）はまだ進化の途上にありますが、一般的には保護のために人間の著作性を要求します。ユーザーがClaudeから未修正の生のコードを単純に取得し、著作権を主張しようとすると、困難に直面する可能性があります。しかし、Claudeをドラフト生成ツールとして使用し、その後、人間の開発者が大幅にレビュー、編集、増補した場合、結果として得られる著作物は著作権の根拠がはるかに強固になります。Anthropicの規約（「もしあれば」権利）は、この法的なニュアンスを認めています。

したがって、IPの所有権と保護が重要な商用プロジェクトでは、開発者はClaude Codeを、人間の創造性と監視を完全に置き換えるものではなく、作業を強化する強力なアシスタントとして扱うべきです。生成されたコードは、品質を確保し、IPの主張を強化するために、人間によって慎重にレビュー、テスト、統合されるべきです。

### **5.4. データ処理、プライバシー、セキュリティ**

クエリは中間サーバーを経由せずに直接AnthropicのAPIに送信されます 1。Anthropicは、Claude Codeからのフィードバックを使用して生成モデルをトレーニングすることはなく、ユーザーフィードバックのトランスクリプトは30日間のみ保存されます 1。Claude Codeはターミナルでローカルに実行され、変更やコマンド実行の前に許可を求めます 4。これらのポリシーは、特に機密性の高いコードベース情報に関するプライバシーとセキュリティの懸念に対処することを目的としています。詳細については、Anthropicの商用サービス利用規約とプライバシーポリシーを参照することが推奨されます 1。

## **6\. 比較考察と制限事項**

### **6.1. Claude Code vs. GitHub Copilot および Amazon CodeWhisperer**

* **GitHub Copilotとの比較**: Copilotは、速度とシームレスなIDE統合（入力中の提案）でしばしば引用されます 49。一方、Claudeは、教育、デバッグ、長文思考、背景にある「理由」の説明、複雑なロジックやエッジケースの処理に優れており、ハルシネーション率が低いとされています 49。Claude CodeはターミナルやIDE内の会話型エージェントに近いのに対し、Copilotはインライン補完で知られています 50。現在、GitHub Copilot Chat内でClaudeモデルを使用することも可能です 25。  
* **Amazon CodeWhispererとの比較**: CodeWhispererはAmazon Q Developerエコシステムの一部であり、AWS環境に強く、組み込みの脆弱性スキャン機能を備えています 52。Claude Codeはターミナルファーストであり、MCP (Model Context Protocol) を介してSlackやGitLabなどのツールとの幅広い互換性を提供します 52。また、Claudeは直接的なGitワークフロー管理機能を備えています 52。

選択は特定のニーズに依存します。迅速な補完（Copilot）、深い推論や説明（Claude）、あるいはAWSエコシステムやセキュリティスキャン（CodeWhisperer）など、目的によって最適なツールは異なります。

#### **6.1.1. 補完的な強みが示唆する複数ツールの活用**

比較検討では、あるツールが普遍的に優れているというよりも、それぞれ異なる強みが強調されることがよくあります 49。ボイラープレートコードにはCopilotを使用し、クリーンアップや説明にはClaudeを使用するといった提案も見られます 50。

現在、単一のAIコーディングツールがソフトウェア開発のあらゆる側面で等しく優れているわけではありません。開発者は、新しいコードを書く際にGitHub Copilotで迅速なインライン提案を得つつ、複雑なモジュールの詳細な分析や自然言語リクエストに基づく既存コードのリファクタリング、あるいはClaude Code SDKを使用したスクリプトによる複数ステップタスクの自動化にはClaude Codeを利用するといった使い分けが考えられます。GitHub Copilot Chat内でClaudeモデルを使用できるようになったこと 25 は、この境界をさらに曖昧にし、使い慣れたインターフェース内でタスクに最適なモデルを活用するという考え方を支持します。

したがって、開発者は、目の前の特定のタスクに基づいて、Claudeとの様々なインタラクション方法（CLI、公式VSCode連携、サードパーティ拡張機能、またはCopilot Chat経由）を含む、異なるAIツールを戦略的に組み合わせることで、最適な生産性を達成できる可能性があります。

### **6.2. Claude Codeの既知の制限事項**

* **APIレート制限**: RPM（1分あたりのリクエスト数）、ITPM（1分あたりの入力トークン数）、OTPM（1分あたりの出力トークン数）の制限があり、モデルや使用ティアによって異なります。これを超えると429エラーが発生します 54。  
* **支出制限**: 組織がAPI使用に対して毎月負担できる最大コスト 54。  
* **知識のカットオフ**: 知識は特定の時点までのトレーニングデータに基づいており、非常に新しい開発に関するデータが不足している場合があります 55。  
* **ニュアンスのある言語**: 明示的にトレーニングされていない場合、深い皮肉、ユーモア、または非常に特殊な文化的ニュアンスの解釈に苦労する可能性があります 55。  
* **パフォーマンスの問題**: 状況によっては、動作の遅延、単純なコマンドでのハングアップ、過剰なAPI呼び出しといったユーザー報告があります 41。  
* **VSCodeターミナルの制限**: 長いペースト内容が切り捨てられることがあります 28。  
* **ベータステータス**: Claude Code GitHub Actionsはベータ版であり、機能は進化する可能性があります 11。Claude Codeツール自体も、フィードバックに基づいて進化するリサーチプレビューとして説明されています 6。

これらの制限を理解することは、現実的な期待値を設定し、回避策（API呼び出しの管理、ファイルベースのワークフローの使用など）を開発するのに役立ちます。

## **7\. 結論と今後の展望**

### **7.1. 開発者にとってのClaude Codeの強みの要約**

Claude Codeは、そのエージェント能力により複雑な複数ステップのタスクを実行でき、深いコードベース理解とコンテキスト認識能力を備えています。ターミナルや既存の開発者ツールとの強力な統合、コーディングに最適化された高性能モデル（Opus 4、Sonnet 4）の利用、そして特にVSCodeにおけるインライン編集機能を通じたIDE統合の深化は、開発者にとって大きな利点です。さらに、SDKとMCPを介した拡張性により、GitHub Actionsのようなカスタム自動化も可能です。

### **7.2. 開発ワークフローへの潜在的な影響**

Claude Codeは、リファクタリング、デバッグ、ドキュメンテーションといった一般的なタスクを加速し、複雑なレガシーコードのオンボーディングと理解を向上させることが期待されます。GitHub Actionsを介したCI/CDタスクの自動化は、開発サイクルの効率化に貢献し、小規模チームでも大規模プロジェクトに取り組むことを可能にするかもしれません 56。将来的には、人間の開発者の役割が、AIがより多くの実装詳細を処理する中で、より「監督的」または「指示的」なものへと移行していく可能性があります 56。

### **7.3. 今後の開発**

計画されているTypeScriptおよびPython SDKのリリースは、プログラムによる統合オプションをさらに広げるでしょう 14。ツール実行の信頼性、長時間実行コマンドのサポート、モデル能力の継続的な改善も期待されます 6。特にGitHub Actionsのようなベータ機能については、ユーザーフィードバックに基づいた進化が続くでしょう 6。

#### **7.3.1. より自律的で統合されたAIチームメイトへの軌跡**

Claude Code自体の開発（80%の自己コーディングの主張 56 を含む）、エージェント的振る舞いへの焦点、SDK、そして深い統合は、AIツールが受動的なアシスタントから、より能動的な協力者へと進化していく未来を示唆しています。

単純なコード補完から、コードベース全体を理解し、コマンドを実行し、PRを管理できるエージェントツールへの進歩は、大きな飛躍です。SDKとGitHub Actionsは、これらのエージェントが開発パイプライン内でより自律的に動作することを可能にします。CLAUDE.mdによるプロジェクト固有情報の提供やClaudeへの「教育」の重視は、AIが知識豊富なチームメンバーになることへの期待を示しています。将来のPython/TypeScript SDKは、カスタムエージェントワークフローの構築をさらに容易にするでしょう。

開発者は、AIツールがより複雑でエンドツーエンドのソフトウェア開発タスクを処理できるようになることを予期すべきです。求められるスキルは、単に一行一行コードを書くことよりも、これらのAIエージェントを効果的に指示し、管理し、協力する能力へとシフトしていくでしょう。テキストだけでなく、コンテキストファイル（CLAUDE.md）、ツールパーミッション、ワークフロー定義といった要素を用いた「プロンプトエンジニアリング」の理解がますます重要になります。

#### **引用文献**

1. Claude Code overview \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/overview](https://docs.anthropic.com/en/docs/claude-code/overview)  
2. Meet Claude \- Anthropic, 5月 25, 2025にアクセス、 [https://www.anthropic.com/claude](https://www.anthropic.com/claude)  
3. Write beautiful code, ship powerful products | Claude by Anthropic ..., 5月 25, 2025にアクセス、 [https://www.anthropic.com/solutions/coding](https://www.anthropic.com/solutions/coding)  
4. Claude Code: Deep Coding at Terminal Velocity \\ Anthropic, 5月 25, 2025にアクセス、 [https://www.anthropic.com/claude-code](https://www.anthropic.com/claude-code)  
5. Claude Code: A Guide With Practical Examples | DataCamp, 5月 25, 2025にアクセス、 [https://www.datacamp.com/tutorial/claude-code](https://www.datacamp.com/tutorial/claude-code)  
6. Claude Code overview \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/agents/claude-code/introduction](https://docs.anthropic.com/en/docs/agents/claude-code/introduction)  
7. IDE integrations \- Anthropic, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/ide-integrations](https://docs.anthropic.com/en/docs/claude-code/ide-integrations)  
8. Setting Up Claude Code in VS Code \- Community.aws, 5月 25, 2025にアクセス、 [https://community.aws/content/2v5sof1SSJ89ke01CbCE6o4GZKz/setting-up-claude-code-in-vs-code](https://community.aws/content/2v5sof1SSJ89ke01CbCE6o4GZKz/setting-up-claude-code-in-vs-code)  
9. Anthropic Releases Best Practices Guide for Claude Code, Seamlessly Integrating AI into Developer Workflows \- AIbase, 5月 25, 2025にアクセス、 [https://www.aibase.com/news/17387](https://www.aibase.com/news/17387)  
10. Claude Code: Best practices for agentic coding \- Anthropic, 5月 25, 2025にアクセス、 [https://www.anthropic.com/engineering/claude-code-best-practices](https://www.anthropic.com/engineering/claude-code-best-practices)  
11. GitHub Actions \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/github-actions](https://docs.anthropic.com/en/docs/claude-code/github-actions)  
12. Anthropic's Guide to Claude Code: Best Practices for Agentic Coding : r/ClaudeAI \- Reddit, 5月 25, 2025にアクセス、 [https://www.reddit.com/r/ClaudeAI/comments/1k5slll/anthropics\_guide\_to\_claude\_code\_best\_practices/](https://www.reddit.com/r/ClaudeAI/comments/1k5slll/anthropics_guide_to_claude_code_best_practices/)  
13. policyengine-us/CLAUDE.md at master \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/PolicyEngine/policyengine-us/blob/master/CLAUDE.md](https://github.com/PolicyEngine/policyengine-us/blob/master/CLAUDE.md)  
14. SDK \- Anthropic, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/sdk](https://docs.anthropic.com/en/docs/claude-code/sdk)  
15. Introducing Claude 4 \\ Anthropic, 5月 25, 2025にアクセス、 [https://www.anthropic.com/news/claude-4](https://www.anthropic.com/news/claude-4)  
16. Troubleshooting \- Claude Code \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/troubleshooting](https://docs.anthropic.com/en/docs/claude-code/troubleshooting)  
17. Issues · anthropics/claude-code \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code/issues](https://github.com/anthropics/claude-code/issues)  
18. Introducing Claude Code \- YouTube, 5月 25, 2025にアクセス、 [https://www.youtube.com/watch?v=AJpK3YTTKZ4\&pp=0gcJCdgAo7VqN5tD](https://www.youtube.com/watch?v=AJpK3YTTKZ4&pp=0gcJCdgAo7VqN5tD)  
19. Code with Claude Opening Keynote \- YouTube, 5月 25, 2025にアクセス、 [https://www.youtube.com/watch?v=EvtPBaaykdo](https://www.youtube.com/watch?v=EvtPBaaykdo)  
20. Tutorials \- Claude Code \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/tutorials](https://docs.anthropic.com/en/docs/claude-code/tutorials)  
21. Claude Coder \- Visual Studio Marketplace, 5月 25, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=kodu-ai.claude-dev-experimental](https://marketplace.visualstudio.com/items?itemName=kodu-ai.claude-dev-experimental)  
22. If you use Claude for coding, you need to check out Claude Dev. \- Reddit, 5月 25, 2025にアクセス、 [https://www.reddit.com/r/ClaudeAI/comments/1fzztp0/if\_you\_use\_claude\_for\_coding\_you\_need\_to\_check/](https://www.reddit.com/r/ClaudeAI/comments/1fzztp0/if_you_use_claude_for_coding_you_need_to_check/)  
23. Claude Code Assistant for VSCode \- Visual Studio Marketplace, 5月 25, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=codeflow-studio.claude-code-extension](https://marketplace.visualstudio.com/items?itemName=codeflow-studio.claude-code-extension)  
24. rexdotsh/claudesync-vscode: VSCode Extension to sync your code with Claude.ai Projects. \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/rexdotsh/claudesync-vscode](https://github.com/rexdotsh/claudesync-vscode)  
25. AI language models in VS Code, 5月 25, 2025にアクセス、 [https://code.visualstudio.com/docs/copilot/language-models](https://code.visualstudio.com/docs/copilot/language-models)  
26. Using Claude in Copilot Chat \- GitHub Docs, 5月 25, 2025にアクセス、 [https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot](https://docs.github.com/en/copilot/using-github-copilot/ai-models/using-claude-in-github-copilot)  
27. Claude Code Tutorial: How to Generate, Debug and Document Code with AI | Codecademy, 5月 25, 2025にアクセス、 [https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai](https://www.codecademy.com/article/claude-code-tutorial-how-to-generate-debug-and-document-code-with-ai)  
28. Claude Code settings \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/claude-code/settings](https://docs.anthropic.com/en/docs/claude-code/settings)  
29. Pricing \\ Anthropic, 5月 25, 2025にアクセス、 [https://www.anthropic.com/pricing](https://www.anthropic.com/pricing)  
30. Pricing \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/about-claude/pricing](https://docs.anthropic.com/en/docs/about-claude/pricing)  
31. Using Claude Code with your Max Plan | Anthropic Help Center, 5月 25, 2025にアクセス、 [https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-max-plan](https://support.anthropic.com/en/articles/11145838-using-claude-code-with-your-max-plan)  
32. Claude Code Action Official \- GitHub Marketplace, 5月 25, 2025にアクセス、 [https://github.com/marketplace/actions/claude-code-action-official](https://github.com/marketplace/actions/claude-code-action-official)  
33. anthropics/claude-code-action \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)  
34. anthropics/claude-code-base-action \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code-base-action](https://github.com/anthropics/claude-code-base-action)  
35. Faster Claude Code agents in GitHub Actions \- Depot, 5月 25, 2025にアクセス、 [https://depot.dev/blog/claude-code-in-github-actions](https://depot.dev/blog/claude-code-in-github-actions)  
36. An AI Agent that operates Claude Code on GitHub Actions. By using this action, you can directly invoke Claude Code from GitHub Issues or Pull Request comments and automate code changes., 5月 25, 2025にアクセス、 [https://github.com/potproject/claude-code-github-agent](https://github.com/potproject/claude-code-github-agent)  
37. How to Automate Git with Claude Code \- YouTube, 5月 25, 2025にアクセス、 [https://www.youtube.com/watch?v=tqKOQa9PkF4](https://www.youtube.com/watch?v=tqKOQa9PkF4)  
38. diekotto/ai-pull-review: A GitHub Action that leverages Anthropic's Claude AI to provide intelligent analysis and review of pull requests., 5月 25, 2025にアクセス、 [https://github.com/diekotto/ai-pull-review](https://github.com/diekotto/ai-pull-review)  
39. Claude Code \+ GitHub Actions \- YouTube, 5月 25, 2025にアクセス、 [https://www.youtube.com/watch?v=L\_WFEgry87M](https://www.youtube.com/watch?v=L_WFEgry87M)  
40. Issues · anthropics/claude-code-action \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code-action/issues](https://github.com/anthropics/claude-code-action/issues)  
41. \[BUG\] · Issue \#727 · anthropics/claude-code \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code/issues/727](https://github.com/anthropics/claude-code/issues/727)  
42. Critical Bug: Claude Code CLI is making excessive background API calls, ignoring model configuration, and console reporting inconsistencies · Issue \#1224 \- GitHub, 5月 25, 2025にアクセス、 [https://github.com/anthropics/claude-code/issues/1224](https://github.com/anthropics/claude-code/issues/1224)  
43. Claude Code Review : r/ChatGPTCoding \- Reddit, 5月 25, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTCoding/comments/1j2lo98/claude\_code\_review/](https://www.reddit.com/r/ChatGPTCoding/comments/1j2lo98/claude_code_review/)  
44. Solving GitHub Issues with Claude Code \- Coder, 5月 25, 2025にアクセス、 [https://coder.com/blog/coding-with-claude-code](https://coder.com/blog/coding-with-claude-code)  
45. What are some things I can use Claude for? | Anthropic Help Center, 5月 25, 2025にアクセス、 [https://support.anthropic.com/en/articles/7996845-what-are-some-things-i-can-use-claude-for](https://support.anthropic.com/en/articles/7996845-what-are-some-things-i-can-use-claude-for)  
46. Multilingual support \- Anthropic, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support](https://docs.anthropic.com/en/docs/build-with-claude/multilingual-support)  
47. Who Owns Claude's Outputs and How Can They Be Used? (May 2025 Update) – Terms.law, 5月 25, 2025にアクセス、 [https://terms.law/2024/08/24/who-owns-claudes-outputs-and-how-can-they-be-used/](https://terms.law/2024/08/24/who-owns-claudes-outputs-and-how-can-they-be-used/)  
48. Shocking: Anthropic Claude Code Takedown Sparks Developer Backlash Over AI Licensing, 5月 25, 2025にアクセス、 [https://coinstats.app/news/0b178d126704a9044abdf46423b7502ff954aa5e728718a7b21bf94b182c7886\_Shocking-Anthropic-Claude-Code-Takedown-Sparks-Developer-Backlash-Over-AI-Licensing/](https://coinstats.app/news/0b178d126704a9044abdf46423b7502ff954aa5e728718a7b21bf94b182c7886_Shocking-Anthropic-Claude-Code-Takedown-Sparks-Developer-Backlash-Over-AI-Licensing/)  
49. techpoint.africa, 5月 25, 2025にアクセス、 [https://techpoint.africa/guide/claude-vs-github-copilot-for-coding/\#:\~:text=Copilot%20is%20unbeatable%20for%20speed,through%20the%20why%20behind%20it.](https://techpoint.africa/guide/claude-vs-github-copilot-for-coding/#:~:text=Copilot%20is%20unbeatable%20for%20speed,through%20the%20why%20behind%20it.)  
50. I tested Claude vs GitHub Copilot with 5 coding prompts – Here's my winner, 5月 25, 2025にアクセス、 [https://techpoint.africa/guide/claude-vs-github-copilot-for-coding/](https://techpoint.africa/guide/claude-vs-github-copilot-for-coding/)  
51. OpenAI Codex Vs. Claude Code Vs. GitHub Copilot \- Empathy First Media, 5月 25, 2025にアクセス、 [https://empathyfirstmedia.com/openai-codex-vs-claude-code-vs-github-copilot/](https://empathyfirstmedia.com/openai-codex-vs-claude-code-vs-github-copilot/)  
52. Claude Code Vs Amazon Codewhisperer \- Empathy First Media, 5月 25, 2025にアクセス、 [https://empathyfirstmedia.com/claude-code-vs-amazon-codewhisperer/](https://empathyfirstmedia.com/claude-code-vs-amazon-codewhisperer/)  
53. Compare Amazon Q Developer vs. Claude \- G2, 5月 25, 2025にアクセス、 [https://www.g2.com/compare/amazon-q-developer-vs-anthropic-claude](https://www.g2.com/compare/amazon-q-developer-vs-anthropic-claude)  
54. Rate limits \- Anthropic API, 5月 25, 2025にアクセス、 [https://docs.anthropic.com/en/api/rate-limits](https://docs.anthropic.com/en/api/rate-limits)  
55. Claude AI: Breaking Down Barriers and Limitations \- AutoGPT, 5月 25, 2025にアクセス、 [https://autogpt.net/claude-ai-breaking-down-barriers-and-limitations/](https://autogpt.net/claude-ai-breaking-down-barriers-and-limitations/)  
56. Can an AI Really Code Itself? — Inside Anthropic's “Claude Code” Phenomenon \- SmythOS, 5月 25, 2025にアクセス、 [https://smythos.com/ai-industry-solutions/process-automation/can-an-ai-code-itself-claude-code/](https://smythos.com/ai-industry-solutions/process-automation/can-an-ai-code-itself-claude-code/)  
57. "Claude Code wrote 80% of its own code" \- anthropic dev : r/singularity \- Reddit, 5月 25, 2025にアクセス、 [https://www.reddit.com/r/singularity/comments/1khxwjh/claude\_code\_wrote\_80\_of\_its\_own\_code\_anthropic\_dev/](https://www.reddit.com/r/singularity/comments/1khxwjh/claude_code_wrote_80_of_its_own_code_anthropic_dev/)  
58. VSCode \+ Claude 3.7 Is The FASTEST Coding AI EVER \- YouTube, 5月 25, 2025にアクセス、 [https://www.youtube.com/watch?v=WE0lUPt3xG4](https://www.youtube.com/watch?v=WE0lUPt3xG4)  
59. Anyone working on a Claude Code extension for vscode? : r/ClaudeAI \- Reddit, 5月 25, 2025にアクセス、 [https://www.reddit.com/r/ClaudeAI/comments/1kcow0v/anyone\_working\_on\_a\_claude\_code\_extension\_for/](https://www.reddit.com/r/ClaudeAI/comments/1kcow0v/anyone_working_on_a_claude_code_extension_for/)