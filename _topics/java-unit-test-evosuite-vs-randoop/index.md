---
layout: topic
title: "Javaユニットテスト自動生成ツールEvoSuiteとRandoopの機能比較と評価"
date: 2025-06-05
prompt: "Javaのユニットテストを自動で作成したい。EvoSuiteとRandoopの機能を比較して、実行環境や特徴などそれぞれのツールの良し悪しをまとめて欲しい。"
category: "engineering"
tags: [ユニットテスト]
audio: "/share-deepresearch/assets/audio/java-unit-test-evosuite-vs-randoop.mp3"
supplementary_materials:
  - title: "Javaユニットテスト自動生成ツール比較：EvoSuite vs Randoop"
    url: "/share-deepresearch/topics/java-unit-test-evosuite-vs-randoop/infographic.html"
---

# **Javaユニットテスト自動生成ツールEvoSuiteとRandoopの機能比較と評価**

## **1\. はじめに**

### **1.1. 現代Java開発における自動ユニットテストの必要性**

現代のソフトウェア開発において、ユニットテストは品質保証の根幹をなす要素です。しかし、手動によるユニットテストの作成と維持は、多大な時間と労力を要し、ヒューマンエラーの温床となり得るだけでなく、開発サイクルの遅延やメンテナンスコストの増大といった課題を抱えています。このような背景から、ユニットテスト生成の自動化は、開発者の生産性向上、コード品質の改善、フィードバックサイクルの高速化、そしてリグレッションの防止といった多岐にわたる恩恵をもたらす技術として注目されています。

### **1.2. EvoSuiteとRandoop：Javaテスト自動生成における主要ツール**

本レポートでは、Javaアプリケーション向けのJUnitテストを自動生成する代表的なオープンソースツールであるEvoSuiteとRandoopについて、詳細な比較分析を行います。これらのツールは、学術研究に裏打ちされた堅牢な基盤を持ち、テスト作成の自動化という共通の目標を掲げつつも、その設計思想やテスト生成アプローチにおいて顕著な違いを有しています 1。本稿では、それぞれの機能、実行環境、特性、長所と短所を深掘りし、Java開発プロジェクトにおける最適なツール選択の一助となる情報を提供します。

## **2\. EvoSuite：詳細分析**

EvoSuiteは、特にコードカバレッジ基準の達成を目標としてJUnitテストスイートを自動生成するツールです。

### **2.1. コア機能とテスト生成方法論**

EvoSuiteの核心的な特徴は、遺伝的アルゴリズム（GA）を駆使してテストスイート全体を進化的に最適化する点にあります 3。

* テストスイート全体の進化的最適化:  
  個々のテストケースを個別の目標に対して逐次生成するのではなく、EvoSuiteはテストスイート全体を一個体として扱い、集団内で進化させます。この際、分岐カバレッジのようなカバレッジ基準を最大化しつつ、テストスイートの総サイズを最小限に抑えることを目指します 7。この「ホールテストスイート（whole test suite）」アプローチは、テスト目標の処理順序への依存性や到達不可能な目標の扱いに起因する、目標ごとのテスト生成手法の限界を克服するように設計されています 7。  
  具体的には、ランダムに生成されたテストスイートの初期集団から開始し、選択、交叉、突然変異といった進化的操作を繰り返し適用することで、より優れたテストスイートへと改良していきます 7。多くの場合、DynaMOSAがデフォルトのアルゴリズムとして採用されています 10。  
* **主要な出力:**  
  * JUnitテストを生成します 1。  
  * テスト対象クラス（CUT: Class Under Test）の現在の振る舞いを捉えるためのリグレッションアサーションを追加します 1。  
  * 生成されたテストの可読性を向上させるために、テストケースを最小化します 3。

EvoSuiteの進化的かつホールスイート最適化アプローチは、構造的カバレッジを効率的に高く達成することに根本的に適しています。遺伝的アルゴリズムは複雑な最適化問題に対する強力な探索ヒューリスティクスであり 7、スイート全体を対象とすることでテストケース間の相互依存関係やカバレッジ目標をより適切に扱うことができます 7。カバレッジ最大化とサイズ最小化という二重の目的 7 は、テストスイートの品質と保守性に関する実用的な懸念に直接的に対応しています。これは、EvoSuiteが特定の高い構造的カバレッジレベルの達成が主要な目標となるシナリオ向けに設計されていることを示唆しています。

### **2.2. 実行環境**

* **対応Javaバージョン:**  
  * Java 8でコンパイルされています 13。  
  * バージョン1.1.0（2020年10月）では、いくつかの注意点（DSEはJava 8まで、JEEサポートは当面削除）付きでJava 9以降のサポートが追加されました 10。  
  * バージョン1.2.0（2021年9月）には、DSEおよびEclipseプラグイン向けのJava 9サポートが含まれていました 10。  
  * 2023年11月時点で、Java 17および21のサポートに関するユーザーからの問い合わせがありましたが、最新の公式リリースは2021年のものです 14。  
  * DockerイメージはJava 8およびJava 11用の環境を提供しています 3。  
* **オペレーティングシステム互換性:**  
  * Javaベースであるため、一般的にMac、Linux、Windowsで動作するはずです 13。  
  * IntelliJプラグインはMac OS XおよびWindows 7でテストされており、他のOSでは動作しない可能性があります 13。  
  * EclipseプラグインはEclipse MarsおよびLunaでテストされています 13。  
  * evosuite-coverage-toolsのGitHub ActionsはLinux、macOS、Windowsで実行されます 15。  
* **ビルドツールおよびIDEとの連携:**  
  * **Mavenプラグイン:** EvoSuiteを統合するための主要な手段であり、ドキュメントも充実しています 1。  
    * *設定:* pom.xmlファイルでプラグイン、ランタイム依存性（evosuite-standalone-runtime）、JUnit、Surefireリスナーを設定します 1。  
    * *利点:* CI/CD連携（例：Jenkins）、ローカルインストール不要、クラスパス管理 3。  
  * **IntelliJ IDEAプラグイン:** JetBrainsプラグインリポジトリから入手可能です。プロジェクトがMavenを使用している場合、Mavenプラグインのラッパーとして機能します 3。  
  * **Eclipseプラグイン:** 実験的なプラグインがアップデートサイト経由で提供されています 3。  
  * **コマンドライン:** evosuite.jarを使用したEvoSuiteの基本的な実行方法です 1。  
  * **Gradle連携:** 公式ドキュメントは主にMavenを強調していますが、サードパーティ製のGradleプラグインも存在します（例：LajosCseppento氏によるgradle-evosuite-plugin 21）。1では、Gradleがビルドツールとして勢いを増していると言及されています。  
* **主要な依存関係とランタイム要件:**  
  * 生成されたテストの実行にはevosuite-standalone-runtime.jarが不可欠です 1。  
  * JUnit（バージョン4.12以上を推奨）が必要です 17。  
  * MavenプラグインにはMaven 3.1以上が必要です 17。

Maven連携とそれに関する詳細な設定（17）が強く強調されていることから、EvoSuiteはMavenが標準でありCI/CD連携が不可欠な、確立されたエンタープライズ環境に適していると考えられます。IDEプラグインの提供は、そのような環境内の個々の開発者にとっての導入障壁をさらに低くします。これは、Mavenが大規模なJavaプロジェクトで普及している成熟したビルドツールであること、EvoSuiteのドキュメントがランタイム依存関係の処理や混合テスト環境向けのSurefire設定を含むMavenセットアップに関する広範なガイダンスを提供していること 17、そしてローカルインストールなしにMaven経由でEvoSuiteを実行できる能力がCIサーバーでのデプロイメントを簡素化すること 3 に基づいています。これは、主にコマンドラインの使用や、詳細なビルドツールサポートなしの単純なIDE連携に焦点を当てたツールとは対照的です。

