---
layout: topic
title: "JaCoCoコードカバレッジライブラリの包括的な技術分析"
date: 2025-06-18
prompt: "JaCoCoの技術的な調査を行いたい。どの様にカバレッジを計測しているのか、精度や懸念など多角的に調べて欲しい。"
category: "engineering"
tags: [開発環境]
audio: "/share-deepresearch/assets/audio/jacoco.mp3"
supplementary_materials:
  - title: "JaCoCo技術調査インフォグラフィック"
    url: "/share-deepresearch/topics/jacoco/infographic.html"
  - title: "JaCoCoを使いこなすための技術深掘りとベストプラクティス"
    url: "/share-deepresearch/topics/jacoco/reveal.html"
---

# **JaCoCoコードカバレッジライブラリの包括的な技術分析**

## **エグゼクティブサマリー**

本レポートは、Javaエコシステムにおけるコードカバレッジ計測のデファクトスタンダードであるJaCoCo（Java Code Coverage Library）について、その技術的側面を多角的に掘り下げた包括的な分析を提供する。JaCoCoの核となる技術は、Javaエージェントを利用した「オンザフライ」でのバイトコードインスツルメンテーションであり、これによりソースコードへのアクセスなしにコード実行を追跡する柔軟性と、ビルドプロセスへの容易な統合を実現している。

本分析では、まずJaCoCoがどのようにしてバイトコードを解析し、制御フローグラフを構築し、最小限のプローブを挿入することで実行情報を収集するのか、その精緻な内部メカニズムを解明する。命令（C0）、分岐（C1）、サイクロマティック複雑度といったバイトコードレベルの指標から、行、メソッド、クラスといったソースコードレベルの指標まで、JaCoCoが提供する各カバレッジメトリクスの正確な定義と計算方法を詳述し、特に論理的な網羅性を示す分岐カバレッジの重要性を強調する。

しかし、JaCoCoの強力な低レベルアプローチは、現代のソフトウェア開発がもたらす複雑性と常に緊張関係にある。本レポートでは、その精度と信頼性に関する重要な懸念事項を詳細に検討する。特に、Javaのtry-with-resources構文やKotlinのコルーチン、ラムダ式など、コンパイラが生成する複雑なバイトコードが、どのようにしてカバレッジレポートの「不正確さ」を引き起こすのかをケーススタディを通じて明らかにする。また、PowerMockのような他のバイトコード操作ツールとの深刻な互換性問題や、リフレクション使用時の注意点についても論じる。

さらに、パフォーマンスの観点から、一般的なユースケースでは軽微とされるオーバーヘッドが、高並行性を持つアプリケーションにおいてはCPUのキャッシュコンテンションを引き起こし、実行時間が10倍以上にも悪化しうるという重大なボトルネックを特定する。

最後に、これらの技術的背景を踏まえ、CI/CDパイプラインへの戦略的な統合方法を提案する。単なるカバレッジ率の追求がもたらす「100%カバレッジの幻想」を避け、Pull Requestにおける変更差分のみを対象とする「Diff Coverage」を品質ゲートとして運用することが、現代の開発ワークフローにおいて最も効果的であることを示す。本レポートは、開発者、アーキテクト、品質保証担当者がJaCoCoを最大限に活用し、その潜在的な落とし穴を回避するための技術的指針となることを目指すものである。

---

## **1\. JaCoCoのコアメカニズム：オンザフライ・バイトコードインスツルメンテーション**

JaCoCoの能力と限界を理解するための第一歩は、その根幹をなす技術、すなわちバイトコードインスツルメンテーションの仕組みを解明することである。JaCoCoはソースコードを直接解析するのではなく、コンパイル後のJavaバイトコードを対象とすることで、言語からの独立性と高い柔軟性を獲得している。

### **1.1. Javaエージェント：オンザフライ vs オフラインインスツルメンテーション**

JaCoCoは主に二つのインスツルメンテーション方式を提供するが、その中心的なアプローチは「オンザフライ」方式である 1。

* **オンザフライ・インスツルメンテーション**: これはJaCoCoが推奨する主要な動作モードである 1。JVMの起動時に  
  \-javaagentフラグを用いてJaCoCoエージェント（jacocoagent.jar）をアタッチすることで実現される 2。このエージェントは、クラスローダーがクラスをメモリにロードする瞬間に、そのバイトコードを動的に書き換える 3。この方式の最大の利点は、ディスク上の  
  .classファイルが一切変更されないことである 1。そのため、ビルドプロセスが簡素化され、Coberturaや古いEmmaのようなツールで必要だった事前のインスツルメンテーション工程や複雑なクラスパスの調整が不要になる 1。  
* **オフライン・インスツルメンテーション**: これは、Javaエージェントが使用できない特殊な環境、特にAndroidプラットフォームでの実行を主目的とした代替手段である 1。このモードでは、ビルド時にあらかじめクラスファイルをインスツルメントし、変更されたクラスファイルを最終的なアプリケーションにパッケージングする。

エージェントはテスト実行中にカバレッジ情報を収集し、JVMの終了時、またはTCPサーバーを介した外部からの要求に応じて、その結果をバイナリファイル（通常はjacoco.exec）に出力する 4。

### **1.2. バイトコード解析：制御フローグラフとプローブ挿入戦略**

JaCoCoの解析は、ソースコードではなく、コンパイル済みのJavaバイトコードに対して行われる 9。このアプローチにより、KotlinやScalaなど、JVMバイトコードにコンパイルされるあらゆる言語で利用可能となっている 11。

* **制御フローグラフ（CFG）の構築**: JaCoCoは各メソッドのバイトコードを読み込み、内部的に制御フローグラフを構築する。このグラフでは、各バイトコード命令がノードとなり、GOTOやIFEQ（if-equal）のようなジャンプ命令によって表現される実行可能な経路がエッジとなる 9。  
* **最小プローブ挿入戦略**: CFGのすべてのエッジに実行記録用のコード（プローブ）を挿入すると、クラスファイルのサイズが肥大化し、実行速度が著しく低下する。これを避けるため、JaCoCoは非常に洗練された最小プローブ挿入戦略を採用している 9。この戦略では、キーとなるポイントにのみプローブを配置し、そこから他の命令や分岐の実行状態を推測する 9。具体的には、プローブは以下の場所に挿入される。  
  1. メソッドが終了するすべての箇所（return命令または例外スロー）  
  2. 複数のエッジが合流する命令の直前の各エッジ 9

この最適化により、JaCoCoは一般的に低いパフォーマンスオーバーヘッドを実現している。条件分岐の場合、JaCoCoは条件ジャンプ命令のロジックを反転させ、その直後にプローブを挿入し、その後GOTO命令で元のジャンプ先に飛ぶという手法で分岐を計測する 9。

### **1.3. プローブの実装：boolean配列による実行記録**

プローブは、コードの特定の部分が実行されたことを記録するための、メソッドに挿入される短いバイトコードシーケンスである 9。

JaCoCoのプローブ実装は、効率性とスレッドセーフティを両立させている。各クラスには、インスツルメンテーションによってプライベートかつ静的なboolean型の配列が追加される 9。クラス内の各プローブは、この配列の特定のインデックスに対応付けられる。

プローブが実行されると、以下の4つの単純なバイトコード命令によって、対応する配列要素がtrueに設定される。  
ALOAD probearray, xPUSH probeid, ICONST\_1, BASTORE  
この操作はアトミックではないが、一度trueになった値は変わらないため、複数スレッドから同時に書き込みが発生しても競合状態にはならず、実質的にスレッドセーフである 9。  
このプローブ配列への参照を取得するため、すべての非インターフェースクラスには$jacocoinit()という合成静的メソッドが追加され、各メソッドの冒頭で呼び出される 9。

### **1.4. データ収集とレポート生成**

テストが実行されると、通過したプローブに対応するboolean配列のフラグがtrueに設定される。テスト実行後、mvn jacoco:dumpコマンドやJVM終了時のフックによって、JaCoCoエージェントはこれらのプローブ配列の状態をjacoco.execというバイナリファイルに書き出す 2。

人間が読める形式のレポート（HTML, XML, CSV）は、mvn jacoco:reportのような別のゴールで生成される 12。このレポート生成プロセスには、以下の3つの情報が不可欠である。

