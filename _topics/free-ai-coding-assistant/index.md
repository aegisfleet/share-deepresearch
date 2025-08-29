---
audio: /share-deepresearch/assets/audio/free-ai-coding-assistant.mp3
category: ai
date: 2025-08-29
description: GitHub Copilotに代表されるコーディング用のAIエージェントで無料で使えるものを調査し、各ツールの無料利用の範囲を比較分析します。
ga4_metrics:
  avgSessionDuration: 0.0
  pageViews: 0
  users: 0
layout: topic
prompt: GitHub Copilotに代表されるコーディング用のAIエージェントで無料で使えるものを調べて欲しい。各ツールにおいてどの程度無料で使えるのかも知りたい。
supplementary_materials:
- title: インフォグラフィック：無料AIコーディングアシスタントの現状 (2025年)
  url: /share-deepresearch/topics/free-ai-coding-assistant/infographic.html
tags:
- AIツール
title: 無料で利用可能なAIコーディングアシスタント：2025年版 徹底比較分析レポート
video: /share-deepresearch/assets/video/free-ai-coding-assistant.mp4
---

# **無料で利用可能なAIコーディングアシスタント：2025年版 徹底比較分析レポート**

## **第1章：AI駆動開発の進化と無料コーディングアシスタントの台頭**

### **1.1 序論：GitHub Copilotが切り拓いた新時代**

ソフトウェア開発の歴史において、AIが開発者の日常的なワークフローに不可欠なパートナーとして組み込まれる時代の幕開けは、GitHub Copilotの登場によって象徴されます。このツールは単なるコード補完機能を超え、「AIペアプログラマー」という新たな概念を市場に確立しました 1。開発者がエディタ内で自然言語のコメントや書きかけのコードを入力すると、Copilotが文脈を理解し、数行から時には関数全体に至るまでのコードブロックをリアルタイムで提案する能力は、開発の生産性を根底から変革する可能性を示しました。この革新的な体験は瞬く間に開発者コミュニティに受け入れられ、AIコーディングアシスタントという新しい市場カテゴリーの事実上の標準、すなわちベンチマークとしての地位を築き上げました 3。

Copilotの商業的成功は、市場に強力なシグナルを送りました。それは、開発者がAI支援に対して対価を支払う意思があること、そしてこの技術が単なる目新しさではなく、実用的な価値を持つことを証明したのです。この市場の検証を受けて、テクノロジー業界の巨人が次々とこの分野への本格参入を開始しました。Googleは自社の強力なAIモデルを背景に「Gemini Code Assist」を、Amazon Web Services (AWS) はクラウドとの親和性を武器に「Amazon Q Developer」を投入しました 4。MicrosoftはGitHub Copilotを通じて、自社の開発エコシステムをさらに強化しています。

同時に、この新しい市場の活況は、革新的なアイデアを持つスタートアップにも大きな機会をもたらしました。VS Codeをフォークし、AIとの対話を前提に再設計されたエディタ「Cursor」や、当初から個人利用の完全無料を掲げて注目を集めた「Windsurf」（旧Codeium）、そしてプライバシーを重視する開発者向けに独自の地位を築いた「Tabnine」など、多様なプレイヤーが独自の価値提案を掲げて参入しました 4。これらのツールは、Copilotが設定したベンチマークを意識しつつも、機能、価格設定、ターゲットユーザー層において差別化を図り、市場は急速に多様化と競争の時代へと突入しました。本レポートは、この活気に満ちた市場において、特に「無料」で利用可能なツールに焦点を当て、その実態を詳細に分析するものです。

### **1.2 「無料」の多様性：フリーミアム市場の解読**

AIコーディングアシスタント市場における「無料」という言葉は、一義的なものではありません。各社が採用するビジネスモデルによって、その意味合い、範囲、そして持続可能性は大きく異なります。開発者がツールを選定する上で、この「無料」の構造を正確に理解することは極めて重要です。本レポートでは、市場に存在する主要な無料提供モデルを以下の4つに分類し、以降の章で各ツールを分析するためのフレームワークとして提示します。

1. **寛大な無料枠モデル (Generous Free Tier):** このモデルは、個人開発者や学生、ホビイストを主なターゲットとし、非常に高い利用上限、あるいは実質的に無制限に近い形で主要機能を提供します。代表例はGoogleのGemini Code Assistで、月間18万回ものコード補完リクエストを無料で提供しています 5。このモデルの背景には、開発ツールそのものではなく、開発者を自社のクラウドプラットフォームなどのエコシステムに誘導するという戦略的な意図が存在します。ユーザーは利用量を気にすることなく、ツールの全機能を存分に試すことができます。  
2. **クレジット消費モデル (Credit-Based):** このモデルでは、ユーザーに毎月一定量の無料「クレジット」が付与されます。ユーザーは基本的な機能（例：単純なコード補完）は無制限に利用できる一方で、より高度なAIモデルを使用したチャットや複雑なコード生成といったプレミアム機能を利用する際に、このクレジットを消費します。WindsurfやSourcegraph Ampがこのモデルを採用しています 7。このアプローチは、基本的な利用は無料に保ちつつ、パワーユーザーや高度な機能を求めるユーザーから収益を得るためのバランスの取れた戦略です。ユーザーは自身の利用頻度に応じてコストを管理する必要があります。  
3. **機能制限モデル (Feature-Limited):** このモデルは、フリーミアムの最も古典的な形態です。基本的な機能、例えば一行単位の短いコード補完などは無料で提供されますが、複数行の補完、関数全体の生成、高度なチャット機能といった付加価値の高い機能は有料プランに限定されます。かつてのTabnine Basicプランがこの典型例でした 9。ユーザーは無料でツールの基本的な有用性を体験できますが、本格的な生産性向上を求める場合はアップグレードが必要となります。  
4. **セルフホスト・オープンソースモデル (Self-Hosted Open Source):** このモデルでは、ソフトウェアのライセンス自体がオープンソース（MITライセンスなど）として提供されるため、ライセンス料は完全に無料です。TabbyMLがこのモデルの代表格です 10。最大の利点は、ユーザーが自身のサーバー（オンプレミスまたはプライベートクラウド）にツールをデプロイできるため、ソースコードが外部に送信されることがなく、最大限のプライバシーとセキュリティを確保できる点です。しかし、「無料」なのはライセンス料のみであり、サーバーの構築・維持にかかるハードウェアコスト、電気代、そして管理・運用にかかる人件費といった「総所有コスト（TCO）」はユーザーが負担する必要があります。

これらのモデルを理解することは、各ツールの無料プランが提供する真の価値と、その裏にあるビジネス戦略を見抜く上で不可欠です。

### **1.3 評価軸の提示**

本レポートでは、多様なAIコーディングアシスタントを公平かつ多角的に評価するため、以下の主要な基準を設定します。これらの評価軸は、開発者が自身のニーズやプロジェクトの特性に最も合致したツールを選択する際の判断材料となることを目的としています。

* **無料プランの範囲と制限:** 各ツールの無料プランで何が提供され、どのような制限があるのかを具体的に分析します。これには、リクエスト回数、クレジット量、利用可能なAIモデルの種類、利用期間の有無などが含まれます。これは、「どこまで無料で使えるのか」というユーザーの最も基本的な問いに答えるための核心的な評価軸です。  
* **コア機能:** AIコーディングアシスタントとしての基本的な能力を評価します。主な評価項目は以下の通りです。  
  * **コード補完:** 提案の速度、精度、文脈理解度（単一行、複数行、関数全体）。  
  * **AIチャット:** コードに関する質問応答、デバッグ支援、仕様からのコード生成能力。  
  * **リファクタリング:** 既存コードの品質改善、最適化、言語変換能力。  
  * **テスト生成:** 単体テストやエッジケースを考慮したテストコードの自動生成能力。  
* **IDE/エディタ統合:** 開発者が日常的に使用する統合開発環境（IDE）やコードエディタとの連携の深さと広さを評価します。VS CodeやJetBrains製品群（IntelliJ, PyCharmなど）といった主要な環境への対応はもちろん、拡張機能の安定性やUIの使いやすさも重要な要素です。  
* **対応言語とフレームワーク:** サポートするプログラミング言語の多様性と、主要なフレームワーク（例: React, Django, Spring Boot）に対する理解度を評価します。特定の言語やフレームワークに特化した機能を持つツールも存在するため、その専門性も考慮に入れます。  
* **プライバシーとセキュリティ:** ユーザーのソースコードがどのように扱われるかは、特に企業利用において極めて重要な評価軸です。コードが外部サーバーに送信されるか、AIモデルの学習データとして利用されるか、そしてセルフホストという選択肢が提供されているか否かを明確にします。  
* **対象ユーザー層:** 各ツールがどのような開発者をメインターゲットとしているかを分析します。個人開発者、学生、スタートアップ、あるいはセキュリティ要件の厳しい大企業など、ターゲット層によって機能セットや価格設定の思想が異なるため、この点を明らかにします。

