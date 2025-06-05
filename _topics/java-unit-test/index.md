---
layout: topic
title: "Javaユニットテスト自動化のための無料ツール調査：AI活用とAzure連携の可能性"
date: 2025-06-05
prompt: "Javaのユニットテストを自動で作成したい。前提条件として無料で使用できる必要がある。生成AIを使用する場合はAzureと接続できるものとする。"
category: "ai"
tags: [ユニットテスト]
audio: "/share-deepresearch/assets/audio/java-unit-test.mp3"
supplementary_materials:
  - title: "Javaユニットテスト自動化ツール インフォグラフィック"
    url: "/share-deepresearch/topics/java-unit-test/infographic.html"
---

# **Javaユニットテスト自動化のための無料ツール調査：AI活用とAzure連携の可能性**

## **I. はじめに：無料で効率的なJavaユニットテスト自動化の探求**

現代のソフトウェア開発において、迅速な高品質ソフトウェアの提供というプレッシャーは増す一方であり、Javaエコシステムにおけるユニットテストの重要性はますます高まっています 1。本レポートは、Javaのユニットテスト作成を自動化し、かつ無料で使用できるツールを求めるユーザーの具体的なニーズに応えるものです。さらに、生成AIツールを検討する場合には、Azureサービス（例：Azure OpenAI）との連携が可能であることが条件として挙げられています。

本レポートでは、これらの要件を満たす可能性のあるツールを特定し、その機能、ライセンス条件（特に無料版の商用利用）、IDEとの連携、モック作成能力（Mockitoなど）、そしてAIツールにおけるAzure連携の実現性について包括的に評価します。

ユーザーの「無料」という制約と、AIツールにおける「Azure AI連携」という二重の制約は、特にAIを活用したソリューションにおいて、選択肢を著しく狭める要因となります。多くのAIツールは商用であり、その無料版ではAzure OpenAIのような外部LLM（大規模言語モデル）との連携機能が提供されていなかったり、提供されていても有償版やエンタープライズ版に限定されていたりするケースが想定されます。このため、無料版のライセンス条項や機能セットを精査することが不可欠となります。この要求は、開発者が予算の制約内でAzure OpenAIのような強力なクラウドベースAIサービスの活用を模索し、多くの場合、まず無料ツールでその価値を検証しようとする近年の傾向を反映していると言えるでしょう。

## **II. 基礎知識：Javaユニットテスト自動化の理解**

ユニットテストとは、Javaの文脈においては、個々のメソッドやクラスといったソフトウェアの最小単位が正しく機能するかを検証するテストを指します。JUnit 1 やTestNG 2 といったフレームワークが広く利用されていますが、本レポートの焦点はこれらのテストを自動で「生成」するツールにあります。

テスト自動生成ツールの導入は、開発プロセスに多くの利点をもたらします。まず、反復的なテストケース作成にかかる手作業と時間を大幅に削減できます 1。次に、テストカバレッジを向上させ、人間が見逃しがちなエッジケースを発見する可能性があります 7。これにより、開発ライフサイクルの早期段階でバグを検出し、修正コストを低減できます 6。さらに、テスト駆動開発（TDD）やビヘイビア駆動開発（BDD）といった開発手法の実践を支援し 2、長期的にはコードの品質と保守性の向上に貢献します。手動でのユニットテスト作成は、その単調さ、時間的制約、網羅的なカバレッジ確保の難しさから、開発者が自動化を求める主な理由となっています。

テスト生成ツールを求める根本的な目的は、ソフトウェアの品質向上と開発速度の加速にあると考えられます。したがって、いかなる生成ツールの有効性も、単に生成されるテストの量だけでなく、それらのテストがこれらの目標達成にどれだけ貢献するかによって最終的に判断されるべきです。カバレッジが高いとしても、品質が低い、あるいは保守が困難なテストが大量に生成されるのでは問題があります 12。つまり、自動化ツールの「価値」は、生成速度や量だけでなく、生成されたテストが実際のバグ発見に役立ち、かつ保守が容易であるかという質的側面にも左右されるのです。また、JUnit 5やTestNGといったユニットテスト「フレームワーク」の選択は、テスト生成ツールがどの程度スムーズに連携できるか、あるいはどの機能を活用できるかに影響を与える可能性があります。ツールによっては、特定のフレームワークのバージョンや機能に最適化されている場合もあります（例：EvoSuiteのJUnit 5出力対応 14）。

## **III. 無料Javaユニットテスト生成ツールの概観**

利用可能な無料ツールは、伝統的なアプローチ（多くは探索ベースや記号的実行に基づく）とAIを活用したアプローチに大別できます。

**A. 伝統的なテスト生成ツール（主に無料かつオープンソース）**

* **EvoSuite:** Javaクラスに対してアサーション付きのテストケースを自動生成するツールとして知られ、多くの場合、探索ベースの手法を用いています 7。オープンソースであり、LGPLライセンスで提供されています 17。  
* **Randoop:** フィードバック指向のランダムテスト生成技術を用いてJavaクラス用のJUnitテストを生成するツールです 7。こちらもオープンソースで、MITライセンスの下で公開されています 20。

**B. AIを活用したテスト生成ツール（無料版に焦点）**

* **Diffblue Cover Community Edition:** AI（特に強化学習 10）を利用してJavaのユニットテストを生成する無料のIntelliJプラグインです 8。  
* **JetBrains AI Assistant (無料版):** JetBrains IDEに統合されたAIコーディングアシスタントで、ユニットテスト生成機能を提供します 24。Azure OpenAIとの連携可能性（有償版において）も注目されます 27。  
* **Windsurf (旧Codeium) (無料版):** Eclipse 28 やIntelliJ 28 を含むIDEプラグインを提供するAIコーディング支援ツールで、ユニットテストにも応用可能なコード生成機能を持ちます 28。最近OpenAIに買収されたことが報じられています 31。

「無料」のツール群は多様性に富んでおり、学術研究から生まれた完全なFOSS（Free and Open Source Software）ツール（EvoSuite, Randoop）から、高度な商用AI製品の無料版まで様々です。これは、サポートモデル、無料版で提供される機能の豊富さ、そしてライセンスの複雑さがツールによって異なることを意味します。EvoSuiteやRandoopは学術・研究機関発のFOSSであり 17、通常、コミュニティサポートが中心で、全機能が利用可能、ライセンスも比較的寛容です。一方、Diffblue Cover Community Edition、JetBrains AI Assistant無料版、Windsurf無料版は商用製品への入り口として位置づけられています 8。商用製品の無料版は、有償版へのアップグレードを促すために、利用制限（クォータ、機能制限など）が設けられていることが一般的です 34。したがって、「無料」といってもその内容は一様ではありません。ユーザーは、商用無料版の洗練されたUI/UXや最先端AIの利点と、FOSSツールの完全性やオープン性を比較検討する必要があります。

AIを活用したツールの台頭は、純粋にアルゴリズム的なテスト生成から、LLMやその他の機械学習技術を活用する方向へのシフトを示唆しています。これにより、より「インテリジェント」あるいは「人間らしい」テスト作成が期待される一方で、モデルの選択、プロンプトエンジニアリング、データプライバシーといった新たな複雑性も生じています 25。

## **IV. 有望な無料ツールの詳細分析**