1. 実行データ（jacoco.exec）  
2. テスト実行時に使用されたものと**全く同じ**バージョンの、インスツルメントされていない.classファイル  
3. ソースコードの行ごとのハイライト表示を行うための、オリジナルの.javaソースファイル（オプション） 2

ここで重要なのは、ランタイムで使用されたクラスファイルとレポート生成時に提供されるクラスファイルが一致している必要があるという点である。もしクラスのバージョンが異なると、JaCoCoは実行データとクラスファイルを正しくマッピングできず、カバレッジが0%として報告されることになる 15。

このアーキテクチャは、JaCoCoの強力さとその限界の両方を規定している。バイトコードを直接操作することで、言語非依存性とビルドツールへの容易な統合を実現している。しかし、それは同時に、JaCoCoがソースコードのセマンティクスを理解せず、あくまでコンパイラが生成した最終的なバイトコードの構造しか見ていないことを意味する。この「コンパイラに対するブラックボックス」という性質が、JavaやKotlinの現代的な言語機能によって生成される複雑なバイトコードと組み合わさったときに、セクション3で詳述するような「精度の問題」の根本原因となる。開発者のソースコードに対するメンタルモデルと、JaCoCoが観測するバイトコードの実行状態との間に生じるこの乖離こそが、JaCoCoを効果的に利用する上で最も理解すべき核心的な概念である。

---

## **2\. JaCoCoのカバレッジメトリクスの詳細な解説**

JaCoCoは、テストスイートがコードベースのどの部分を実行したかを定量化するために、複数のメトリクスを提供する。これらのメトリクスを正確に理解することは、カバレッジレポートから意味のある洞察を引き出し、品質向上のための具体的なアクションを導き出す上で不可欠である。

### **2.1. 基本カウンターの定義：命令（C0）、分岐（C1）、サイクロマティック複雑度**

JaCoCoのすべてのメトリクスは、バイトコードレベルで収集される基本的なカウンターから派生する。

* **命令カバレッジ（Instructions, C0 Coverage）**: これはJaCoCoが計測する最も基本的な単位であり、個々のJavaバイトコード命令の実行有無を追跡する 16。このメトリクスは、ソースコードのフォーマットや、デバッグ情報（行番号テーブル）の有無に依存せず、常に利用可能である 16。JVMによって物理的に実行されたコード量を最も純粋に反映する指標と言える。  
* **分岐カバレッジ（Branches, C1 Coverage）**: JaCoCoは、すべてのif文およびswitch文を「分岐」としてカウントする。メソッド内の分岐の総数と、そのうち実行された分岐の数を計測する 16。ここで極めて重要な点は、JaCoCoの定義では、  
  **例外処理（try-catchブロック）は分岐としてカウントされない**ことである 16。この仕様を理解していないと、レポートの解釈を誤る可能性がある。  
* **サイクロマティック複雑度（Cyclomatic Complexity）**: このメトリクスは、メソッドの制御フローグラフにおける独立した実行パスの数を表し、コードの構造的な複雑さを示す 16。McCabeの定義に基づき、JaCoCoは分岐数（B）と決定点数（D）を用いて  
  v(G)=B−D+1 という等価な式で計算する 16。さらに、JaCoCoは「カバーされた複雑度」と「未カバーの複雑度」も報告する。後者は、そのメソッドを完全にテストするために、あとどれだけの独立したテストケースが必要かを示唆する指標となる 16。

### **2.2. ソースコードへのマッピング：行、メソッド、クラスカバレッジ**

バイトコードレベルのカウンターは、デバッグ情報が存在する場合、ソースコード上のエンティティに対応付けられる。

* **行カバレッジ（Line Coverage）**: このメトリクスは、クラスファイルがデバッグ情報（特にソースファイル名と行番号テーブル）付きでコンパイルされている場合にのみ計算可能である 14。ソースコードの特定の行は、その行に対応付けられたバイトコード命令が少なくとも1つ実行された場合に「カバーされた」と見なされる 16。1行のソースコードは複数のバイトコード命令にコンパイルされることが多いため、JaCoCoのレポートでは行ごとに3つの状態が示される 16。  
  * **緑色（Full Coverage）**: その行のすべての命令が実行された。  
  * **黄色（Partial Coverage）**: その行の命令の一部のみが実行された（例：三項演算子の一方の分岐のみが実行された）。  
  * **赤色（No Coverage）**: その行の命令が全く実行されなかった。  
* **メソッドカバレッジ（Method Coverage）**: メソッドは、その内部のバイトコード命令が少なくとも1つ実行された場合に「カバーされた」と見なされる。JaCoCoは、通常のメソッドだけでなく、コンストラクタ（\<init\>）や静的初期化子（\<clinit\>）もメソッドとしてカウントする 16。  
* **クラスカバレッジ（Class Coverage）**: クラスは、そのクラスに属するメソッドのいずれか1つ（コンストラクタや静的初期化子を含む）が実行された場合に「カバーされた」と見なされる 16。

### **2.3. ビジュアルレポートの解釈：色と記号のガイド**

JaCoCoが生成するHTMLレポートは、カバレッジの状態を直感的に理解できるよう、色と記号を効果的に使用している 7。

* **背景色（行カバレッジ）**: 前述の通り、行の背景色は行カバレッジの状態（緑：完全、黄：部分的、赤：未カバー）を示す 16。  
* **ひし形（ダイヤモンド）記号（分岐カバレッジ）**: if文やswitch文など、条件分岐を含む行の横に表示される。  
  * **緑色のひし形**: その行のすべての分岐が実行されたことを示す。  
  * **黄色のひし形**: 分岐の一部のみが実行されたことを示す（例：if文は実行されたがelse文は実行されなかった）。  
  * **赤色のひし形**: その行の分岐が全く実行されなかったことを示す 16。

これらの視覚的要素は、テストが不足している箇所を特定するための強力な手がかりとなる。

| メトリクス名 | 定義 | 計算基盤 | 実用的な意義・解釈 | 主要な限界 |
| :---- | :---- | :---- | :---- | :---- |
| **命令 (C0)** | 実行されたバイトコード命令の割合。 | バイトコード命令 | 最も正確で基本的な実行の証跡。ソースの書式やコンパイラの挙動に影響されない。 | 開発者が直接意識する単位ではなく、直感的ではない。 |
| **分岐 (C1)** | 実行された条件分岐（if/switch）の経路の割合。 | 制御フローグラフのエッジ | コードの論理的な網羅性を示す最も重要な指標の一つ。未実行の分岐はテストケースの欠落を直接示す。 | JaCoCoの定義では例外処理は分岐に含まれない 16。コンパイラ生成の分岐がノイズになることがある。 |
| **サイクロマティック複雑度** | コードの構造的な複雑さを示す指標。 | 分岐数と決定点数 | 完全にカバーするために必要な最小テストケース数を示唆する。「未カバーの複雑度」は追加すべきテストの目安となる。 | カバレッジそのものではなく、あくまでコードの複雑性を示す指標。 |
| **行** | 実行されたソースコード行の割合。 | 行番号テーブルと命令 | 直感的で理解しやすい。多くのチームで目標値として採用される。デバッグ情報が必要 14。 | 1行に複数の分岐が含まれる場合、行がカバーされても論理的な網羅性は保証されない 22。 |
| **メソッド** | 実行されたメソッドの割合。 | 命令 | どのメソッドがテストによって呼び出されたかを示す。 | メソッドが呼び出されただけで、その内部ロジックが完全にテストされたかを保証するものではない。 |
| **クラス** | 実行されたクラスの割合。 | メソッド | どのクラスがテスト対象となっているかの大まかな指標。 | クラスがカバーされていても、そのクラスの重要な機能がテストされているとは限らない。 |

これらのメトリクスの中で、一般的に目標とされるのは「行カバレッジ」であるが、ソフトウェアの品質を保証するという観点からは「**分岐カバレッジ**」がより深い洞察を提供する。行カバレッジが100%であっても、if (a && b)のような条件式でaが常にfalseのテストケースしかない場合、bの評価部分は実行されず、潜在的なバグを見逃す可能性がある。分岐カバレッジは、このような論理的な欠陥を明確に可視化する。したがって、開発チームは単に行カバレッジの数値を追うのではなく、レポート内の黄色や赤色のひし形記号を解消し、分岐カバレッジを向上させることに注力すべきである。