### **2.3. 主要な特性**

* **コードカバレッジ能力と測定:**  
  * 行カバレッジや分岐カバレッジといった構造的カバレッジ基準を目標とします 1。  
  * コードカバレッジを測定でき 16、レポートを生成できます（例：特定の基準に対するカバレッジを示すCSV出力 23）。  
  * 実際には高い分岐カバレッジを達成します（ある大規模研究ではクラスあたり平均71% 9）。  
  * **カバレッジ測定の課題:** EvoSuiteによるバイトコード計装（モック作成、環境分離のため）が、外部のカバレッジツール（JaCoCo、Coberturaなど）と競合し、カバレッジが0%と表示される可能性があります 22。  
    * *解決策:* EvoSuiteは2つの計装モード（独自のクラスローダー対Javaエージェント）を提供しています。JaCoCoのようなツールによるオフライン計装は一般的に堅牢性が高いです 22。  
* **生成テストの品質、可読性、保守性:**  
  * **最小化:** 生成されたテストは可読性向上のために最小化されます 3。  
  * **アサーション:** リグレッションアサーションは現在の振る舞いを捉えます 1。EvoSuiteはミューテーション分析を使用して効果的なアサーションを選択します 9。  
  * **可読性の問題:** 最小化されても、自動生成されたテストは依然として読みにくい場合があります 24。ある研究では、EvoSuiteが生成したテストは最適化によりランダムシーケンスよりも優れていると指摘されています 25。SBFT 2025コンペティションでは、EvoSuite（およびEvoFuzz）がRandoopよりも優れた可読性メトリクスを示しました 11。  
  * **テスト命名:** 生成されるテスト名（例：test00、test01）は曖昧な場合があり、特にオーバーロードされたメソッドの場合、どの特定のメソッドがテストされているかを特定するのが困難になることがあります 40。  
  * **スキャフォールディング:** \_ESTest\_scaffolding.javaファイルを生成し、一部のユーザーはこれを破棄することを提案しています 19。  
* **セットアップの複雑さと設定オプション:**  
  * 特に他のツールと比較して、セットアップが複雑になる可能性があります 2。これには、プラグインのインストール、Maven/Javaホームの指定、テスト生成のためのpom.xmlの変更が含まれます 26。  
  * 多数のコマンドラインパラメータ（-Dkey=value）と、遺伝的アルゴリズムやその他の設定を詳細に構成するためのevosuite.propertiesファイルを提供します 20。  
  * IDEプラグインは使用の簡素化を目的としています 16。  
* **パフォーマンスと実行速度:**  
  * 大規模プロジェクトや複雑なクラスの場合、実行時間が長くなる可能性があります 24。しかし、5分間の実行で完了したという報告もあります 41。  
  * SBFT 2025ベンチマーク：EvoSuiteは、CUTあたり120秒の時間予算で55個のCUTに対し、2時間51分で2,049個のテスト（平均13.0テスト/CUT）を生成しました 11。これは、その特定のベンチマークにおいてRandoopよりも高速で、生成するテスト数も少ないです。  
  * パフォーマンスはクラスの複雑さ 42 や設定（例：検索予算 20）に影響されます。  
* **欠陥検出効果とパターン:**  
  * 研究において良好な欠陥検出能力を示し、しばしばRandoopを上回ります 30。ある研究では10件中7件の欠陥を検出しました 30。  
  * クラッシュや未宣言の例外を検出できます 9。  
  * **限界:**  
    * ファイルシステムやネットワークといった環境への強い依存関係を持つコード内の欠陥の扱いに苦労します。これは、これらの領域でのカバレッジが低いためです 9。  
    * マルチスレッドコード向けには最適化されておらず、並行性関連の欠陥を見逃す可能性があります 9。  
    * クラスレベルでの生成と汎用的なテスト命名のため、特定のメソッドに対するテスト生成が困難な場合があります 40。  
    * 不安定なテストを生成する可能性があります（ある研究では0.2%～5.4% 45）。ただし、これを軽減するメカニズムも備えています 22。  
    * 複雑なオブジェクトのインスタンス化が課題となることがあります 46。

EvoSuiteのモック用バイトコード計装や詳細な設定オプションといった高度な機能は強力である一方、セットアップの複雑さや（カバレッジツールなどとの）競合の可能性の一因となっています。バイトコード計装 22 は、テストを環境から分離するために必要な高度な技術であり、テストの安定性には有益です。しかし、これはカバレッジ分析ツールのようなバイトコードを計装する他のツールと衝突する可能性があり、慎重な設定（例：use\_separate\_classloaderオプション 22）を必要とします。広範な設定可能パラメータのリスト 20 は微調整を可能にしますが、新規ユーザーにとっては圧倒される可能性があります 2。これは、EvoSuiteがより急な学習曲線とより複雑なセットアップを犠牲にして、詳細な制御と堅牢なテスト分離を提供することを示唆しています。

### **2.4. EvoSuiteの長所**

* **高いコードカバレッジ:** 構造的カバレッジ（分岐、行、ミューテーション）の達成に優れています 1。  
* **効果的な欠陥検出:** 比較研究において、一般的に強力な欠陥検出能力を示します 30。  
* **テストの最小化とリグレッションアサーション:** テストの品質を向上させ、現在の振る舞いを捉えるのに役立ちます 1。  
* **連携能力:** Mavenの強力なサポートとIDEプラグイン（Eclipse、IntelliJ）により、一般的な開発環境での使用が容易になります 1。  
* **オープンソースと（歴史的な）活発な開発:** 強力な学術的支援とコンペティションへの参加実績があります 2。  
* **環境分離:** テストを環境依存性（ファイルシステム、ネットワーク）から分離しようと試み、より安定したテストにつながります 1。

### **2.5. EvoSuiteの短所と限界**

* **セットアップの複雑さ:** 特に初心者にとって、設定と統合が複雑になる可能性があります 2。  
* **実行時間:** 大規模または複雑なコードベースの場合、テスト生成に時間がかかることがあります 24。  
* **Javaバージョンサポートの遅れ:** 公式リリースが最新のJava LTSバージョンに遅れる可能性があります 10。  
* **生成テストの可読性:** 最小化されても、テストは人間にとって理解し保守するのが難しい場合があります 24。  
* **カバレッジツールとの競合:** バイトコード計装が外部のコードカバレッジツールと干渉する可能性があります 22。  
* **特定のコード構造の扱い:**  
  * 環境依存性（ファイル、ネットワーク）、マルチスレッドの扱いに困難があります 9。  
  * 汎用的な命名のため、特定のメソッドのテストを特定するのが難しい場合があります 40。  
  * テスト命名におけるポリモーフィズムやオーバーロードされたメソッドの課題があります 40。  
  * 複雑なオブジェクトのインスタンス化は依然としてハードルです 46。  
* **モノリシックなアーキテクチャ（内部API）:** あるレビューでは、内部APIがサードパーティによる使用を想定して設計されていないため、拡張が困難であると指摘されています 25。

## **3\. Randoop：詳細分析**