前述の各ツールについて、機能、ライセンス、IDE連携、Mockitoサポート、テスト品質、AIアプローチ、Azure連携の観点から詳細に分析します。

**1\. EvoSuite**

* **概要と主要なユニットテスト生成機能:**  
  * Javaクラス向けのJUnitテストスイートを自動生成します 15。  
  * 遺伝的アルゴリズムなどの探索ベースソフトウェアテスト（SBST）技術を用い、カバレッジ基準を満たすようにテストスイートを最適化します 12。デフォルトアルゴリズムは現在DynaMOSAです 14。  
  * 現在の振る舞いを捉えるためのアサーションを生成します 15。  
  * テストはサンドボックス環境で実行されます 15。  
* **ライセンス：無料版詳細と商用利用に関する考慮事項:**  
  * オープンソースであり、LGPL（GNU Lesser General Public License）でライセンスされています 17。これは一般的に商用利用を許可しますが、EvoSuiteを改変したり配布したりする場合にはLGPLの義務を理解する必要があります。なお、37 はEvoSuiteテスト生成ツールとは異なる「EVO Suite」製品に関するものであり、関連性は低いと考えられます。  
* **IDE連携 (IntelliJ, Eclipseなど):**  
  * IntelliJプラグインが利用可能です 7。  
  * Eclipseプラグインも利用可能です 38。  
  * Mavenとの連携が可能です 14。  
  * コマンドラインからの実行もサポートされています 7。  
* **Mockito連携とモック機能:**  
  * バージョン1.0.6で「モック基盤／Mockito連携」の改善が言及されています 14。公式ドキュメントにはより詳細な情報が含まれている可能性があります（38 \- 一部アクセス不可でした）。  
* **報告されているテスト品質、保守性、ユーザビリティ:**  
  * 高いカバレッジを目指しています 12。  
  * 一部の研究では、EvoSuiteのような探索ベースのツールは、理解や保守が難しいテストを生成する可能性があると指摘されています 12。  
  * いくつかの研究ではバランスの取れた性能を示しています 16。  
* **生成AIアプローチ:** 主にLLMベースの生成AIツールではなく、探索アルゴリズムとヒューリスティクスを使用します。  
* **Azure連携:** LLMベースのAIツールではないため、該当しません。43 および 44 はメディアストレージとAzureを含むクラウド連携に関する別の「EVO Suite」製品について言及しており、これはJavaテスト生成用のEvoSuiteではありません。

**2\. Randoop**

* **概要と主要なユニットテスト生成機能:**  
  * Javaクラス向けのユニットテストをJUnit形式で自動作成します 18。  
  * フィードバック指向のランダムテスト生成を使用します。これは、テスト対象クラスのメソッド／コンストラクタ呼び出しシーケンスを疑似ランダムかつスマートに生成し、実行結果を用いてプログラムの振る舞いを捉えるアサーションを作成する技術です 19。  
  * バグ発見やリグレッションテスト作成に利用できます 19。  
* **ライセンス：無料版詳細と商用利用に関する考慮事項:**  
  * オープンソースであり、MITライセンスの下で提供されています 18。MITライセンスは寛容であり、主に帰属表示を条件として商用利用を一般的に許可します。  
* **IDE連携 (IntelliJ, Eclipseなど):**  
  * 主にコマンドラインツールです 7。IDE連携は通常、Gradle/Mavenのようなビルドツールやカスタムシェルスクリプト実行を介して行われます。  
  * Gradleでビルドされます 45。  
* **Mockito連携とモック機能:**  
  * RandoopのマニュアルにはMockito連携に関する明示的な言及はありません 19。  
  * しかし、Randoopにはreplacecallエージェントがあり、テスト対象コードを変換して望ましくないメソッド呼び出しを他の（モック）メソッド呼び出しに置き換えることができます 47。これはモックメカニズムを提供しますが、直接的なMockito連携ではありません。  
* **報告されているテスト品質、保守性、ユーザビリティ:**  
  * 広く使われているライブラリでもエラーを発見するのに効果的です 19。  
  * 他の自動化ツールと同様に、生成されたテストは時に読みにくかったり非現実的だったりするため、開発者による検証が必要になる場合があります 13。  
  * いくつかの研究では、個々の障害は特定するものの、他の特化した戦略ほど障害ドメインを検出できない可能性が示唆されています 49。  
* **生成AIアプローチ:** LLMベースの生成AIツールではなく、フィードバック指向のランダム生成を使用します。  
* **Azure連携:** 該当しません。45 はRandoop自体のCIテストのためのAzure Pipelinesについて言及しており、RandoopがAzure AIサービスを使用することについてではありません。50 はRandoopが.NET CLRチーム（Microsoft Azureの文脈）で使用されたことに言及していますが、これは利用実績であり、テスト生成のためのAzure AI連携ではありません。

**3\. Diffblue Cover Community Edition**

* **概要と主要なユニットテスト生成機能:**  
  * Javaのユニットリグレッションテストを自動作成します 23。  
  * AI（10 によると主にLLMではなく強化学習）を利用して、既存のコードベースのロジックを尊重したテストを合成します 8。  
  * コードカバレッジを迅速に向上させることを目指しています 8。  
  * 既存のテストを分析し、改善を提案することも可能です 23。  
* **ライセンス：無料版詳細と商用利用に関する考慮事項:**  
  * 無料のIntelliJプラグインです 8。  
  * Community Editionの永続ライセンスを有効化するには製品認証が必要です 51。  
  * オープンソースまたは商用のJavaコード向けに設計されています 8。無料CEの「永続ライセンス」という言葉は好意的ですが、「製品認証」と「リモートライセンスチェック」51 はオンライン接続が必要であることを示唆しています。CEの商用利用は許可されているようです。  
* **IDE連携 (IntelliJ, Eclipseなど):**  
  * IntelliJ IDEAプラグイン 8。  
  * CLIツールとしても利用可能です 53。  
* **Mockito連携とモック機能:**  
  * テスト対象コードを分離するためにMockitoを活用します（9 \- Jtestの文脈ですが、Diffblueが意味のあるテストに焦点を当てていることを考えると関連性があります。11 はDiffblueとMockitoを明示的に言及しています）。  
  * 公式ドキュメントに詳細が含まれている可能性があります（55 \- 一部アクセス不可でした）。  
* **報告されているテスト品質、保守性、ユーザビリティ:**  
  * 読みやすく、自動的に保守されるテストを目指しています 8。  
  * 人間が見逃す可能性のあるエッジケースを捉えることができます 8。  
  * 開発者はAIが生成したテストを理解し、洗練させるのに時間を費やす必要があるかもしれません 23。  
* **生成AIアプローチ:** コア技術は強化学習です 10。「AI for Code」ですが、LLMベースの生成とは異なります。  
* **Azure連携:**  
  * 提供された情報からは、Community EditionにおけるAzure OpenAI連携に関する直接的な言及は見つかりませんでした。  
  * Diffblue社は独自のAIに注力しています 10。有償のエンタープライズソリューションではより広範な連携が提供される可能性がありますが、無料のCEはそのAIにおいて自己完結しているようです。57（Azure OpenAIモデル）と10（Diffblue AI）は別々の文脈です。

**4\. JetBrains AI Assistant (無料版)**