---

## **3\. 精度と正確性：JaCoCoの既知の限界と非互換性の克服**

JaCoCoは強力なツールであるが、そのバイトコード中心のアプローチは、特定の状況下で「不正確」または紛らわしいカバレッジレポートを生成する可能性がある。これらの限界を理解し、適切に対処することは、JaCoCoを効果的に活用する上で不可欠である。

### **3.1. コンパイラ生成アーティファクトという課題**

JaCoCoの精度の問題の多くは、JavaやKotlinのコンパイラが言語機能を実装するために生成する、開発者が直接記述していない「合成コード」に起因する 16。JaCoCoはこれらの合成コードも忠実にインスツルメントするため、開発者の直感と異なるカバレッジ結果が生じる。

#### **3.1.1. ケーススタディ：try-with-resourcesと到達不能な分岐**

Java 7で導入されたtry-with-resources構文は、リソースの自動クローズを保証する便利な機能だが、その裏側ではコンパイラが複雑なtry-finallyブロックを生成している 24。

* **問題**: javacコンパイラは、リソースのnullチェックや例外の抑制（suppressed exception）など、あらゆるエッジケースを処理するために、単一のリソースに対しても最大8つもの分岐を生成することがあった 24。これらの生成された分岐の一部は、通常のコードパスでは論理的に到達不能であり、テストで100%の分岐カバレッジを達成することが不可能だった 24。これはJaCoCoの初期のユーザーにとって大きな悩みの種であった 25。  
* **解決策**: JaCoCo開発チームはこの問題を認識し、javacやEclipseのecjコンパイラが生成するtry-with-resourcesの特定のバイトコードパターンを検出し、レポートから除外するフィルターを導入した 27。この改善はJaCoCo 0.8.0および0.8.2で実装され、現在ではこの問題は大部分が解決されている 26。

#### **3.1.2. ケーススタディ：Kotlinのコルーチン、ラムダ、そしてステートマシン**

Kotlinの強力な言語機能、特にラムダとコルーチンは、コンパイラによる大幅なバイトコード変換によって実現されている。

* **ラムダ式**: Kotlinのラムダ式は、コンパイル時に匿名の内部クラスまたは静的メソッドとして実装される 31。このため、ラムダを含む行が実行されても、ラムダ本体のコードがテストで実行されなければ、その部分は未カバーとして報告される。この問題は、JaCoCoの後のバージョンでフィルターが改善され、大部分は対処されている 30。  
* **コルーチン**: Kotlinのsuspend関数は、コンパイラによってステートマシンに変換される。このプロセスで、invokeSuspendという名前の合成メソッドが生成され、その内部には状態遷移を管理するためのswitch文（バイトコードレベルではtableswitch）が含まれる 10。JaCoCoはこれらのコンパイラ生成の分岐をインスツルメントするため、ユーザーが記述したロジックとは無関係な「未カバレッジの分岐」が多数報告されることがある 10。  
* **解決策**: JaCoCoは、Kotlinコンパイラが生成する特有のアーティファクトに対するフィルターを継続的に追加している 29。例えば、バージョン0.8.3ではサスペンドラムダ用のフィルターが追加された 10。しかし、これはKotlinコンパイラの進化との絶え間ない追いかけっこであり、新しいコンパイラバージョンが異なるバイトコードパターンを生成すると、新たなフィルターが必要になる 29。  
  withContextやflatMapLatestのような特定のコルーチンビルダーでは、依然としてカバレッジの問題が報告されている 34。

#### **3.1.3. kotlinx-koverの台頭とJaCoCoバックエンドへの移行**

Kotlin特有のカバレッジ問題をより効果的に解決するため、JetBrainsはkotlinx-koverという専用ツールを開発した 36。

当初、Koverは独自のIntelliJベースのカバレッジエージェントを使用していた。しかし、戦略的な方針転換により、Koverはその独自エージェントを非推奨とし、**JaCoCoをデフォルトのバックエンドとして採用する**ことを決定した 38。この移行の動機は、IntelliJエージェントの機能がJaCoCoの機能と収束し、互換性のない実行ファイル形式を持つ2つの異なるインフラを維持することが非効率になったためである 38。業界標準であるJaCoCoに統合することで、ユーザーは既存のツールエコシステム（SonarQubeなど）との連携を維持しつつ、Kotlinに特化した追加機能の恩恵を受けることができる。

この動きは、KotlinエコシステムがJaCoCoのサポートに大きく依存することを意味し、JetBrainsとJaCoCoコミュニティ間の協力関係を強化する。結果として、Kotlinに関するカバレッジの問題は、将来的により体系的に対処されることが期待され、JaCoCoをKotlinプロジェクトで利用する際の長期的な信頼性を高めている 38。

### **3.2. 他のバイトコード操作ツールとの競合**

JaCoCoのインスツルメンテーションは、同じくバイトコードを操作する他のツールと深刻な競合を引き起こす可能性がある。

#### **3.2.1. PowerMock/Mockitoとのインスツルメンテーション競合**

PowerMockやmockito-inlineのようなモックライブラリは、staticメソッドやfinalクラスのモック化を実現するために、JaCoCoと同様にバイトコードを書き換える 39。

* **問題**: 複数のJavaエージェントが有効な場合、「最後にロードされたエージェントが勝つ」という競合が発生する。もしPowerMockのエージェントがJaCoCoのエージェントの後にクラスを書き換えると、JaCoCoが挿入したプローブが削除されてしまう可能性がある。その結果、テストは成功するものの、プローブが実行されないためカバレッジが0%と報告されるという事態に陥る 40。  
* **解決策**: この問題に対する最も確実な解決策は、PowerMockを使用する際にはJaCoCoの**オフラインインスツルメンテーション**を利用することである 42。つまり、ビルドプロセスでまずJaCoCoによってクラスをインスツルメントし、その後にPowerMockがランタイムで動作するように構成する。これは設定が複雑になるが、両ツールの競合を避けるための標準的なアプローチである。特定のバージョン（例：PowerMock 1.6.5以降）ではオンザフライでの互換性が向上したとの報告もある 42。

#### **3.2.2. リフレクションと合成メンバーの影響**

JaCoCoはインスツルメンテーションの過程で、すべてのクラスにprivate staticなフィールド（$jacocoData）とメソッド（$jacocoInit）を追加する 14。これらのメンバーは

syntheticフラグが付与される。

* **問題**: リフレクションを用いてクラスのフィールドやメソッドを動的に走査するコードが、これらの合成メンバーの存在を考慮していない場合、予期せぬ動作やNullPointerExceptionを引き起こすことがある 44。  
* **解決策**: 堅牢なリフレクションコードを記述するためのベストプラクティスは、フィールドやメソッドを処理する前にisSynthetic()メソッドを呼び出し、合成メンバーを明示的に除外することである 45。

### **3.3. フィルタリングと除外のベストプラクティス**

意味のあるカバレッジレポートを得るためには、テストの価値が低いコードや自動生成されたコードを適切に除外することが重要である。

* **Lombok**: Lombokはコンパイル時にゲッター、セッター、equalsなどの定型的なコードを生成する。これらのコードをテストすることは一般的に価値が低いと見なされる。  
  * **解決策**: プロジェクトのルートにlombok.configファイルを配置し、lombok.addLombokGeneratedAnnotation \= trueと記述する 47。これにより、Lombokは生成するすべてのコードに  
    @lombok.Generatedアノテーションを付与する。JaCoCo 0.8.0以降は、名前に "Generated" を含むRUNTIMEまたはCLASSリテンションのアノテーションを認識し、その対象をレポートから自動的に除外する 49。  
* **一般的な除外**: JaCoCoの各種プラグインやエージェント設定では、ワイルドカードを用いたパッケージやクラス名のパターンで、計測対象から除外するクラスを指定できる 4。DTO（Data Transfer Object）や設定クラスなど、ビジネスロジックを含まないクラスを除外するのに有効である。