Randoopは、フィードバック指向のランダムテスト生成を用いてJUnitテストを自動生成するツールです。

### **3.1. コア機能とテスト生成方法論**

Randoopの基本的なアプローチは、メソッドやコンストラクタの呼び出しシーケンスを疑似ランダムに生成することです 5。

* フィードバック指向ランダムテスト生成:  
  テストを段階的に構築します。新しいテストごとに、呼び出すメソッドを選択し、以前のテストで計算された値またはシード値から引数を選択します 47。  
  生成されたシーケンスを実行し、その結果（例外、戻り値など）を使用してアサーションを作成し、将来のテスト生成をガイドします（例えば、冗長または不正なシーケンスを回避するなど）5。  
* **主要な出力:** 5  
  * **エラー検出テスト:** 実行時に失敗するJUnitテストで、契約違反（例：equals()、hashCode()、null性）や予期せぬ例外の発生によって潜在的なバグを示します。  
  * **リグレッションテスト:** 実行時に成功するJUnitテストで、プログラムの現在の観測された振る舞いを捉えます。これらには、観測された戻り値やスローされた例外に基づくアサーションが含まれます。

Randoopの強みは、ランダムなシーケンスを通じて多種多様な正当および不正なプログラムの振る舞いを迅速に探索する能力にあり、これにより、検索ベースのアプローチよりも少ない初期設定で契約違反や予期せぬ例外を発見するのに効果的です。ランダム生成は、人間のテスターが考慮しないような珍しい（しかし正当な）呼び出しシーケンスを作成する可能性があります 5。フィードバックメカニズムは、明らかに問題のあるパス（例：常に早期に例外をスローするパス）を枝刈りし、ランダム性を「より賢く」します 5。契約違反に基づく「エラー検出」テストの明示的な生成 47 は、即座に実行可能なバグレポートを提供します。このアプローチは、網羅的な構造的カバレッジよりも、契約と観測された出力によって定義される振る舞いの正当性に本質的に焦点を当てています。

### **3.2. 実行環境**

* **対応Javaバージョン:**  
  * Java 8以降のJVMで動作します 47。  
  * 最近のJavaバージョンを積極的にサポートしています：Java 17、19、20が最近のリリース（2022年～2024年）で明示的に言及されています 51。  
  * Randoop自体はJava 8ではもはや*ビルド*されませんが、Java 8で*実行*は可能です（v4.3.3、2024年5月時点）51。  
* **オペレーティングシステム互換性:**  
  * Javaツールとして、一般的にクロスプラットフォームです（Linux、macOS、Windows）52。  
* **ビルドツールおよびIDEとの連携:**  
  * **コマンドライン:** 主要な操作モードで、java \-cp... randoop.main.Main gentests... を介して呼び出されます 47。  
  * **Gradle連携:** Randoop自体はGradleでビルドされます 4。JavaプロジェクトでRandoopを実行するための実験的なGradleプラグイン（SRI-CSLのrandoop-gradle-plugin）が存在します 55。  
  * **IDE連携:** Randoop開発者マニュアルには、Gradleタスク（./gradlew idea、./gradlew eclipse）を実行することで、IntelliJ IDEA、NetBeans、Eclipse内でRandoopを開発用にセットアップする方法が記載されています 54。これは、ユーザー向けのテスト生成プラグインというよりは、Randoop自体の開発向けです。  
  * **Maven連携:** Randoop自身のビルドに関しては、公式ドキュメントではGradleほど強調されていません。ユーザーは通常、Mavenからexec-maven-pluginや同様のメカニズムを使用してコマンドラインを呼び出すことになります。  
* **主要な依存関係とランタイム要件:**  
  * randoop-all-\<version\>.jar にはRandoopとその依存関係が含まれています 47。  
  * 生成されたテストにはJUnitが必要です 4。

Randoopのより最新のJavaバージョンサポート 51 とGradleへの依存 4 は、最新のJavaバージョンとGradleを主要なビルドツールとして使用しているプロジェクトにとって、より簡単な選択肢となる可能性があります。コマンドライン実行のセットアップはよりシンプルに見えます。これは、新しいJavaリリースに対する頻繁なアップデートが最新のJavaリリースを使用するプロジェクトの摩擦を軽減すること、EvoSuiteは強力なMavenサポートを持っていますが、Randoopのエコシステム（ビルドと実験的プラグイン）はGradleに傾倒しており、新しいJavaプロジェクトのトレンドと一致していること、そしてコマンドライン経由の主要な文書化された使用法 47 は直接的であり、基本的な操作のために複雑なIDEやビルドツールプラグインの設定を必要としないことに基づいています。

### **3.3. 主要な特性**

* **コードカバレッジ能力:**  
  * EvoSuiteのような主要な最適化目標ではありませんが、Randoopもコードカバレッジを達成します。フィードバック指向のランダムテストは、場合によっては従来のランダムテストよりも短時間で同等以上のカバレッジを達成できます 56。  
  * Randoopが生成したテストのカバレッジデータは、JaCoCoのようなツールを使用して収集できます 57。  
* **生成テストの品質、可読性、保守性:**  
  * **エラー検出テスト vs. リグレッションテスト:** 出力において明確に区別されます 47。  
  * **可読性の問題:** 生成されたテストは「ほとんど読めず、しばしば些細で、冗長性が高い」ことがあります 25。ランダムな性質により、手動レビューが必要な有用性の低いテストが生成される可能性があります 2。  
  * **テストの最小化:** Randoopは、失敗したテスト（Randoopが生成しなかったものも含む）を単純化するためのminimizeコマンドを提供しています 47。  
  * **アサーション:** リグレッションテストは現在の振る舞いを捉えます。エラー検出テストは特定の契約をチェックします 47。  
  * **不安定性（Flakiness）:** 研究によると、Randoopのテストは不安定になる可能性があります（ある研究では約5% 58）。しかし、別の比較ではEvoSuiteよりも低い結果でした 30。Randoopには不安定なテストを処理するためのオプション（--flaky-test-behavior）があります 47。  
* **セットアップの複雑さと設定オプション:**  
  * 特にコマンドライン経由での基本的な使用は、比較的簡単にセットアップできます 2。  
  * 微調整のための多くのコマンドラインオプションがあります。例：--classlist、--time-limit、--output-limit、--omit-methods、契約チェック用の--specifications 47。  
* **パフォーマンスと実行速度:**  
  * ユーザー定義の時間制限内でテストを生成します（例：--time-limit=60）47。  
  * SBFT 2025ベンチマーク：Randoopは、CUTあたり120秒の時間予算で55個のCUTに対し、5時間35分で1,561,533個のテスト（平均9521.5テスト/CUT）を生成しました 11。これは、そのベンチマークにおいてEvoSuiteよりも低速ですが、はるかに多くのテストを生成します。  
  * 時々、終了しないテストや実行に非常に時間がかかるテストを作成することがあります。--usethreadsオプションが役立つ場合がありますが、パフォーマンスは低下します 59。  
* **欠陥検出効果とパターン:**  
  * JDKのような広く使用されているライブラリを含む、バグの発見に効果的です 5。ある研究では10件中5件の欠陥を検出しました 30。  
  * 契約違反（例：equalsの反射性 48）や予期せぬランタイム例外の発見に優れています。  
  * APIメソッドシーケンスに焦点を当てているため、ファズテストでは見逃されるエラーを発見できます 56。  
  * **限界:**  
    * ランダムな性質により、特定の複雑なバグ（ターゲットを絞った検索が必要）を見逃す可能性があります。  
    * 効果は初期期間後に頭打ちになることがあります 56。  
    * ランダムに到達しにくい分岐に苦労する可能性があります 56。  
    * プライベートメソッドを直接テストしません（ただし、生成されたテストが間接的に呼び出す可能性はあります）59。