* **概要と主要なユニットテスト生成機能:**  
  * JetBrains IDEに統合されたAIコーディング支援機能です 25。  
  * ユニットテストを生成できます 24。  
  * メソッドやクラスに対するテスト生成をプロンプトで指示できます 24。  
  * LLM（JetBrains独自のMellum、およびOpenAI、Google、Anthropicなど他社製）を活用します 25。  
* **ライセンス：無料版詳細と商用利用に関する考慮事項:**  
  * IDEライセンスに含まれる「AI Free」版があります 26。これには無料のIDE版（Community Editionなど）も含まれますが、35 はAI FreeがPyCharm/IntelliJ IDEAのCommunity Editionでは利用**できない**と指摘しており、これは「完全に無料」という要件にとって極めて重要な制限です。  
  * WebStormとRiderは現在、非商用利用であれば無料であり、これにはAI機能も含まれます 62。「Toolbox Subscription Agreement for Non-Commercial Use」62 が商用利用を定義しています。コンテンツ作成は一般的に非商用とされています。  
  * AI Free版は、無制限のコード補完（ローカルモデル）と、クレジットベースのクラウドAI利用（コーディングエージェントJunieを含む）を提供します 26。  
  * 「AI Free」版の商用利用については、それがバンドルされている特定のIDEライセンスとJetBrains AI Serviceの規約を慎重に確認する必要があります（65）。61 は「AI機能は、教育用および非商用ライセンスを含む、アクティブなJetBrains IDEライセンスに無料で含まれています」と述べています。ベースとなるIDEが商用利用ライセンス（例：IntelliJ IDEA Ultimate有償版）であれば、AI Free版の特典はその範囲に及びます。ベースIDEが無料のCommunity Editionの場合、35 はAI Freeが利用できないとしています。これはユーザーの「無料」という要件にとって重要な点です。  
* **IDE連携 (IntelliJ, Eclipseなど):**  
  * JetBrains IDE（IntelliJ IDEAなど）に深く統合されています 25。  
  * Eclipseには該当しません。  
* **Mockito連携とモック機能:**  
  * LLMベースのアシスタントとして、適切にプロンプトを与えたり、分析対象のプロジェクトコンテキストにMockitoが存在したりすれば、Mockitoを使用するコードを生成できる可能性があります（25 はコンテキスト認識を示唆しています）。  
  * 70 および 71 はLLMとMockito/テスト生成に関する一般的な文脈を提供しますが、JetBrains AI AssistantとMockitoを用いた具体的な例ではありません。  
* **報告されているテスト品質、保守性、ユーザビリティ:**  
  * スマートでコンテキストを意識した提案を目指しています 25。  
  * LLMが生成したテストは自然で理解しやすい場合がありますが、洗練が必要な場合もあります 72。品質はLLMとプロンプトに依存します。  
* **生成AIアプローチ:** LLM（JetBrains Mellum、OpenAI、Google、Anthropic）を使用します 25。  
* **Azure連携:**  
  * **重要な点として、JetBrains AI Enterprise（IDE Servicesの一部である有償製品）は、ユーザー自身のAzure OpenAIサブスクリプションをプロバイダーとして設定できます** 27。  
  * **提供された情報では、JetBrains AI Assistantの「無料版」がユーザー自身のAzure OpenAIサブスクリプションに直接接続できるとは明示されていません。** 無料版はJetBrains AIサービスを使用し、それが様々なLLMに接続します 27。その中にはOpenAIモデルも含まれますが、それはJetBrainsのサービス経由であり、無料版のための直接的なユーザーAzure OpenAIエンドポイントではありません。これはユーザーの質問にとって重要な区別です。

**5\. Windsurf (旧Codeium) (無料版)**

* **概要と主要なユニットテスト生成機能:**  
  * コード補完、チャット、そしてプロンプトによるユニットテスト生成の可能性を含むAIコーディングアシスタントです 28。  
  * 複雑なタスクのための「Cascade」機能があります 29。  
  * 70以上の言語をサポートしています 30。  
* **ライセンス：無料版詳細と商用利用に関する考慮事項:**  
  * 特定の制限（例：プロンプトクレジット）付きの「無料」個人プランを提供しています 30。  
  * 28 は、Windsurf（Codeium時代）のEclipseプラグインについて「永久無料、商用利用可能」と述べています。  
  * Individual & Pro向けの利用規約 75 およびマーケットプレイスのEULA 76 は、現在の無料版の商用利用に関する詳細について慎重な確認が必要です。（77 はこれらの規約を取得しようとした試みです。）  
* **IDE連携 (IntelliJ, Eclipseなど):**  
  * IntelliJ、VS Code、Eclipseを含む多くのIDE向けのプラグインがあります 28。  
* **Mockito連携とモック機能:**  
  * LLMベースのツールとして、Mockitoが使用されているJavaプロジェクトのコンテキスト内でプロンプトを与えれば、Mockitoコードを生成できる可能性があります。特定のMockito連携機能は情報源では強調されていません 73。  
* **報告されているテスト品質、保守性、ユーザビリティ:**  
  * インテリジェントな自動補完とコンテキストを意識した提案を目指しています 30。  
  * 無料版は大規模なコードベースのインデックス作成が制限されたり、時折無関係な提案をしたりする可能性があります 30。  
* **生成AIアプローチ:** LLMを使用します。Windsurfは独自のLLMを持ち、他も使用できるとされていましたが（33 は中立性が特徴であったことを示唆）、OpenAIによる買収がこれを変更する可能性があります 31。  
* **Azure連携:**  
  * OpenAIによる買収後 31、LLMの中立性やAzure OpenAIのような特定の連携に関する将来のロードマップは不透明です。  
  * 情報源には、現在の「無料版」がユーザーのAzure OpenAIサブスクリプションに直接接続するという明示的な言及はありません。33 はWindsurfが広範なLLMサポートを「継続」するかどうかを議論しています。82（Windsurf Codeium "Azure OpenAI" "roadmap"）は具体的な結果をもたらしませんでした。

これらの分析から、「無料」の定義が大きく異なることが明らかになります。FOSSツール（EvoSuite, Randoop）はコストとライセンスの観点からは真に無料です（LGPL/MITは商用利用を許可）。一方、商用AIツールの「無料版」（Diffblue CE, JetBrains AI Assistant, Windsurf）には、利用制限、機能制限、オンライン認証、商用利用やデータプライバシーに関するより複雑なライセンスといった条件が付随する場合があります。

最先端のAI機能（多くは商用ツール、その無料版でさえ見られる）と、伝統的なFOSSツールの真のオープン性／制約のないアクセスとの間には緊張関係が存在します。新しいAIツールは、より「ガイドされた」あるいは「インテリジェントな」体験を提供することが多いですが、透明性が低かったり、より制限的であったりする可能性があります。

ユーザーの選択は、トレードオフを伴うことになるでしょう。

* **FOSSツール:** 完全な制御、隠れたコストなし、コミュニティサポート。しかし、学習曲線が急であったり、UXが洗練されていなかったり、テスト品質が手動レビューをより多く必要とする可能性があります 12。  
* **AIツール無料版:** より高度な生成、優れたIDE連携（JetBrains/Diffblueの場合）。しかし、利用上限、オンライン依存、商用シナリオにおけるより複雑なライセンスが伴います。「無料版」でのAzure OpenAI連携は、ほとんどのツールにとって大きな疑問符が残ります。