| シナリオ | 問題の概要 | 推奨される解決策 | 設定例（lombok.configまたはpom.xml/build.gradle） |
| :---- | :---- | :---- | :---- |
| **Lombok生成コード** | get/set, equals, hashCode等の自動生成コードがカバレッジ率を不当に下げる。 | lombok.configファイルを使用し、Lombokに@Generatedアノテーションを付与させ、JaCoCoにそれを無視させる。 | lombok.config: lombok.addLombokGeneratedAnnotation \= true |
| **DTO/モデルクラス** | ビジネスロジックを含まない単純なデータ保持クラス。 | ビルド設定で特定のパッケージやクラスパターンをカバレッジ計測から除外する。 | pom.xml: \<excludes\>\<exclude\>\*\*/model/\*\*\</exclude\>\</excludes\> |
| **try-with-resources（旧バージョン）** | コンパイラが到達不能な分岐を生成し、100%カバレッジが不可能だった。 | JaCoCoのバージョンを上げる。0.8.2以降では、コンパイラ生成パターンを検出する内部フィルターが搭載されている。 | N/A (JaCoCoのバージョンアップで対応) |
| **Kotlinコルーチン** | コンパイラが生成するステートマシン（invokeSuspendメソッド内の分岐）が未カバレッジとして報告される。 | JaCoCoのバージョンを上げることで一部フィルタリングされる。完全な解決は進行中。問題のある箇所を特定し、除外設定を追加する。 | build.gradle: classDirectories.setFrom(files(classDirectories.files.collect { fileTree(dir: it, exclude: '\*\*/coroutines/\*\*') })) |
| **リフレクション利用コード** | JaCoCoが挿入する合成メンバー（$jacocoData）をリフレクションコードが誤って処理し、エラーを引き起こす。 | リフレクションを使用するコード側で、Field.isSynthetic()やMethod.isSynthetic()をチェックし、合成メンバーをスキップする。 | N/A (アプリケーションコード側での対応) |

---

## **4\. パフォーマンス分析と最適化**

JaCoCoは一般的に低オーバーヘッドであるとされているが、特定の条件下では深刻なパフォーマンス低下を引き起こす可能性がある。このセクションでは、その原因を技術的に分析し、最適化のための具体的な戦略を提示する。

### **4.1. JaCoCoのパフォーマンスオーバーヘッドの理解**

* **一般的な認識**: JaCoCoの公式ドキュメントや多くのベンチマークでは、インスツルメンテーションによるパフォーマンスオーバーヘッドは比較的小さく、一般的な単体テストでは10%から25%程度と報告されている 9。  
* **深刻なケース**: しかし、多数のユーザー報告によれば、特にCPU負荷の高い処理や、高度に並列化された統合テストのシナリオでは、オーバーヘッドが劇的に増大することがある。実行時間が2分から20分へと10倍に増加した事例や 51、CPU使用率が4倍以上に跳ね上がり、テスト全体の実行時間が83%増加したという詳細な報告も存在する 52。

### **4.2. 高並行環境におけるキャッシュコンテンション・ボトルネック**

この劇的なパフォーマンス低下の根本原因は、単純な命令追加によるオーバーヘッドではなく、より深く、ハードウェアレベルに起因する**CPUキャッシュコンテンション**である可能性が指摘されている 52。

* **メカニズムの解明**:  
  1. JaCoCoは、クラスごとに単一の静的なbooleanプローブ配列を共有リソースとして使用する 9。  
  2. 高並行アプリケーションでは、複数のスレッドが同じクラス内のメソッドを同時に実行する。  
  3. 各スレッドは、プローブを通過するたびに、この共有配列の要素にtrueを書き込もうと試みる 52。  
  4. あるCPUコア上のスレッドがこの配列に書き込みを行うと、プロセッサのキャッシュコヒーレンシプロトコル（例：MESIプロトコル）により、他のすべてのCPUコア上にある同じキャッシュライン（メモリ領域）が無効化される。  
  5. 他のスレッドが再びその配列にアクセスしようとすると、キャッシュミスが発生し、メモリから最新のデータを読み込む必要がある。さらに、書き込みのためにはキャッシュラインの排他制御権を獲得する必要があり、スレッド間でその所有権の競合が発生する。  
  6. この結果、スレッドは実際に処理を進めるのではなく、キャッシュラインへのアクセス権を待つためにCPUサイクルを消費する「スピンロック」に似た状態に陥る。これが、観測された極端なCPU使用率の上昇とパフォーマンス低下の直接的な原因であると推測される 52。  
* **提案された対策**: この問題を指摘したユーザーは、インスツルメントされたコードが単純な書き込みを行うのではなく、「読み取り、条件分岐、書き込み」のシーケンス（check-then-write）を行うよう変更することを提案した 52。具体的には、  
  if (\!jacocoData\[i\]) { jacocoData\[i\] \= true; }のようなコードを生成する。これにより、プローブが一度trueに設定された後は、高価な書き込み操作とそれに伴うキャッシュ無効化が発生しなくなり、後続の実行はほぼネイティブの速度で行われるようになる。ただし、この提案はJaCoCo本体にはまだ実装されていない。

この分析は、JaCoCoの公称パフォーマンスが、特定の（しかし現代的なサーバーサイドアプリケーションでは一般的な）ワークロードにおいて、いかに誤解を招く可能性があるかを示している。パフォーマンスが重要な並列処理をテストする場合、JaCoCoによる計測行為自体がパフォーマンスのボトルネックとなり、測定結果を歪める可能性があることをアーキテクトは認識する必要がある。

### **4.3. パフォーマンスチューニング：エージェント設定とベストプラクティス**

キャッシュコンテンションのような根本的な問題はユーザー側で解決困難だが、エージェントの設定を最適化することで、オーバーヘッドを大幅に削減することは可能である。

* **インスツルメンテーション対象の絞り込み**: パフォーマンスを向上させる最も効果的な方法は、JaCoCoがインスツルメントするクラスの範囲を限定することである。エージェントオプションのincludesとexcludesを使い、計測対象を自社のアプリケーションパッケージ（例：includes=com.example.\*）に限定し、無関係なサードパーティライブラリやフレームワークを除外することが極めて重要である 2。  
* **出力モードの選択**: JaCoCoエージェントは、カバレッジデータの出力方法としてfile（デフォルト）、tcpserver、tcpclientの3つのモードを提供する 4。  
  * fileモード: JVM終了時にjacoco.execファイルに結果を書き出す。シンプルだが、アプリケーションサーバーのような長時間稼働するプロセスには不向きである 54。  
  * tcpserverモード: エージェントがTCPポートで待機し、外部ツール（例：jacoco:dump）からの要求に応じていつでもカバレッジデータをダンプできる。稼働中のサーバーに対して結合テストを行う場合に理想的である 2。ネットワークI/Oのオーバーヘッドは発生するが、通常はインスツルメンテーション自体のオーバーヘッドに比べれば無視できるレベルである。  
  * tcpclientモード: エージェントが指定されたTCPエンドポイントに接続し、データを送信する。  
* **オンザフライ vs オフライン**: パフォーマンスとビルドの簡潔さの観点から、特殊な要件がない限り、**オンザフライ・インスツルメンテーション**が強く推奨される。オフライン方式は、ビルドの複雑化や、インスツルメント済みと未済みの2種類の成果物を管理する必要性を生じさせる 1。

---

## **5\. 戦略的インテグレーションとベストプラクティス**

これまでの技術的な分析を踏まえ、本セクションではJaCoCoを現代のソフトウェア開発プロセスに効果的に組み込むための実践的な戦略とベストプラクティスを提示する。

### **5.1. 数値の先へ：行動可能な洞察を得るための効果的なレポート解釈**

カバレッジレポートは、単なる数値目標の達成度を確認するためだけのものではない。品質向上のための具体的なアクションを導き出すためのツールとして活用すべきである。