Randoopが大量のテスト（多くは単純なものを含む、SBFT 2025ベンチマーク 11 で見られるように）を生成し、契約チェックと組み合わせることは、振る舞いの異常や標準的な契約違反を発見するために「広範な網を投げる」ツールであることを示しています。生成されるシーケンスの数が多いため、多様な状態やメソッドの相互作用に遭遇する確率が高まります 25。Object契約の組み込みチェック 40 は、正当性のベースラインを提供します。多くのテストは些細または冗長である可能性がありますが 25、この大量生成は、単純なバグや期待される基本的な振る舞いからの逸脱を迅速に発見するのに効果的です。これは、特定のカバレッジ目標を満たすために複雑なシーケンスをよりターゲットを絞って検索するEvoSuiteとは対照的です。

### **3.4. Randoopの長所**

* **効果的なバグ発見ツール:** 成熟したソフトウェアを含む、実際のバグを発見することが証明されています 5。  
* **フィードバック指向のランダム性:** 純粋なランダム生成よりも賢く、多くの無用なテストを回避します 5。  
* **エラー検出テストとリグレッションテスト:** 新しい問題を発見するテストと既存の振る舞いを捉えるテストを明確に分離します 47。  
* **契約チェック:** 標準的なJavaオブジェクト契約とユーザー定義の仕様をチェックするための強力なサポートがあります 47。  
* **基本的な使用の容易さ:** 特にコマンドライン経由で比較的簡単に始めることができます 2。  
* **オープンソースと活発なメンテナンス:** 良好なリリースペースと最新Javaバージョンのサポートがあります 2。  
* **スケーラビリティ:** 非常に多数のテストを生成できます 11。

### **3.5. Randoopの短所と限界**

* **テストの可読性と品質:** 生成されたテストは読みにくく、些細であったり、冗長であったりすることがあります 2。  
* **カバレッジは主要目標ではない:** そのために特別に最適化されたツールほど高い構造的カバレッジを達成できない場合があります 30。  
* **ランダムな性質:** 無関係なテストを生成したり、ガイド付き検索が必要な特定の複雑なバグを見逃したりする可能性があります 2。  
* **限定的な状態分析:** 詳細なプログラム状態分析ではなく、観測された中間結果に依存します 25。  
* **パフォーマンスの頭打ち:** 特定のコードベースに対するバグ発見効果が時間とともに低下する可能性があります 56。  
* **プライベートメソッドの直接テストなし:** パブリックAPIに焦点を当てています 59。

## **4\. 比較分析：EvoSuite vs. Randoop**

EvoSuiteとRandoopは、Javaユニットテストの自動生成という共通の目的を持ちながら、そのアプローチと特性において顕著な違いを示します。

### **4.1. 主要メトリクスにおける直接比較**

**表1：主要機能とアプローチの比較（EvoSuite vs. Randoop）**

| 側面 | EvoSuite | Randoop |
| :---- | :---- | :---- |
| **主要目標** | 構造的カバレッジの最大化 | 振る舞いの探索／契約違反の発見 |
| **テスト生成戦略** | 進化的／検索ベース | フィードバック指向ランダム |
| **主要な出力** | カバレッジ用に最適化されたJUnitテスト | エラー検出およびリグレッションJUnitテスト |
| **アサーション生成** | リグレッションアサーション、ミューテーションベース | 観測された振る舞い、契約違反 |
| **主な強みの例** | 高い分岐カバレッジ達成 | 予期せぬAPI誤用の発見 |

* コードカバレッジ:  
  EvoSuiteは、直接比較において、一般的に高い構造的コードカバレッジ（行、分岐）とミューテーションスコアを達成します 30。例えば、ある研究ではEvoSuiteが平均89%のカバレッジを達成したのに対し、Randoopは平均63%でした 30。これは、EvoSuiteの進化的アルゴリズムがこれらのメトリクスを最適化するように設計されているため、予想される結果です。Randoopのランダムアプローチは、振る舞いを探索する副産物としてコードをカバーします。  
* ミューテーションスコア:  
  EvoSuiteはより高いミューテーションスコアを示す傾向があります 30。前述の研究では、EvoSuiteが67%、Randoopが50%でした 30。高いミューテーションスコアは、EvoSuiteのテストが小さなコード変更を検出するのにより効果的であることを示唆しており、これはしばしば欠陥検出と相関します。  
* 欠陥検出:  
  両ツールとも実際の欠陥を検出します 45。いくつかの研究ではEvoSuiteがより多くの欠陥を検出しました（30ではRandoopの5/10に対し7/10）。しかし、これらは異なる種類の欠陥を発見する可能性があります。Randoopは多様な呼び出しシーケンスからの契約違反や予期せぬ例外の発見に優れており 47、一方EvoSuiteのカバレッジ駆動アプローチは、より曖昧で深くネストされたコードパス内の欠陥を発見する可能性があります 9。Defects4Jに関する研究 45 では、自動生成されたテスト（EvoSuiteとRandoopを含む）が全体の欠陥の55.7%を検出しましたが、個々のテストスイートでは19.9%しか検出しませんでした。これは、単一のツール実行が万能薬ではないことを強調しています。EvoSuiteによる欠陥のあるステートメントの高いカバレッジ 45 は検出の前提条件ですが、欠陥の伝播と効果的なアサーションも重要であり、これらの領域では両ツールとも課題に直面しています 40。

**表3：比較パフォーマンスメトリクスの概要（EvoSuite vs. Randoop）**

| メトリック | EvoSuite (研究参照) | Randoop (研究参照) |
| :---- | :---- | :---- |
| 平均コードカバレッジ (分岐/行 %) | 89% (分岐) 30 | 63% (分岐) 30 |
| 平均ミューテーションスコア (%) | 67% 30 | 50% 30 |
| 欠陥検出率 (例: X/Y件の欠陥) | 7/10件 30 | 5/10件 30 |
| 標準的な実行時間 (例: ベンチマークより) | 2時間51分 (55 CUTs, CUT毎120秒) 11 | 5時間35分 (55 CUTs, CUT毎120秒) 11 |
| 生成テスト数 (ベンチマークより) | 2,049件 (平均13.0/CUT) 11 | 1,561,533件 (平均9521.5/CUT) 11 |

### **4.2. テスト生成思想：テスト特性とユースケースへの影響**

EvoSuiteとRandoopの根本的な設計思想の違いは、生成されるテストの特性や最適なユースケースに大きな影響を与えます。

* **EvoSuite (検索ベース／進化的):**  
  * *思想:* 構造的なカバレッジ目標を最適化するテストスイートを系統的に探索します 3。  
  * *影響:* カバレッジのために高度に最適化され、可読性のために最小化されたテストを生成します。困難な分岐をカバーするために複雑なシーケンスを生成できます 3。  
  * *ユースケース:* 構造的カバレッジによる高い保証が求められるプロジェクト、振る舞いが明確に定義されたリグレッションテスト、カバレッジ義務のコンプライアンスチェック。  