これらの評価軸に基づき、次章以降で各ツールを詳細に分析・評価していきます。

## **第2章：主要クラウドベースAIコーディングアシスタント：無料プラン徹底解剖**

クラウドベースのAIコーディングアシスタントは、導入の手軽さと強力なAIモデルへのアクセスを両立させており、現在の市場の主流を形成しています。本章では、特に注目すべきクラウドベースのツールを取り上げ、それぞれの無料プランが提供する機能、利用上限、そして特徴を徹底的に解剖します。

### **2.1 Gemini Code Assist (Google): 個人開発者のための圧倒的無料枠**

概要  
Googleが提供するGemini Code Assistは、同社の最先端AIモデルであるGemini 2.5 Proを搭載した、極めて強力なAIコーディングアシスタントです 11。Googleの膨大な技術的資産を背景に、特に個人開発者や学生、学習者に対して、市場で最も寛大な無料プランを提供している点が最大の特徴です。この戦略は、開発ツール市場におけるGoogleの存在感を一気に高める要因となっています。  
無料プランの範囲と制限  
Gemini Code Assistの個人向け無料プランは、その利用上限の高さにおいて他の追随を許しません。

* **アカウント要件:** この無料プランを利用するためには、@gmail.comのような個人のGoogleアカウントが必要です。企業のIT管理者が管理するGoogle Workspaceアカウントは対象外となるため、利用時には注意が必要です 13。  
* **利用上限:** 最大の魅力は、その圧倒的な利用枠にあります。コード補完や生成などのコード関連リクエストは**1日あたり6,000件**、AIとの対話を行うチャットリクエストは**1日あたり240件**まで無料で利用可能です 11。これを月間に換算すると、コード関連リクエストは約180,000件に達します。これは、他の多くの無料ツールが月間数千件程度に制限しているのと比較して桁違いに多く、「最も熱心なプロの開発者でさえ、この上限を超えるのは難しい」と公式に言及されるほどです 5。  
* **提供機能:** 無料でありながら、機能に大きな制限はありません。リアルタイムのコード補完、自然言語からのコード生成、IDEに統合されたAIチャット、既存コードのリファクタリング、単体テストの自動生成、さらにはデバッグ支援といった、開発ワークフローを加速させるための主要な機能がすべて無料で提供されます 11。

**IDE統合と対応言語**

* **IDE統合:** 開発者の多様な環境に対応するため、主要なIDEやエディタを幅広くサポートしています。Visual Studio Code (VS Code) やJetBrains製のIDE群（IntelliJ IDEA, PyCharm, Android Studioなど）向けの公式拡張機能が提供されています 11。また、ブラウザベースで利用できるGoogle Cloud Shell Editorにはプリインストールされており、環境構築なしで即座に試すことが可能です 11。  
* **対応言語:** 公開されている膨大なコードでトレーニングされているため、特定の言語に限定されることなく、Python, JavaScript, Java, Go, C++, Rust, SQLなど、事実上すべてのプログラミング言語をサポートしています 14。

Googleのこの戦略を深く分析すると、Gemini Code Assistの寛大な無料プランが、単なる開発者向けツール提供にとどまらない、より広範な目的を持っていることが明らかになります。他の多くの無料ツールが月間数千リクエストという上限を設ける中で、月間18万回という「実質的に無制限」とも言える上限を設定する背景には、開発者の心理に働きかける意図があります。クレジットベースのシステムで常に残量を気にしたり、厳しい上限に達して作業が中断されたりするストレスは、開発者にとって大きな認知負荷となります。Googleはこの認知負荷を完全に取り除くことで、「Gemini Code Assistを使っていれば上限の心配はない」という強力な安心感をユーザーに与えています。

この圧倒的な無料枠は、競合に対する強力な参入障壁として機能します。特に、AIアシスタントそのものが主要な収益源である独立系のツール企業にとって、同等の無料枠を提供することはビジネスモデル上不可能です。これにより、Googleは個人開発者、学生、ホビイストといった開発者コミュニティの草の根層におけるマインドシェアを独占し、将来の有料顧客やGoogle Cloud Platform (GCP) の利用者を育成することを目指しています。つまり、この無料プランは、コアとなるコード補完機能を市場でコモディティ化させ、競合他社に「単に強力なモデルにアクセスできる」以上の付加価値での勝負を強いる、極めて戦略的な一手なのです。

### **2.2 Amazon Q Developer (AWS): AWSエコシステムとのシームレスな連携**

概要  
Amazon Q Developerは、Amazon Web Services (AWS) が提供するAIコーディングアシスタントであり、旧サービスであるAmazon CodeWhispererから進化を遂げたものです 1。その最大の特徴は、AWSのサービス、API、ベストプラクティスに関する深い専門知識を持ち、AWS上でのアプリケーション開発に特化した支援を提供できる点にあります。AWSを主要なインフラとして利用する開発者やチームにとって、強力な味方となるツールです 4。  
無料プランの範囲と制限  
Amazon Q Developerは、開発者が気軽に試せるように恒久的な無料ティア（Perpetual Free Tier）を提供しています。

* **アカウント要件:** 無料プランを利用するには、個人のAWS Builder ID、または組織のAWS Identity and Access Management (IAM) ユーザーとしてログインする必要があります 19。IDE内での利用は、主にAWS Builder IDユーザー向けに提供されています。  
* **利用上限:** 無料ティアでは、**月間50回のエージェントリクエスト**が提供されます。これには、IDE内でのQ\&Aチャットや、より自律的なコード生成（エージェントコーディング）が含まれます 19。さらに、Javaアプリケーションのバージョンアップグレードを支援する機能として、  
  **月間1,000行のコード変換**も無料枠に含まれています 19。  
* **提供機能:** コア機能であるリアルタイムのコード提案はもちろんのこと、セキュリティの脆弱性をスキャンし、修正案を提示する機能も利用できます 1。特に強力なのは、AWSサービスに関する専門的なチャット機能です。「特定のIAMポリシーを作成するPythonコードを生成して」といった具体的な指示に対して、AWSのベストプラクティスに基づいた正確なコードを生成することができます 21。

**IDE統合と対応言語**

* **IDE統合:** 主要な開発環境を幅広くカバーしています。VS Code、JetBrains IDEs (IntelliJ, PyCharmなど)、Eclipse、Visual Studio向けの拡張機能が提供されており、AWS独自のクラウドベースIDEであるAWS Cloud9にも統合されています 20。  
* **対応言語:** Java, Python, JavaScript, TypeScript, C\#, Go, Rust, PHP, Ruby, Kotlin, C/C++など、15以上の主要なプログラミング言語と、Terraformなどで使用されるHCL (HashiCorp Configuration Language) をサポートしており、インフラ構築からアプリケーション開発まで幅広く対応します 23。

Amazon Q Developerの無料プランは、GoogleのGemini Code Assistと同様に、より大きなエコシステムへの誘導という戦略的文脈で理解する必要があります。月間50回というエージェントリクエストの上限は、一見すると限定的に見えるかもしれませんが、その価値はAWSという特定のドメイン知識にあります。このツールは、開発者がAWSの複雑で広範なサービス群を効率的に利用するための学習ツールおよびナビゲーターとして機能します。開発者は、ドキュメントを読み込む時間を削減し、AIとの対話を通じて迅速に必要なコードや設定例を入手できるため、AWS上での開発サイクルが大幅に短縮されます。したがって、Amazon Q Developerの無料プランは、単なるコーディング支援に留まらず、AWSプラットフォーム自体の利用体験を向上させ、開発者をAWSエコシステムに深く定着させるための強力なツールとして位置づけられているのです。

### **2.3 Windsurf (旧Codeium): 速度と寛容性を両立したフリーミアムモデル**

概要  
Windsurfは、かつて「個人利用は完全無料で無制限」という非常に寛大なポリシーで開発者コミュニティから高い評価を得ていたCodeiumがリブランドしたツールです 24。その核となる哲学は引き継がれつつ、より高度なエージェント機能（  
Cascade）をプレミアム機能として提供する、バランスの取れたフリーミアムモデルへと進化しました。稲妻のような高速なコード補完と、最新のAIモデルを活用した高度な対話機能の両立を目指しています 24。

無料プランの範囲と制限  
Windsurfの無料プランは、日常的なコーディング作業と、時折必要となる高度なAI支援を巧みに両立させる構成になっています。