## **V. 無料Javaユニットテスト自動化ツールの比較概要**

セクションIVでの詳細な分析結果を基に、ユーザーの要求に最も関連性の高い側面に着目して各ツールを直接比較します。真に無料で、質の高いJavaユニットテストを生成し、かつ（AIベースの場合）その無料版でAzure OpenAIに接続できるツールを見つけることの難しさを改めて強調します。

**無料Javaユニットテスト生成ツールの比較**

| 特徴 | EvoSuite | Randoop | Diffblue Cover Community Edition | JetBrains AI Assistant (無料版) | Windsurf (旧Codeium) (無料版) |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **主要生成手法** | 探索ベース (SBST) | フィードバック指向ランダム生成 | 強化学習AI | LLMベースAI | LLMベースAI |
| **主要Javaユニットテスト機能** | JUnit/TestNGサポート、アサーション生成、カバレッジ重視 14 | JUnitサポート、アサーション生成、バグ発見重視 19 | JUnit/TestNGサポート、意味のあるリグレッションテスト生成、カバレッジ向上 8 | JUnit/TestNGサポート（LLMによる）、アサーション生成（LLMによる）、コンテキストに基づいたテスト生成 24 | プロンプトに応じたテストケースのスケルトン生成、多言語対応 29 |
| **無料版ライセンスと主な商用利用注意点** | LGPL 17 (商用利用可、LGPL義務に注意) | MITライセンス 20 (寛容な商用利用) | 無料IntelliJプラグイン、永続ライセンス（製品認証要）8。商用コードに利用可。 | IDEライセンスにAI Free版が付属 26。**IntelliJ/PyCharm Community EditionではAI Free利用不可** 35。無料WebStorm/Riderは非商用利用限定 62。クラウドAIはクレジット制 35。商用利用はベースIDEライセンスとJetBrains AI規約による。 | 無料個人プラン（プロンプトクレジット等制限あり）30。旧Eclipseプラグインは商用利用可と記載 28。現行規約の確認要。 |
| **IDEサポート** | IntelliJ, Eclipse, Maven, CLI 7 | CLI中心、Gradle/Maven連携 7 | IntelliJ IDEA 8, CLI 54 | JetBrains IDE (IntelliJ IDEAなど) 25 | IntelliJ, Eclipse, VS Codeなど多数 28 |
| **Mockito/モックサポート** | Mockito連携あり (v1.0.6以降) 14 | replacecallエージェントによる間接的モック 47 | Mockito活用 9 | LLMがコンテキストに応じてMockitoコードを生成可能 25 | LLMがコンテキストに応じてMockitoコードを生成可能 |
| **Azure OpenAI連携 (AIツール無料版)** | 該当なし | 該当なし | なし (Diffblue独自のAI) 10 | **間接的** (JetBrains AIサービス経由でOpenAIモデル利用、ユーザー自身のAzure OpenAIエンドポイント直接接続は不可) 27 | **不明** (OpenAI買収後のロードマップ、特に無料版でのAzure OpenAI連携は未確定) 33 |
| **主な長所** | 高いカバレッジ達成力、オープンソース | バグ発見能力、オープンソース | 高速なカバレッジ向上、読みやすいテスト生成の試み、IDE連携 8 | 強力なLLM機能、深いIDE連携、多様なLLM選択肢（JetBrains AIサービス経由）25 | 幅広いIDE/言語サポート、柔軟なAIチャット機能 28 |
| **主な短所/制限事項** | 生成テストの保守性に課題の可能性 12 | 生成テストの可読性/現実性に課題の可能性 13、CLI中心 | 強化学習ベースでありLLMではない、オンライン認証が必要 51 | **無料IDE(Community Edition)でのAI Free利用不可** 35。クラウドAIはクレジット制で制限あり 35。無料版での直接的なユーザーAzure OpenAI接続は不可。 | 無料版はクレジット制限あり 34。OpenAI買収による将来的なサービス内容変更の可能性。無料版での直接的なユーザーAzure OpenAI接続は不明。 |

この比較表からも明らかなように、すべての理想的な基準（最先端のLLM AI、あらゆる商用利用に対する完全な無料性、無料版での直接的なAzure OpenAI接続、完璧なテスト品質）を完全に満たす単一の無料ツールは存在しない可能性が高いです。ユーザーは優先順位を考慮して選択する必要があります。例えば、EvoSuiteやRandoopは完全に無料でオープンソースですが、LLMベースのAIではなく、ユーザビリティやテスト品質に懸念が残る場合があります 12。Diffblue Cover Community EditionはAIベース（非LLM）で無料ですが、CE版でのAzure OpenAI接続は提供されていません。JetBrains AI Assistant無料版は、Azure OpenAIへのアクセスが間接的（JetBrainsサービス経由）であり、その「無料性」はIDEライセンスに依存し、Community Editionでは利用が制限されています 35。Windsurf無料版にはクレジット制限があり、買収後のAzure OpenAI連携については無料版では不明確です。したがって、何らかの妥協が必要となるでしょう。

「最良」のツールは、利用状況や優先順位に大きく左右されます。オープンソースプロジェクトに取り組む個人開発者であれば、ライセンスの寛容さからRandoopを選択するかもしれません。一方、既にJetBrainsエコシステム内にいる開発者は、無料版の制限を念頭に置きつつAI Assistantを検討するかもしれません。

## **VI. 生成AIによるユニットテスト：Azureとの連携**

**JetBrains AI Assistant (Azure連携はエンタープライズ版の文脈で)**

JetBrains AI Assistantの無料版は、LLMへのアクセスにJetBrains独自のサービスレイヤーを使用しますが 27、**JetBrains AI Enterprise**ソリューション（IDE Servicesの一部であり有償製品）では、ユーザー自身のAzure OpenAIサブスクリプションとの連携設定が明示的に可能です 27。

JetBrains AI EnterpriseとAzure OpenAIの連携設定手順は、27 および 27 に詳述されている通り、Azureリソースの作成、GPT-3.5-TurboやGPT-4といったモデルのデプロイ、エンドポイント／APIキーの取得、そしてJetBrains IDE Servicesでの設定が含まれます。これは、たとえこの特定の連携が「無料」という制約に直接合致しなくても、そのような連携がどのように機能するかの実例となります。通常使用されるモデルにはGPT-3.5-Turbo、GPT-4、GPT-4oなどがあります 27。Azureに接続する場合、ツールのライセンスとは別に、Azure側での利用コストが発生することに注意が必要です（IDE Servicesの従量課金モデル 27）。Azure自体にも独自のクォータと制限が存在します 83。

**Parasoft Jtest (有償ツールの参考例)**

Parasoft Jtestは、OpenAI/Azure OpenAIと連携する商用Javaテストツールの一例として挙げられます 5。AI支援によるユニットテスト生成、LLMが生成したコード修正案の利用、カバレッジと信頼性向上のためのAI活用などが特徴です 5。**Jtestは有償ツールであること** 84 を明確にしておきますが、Javaテスト自動化の広範な市場において、このようなAzure OpenAI連携が存在することを示すことで、ユーザーが目指す方向性の文脈を提供します。

**AIテスト生成におけるAzure利用を示唆する研究**