* **Randoop (フィードバック指向ランダム):**  
  * *思想:* 多くの多様な（時には単純、時には複雑な）操作シーケンスを生成することでプログラムの振る舞いを探索し、有望でないパスを枝刈りするためのフィードバックを用います 5。  
  * *影響:* 契約をチェックし、観測された振る舞いを捉えるテストを生成します。ランダム性により、予期せぬ相互作用やエッジケースを発見できます。しばしば大量のテストを生成します 11。  
  * *ユースケース:* APIの誤用や契約違反に関連するバグの迅速な発見、現在の振る舞いを捉えるための広範なリグレッションテストの生成、ライブラリの探索的テスト。

これらの異なる思想は、ツールが純粋な競合相手というよりも補完的であることを意味します。EvoSuiteは、すべての設計図の線を検査しようとする几帳面なエンジニアに似ています。一方、Randoopは、機能や組み合わせをランダムに試す好奇心旺盛なユーザーのようです。プロジェクトは両方を使用すること、あるいは戦略を組み合わせたツール（Tackle-test 6 など）を使用することで恩恵を受ける可能性があります。EvoSuiteの系統的な検索は、既知のパスがテストされることを保証するのに強力です 7。Randoopのランダム性は、開発者が予期しなかった「未知の未知」の相互作用や入力を発見することができます 5。4545 のような研究は、異なるツールが異なる欠陥を発見することを示しており、補完性の議論を裏付けています。Toradocu 63 のような、EvoSuiteとRandoopの両方をオラクル改善によって強化するツールの存在は、テストエコシステムにおけるそれらの明確かつ価値ある役割をさらに示しています。

### **4.3. 実行環境と互換性：横並び比較**

**表2：実行環境互換性マトリクス（EvoSuite vs. Randoop）**

| 側面 | EvoSuite | Randoop |
| :---- | :---- | :---- |
| 最新確認済みJavaバージョンサポート | Java 9+ (v1.2.0, 2021年) 10, Java 8/11 (Docker) 3 | Java 20 (v4.3.3, 2024年) 51 |
| 主要OS互換性 | Mac, Linux, Windows 13 | Linux, macOS, Windows 52 |
| 公式IDEプラグイン | IntelliJ IDEA, Eclipse (実験的) 3 | なし (開発者向けIDE設定はあり 54) |
| 主要ビルドツール連携 | Maven (強力) 3, Gradle (サードパーティ) 21 | Gradle (自身のビルド用、実験的ユーザープラグイン) 4 |
| コマンドラインインターフェース | あり、主要な方法の一つ 3 | あり、主要な方法 47 |

Randoopは、最近のJavaバージョンに対してより一貫して最新の状態を保っているように見えます 10。両ツールともJavaベースであり、一般的にクロスプラットフォームです 13。IDE/ビルドツールの連携に関しては、EvoSuiteは強力なMavenサポートと優れたIntelliJ/Eclipseプラグインを備えています 3。一方、Randoopは主にコマンドラインで使用され、自身のビルドにはGradleを使用し、ユーザー向けの実験的なGradleプラグインがあります 4。依存関係については、両ツールともJUnitを必要とし、EvoSuiteは独自のevosuite-standalone-runtimeを持っています 4。

### **4.4. テスト品質と可読性：比較の観点**

* **EvoSuite:** 最小化 3 と最適化されたアサーションにより可読性を目指しています。SBFT 2025ではRandoopよりも可読性が高いと評価されました 11。しかし、複雑に最適化されたテストは依然として読みにくいことがあります 25。  
* **Randoop:** テストは些細であったり、非常に冗長で読みにくかったりすることがあります 2。テストの最小化を別のステップとして提供しています 47。  
* **一般的な懸念:** 可読性は、ほとんどの自動生成テストにとって既知の課題です 6。 EvoSuiteには可読性向上のための組み込みメカニズム（最小化）がありますが、Randoopのランダムな性質は、特定の契約違反に対して非常に単純で理解しやすいテストを生成することもあれば、逆に非常に長く曖昧なテストを生成することもあります。SBFT 2025の結果がEvoSuiteの可読性を支持している点は重要です 11。

### **4.5. パフォーマンスとスケーラビリティ：ベンチマークと所見**

* **EvoSuite:** 時間がかかる場合がありますが 24、SBFT 2025では、特定のCUT/時間予算に対してRandoopよりも少ない、よりターゲットを絞ったテストをより速く生成しました 11。そのパフォーマンスは調整可能です 20。  
* **Randoop:** 大量のテストを迅速に生成できますが 11、個々のテストの実行時間が終了しないテストの場合に問題となることがあります 59。 「パフォーマンス」は多面的です。Randoopは生のテスト*量*の生成では高速です。EvoSuiteは、より少数のテストに対して特定のカバレッジ目標を特定の時間内に達成するという点で、より「効率的」かもしれません。非常に大規模なプロジェクトへのスケーラビリティは両ツールにとって懸念事項であり、実行時間が主要な要因となります。

### **4.6. セットアップの容易さ、学習曲線、ユーザビリティ**

* **EvoSuite:** プラグイン設定や潜在的な競合のため、一般的にセットアップがより複雑であると考えられています 2。広範な設定オプションは圧倒される可能性があります 2。  
* **Randoop:** 基本的なコマンドラインの使用はより簡単です 2。 Randoopは初期の実験に対する障壁が低いかもしれませんが、EvoSuiteの連携オプションは、一度習得すれば、サポートされている環境（Mavenベースのプロジェクトなど）でよりシームレスなエクスペリエンスを提供する可能性があります。

### **4.7. 境界値および契約ベースのテスト能力**

* **EvoSuite:** ドキュメント 16 では、境界値テストに関する専用機能について明示的に詳述されていません。そのテスト生成は主にカバレッジ駆動です。契約遵守は、観測された振る舞いを捉えるアサーションを通じて、または特定のプロパティが適合度関数によってターゲットにされた場合（あまり一般的ではない）に行われます。  
* **Randoop:** Object契約のチェックを明示的にサポートしており 47、ユーザーがメソッド仕様（事前/事後条件、スロー条件）をJSON形式で提供してテスト生成と分類をガイドすることを可能にしています 47。-1、0、1のようなシード値を使用しますが 47、伝統的な意味での体系的な境界値分析を自動的に実行するわけではありません。ユーザーは関連する境界リテラルを提供するか、仕様でそれらを定義する必要があります。 Randoopは、契約ベースのテストに対してより明示的でユーザー設定可能な機能を備えています。EvoSuiteは、暗黙的に正しい振る舞いを処理するために、一般的な検索とアサーション生成により依存しています。どちらのツールも、ユーザーがこれらの境界を指定しない限り、高度な境界値*分析*を標準で提供しているようには見えません。

## **5\. ツール選択における実用的な考慮事項**

### **5.1. プロジェクトニーズへのツール強みの適合**

* **高いカバレッジ要件:** 主要な目標が構造的カバレッジを高く達成することである場合（例：コンプライアンス、クリティカルシステム）、EvoSuiteの検索ベースのアプローチがより適している可能性が高いです 3。  
* **迅速なバグ発見とAPI探索:** 契約違反、予期せぬ例外、またはAPIの振る舞いを迅速に発見することが目標である場合、Randoopのランダムアプローチが初期にはより速い結果をもたらす可能性があります 5。  
* **新規コード vs. レガシーコード:** TDDで開発された新規コードの場合、Randoopのリグレッションテストは初期の振る舞いを捉えることができます。カバレッジの低いレガシーコードの場合、EvoSuiteを使用してテストスイートをブートストラップできます。