* **基本機能（無制限・無料）:** 開発者が最も頻繁に利用するであろう基本的なコード補完機能（Fast Tab）、自然言語によるコマンド実行（Command）、そしてWindsurf独自の軽量モデル（SWE-1 Lite）の利用は、**完全に無料で、利用回数に制限はありません** 7。これは、旧Codeiumの「個人利用は無料」という精神を色濃く反映しており、開発者はコストを気にすることなくコーディングの効率化を図ることができます。  
* **クレジットシステム（制限あり）:** OpenAIのGPTシリーズやAnthropicのClaudeシリーズ、GoogleのGeminiといった最先端のプレミアムAIモデルを利用した高度なチャット機能（Cascade）には、クレジットシステムが適用されます。無料プランのユーザーには、**毎月25プロンプトクレジット**が付与されます 7。  
* **消費ルール:** このクレジットは、ユーザーがプレミアムモデルに対してプロンプトを送信するごとに1回消費されます。重要なのは、AIが内部で複数のステップ（ツールコールや思考プロセス）を実行した場合でも、ユーザー側のアクションは1プロンプトとしてカウントされる点です 27。これにより、ユーザーはクレジットの消費を予測しやすくなっています。例えば、1クレジットでGPT-4.1を利用したプロンプトが約4回可能とされており、実質的には月間100回程度の高度なAIとの対話が無料で行える計算になります 29。

**IDE統合と対応言語**

* **IDE統合:** Windsurfは非常に幅広い開発環境をサポートしており、VS Code, JetBrains IDEs, Jupyter Notebookなど、40種類以上のIDEやエディタに対応する拡張機能を提供しています 31。  
* **対応言語:** 対応言語も70種類以上と多岐にわたり、Python, JavaScript, TypeScript, PHP, Go, Java, C++, Rust, Rubyといった主要言語を網羅しています 33。

Windsurfのフリーミアムモデルは、市場における巧みなポジショニング戦略を反映しています。基本的なコード補完を無制限・無料とすることで、日常的なコーディング効率を求める大多数の開発者を惹きつけ、ユーザーベースを拡大します。一方で、より複雑な問題解決やアーキテクチャ設計のために最新・最強のAIモデルを求めるパワーユーザーに対しては、クレジットベースの課金モデルを用意することで収益化を図っています。この二段構えのアプローチにより、GoogleやAmazonのような巨大資本を持たない独立系ツールでありながら、持続可能なビジネスモデルを構築し、幅広いユーザー層に価値を提供することに成功しています。

### **2.4 Cursor: AIネイティブな開発体験を提供するエディタ**

概要  
Cursorは、一般的なIDEに拡張機能としてAIを追加するアプローチとは一線を画します。広く普及しているオープンソースエディタであるVS Codeを基盤（フォーク）としながら、AIとの対話や協調を前提としてエディタ全体を再設計した「AIネイティブ」な開発環境です 35。これにより、単なる機能追加では実現できない、よりシームレスで深いレベルでのAI統合体験を提供することを目指しています。VS Codeユーザーであれば、既存の拡張機能、テーマ、ショートカットキーをそのまま引き継げるため、移行がスムーズである点も大きな利点です 35。  
無料プランの範囲と制限  
Cursorの無料プランは「Hobby」プランと名付けられており、ツールの基本的な機能を試すためのエントリーポイントとして位置づけられています 37。

* **利用上限:** 新規ユーザーはまず2週間のProプランのトライアルを体験できます。トライアル期間が終了すると、Hobbyプランの制限が適用されます。具体的には、高度なAIエージェント機能の利用が**月間50回の低速リクエスト（slow requests）に、そしてリアルタイムのコード補完（Tab completions）が月間2,000回**に制限されます 38。  
* **モデルアクセス:** 無料プランで利用できるAIモデルには制限がある可能性があります。有料のProプランでは、Claude Sonnet 4, OpenAI GPT-4.1, Gemini 2.5 Proといった、市場をリードする複数のフロンティアモデルを切り替えて利用することが可能です 37。  
* **機能:** コードベース全体に関する質問、複数ファイルにまたがるコード編集、Web検索を伴う調査など、エディタに深く統合されたエージェント機能がCursorの真骨頂ですが、無料プランではこれらの利用回数が限られます。

Cursorは、その革新的なアプローチで多くの先進的な開発者を惹きつけましたが、同時に価格設定の変更を巡る混乱は、開発者ツール市場における重要な教訓を残しました。2025年6月、CursorはProプランの価格体系を、月間500リクエストという明確な上限から、「20ドル分のAPI利用量」に相当するという曖昧な「コンピュート上限」へと予告なく変更しました 40。この変更は十分に周知されず、これまで上限を気にせずに利用していた多くのユーザーが、予期せぬレート制限に遭遇したり、利用料金が急騰したりする事態に直面しました 40。

この出来事に対する開発者コミュニティの反応は、単なる価格への不満にとどまりませんでした。問題の核心は、開発者が自身のワークフローの基盤として信頼するツールが、突如として予測不可能な振る舞いを始めたことによる「信頼の喪失」でした。開発ツールにとって、機能の優劣と同じくらい、動作の安定性、予測可能性、そして価格の透明性が重要です。この一件は、たとえ技術的に優れた製品であっても、ユーザーとの信頼関係を損なうようなコミュニケーションや価格戦略は、深刻なユーザー離れを引き起こしかねないことを示しています。したがって、無料ツールを評価する際には、提示されている利用上限の数値だけでなく、その制限がどれだけ明確で、安定的であるかという点も考慮に入れるべきでしょう。

### **2.5 Kiro (Amazon): スペック駆動開発という新たなパラダイム**

概要  
Kiroは、Amazonから登場した新しいAI開発環境であり、従来のAIコーディングのあり方に一石を投じる野心的なコンセプトを掲げています 44。多くのAIアシスタントが、開発者によるその場その場の思いつきのプロンプト（Amazonはこれを "vibe coding" と呼ぶ）に反応する形で機能するのに対し、Kiroはまず初めに自然言語で記述された仕様書（"spec"）を作成し、その仕様書に基づいて体系的に開発を進める「スペック駆動開発」を提唱しています 46。これにより、大規模で複雑なプロジェクトにおいてもAIエージェントが一貫性を保ち、開発者の真の意図から逸脱することなく作業を進めることを可能にします。  
無料プランの範囲と制限  
Kiroは比較的新しいツールであり、その価格体系はまだ流動的です。

* **現状:** 2025年8月現在、Kiroはプレビュー期間中であり、**無料で利用可能**です。これにより、ユーザーは新しい開発パラダイムをリスクなく試すことができます 44。  
* **正式リリース後の予定:** プレビュー期間の終了後には、正式な無料ティアが提供される計画です。この無料プランには、**月間50回のエージェントインタラクション**が含まれる予定です 48。  
* **リクエストの定義:** Kiroの利用量は、2種類のインタラクションで計測されます。  
  1. **Vibe Request:** 従来のAIチャットのように、Q\&Aや対話形式でのコード生成など、自由形式のプロンプトによるインタラクションを指します。無料プランの上限である「50回のエージェントインタラクション」は、主にこのVibe Requestを指すものと考えられます 49。  
  2. **Spec Request:** Kiroの核心機能であり、生成された仕様書（tasks.mdなど）に基づいて、構造化されたタスクを実行するリクエストです。1つのタスク実行が1 Spec Requestに相当します 50。プレビュー終了後の無料プランに、このSpec Requestが含まれるかどうかは現時点では明確にされていません 51。

IDE統合と対応言語  
Kiroは独自のIDEとして提供されるか、あるいはVS Codeなどの主要なエディタ向けの拡張機能として提供されることが想定されます。内部ではAnthropic社のClaude Sonnet 4を主要なAIモデルとして利用しており 44、主要なプログラミング言語は幅広くサポートされる見込みです。Kiroのスペック駆動開発は、AIとの協業における新たな標準となる可能性を秘めており、今後の動向が注目されます。

### **2.6 Bito: コードレビューとPR要約に強み**

概要  
Bitoは、単なるコード生成や補完に留まらず、特にチーム開発のワークフローにおいて重要な「コードレビュー」と「プルリクエスト（PR）の要約」というプロセスにAIを適用することで、独自の価値を提供するツールです 9。開発者が作成した変更内容をAIが自動的に分析し、人間がレビューしやすいように要約を生成したり、潜在的な問題を指摘したりすることで、チーム全体の開発速度とコード品質の向上を目指します。  
無料プランの範囲と制限  
Bitoは「Forever Free」と銘打った恒久的な無料プランを提供しており、個人開発者や小規模チームが気軽に利用を開始できます 53。