* **未カバレッジコードへの集中**: レポート上で赤色でハイライトされた行やひし形は、「確実にテストされていない」コード領域を示す最も重要なシグナルである。まずはこれらの領域を解消することに注力すべきである 7。  
* **分岐カバレッジの優先**: 前述の通り、行カバレッジよりも分岐カバレッジの方がテストの論理的な網羅性を示す上でより優れた指標である。if文の横にある黄色のひし形は、テストケースが特定の条件分岐の片方のパスしか通っていないことを明確に示しており、テストケースの追加が必要な箇所を具体的に教えてくれる 55。  
* **カバレッジのトレンド分析**: カバレッジ率を時系列で追跡することで、新規コードが適切にテストされているか、またレガシーコードのカバレッジが徐々に改善されているかを確認できる。これは品質文化を醸成する上で有効なプラクティスである 57。  
* **デッドコードの特定**: 広範な手動テストや結合テストを実行してもなおカバレッジが0%のコードは、「デッドコード」（使用されていないコード）である可能性が高い。これらのコードはリファクタリングによる削除の候補となり、コードベースの保守性向上に貢献する 7。

### **5.2. 「100%カバレッジ」の幻想：意味のある品質目標の設定**

ソフトウェアテストの専門家やコミュニティの間では、100%のカバレッジを目指すことは非現実的であり、しばしば逆効果であるというコンセンサスが形成されている 22。

* **メトリクスの形骸化**: 100%という目標は、「メトリクスをゲーム化」するインセンティブを生む。開発者は、テストのアサーション（検証）の質を問わず、単にカバレッジ率を上げるためだけに、意味のないテストを記述するようになる可能性がある 59。  
* **非効率なテスト**: ゲッターやセッターのような、ビジネスロジックを含まない低リスクなコードのテストに多大な労力を費やすことになる 22。  
* **現実的な目標**: 業界で一般的に受け入れられている目標値は80%前後である 62。重要なのは、数値自体よりも、アプリケーションのクリティカルで複雑な部分が十分にテストされていることを保証することである。

### **5.3. 成功のための構成：マルチモジュールプロジェクトにおける単体・結合テストカバレッジ**

現代的なアプリケーションは複数のモジュールで構成されることが多く、テストもその性質に応じて分離することが推奨される。

* **テストタイプの分離**: 単体テスト（高速、外部依存なし）と結合テスト（低速、複数コンポーネント連携、DBやネットワークアクセスを伴う）を明確に分離することは、開発プロセスにおける重要なベストプラクティスである 65。これにより、開発中は高速な単体テストで迅速なフィードバックを得て、CIサーバーではより包括的な結合テストを実行するという効率的なワークフローが実現できる 65。  
* **JaCoCoによる集約レポート**: JaCoCoは、これらの異なる種類のテストから得られたカバレッジデータをマージし、分離または集約したレポートを生成する機能をサポートしている。  
  * **Maven**: maven-surefire-pluginを単体テストに、maven-failsafe-pluginを結合テストに割り当てる。jacoco-maven-pluginでは、prepare-agentとprepare-agent-integrationという二つのexecutionを定義し、それぞれ異なるプロパティ名（例：argLineとitArgLine）と実行データファイル（例：jacoco-ut.execとjacoco-it.exec）を指定する。最後にmergeゴールで実行データファイルを統合し、report-aggregateゴールでプロジェクト全体の集約レポートを生成する 68。  
  * **Gradle**: jacoco-report-aggregationプラグインが推奨される現代的なアプローチである。このプラグインはjvm-test-suiteプラグインと連携し、異なるテストスイートやサブプロジェクトからのカバレッジ結果を自動的に集約する 71。

### **5.4. CI/CDインテグレーション：効果的な品質ゲートの実装**

JaCoCoの最も強力な利用法の一つは、CI/CDパイプラインに品質ゲートを組み込み、コード品質基準を自動的に強制することである 58。

#### **5.4.1. 全体カバレッジ vs 変更ファイルカバレッジ（Diff Coverage）**

従来の品質ゲートは、プロジェクト全体のカバレッジ率にしきい値を設けるものだった。しかし、大規模なレガシープロジェクトではこのアプローチは機能しにくい。より効果的で現代的な戦略は、Pull Requestで**新規に追加または変更されたコード（差分）に対してのみ**高いカバレッジ率（例：80%）を要求する「**Diff Coverage**」である。この「Clean as You Code」アプローチは、既存のコードベース全体に手を入れることなく、新たな技術的負債の発生を防ぎ、コード品質を漸進的に向上させることができる 58。JenkinsやGitHub Actionsのプラグインは、この差分カバレッジをベースラインとした品質ゲートを強力にサポートしている 75。

#### **5.4.2. JenkinsとGitHub Actionsにおける実装パターン**

| CI/CDプラットフォーム | 設定スニペット例 | 主要パラメータ | 説明 |  |
| :---- | :---- | :---- | :---- | :---- |
| **Jenkins (Pipeline)** | recordCoverage(tools: \[\[parser: 'JACOCO'\]\], qualityGates:\]) | metric: LINE, BRANCH等 baseline: MODIFIED\_FILES, MODIFIED\_LINES threshold: 80.0 | Jenkins Coverage Plugin 75 を使用。 | baselineパラメータでMODIFIED\_FILES（変更ファイル）やMODIFIED\_LINES（変更行）を指定することで、差分カバレッジを品質ゲートの基準にできる。 |
| **GitHub Actions** | uses: madrapps/jacoco-report@v1.7.2 with: paths: '\*\*/build/reports/jacoco/\*\*/\*.xml' token: ${{ secrets.GITHUB\_TOKEN }} min-coverage-changed-files: 80 | paths: レポートXMLへのパス token: GitHubトークン min-coverage-changed-files: 変更ファイルの最小カバレッジ率 | madrapps/jacoco-report 76 のようなActionを使用。 | min-coverage-changed-files入力で差分カバレッジのしきい値を設定し、PRにコメントを投稿したり、しきい値未達の場合にワークフローを失敗させたりできる。 |

品質ゲートの考え方は、「プロジェクト全体のカバレッジはいくつか？」という問いから、「このPull Requestはコードの品質を悪化させていないか？」という、より実践的で開発者にとって行動可能な問いへと進化している。この変化は、大規模なコードベースを維持しながら漸進的な改善を促すための、ソフトウェア品質管理におけるプラグマティックな進化である。現代の開発チームがJaCoCoを導入する際には、最初からこの差分カバレッジ戦略を採用することが、最も効果的で持続可能なアプローチと言える。

---

## **結論と戦略的提言**

JaCoCoは、Javaエコシステムにおいて成熟し、広く採用されている堅牢なコードカバレッジツールである。その中核をなすオンザフライ・バイトコードインスツルメンテーションは、ビルドプロセスを簡素化し、多様なJVM言語に対応する柔軟性をもたらす。しかし、その技術的基盤は、現代のソフトウェア開発におけるいくつかの重要な課題も浮き彫りにする。

### **JaCoCoの強みと弱みの要約**

* **強み**:  
  * **成熟度と標準化**: 長年の実績があり、MavenやGradle、各種CI/CDツールとの統合が容易な業界標準ツールである 12。  
  * **柔軟なインスツルメンテーション**: オンザフライ方式により、ビルドプロセスを複雑化することなくカバレッジを計測できる 1。  
  * **活発なメンテナンス**: 新しいJavaやKotlinの言語機能に対応するため、コンパイラ生成アーティファクトに対するフィルターが継続的に追加・改善されている 29。  
* **弱み**:  
  * **高並行性下でのパフォーマンス**: 共有プローブ配列へのアクセスに起因するCPUキャッシュコンテンションにより、マルチスレッド環境下で深刻なパフォーマンス低下を引き起こす可能性がある 52。  
  * **コンパイラ生成コードへの依存**: バイトコードを直接解析するため、コンパイラの出力に精度が左右される。特にKotlinのような言語では、コンパイラの変更に対応するための継続的なフィルター開発が必要となる 10。  
  * **ツール間の互換性**: PowerMockのような他のバイトコード操作ツールとは、オンザフライモードでは根本的な競合を起こし、カバレッジが計測できなくなる 40。

### **行動喚起と提言**

これらの分析に基づき、異なる役割を持つチームメンバーに対して以下の戦略的提言を行う。