### **5.2. チームの専門知識とリソースの可用性**

* **学習曲線:** Randoopは、より単純なコマンドライン操作のため、初期使用が容易かもしれません 2。EvoSuiteの広範な設定オプションと潜在的なセットアップの複雑さは、より多くの学習を必要とする場合があります 2。  
* **テスト生成時間:** CI/CDで利用可能な時間を考慮してください。EvoSuiteはより短い実行時間で設定できますが、詳細な検索には時間がかかります 20。Randoopの時間制限は直接的な制御です 47。

### **5.3. 既存の開発およびCI/CDワークフローへの統合**

* **ビルドシステム:** EvoSuiteは強力なMavenサポートを持っています 3。RandoopはGradleと統合します（自身のビルド用およびコミュニティプラグイン経由）54。Maven経由のEvoSuiteのCI/CD統合は十分に文書化されています 3。Randoopの場合、これは通常、コマンドライン呼び出しのスクリプト作成を伴います 47。  
* **テストメンテナンス:** 生成されたテストの可読性と安定性は非常に重要です。両ツールとも課題がありますが、EvoSuiteの最小化とSBFT 2025の可読性の結果 3 は、維持されるならば優位性をもたらす可能性があります。Randoopの多数の潜在的に些細なテスト 11 はメンテナンスを増加させる可能性があります。

### **5.4. コミュニティサポートと長期的な実行可能性**

* 両方とも学術的なルーツを持つオープンソースです 2。  
* スニペットの日付に基づくと、Randoopの方が最近のリリースとJavaバージョンの更新が多いように見えます 10。  
* ドキュメント、メーリングリスト 53、課題追跡システム 53 の利用可能性は重要です。

ツールの選択は単に技術的な特徴だけでなく、チームが採用したい「テスト哲学」にも関わります。既知のコードパスの厳密で体系的なカバレッジを優先するチームはEvoSuiteに傾倒するかもしれません。APIにおける予期せぬ振る舞いの迅速な発見や、振る舞いテストのベースラインを迅速に生成する必要があるチームはRandoopを好むかもしれません。「最適な」ツールは非常に状況に依存します。EvoSuiteの設計は、詳細で最適化された構造テストの哲学を反映しています 7。Randoopの設計は、広範なランダムな振る舞いの探索と契約強制の哲学を反映しています 5。プロジェクトの制約（時間、専門知識、既存のコード品質、特定のテスト目標など、これらのツールにとって主要ではないセキュリティやパフォーマンスなど）は、どの哲学がより有益であるかに大きく影響します。4545 の「万能薬はない」という発見は、単一のツール/アプローチがすべてのニーズをカバーすることはめったにないことを補強しています。

## **6\. まとめと推奨事項**

### **6.1. 主要な違い、長所、短所の要約**

EvoSuiteとRandoopは、Javaユニットテストの自動生成においてそれぞれ独自のアプローチと強みを持つツールです。EvoSuiteは進化的アルゴリズムを用いて構造的カバレッジの最大化を目指し、特にMaven環境との親和性が高いです。一方、Randoopはフィードバック指向のランダムテスト生成により、契約違反や予期せぬ振る舞いの発見に長け、コマンドラインでの手軽な利用が可能です。

**表4：EvoSuiteとRandoopの長所と短所の集約**

| ツール | 長所 | 短所 |
| :---- | :---- | :---- |
| **EvoSuite** | 高い構造的カバレッジ達成 30\<br\>強力なMaven連携 17\<br\>テストの最小化機能 3\<br\>効果的な欠陥検出 30 | セットアップの複雑さ 2\<br\>詳細な検索には時間がかかる 24\<br\>Javaバージョンサポートの遅れの可能性 14\<br\>環境依存性のあるコードの扱いの難しさ 9 |
| **Randoop** | 契約違反の発見に強い 47\<br\>基本的なセットアップが比較的容易 2\<br\>最新Javaバージョンへの良好な対応 51\<br\>多様なテストを大量に生成 11 | 構造的カバレッジはEvoSuiteに劣る傾向 30\<br\>テストの可読性が低い場合がある 25\<br\>ランダム性により特定のバグを見逃す可能性 2\<br\>パフォーマンスの頭打ちの可能性 56 |

### **6.2. 適切なツールの選択に関するガイダンス**

* **シナリオ1：成熟したプロジェクトにおける構造的カバレッジの最大化:** EvoSuiteが推奨されます。  
* **シナリオ2：ライブラリにおけるAPI誤用と契約バグの迅速な発見:** 初期にはRandoopがより効果的である可能性があります。  
* **シナリオ3：レガシーコードのテストのブートストラップ:** EvoSuiteは包括的なベースラインを生成できます。  
* **シナリオ4：最新JavaとGradleを使用するプロジェクト:** Randoopの方が環境統合がスムーズかもしれません。  
* **シナリオ5：初期セットアップの容易さを優先するチーム:** Randoopのコマンドラインのシンプルさは利点です。

### **6.3. 組み合わせアプローチの可能性**

Tackle-test 6 のように両方の戦略を活用するツールや、Toradocu 63 のように両ツールを強化できるツールの存在は、将来的にハイブリッドアプローチやツールチェーンがより一般的になることを示唆しています。

### **6.4. Javaユニットテスト自動生成の今後の展望**

可読性の向上、不安定性の削減、AI/LLMの統合（これらの特定ツールの現在の情報源に基づくコアメカニズム外ではありますが、40は一般的にテスト生成のためのLLMに言及し、11はコンペティションでの可読性評価にLLMを使用）に関する研究が進行中です。これらの進展は、自動テスト生成ツールが開発者のワークフローによりシームレスに統合され、さらに高品質なテストを効率的に提供できるようになる未来を示唆しています。

#### **引用文献**

