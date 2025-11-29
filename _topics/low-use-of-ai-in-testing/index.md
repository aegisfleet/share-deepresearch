---
audio: /share-deepresearch/assets/audio/low-use-of-ai-in-testing.m4a
video: /share-deepresearch/assets/video/low-use-of-ai-in-testing.mp4
category: engineering
date: 2025-11-29
description: AIはコーディングでは97.5%の採用率に達した一方、テスト自動化では55.7%に留まっている。本調査はこの「普及の断層」が確実な業界トレンドであることを立証し、テストオラクル問題、フレーキーテスト、Vibe Codingの弊害、スキルギャップなど、技術的・運用的・組織的な構造的要因を多角的に分析する。
layout: topic
prompt: ソフトウェアの設計やコーディングにはAIの活用が進んでいるが、テストにおいては使用率が低いという調査データがある。そのデータが業界全体の傾向なのか調査し、なぜテストにおけるAIの使用率が低いのかまとめて欲しい。
supplementary_materials:
  - title: スライド資料
    pdf: /share-deepresearch/topics/low-use-of-ai-in-testing/slide.pdf
tags: 
- テスト自動化
title: ソフトウェア品質保証の未来とAIの乖離：コーディングにおけるAI普及とテスト自動化における停滞の構造的要因に関する包括的調査報告書
---

# **ソフトウェア品質保証の未来とAIの乖離：コーディングにおけるAI普及とテスト自動化における停滞の構造的要因に関する包括的調査報告書**

## **エグゼクティブサマリー**

2024年から2025年にかけてのソフトウェアエンジニアリング業界における最大のトピックは、生成AI（Generative AI）の爆発的な普及である。GitHub CopilotやChatGPTに代表されるAIコーディングアシスタントは、開発者の生産性を劇的に向上させ、業界全体の97.5%が何らかの形でAIを導入するという「完全普及期」に突入している1。しかし、この技術革新の波において、品質保証（QA）およびソフトウェアテストの領域は、コーディングや設計といった上流工程と比較して、著しい採用の遅れを見せている。

本報告書は、ユーザーから提起された「ソフトウェア設計やコーディングではAI活用が進んでいるが、テストにおいては使用率が低い」という仮説が、業界全体の確固たる傾向であることを複数の国際的な調査データに基づき立証するものである。さらに、なぜテスト領域においてのみAIの社会実装が阻害されているのか、その要因を技術的ハードル（テストオラクル問題、非決定論的挙動）、運用上の課題（メンテナンスコスト、信頼性の欠如）、そして組織・文化的背景（スキルギャップ、責任の所在）の多角的な視点から徹底的に分析する。

調査の結果、テストにおけるAI採用の低さは、単なる「ツールの未成熟」によるものではなく、生成AIの本質である「確率論的な生成」と、テストに求められる「決定論的な検証」という根本的な相性の悪さに起因していることが明らかとなった。また、AIによってコード生成が加速することで生じる「Vibe Coding（雰囲気コーディング）」現象が、テスト負債を増大させ、皮肉にもQAエンジニアの負担を減らすどころか増大させている現状も浮き彫りとなった。本報告書では、これらの課題を克服するための次世代技術「エージェンティックAI（Agentic AI）」の可能性についても言及し、今後の展望を提示する。

---

## **1\. AI導入の現況：「生成」と「検証」の不均衡な進化**

ソフトウェア開発ライフサイクル（SDLC）全体を見渡した際、AIの導入率は均一ではない。開発者がコードを書く「生成（Creation）」のフェーズと、その正しさを確認する「検証（Verification）」のフェーズの間には、明確な「普及の断層（Adoption Gap）」が存在する。

### **1.1 業界データに見る普及率の乖離**

複数の信頼できる業界調査が、この不均衡を裏付けている。2025年のTechReviewerによる調査では、ソフトウェアエンジニアリング全体でのAI採用率は97.5%に達し、前年の90.9%からさらに上昇し、市場は飽和状態に近づいている1。しかし、その内訳を見ると、AIの適用用途には大きな偏りがあることが分かる。

**表1：SDLC各工程におけるAI採用率の比較（2024年-2025年比較）**