学術研究においても、AI駆動型テスト生成にAzureが利用されている例があります。例えば、86 では、アクセプタンステストのためにAzure OpenAI経由でGPT-4 Turboを利用するAutoUATおよびTest Flowツールが紹介されています。これはユニットテストではありませんが、AIテスト研究におけるAzureの役割を示しています。87 (PromptPex) は、異なるモデル（Azure上でホストされている可能性のあるものを含む）に対してプロンプトをテストすることについて議論しています。

**「無料版でのAzure OpenAI連携」のギャップへの対応**

現時点の情報に基づけば、AIツールの**無料版**が、ユーザー自身のAzure OpenAIエンドポイントへの直接的かつユーザー設定可能な接続を提供しているケースは見当たりません。JetBrains AI Assistant無料版は、JetBrains AIサービスを介してOpenAIモデルを利用しますが、これはユーザー自身のAzureサブスクリプションへの直接接続ではありません。

ユーザーが「無料ツール \+ Azure OpenAI」を望む背景には、強力で、場合によってはカスタマイズされた、あるいは企業が承認したLLM（Azure OpenAI）を、テスト生成ツール自体の費用をかけずに活用したいという意図があると考えられます。しかし、その場合でもAzure OpenAIの運用コストは発生します。無料版の現在の市場は、この特定の直接連携モデルをサポートしていないようです。その理由は、AIツールベンダーのビジネスモデルに関連していると考えられます。無料版のAIツールは、ツールベンダーにとって低コストの導入手段として設計されています。ユーザーが管理する外部の、潜在的に高コストなサービス（Azure OpenAIなど）への接続を無料版で許可することは、ツールベンダーにとって、その特定機能からの直接的な収益がないまま複雑性とサポートのオーバーヘッドを増大させます。そのため、この機能は通常、顧客が既にプレミアムサービスに対して支払いを行っている有償版やエンタープライズ版（例：JetBrains AI Enterprise 27）のために確保されています。

開発者は、ツールが汎用的なOpenAIモデル（ベンダーによってAzureを含むどこかでホストされている可能性がある）を使用していることと、ツールがユーザー自身の特定のAzure OpenAIインスタンスへの接続を許可していることとを区別する必要があります。後者はより多くの制御を提供しますが、通常は有償機能です。

## **VII. 自動ユニットテスト生成導入のベストプラクティス**

**ワークフローへの統合**

これらのツールをCI/CDパイプラインに統合することを検討すべきです 6。生成されたテストを手動で記述されたテストと並行して定期的に実行することが重要です。

**生成されたテストのレビューと保守**

AIやアルゴリズムによって生成されたテストは完全ではなく、人間によるレビューと理解が必要です 12。生成されたテストをリファクタリングし、可読性と保守性を向上させる戦略が求められます。「人間参加型（human-in-the-loop）」のアプローチが極めて重要です（Junieの文脈での64）。

**自動テストと手動テストのバランス**

自動生成は、特に複雑なシナリオやビジネスロジックに対する思慮深い手動テスト設計を完全に置き換えるものではなく、あくまで補完的なものです。カバレッジが低い領域や、定型的なテストパターンが多い箇所に自動生成を集中させるとよいでしょう。

**ツール固有の設定の理解**

プロジェクトのニーズに合わせてテスト生成を調整するために、ツールの設定オプションを積極的に調査することが推奨されます（例：Randoopのreplacecall 47、Diffblueの設定 54）。

**量やカバレッジだけでなくテスト品質に注目**

生成されたテストによる高いカバレッジ数値が、必ずしも高品質なバグ検出に繋がるわけではありません。テストが些末であったり、脆弱であったりすればその限りではありません 12。ツールが提供する、あるいは測定可能なミューテーションスコアは、テストの有効性を示すより良い指標となり得ます 12。

これらのツールを効果的に導入するには、ツールの技術的能力と同じくらい、プロセスと心構えが重要です。レビューと統合の戦略なしに単にジェネレータを「オン」にするだけでは、煩雑で役に立たないテストスイートが生じる可能性が高いです。自動化ツールはテストを迅速に生成しますが 5、これらのテストは必ずしも完璧であったり理解しやすかったりするわけではありません 12。未レビュー／未管理の大量の低品質テストは保守の負担となり、この負担は自動化による初期の時間節約を相殺しかねません。したがって、生成されたテストをレビューし、リファクタリングし、統合するための規律あるアプローチが長期的な成功には不可欠です。生成されたテストの保守性 12 は、長期的なROIに直接影響します。生成に多少時間がかかったり、初期のカバレッジが若干低かったりしても、より人間が読みやすく堅牢なテストを生成するツールの方が、長期的には優れている可能性があります。

## **VIII. 推奨事項と戦略的考慮事項**

ユーザーの主要なニーズ（無料、Javaユニットテスト自動化、AIツールの場合はAzure連携）を再確認した上で、優先順位に基づいた推奨戦略を以下に示します。

**優先順位に基づく推奨戦略**

* **「完全無料かつオープンソース」が最優先（かつ、ツール自体への直接的なAzure AI連携が必須ではない場合）：**  
  * **EvoSuite (LGPL** 17**):** カバレッジ駆動型の生成に適しており、Mockitoをサポートし 14、IDEプラグインも提供されています。ただし、生成されたテストは保守性の観点からレビューが必要となる場合があります 12。  
  * **Randoop (MIT** 20**):** ランダム探索によるバグ発見に強力です。モックはエージェント経由であり、直接的なMockito連携ではありません 47。CLI中心の利用となります。  
* **「無料版のあるAI駆動型生成」を希望（かつ、Azure AI連携は間接的であるか有償アップグレードで対応可能と考える場合）：**  
  * **Diffblue Cover Community Edition:** 独自のAI（強化学習 10）を使用し、無料のIntelliJプラグインが提供され 8、カバレッジ向上に優れMockitoもサポートしています 11。CE版での直接的なAzure OpenAI連携はありません。「無料のAI Javaユニットテスト」としては有力な候補です。  
  * **JetBrains AI Assistant (無料版):** 強力なLLM機能を持ち、IDEとの連携も深いです 25。しかし、商用利用における「無料性」はIDEのライセンスに依存し、AI Free版はIntelliJ/PyCharmの無料Community Editionでは利用できません 35。無料版でのAzure OpenAI利用はJetBrainsのサービス経由であり、ユーザー自身のエンドポイントへの直接接続ではありません。ユーザーが有償のJetBrains IDEを所有しているか、無料の非商用Rider/WebStormの対象となる場合 62 は選択肢となりますが、無料版におけるAzure連携の制約は直接的には満たせません。  
  * **Windsurf (無料版):** クレジット制限付きの無料版を提供しています 34。IDEサポートは広範です 28。OpenAIによる買収後、そのLLM戦略や（特に無料版での）Azure OpenAI連携の可能性は不透明です 33。

**無料ツールにおけるAzure OpenAI連携の制約への対応**

AIツールの**無料版**で、ユーザー自身のAzure OpenAIサブスクリプションへの直接接続を許可するものは、現時点では特定できませんでした。

もしAIツール自体へのAzure OpenAI連携が譲れない要件である場合、ユーザーは以下を検討する必要があるでしょう。