* **利用上限:**  
  * **AIチャット:** 無料プランでは、GPT-3.5などの基本的なAIモデルを使用して、**1日あたり最大75リクエスト**までチャット機能を利用できます 54。ただし、一部の資料では日次20リクエストという記述も見られ、利用状況によって変動する可能性があります 53。  
  * **コード補完:** コード補完機能は、**月間300回**まで利用可能です。これには1日あたり75回という上限も設定されています 54。  
* **提供機能:** 無料プランの最も特徴的な機能は、GitHub, GitLab, Bitbucketと連携した**AIによるプルリクエスト要約**です 52。これにより、レビュー担当者は変更の概要を迅速に把握できます。一方で、GPT-4oのようなより高度なAIモデルの利用や、リポジトリ全体を深く理解して文脈に応じたフィードバックを行う「コードベース認識」機能、詳細なコードレビュー機能などは有料のTeamプランに含まれます 53。

**IDE統合とプライバシー**

* **IDE統合:** Bitoは、VS CodeやJetBrains IDEs向けの拡張機能を提供しており、開発者は慣れ親しんだ環境でその機能を利用できます 57。  
* **プライバシー:** Bitoはプライバシー保護を重視しており、ユーザーのコードをサーバーに保存したり、AIモデルのトレーニングデータとして利用したりしないことを明確に約束しています 9。通信は暗号化され、AIパートナー（OpenAI, Anthropic）のサーバーにもコードデータは保存されないとされており、セキュリティを重視するユーザーにとって安心材料となります 57。

Bitoの無料プランは、特にチームでの共同作業やオープンソースプロジェクトへの貢献など、他者のコードをレビューする機会が多い開発者にとって、ユニークで実用的な価値を提供します。

## **第3章：セルフホスト型オープンソースという選択肢**

クラウドベースのサービスが手軽さと高性能なモデルへのアクセスを提供する一方で、セキュリティ、プライバシー、そしてカスタマイズ性を最優先する開発者や企業にとっては、セルフホスト型のオープンソースツールが依然として強力な選択肢であり続けています。本章では、このカテゴリーの代表格であるTabbyMLに焦点を当て、その特徴と「無料」という言葉が持つ独自の意味合いを深く掘り下げます。

### **3.1 TabbyML: プライバシーとコントロールを最優先する開発者のための選択肢**

概要  
TabbyMLは、GitHub Copilotのオープンソースかつオンプレミスな代替となることを明確な目標として開発されている、セルフホスト型のAIコーディングアシスタントです 58。最大の特徴は、すべてのコンポーネントをユーザーが管理するインフラストラクチャ上で実行できる点にあります。これにより、ソースコードや開発中のデータが組織のファイアウォールから一切外部に出ることがなく、最高レベルのセキュリティとデータプライバシーを確保することが可能です 59。  
「無料」の定義  
TabbyMLにおける「無料」とは、ソフトウェアライセンス料が不要であることを意味します。プロジェクトはMITライセンスなどの寛容なオープンソースライセンスの下で公開されており、誰でも自由にダウンロードし、利用し、改変することができます 60。しかし、これはクラウドサービスのようにサインアップすればすぐに使える「無料」とは根本的に異なります。TabbyMLの「無料」は、その運用に伴うコストをユーザー自身が負担することを前提としています。  
この運用コストは「総所有コスト（Total Cost of Ownership, TCO）」という概念で捉えるのが適切です。TCOには、AIモデルを稼働させるためのサーバーハードウェアの購入費用（資本的支出、CapEx）や、サーバーの電気代、そして最も見過ごされがちですが重要な、システムのセットアップ、定期的なメンテナンス、アップデート、トラブルシューティングに対応するためのエンジニアの時間（運用的支出、OpEx）が含まれます。したがって、TabbyMLが経済的に合理的な選択肢となるのは、既に適切なハードウェア資産を保有しているか、あるいは厳格なセキュリティ要件のために外部サービスを利用できないといった、明確な理由がある場合に限られます。個人開発者がTabbyMLのために高性能なGPUを新たに購入する場合、その費用は数年分の有料クラウドサービスのサブスクリプション料金を容易に上回る可能性があります。

主要機能  
ライセンスが無料であるからといって、機能が劣っているわけではありません。TabbyMLは、最先端のクラウドサービスに匹敵する豊富な機能セットを提供しています。

* **コア機能:** リアルタイムのコード補完はもちろん、リポジトリ内のドキュメントやコードを学習し、質問に答えるAIチャット機能（Answer Engine）、そしてエディタ内で直接AIと対話しながらコーディングを進めるインラインチャットなど、モダンなAIアシスタントに求められる機能が一通り揃っています 59。  
* **カスタマイズ性:** TabbyMLの真価は、その高いカスタマイズ性にあります。ユーザーは、CodeLlamaやStarCoderといった様々なオープンソースLLMの中から、自身の要件やハードウェア性能に合ったモデルを自由に選択して接続できます 62。さらに、自社のプライベートリポジトリのコードを用いてモデルをファインチューニングし、独自のコーディング規約や内部ライブラリに特化した、世界に一つだけのAIアシスタントを構築することも可能です 60。

ハードウェア要件（セルフホストのコスト）  
TabbyMLを快適に運用するためには、一定水準のハードウェアが要求されます。

* **CPU/RAM:** 基本的な運用には最低でも8GBのシステムRAMが必要ですが、より大規模なモデルを扱う場合は16GB以上が強く推奨されます 63。  
* **GPU:** CPUのみでも動作は可能ですが、実用的な応答速度を得るためにはGPUの利用がほぼ必須です。コンシューマーグレードのGPU、例えばNVIDIAのGeForce 10シリーズ以上や、Apple Silicon (M1/M2) などで動作させることが可能です 58。特に、CodeLlama-7Bのような中規模モデルをint8量子化モードで快適に動作させるためには、8GB以上のVRAMを持つGPUが一つの目安となります 65。

**IDE統合と対応言語**

* **IDE統合:** TabbyMLは、開発者の多様な作業環境に対応するため、非常に幅広いIDEをサポートしています。VS Code、JetBrains製品群（IntelliJ, PyCharm, GoLand, Riderなど）、Neovim、Eclipse、さらにはVimまで、主要なエディタ向けの拡張機能が提供されています 59。  
* **対応言語:** Rust, Python, JavaScript/TypeScript, Go, Java/Kotlin, C/C++, PHP, C\#, Rubyなど、現代的なソフトウェア開発で用いられるほとんどの主要言語を公式にサポートしています 69。

結論として、TabbyMLは「無料」の概念をライセンス料から総所有コストへと転換させることで、絶対的なデータコントロールと無限のカスタマイズ性という、クラウドサービスでは得られない独自の価値を提供します。これは、コストよりもプライバシーと自律性を優先する組織や開発者にとって、他に代えがたい選択肢となり得ます。

## **第4章：提供形態が移行・終了するツールに関する注記**

AIコーディングアシスタント市場は非常に速いペースで進化しており、各社のビジネスモデルやサービス提供形態も頻繁に変化します。本レポートの基準日である2025年8月時点で、かつては著名な無料プランを提供していたものの、現在はその形態を終了、あるいは大きく変更したツールがいくつか存在します。ユーザーが古い情報に惑わされることのないよう、本章ではこれらのツールに関する最新状況を正確に記述します。

### **4.1 Sourcegraph Cody: 無料プランの終了と「Amp」への移行**

重要なお知らせ  
Sourcegraph社は、同社のAIコーディングアシスタントであるCodyに関して、戦略的な方針転換を行いました。公式発表によると、2025年7月23日をもって、従来の「Cody Free」および「Cody Pro」プランの提供は完全に終了されました 70。したがって、本レポートの基準日である2025年8月時点において、これらのプランは新規・既存ユーザーともに利用不可能です。この変更は、同社がより高度で自律的な「エージェント」機能に注力するための戦略的判断の一環です。  
後継サービス「Amp」  
Cody Free/Proプランの終了に伴い、Sourcegraphは後継となる新しいAIツール「Amp」を市場に投入しました 8。Ampは、単一のプロンプトで複数ファイルにまたがる複雑なタスクを自律的に実行する「エージェント的ワークフロー」に特化しており、従来のCodyとは異なるコンセプトの製品です 8。  
Ampの無料利用  
Ampには恒久的な無料プランは存在しませんが、新規ユーザーがサービスを試用できるよう、クレジットベースのインセンティブが提供されています。