| SDLC工程 | 2024年採用率 | 2025年採用率 | 主な用途 | 傾向分析 |
| :---- | :---- | :---- | :---- | :---- |
| **コード生成** | 67.5% | 72.2% | ボイラープレート生成、自動補完、リファクタリング | **主流化**：開発者の必須ツールとして定着 |
| **ドキュメント生成** | データなし | 67.1% | API仕様書、README作成、コード解説 | **急増**：LLMの要約能力と親和性が高い |
| **コードレビュー** | データなし | 67.1% | 構文チェック、スタイル是正 | **普及**：静的解析の延長として導入容易 |
| **自動テスト/デバッグ** | 62.5% | 55.7%\* | 単体テスト生成、テストデータ作成 | **停滞・減少**：実運用での課題が露呈し、実験的使用から選別段階へ移行1 |
| **UI/UX最適化** | 32.5% | 48.1% | ビジュアル分析、レイアウト調整 | **成長**：マルチモーダルAIの進化が寄与 |

1のデータに基づく。なお、テストにおける採用率の数値上の減少は、初期の「とりあえず使ってみる」フェーズから、実務適用における厳格な選別に移行した結果、実稼働していないツールが計上されなくなった可能性を示唆している。

GitHubの調査（2024年）でも同様の傾向が見られる。開発者の97%がAIコーディングツールを使用した経験があると回答している一方で、テスト生成へのAI活用に関しては、組織的な推奨や実運用レベルでの統合が進んでいない現状がある2。特に注目すべきは、Stack Overflowの2024年開発者調査である。現在AIツールを使用している開発者の82%が「コード作成」に使用しているのに対し、「テストコードの作成」に使用しているのはわずか27.2%に留まっている3。

この「82% vs 27%」という数字の開きこそが、ユーザーの問いに対する定量的な回答である。すなわち、**「テストにおけるAI使用率が低い」という認識は、個人の感覚ではなく、グローバルな業界全体の明確なトレンドである。**

### **1.2 「実験」と「信頼」のギャップ**

さらに深い洞察を得るためには、「使用経験（Experimentation）」と「信頼・定着（Trust/Reliance）」を区別する必要がある。GitLabのレポートによれば、回答者の98%が「テストケース生成にAIを使用した実験」を行っているものの、実際に日々の業務タスクを人間のレビューなしにAIに任せられると回答した層はわずか37%に過ぎない2。

これは「信頼のパラドックス」と呼ばれる現象である。開発者はCopilotが提案するコードスニペットを採用することには抵抗がないが、AIが生成したテストケースが「本当にバグを検出できるか（False Negativeがないか）」、あるいは「正しい機能を誤ってバグとして報告しないか（False Positiveがないか）」という点については、強い懐疑心を持っている。

特に地域差もこの傾向に影響を与えている。米国では88%の開発者が会社からAI使用のサポートを得ているのに対し、ドイツでは59%に留まる2。品質や安全性に対して保守的な文化圏や産業（自動車、金融、医療など）において、テストプロセスへのAI導入は、コンプライアンスや責任の所在という観点から、より慎重にならざるを得ない状況がある。

### **1.3 開発速度の加速とQAのボトルネック化**

AIコーディングツールの普及は、皮肉な結果を招いている。GitLabの調査によれば、経営層（CxO）の69%が「1年前と比較して2倍の速度でソフトウェアをリリースしている」と回答している5。AIによってコードを書く速度は劇的に向上した。しかし、テストの速度がそれに追いついていないため、QA工程が巨大なボトルネックとなっているのである。

開発者が「Vibe Coding（雰囲気コーディング）」、つまり自然言語プロンプトだけで、その背後にあるロジックや副作用を深く理解せずにコードを生成・出荷する傾向が強まっていることが、この問題を悪化させている4。理解度の浅いコードが大量に生産されることで、テスト工程には「未知の挙動」を持つコードが大量に流れ込むことになる。これに対し、AIによるテスト自動化ツールは、生成されたコードの意図（仕様）を正確に理解できないため、有効なテストケースを生成できず、結果として人間によるレビューや手動テストの負荷が増大しているのである7。

---

## **2\. テストにおけるAI普及を阻む技術的障壁**

なぜAIは「コードを書く」ことは得意なのに、「テストを書く」ことは苦手なのか。この問いに対する答えは、生成AIの根本的な仕組みと、ソフトウェアテストに求められる厳密性の間のミスマッチにある。

### **2.1 「テストオラクル問題」：正解を知らないAI**