* JetBrains AI Enterprise 27 やParasoft Jtest 5 のようなツールの有償版。  
* あるいは、EvoSuite/Randoopのような無料／オープンソースのテスト生成ツールを使用し、それとは別にカスタムスクリプトや他の手段を介してAzure OpenAIを利用し、テストのアイデアを提案させたり既存テストをリファクタリングさせたりする方法（生成ツール内での直接連携ではない）。

**最終的な戦略的考察**

ユーザーの要求は、オープンソースツール、商用AI-as-a-Service、クラウドプラットフォーム連携という、急速に進化する複数の領域の交差点に位置しています。今日、すべての基準を満たす「完璧な」無料ソリューションは存在しない可能性が高く、現実的なアプローチが求められます。「無料」であることへの要望は一般的です。同様に、「Azure OpenAI」のような強力なマネージドAIサービスを利用したいという要望も高まっています。しかし、「無料版」を提供するツールベンダーは収益化への道筋を必要としており、外部の有償サービス（Azure OpenAIなど）との直接連携のようなプレミアム機能は、多くの場合、有償顧客向けに確保されています。オープンソースツールは真に無料ですが、最新の商用AIサービスを直接連携させる点では遅れをとる可能性があります。したがって、ユーザーは戦略的な選択を迫られる可能性が高いです。つまり、「無料ツール」の側面を優先する（そしてそのツール内での直接的なAzure AI連携に関する制限を受け入れる）か、あるいは「Azure AI連携」を優先する（そしてツール自体が商用／有償になる可能性を受け入れる）かです。

LLMがよりコモディティ化し、APIが標準化されるにつれて、ユーザー提供のAzure OpenAIエンドポイントを含む様々なAIバックエンドとのより容易な連携ポイントを提供する無料／オープンソースツールが増えるかもしれません。しかし、現時点では、これは有償ツールでより一般的な機能です。OpenAIによるWindsurfの買収 33 も、その特定のツールの状況を変える可能性があります。

最終的には、主要な制約に最も合致するツールから開始し、コードベースの小規模な部分でパイロット運用を行い、生成されたテストの品質、保守性、実際の時間節約効果を評価し、必要に応じてツールを調整したり組み合わせたりする準備をしておくことが賢明です。

#### **引用文献**