* **初回無料クレジット:** Ampに新規登録したユーザーには、**10ドル相当の無料クレジット**が付与されます 8。  
* **移行ユーザー向けクレジット:** サービス終了の影響を受ける旧Codyユーザーに対しては、追加のクレジットが提供される移行措置が取られました。Cody Freeからの移行ユーザーには10ドル分、Cody Proからの移行ユーザーにはさらに30ドル分を追加した合計40ドル分のクレジットが付与されます 71。  
* **クレジット消費モデル:** Ampのクレジットは、使用する大規模言語モデル（LLM）の種類や処理量に応じて消費されます。そのため、付与された10ドル分のクレジットでどの程度の作業が可能かは、ユーザーの利用パターン（例えば、複雑なタスクを依頼するか、簡単な質問をするかなど）に大きく依存します。一部のユーザーレビューでは、クレジットの消費ペースが想定よりも速いとの指摘も見られ、利用時には注意が必要です 73。

この変更は、AIコーディングアシスタント市場が、単純なコード補完から、より高度で価値の高いエージェント機能へと進化していることを象徴しています。Sourcegraphは、無料ユーザー層を広くカバーする戦略から、高度な機能を求めるプロフェッショナルユーザーに焦点を絞った、より持続可能なビジネスモデルへと舵を切ったと分析できます。

### **4.2 Tabnine: Basic無料プランの終了とDev Previewへの移行**

重要なお知らせ  
AIコーディングアシスタントの草分け的存在であるTabnineもまた、無料プランに関する大きな戦略変更を行いました。公式なアナウンスによると、2025年4月2日をもって、長年提供されてきた「Tabnine Basic」無料プランは提供を終了しました 74。これにより、かつてTabnineの代名詞であった「基本的なコード補完が永続的に無料」というモデルは過去のものとなりました。  
新体系「Tabnine Dev Preview」  
従来のBasicプランに代わり、Tabnineは新たなトライアル制度を導入しました。

* **Dev Preview:** 新規ユーザーは、「Tabnine Dev Preview」として、有料プランである「Dev」プランの全機能を**14日間、無料で体験**することができます 74。  
* **登録要件:** このプレビュー期間を利用するためにクレジットカードの登録は不要ですが、メールアドレスによるユーザー登録が必須となりました。これは、サービスの不正利用を防ぐための措置です 74。  
* **プレビュー後の流れ:** 14日間のプレビュー期間が終了した後、Tabnineを引き続き利用するためには、有料の「Dev」プラン（月額9ドルから）に移行する必要があります 74。  
* **情報の錯綜に関する注記:** 一部のサードパーティのウェブサイトでは、依然としてTabnineに機能が制限された無料プランが存在するかのような記述が見受けられますが 9、Tabnine自身の公式ドキュメントおよび発表 74 に基づけば、恒久的に利用可能な無料プランは2025年8月時点では存在しないと結論付けるのが正確です。

Tabnineのこの戦略変更は、市場の成熟を反映しています。AIモデルの運用コストが増大する中で、多くの独立系ツール企業にとって、機能が制限された無料プランを永続的に提供し続けることは、ビジネス上の負担となりつつあります。Tabnineは、無料ユーザーを広く維持するモデルから、有料転換を前提とした期間限定のフルトライアルモデルへと移行することで、より持続可能な収益構造の構築を目指していると考えられます。これにより、ユーザーは短期間で製品の全価値を評価することが求められるようになります。

## **第5章：総合比較とユースケース別選定ガイド**

これまで各ツールの詳細を分析してきましたが、本章ではそれらの情報を統合し、読者が自身の状況に最適なツールを戦略的に選択できるよう、多角的な比較と具体的なユースケースに基づいた選定ガイドを提供します。

### **5.1 機能比較マトリクス**

以下の表は、本レポートで取り上げた主要なAIコーディングアシスタントの無料プランにおける特徴を一覧にまとめたものです。これにより、各ツールの強みと制限を迅速に比較検討することが可能となります。

**Table 1: 主要AIコーディングアシスタント無料プラン比較**

| ツール名 | 無料プランのコア機能 | 無料プランの主な制限 | 主要AIモデル | 主要対応IDE | 特徴/差別化要因 |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **Gemini Code Assist** | コード補完, チャット, リファクタリング | 日次6,000補完, 240チャット | Gemini 2.5 Pro | VS Code, JetBrains, Android Studio | 圧倒的な無料枠、Google Cloud連携 |
| **Amazon Q Developer** | コード補完, AWS特化チャット | 月間50エージェントリクエスト | Claude | VS Code, JetBrains, AWS Cloud9 | AWSエコシステムとの深い統合 |
| **Windsurf** | 無制限の基本補完, チャット | プレミアムモデル利用は月25クレジット | 独自モデル, OpenAI, Claude, Gemini | VS Code, JetBrains (40+) | 高速な基本補完は完全無料 |
| **Cursor** | AI統合エディタ | 月間50低速リクエスト, 2000補完 | OpenAI, Claude, Gemini | 独自 (VS Codeベース) | AIネイティブなエディタ体験 |
| **Kiro** | スペック駆動開発, チャット | (プレビュー後) 月間50 Vibeリクエスト | Claude Sonnet 4 | 独自IDE/VS Code拡張 | 仕様書ベースの体系的開発支援 |
| **Bito** | PR要約, チャット, コード補完 | 日次75チャット, 月間300補完 | OpenAI, Anthropic | VS Code, JetBrains | コードレビューとPR要約機能 |
| **TabbyML** | コード補完, チャット | セルフホストのハードウェア/運用コスト | 選択可能 (CodeLlama等) | VS Code, JetBrains, Neovim | オープンソース, 完全セルフホスト |
| **(旧) Sourcegraph Cody** | \- | 2025年7月23日提供終了 | \- | \- | 後継のAmpは$10の初回クレジット提供 |
| **(旧) Tabnine Basic** | \- | 2025年4月2日提供終了 | \- | \- | 14日間のDev Previewに移行 |

### **5.2 「無料」のスペクトラム分析**

第1章で提示した4つの「無料」モデルに基づき、各ツールを分類することで、その提供形態の本質をより明確に理解することができます。

* **寛大な無料枠モデル:** このカテゴリーに属するのは、**Gemini Code Assist**と**Amazon Q Developer**です。両者ともに巨大なクラウドプラットフォームを背景に持ち、開発ツールをエコシステムへの入り口と位置づけているため、他の追随を許さない寛大な無料プランを提供できています。ユーザーは利用量をほとんど気にすることなく、高度な機能を利用できます。  
* **クレジット消費モデル:** **Windsurf**とSourcegraphの**Amp**がこのモデルを採用しています。基本的な機能は無料または低コストに抑えつつ、最新・最強のAIモデルを利用するような高度な操作に対してクレジットを消費させるハイブリッドなアプローチです。これにより、ライトユーザーからパワーユーザーまで、幅広い層のニーズに対応しつつ、収益性を確保しています。  
* **機能制限モデル:** **Cursor**, **Kiro**, **Bito**がこのカテゴリーに分類されます。これらのツールは、無料プランで基本的な機能や一定回数の利用を提供し、ツールのコンセプトや有用性を体験させます。しかし、本格的に生産性を向上させるためには、より多くの機能や高い利用上限を持つ有料プランへのアップグレードが実質的に必要となる設計になっています。  
* **セルフホスト・オープンソースモデル:** **TabbyML**がこのモデルの唯一の代表です。ライセンス料は無料ですが、運用にかかる総所有コスト（TCO）はユーザーが負担します。絶対的なプライバシーとコントロールを求めるユーザーにとっての選択肢です。  
* **トライアルのみ:** **Tabnine**は、恒久的な無料プランを廃止し、14日間の全機能トライアル（Dev Preview）に移行しました。これは、製品の価値を短期間で集中的に評価してもらい、有料プランへの転換を促す戦略です。

### **5.3 あなたに最適なAIペアプログラマーは？：ユースケース別推奨ツール**

最適なツールは、開発者の目的、プロジェクトの性質、そして所属する組織のポリシーによって異なります。以下に、具体的なユースケースに基づいた推奨ツールを提示します。

**ユースケース1: 学習目的の学生・ホビイスト、またはコストを最優先する個人開発者**

* **推奨ツール:** **Gemini Code Assist**  
* **選定理由:** 他のツールとは比較にならない圧倒的な無料利用枠が最大の理由です。利用上限を心配することなく、コード生成、チャットによる質問、リファクタリング、テスト生成といったAIコーディングのあらゆる側面を心ゆくまで探求できます 5。主要なIDEとほぼ全てのプログラミング言語をサポートしているため、特定の技術スタックに縛られることなく、幅広い学習用途に最適です。

**ユースケース2: プライバシーとデータの管理を最優先する企業・開発者**

* **推奨ツール:** **TabbyML**  
* **選定理由:** ソースコードを絶対に外部のサーバーに送信できない、あるいはしたくないという厳格なセキュリティ要件を持つ場合、セルフホスト可能なTabbyMLが唯一の選択肢となります 59。オープンソースであるため、内部で何が行われているかの透明性が高く、企業のセキュリティ監査にも対応しやすいです。導入にはハードウェアと運用スキルが必要ですが、それに見合うだけのコントロールと安心感を得られます。