テストにおけるAI活用の最大の障壁は、学術的に「テストオラクル問題（The Test Oracle Problem）」として知られる課題である9。テストオラクルとは、実行結果が「正しい」か「誤り」かを判断するための基準（正解）のことである。

* **コンテキストの欠如**：LLMはGitHub上の膨大なオープンソースコードで学習しており、一般的なコーディングパターン（例：ログイン画面のHTML構造、典型的なソートアルゴリズム）は熟知している。しかし、特定の企業の、特定のプロジェクトにおける「ビジネスロジック」や「仕様」は学習していない。  
* **循環論法のリスク**：AIに「このコードのテストを書いて」と依頼した場合、AIは渡されたコード（実装）を解析し、その実装が通るようなテストケースを生成する傾向がある。もし元のコードにバグが含まれていた場合、AIはそのバグを含んだ挙動を「正仕様」と見なし、バグを見逃す（Passさせてしまう）テストコードを生成する11。これはテストの目的である「欠陥の検出」を根本から否定するものである。  
* **仕様書の不在**：理想的には、AIに詳細な仕様書や要件定義書を読ませ、そこからテストケースを生成させるべきである。しかし、多くの現場では仕様書が不完全であったり、最新の状態に更新されていなかったりする。正解（仕様）が存在しない状態で、AIに正誤判定を求めること自体が論理的に不可能なのである。

### **2.2 非決定論的な挙動と「幻覚（ハルシネーション）」のリスク**

ソフトウェアテスト、特に回帰テスト（リグレッションテスト）に求められる最も重要な特性は「決定論（Determinism）」と「再現性」である。同じ入力に対しては、常に同じ結果が返ってこなければならない。

しかし、生成AIは本質的に「確率論的（Probabilistic）」なシステムである。同じプロンプトを入力しても、毎回異なるテストコードやアサーション（判定条件）が出力される可能性がある12。

* **存在しない要素の捏造**：AIが生成したテストスクリプトが、画面上に存在しないボタンIDやCSSセレクタを「幻覚」として生成するケースが多発している13。  
* **微妙なロジックの誤り**：例えば、「在庫が0の時は購入ボタンが無効化される」という仕様に対し、AIが「在庫が0でも購入ボタンが表示されていればOK」という緩い判定基準を生成してしまうリスクがある。このような「嘘の合格（False Negative）」は、人間がコード一行一行を精査しない限り発見が困難であり、信頼性を著しく損なう9。

### **2.3 テストレベルによる適性の差：単体テスト vs E2Eテスト**

「テスト」と一口に言っても、その種類によってAIの適性は大きく異なる。調査データからは、単体テスト（Unit Test）ではAI活用が進んでいる一方で、エンドツーエンド（E2E）テストでは苦戦しているという傾向が見て取れる14。

**表2：テストレベル別に見るAIの成熟度と課題**

| テスト種類 | AI適性 | 普及度 | 技術的背景 |
| :---- | :---- | :---- | :---- |
| **単体テスト (Unit Test)** | **高** | 進んでいる | 関数やメソッド単位でロジックが完結しており、外部依存が少ない。入力と出力の関係が数学的・論理的に明確であるため、LLMによる推論が容易で、ボイラープレートの生成効果が高い16。 |
| **統合テスト (Integration)** | **中** | 限定的 | 複数のモジュールやDBとの連携が必要となり、AIが理解すべきコンテキスト（文脈）が増大する。モックデータの作成や依存関係の解決に人間の介入が必要となる。 |
| **E2Eテスト (UI/UX)** | **低** | **遅れている** | 画面操作、状態遷移、非同期処理、ユーザー体験の理解が必要。DOM構造の変更に弱く、AI生成スクリプトが頻繁に壊れる（Flakiness）。ビジネスフロー全体の理解が不可欠18。 |
| **視覚的回帰テスト (VRT)** | **中高** | 拡大中 | 画像比較（ピクセル差分）はAI（特にCNNなどの画像認識モデル）の得意分野。デザイン崩れの検出において、人間より高速かつ正確に機能するツール（Applitools等）が存在する20。 |

E2EテストにおけるAI活用の低さは、次節で詳述する「メンテナンスの悪夢」と直結している。

---

## **3\. 運用上の現実：メンテナンスの悪夢と「自己修復」の限界**

多くの企業がテスト自動化にAIを導入しようとして挫折する最大の理由は、導入コストではなく、導入後の\*\*運用・保守コスト（Maintenance Burden）\*\*にある。