1. 単体テストアシスタント | Java対応静的解析・単体テストツール Jtest | テクマトリックス株式会社, 6月 5, 2025にアクセス、 [https://www.techmatrix.co.jp/product/jtest/unittest/index.html](https://www.techmatrix.co.jp/product/jtest/unittest/index.html)  
2. 無料で使えるオープンソース自動テストツール12選 \- Zenn, 6月 5, 2025にアクセス、 [https://zenn.dev/takuya77088/articles/8fb51485730ebb](https://zenn.dev/takuya77088/articles/8fb51485730ebb)  
3. Top 8 Java Unit Testing Frameworks for 2025 \- Continuously Merging \- Mergify, 6月 5, 2025にアクセス、 [https://blog.mergify.com/java-unit-testing-frameworks/](https://blog.mergify.com/java-unit-testing-frameworks/)  
4. Java Testing Frameworks: Top 5 Options for Robust Application Development \- Netguru, 6月 5, 2025にアクセス、 [https://www.netguru.com/blog/java-testing-frameworks](https://www.netguru.com/blog/java-testing-frameworks)  
5. AI-Powered Java Unit Testing Solution Boosts Developer's Productivity \- Parasoft, 6月 5, 2025にアクセス、 [https://www.parasoft.com/news/ai-powered-java-unit-testing-solution-boosts-developers-productivity/](https://www.parasoft.com/news/ai-powered-java-unit-testing-solution-boosts-developers-productivity/)  
6. Transform Java Code-Level Testing With Automation & AI \- Parasoft, 6月 5, 2025にアクセス、 [https://www.parasoft.com/blog/transform-java-code-level-testing-automation-ai/](https://www.parasoft.com/blog/transform-java-code-level-testing-automation-ai/)  
7. ユニットテストの自動作成ツールを調べてみた(2019年末版） \#Java \- Qiita, 6月 5, 2025にアクセス、 [https://qiita.com/policeman-kh/items/00b4f3b524d7f227a7da](https://qiita.com/policeman-kh/items/00b4f3b524d7f227a7da)  
8. Community Edition (Download) \- Diffblue, 6月 5, 2025にアクセス、 [https://www.diffblue.com/community-edition-download/](https://www.diffblue.com/community-edition-download/)  
9. AI-Powered Java Testing Tool \- Boost Productivity \- Parasoft, 6月 5, 2025にアクセス、 [https://www.parasoft.com/products/parasoft-jtest/](https://www.parasoft.com/products/parasoft-jtest/)  
10. Artificial Intelligence \- Diffblue, 6月 5, 2025にアクセス、 [https://www.diffblue.com/resources/artificial-intelligence/](https://www.diffblue.com/resources/artificial-intelligence/)  
11. Java Unit Testing: Best Practices for Developers \- Diffblue, 6月 5, 2025にアクセス、 [https://www.diffblue.com/resources/java-unit-testing-best-practices-for-developers/](https://www.diffblue.com/resources/java-unit-testing-best-practices-for-developers/)  
12. TestForge: Feedback-Driven, Agentic Test Suite Generation \- arXiv, 6月 5, 2025にアクセス、 [https://arxiv.org/pdf/2503.14713](https://arxiv.org/pdf/2503.14713)  
13. Exploiting Test Structure to Enhance Language Models for Software Testing \- Kush Jain, 6月 5, 2025にアクセス、 [https://www.kushjain.com/files/thesis\_final.pdf](https://www.kushjain.com/files/thesis_final.pdf)  
14. EvoSuite | Automatic Test Suite Generation for Java, 6月 5, 2025にアクセス、 [https://www.evosuite.org/](https://www.evosuite.org/)  
15. About | EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/evosuite/](https://www.evosuite.org/evosuite/)  
16. Comparative Analysis of Automated Test Case Generation Tools in Java \- DiVA, 6月 5, 2025にアクセス、 [https://lnu.diva-portal.org/smash/get/diva2:1942973/FULLTEXT01.pdf](https://lnu.diva-portal.org/smash/get/diva2:1942973/FULLTEXT01.pdf)  
17. EvoSuite source code on GitHub, 6月 5, 2025にアクセス、 [https://www.evosuite.org/evosuite-source-code-on-github/](https://www.evosuite.org/evosuite-source-code-on-github/)  
18. randoop/randoop: Automatic test generation for Java \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/randoop/randoop](https://github.com/randoop/randoop)  
19. Automatic unit test generation for Java \- Randoop, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/](https://randoop.github.io/randoop/)  
20. randoop/LICENSE.txt at master \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/randoop/randoop/blob/master/LICENSE.txt](https://github.com/randoop/randoop/blob/master/LICENSE.txt)  
21. net.sourceforge.javydreamercsw:randoop \- Maven Central, 6月 5, 2025にアクセス、 [https://central.sonatype.com/artifact/net.sourceforge.javydreamercsw/randoop](https://central.sonatype.com/artifact/net.sourceforge.javydreamercsw/randoop)  
22. AIによるテスト自動生成ツール「Diffblue」を使ってみた \#Java \- Qiita, 6月 5, 2025にアクセス、 [https://qiita.com/YutaSakamoto-ULS/items/a5f8a8e07e1b5750fb78](https://qiita.com/YutaSakamoto-ULS/items/a5f8a8e07e1b5750fb78)  
23. Top 20 AI Software Testing Tools: Complete List \- ThinkSys Inc, 6月 5, 2025にアクセス、 [https://thinksys.com/qa-testing/top-ai-software-testing-tools/](https://thinksys.com/qa-testing/top-ai-software-testing-tools/)  
24. JetBrains AI Assistant 2024.2: コード補完の改善、よりスマートなチャット、追加の AI 機能, 6月 5, 2025にアクセス、 [https://blog.jetbrains.com/ja/ai/2024/08/jetbrains-ai-assistant-2024-2/](https://blog.jetbrains.com/ja/ai/2024/08/jetbrains-ai-assistant-2024-2/)  
25. AI Assistant Features \- JetBrains, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/ai-assistant/](https://www.jetbrains.com/ai-assistant/)  
26. JetBrains IDEs Go AI: Coding Agent, Smarter Assistance, Free Tier ..., 6月 5, 2025にアクセス、 [https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/](https://blog.jetbrains.com/blog/2025/04/16/jetbrains-ides-go-ai/)  
27. Manage AI Enterprise | IDE Services Documentation \- JetBrains, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/help/ide-services/manage-aie.html](https://www.jetbrains.com/help/ide-services/manage-aie.html)  
28. Eclipseの完全無料コード生成AIプラグインWindsurf（Copilot的な） \- Qiita, 6月 5, 2025にアクセス、 [https://qiita.com/cypher256/items/99e1f2388228a50c732a](https://qiita.com/cypher256/items/99e1f2388228a50c732a)  
29. Windsurf Editor | Windsurf (formerly Codeium), 6月 5, 2025にアクセス、 [https://windsurf.com/editor](https://windsurf.com/editor)  
30. Windsurf (Former Codeium) vs Github Copilot \- Which One to Choose? \- Zencoder, 6月 5, 2025にアクセス、 [https://zencoder.ai/blog/codeium-vs-copilot](https://zencoder.ai/blog/codeium-vs-copilot)  
31. The real reason OpenAI bought WindSurf : r/LocalLLaMA \- Reddit, 6月 5, 2025にアクセス、 [https://www.reddit.com/r/LocalLLaMA/comments/1kgdmz6/the\_real\_reason\_openai\_bought\_windsurf/](https://www.reddit.com/r/LocalLLaMA/comments/1kgdmz6/the_real_reason_openai_bought_windsurf/)  
32. OpenAI reaches agreement to buy Windsurf for $3B | Hacker News, 6月 5, 2025にアクセス、 [https://news.ycombinator.com/item?id=43900877](https://news.ycombinator.com/item?id=43900877)  
33. OpenAI Windsurf Acquisition Sends Shot Heard Around the AI World \- The Futurum Group, 6月 5, 2025にアクセス、 [https://futurumgroup.com/insights/openai-windsurf-boosts-ai-coding-agentic-software-development/](https://futurumgroup.com/insights/openai-windsurf-boosts-ai-coding-agentic-software-development/)  
34. Pricing | Windsurf (formerly Codeium), 6月 5, 2025にアクセス、 [https://windsurf.com/pricing](https://windsurf.com/pricing)  
35. Licensing and subscriptions | AI Assistant Documentation \- JetBrains, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html](https://www.jetbrains.com/help/ai-assistant/licensing-and-subscriptions.html)  
36. EvoSuite \- automated generation of JUnit test suites for Java classes \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/EvoSuite/evosuite](https://github.com/EvoSuite/evosuite)  
37. The EVO Suite — Included with EVO \- Studio Network Solutions, 6月 5, 2025にアクセス、 [https://www.studionetworksolutions.com/evo-suite/](https://www.studionetworksolutions.com/evo-suite/)  
38. Documentation | EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/](https://www.evosuite.org/documentation/)  
39. New 1.0.6 release \- EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/new-1-0-6-release/](https://www.evosuite.org/new-1-0-6-release/)  
40. 1月 1, 1970にアクセス、 [https://www.evosuite.org/documentation/mocking/](https://www.evosuite.org/documentation/mocking/)  
41. EvoSuite \- Google Groups, 6月 5, 2025にアクセス、 [https://groups.google.com/g/evosuite](https://groups.google.com/g/evosuite)  
42. 1月 1, 1970にアクセス、 [https://www.evosuite.org/documentation/tutorials/](https://www.evosuite.org/documentation/tutorials/)  
43. EVO Enhances Existing Storage Systems \- Studio Network Solutions, 6月 5, 2025にアクセス、 [https://www.studionetworksolutions.com/evo-enhances-existing-storage-systems/](https://www.studionetworksolutions.com/evo-enhances-existing-storage-systems/)  
44. New EVO Suite Features Announced At NAB Show 2024 — SNS (Studio Network Solutions), 6月 5, 2025にアクセス、 [https://www.studionetworksolutions.com/new-evo-suite-features-announced-at-nab-show-2024/](https://www.studionetworksolutions.com/new-evo-suite-features-announced-at-nab-show-2024/)  
45. Randoop Developer's Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/dev.html](https://randoop.github.io/randoop/manual/dev.html)  
46. Randoop Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/index.html\#generating-tests](https://randoop.github.io/randoop/manual/index.html#generating-tests)  
47. Randoop Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/index.html\#miscellaneous-notes](https://randoop.github.io/randoop/manual/index.html#miscellaneous-notes)  
48. Randoop Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/](https://randoop.github.io/randoop/manual/)  
49. New Strategies for Automated Random Testing \- CORE, 6月 5, 2025にアクセス、 [https://core.ac.uk/download/pdf/29030485.pdf](https://core.ac.uk/download/pdf/29030485.pdf)  
50. Shuvendu Lahiri at Microsoft Research, 6月 5, 2025にアクセス、 [https://www.microsoft.com/en-us/research/people/shuvendu/](https://www.microsoft.com/en-us/research/people/shuvendu/)  
51. Licensing \- Diffblue Documentation, 6月 5, 2025にアクセス、 [https://docs.diffblue.com/get-started/licensing](https://docs.diffblue.com/get-started/licensing)  
52. Online license activation \- Diffblue Documentation, 6月 5, 2025にアクセス、 [https://docs.diffblue.com/get-started/licensing/licensing-online](https://docs.diffblue.com/get-started/licensing/licensing-online)  
53. Free trial | Diffblue Documentation, 6月 5, 2025にアクセス、 [https://docs.diffblue.com/get-started/get-started/free-trial](https://docs.diffblue.com/get-started/get-started/free-trial)  
54. Get started \- Cover Plugin \- Diffblue Documentation, 6月 5, 2025にアクセス、 [https://docs.diffblue.com/get-started/get-started/get-started-cover-plugin](https://docs.diffblue.com/get-started/get-started/get-started-cover-plugin)  
55. 1月 1, 1970にアクセス、 [https://docs.diffblue.com/cover-plugin/writing-tests/mocks-and-templates/](https://docs.diffblue.com/cover-plugin/writing-tests/mocks-and-templates/)  
56. Diffblue Documentation: Discover Diffblue Cover, 6月 5, 2025にアクセス、 [https://docs.diffblue.com/](https://docs.diffblue.com/)  
57. Azure OpenAI in Azure AI Foundry Models \- Learn Microsoft, 6月 5, 2025にアクセス、 [https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)  
58. ReSharper \- ユニットテスト－機能 \- JetBrains, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/ja-jp/resharper//features/unit\_testing.html](https://www.jetbrains.com/ja-jp/resharper//features/unit_testing.html)  
59. Install AI Assistant in a JetBrains IDE, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/help/ai-assistant/installation-guide-ai-assistant.html](https://www.jetbrains.com/help/ai-assistant/installation-guide-ai-assistant.html)  
60. JetBrains AI Assistant \- IntelliJ IDEs Plugin | Marketplace, 6月 5, 2025にアクセス、 [https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant](https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant)  
61. JetBrains AI Plans & Pricing, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/ai-ides/buy/](https://www.jetbrains.com/ai-ides/buy/)  
62. WebStorm and Rider Are Now Free for Non-Commercial Use | The JetBrains Blog, 6月 5, 2025にアクセス、 [https://blog.jetbrains.com/blog/2024/10/24/webstorm-and-rider-are-now-free-for-non-commercial-use/](https://blog.jetbrains.com/blog/2024/10/24/webstorm-and-rider-are-now-free-for-non-commercial-use/)  
63. JetBrains Makes Rider Free for Non-Commercial Use – A Game-Changer for F\# Devs\! : r/fsharp \- Reddit, 6月 5, 2025にアクセス、 [https://www.reddit.com/r/fsharp/comments/1gb3idg/jetbrains\_makes\_rider\_free\_for\_noncommercial\_use/](https://www.reddit.com/r/fsharp/comments/1gb3idg/jetbrains_makes_rider_free_for_noncommercial_use/)  
64. JetBrains announces a free tier for its AI tools \- SD Times, 6月 5, 2025にアクセス、 [https://sdtimes.com/softwaredev/jetbrains-announces-a-free-tier-for-its-ai-tools/](https://sdtimes.com/softwaredev/jetbrains-announces-a-free-tier-for-its-ai-tools/)  
65. JetBrains AI EAP Terms of Service, 6月 5, 2025にアクセス、 [https://www.jetbrains.com/legal/docs/terms/jetbrains-ai/](https://www.jetbrains.com/legal/docs/terms/jetbrains-ai/)  
66. 1月 1, 1970にアクセス、 [https.www.jetbrains.com/legal/docs/terms/jetbrains\_ai\_service.html](http://docs.google.com/https.www.jetbrains.com/legal/docs/terms/jetbrains_ai_service.html)  
67. 1月 1, 1970にアクセス、 [https://www.jetbrains.com/legal/docs/terms/ai-assistant/](https://www.jetbrains.com/legal/docs/terms/ai-assistant/)  
68. 1月 1, 1970にアクセス、 [https://www.jetbrains.com/legal/docs/terms/toolbox\_subscription/](https://www.jetbrains.com/legal/docs/terms/toolbox_subscription/)  
69. 1月 1, 1970にアクセス、 [https://www.jetbrains.com/ai-assistant/faq/](https://www.jetbrains.com/ai-assistant/faq/)  
70. BaseRock-AI/docs \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/Sapient-AI/docs](https://github.com/Sapient-AI/docs)  
71. A Comparative Study of SBST, Symbolic Execution, and LLM-Based Approaches to Unit Test Generation \- arXiv, 6月 5, 2025にアクセス、 [https://arxiv.org/html/2501.10200v1](https://arxiv.org/html/2501.10200v1)  
72. Learning Deep Semantics for Test Completion | Request PDF \- ResearchGate, 6月 5, 2025にアクセス、 [https://www.researchgate.net/publication/372385727\_Learning\_Deep\_Semantics\_for\_Test\_Completion](https://www.researchgate.net/publication/372385727_Learning_Deep_Semantics_for_Test_Completion)  
73. AI Code Review and the Best AI Code Review Tools in 2025 \- Qodo, 6月 5, 2025にアクセス、 [https://www.qodo.ai/learn/code-review/ai/](https://www.qodo.ai/learn/code-review/ai/)  
74. \[AINews\] o3 solves AIME, GPQA, Codeforces, makes 11 years of progress in ARC-AGI and 25% in FrontierMath \- Buttondown, 6月 5, 2025にアクセス、 [https://buttondown.com/ainews/archive/ainews-o3-solves-aime-gpqa-codeforces-makes-11/](https://buttondown.com/ainews/archive/ainews-o3-solves-aime-gpqa-codeforces-makes-11/)  
75. Terms of Service: Individual & Pro | Windsurf (formerly Codeium), 6月 5, 2025にアクセス、 [https://windsurf.com/terms-of-service-individual](https://windsurf.com/terms-of-service-individual)  
76. Windsurf \- Atlassian Marketplace, 6月 5, 2025にアクセス、 [https://marketplace.atlassian.com/apps/1231479/windsurf?tab=overview](https://marketplace.atlassian.com/apps/1231479/windsurf?tab=overview)  
77. codeium.com, 6月 5, 2025にアクセス、 [https://codeium.com/terms-of-service](https://codeium.com/terms-of-service)  
78. 1月 1, 1970にアクセス、 [https://codeium.com/terms](https://codeium.com/terms)  
79. FAQ | Windsurf (formerly Codeium), 6月 5, 2025にアクセス、 [https://codeium.com/faq](https://codeium.com/faq)  
80. 1月 1, 1970にアクセス、 [https://codeium.com/individual](https://codeium.com/individual)  
81. FAQ | Windsurf (formerly Codeium), 6月 5, 2025にアクセス、 [https://windsurf.com/faq](https://windsurf.com/faq)  
82. All Articles \- BestofAI, 6月 5, 2025にアクセス、 [https://bestofai.com/allArticles](https://bestofai.com/allArticles)  
83. Azure OpenAI in Azure AI Foundry Models quotas and limits \- Learn Microsoft, 6月 5, 2025にアクセス、 [https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits](https://learn.microsoft.com/en-us/azure/ai-services/openai/quotas-limits)  
84. www.eweek.com, 6月 5, 2025にアクセス、 [https://www.eweek.com/it-management/jtest-5.0-eliminates-excuses/\#:\~:text=Pricing%20for%20Jtest%205.0%20starts%20at%20%243%2C495.\&text=PRO%3A%20Extensive%20control%20of%20coding,click%20repair%20of%20many%20errors.](https://www.eweek.com/it-management/jtest-5.0-eliminates-excuses/#:~:text=Pricing%20for%20Jtest%205.0%20starts%20at%20%243%2C495.&text=PRO%3A%20Extensive%20control%20of%20coding,click%20repair%20of%20many%20errors.)  
85. Jtest 5.0 Eliminates Excuses \- eWEEK, 6月 5, 2025にアクセス、 [https://www.eweek.com/it-management/jtest-5.0-eliminates-excuses/](https://www.eweek.com/it-management/jtest-5.0-eliminates-excuses/)  
86. Acceptance Test Generation with Large Language Models: An Industrial Case Study \- arXiv, 6月 5, 2025にアクセス、 [https://arxiv.org/html/2504.07244v1](https://arxiv.org/html/2504.07244v1)  
87. PromptPex: Automatic Test Generation for Language Model Prompts \- arXiv, 6月 5, 2025にアクセス、 [https://arxiv.org/pdf/2503.05070](https://arxiv.org/pdf/2503.05070)