**ユースケース3: AWSをメインのクラウドプラットフォームとして利用する開発者**

* **推奨ツール:** **Amazon Q Developer**  
* **選定理由:** AWSのサービス、API、IAMポリシー、インフラ構成などに関する質問に対して、他のどの汎用AIツールよりも正確で、文脈に応じた、ベストプラクティスに基づいた回答を提供します 4。AWSコンソールとの深い統合も強みであり、AWS上での開発と運用の効率を劇的に向上させることができます。

**ユースケース4: とにかく高速なコード補完を無制限に使いたい開発者**

* **推奨ツール:** **Windsurf**  
* **選定理由:** 開発作業の中で最も頻度が高いのは、やはりコードの入力と補完です。Windsurfは、この最も基本的なコード補完機能（Fast Tab）を、完全に無料で、しかも利用回数無制限で提供しています 7。高度なチャット機能はクレジット制ですが、日常的なコーディングの大部分を占める補完作業を、コストを一切気にすることなく高速化できる点は、多くの開発者にとって大きな魅力です。

**ユースケース5: 最新のAIエージェント機能を試したい、先進的な開発者**

* **推奨ツール:** **Cursor** または **Kiro**  
* **選定理由:** これらのツールは、単なる補完・チャットツールという枠組みを超え、AIとのより深い対話を通じて開発プロセス全体を革新しようという野心的なビジョンを持っています。CursorはAIとの協調を前提としたエディタ体験を 35、Kiroは仕様書に基づいた体系的な自律開発を目指しています 78。無料プランには制限がありますが、AIによるソフトウェア開発の未来をいち早く体験したい開発者にとっては、最も刺激的な選択肢となるでしょう。

## **第6章：結論と今後の展望**

### **6.1 調査結果の要約**

本レポートで実施した広範な調査分析の結果、2025年8月時点における無料で利用可能なAIコーディングアシスタント市場に関して、以下の結論が導き出されました。

第一に、個人開発者が無料で利用できる高品質なツールは多数存在しますが、「無料」という言葉が内包する価値と制約は、ツールによって大きく異なることが明らかになりました。利用者は、単に「無料」であるという事実だけでなく、その提供形態（寛大な無料枠、クレジット消費、機能制限、セルフホスト）を深く理解し、自身のニーズと照らし合わせる必要があります。

第二に、市場の競争構造は、巨大クラウドプロバイダー（Google, Amazon）と、独立系ツールベンダーとの間で明確に二極化しています。前者は、AIアシスタントを自社の広範なエコシステムへの戦略的なゲートウェイと位置づけ、市場で最も寛大な無料プランを提供することでユーザーベースの獲得を狙っています。これに対し、後者はAIアシスタント自体を主要な収益源とするため、持続可能なビジネスモデルを模索する中で、無料プランの制限を強化したり、より洗練されたクレジットベースのモデルへと移行したりする傾向が顕著です。Sourcegraph CodyやTabnineの無料プラン終了は、この市場力学を象徴する出来事です。

第三に、プライバシーとデータコントロールは、依然として重要な差別化要因であり続けています。TabbyMLに代表されるセルフホスト型オープンソースの選択肢は、クラウドベースのサービスが提供する利便性とは異なる次元で、セキュリティ要件の厳しい企業やプライバシーを重視する開発者層から強い支持を得ています。

### **6.2 市場の今後の展望**

AI技術の急速な進化と市場競争の激化を踏まえると、AIコーディングアシスタント市場は今後、以下の方向に沿って発展していくと予測されます。

* **機能のコモディティ化と差別化の深化:** 現在、主要な差別化要因となっているコード補完や基本的なチャット機能は、今後さらに性能が向上し、どのツールでも高い水準で提供される「当たり前の機能」へとコモディティ化が進むでしょう。その結果、市場での競争軸は、より高度な領域へとシフトします。具体的には、複数ファイルにまたがる複雑なタスクを自律的に実行する「エージェント機能」、AWSやWordPressといった特定の技術ドメインやプラットフォームへの深い専門性、そしてコードレビュー、テスト、デプロイといった開発ライフサイクル全体への統合の度合いが、新たな差別化のポイントになると考えられます。  
* **ビジネスモデルのさらなる多様化:** 市場の成熟に伴い、ビジネスモデルもさらに洗練され、多様化していくことが予想されます。単純な月額固定課金だけでなく、AmpやWindsurfが採用する、実際の利用量に応じてコストが変動するクレジット消費モデルは、より公平な価格設定として広まる可能性があります。また、TabbyMLのように、オープンソースの本体は無料で提供しつつ、導入支援やセキュリティ機能、プライベートモデルのホスティングといったエンタープライズ向けのサポートを有料で提供するビジネスモデルも、独立系ベンダーにとって有力な戦略となるでしょう。  
* **開発者体験（Developer Experience, DX）の至上主義:** 最終的に、どのツールが開発者に選ばれるかを決定づけるのは、技術仕様や機能リスト以上に、総合的な「開発者体験」です。AIの提案がどれだけ開発者の思考の流れを妨げずに、シームレスに統合されるか。UI/UXは直感的で、応答速度はストレスなく、提案されるコードの品質は信頼に足るものか。これらの要素が、日々の生産性に直接的な影響を与えます。AIが開発者の「邪魔」になるのではなく、真に「思考の増幅器」として機能するような、優れた開発者体験を提供できるツールが、最終的な勝者となるでしょう。

AIコーディングアシスタントは、もはや一部の先進的な開発者だけのものではなく、すべての開発者にとって標準的なツールキットの一部となりつつあります。このダイナミックな市場の進化は、ソフトウェア開発の未来そのものを形作っていくに違いありません。

#### **引用文献**