### **3.1 フレーキーテスト（Flaky Tests）と信頼性の崩壊**

UIテスト自動化における最大の敵は「フレーキーテスト（Flaky Tests）」である。これは、コードに変更がないにもかかわらず、タイミングや環境要因によって成功したり失敗したりする不安定なテストのことである18。

AIが生成したSeleniumやPlaywrightのスクリプトは、往々にしてウェブページの構造（DOM）に強く依存した「脆い（Brittle）」セレクタを使用する傾向がある。開発者がデザインを僅かに変更しただけで、IDやClass名が変わり、テストが大量に失敗する。  
GitLabの調査によれば、DevSecOpsチームはAIツールの導入にもかかわらず、依然として多くの時間を「非効率なプロセス（テストの修正やデバッグ）」に費やしている4。AIが大量のテストケースを自動生成したとしても、それらが頻繁に壊れるのであれば、メンテナンス工数は削減されるどころか増大してしまう。これが「テストにおけるAI使用率が低い」主要因の一つである。

### **3.2 「自己修復（Self-Healing）」機能の功罪**

この問題に対処するため、MablやTestim、ApplitoolsといったAIテストツールベンダーは「自己修復（Self-Healing）」機能を売りにしている。これは、要素のIDが変わっても、AIが周囲のテキストや位置関係から「これがおそらく対象のボタンである」と推測し、テストを継続させる機能である23。

しかし、現実のデータは、この機能が万能ではないことを示している。  
437の企業実装を分析した研究によれば、自己修復機能を有効にしたチームでは、従来の手法と比較して\*\*「誤検知（False Positive）」の発生率が23%高かった\*\*というデータがある13。

* **誤った修復のリスク**：例えば、バグによって「購入」ボタンが画面から消えたとする。本来ならばテストは「購入ボタンが見つからない」として失敗（Fail）すべきである。しかし、AIの自己修復機能が過剰に働き、近くにある「キャンセル」ボタンや「お気に入り」ボタンを誤って「購入ボタンの代わり」として認識し、クリックしてしまうことがある。その結果、テストは「成功（Pass）」として報告され、致命的なバグが見逃される19。  
* **パフォーマンスの低下**：自己修復プロセスは、要素が見つからない場合にページ全体を再解析するため、テスト実行時間を増大させる。ある事例では、AI機能によってテスト実行が2〜3倍遅くなったという報告もある13。

このように、AIによる「便利機能」が、かえってテストの信頼性を損ない、エンジニアが「結局、自分で書いたほうが確実だ」と判断してAIツールの使用を中止するケースが後を絶たない。

---

## **4\. セキュリティ、信頼、そして「Vibe Coding」のリスク**

技術的な問題に加え、企業のコンプライアンスやセキュリティポリシーも、テスト領域でのAI活用を阻害している。

### **4.1 データプライバシーとコンプライアンスの壁**

テストには、本番環境に近いデータ（氏名、住所、金融取引データなど）が必要となる場合が多い。しかし、これらのデータをChatGPTなどのパブリックなLLMに入力することは、GDPRやCCPAなどのデータ保護規制、および企業のセキュリティポリシーに抵触する恐れがある25。

金融機関や医療機関など、特に規制が厳しい業界では、「AIがなぜそのテスト結果を良しとしたのか」という説明責任（Explainability）が求められる。しかし、ディープラーニングモデルは「ブラックボックス」であり、なぜその判定を下したのかを論理的に説明することが困難である27。監査において「AIがOKと言ったから」という理由は通用しないため、人間による再検証が必須となり、自動化のメリットが相殺されてしまう。

### **4.2 Vibe Coding（雰囲気コーディング）が生む「テスト負債」**

近年、開発現場で急速に広がっている「Vibe Coding」という現象が、QAチームに深刻な影響を与えている。「Vibe Coding」とは、開発者が自然言語でAIに指示を出し、出力されたコードの内容を精査せずに「なんとなく動いているからOK（Vibe is good）」として実装を進めるスタイルを指す4。

GitLabの調査では、73%の回答者が「コードの仕組みを理解せずに自然言語プロンプトを使用して作成されたコード（Vibe Coding）」による問題を経験していると回答している4。