1. Unit Test Generation During Software Development: EvoSuite Plugins for Maven, IntelliJ and Jenkins \- White Rose Research Online, 6月 5, 2025にアクセス、 [https://eprints.whiterose.ac.uk/id/eprint/116455/1/paper\_tool.pdf](https://eprints.whiterose.ac.uk/id/eprint/116455/1/paper_tool.pdf)  
2. Revolutionising Java Development: Exploring AI's Role in Enhancing Regression and End-to-End Testing alongside BDD \- Estafet, 6月 5, 2025にアクセス、 [https://estafet.com/revolutionising-java-development-exploring-ais-role-in-enhancing-regression-and-end-to-end-testing-alongside-bdd-an-overview-and-analysis-of-emerging-tools-and-techniques/](https://estafet.com/revolutionising-java-development-exploring-ais-role-in-enhancing-regression-and-end-to-end-testing-alongside-bdd-an-overview-and-analysis-of-emerging-tools-and-techniques/)  
3. EvoSuite/evosuite: EvoSuite \- automated generation of ... \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/EvoSuite/evosuite](https://github.com/EvoSuite/evosuite)  
4. randoop/README.md at master \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/randoop/randoop/blob/master/README.md](https://github.com/randoop/randoop/blob/master/README.md)  
5. Automatic unit test generation for Java \- Randoop, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/](https://randoop.github.io/randoop/)  
6. Use this open source tool for automated unit testing Opensource.com, 6月 5, 2025にアクセス、 [https://opensource.com/article/21/8/tackle-test](https://opensource.com/article/21/8/tackle-test)  
7. Whole Test Suite Generation \- EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/wp-content/papercite-data/pdf/tse12\_evosuite.pdf](https://www.evosuite.org/wp-content/papercite-data/pdf/tse12_evosuite.pdf)  
8. Evolutionary Generation of Whole Test Suites \- Computer Science (CS), 6月 5, 2025にアクセス、 [https://courses.cs.vt.edu/cs6704/spring21/presentations/CS6704\_EVOSUITE.pdf](https://courses.cs.vt.edu/cs6704/spring21/presentations/CS6704_EVOSUITE.pdf)  
9. www.evosuite.org, 6月 5, 2025にアクセス、 [https://www.evosuite.org/wp-content/papercite-data/pdf/tosem\_evaluation.pdf](https://www.evosuite.org/wp-content/papercite-data/pdf/tosem_evaluation.pdf)  
10. Releases · EvoSuite/evosuite \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/EvoSuite/evosuite/releases](https://github.com/EvoSuite/evosuite/releases)  
11. SBFT Tool Competition 2025 \- Java Test Case Generation Track \- arXiv, 6月 5, 2025にアクセス、 [https://arxiv.org/html/2504.09168v1](https://arxiv.org/html/2504.09168v1)  
12. arxiv.org, 6月 5, 2025にアクセス、 [https://arxiv.org/pdf/2504.09168](https://arxiv.org/pdf/2504.09168)  
13. Downloads EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/downloads/](https://www.evosuite.org/downloads/)  
14. Porting EvoSuite to java 17? \- unit testing \- Stack Overflow, 6月 5, 2025にアクセス、 [https://stackoverflow.com/questions/77452158/porting-evosuite-to-java-17](https://stackoverflow.com/questions/77452158/porting-evosuite-to-java-17)  
15. Actions · EvoSuite/evosuite-coverage-tools \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/EvoSuite/evosuite-coverage-tools/actions](https://github.com/EvoSuite/evosuite-coverage-tools/actions)  
16. Documentation EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/](https://www.evosuite.org/documentation/)  
17. Maven plugin EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/maven-plugin/](https://www.evosuite.org/documentation/maven-plugin/)  
18. IntelliJ IDEA plugin \- EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/intellij-idea-plugin/](https://www.evosuite.org/documentation/intellij-idea-plugin/)  
19. This is a tutorial for EvoSuite on IDEA \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/zhiyufan/EvoSuite-IDEA](https://github.com/zhiyufan/EvoSuite-IDEA)  
20. Commandline EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/commandline/](https://www.evosuite.org/documentation/commandline/)  
21. LajosCseppento/gradle-evosuite-plugin: Gradle plugin for ... \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/LajosCseppento/gradle-evosuite-plugin](https://github.com/LajosCseppento/gradle-evosuite-plugin)  
22. Measuring Code Coverage EvoSuite, 6月 5, 2025にアクセス、 [https://www.evosuite.org/documentation/measuring-code-coverage/](https://www.evosuite.org/documentation/measuring-code-coverage/)  
23. Advanced Software Quality \- EvoSuite \- YouTube, 6月 5, 2025にアクセス、 [https://www.youtube.com/watch?v=uv4DD9SpVeo](https://www.youtube.com/watch?v=uv4DD9SpVeo)  
24. Homework 4: Generating Tests with EvoSuite CS 684 (Sp24), 6月 5, 2025にアクセス、 [https://kelloggm.github.io/martinjkellogg.com/teaching/cs684-sp24/projects/hw4.html](https://kelloggm.github.io/martinjkellogg.com/teaching/cs684-sp24/projects/hw4.html)  
25. Test Generation in Java \- an Overview, 6月 5, 2025にアクセス、 [http://www.amygdalum.net/en/testgenerators-a-detailed-overview.html](http://www.amygdalum.net/en/testgenerators-a-detailed-overview.html)  
26. Unlogged: The Best Choice Among the Regression Testing Tools for ..., 6月 5, 2025にアクセス、 [https://www.reddit.com/r/Unlogged/comments/15f43jj/unlogged\_the\_best\_choice\_among\_the\_regression/](https://www.reddit.com/r/Unlogged/comments/15f43jj/unlogged_the_best_choice_among_the_regression/)  
27. (PDF) Classifying generated white-box tests: an exploratory study, 6月 5, 2025にアクセス、 [https://www.researchgate.net/publication/333164293\_Classifying\_generated\_white-box\_tests\_an\_exploratory\_study](https://www.researchgate.net/publication/333164293_Classifying_generated_white-box_tests_an_exploratory_study)  
28. Tests4J Benchmark: Execution-based Evaluation of Context-Aware Language Models for Test Case Generation, 6月 5, 2025にアクセス、 [https://elib.uni-stuttgart.de/bitstreams/ac90426a-b71f-4010-938c-4c332b4b44ec/download](https://elib.uni-stuttgart.de/bitstreams/ac90426a-b71f-4010-938c-4c332b4b44ec/download)  
29. elib.uni-stuttgart.de, 6月 5, 2025にアクセス、 [https://elib.uni-stuttgart.de/server/api/core/bitstreams/ac90426a-b71f-4010-938c-4c332b4b44ec/content](https://elib.uni-stuttgart.de/server/api/core/bitstreams/ac90426a-b71f-4010-938c-4c332b4b44ec/content)  
30. lnu.diva-portal.org, 6月 5, 2025にアクセス、 [http://lnu.diva-portal.org/smash/get/diva2:1764443/FULLTEXT01.pdf](http://lnu.diva-portal.org/smash/get/diva2:1764443/FULLTEXT01.pdf)  
31. jcst.ict.ac.cn, 6月 5, 2025にアクセス、 [https://jcst.ict.ac.cn/fileup/1000-9000/PDF/JCST-2024-3-11-1935-715.pdf](https://jcst.ict.ac.cn/fileup/1000-9000/PDF/JCST-2024-3-11-1935-715.pdf)  
32. dl.acm.org, 6月 5, 2025にアクセス、 [https://dl.acm.org/doi/abs/10.1145/3340433.3342824](https://dl.acm.org/doi/abs/10.1145/3340433.3342824)  
33. ieeexplore.ieee.org, 6月 5, 2025にアクセス、 [https://ieeexplore.ieee.org/document/8094424](https://ieeexplore.ieee.org/document/8094424)  
34. 1月 1, 1970にアクセス、 [https://dl.acm.org/doi/pdf/10.1145/3340433.3342824](https://dl.acm.org/doi/pdf/10.1145/3340433.3342824)  
35. 1月 1, 1970にアクセス、 [https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8094424](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8094424)  
36. 1月 1, 1970にアクセス、 [https://www.researchgate.net/publication/336226803\_Evaluating\_Test\_Suite\_Readability\_with\_Human\_Assessment\_and\_Readability\_Metrics](https://www.researchgate.net/publication/336226803_Evaluating_Test_Suite_Readability_with_Human_Assessment_and_Readability_Metrics)  
37. 1月 1, 1970にアクセス、 [https://www.researchgate.net/publication/319333934\_Are\_automatically\_generated\_test\_cases\_readable\_An\_empirical\_study\_of\_the\_readability\_of\_tests\_generated\_by\_Randoop\_and\_EvoSuite](https://www.researchgate.net/publication/319333934_Are_automatically_generated_test_cases_readable_An_empirical_study_of_the_readability_of_tests_generated_by_Randoop_and_EvoSuite)  
38. 1月 1, 1970にアクセス、 [https://scholar.google.com/scholar?q=%22Evaluating+Test+Suite+Readability+with+Human+Assessment+and+Readability+Metrics%22](https://scholar.google.com/scholar?q=%22Evaluating+Test+Suite+Readability+with+Human+Assessment+and+Readability+Metrics%22)  
39. 1月 1, 1970にアクセス、 [https://scholar.google.com/scholar?q=%22Are+automatically+generated+test+cases+readable%3F+An+empirical+study+of+the+readability+of+tests+generated+by+Randoop+and+EvoSuite%22](https://scholar.google.com/scholar?q=%22Are+automatically+generated+test+cases+readable?+An+empirical+study+of+the+readability+of+tests+generated+by+Randoop+and+EvoSuite%22)  
40. Addressing EvoSuite's Limitations: Method-Specific Test Case Generation and Execution in Controlled Environments \- ThinkMind, 6月 5, 2025にアクセス、 [https://www.thinkmind.org/articles/valid\_2024\_1\_40\_40010.pdf](https://www.thinkmind.org/articles/valid_2024_1_40_40010.pdf)  
41. Homework Assignment \#2 — Test Automation, 6月 5, 2025にアクセス、 [https://web.eecs.umich.edu/\~weimerw/2022-481F/hw2.html](https://web.eecs.umich.edu/~weimerw/2022-481F/hw2.html)  
42. Comparative Analysis of Automated Test Case ... \- DiVA portal, 6月 5, 2025にアクセス、 [https://www.diva-portal.org/smash/get/diva2:1942973/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1942973/FULLTEXT01.pdf)  
43. Empirical Comparison Between Conventional and AI-based Automated Unit Test Generation Tools in Java \- DiVA, 6月 5, 2025にアクセス、 [http://lnu.diva-portal.org/smash/record.jsf?pid=diva2:1764443](http://lnu.diva-portal.org/smash/record.jsf?pid=diva2:1764443)  
44. Bachelor Degree Project Empirical Comparison Between Conventional and AI-based Automated Unit Test Generation Tools in Java, 6月 5, 2025にアクセス、 [https://fardapaper.ir/mohavaha/uploads/2023/09/5-Empirical-Comparison-Between-Conventional-and-AI-based-Automated-Unit-Test-Generation-Tools-in-Java.pdf](https://fardapaper.ir/mohavaha/uploads/2023/09/5-Empirical-Comparison-Between-Conventional-and-AI-based-Automated-Unit-Test-Generation-Tools-in-Java.pdf)  
45. www.evosuite.org, 6月 5, 2025にアクセス、 [https://www.evosuite.org/wp-content/papercite-data/pdf/ase15\_faults.pdf](https://www.evosuite.org/wp-content/papercite-data/pdf/ase15_faults.pdf)  
46. www.evosuite.org, 6月 5, 2025にアクセス、 [https://www.evosuite.org/wp-content/papercite-data/pdf/fse21\_objectseed.pdf](https://www.evosuite.org/wp-content/papercite-data/pdf/fse21_objectseed.pdf)  
47. Randoop Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/](https://randoop.github.io/randoop/manual/)  
48. Feedback-directed Random Test Generation \- Microsoft, 6月 5, 2025にアクセス、 [https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/randoop-tr.pdf](https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/randoop-tr.pdf)  
49. Automated Unit Testing with Randoop, JWalk and µJava versus Manual JUnit Testing, 6月 5, 2025にアクセス、 [https://staffwww.dcs.shef.ac.uk/people/A.Simons/research/reports/jwalksmeets.pdf](https://staffwww.dcs.shef.ac.uk/people/A.Simons/research/reports/jwalksmeets.pdf)  
50. Randoop Tutorial PDF PDF Software Bug Java (Programming ..., 6月 5, 2025にアクセス、 [https://fr.scribd.com/document/466706998/randoop-tutorial-pdf](https://fr.scribd.com/document/466706998/randoop-tutorial-pdf)  
51. Releases · randoop/randoop \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/randoop/randoop/releases](https://github.com/randoop/randoop/releases)  
52. Actions · randoop/tutorial-examples \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/randoop/tutorial-examples/actions](https://github.com/randoop/tutorial-examples/actions)  
53. Using Randoop To Generate Test Cases (Based on Pre- and Post- Conditions), 6月 5, 2025にアクセス、 [https://stackoverflow.com/questions/54612864/using-randoop-to-generate-test-cases-based-on-pre-and-post-conditions](https://stackoverflow.com/questions/54612864/using-randoop-to-generate-test-cases-based-on-pre-and-post-conditions)  
54. Randoop Developer's Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/dev.html](https://randoop.github.io/randoop/manual/dev.html)  
55. SRI-CSL/randoop-gradle-plugin: (experimental) randoop ... \- GitHub, 6月 5, 2025にアクセス、 [https://github.com/SRI-CSL/randoop-gradle-plugin](https://github.com/SRI-CSL/randoop-gradle-plugin)  
56. Feedback-directed Random Test Generation \- Randoop, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/files/randoop\_case\_study\_2008.ppt](https://randoop.github.io/randoop/files/randoop_case_study_2008.ppt)  
57. randoop / coverage-tools · GitLab, 6月 5, 2025にアクセス、 [https://gitlab.cs.washington.edu/randoop/coverage-tools](https://gitlab.cs.washington.edu/randoop/coverage-tools)  
58. An Experimental Study on Flakiness and Fragility of Randoop Regression Test Suites, 6月 5, 2025にアクセス、 [https://www.researchgate.net/publication/335967914\_An\_Experimental\_Study\_on\_Flakiness\_and\_Fragility\_of\_Randoop\_Regression\_Test\_Suites](https://www.researchgate.net/publication/335967914_An_Experimental_Study_on_Flakiness_and_Fragility_of_Randoop_Regression_Test_Suites)  
59. Randoop project ideas, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/projectideas.html](https://randoop.github.io/randoop/projectideas.html)  
60. Randoop Manual, 6月 5, 2025にアクセス、 [https://randoop.github.io/randoop/manual/index.html\#specifying-expected-code-behavior](https://randoop.github.io/randoop/manual/index.html#specifying-expected-code-behavior)  
61. A Large Scale Study On the Effectiveness of Manual and Automatic Unit Test Generation \- Beatriz Souza, 6月 5, 2025にアクセス、 [https://biabs1.github.io/publications/SBES-2020.pdf](https://biabs1.github.io/publications/SBES-2020.pdf)  
62. Bachelor Degree Project Empirical Comparison Between Conventional and AI-based Automated Unit Test Generation Tools in Java \- DiVA portal, 6月 5, 2025にアクセス、 [https://www.diva-portal.org/smash/get/diva2:1764443/FULLTEXT01.pdf](https://www.diva-portal.org/smash/get/diva2:1764443/FULLTEXT01.pdf)  
63. Automatic Generation of Oracles for Exceptional Behaviors \- The IMDEA Software Institute, 6月 5, 2025にアクセス、 [https://software.imdea.org/\~alessandra.gorla/papers/Goffi-Toradocu-ISSTA16.pdf](https://software.imdea.org/~alessandra.gorla/papers/Goffi-Toradocu-ISSTA16.pdf)  
64. 1月 1, 1970にアクセス、 [https://www.evosuite.org/documentation/tutorial-part-4-extending-evosuite/](https://www.evosuite.org/documentation/tutorial-part-4-extending-evosuite/)  
65. 1月 1, 1970にアクセス、 [https://www.evosuite.org/documentation/master/cfg/](https://www.evosuite.org/documentation/master/cfg/)  