* **開発者向け**:  
  1. **バイトコードレベルでの理解**: JaCoCoがソースコードではなくバイトコードを見ていることを常に意識する。レポート上の不可解な未カバレッジは、コンパイラ生成コードが原因である可能性が高い。  
  2. **分岐カバレッジを重視**: 単なる行カバレッジ率の向上を目指すのではなく、レポート上の黄色いひし形（未実行の分岐）を解消することに注力する。これがテストスイートの論理的な網羅性を高める最も効果的な方法である。  
  3. **クリーンなレポートの維持**: Lombokには@Generatedアノテーションを、DTOや設定クラスにはパッケージ除外設定を適用し、意味のあるコードのみがカバレッジレポートに表示されるように構成する。  
  4. **リフレクションの安全な使用**: リフレクションを用いる際は、isSynthetic()チェックを必ず行い、JaCoCoが挿入したメンバーを誤って処理しないようにする 45。  
* **アーキテクトおよびテックリード向け**:  
  1. **パフォーマンスのボトルネックを認識**: 特にCPU負荷の高いマルチスレッドシステムでは、JaCoCoを有効にしたビルドをパフォーマンスベンチマークとして使用しない。計測自体が性能を著しく低下させる可能性があることを周知する 52。  
  2. **Diff Coverageの導入**: CI/CDパイプラインにおける主要な品質管理メカニズムとして、プロジェクト全体のカバレッジではなく、変更差分に対するカバレッジを要求する品質ゲートを導入する。これは、レガシーコードを持つプロジェクトでも漸進的な品質向上を可能にする現代的なベストプラクティスである 58。  
  3. **テストレポートの分離**: 単体テストと結合テストのレポートを分離・集約する構成を標準化する。これにより、開発サイクル中のフィードバック速度とレポートの明確性が向上する 68。  
* **品質保証（QA）およびSDET向け**:  
  1. **テストギャップの発見**: 結合テストや手動テストの実行時にJaCoCoエージェント（tcpserverモード）を使用することで、エンドツーエンドのシナリオでカバーされていないコード領域や、全く使用されていない「デッドコード」を特定する 2。  
  2. **カバレッジの役割を正しく理解**: 高いカバレッジ率が、質の高いテストケースや探索的テストの必要性を代替するものではないことを理解する。カバレッジはテストの質を測るものではなく、テストの努力をどこに向けるべきかを示すためのガイドとして利用する 22。

JaCoCoは、その技術的特性と限界を深く理解し、現代的なベストプラクティスに沿って戦略的に活用することで、依然としてJavaエコシステムにおけるソフトウェア品質を維持・向上させるための非常に価値のあるツールであり続ける。

#### **引用文献**