* **理解なき実装**：開発者自身がコードのロジックを理解していないため、どのようなエッジケース（境界値）が存在し、どこに脆弱性が潜んでいるかを予測できない。  
* **テスト不能なコード**：AIが生成するコードは、必ずしもテスト容易性（Testability）を考慮して設計されていない。巨大な関数や密結合なクラスが生成され、単体テストを書くこと自体が困難になるケースがある。  
* **負債の爆発**：AIによって「動くコード」は大量に生産されるが、それに対応する「品質保証」が追いつかない。結果として、テストされていない、あるいは不十分なテストしかされていないコードが積み上がり、QAチームはその尻拭いに追われることになる。この状況下では、未成熟なAIテストツールを導入して混乱を招くよりも、既存の確実な手動テストやスクリプトテストに頼らざるを得なくなる。

---

## **5\. 人的要因と組織文化：スキルギャップと抵抗**

ツールや技術の問題だけでなく、それを使う「人間」と「組織」の問題も見逃せない。

### **5.1 QAエンジニアのスキルギャップと役割の変化**

従来のQAエンジニアやテスターの多くは、手動テストの実行や、Seleniumなどの特定ツールのスクリプト作成に特化したスキルセットを持っている。しかし、AIを活用したテストには、プロンプトエンジニアリングや、AIの出力を批判的に評価するスキル、さらにはAIモデルの特性（幻覚やバイアス）への理解が求められる28。

経営層はAI導入による効率化を期待する（35%のCxOがスキル不足を課題視）一方で、現場のエンジニアに対する十分なトレーニングやリソースが提供されていない（25%の個人貢献者がトレーニング不足を指摘）というギャップが存在する5。  
「AIを使え」というトップダウンの指示に対し、現場は「使い方がわからない」「使ってみたが品質が低い」というリアクションになりがちであり、これが使用率の低迷に繋がっている。

### **5.2 組織文化と「自動化への不信感」**

Stack Overflowの調査によれば、開発者のAIツールに対する好感度は2023年の77%から2024年には72%へと低下している3。これは「期待値の調整」が起きていることを示唆している。初期の過剰な期待（ハイプ）が落ち着き、実際の業務で直面する「直しの手間」や「不正確さ」に対する失望感が広がっている。

特にテスト領域では、一度でもAIが重大なバグを見逃したり、無実のコードをバグ扱いしたりすると、チーム全体の信頼を一瞬で失う。「またAIが間違えたのか」という徒労感が蔓延し、結局「人間がやったほうが早い」という結論に戻ってしまう文化的・心理的な障壁が高い31。

---

## **6\. 将来展望：エージェンティックAIがもたらすブレイクスルー**

現状の分析は厳しいものであるが、2025年以降の展望は明るい兆しを見せている。これまでの限界を突破する鍵となるのが「エージェンティックAI（Agentic AI）」である。

### **6.1 生成AIからエージェンティックAIへの進化**

これまでのAIテストツール（GitHub Copilot等）は、あくまで「支援型（Assistive）」であり、人間が指示したコードを補完するものであった。これに対し、現在登場しつつある**エージェンティックAI**は、「自律型（Autonomous）」である32。

エージェンティックAIは、「ログインして、赤いシャツをカートに入れ、購入する」という抽象的なゴール（目的）を与えられると、以下のプロセスを自律的に実行する：

1. **計画（Planning）**：画面を見て、どの手順で操作すべきかを考える。  
2. **実行（Execution）**：実際にブラウザを操作する。  
3. **観察（Observation）**：操作の結果、画面がどう変化したかを確認する。  
4. **修正（Correction）**：もしボタンが見つからなければ、スクロールしたり、検索したりして、人間のように臨機応変に対応する。

このアプローチにより、従来の「脆いセレクタ」問題や「メンテナンス地獄」が劇的に改善される可能性がある。AIはIDやXPathといった内部構造ではなく、人間と同じように「視覚情報」と「文脈」に基づいて操作を行うため、UIの変更に対して極めて堅牢になる34。

### **6.2 プラットフォームエンジニアリングへの統合**

もう一つの重要なトレンドは、AIテスト機能のプラットフォームへの統合である。GitLabやGitHub、Azure DevOpsといったプラットフォーム自体にAIが組み込まれ、コードがコミットされた瞬間に、バックグラウンドで自動的にテスト生成、セキュリティスキャン、影響範囲分析が行われるようになる4。  
これにより、開発者が個別のテストツールをセットアップしたり、メンテナンスしたりする手間がなくなり、AIテストの普及が「意識しない形」で進むと予測される。