1. 【徹底比較】コード生成AIツールおすすめ10選と選び方・活用ガイド \- Qbook, 8月 29, 2025にアクセス、 [https://www.qbook.jp/column/2004.html](https://www.qbook.jp/column/2004.html)  
2. 2025年のトップ18 AIコーディングアシスタントツール \- Apidog, 8月 29, 2025にアクセス、 [https://apidog.com/jp/blog/top-ai-coding-assistant-tools-jp/](https://apidog.com/jp/blog/top-ai-coding-assistant-tools-jp/)  
3. 20 Best AI-Powered Coding Assistant Tools in 2025 \- Spacelift, 8月 29, 2025にアクセス、 [https://spacelift.io/blog/ai-coding-assistant-tools](https://spacelift.io/blog/ai-coding-assistant-tools)  
4. Best AI Coding Assistants as of August 2025 \- Shakudo, 8月 29, 2025にアクセス、 [https://www.shakudo.io/blog/best-ai-coding-assistants](https://www.shakudo.io/blog/best-ai-coding-assistants)  
5. Get coding help from Gemini Code Assist — now for free \- The Keyword, 8月 29, 2025にアクセス、 [https://blog.google/technology/developers/gemini-code-assist-free/](https://blog.google/technology/developers/gemini-code-assist-free/)  
6. Gemini Code Assist によるコーディング支援が無償で利用可能に Google Cloud 公式ブログ, 8月 29, 2025にアクセス、 [https://cloud.google.com/blog/ja/topics/developers-practitioners/gemini-code-assist](https://cloud.google.com/blog/ja/topics/developers-practitioners/gemini-code-assist)  
7. Pricing \- Windsurf, 8月 29, 2025にアクセス、 [https://windsurf.com/pricing](https://windsurf.com/pricing)  
8. Pricing \- Sourcegraph, 8月 29, 2025にアクセス、 [https://sourcegraph.com/pricing](https://sourcegraph.com/pricing)  
9. 18 Free GitHub Copilot Alternatives for VS Code 2025 \- Bito AI, 8月 29, 2025にアクセス、 [https://bito.ai/blog/free-github-copilot-alternatives-for-vs-code/](https://bito.ai/blog/free-github-copilot-alternatives-for-vs-code/)  
10. TabbyML/tabby: Self-hosted AI coding assistant \- GitHub, 8月 29, 2025にアクセス、 [https://github.com/TabbyML/tabby](https://github.com/TabbyML/tabby)  
11. Gemini Code Assist AI coding assistant, 8月 29, 2025にアクセス、 [https://codeassist.google/](https://codeassist.google/)  
12. developers.google.com, 8月 29, 2025にアクセス、 [https://developers.google.com/gemini-code-assist/docs/overview](https://developers.google.com/gemini-code-assist/docs/overview)  
13. FAQs Gemini Code Assist Google for Developers, 8月 29, 2025にアクセス、 [https://developers.google.com/gemini-code-assist/resources/faqs](https://developers.google.com/gemini-code-assist/resources/faqs)  
14. Gemini Code Assist \- Visual Studio Marketplace, 8月 29, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist](https://marketplace.visualstudio.com/items?itemName=Google.geminicodeassist)  
15. Supported languages, IDEs, and interfaces Gemini for Google Cloud, 8月 29, 2025にアクセス、 [https://cloud.google.com/gemini/docs/codeassist/supported-languages](https://cloud.google.com/gemini/docs/codeassist/supported-languages)  
16. Code with Gemini Code Assist Standard and Enterprise Gemini for Google Cloud, 8月 29, 2025にアクセス、 [https://cloud.google.com/gemini/docs/codeassist/write-code-gemini](https://cloud.google.com/gemini/docs/codeassist/write-code-gemini)  
17. Supported Languages and Frameworks \- Tutorialspoint, 8月 29, 2025にアクセス、 [https://www.tutorialspoint.com/gemini-code-assist/supported-languages-and-frameworks.htm](https://www.tutorialspoint.com/gemini-code-assist/supported-languages-and-frameworks.htm)  
18. 解体新書：AIコーディング支援ツールとは \- Arpable, 8月 29, 2025にアクセス、 [https://arpable.com/artificial-intelligence/ai-coding-assistance-tool/](https://arpable.com/artificial-intelligence/ai-coding-assistance-tool/)  
19. AI for Software Development – Amazon Q Developer Pricing \- AWS, 8月 29, 2025にアクセス、 [https://aws.amazon.com/q/developer/pricing/](https://aws.amazon.com/q/developer/pricing/)  
20. Amazon Q Developer \- Generative AI, 8月 29, 2025にアクセス、 [https://aws.amazon.com/q/developer/](https://aws.amazon.com/q/developer/)  
21. Amazon Q \- Visual Studio Marketplace, 8月 29, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode)  
22. Getting Started with Amazon Q Developer, 8月 29, 2025にアクセス、 [https://aws.amazon.com/q/developer/getting-started/](https://aws.amazon.com/q/developer/getting-started/)  
23. AI for Software Development – Amazon Q Developer FAQs – AWS, 8月 29, 2025にアクセス、 [https://aws.amazon.com/q/developer/faqs/](https://aws.amazon.com/q/developer/faqs/)  
24. 14 Best GitHub Copilot Alternatives to try in 2025 (free and paid), 8月 29, 2025にアクセス、 [https://www.copilot.live/blog/github-copilot-alternative](https://www.copilot.live/blog/github-copilot-alternative)  
25. 【Codeium】VS Codeで使える！完全無料のAIコード補完を徹底紹介 \- 有限会社Bit Beans, 8月 29, 2025にアクセス、 [https://bitbeans.com/blog/codeiumai/](https://bitbeans.com/blog/codeiumai/)  
26. Windsurf Pricing Explained: Plans, Use Cases & Comparisons UI Bakery Blog, 8月 29, 2025にアクセス、 [https://uibakery.io/blog/windsurf-pricing](https://uibakery.io/blog/windsurf-pricing)  
27. Plans and Credit Usage \- Windsurf Docs, 8月 29, 2025にアクセス、 [https://docs.windsurf.com/windsurf/accounts/usage](https://docs.windsurf.com/windsurf/accounts/usage)  
28. IDE Free Tier War: Windsurf's Push to Win Over Developers AI Native Dev, 8月 29, 2025にアクセス、 [https://ainativedev.io/news/ide-free-tier-war-windsurf](https://ainativedev.io/news/ide-free-tier-war-windsurf)  
29. Windsurf Pricing 2025: Compare Plans and Costs \- TrustRadius, 8月 29, 2025にアクセス、 [https://www.trustradius.com/products/windsurf/pricing](https://www.trustradius.com/products/windsurf/pricing)  
30. WindSurf AI IDE Reviews \- Read Customer Reviews of Codeium.comwindsurf, 8月 29, 2025にアクセス、 [https://windsurf-ai-ide.tenereteam.com/](https://windsurf-ai-ide.tenereteam.com/)  
31. 生成AI対応のコードエディタ5選｜無料で使えるおすすめAIツールまとめ【2025年最新版】, 8月 29, 2025にアクセス、 [https://o-mochiblog.com/ai-code-editors-free/](https://o-mochiblog.com/ai-code-editors-free/)  
32. Exploring Windsurf's Support for Multiple Programming Languages \- Arsturn, 8月 29, 2025にアクセス、 [https://www.arsturn.com/blog/exploring-windsurfs-support-for-multiple-programming-languages](https://www.arsturn.com/blog/exploring-windsurfs-support-for-multiple-programming-languages)  
33. Windsurf Plugin (formerly Codeium): AI Coding Autocomplete and Chat for Python, JavaScript, TypeScript, and more \- Visual Studio Marketplace, 8月 29, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=Codeium.codeium](https://marketplace.visualstudio.com/items?itemName=Codeium.codeium)  
34. Windsurf Plugin (formerly Codeium) for Python, JS, Java, Go... \- JetBrains Marketplace, 8月 29, 2025にアクセス、 [https://plugins.jetbrains.com/plugin/20540-windsurf-plugin-formerly-codeium-for-python-js-java-go--](https://plugins.jetbrains.com/plugin/20540-windsurf-plugin-formerly-codeium-for-python-js-java-go--)  
35. 【2025】無料で使えるコード生成AIおすすめ12選！選び方や注意点, 8月 29, 2025にアクセス、 [https://ai-kenkyujo.com/news/code-seiseiai/](https://ai-kenkyujo.com/news/code-seiseiai/)  
36. Copilot, Tabnine, or self-hosted TabbyML \- what is better for you? \- Viblo, 8月 29, 2025にアクセス、 [https://viblo.asia/p/copilot-tabnine-or-self-hosted-tabbyml-what-is-better-for-you-Ny0VGRQYLPA](https://viblo.asia/p/copilot-tabnine-or-self-hosted-tabbyml-what-is-better-for-you-Ny0VGRQYLPA)  
37. Pricing Cursor \- The AI Code Editor, 8月 29, 2025にアクセス、 [https://cursor.com/pricing](https://cursor.com/pricing)  
38. Cursor AI Pricing Explained: Which Plan is Right for You? UI Bakery Blog, 8月 29, 2025にアクセス、 [https://uibakery.io/blog/cursor-ai-pricing-explained](https://uibakery.io/blog/cursor-ai-pricing-explained)  
39. Does free plan has limits : r/cursor \- Reddit, 8月 29, 2025にアクセス、 [https://www.reddit.com/r/cursor/comments/1j55oyt/does\_free\_plan\_has\_limits/](https://www.reddit.com/r/cursor/comments/1j55oyt/does_free_plan_has_limits/)  
40. Cursor's Pricing Disaster: How a "Routine Update" Turned Into a Developer Exodus, 8月 29, 2025にアクセス、 [https://www.wearefounders.uk/cursors-pricing-disaster-how-a-routine-update-turned-into-a-developer-exodus/](https://www.wearefounders.uk/cursors-pricing-disaster-how-a-routine-update-turned-into-a-developer-exodus/)  
41. Updates to Ultra and Pro Cursor \- The AI Code Editor, 8月 29, 2025にアクセス、 [https://cursor.com/blog/new-tier](https://cursor.com/blog/new-tier)  
42. How many premium requests does Cursor Pro actually get you now? : r/ChatGPTCoding \- Reddit, 8月 29, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTCoding/comments/1lvrqms/how\_many\_premium\_requests\_does\_cursor\_pro/](https://www.reddit.com/r/ChatGPTCoding/comments/1lvrqms/how_many_premium_requests_does_cursor_pro/)  
43. Cursor: pay more, get less, and don't ask how it works : r/programming \- Reddit, 8月 29, 2025にアクセス、 [https://www.reddit.com/r/programming/comments/1lu8eyb/cursor\_pay\_more\_get\_less\_and\_dont\_ask\_how\_it\_works/](https://www.reddit.com/r/programming/comments/1lu8eyb/cursor_pay_more_get_less_and_dont_ask_how_it_works/)  
44. Amazon Kiro Is Here to Tame the Vibe Coding Chaos \- PCMag, 8月 29, 2025にアクセス、 [https://www.pcmag.com/news/amazon-kiro-is-here-to-tame-the-vibe-coding-chaos](https://www.pcmag.com/news/amazon-kiro-is-here-to-tame-the-vibe-coding-chaos)  
45. Introducing Kiro \- Kiro.dev, 8月 29, 2025にアクセス、 [https://kiro.dev/blog/introducing-kiro/](https://kiro.dev/blog/introducing-kiro/)  
46. Kiro and the future of AI spec-driven software development, 8月 29, 2025にアクセス、 [https://kiro.dev/blog/kiro-and-the-future-of-software-development/](https://kiro.dev/blog/kiro-and-the-future-of-software-development/)  
47. Kiro AI: A Guide With Practical Examples \- DataCamp, 8月 29, 2025にアクセス、 [https://www.datacamp.com/tutorial/kiro-ai](https://www.datacamp.com/tutorial/kiro-ai)  
48. Amazon targets vibe-coding chaos with new 'Kiro' AI software development tool \- GeekWire, 8月 29, 2025にアクセス、 [https://www.geekwire.com/2025/amazon-targets-vibe-coding-chaos-with-new-kiro-ai-software-development-tool/](https://www.geekwire.com/2025/amazon-targets-vibe-coding-chaos-with-new-kiro-ai-software-development-tool/)  
49. Vibe vs Spec sessions \- Docs \- Kiro, 8月 29, 2025にアクセス、 [https://kiro.dev/docs/chat/vibe/](https://kiro.dev/docs/chat/vibe/)  
50. Understanding Kiro's Pricing: Specs, Vibes, and Usage Tracking \- Kiro, 8月 29, 2025にアクセス、 [https://kiro.dev/blog/understanding-kiro-pricing-specs-vibes-usage-tracking/](https://kiro.dev/blog/understanding-kiro-pricing-specs-vibes-usage-tracking/)  
51. Pricing \- Kiro, 8月 29, 2025にアクセス、 [https://kiro.dev/pricing/](https://kiro.dev/pricing/)  
52. Bito AI Code Reviews \- Visual Studio Marketplace, 8月 29, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=Bito.Bito](https://marketplace.visualstudio.com/items?itemName=Bito.Bito)  
53. The best AI-powered dev tools $15 can buy \- Bito, 8月 29, 2025にアクセス、 [https://bito.ai/blog/the-best-ai-powered-dev-tools-15-can-buy/](https://bito.ai/blog/the-best-ai-powered-dev-tools-15-can-buy/)  
54. Overview Bito Docs, 8月 29, 2025にアクセス、 [https://docs.bito.ai/help/billing-and-plans/overview](https://docs.bito.ai/help/billing-and-plans/overview)  
55. Bito AI Features, Pricing, and Alternatives \- AI Tools, 8月 29, 2025にアクセス、 [https://aitools.inc/tools/bito-ai](https://aitools.inc/tools/bito-ai)  
56. Overview Bito Docs, 8月 29, 2025にアクセス、 [https://docs.bito.ai/other-bito-ai-tools/ide-extension/ai-code-completions/overview](https://docs.bito.ai/other-bito-ai-tools/ide-extension/ai-code-completions/overview)  
57. Pricing: Free, Team & Enterprise Plans for AI Code Reviews Bito, 8月 29, 2025にアクセス、 [https://bito.ai/pricing/](https://bito.ai/pricing/)  
58. Tabby: Self-hosted AI Coding Assistant — SkyPilot documentation, 8月 29, 2025にアクセス、 [https://docs.skypilot.co/en/v0.9.3/examples/applications/tabby.html](https://docs.skypilot.co/en/v0.9.3/examples/applications/tabby.html)  
59. Tabby \- Opensource, self-hosted AI coding assistant, 8月 29, 2025にアクセス、 [https://www.tabbyml.com/](https://www.tabbyml.com/)  
60. Tabby: FREE Self-hosted AI coding Assistant\! Develop Apps, Debug, Code Completion, etc\!, 8月 29, 2025にアクセス、 [https://www.youtube.com/watch?v=8lc5jGwIqRo](https://www.youtube.com/watch?v=8lc5jGwIqRo)  
61. Tabby \- AI Agent for Code Completion, 8月 29, 2025にアクセス、 [https://bestaiagents.ai/agent/tabby](https://bestaiagents.ai/agent/tabby)  
62. What's Tabby, 8月 29, 2025にアクセス、 [https://tabby.tabbyml.com/docs/welcome/](https://tabby.tabbyml.com/docs/welcome/)  
63. Tabbyml tutorial: a practical guide for developers and SMBs \- BytePlus, 8月 29, 2025にアクセス、 [https://www.byteplus.com/en/topic/555335](https://www.byteplus.com/en/topic/555335)  
64. www.byteplus.com, 8月 29, 2025にアクセス、 [https://www.byteplus.com/en/topic/555334\#:\~:text=Prerequisites%20for%20a%20successful%20tabbyml%20installation,-To%20avoid%20common\&text=Python%20version%3A%20Python%203.8%20or,optional%20but%20recommended%20for%20performance.](https://www.byteplus.com/en/topic/555334#:~:text=Prerequisites%20for%20a%20successful%20tabbyml%20installation,-To%20avoid%20common&text=Python%20version%3A%20Python%203.8%20or,optional%20but%20recommended%20for%20performance.)  
65. ⁉️ Frequently Asked Questions Tabby, 8月 29, 2025にアクセス、 [https://tabby.tabbyml.com/docs/faq/](https://tabby.tabbyml.com/docs/faq/)  
66. How to install TabbyML on Mac \- Cedric Ferry \- Medium, 8月 29, 2025にアクセス、 [https://sonique6784.medium.com/how-to-install-tabbyml-on-mac-b0479613941c](https://sonique6784.medium.com/how-to-install-tabbyml-on-mac-b0479613941c)  
67. Tabby VSCode Extension \- Visual Studio Marketplace, 8月 29, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=TabbyML.vscode-tabby](https://marketplace.visualstudio.com/items?itemName=TabbyML.vscode-tabby)  
68. Tabby \- IntelliJ IDEs Plugin \- JetBrains Marketplace, 8月 29, 2025にアクセス、 [https://plugins.jetbrains.com/plugin/22379-tabby](https://plugins.jetbrains.com/plugin/22379-tabby)  
69. Programming Languages Tabby, 8月 29, 2025にアクセス、 [https://tabby.tabbyml.com/docs/references/programming-languages/](https://tabby.tabbyml.com/docs/references/programming-languages/)  
70. Changes to Cody Free, Pro, and Enterprise Starter plans \- Sourcegraph, 8月 29, 2025にアクセス、 [https://sourcegraph.com/changelog/cody-plan-changes](https://sourcegraph.com/changelog/cody-plan-changes)  
71. Changes to Cody Free, Pro, and Enterprise Starter plans Sourcegraph Blog, 8月 29, 2025にアクセス、 [https://sourcegraph.com/blog/changes-to-cody-free-pro-and-enterprise-starter-plans](https://sourcegraph.com/blog/changes-to-cody-free-pro-and-enterprise-starter-plans)  
72. Amp \- an AI coding agent built by Sourcegraph, 8月 29, 2025にアクセス、 [https://sourcegraph.com/amp](https://sourcegraph.com/amp)  
73. Cody gives 1 month for $10, but AMP burns $10 in just one day — why the huge difference? : r/sourcegraph \- Reddit, 8月 29, 2025にアクセス、 [https://www.reddit.com/r/sourcegraph/comments/1m74wy7/cody\_gives\_1\_month\_for\_10\_but\_amp\_burns\_10\_in/](https://www.reddit.com/r/sourcegraph/comments/1m74wy7/cody_gives_1_month_for_10_but_amp_burns_10_in/)  
74. Scaling Enterprise AI: Why we're sunsetting Tabnine Basic, 8月 29, 2025にアクセス、 [https://www.tabnine.com/blog/scaling-enterprise-ai-why-were-sunsetting-tabnine-basic/](https://www.tabnine.com/blog/scaling-enterprise-ai-why-were-sunsetting-tabnine-basic/)  
75. Basic Tabnine Docs, 8月 29, 2025にアクセス、 [https://docs.tabnine.com/main/welcome/readme/tabnine-subscription-plans/basic](https://docs.tabnine.com/main/welcome/readme/tabnine-subscription-plans/basic)  
76. Tabnine \- Features, Pricing, Pros & Cons (August 2025\) \- Siteefy, 8月 29, 2025にアクセス、 [https://siteefy.com/ai-tools/tabnine/](https://siteefy.com/ai-tools/tabnine/)  
77. Plans & Pricing Tabnine: The AI code assistant that you control, 8月 29, 2025にアクセス、 [https://www.tabnine.com/pricing/](https://www.tabnine.com/pricing/)  
78. Exploring the Unique Features That Make Kiro Different from Other AI IDEs \- Momen, 8月 29, 2025にアクセス、 [https://momen.app/blogs/difference-between-kiro-and-other-ai-ides-features-comparison/](https://momen.app/blogs/difference-between-kiro-and-other-ai-ides-features-comparison/)