1. how to prevent jacoco instrumenting production code? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/49296416/how-to-prevent-jacoco-instrumenting-production-code](https://stackoverflow.com/questions/49296416/how-to-prevent-jacoco-instrumenting-production-code)  
2. How to Measure Code Coverage in a Running Java Application Using JaCoCo, 6月 18, 2025にアクセス、 [https://dev.to/arturmkr/how-to-measure-code-coverage-in-a-running-java-application-using-jacoco-5b13](https://dev.to/arturmkr/how-to-measure-code-coverage-in-a-running-java-application-using-jacoco-5b13)  
3. JaCoCo \- Implementation Design, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/doc/implementation.html](https://www.jacoco.org/jacoco/trunk/doc/implementation.html)  
4. Java Agent \- JaCoCo \- EclEmma, 6月 18, 2025にアクセス、 [https://www.eclemma.org/jacoco/trunk/doc/agent.html](https://www.eclemma.org/jacoco/trunk/doc/agent.html)  
5. Code Coverage Tools (JaCoCo, Cobertura, Emma) Comparison in Sonar, 6月 18, 2025にアクセス、 [https://onlysoftware.wordpress.com/2012/12/19/code-coverage-tools-jacoco-cobertura-emma-comparison-in-sonar/](https://onlysoftware.wordpress.com/2012/12/19/code-coverage-tools-jacoco-cobertura-emma-comparison-in-sonar/)  
6. 7\. カバレッジツール, 6月 18, 2025にアクセス、 [https://docs.nec.co.jp/sites/default/files/webotx\_manual\_v96/WebOTX/96/html/dev\_devstudio\_common/7\_coverage.html](https://docs.nec.co.jp/sites/default/files/webotx_manual_v96/WebOTX/96/html/dev_devstudio_common/7_coverage.html)  
7. JaCoCo Test Report Generation \- Coding Shuttle, 6月 18, 2025にアクセス、 [https://www.codingshuttle.com/spring-boot-handbook/ja-co-co-test-report-generation](https://www.codingshuttle.com/spring-boot-handbook/ja-co-co-test-report-generation)  
8. JaCoCo+Tomcat+Jenkinsを使って手動テストのカバレッジレポートを出力する | TECHSCORE BLOG, 6月 18, 2025にアクセス、 [https://www.techscore.com/blog/2015/06/26/jacocotomcatjenkins%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E6%89%8B%E5%8B%95%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E3%82%AB%E3%83%90%E3%83%AC%E3%83%83%E3%82%B8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88/](https://www.techscore.com/blog/2015/06/26/jacocotomcatjenkins%E3%82%92%E4%BD%BF%E3%81%A3%E3%81%A6%E6%89%8B%E5%8B%95%E3%83%86%E3%82%B9%E3%83%88%E3%81%AE%E3%82%AB%E3%83%90%E3%83%AC%E3%83%83%E3%82%B8%E3%83%AC%E3%83%9D%E3%83%BC%E3%83%88/)  
9. JaCoCo \- Control Flow Analysis, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/doc/flow.html](https://www.jacoco.org/jacoco/trunk/doc/flow.html)  
10. Incorrect Jacoco code coverage for Kotlin coroutine \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/53485360/incorrect-jacoco-code-coverage-for-kotlin-coroutine](https://stackoverflow.com/questions/53485360/incorrect-jacoco-code-coverage-for-kotlin-coroutine)  
11. 8 Of The Best Code Coverage Tools, 6月 18, 2025にアクセス、 [https://www.goretro.ai/post/code-coverage-tools](https://www.goretro.ai/post/code-coverage-tools)  
12. JaCoCo \- Maven Plug-in \- EclEmma, 6月 18, 2025にアクセス、 [https://www.eclemma.org/jacoco/trunk/doc/maven.html](https://www.eclemma.org/jacoco/trunk/doc/maven.html)  
13. How To Generate Code Coverage Report Using JaCoCo-Maven Plugin | LambdaTest, 6月 18, 2025にアクセス、 [https://www.lambdatest.com/blog/reporting-code-coverage-using-maven-and-jacoco-plugin/](https://www.lambdatest.com/blog/reporting-code-coverage-using-maven-and-jacoco-plugin/)  
14. JaCoCo \- FAQ, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/doc/faq.html](https://www.jacoco.org/jacoco/trunk/doc/faq.html)  
15. How to get JaCoCo instrumentation code coverage while executing webApplication on server \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/42133100/how-to-get-jacoco-instrumentation-code-coverage-while-executing-webapplication-o](https://stackoverflow.com/questions/42133100/how-to-get-jacoco-instrumentation-code-coverage-while-executing-webapplication-o)  
16. Coverage Counter \- JaCoCo \- EclEmma, 6月 18, 2025にアクセス、 [https://www.eclemma.org/jacoco/trunk/doc/counters.html](https://www.eclemma.org/jacoco/trunk/doc/counters.html)  
17. Understanding the JaCoCo coverage XML report \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/60803055/understanding-the-jacoco-coverage-xml-report](https://stackoverflow.com/questions/60803055/understanding-the-jacoco-coverage-xml-report)  
18. Code Coverage with JaCoCo \- Blue Acorn iCi, 6月 18, 2025にアクセス、 [https://www.blueacornici.com/blog/code-coverage-with-jacoco](https://www.blueacornici.com/blog/code-coverage-with-jacoco)  
19. Intro to JaCoCo | Baeldung, 6月 18, 2025にアクセス、 [https://www.baeldung.com/jacoco](https://www.baeldung.com/jacoco)  
20. Mastering Test Coverage with JaCoCo: Insights and Best Practices \- Neova Solutions, 6月 18, 2025にアクセス、 [https://www.neovasolutions.com/2024/04/09/mastering-test-coverage-with-jacoco-insights-and-best-practices/](https://www.neovasolutions.com/2024/04/09/mastering-test-coverage-with-jacoco-insights-and-best-practices/)  
21. How To Generate Code Coverage Report Using JaCoCo-Maven Plugin \- DZone, 6月 18, 2025にアクセス、 [https://dzone.com/articles/how-to-generate-code-coverage-report-jacoco-maven](https://dzone.com/articles/how-to-generate-code-coverage-report-jacoco-maven)  
22. unit testing \- Pitfalls of code coverage \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/695811/pitfalls-of-code-coverage](https://stackoverflow.com/questions/695811/pitfalls-of-code-coverage)  
23. Jacoco code coverage: non-existent Static block shows only 75% coverage \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/63560283/jacoco-code-coverage-non-existent-static-block-shows-only-75-coverage](https://stackoverflow.com/questions/63560283/jacoco-code-coverage-non-existent-static-block-shows-only-75-coverage)  
24. 8 branches for try with resources \- jacoco coverage possible? \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/17354150/8-branches-for-try-with-resources-jacoco-coverage-possible](https://stackoverflow.com/questions/17354150/8-branches-for-try-with-resources-jacoco-coverage-possible)  
25. try-with-resources Statement: wrong coverage · Issue \#82 · jacoco/jacoco \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/jacoco/jacoco/issues/82](https://github.com/jacoco/jacoco/issues/82)  
26. JaCoCo branch coverage try with resources \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/41334555/jacoco-branch-coverage-try-with-resources](https://stackoverflow.com/questions/41334555/jacoco-branch-coverage-try-with-resources)  
27. TryWithResourcesJavacFilter.java \- JaCoCo, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/coverage/org.jacoco.core/org.jacoco.core.internal.analysis.filter/TryWithResourcesJavacFilter.java.html](https://www.jacoco.org/jacoco/trunk/coverage/org.jacoco.core/org.jacoco.core.internal.analysis.filter/TryWithResourcesJavacFilter.java.html)  
28. TryWithResourcesEcjFilter.java \- JaCoCo, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/coverage/org.jacoco.core/org.jacoco.core.internal.analysis.filter/TryWithResourcesEcjFilter.java.html](https://www.jacoco.org/jacoco/trunk/coverage/org.jacoco.core/org.jacoco.core.internal.analysis.filter/TryWithResourcesEcjFilter.java.html)  
29. FilteringOptions · jacoco/jacoco Wiki \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/jacoco/jacoco/wiki/FilteringOptions](https://github.com/jacoco/jacoco/wiki/FilteringOptions)  
30. JaCoCo \- Change History, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/doc/changes.html](https://www.jacoco.org/jacoco/trunk/doc/changes.html)  
31. Code coverage of lambda expression shows only one line · Issue \#885 \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/jacoco/jacoco/issues/885](https://github.com/jacoco/jacoco/issues/885)  
32. jacoco showing filtered code in the coverage report \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/72747532/jacoco-showing-filtered-code-in-the-coverage-report](https://stackoverflow.com/questions/72747532/jacoco-showing-filtered-code-in-the-coverage-report)  
33. Lambda Expression Body was not covered in Jacoco 0.8.4 · Issue \#929 \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/jacoco/jacoco/issues/929](https://github.com/jacoco/jacoco/issues/929)  
34. Kotlin 1.9.2, jdk 21 (Spring boot) Jacoco (plugin 0.8.12) is complaining about missing branches \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/78468280/kotlin-1-9-2-jdk-21-spring-boot-jacoco-plugin-0-8-12-is-complaining-about-m](https://stackoverflow.com/questions/78468280/kotlin-1-9-2-jdk-21-spring-boot-jacoco-plugin-0-8-12-is-complaining-about-m)  
35. JaCoCo reports coverage on invalid line="0" when using ... \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/Kotlin/kotlinx.coroutines/issues/3911](https://github.com/Kotlin/kotlinx.coroutines/issues/3911)  
36. Implementing Test Coverage in a Multi-module Android Project with Sonar and JaCoCo/Kover \- Testableapple, 6月 18, 2025にアクセス、 [https://testableapple.com/implementing-test-coverage-multi-module-android-project-sonar-jacoco-kover/](https://testableapple.com/implementing-test-coverage-multi-module-android-project-sonar-jacoco-kover/)  
37. Kover : Code Coverage plugin for Kotlin \- Julien's DevRel corner, 6月 18, 2025にアクセス、 [https://lengrand.fr/kover-code-coverage-plugin-for-kotlin/](https://lengrand.fr/kover-code-coverage-plugin-for-kotlin/)  
38. Switching to using the JaCoCo JVM Agent · Issue \#720 · Kotlin/kotlinx-kover \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/Kotlin/kotlinx-kover/issues/720](https://github.com/Kotlin/kotlinx-kover/issues/720)  
39. jacoco offline instrumentation incompatibility with powermock byte ..., 6月 18, 2025にアクセス、 [https://github.com/powermock/powermock/issues/645](https://github.com/powermock/powermock/issues/645)  
40. Java Programming Skills – Writing Process of Unit Test Case \- Alibaba Cloud Community, 6月 18, 2025にアクセス、 [https://www.alibabacloud.com/blog/java-programming-skills-writing-process-of-unit-test-case\_598057](https://www.alibabacloud.com/blog/java-programming-skills-writing-process-of-unit-test-case_598057)  
41. Use ByteBuddy to instrument classes instead Javassist · Issue \#727 \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/powermock/powermock/issues/727](https://github.com/powermock/powermock/issues/727)  
42. java \- Unable to get Jacoco to work with Powermockito using offline ..., 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/23983740/unable-to-get-jacoco-to-work-with-powermockito-using-offline-instrumentation](https://stackoverflow.com/questions/23983740/unable-to-get-jacoco-to-work-with-powermockito-using-offline-instrumentation)  
43. coverage problem with powermockito \- Google Groups, 6月 18, 2025にアクセス、 [https://groups.google.com/g/powermock/c/ZHPpkdVcIyg](https://groups.google.com/g/powermock/c/ZHPpkdVcIyg)  
44. Reflections with Jacoco · Issue \#64 · ronmamo/reflections \- GitHub, 6月 18, 2025にアクセス、 [https://github.com/ronmamo/reflections/issues/64](https://github.com/ronmamo/reflections/issues/64)  
45. maven \- Java annotation capturing with reflection will not work when ..., 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/41542187/java-annotation-capturing-with-reflection-will-not-work-when-execuete-jacoco-pre](https://stackoverflow.com/questions/41542187/java-annotation-capturing-with-reflection-will-not-work-when-execuete-jacoco-pre)  
46. JaCoCo can't test certain uses of reflection? What are the workarounds? \- Google Groups, 6月 18, 2025にアクセス、 [https://groups.google.com/g/jacoco/c/jz9APFSELIs](https://groups.google.com/g/jacoco/c/jz9APFSELIs)  
47. junit code coverage for branch is not 100% for lombok @Data \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/79491106/junit-code-coverage-for-branch-is-not-100-for-lombok-data](https://stackoverflow.com/questions/79491106/junit-code-coverage-for-branch-is-not-100-for-lombok-data)  
48. Exclude lombok generated code from test coverage (JaCoCo/SonarQube), 6月 18, 2025にアクセス、 [https://dev.to/derlin/exclude-lombok-generated-code-from-test-coverage-jacocosonarqube-4nh1](https://dev.to/derlin/exclude-lombok-generated-code-from-test-coverage-jacocosonarqube-4nh1)  
49. JaCoCo: exclude generated methods (using it with Lombok) \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/29520912/jacoco-exclude-generated-methods-using-it-with-lombok](https://stackoverflow.com/questions/29520912/jacoco-exclude-generated-methods-using-it-with-lombok)  
50. java \- How would I add an annotation to exclude a method from a ..., 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/47824761/how-would-i-add-an-annotation-to-exclude-a-method-from-a-jacoco-code-coverage-re](https://stackoverflow.com/questions/47824761/how-would-i-add-an-annotation-to-exclude-a-method-from-a-jacoco-code-coverage-re)  
51. \[java code coverage\] Reasons for huge performance impact \- jacoco@googlegroups.com, 6月 18, 2025にアクセス、 [https://jacoco.narkive.com/adoFZzfD/java-code-coverage-reasons-for-huge-performance-impact](https://jacoco.narkive.com/adoFZzfD/java-code-coverage-reasons-for-huge-performance-impact)  
52. Remove Instrumentation · Issue \#782 · jacoco/jacoco · GitHub, 6月 18, 2025にアクセス、 [https://github.com/jacoco/jacoco/issues/782](https://github.com/jacoco/jacoco/issues/782)  
53. Jacoco Agent Measures Code Coverage for Any Test \- InfoQ, 6月 18, 2025にアクセス、 [https://www.infoq.com/news/2023/09/jacoco-agent-code-coverage/](https://www.infoq.com/news/2023/09/jacoco-agent-code-coverage/)  
54. The Trouble with JaCoCo: Lessons Learned \- Teamscale, 6月 18, 2025にアクセス、 [https://teamscale.com/blog/en/news/blog/profiling-with-jacoco](https://teamscale.com/blog/en/news/blog/profiling-with-jacoco)  
55. Beyond the Basics: Code Coverage and Test Coverage explained \- Diffblue, 6月 18, 2025にアクセス、 [https://www.diffblue.com/resources/code-coverage-and-test-coverage-explained/](https://www.diffblue.com/resources/code-coverage-and-test-coverage-explained/)  
56. What Is JaCoCo? Understanding the JaCoCo Code Coverage Tool \- Diffblue, 6月 18, 2025にアクセス、 [https://www.diffblue.com/resources/what-is-jacoco-understanding-the-jacoco-code-coverage-tool/](https://www.diffblue.com/resources/what-is-jacoco-understanding-the-jacoco-code-coverage-tool/)  
57. JaCoCo vs Cobertura: A Comprehensive Comparison \- Graph AI, 6月 18, 2025にアクセス、 [https://www.graphapp.ai/blog/jacoco-vs-cobertura-a-comprehensive-comparison](https://www.graphapp.ai/blog/jacoco-vs-cobertura-a-comprehensive-comparison)  
58. Best practices for increasing code coverage \- SonarQube Server / Community Build, 6月 18, 2025にアクセス、 [https://community.sonarsource.com/t/best-practices-for-increasing-code-coverage/21423](https://community.sonarsource.com/t/best-practices-for-increasing-code-coverage/21423)  
59. Why reaching 100% Code Coverage must NOT be your testing goal (with examples in C\#) : r/programming \- Reddit, 6月 18, 2025にアクセス、 [https://www.reddit.com/r/programming/comments/1beg654/why\_reaching\_100\_code\_coverage\_must\_not\_be\_your/](https://www.reddit.com/r/programming/comments/1beg654/why_reaching_100_code_coverage_must_not_be_your/)  
60. ThinkingLabs:: Thierry de Pauw \- The Fallacy of the 100% Code Coverage, 6月 18, 2025にアクセス、 [https://thinkinglabs.io/articles/2022/03/19/the-fallacy-of-the-100-code-coverage.html](https://thinkinglabs.io/articles/2022/03/19/the-fallacy-of-the-100-code-coverage.html)  
61. What is a reasonable code coverage % for unit tests (and why)? \[closed\] \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/90002/what-is-a-reasonable-code-coverage-for-unit-tests-and-why](https://stackoverflow.com/questions/90002/what-is-a-reasonable-code-coverage-for-unit-tests-and-why)  
62. What is Code Coverage & How to Calculate It? \+6 Tips to Get Started \- Testlio, 6月 18, 2025にアクセス、 [https://testlio.com/blog/code-coverage/](https://testlio.com/blog/code-coverage/)  
63. What is Code Coverage? | Atlassian, 6月 18, 2025にアクセス、 [https://www.atlassian.com/continuous-delivery/software-testing/code-coverage](https://www.atlassian.com/continuous-delivery/software-testing/code-coverage)  
64. Stop Bad Code: 5 Quality Gates Your Jenkins Pipeline Needs \- Java Tech Blog, 6月 18, 2025にアクセス、 [https://javanexus.com/blog/stop-bad-code-5-quality-gates-jenkins-pipeline](https://javanexus.com/blog/stop-bad-code-5-quality-gates-jenkins-pipeline)  
65. Separating Unit from Integration tests in Java using Gradle, 6月 18, 2025にアクセス、 [http://stuartingram.com/2016/09/15/separating-unit-from-integration-tests-in-java-using-gradle/](http://stuartingram.com/2016/09/15/separating-unit-from-integration-tests-in-java-using-gradle/)  
66. Unit Testing vs Integration Testing: Key Differences and Best Practices \- Harness, 6月 18, 2025にアクセス、 [https://www.harness.io/harness-devops-academy/unit-testing-vs-integration-testing](https://www.harness.io/harness-devops-academy/unit-testing-vs-integration-testing)  
67. Should I separate unit tests and integration tests? \- Software Engineering Stack Exchange, 6月 18, 2025にアクセス、 [https://softwareengineering.stackexchange.com/questions/340347/should-i-separate-unit-tests-and-integration-tests](https://softwareengineering.stackexchange.com/questions/340347/should-i-separate-unit-tests-and-integration-tests)  
68. Code coverage reports with Maven in multi-module projects \- Business \- doubleSlash Blog, 6月 18, 2025にアクセス、 [https://blog.doubleslash.de/en/software-technologies/code-coverage-reports-with-maven-in-multi-module-projects](https://blog.doubleslash.de/en/software-technologies/code-coverage-reports-with-maven-in-multi-module-projects)  
69. Merging Integration and Unit test reports with JaCoCo \- Stack Overflow, 6月 18, 2025にアクセス、 [https://stackoverflow.com/questions/33349864/merging-integration-and-unit-test-reports-with-jacoco](https://stackoverflow.com/questions/33349864/merging-integration-and-unit-test-reports-with-jacoco)  
70. Maven Surefire, Failsafe plugins with Jacoco for unit and integration testing with code coverage. https://natritmeyer.com/howto/reporting-aggregated-unit-and-integration-test-coverage-with-jacoco/ · GitHub, 6月 18, 2025にアクセス、 [https://gist.github.com/mikybars/e2a6b75f1e2377b9613bfb273d617cfa](https://gist.github.com/mikybars/e2a6b75f1e2377b9613bfb273d617cfa)  
71. The JaCoCo Report Aggregation Plugin \- Gradle User Manual, 6月 18, 2025にアクセス、 [https://docs.gradle.org/current/userguide/jacoco\_report\_aggregation\_plugin.html](https://docs.gradle.org/current/userguide/jacoco_report_aggregation_plugin.html)  
72. \[Jacoco\] Aggregating Jacoco Reports for Multi-Module Projects | HARIL, 6月 18, 2025にアクセス、 [https://haril.dev/en/blog/2022/07/29/jacoco-aggregation-report](https://haril.dev/en/blog/2022/07/29/jacoco-aggregation-report)  
73. The JaCoCo Plugin \- Gradle User Manual, 6月 18, 2025にアクセス、 [https://docs.gradle.org/current/userguide/jacoco\_plugin.html](https://docs.gradle.org/current/userguide/jacoco_plugin.html)  
74. Add SonarQube quality gates to your Jenkins build pipeline | Tom Gregory, 6月 18, 2025にアクセス、 [https://tomgregory.com/jenkins/sonarqube-quality-gates-in-jenkins-build-pipeline/](https://tomgregory.com/jenkins/sonarqube-quality-gates-in-jenkins-build-pipeline/)  
75. Coverage \- Jenkins Plugins, 6月 18, 2025にアクセス、 [https://plugins.jenkins.io/coverage/](https://plugins.jenkins.io/coverage/)  
76. JaCoCo Report · Actions · GitHub Marketplace, 6月 18, 2025にアクセス、 [https://github.com/marketplace/actions/jacoco-report](https://github.com/marketplace/actions/jacoco-report)  
77. Code Coverage Guide | Venice, 6月 18, 2025にアクセス、 [http://venicedb.org/docs/dev\_guide/how\_to/code\_coverage\_guide](http://venicedb.org/docs/dev_guide/how_to/code_coverage_guide)  
78. JaCoCo \- Java Code Coverage Library, 6月 18, 2025にアクセス、 [https://www.jacoco.org/jacoco/trunk/index.html](https://www.jacoco.org/jacoco/trunk/index.html)