---

## **結論**

「ソフトウェアの設計やコーディングにはAI活用が進んでいるが、テストにおいては使用率が低い」というユーザーの指摘は、最新の業界データによって完全に裏付けられた事実である。その背景には、単なる技術的な遅れではなく、以下のような構造的な要因が存在する。

1. **テストオラクル問題**：AIは「何が正解か」を知らないため、仕様書なきコードからのテスト生成は循環論法に陥りやすい。  
2. **信頼性と決定論の欠如**：確率論的なAIは、厳密な再現性を求めるテスト工程において「幻覚」や「フレーキーテスト」を生み出し、信頼を損なっている。  
3. **運用コストの逆転**：AIが生成した低品質なテストスクリプトのメンテナンス（自己修復の誤検知対応など）にかかる工数が、自動化による削減工数を上回ってしまっている。  
4. **Vibe Codingの弊害**：AIによる高速かつ理解の浅いコーディングが、テスト負債を爆発的に増大させ、QAチームを圧迫している。

しかし、この停滞は一時的なものである可能性が高い。2025年以降、**エージェンティックAI**の実用化により、AIは「スクリプトを書く」存在から「自律的にテストを実行する」存在へと進化する。これにより、テスト領域におけるAI活用は、現在の「低迷期」を脱し、コーディング領域と同様、あるいはそれ以上の不可欠なインフラへと成長していくことが予測される。

企業やエンジニアに求められるのは、現状の未成熟なツールに失望してAIを全否定することではない。AIが得意とする領域（単体テスト、視覚的回帰テスト）と、人間が担うべき領域（仕様策定、E2Eテストの戦略立案、探索的テスト）を適切に見極め、来るべきエージェンティックAIの時代に備えて「AIを監督・指揮（Orchestrate）するスキル」を磨くことである。

#### **引用文献**

1. AI in Software Development 2025: From Exploration to ..., 11月 29, 2025にアクセス、 [https://techreviewer.co/blog/ai-in-software-development-2025-from-exploration-to-accountability-a-global-survey-analysis](https://techreviewer.co/blog/ai-in-software-development-2025-from-exploration-to-accountability-a-global-survey-analysis)  
2. Survey: The AI wave continues to grow on software development ..., 11月 29, 2025にアクセス、 [https://github.blog/news-insights/research/survey-ai-wave-grows/](https://github.blog/news-insights/research/survey-ai-wave-grows/)  
3. AI | 2024 Stack Overflow Developer Survey, 11月 29, 2025にアクセス、 [https://survey.stackoverflow.co/2024/ai](https://survey.stackoverflow.co/2024/ai)  
4. GitLab Survey Reveals the "AI Paradox," Faster Coding Creates New Bottlenecks Requiring Platform Solutions, 11月 29, 2025にアクセス、 [https://ir.gitlab.com/news/news-details/2025/GitLab-Survey-Reveals-the-AI-Paradox-Faster-Coding-Creates-New-Bottlenecks-Requiring-Platform-Solutions/default.aspx](https://ir.gitlab.com/news/news-details/2025/GitLab-Survey-Reveals-the-AI-Paradox-Faster-Coding-Creates-New-Bottlenecks-Requiring-Platform-Solutions/default.aspx)  
5. GitLab Survey Reveals Tension Around AI, Security, and Developer Productivity within Organizations, 11月 29, 2025にアクセス、 [https://about.gitlab.com/press/releases/2024-06-25-gitlab-survey-reveals-tension-around-ai-security-and-developer-productivity-within-organizations/](https://about.gitlab.com/press/releases/2024-06-25-gitlab-survey-reveals-tension-around-ai-security-and-developer-productivity-within-organizations/)  
6. Vibe Coding Risks: What Companies Must Watch Out for When Deploying Generative Applications \- FutureCode IT Consulting, 11月 29, 2025にアクセス、 [https://future-code.dev/en/blog/vibe-coding-risks-what-companies-must-watch-out-for-when-deploying-generative-applications/](https://future-code.dev/en/blog/vibe-coding-risks-what-companies-must-watch-out-for-when-deploying-generative-applications/)  
7. GitLab Global DevSecOps Report, 11月 29, 2025にアクセス、 [https://about.gitlab.com/developer-survey/](https://about.gitlab.com/developer-survey/)  
8. Survey Sees AI Coding Creating Need for More Software Engineers \- DevOps.com, 11月 29, 2025にアクセス、 [https://devops.com/survey-sees-ai-coding-creating-need-for-more-software-engineers/](https://devops.com/survey-sees-ai-coding-creating-need-for-more-software-engineers/)  
9. The Challenge of Software Testing in the Age of Artificial Intelligence \- Architecht, 11月 29, 2025にアクセス、 [https://architecht.com/en/corporate/blog/technology/the-challenge-of-software-testing-in-the-age-of-artificial-intelligence/](https://architecht.com/en/corporate/blog/technology/the-challenge-of-software-testing-in-the-age-of-artificial-intelligence/)  
10. (PDF) The Oracle Problem in Software Testing: A Survey \- ResearchGate, 11月 29, 2025にアクセス、 [https://www.researchgate.net/publication/276255185\_The\_Oracle\_Problem\_in\_Software\_Testing\_A\_Survey](https://www.researchgate.net/publication/276255185_The_Oracle_Problem_in_Software_Testing_A_Survey)  
11. Design choices made by LLM-based test generators prevent them from finding bugs \- arXiv, 11月 29, 2025にアクセス、 [https://arxiv.org/html/2412.14137v1](https://arxiv.org/html/2412.14137v1)  
12. What are AI hallucinations? \- Google Cloud, 11月 29, 2025にアクセス、 [https://cloud.google.com/discover/what-are-ai-hallucinations](https://cloud.google.com/discover/what-are-ai-hallucinations)  
13. Why Your Test Automation Tool's "AI Magic" Isn't Working: The Hidden Learning Gap, 11月 29, 2025にアクセス、 [https://www.ranorex.com/blog/test-automation-learning-gap/](https://www.ranorex.com/blog/test-automation-learning-gap/)  
14. End-to-End Testing vs Unit Testing: Breaking Down the Differences \- Supatest AI, 11月 29, 2025にアクセス、 [https://supatest.ai/blog/end-to-end-testing-vs-unit-testing](https://supatest.ai/blog/end-to-end-testing-vs-unit-testing)  
15. Unit Testing vs End-to-End Testing: Striking the Right Balance in Software Quality, 11月 29, 2025にアクセス、 [https://dev.to/alok\_e75d0463248211c2ca56/unit-testing-vs-end-to-end-testing-striking-the-right-balance-in-software-quality-1op5](https://dev.to/alok_e75d0463248211c2ca56/unit-testing-vs-end-to-end-testing-striking-the-right-balance-in-software-quality-1op5)  
16. 2024 Stack Overflow Developer Survey, 11月 29, 2025にアクセス、 [https://survey.stackoverflow.co/2024/](https://survey.stackoverflow.co/2024/)  
17. What is AI Unit Testing? Ensuring Accuracy and Reliability \- Functionize, 11月 29, 2025にアクセス、 [https://www.functionize.com/automated-testing/ai-unit-testing](https://www.functionize.com/automated-testing/ai-unit-testing)  
18. Flaky Tests: Why They Happen and How We Eliminated 97% of Them with AI, 11月 29, 2025にアクセス、 [https://checksum.ai/blog/flaky-test](https://checksum.ai/blog/flaky-test)  
19. What Is Self Healing Test Automation and How Does It Work? \- Autify, 11月 29, 2025にアクセス、 [https://autify.com/blog/self-healing-test-automation](https://autify.com/blog/self-healing-test-automation)  
20. Visual Regression Testing Tools Compared | BrowserStack, 11月 29, 2025にアクセス、 [https://www.browserstack.com/guide/visual-regression-testing-tool](https://www.browserstack.com/guide/visual-regression-testing-tool)  
21. Applitools vs mabl 2025 | Gartner Peer Insights, 11月 29, 2025にアクセス、 [https://www.gartner.com/reviews/market/ai-augmented-software-testing-tools/compare/applitools-vs-mabl-505967572](https://www.gartner.com/reviews/market/ai-augmented-software-testing-tools/compare/applitools-vs-mabl-505967572)  
22. Flaky Tests in Automation: Strategies for Reliable Automated Testing \- Ranorex, 11月 29, 2025にアクセス、 [https://www.ranorex.com/blog/flaky-tests/](https://www.ranorex.com/blog/flaky-tests/)  
23. Self-Healing Testing: Continuous QA Without Maintenance, 11月 29, 2025にアクセス、 [https://www.virtuosoqa.com/post/self-healing-continuous-testing](https://www.virtuosoqa.com/post/self-healing-continuous-testing)  
24. Self-Healing Test Automation: Reduce Failures & Boost Efficiency \- ACCELQ, 11月 29, 2025にアクセス、 [https://www.accelq.com/blog/self-healing-test-automation/](https://www.accelq.com/blog/self-healing-test-automation/)  
25. New report on AI-assisted tools points to rising stakes for DevSecOps \- GitLab, 11月 29, 2025にアクセス、 [https://about.gitlab.com/blog/new-report-on-ai-assisted-tools-points-to-rising-stakes-for-devsecops/](https://about.gitlab.com/blog/new-report-on-ai-assisted-tools-points-to-rising-stakes-for-devsecops/)  
26. The trust problem in AI is getting worse and nobody wants to talk about it \- Reddit, 11月 29, 2025にアクセス、 [https://www.reddit.com/r/ArtificialInteligence/comments/1nimfvm/the\_trust\_problem\_in\_ai\_is\_getting\_worse\_and/](https://www.reddit.com/r/ArtificialInteligence/comments/1nimfvm/the_trust_problem_in_ai_is_getting_worse_and/)  
27. AI-Generated Testing: Ethics and Responsibility in the Age of Automation | by Betül Aksoy, 11月 29, 2025にアクセス、 [https://medium.com/@aksoybetul/ai-generated-testing-ethics-and-responsibility-in-the-age-of-automation-774da7175002](https://medium.com/@aksoybetul/ai-generated-testing-ethics-and-responsibility-in-the-age-of-automation-774da7175002)  
28. Here's Why 73% QA Will Be REPLACED (REALITY Exposed), 11月 29, 2025にアクセス、 [https://www.youtube.com/watch?v=hDBifxix71A](https://www.youtube.com/watch?v=hDBifxix71A)  
29. Transforming Quality Assurance: Artificial Intelligence in Software Testing \- BairesDev, 11月 29, 2025にアクセス、 [https://www.bairesdev.com/blog/ai-in-software-testing/](https://www.bairesdev.com/blog/ai-in-software-testing/)  
30. AI | 2025 Stack Overflow Developer Survey, 11月 29, 2025にアクセス、 [https://survey.stackoverflow.co/2025/ai](https://survey.stackoverflow.co/2025/ai)  
31. Has anyone actually gotten AI test automation to work or is it all hype? \- Reddit, 11月 29, 2025にアクセス、 [https://www.reddit.com/r/QualityAssurance/comments/1p1aptg/has\_anyone\_actually\_gotten\_ai\_test\_automation\_to/](https://www.reddit.com/r/QualityAssurance/comments/1p1aptg/has_anyone_actually_gotten_ai_test_automation_to/)  
32. Why Agentic AI in Test Automation is the Future of Testing \- Auxis, 11月 29, 2025にアクセス、 [https://www.auxis.com/why-agentic-ai-in-test-automation-is-the-future-of-testing/](https://www.auxis.com/why-agentic-ai-in-test-automation-is-the-future-of-testing/)  
33. Agentic AI in Testing | BrowserStack, 11月 29, 2025にアクセス、 [https://www.browserstack.com/guide/agentic-ai-in-testing](https://www.browserstack.com/guide/agentic-ai-in-testing)  
34. Agentic AI Testing: The Future of Autonomous Software Quality Assurance \- TestGrid, 11月 29, 2025にアクセス、 [https://testgrid.io/blog/agentic-ai-testing/](https://testgrid.io/blog/agentic-ai-testing/)  
35. Rewriting the Rules of Software Quality: Why Agentic QA is the Future CIOs Must Champion, 11月 29, 2025にアクセス、 [https://devops.com/rewriting-the-rules-of-software-quality-why-agentic-qa-is-the-future-cios-must-champion/](https://devops.com/rewriting-the-rules-of-software-quality-why-agentic-qa-is-the-future-cios-must-champion/)  
36. 20 Best AI Coding Assistant Tools \[Updated Aug 2025\] \- Qodo, 11月 29, 2025にアクセス、 [https://www.qodo.ai/blog/best-ai-coding-assistant-tools/](https://www.qodo.ai/blog/best-ai-coding-assistant-tools/)