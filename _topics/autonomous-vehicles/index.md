---
audio: /share-deepresearch/assets/audio/autonomous-vehicles.mp3
category: research
date: 2025-06-29
description: 完全自動運転技術の実態、事故率の比較分析、および事故発生時の搭乗者の行動についての調査報告書です。特に、米国と中国における商業サービスの現状を詳述し、事故事例を通じて安全性と技術的課題を探ります。
ga4_metrics:
  avgSessionDuration: 842.863607
  pageViews: 2
  users: 1
layout: topic
prompt: 既に完全自動運転が実現している国の実態調査を行いたい。完全自動運転車は人が運転する車より事故率は低いのだろうか。事故の事例の調査と事故が発生した際に搭乗者が行わないといけない行動についてまとめて欲しい。
supplementary_materials:
- title: インフォグラフィック：データで見る自動運転の真実
  url: /share-deepresearch/topics/autonomous-vehicles/infographic.html
- title: 完全自動運転の現在地と未来：事故調査レポートから読み解く技術・安全性・社会の課題
  url: /share-deepresearch/topics/autonomous-vehicles/reveal.html
tags:
- 自動運転
title: 完全自動運転の実態：グローバル展開、安全性、および将来展望に関する包括的調査報告書
---

# **完全自動運転の実態：グローバル展開、安全性、および将来展望に関する包括的調査報告書**

## **序論**

本報告書は、完全自動運転技術の実現状況、人間が運転する車両との安全性比較、および事故発生時における搭乗者の対応プロトコルに関する包括的な調査結果を提供するものです。ご依頼内容にある「完全自動運転」という用語は、一般的に米国自動車技術会（SAE International）が定義する自動運転レベルのうち、最高の段階である「レベル5」を指します。しかし、2025年現在、いかなる国や地域においてもレベル5の商用サービスは実現していません 1。現在、商業的に利用可能な最高レベルは、特定の条件下でシステムが全ての運転タスクを担う「レベル4：高度運転自動化」です。したがって、本報告書ではこのレベル4の商業サービスを「現在実現している最高レベルの自動運転」と位置づけ、その実態を詳細に分析します。レベル5については、将来的な展望として論じます。

### **SAE自動運転レベルの明確化**

自動運転技術の能力を理解するためには、SAEが策定した国際的な基準を把握することが不可欠です。この基準は、自動化の度合いに応じてレベル0からレベル5までの6段階に分類されています 3。特に重要なのは、運転操作の主体が「人間」から「システム」へと移行するレベル2とレベル3の境界です 3。

* **レベル0〜2（運転支援車）**: これらのレベルでは、運転の主体はあくまで人間です 3。レベル1はアダプティブ・クルーズ・コントロール（ACC）やレーンキープアシストなど、加減速か操舵のいずれかを支援する機能です 3。レベル2は、これらの機能を同時に作動させ、特定の条件下（主に高速道路）で手放し運転（ハンズオフ）を可能にしますが、ドライバーは常に周囲を監視する責任を負います 4。事故発生時の法的責任は、全面的にドライバーにあります 4。  
* **レベル3（条件付運転自動化／アイズオフ）**: 高速道路の渋滞時など、特定の条件下において、運転の主体がシステムに移ります。この間、ドライバーは視線を道路から外し、読書などのセカンドタスクを行うこと（アイズオフ）が許可されます 6。しかし、システムが介入を要請した際には、即座に運転を引き継がなければならないため、常に待機状態にあることが求められます 7。日本では、2020年の法改正によりレベル3の公道走行が可能となり、ホンダが「Honda SENSING Elite」を搭載したレジェンドで日本初の型式指定を取得しました 3。  
* **レベル4（高度運転自動化／ブレインオフ）**: 本報告書の主要な分析対象です。特定の地理的エリアや気象条件といった「運用設計領域（Operational Design Domain, ODD）」内に限り、システムが全ての運転タスクを実行し、ドライバーの介入は原則として不要となります 5。ODD内では、運転席に人がいなくても走行可能であり、この状態は「ブレインオフ」とも呼ばれます 7。  
* **レベル5（完全運転自動化）**: ODDの制限なく、いかなる道路状況や気象条件下でもシステムが運転を行う、理論上の最終段階です 5。このレベルでは、ハンドルやペダルといった手動操作装置自体が不要になると考えられていますが、その実現はまだ遠い将来の課題とされています 2。

### **調査対象の概要**

本報告書は、レベル4の商業サービスをリードする主要企業とその展開地域に焦点を当てます。具体的には、米国を拠点とするAlphabet傘下の**Waymo**と、中国を拠点とする**Baidu**の自動運転部門**Apollo**を主要な分析対象とします。また、かつてWaymoの有力な競合であったGM傘下の**Cruise**についても、その事業停止に至った経緯が業界に与えた影響の大きさから、重要な事例として取り上げます 1。調査対象国は、これらの企業が活発に事業を展開している米国と中国が中心となります。

## **第1章：完全自動運転（レベル4）のグローバル展開と現状**

本章では、レベル4自動運転技術がどの国で、どのような形で商業化されているかの実態を、各国の規制アプローチ、主要企業の事業戦略、そしてビジネスモデルの観点から多角的に分析します。国や地域の規制環境が、技術の社会実装の速度と形態をいかに規定しているかを明らかにします。

### **1.1 主要国の導入状況と規制環境の比較**

#### **米国：イノベーション主導のボトムアップ型アプローチ**

米国の規制環境は、連邦政府が拘束力のある統一規則を設けるのではなく、各州が独自に法整備を進める「パッチワーク」状態が特徴です 10。このアプローチは、企業が比較的自由に実証実験やサービス展開を行うことを可能にし、技術革新を促進する一方で、州ごとに異なる規制が全国規模での展開における障壁となる可能性も指摘されています。

* **Waymoの展開**: Alphabet傘下のWaymoは、この分野における明確なリーダーです。アリゾナ州フェニックス、カリフォルニア州サンフランシスコおよびロサンゼルス、テキサス州オースティン、ジョージア州アトランタなど、複数の主要都市で完全無人のロボタクシーサービス「Waymo One」を展開しています 2。特にフェニックスでは、315平方マイル（約816平方キロメートル）という広大なサービスエリアで24時間365日、一般市民向けにサービスを提供しており、商業化の最前線を走っています 15。さらに、配車サービス大手のUberとの戦略的提携を通じて、オースティンやアトランタではUberのアプリからWaymoの車両を呼び出せるようにし、顧客基盤の飛躍的な拡大を図っています 12。  
* **Cruiseの蹉跌**: GM傘下のCruiseは、サンフランシスコにおいてWaymoと激しい競争を繰り広げていました。しかし、2023年10月に発生した重大な歩行者事故（詳細は第3章で後述）が転機となります。この事故とその後の対応における透明性の欠如が問題視され、カリフォルニア州車両管理局（DMV）から無期限の営業許可停止処分を受け、最終的には米国内の全事業を停止する事態に追い込まれました 17。この事例は、一つの重大な技術的・倫理的失敗が、企業の存続そのものを脅かすことを示す象徴的な出来事となりました。  
* **規制動向**: 米国運輸省道路交通安全局（NHTSA）は、事故報告に関する恒久一般命令（Standing General Order, SGO）を発令し、メーカーからのデータ収集を強化することで安全監視を行う一方 19、一部の連邦自動車安全基準（FMVSS）からの免除を認めるなど、イノベーションを阻害しないための柔軟な規制緩和も模索しています 21。

#### **中国：国家主導のトップダウン型アプローチ**

中国は、自動運転を国家の重要戦略と位置づけ、政府が強力なリーダーシップを発揮して産業育成を進めるトップダウン型のアプローチを採っています 24。

* **Baidu Apollo Goの展開**: 検索エンジン大手のBaiduが率いるApolloプラットフォームは、この国家戦略を背景に急成長を遂げています。北京、武漢、重慶、深圳といった複数の巨大都市で、世界最大規模のロボタクシーサービス「Apollo Go」を展開しています 25。特に武漢では、長江を渡る橋梁を含む複雑な都市環境で、24時間年中無休の完全無人サービスを実現しており、その運用規模と技術レベルの高さを示しています 26。  
* **規制動向**: 中国政府は、2023年後半にレベル3およびレベル4の自動運転車が公道を合法的に走行できるようにする一連の政策を発表し、商用化を強力に後押ししています 29。北京の亦庄（Yizhuang）経済開発区のような大規模な実証実験エリアを設定し、スマートインフラ（V2I通信など）の整備も一体で進めることで、技術開発を加速させています 10。一方で、最近では安全性を重視する動きも顕著です。消費者や利用者の誤解を招く「自動運転」や「インテリジェント運転」といったマーケティング用語の使用を厳しく規制し、無線通信によるソフトウェア更新（OTAアップデート）にも厳格な政府承認プロセスを課すなど、急速な技術普及に伴うリスク管理を強化しています 30。

#### **欧州：統一規制を目指す協調的アプローチ**

欧州では、個々の国が先行しつつも、EU全体として統一された規制枠組みの構築を目指す協調的なアプローチが見られます。

* **ドイツの先行**: ドイツは2021年、世界に先駆けてレベル4の自動運転車を特定の公道で通常運用することを可能にする国内法を成立させ、法整備の面で世界をリードしました 34。この法律は、特にシャトルバスや物流トラックといった特定用途での商用化を促進することを目的としています。  
* **EUの統一フレームワーク**: 現在、EU内では自動運転に関する規制が加盟国ごとに異なり、国境を越えたサービス展開の障壁となっています。この「パッチワーク」状態を解消するため、EUは2026年までに加盟国全体で適用される統一的な規制枠組みを導入することを目指しています 10。これが実現すれば、欧州市場における自動運転技術のスケールアップが大きく加速すると期待されています。

#### **その他の注目国**

KPMGが発表した自動運転車準備度指数（Autonomous Vehicles Readiness Index）などによると、シンガポール、オランダ、英国なども、先進的な法改正、質の高い道路インフラ、そして国民の受容性の高さといった点で高い評価を得ており、今後の展開が注目されます 35。

#### **規制アプローチが事業展開モデルを規定する**

各国の導入状況を比較すると、規制環境のアプローチが企業の事業戦略や展開モデルを直接的に形成している構図が浮かび上がります。

米国の「許可的（Permissive）」な規制環境は、州レベルでの競争と連邦レベルの緩やかな監督を特徴とします。この環境は、WaymoやCruiseのような企業に、多様な都市で迅速にサービスを開始し、試行錯誤を重ねるインセンティブを与えました。その結果、企業はまず特定の都市（例：Waymoにとってのフェニックス）で深くサービスを掘り下げて運用ノウハウを蓄積し、その成功モデルを他の都市へ水平展開する（例：WaymoとUberの提携によるオースティン、アトランタへの展開 12）という、地理的に限定的だが深い浸透を目指す事業モデルを採用する傾向にあります。

対照的に、中国の「指示的（Directive）」な規制環境は、中央政府と地方政府が一体となり、インフラ整備を含む大規模な実証実験区（例：北京亦庄 27）を国家プロジェクトとして設定します。この強力なトップダウンのアプローチにより、Baiduのような企業は政府の計画と歩調を合わせ、複数の巨大都市で同時並行的に大規模なフリートを展開し、一気に事業規模（スケール）を獲得するという戦略を取ることが可能になっています 26。

この規制アプローチの違いは、将来の技術的覇権争いにおいて決定的な要因となり得ます。米国モデルは、多様なユースケースと技術的アプローチを生み出す土壌となる可能性がある一方で、規制の断片化が全国規模での標準化や展開を遅らせるリスクを内包しています。対する中国モデルは、迅速なスケールと標準化において圧倒的な強みを発揮しますが、トップダウンの画一的な規制が、長期的にはイノベーションの多様性を制限する可能性も否定できません。

## **第2章：自動運転車と人間が運転する車の事故率比較分析**

本章では、自動運転車（AV）の安全性を客観的に評価するため、人間ドライバーとの事故率を多角的に比較分析します。特に、単純な事故件数ではなく、事故の重大性に着目することが、より本質的な安全性の理解につながることを示します。

### **2.1 データソースの概要と解釈における重要な注意点**

AVの安全性を評価するための主要な公的データソースには、米国のNHTSAが収集するSGOデータベース 19 や、カリフォルニア州DMVが公開する衝突報告書 37 があります。これらに加え、WaymoやCruiseといった企業が自主的に公開する詳細な安全性レポートも重要な情報源となります 39。

これらのデータを解釈する上で、極めて重要な注意点が存在します。それは「報告バイアス」です。  
AVの運用企業は、規制当局への報告義務や、技術に対する社会的な信頼を構築する必要性から、ミラーの接触のようなごく軽微な事象であっても、ほぼ全ての物理的接触を事故として報告します 40。

一方で、人間ドライバーによる事故は、特に物損のみの軽微な事故や、負傷者がいても警察を介さない事故が多数存在します。NHTSAの推計によれば、物損のみの事故の60%、負傷を伴う事故の32%が警察に報告されていないとされています 40。  
この報告義務と慣行の著しい非対称性により、単純に「全事故件数」や「走行距離あたりの事故率」を比較すると、AVの事故率が人間ドライバーよりも不当に高く見えるという、逆説的な結果が生じることがあります 43。

#### **安全性の指標を再定義する必要性**

この報告バイアスの存在は、AVの安全性を評価するための指標そのものを見直す必要性を示唆しています。AVの真の安全性を評価するためには、報告の有無に左右されにくい、より客観的で比較可能性の高い指標を用いるべきです。

この課題を認識したWaymoなどの企業は、単純な事故件数ではなく、報告バイアスの影響が比較的小さい「警察への報告があった事故」や「負傷を伴う事故」、特に「重篤な傷害や死亡に至った事故」に焦点を当てた分析を、スイス・リー（Swiss Re）のような第三者の保険・再保険会社と共同で発表する戦略をとっています 40。このアプローチは、AVの安全性をめぐる公的な議論や政策決定が、より本質的な指標、すなわち「社会全体の死傷者数をどれだけ削減できるか」に基づいて行われるべきであることを示唆しています。規制当局やメディアも、この報告バイアスの存在を社会に周知し、より正確なリスク認識を促す重要な役割を担っています。

### **2.2 定量的な事故率比較：重篤な事故の削減効果**

重篤度でフィルタリングされたデータを比較すると、AVの安全性の高さが顕著になります。

* **Waymoのデータ**:  
  * 世界有数の再保険会社であるSwiss Reとの共同研究では、2,530万マイル（約4,070万キロメートル）の走行データに基づき、人間ドライバーと比較して**物損害賠償請求が88%、人身傷害賠償請求が92%少ない**という結果が示されました 41。これは、保険金支払いの実績に基づいた、極めて客観的なデータです。  
  * Waymoが自社のサービス提供エリアにおける人間ドライバーの事故率（ベンチマーク）と比較したレポートでは、「負傷を伴う事故」が**85%**、「警察への報告があった事故」が\*\*57%\*\*少ないと報告されています 46。具体的には、走行100万マイル（約160万キロメートル）あたりの負傷事故発生率は、Waymoが0.41件であるのに対し、人間ドライバーのベンチマークは2.78件でした 48。  
* **Cruiseのデータ**:  
  * 事業停止前のデータになりますが、最初の100万マイルの無人走行において、サンフランシスコの人間ドライバーのベンチマークと比較して、**全衝突事故が54%**、\*\*負傷リスクのある衝突が73%\*\*少なかったと報告しています 42。  
* **Baiduのデータ**:  
  * Baidu Apolloの自動運転システムを用いたシミュレーション研究では、人間が実際に起こした事故シナリオ596件を再現したところ、そのうち**約60.9%（363件）を完全に回避**し、回避できなかった事故においても、衝突速度を低下させることで傷害の重篤度を大幅に軽減できたと報告されています 49。

これらのデータをまとめたものが以下の表です。

**表2.1: 主要AV企業と人間ドライバーの事故率比較（重篤度別）**

| 指標 (100万マイルあたり) | Waymo | Cruise | 人間ドライバー (ベンチマーク) | データソース |
| :---- | :---- | :---- | :---- | :---- |
| 負傷を伴う事故率 | 0.41 | データなし | 2.78 | 46 |
| 警察への報告があった事故率 | 2.1 | データなし | 4.85 | 46 |
| 全衝突事故率 (参考値) | データなし | 18.0\* | データなし | 42 |
| 重篤な傷害・死亡事故率 | 0.03 | データなし | 0.23 | 40 |

\*注: Cruiseのデータは最初の100万マイルで36件の衝突があったため、200万マイル走行時の値に換算して比較。

この表は、報告バイアスの影響を受けにくい指標（負傷、警察報告、重篤度）で比較した場合、主要なAVシステムが人間ドライバーよりも統計的に有意に安全であることを明確に示しています。

### **2.3 質的分析：事故の傾向と特徴**

事故率だけでなく、どのような種類の事故が起きているかを質的に分析することも重要です。

* **AVが「被害者」となる事故**: Waymo、Cruiseともに、関与した事故の圧倒的多数は相手方（主に人間ドライバー）の過失によるものです 42。特に顕著なのは、停車中や信号待ち、あるいは低速で慎重に走行しているAVに対し、  
  **後続の人間ドライバーが不注意やいらだちから追突するケース**です 42。これは、AVが交通法規を厳格に遵守するがゆえに発生する、特有の現象と言えます。  
* **交通弱者（VRU）とのインタラクション**: Waymoのデータは、歩行者、自転車、オートバイといった交通弱者（Vulnerable Road Users）が関与する負傷事故が、人間ドライバーと比較して**81%から93%と劇的に減少**していることを示しています 39。これは、LiDAR、レーダー、カメラを組み合わせた360度のセンサーシステムが、人間の死角や不注意を効果的に補い、予測不能な動きをする交通弱者を早期に検知・回避できる能力を持つことを示唆しています。  
* **交差点での安全性**: 交差点は人間ドライバーにとって事故が多発する場所ですが、Waymoは交差点で発生する負傷事故が人間比で**96%少ない**と報告しています 39。この優れた性能は、システムが信号無視をして交差点に進入してくる車両などを遠方からでも正確に検知し、適切に対応できる能力に起因すると分析されています。

#### **AVの「非人間的な」運転スタイルが新たなリスクを生む可能性**

これらの分析から、AVの安全性をめぐる新たな論点が浮かび上がります。AVは交通法規を厳格に遵守し、常に安全マージンを最大限に確保しようとプログラムされています 51。この結果、AVは人間ドライバーが日常的に行っているような暗黙の社会的ルール（例えば、交通の流れに乗るための多少の速度超過や、効率を優先したやや詰めた車間距離など）を許容しません。この法規に忠実で極めて慎重な（cautious）運転スタイル 43 は、人間ドライバーから見ると「遅すぎる」「予期せぬタイミングで減速する」といった、予測不能な挙動に映ることがあります。

この「予測可能性のズレ」が、後続の人間ドライバーのいらだちや誤解を招き、不適切な車間距離での追従や無理な追い越しを誘発し、結果としてAVが被害者となる追突事故の多発につながっている可能性があります 42。

これは、AVの安全性を向上させるためには、AV単体の技術的性能を高めるだけでは不十分であり、人間とAVが混在する交通環境（Mixed Traffic）における**相互作用（Human-Robot Interaction）の設計**が不可欠であることを示唆しています。将来的には、AVが人間ドライバーに対してより予測可能で自然な挙動を示すようにプログラミングする「社会的受容性を考慮したチューニング」や、人間ドライバーがAVの特性を理解し、安全に共存するための教育・啓発活動が重要な課題となるでしょう。これは単なる技術的な課題ではなく、社会心理学的な側面を含む複合的な課題です。

## **第3章：主要な事故の事例調査と分析**

本章では、自動運転車の技術的限界、倫理的課題、そして組織としての対応の重要性を浮き彫りにした象徴的な事故事例を詳細に分析し、業界全体にとっての教訓を抽出します。

### **3.1 Cruise社：歩行者引きずり事故（2023年10月、サンフランシスコ）**

この事故は、自動運転技術の社会実装におけるリスク管理の複雑さと、企業倫理の重要性を最も明確に示した事例です。

* **事故の経緯**:  
  1. 2023年10月2日夜、サンフランシスコ市内の交差点で、まず人間の運転する日産車が、横断禁止の信号（赤信号）で道路を渡っていた歩行者に衝突しました 52。  
  2. 歩行者はこの最初の衝突でボンネットに乗り上げ、その後、日産車から弾き飛ばされる形で、隣の車線を走行していたCruise社の完全無人ロボタクシーの進路上に投げ出されました 52。  
  3. Cruise車両はブレーキをかけましたが間に合わず、時速約18.6マイル（約30km/h）で歩行者と二次衝突しました 52。  
  4. 問題は、この二次衝突の後に発生しました。Cruise車両は、事故後に車両を路肩などの安全な場所へ自動的に移動させる「ミニマル・リスク・コンディション（MRC）」と呼ばれる安全プロトコルを実行しようとしました 52。  
  5. しかし、システムは歩行者が**車両の下に巻き込まれ、左前輪の下に閉じ込められていることを検知できませんでした**。その結果、歩行者を引きずったまま約6メートル（20フィート）、時速約7.7マイル（約12km/h）で低速移動し、最終的に停止しました 18。  
* **技術的・組織的問題の分析**:  
  * **認識（Perception）の失敗**: 外部調査報告書によると、Cruiseのシステムは二次衝突を、車両の下に人を巻き込む可能性のある「正面衝突」ではなく、比較的リスクの低い「側面衝突」と誤って分類しました。この誤認識により、車両下に人がいる可能性を考慮する安全ロジックが作動しませんでした 55。センサーデータ上は歩行者が存在していたにもかかわらず、システムは衝突の混乱の中で歩行者の追跡に失敗し、その存在を事実上「忘却」してしまったのです 55。  
  * **透明性の欠如と信頼の失墜**: Cruise社は当初、規制当局（カリフォルニア州DMVやNHTSA）への報告において、この「引きずり」という極めて重要な事実を十分に開示しませんでした。後にビデオ映像によってこの事実が明らかになると、同社の透明性と誠実さに対する信頼は完全に失墜しました 18。  
* 影響と教訓:  
  この事故は、自動運転システムが「エッジケース」（予期せぬ稀な事象）にいかに脆弱であるかを露呈しました。特に、複数の独立した事象が連鎖して発生する複雑なシナリオへの対応能力が、依然として大きな技術的課題であることが明確になりました。しかし、それ以上に深刻だったのは組織的な対応の失敗です。技術的な欠陥は改善可能ですが、失われた信頼の回復は遥かに困難です。この一件は、カリフォルニア州DMVによる無期限の営業許可停止、CEOを含む経営陣の辞任、そして大規模な人員削減へと直結し、企業の存続を揺るがす事態となりました 17。これは自動運転業界全体に対し、高度な安全文化の醸成と、規制当局や社会に対する徹底した透明性と誠実な対応が、事業継続の生命線であることを示す痛烈な教訓となりました。

### **3.2 Waymo社：静止物への衝突とNHTSAによる調査**

業界のリーダーであるWaymoも、技術的な課題と無縁ではありません。

* **事象の概要**: Waymoは、門扉、チェーン、ポール、駐車車両といった、動かない静止物や半静止物との軽微な衝突を複数回報告しています 57。これらは重篤な事故ではありませんが、システムの基本的な認識能力に疑問を投げかけるものでした。  
* **NHTSAの調査開始 (PE24016)**: 2024年5月、NHTSAはこれらの事象（22件のインシデントを特定）を受け、Waymoの第5世代自動運転システム（ADS）が、交通制御装置（信号機など）をどのように認識・反応し、静止物をいかにして回避しているかについて、予備的評価（Preliminary Evaluation）を開始しました 58。  
* **Waymoの対応**: Waymoは、これらの衝突がソフトウェアの欠陥に起因することを認め、対象となる全車両のソフトウェアをOTA（Over-the-Air）でアップデートするリコール（自主改善措置）を実施しました 57。  
* **教訓**: この一連の出来事は、業界をリードするWaymoでさえ、基本的な物体認識や状況判断といった領域で未だ課題を抱えていることを示しています。これは、自動運転の認識システムが完璧ではなく、継続的なデータの収集、改善、そして検証が不可欠であることを物語っています。また、NHTSAが比較的軽微な事故のパターンから体系的なリスクの兆候を読み取り、迅速に調査を開始したことは、規制当局が業界の動向を厳しく監視している姿勢の表れです。

### **3.3 Baidu Apollo社：予測不能な人間とのインタラクション**

中国で発生した事故は、異なる交通文化における課題を浮き彫りにします。

* **事象の概要**:  
  * **武漢での歩行者接触事故**: 中国・武漢で、青信号に従って発進したBaiduのロボタクシーが、赤信号で横断してきた歩行者と軽微な接触事故を起こしました。歩行者に目立った外傷はありませんでした 59。  
  * **北京での追突被害事故**: 北京の公道で、Baiduの試験車両が通常走行中に後続のトラックから追突されました。調査の結果、責任は100%トラック運転手にあると判断されました 62。  
* 分析と教訓:  
  これらの事例は、第2章で指摘した自動運転車が直面する2つの典型的な課題、すなわち「交通ルールを遵守しない人間の予測不能な行動への対応」と「AVの慎重な運転スタイルに起因する他者からの追突被害」を改めて示しています。

#### **事故に対する社会的・文化的文脈の差異**

これらの事故を比較分析すると、同じような事象であっても、その責任の所在や世論の反応が、国や地域の文化的・法的背景によって大きく異なるという重要な点が浮かび上がります。

武漢で発生した歩行者との接触事故では、AVは交通ルール（青信号で発進）を遵守していた一方で、歩行者はルールを破っていました（赤信号で横断）。中国国内のソーシャルメディアでは、ルールを破った歩行者を非難し、ルールを守ったBaiduを擁護する声が多数を占めました 61。

これは、米国で発生したCruiseの事故とは対照的です。Cruiseの事故でも、歩行者は横断禁止の場所を渡っていましたが、結果として重傷を負わせたAV（およびその運営企業）に対して、社会と規制当局から極めて厳しい責任が問われました 18。

この対比は、自動運転企業がグローバルに事業を展開する上で、単一の技術基準や安全基準を適用するだけでは不十分であることを示唆しています。各市場の交通文化、法制度、そして「何が社会的に許容されるか」という規範を深く理解し、それに合わせたリスクコミュニケーション戦略を構築することが不可欠です。中国のようにルール遵守を厳格に問う社会と、米国のように結果責任や弱者保護の原則をより重視する社会とでは、同じ事象でもその受け止められ方、ひいては企業の事業継続性に与える影響が全く異なる可能性があるのです。

## **第4章：事故発生時における搭乗者の行動規範**

本章では、利用者がレベル4の自動運転車に乗車中に万が一事故に遭遇した場合に、具体的に何をすべきか（Do's）、そして何をすべきでないか（Don'ts）を、主要企業のプロトコルと一般的な事故対応の原則を統合して解説します。

### **4.1 自動運転車（レベル4）の緊急時プロトコル**

レベル4の自動運転車では、事故対応の主体は乗客ではなく、車両を遠隔で監視・管理する運用会社です。

* **Waymoのプロトコル（確立されたモデル）**:  
  1. **衝突検知と車両の自動停止**: 車両は衝突を検知すると、システムが自動的にブレーキをかけ、安全に停止します 63。  
  2. **遠隔サポートへの自動通知**: 衝突検知と同時に、Waymoのフリートレスポンス専門チームに自動で通知が送信されます 63。  
  3. **乗客への能動的な連絡**: サポートチームは、車内に設置されたスピーカーまたは乗客が登録した個人の電話番号を通じて、直ちに乗客に連絡を取り、状況の確認と安心の提供に努めます 64。  
  4. **緊急サービスへの通報**: 状況に応じて（例：負傷者の発生、車両が交通を妨げている場合など）、サポートチームが911（救急・警察）に通報します 63。  
  5. **現場への専門チーム派遣**: 必要に応じて、Waymoのロードサイドアシスタンスチームが現場に派遣され、乗客のケアや車両の回収にあたります 63。  
  6. **警察との対話**: 車両が警察に停止を求められた場合も、システムがパトカーの灯火やサイレンを検知して安全に停車します。その後、遠隔サポートチームが車内スピーカーを通じて警察官と直接対話し、必要な情報提供や状況説明を行います 64。  
* Baiduのプロトコル:  
  Baiduは、緊急時に「5G遠隔運転サービス」というシステムを活用します。これにより、遠隔地にいる人間のオペレーターが、車両のハンドル、アクセル、ブレーキを直接操作することが可能です 66。これは、Waymoが遠隔からの介入を「アドバイス」や「提案」に留めているのとは異なる、より直接的な介入モデルであり、思想の違いが表れています 68。

#### **乗客の役割の変容：「当事者」から「被保護者」へ**

これらのプロトコルは、自動運転車の事故における乗客の役割が、根本的に変容することを示しています。従来の自動車事故では、運転手はもちろん同乗者も、事故の「当事者」として警察への報告や相手方との情報交換といった行動が求められました。しかし、レベル4のAV事故では、人間ドライバーが存在しないため、事故対応の一次的な責任と操作能力は、乗客ではなく、車両を所有・運用する企業（の遠隔サポートセンター）に完全に移転します 63。

その結果、乗客に求められるのは、自己判断で能動的に行動することではなく、確立されたプロトコルに従い、専門家であるサポートチームからの指示を待つという、比較的受動的な役割となります。これは、航空機事故における乗客が、パイロットや客室乗務員の指示に従う「保護・管理される対象」となる構図に似ています。

この役割の変化は、乗客に安心感を与える一方で、状況を自らコントロールできないという無力感を生む可能性も秘めています。法的な観点からは、乗客の「作為・不作為」が事故の結果に影響を与える場面は極めて限定的になり、責任の所在は主に製造者（メーカー）や運用者（サービス提供者）に集中することになります。これは、将来の製造物責任法や新たな保険制度の設計に大きな影響を与える重要な変化です。

### **4.2 搭乗者が取るべき行動（Do's）**

以上のプロトコルと役割の変化を踏まえ、搭乗者が取るべき具体的な行動は以下の通りです。

1. **【最優先】冷静を保ち、車内に留まる (Stay Calm and Remain in the Vehicle)**: パニックは冷静な判断を妨げます 69。火災や水没といった二次的な危険が明白でない限り、車両は事故後に乗客を守る最も安全なシェルターとして機能します。シートベルトを締めたまま、遠隔サポートからの指示を待つことが基本です 64。  
2. **サポートセンターと通信する (Communicate with Rider Support)**: 車両からの連絡を待つだけでなく、車内のスクリーンや自身のスマートフォンアプリにあるサポートボタンを積極的に使用して、状況を報告し、指示を仰ぎましょう 64。自身の負傷の有無や程度、周囲の状況などを正確に伝えることが、迅速かつ適切な対応につながります。  
3. **緊急サービスの指示に従う (Follow Instructions from Emergency Services)**: 警察や救急隊が現場に到着した場合は、彼らの指示が最優先となります。遠隔サポートチームは彼らと連携して対応を進めるため、安心して指示に従ってください 63。  
4. **証拠を保全する (Document the Scene)**: 自身と周囲の安全が完全に確保された後、もし可能であれば、スマートフォンのカメラで事故現場、自車および相手車両の損傷状態、道路状況などを多角的に撮影しておきましょう 70。これらの記録は、後の保険請求や法的手続きにおいて重要な証拠となる可能性があります。  
5. **医療機関を受診する (Seek Medical Attention)**: 事故直後は興奮状態にあり、アドレナリンの影響で痛みを感じにくいことがあります。目に見える外傷がなくても、あるいは軽微だと感じても、必ず医療機関で専門的な診断を受けることが極めて重要です 72。

### **4.3 搭乗者が行うべきでない行動（Don'ts）**

一方で、状況を悪化させかねない、避けるべき行動もあります。

1. **車両を自分で操作しようとしない (Do Not Attempt to Operate the Vehicle)**: 事故後の車両は、安全のためにシステムがロックダウンしている可能性が高いです。専門家以外が手動での移動や再起動を試みることは、予期せぬ動作を引き起こす可能性があり危険です 63。  
2. **現場で責任について言及しない (Do Not Admit Fault or Speculate on Liability)**: AV事故の責任所在は、ソフトウェア、ハードウェア、運用者、相手方ドライバーなど、複数の要因が絡み合う極めて複雑な問題です。現場で「自分のせいかもしれない」「相手が全面的に悪い」といった断定的な発言や憶測を述べることは、後の調査や交渉で不利に働く可能性があるため、厳に慎むべきです 71。事実は、専門家による詳細なデータ解析によって客観的に明らかになります。  
3. **不必要に車外に出ない (Do Not Exit the Vehicle Unnecessarily)**: 交通量の多い道路では、後続車による二次被害のリスクが常に存在します。遠隔サポートや緊急サービスから安全が確認され、車外への移動指示があるまで、車内待機が原則です 64。  
4. **ソーシャルメディアへの即時投稿を控える (Refrain from Posting on Social Media Immediately)**: 事故直後の混乱した状況で、不正確な情報や感情的な内容を投稿することは、後に法的な争点となったり、プライバシーの侵害につながったりする可能性があります。事実関係が確定するまで、公の場での発信は慎重に行うべきです 74。  
5. **保険会社との安易な交渉に応じない (Do Not Settle with Insurance Companies Hastily)**: AV事故は前例が少なく、適切な補償額を個人で判断することは困難です。特に負傷している場合は、弁護士などの法律専門家に相談し、正当な権利を理解するまで、保険会社からの示談提案に安易に同意すべきではありません 73。

## **結論と将来展望**

本報告書では、完全自動運転の現状、安全性、そして事故発生時の対応について、グローバルな視点から詳細な調査と分析を行いました。以下に、その総括と将来に向けた展望を述べます。

### **4.1 総括：現状の到達点と残された課題**

* **到達点**: SAEレベル5の「完全自動運転」は未だ実現していませんが、レベル4の「高度運転自動化」は、米国や中国の特定都市において、ロボタクシーという形で商業化が始まるという重要なマイルストーンに到達しました。安全性に関する初期データは、特に重篤な傷害や死亡に至る事故の発生率において、自動運転車が人間ドライバーを統計的に上回る大きな可能性を秘めていることを示唆しています 39。  
* **残された課題**: 技術面では、Cruise社の事故が示したように、複数の事象が連鎖する複雑な「エッジケース」への対応能力が最大の課題として残っています。規制面では、米国、中国、欧州で異なるアプローチが採られており、これがグローバルな標準化と普及の障壁となっています 10。社会的受容性の面では、事故発生時の徹底した透明性の確保と、自動運転車の「非人間的」で慎重すぎる運転スタイルに対する人間ドライバーの理解促進が不可欠です。

### **4.2 将来展望：技術・規制・社会の進化**

自動運転技術を取り巻く環境は、今後も急速に進化し続けると予測されます。

* **技術の進化**: レベル5への飛躍的な進化よりも、より現実的で漸進的なアプローチが主流となるでしょう。具体的には、レベル4ロボタクシーの運用設計領域（ODD）が都市部で段階的に拡大していくと同時に、レベル2+（高度運転支援システム）が自家用車に広く普及し、人間のドライバーをより高度に支援する形での進化が進むと考えられます 5。  
* **規制の進化**: 各国政府は、安全性を確保しつつイノベーションを促進するための法整備を加速させます。米国では連邦レベルでの統一的な規制枠組みの構築が 11、欧州ではEU全体での規制調和が 10、そして中国では安全性を最優先した規制強化と標準化 30 が、それぞれ今後の重要な焦点となります。また、従来のハードウェア中心の安全検査に加え、ソフトウェアの検証やサイバーセキュリティ対策を含む、より頻繁で厳格な車両検査制度が導入される可能性があります 23。  
* **倫理的・社会的議論の深化**: 「トロリー問題」のような単純化された二者択一の思考実験から、より現実的な倫理的課題へと議論の焦点が移ります。すなわち、システムが衝突不可避の状況でどのようにリスクを計算し、異なる道路利用者（乗客、他の車両、歩行者など）にリスクを配分するかという、より複雑な問題です 51。さらに、自動運転車が収集する膨大な移動データのプライバシー保護や、トラック運転手やタクシー運転手といった職業の将来像も、避けては通れない重要な社会課題となります 77。

### **4.3 最終提言**

本調査結果に基づき、関係各者に対して以下の提言を行います。

* **政策立案者へ**: 国際的な規制の調和と標準化に向けた議論を主導し、データの「報告バイアス」を考慮した客観的な安全評価基準を確立すべきです。また、AVが関与する重大事故の原因を中立的な立場で調査し、教訓を業界全体で共有するための独立した事故調査機関の設立を検討することが望まれます。  
* **事業者（自動車メーカー・テクノロジー企業）へ**: 技術開発においては、Cruiseの事例を教訓とし、複雑なエッジケースへの対応能力向上を最優先課題とすべきです。同時に、技術的な優位性だけでなく、事故発生時の徹底した透明性と迅速かつ誠実な情報開示を保証する、高い倫理観に基づいた企業文化を醸成することが、長期的な社会の信頼を獲得する上で不可欠です。  
* **社会全体へ**: 自動運転技術は「完璧な安全」を保証する魔法の杖ではなく、「人間よりも統計的に安全な移動手段」を目指すものであるという、現実的な期待値を共有することが重要です。その上で、自動運転がもたらす交通死亡事故の削減、移動の自由の拡大といった多大な便益と、依然として残存するリスクを社会全体でどのように評価し、受容していくかについて、開かれた対話を継続していく必要があります。

#### **引用文献**

1. Level 5 Autonomy: How Close Are We to Fully Self-Driving Cars? (Latest Industry Stats), 6月 29, 2025にアクセス、 [https://patentpc.com/blog/level-5-autonomy-how-close-are-we-to-fully-self-driving-cars-latest-industry-stats](https://patentpc.com/blog/level-5-autonomy-how-close-are-we-to-fully-self-driving-cars-latest-industry-stats)  
2. The 6 Levels of Autonomous Driving Explained-C\&T Solution Inc. 智愛科技股份有限公司, 6月 29, 2025にアクセス、 [https://www.candtsolution.com/news\_events-detail/the-six-level-of-autonomous-driving-explained/](https://www.candtsolution.com/news_events-detail/the-six-level-of-autonomous-driving-explained/)  
3. 【誰でもわかる】自動運転レベルの定義とは？実用化の目安も解説 \- アピステ, 6月 29, 2025にアクセス、 [https://www.apiste.co.jp/column/detail/id=4795](https://www.apiste.co.jp/column/detail/id=4795)  
4. 自動運転レベルとは？0～5の各レベルの定義や対象車種・実用化の現状を解説, 6月 29, 2025にアクセス、 [https://pai-r.com/column/20250528/](https://pai-r.com/column/20250528/)  
5. SAE自動運転レベルと今後の市場 Namuga, 6月 29, 2025にアクセス、 [https://namuga.com/jpn/invest/news\_view.php?v\_seqno=241](https://namuga.com/jpn/invest/news_view.php?v_seqno=241)  
6. 自動運転のレベル分けとは？レベル0～5までを一挙解説 \- スマートシティ/モビリティ \- マクニカ, 6月 29, 2025にアクセス、 [https://www.macnica.co.jp/business/maas/columns/135343/](https://www.macnica.co.jp/business/maas/columns/135343/)  
7. 自動運転のレベル0～5までの定義と車種一覧｜レベル5はいつ実現するのか？, 6月 29, 2025にアクセス、 [https://staff.persol-xtech.co.jp/hatalabo/mono\_engineer/568.html](https://staff.persol-xtech.co.jp/hatalabo/mono_engineer/568.html)  
8. Guide to autonomous driving: what do AD Levels 1-5 really mean? \- EV in Focus, 6月 29, 2025にアクセス、 [https://www.evinfocus.com/guide-to-autonomous-driving-ad/](https://www.evinfocus.com/guide-to-autonomous-driving-ad/)  
9. 自動運転レベルの定義一覧【0･1･2･3･4･5の表】｜日本・海外の実装状況, 6月 29, 2025にアクセス、 [https://jidounten-lab.com/autonomous-level](https://jidounten-lab.com/autonomous-level)  
10. Regulations for Autonomous Vehicles: Where Do Countries Stand in 2024-2030? (Global Policy Trends) PatentPC, 6月 29, 2025にアクセス、 [https://patentpc.com/blog/regulations-for-autonomous-vehicles-where-do-countries-stand-in-2024-2030-global-policy-trends](https://patentpc.com/blog/regulations-for-autonomous-vehicles-where-do-countries-stand-in-2024-2030-global-policy-trends)  
11. Driving the Future of AV Regulations: Barriers to Large-Scale Development \- CSIS, 6月 29, 2025にアクセス、 [https://www.csis.org/analysis/driving-future-av-regulations-barriers-large-scale-development](https://www.csis.org/analysis/driving-future-av-regulations-barriers-large-scale-development)  
12. Waymo's robotaxis to start carrying passengers in Atlanta, expanding Uber partnership, 6月 29, 2025にアクセス、 [https://apnews.com/article/waymo-uber-robotaxis-atlanta-expansion-e8c1d1a379bb14785ec32e97877efd65](https://apnews.com/article/waymo-uber-robotaxis-atlanta-expansion-e8c1d1a379bb14785ec32e97877efd65)  
13. Service areas \- Waymo One Help, 6月 29, 2025にアクセス、 [https://support.google.com/waymo/answer/9059119?hl=en](https://support.google.com/waymo/answer/9059119?hl=en)  
14. Waymo \- Wikipedia, 6月 29, 2025にアクセス、 [https://en.wikipedia.org/wiki/Waymo](https://en.wikipedia.org/wiki/Waymo)  
15. Self-Driving Car Service \- Ride-Hailing in Phoenix, AZ \- Waymo, 6月 29, 2025にアクセス、 [https://waymo.com/waymo-one-phoenix/](https://waymo.com/waymo-one-phoenix/)  
16. Ride with Waymo One on Uber in Austin and Atlanta, 6月 29, 2025にアクセス、 [https://waymo.com/waymo-on-uber/](https://waymo.com/waymo-on-uber/)  
17. Cruise (autonomous vehicle) \- Wikipedia, 6月 29, 2025にアクセス、 [https://en.wikipedia.org/wiki/Cruise\_(autonomous\_vehicle)](https://en.wikipedia.org/wiki/Cruise_\(autonomous_vehicle\))  
18. Cruise to pay $1.5M penalty in connection with San Francisco pedestrian accident, NHTSA says \- CBS News, 6月 29, 2025にアクセス、 [https://www.cbsnews.com/sanfrancisco/news/nhtsa-robotaxi-cruise-pay-penalty-failing-report-san-francisco-crash-involving-pedestrian/](https://www.cbsnews.com/sanfrancisco/news/nhtsa-robotaxi-cruise-pay-penalty-failing-report-san-francisco-crash-involving-pedestrian/)  
19. Standing General Order on Crash Reporting for Automated Driving Systems \- NHTSA, 6月 29, 2025にアクセス、 [https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-06/ADS-SGO-Report-June-2022.pdf](https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-06/ADS-SGO-Report-June-2022.pdf)  
20. NHTSA Autonomous Vehicle Crash Data – Automated Driving Systems, SAE Levels 3-5, 6月 29, 2025にアクセス、 [https://archive.legmt.gov/content/Committees/Interim/2023-2024/Transportation/Meetings/241007-July-10-2024/03.020-nhtsa-av-crash-data-summary-2024-posting2.pdf](https://archive.legmt.gov/content/Committees/Interim/2023-2024/Transportation/Meetings/241007-July-10-2024/03.020-nhtsa-av-crash-data-summary-2024-posting2.pdf)  
21. NHTSA relaxes crash reporting and autonomous vehicle regulations \- Telematics Wire, 6月 29, 2025にアクセス、 [https://telematicswire.net/nhtsa-relaxes-crash-reporting-and-autonomous-vehicle-regulations/](https://telematicswire.net/nhtsa-relaxes-crash-reporting-and-autonomous-vehicle-regulations/)  
22. When will autonomous vehicles and self-driving cars hit the road? World Economic Forum, 6月 29, 2025にアクセス、 [https://www.weforum.org/stories/2025/05/autonomous-vehicles-technology-future/](https://www.weforum.org/stories/2025/05/autonomous-vehicles-technology-future/)  
23. Laws in the driverless future: what to expect \- Board of Innovation, 6月 29, 2025にアクセス、 [https://www.boardofinnovation.com/blog/laws-in-the-driverless-future-what-to-expect/](https://www.boardofinnovation.com/blog/laws-in-the-driverless-future-what-to-expect/)  
24. U.S. eases autonomous driving regulations as China invests heavily in industry \- Chosunbiz, 6月 29, 2025にアクセス、 [https://biz.chosun.com/en/en-industry/2025/01/21/XJDJ77VJEZCI5D4LYBZYYZZMEE/](https://biz.chosun.com/en/en-industry/2025/01/21/XJDJ77VJEZCI5D4LYBZYYZZMEE/)  
25. Baidu's Apollo Go autonomous Robotaxi service comes to Shenzhen, 6月 29, 2025にアクセス、 [http://en.caam.org.cn/Index/show/catid/2/id/1848.html](http://en.caam.org.cn/Index/show/catid/2/id/1848.html)  
26. Baidu Launches China's First 24/7 Robotaxi Service \- AiThority, 6月 29, 2025にアクセス、 [https://aithority.com/technology/baidu-launches-chinas-first-24-7-robotaxi-service/](https://aithority.com/technology/baidu-launches-chinas-first-24-7-robotaxi-service/)  
27. Baidu Wins China Capital City's First-Ever Permit to Provide Fully Driverless Ride-hailing Service \- PR Newswire, 6月 29, 2025にアクセス、 [https://www.prnewswire.com/news-releases/baidu-wins-china-capital-citys-first-ever-permit-to-provide-fully-driverless-ride-hailing-service-301774850.html](https://www.prnewswire.com/news-releases/baidu-wins-china-capital-citys-first-ever-permit-to-provide-fully-driverless-ride-hailing-service-301774850.html)  
28. Baidu Launches Commercial Fully Driverless Ride-Hailing Service in Shenzhen, Expanding Nationwide Operations \- PR Newswire, 6月 29, 2025にアクセス、 [https://www.prnewswire.com/news-releases/baidu-launches-commercial-fully-driverless-ride-hailing-service-in-shenzhen-expanding-nationwide-operations-301853087.html](https://www.prnewswire.com/news-releases/baidu-launches-commercial-fully-driverless-ride-hailing-service-in-shenzhen-expanding-nationwide-operations-301853087.html)  
29. L3/L4 Autonomous Driving and Startups Research Report, 2024 \- ResearchInChina, 6月 29, 2025にアクセス、 [http://www.researchinchina.com/Htmls/Report/2024/73955.html](http://www.researchinchina.com/Htmls/Report/2024/73955.html)  
30. China's MIIT tightens regulations on autonomous driving features, banning key functions, 6月 29, 2025にアクセス、 [https://carnewschina.com/2025/04/17/chinas-miit-tightens-regulations-on-autonomous-driving-features-banning-key-functions/](https://carnewschina.com/2025/04/17/chinas-miit-tightens-regulations-on-autonomous-driving-features-banning-key-functions/)  
31. China Bans Deceptive Autonomous Driving Claims \- CleanTechnica, 6月 29, 2025にアクセス、 [https://cleantechnica.com/2025/04/18/china-bans-deceptive-autonomous-driving-claims/](https://cleantechnica.com/2025/04/18/china-bans-deceptive-autonomous-driving-claims/)  
32. GAC takes safety lead on level 4 self-driving cars \- Tech in Asia, 6月 29, 2025にアクセス、 [https://www.techinasia.com/news/gac-takes-safety-lead-on-level-4-self-driving-cars](https://www.techinasia.com/news/gac-takes-safety-lead-on-level-4-self-driving-cars)  
33. China's MIIT tightens regulations on autonomous driving features, banning key functions : r/electricvehicles \- Reddit, 6月 29, 2025にアクセス、 [https://www.reddit.com/r/electricvehicles/comments/1k1flan/chinas\_miit\_tightens\_regulations\_on\_autonomous/](https://www.reddit.com/r/electricvehicles/comments/1k1flan/chinas_miit_tightens_regulations_on_autonomous/)  
34. New Level 4 Autonomous Driving Regulation propels Germany to driverless mobility, 6月 29, 2025にアクセス、 [https://auto2xtech.com/nautonomous-driving-regulation-l4-future-mobility/](https://auto2xtech.com/nautonomous-driving-regulation-l4-future-mobility/)  
35. Which are the top autonomous vehicle ready countries? \- Geospatial World, 6月 29, 2025にアクセス、 [https://geospatialworld.net/blogs/top-autonomous-vehicle-ready-countries/](https://geospatialworld.net/blogs/top-autonomous-vehicle-ready-countries/)  
36. Standing General Order on Crash Reporting \- NHTSA, 6月 29, 2025にアクセス、 [https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting](https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting)  
37. Autonomous Vehicle Collision Reports \- California DMV \- CA.gov, 6月 29, 2025にアクセス、 [https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/](https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-collision-reports/)  
38. Autonomous Vehicles \- California DMV, 6月 29, 2025にアクセス、 [https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/](https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/)  
39. New Study: Waymo is reducing serious crashes and making streets safer for those most at risk, 6月 29, 2025にアクセス、 [https://waymo.com/blog/2025/05/waymo-making-streets-safer-for-vru](https://waymo.com/blog/2025/05/waymo-making-streets-safer-for-vru)  
40. Waymo Safety Impact, 6月 29, 2025にアクセス、 [https://waymo.com/safety/impact/](https://waymo.com/safety/impact/)  
41. New Swiss Re study: Waymo is safer than even the most advanced human-driven vehicles, 6月 29, 2025にアクセス、 [https://waymo.com/blog/2024/12/new-swiss-re-study-waymo](https://waymo.com/blog/2024/12/new-swiss-re-study-waymo)  
42. Research & Discoveries (R\&D): Cruise's Safety Record Over 1 Million Driverless Miles, 6月 29, 2025にアクセス、 [https://theavindustry.org/resources/blog/research-discoveries-rd-cruises-safety-record-over-1-million-driverless-miles](https://theavindustry.org/resources/blog/research-discoveries-rd-cruises-safety-record-over-1-million-driverless-miles)  
43. Autonomous Vehicle Accidents: 7 Facts and Statistics \- RMD Law, 6月 29, 2025にアクセス、 [https://www.rmdlaw.com/blog/autonomous-vehicle-accidents-facts-statistics/](https://www.rmdlaw.com/blog/autonomous-vehicle-accidents-facts-statistics/)  
44. Examining Autonomous Car Accidents and Statistics \- Lee, Gober & Reyna, 6月 29, 2025にアクセス、 [https://www.lgrlawfirm.com/blog/examining-autonomous-car-accidents-and-statistics-2/](https://www.lgrlawfirm.com/blog/examining-autonomous-car-accidents-and-statistics-2/)  
45. Self-Driving Car Accident Statistics \- CarAccidentAttorney.com, 6月 29, 2025にアクセス、 [https://caraccidentattorney.com/blog/self-driving-car-accident-statistics/](https://caraccidentattorney.com/blog/self-driving-car-accident-statistics/)  
46. Research & Discoveries (R\&D): Waymo Reduces Crash Rates Compared to Human Drivers Over 7+ Million AV Miles \- The Autonomous Vehicle Industry Association, 6月 29, 2025にアクセス、 [https://www.theavindustry.org/blog/waymo-reduces-crash-rates-compared-to-human-drivers](https://www.theavindustry.org/blog/waymo-reduces-crash-rates-compared-to-human-drivers)  
47. Comparing Crash Rates of Waymo and those of Human Drivers, 6月 29, 2025にアクセス、 [https://thelastdriverlicenseholder.com/2023/12/20/comparing-crash-rates-of-waymo-and-those-of-human-drivers/](https://thelastdriverlicenseholder.com/2023/12/20/comparing-crash-rates-of-waymo-and-those-of-human-drivers/)  
48. Comparison of Waymo rider-only crash data to human benchmarks at 7.1 million miles, 6月 29, 2025にアクセス、 [https://waymo.com/research/comparison-of-waymo-rider-only-crash-data-to-human/](https://waymo.com/research/comparison-of-waymo-rider-only-crash-data-to-human/)  
49. How would autonomous vehicles behave in real-world crash scenarios? \- PubMed, 6月 29, 2025にアクセス、 [https://pubmed.ncbi.nlm.nih.gov/38657314/](https://pubmed.ncbi.nlm.nih.gov/38657314/)  
50. Waymo's Crashes Are Largely The Fault Of Us Mere Humans \- Jalopnik, 6月 29, 2025にアクセス、 [https://www.jalopnik.com/1820845/waymo-car-crash-statistics/](https://www.jalopnik.com/1820845/waymo-car-crash-statistics/)  
51. Ethical Decision-Making for Self-Driving Vehicles: A Proposed Model & List of Value-Laden Terms that Warrant (Technical) Specification \- PubMed Central, 6月 29, 2025にアクセス、 [https://pmc.ncbi.nlm.nih.gov/articles/PMC11466986/](https://pmc.ncbi.nlm.nih.gov/articles/PMC11466986/)  
52. Anatomy of a Robotaxi Crash: Lessons from the Cruise Pedestrian Dragging Mishap \- Electrical and Computer Engineering, 6月 29, 2025にアクセス、 [https://users.ece.cmu.edu/\~koopman/cruise/Koopman2024\_CruiseMishap\_arXiv\_Preprint.pdf](https://users.ece.cmu.edu/~koopman/cruise/Koopman2024_CruiseMishap_arXiv_Preprint.pdf)  
53. One crash set off a new era for self-driving cars in S.F. Here's a complete look at what happened, 6月 29, 2025にアクセス、 [https://www.sfchronicle.com/projects/2024/cruise-sf-collision-timeline/](https://www.sfchronicle.com/projects/2024/cruise-sf-collision-timeline/)  
54. Cruise Returns to Bay Area a Year After Pedestrian Crash \- GovTech, 6月 29, 2025にアクセス、 [https://www.govtech.com/transportation/cruise-returns-to-bay-area-a-year-after-pedestrian-crash](https://www.govtech.com/transportation/cruise-returns-to-bay-area-a-year-after-pedestrian-crash)  
55. Lessons from the Cruise Robotaxi Pedestrian Dragging Mishap \- Electrical and Computer Engineering, 6月 29, 2025にアクセス、 [https://users.ece.cmu.edu/\~koopman/cruise/Koopman2024\_CruiseMishap\_IEEEReliabilityMagazine.pdf](https://users.ece.cmu.edu/~koopman/cruise/Koopman2024_CruiseMishap_IEEEReliabilityMagazine.pdf)  
56. NHTSA Announces Consent Order with Cruise After Company Failed to Fully Report Crash Involving Pedestrian, 6月 29, 2025にアクセス、 [https://www.nhtsa.gov/press-releases/consent-order-cruise-crash-reporting](https://www.nhtsa.gov/press-releases/consent-order-cruise-crash-reporting)  
57. Waymo recalls roughly 1,200 self-driving vehicles prone to hitting road barriers \- CBS News, 6月 29, 2025にアクセス、 [https://www.cbsnews.com/news/waymo-car-recall-software-crash-self-driving/](https://www.cbsnews.com/news/waymo-car-recall-software-crash-self-driving/)  
58. Waymo \- ODI RESUME, 6月 29, 2025にアクセス、 [https://static.nhtsa.gov/odi/inv/2024/INOA-PE24016-12382.pdf](https://static.nhtsa.gov/odi/inv/2024/INOA-PE24016-12382.pdf)  
59. Baidu Robotaxi Accident Shines Spotlight on Safety of Unmanned Cars \- Caixin Global, 6月 29, 2025にアクセス、 [https://www.caixinglobal.com/2024-07-12/baidu-robotaxi-accident-shines-spotlight-on-safety-of-unmanned-cars-102215580.html](https://www.caixinglobal.com/2024-07-12/baidu-robotaxi-accident-shines-spotlight-on-safety-of-unmanned-cars-102215580.html)  
60. Baidu ride-hailing driverless car hits pedestrian crossing street \- AIAAIC, 6月 29, 2025にアクセス、 [https://www.aiaaic.org/aiaaic-repository/ai-algorithmic-and-automation-incidents/baidu-ride-hailing-driverless-car-hits-pedestrian-crossing-street](https://www.aiaaic.org/aiaaic-repository/ai-algorithmic-and-automation-incidents/baidu-ride-hailing-driverless-car-hits-pedestrian-crossing-street)  
61. A driverless car hits a person crossing against the light in China AP News, 6月 29, 2025にアクセス、 [https://apnews.com/article/china-autonomous-driving-accident-baidu-b0b4527ff355836f2df03868ff0bd0fc](https://apnews.com/article/china-autonomous-driving-accident-baidu-b0b4527ff355836f2df03868ff0bd0fc)  
62. Baidu's driverless test vehicle rear-ended during normal driving \- CnEVPost, 6月 29, 2025にアクセス、 [https://cnevpost.com/2022/06/08/baidus-driverless-test-vehicle-rear-ended-during-normal-driving/](https://cnevpost.com/2022/06/08/baidus-driverless-test-vehicle-rear-ended-during-normal-driving/)  
63. Waymo Emergency Response Guide and Law Enforcement Interaction Protocol (October 2023\) \- Scribd, 6月 29, 2025にアクセス、 [https://www.scribd.com/document/875970573/Waymo-Emergency-Response-Guide-and-Law-Enforcement-Interaction-Protocol-October-2023](https://www.scribd.com/document/875970573/Waymo-Emergency-Response-Guide-and-Law-Enforcement-Interaction-Protocol-October-2023)  
64. Pulling over, collisions, and security events \- Waymo One Help, 6月 29, 2025にアクセス、 [https://support.google.com/waymo/answer/9449023?hl=en](https://support.google.com/waymo/answer/9449023?hl=en)  
65. Waymo Emergency Response Guide and Law Enforcement Interaction Protocol (October 2023\) \- Googleapis.com, 6月 29, 2025にアクセス、 [https://storage.googleapis.com/waymo-uploads/files/documents/first-responders/Waymo%20Emergency%20Response%20Guide%20and%20Law%20Enforcement%20Interaction%20Protocol%20(October%202023)%20-%20240122.pdf](https://storage.googleapis.com/waymo-uploads/files/documents/first-responders/Waymo%20Emergency%20Response%20Guide%20and%20Law%20Enforcement%20Interaction%20Protocol%20\(October%202023\)%20-%20240122.pdf)  
66. Baidu Apollo launches robotaxis without safety driver in Beijing \- Traffic Technology Today, 6月 29, 2025にアクセス、 [https://www.traffictechnologytoday.com/news/autonomous-vehicles/baidu-apollo-launches-robotaxis-without-safety-driver-in-beijing.html](https://www.traffictechnologytoday.com/news/autonomous-vehicles/baidu-apollo-launches-robotaxis-without-safety-driver-in-beijing.html)  
67. Baidu Apollo's 5G Remote Driving Service \- YouTube, 6月 29, 2025にアクセス、 [https://www.youtube.com/watch?v=QOIOEca2dhU](https://www.youtube.com/watch?v=QOIOEca2dhU)  
68. Comparing Robotaxis: Baidu's Apollo and Alphabet's Waymo \- Stanford CIS, 6月 29, 2025にアクセス、 [https://cyberlaw.stanford.edu/blog/2025/05/comparing-robotaxis-baidus-apollo-and-alphabets-waymo/](https://cyberlaw.stanford.edu/blog/2025/05/comparing-robotaxis-baidus-apollo-and-alphabets-waymo/)  
69. How to Survive a Car Crash as a Passenger: Tips for Safety, 6月 29, 2025にアクセス、 [https://hirejared.com/accidents/how-to-survive-a-car-crash-as-a-passenger/](https://hirejared.com/accidents/how-to-survive-a-car-crash-as-a-passenger/)  
70. What To Do After Being Injured On A Cruise Ship Step By Step, 6月 29, 2025にアクセス、 [https://www.sneedmitchell.com/post/what-to-do-after-being-injured-on-a-cruise-ship-step-by-step](https://www.sneedmitchell.com/post/what-to-do-after-being-injured-on-a-cruise-ship-step-by-step)  
71. What to Do If You're Hit by a Self-Driving Car The Zebra, 6月 29, 2025にアクセス、 [https://www.thezebra.com/resources/driving/self-driving-car-crashes/](https://www.thezebra.com/resources/driving/self-driving-car-crashes/)  
72. 4 Dangers of Self Driving Cars Hazard & Safety Tips, 6月 29, 2025にアクセス、 [https://www.hoffmanlawfirm.com/blog/the-dangers-of-self-driving-cars-2](https://www.hoffmanlawfirm.com/blog/the-dangers-of-self-driving-cars-2)  
73. Autonomous Vehicles Are Here: What to Do In Case Of An Accident \- Tampa Personal Injury Lawyer, 6月 29, 2025にアクセス、 [https://www.accidenttampa.com/autonomous-vehicles-are-here-what-to-do-in-case-of-an-accident/](https://www.accidenttampa.com/autonomous-vehicles-are-here-what-to-do-in-case-of-an-accident/)  
74. Cruise Ship Accident: What to Do if You're Injured on a Cruise Ship \- Dawson Law Firm, 6月 29, 2025にアクセス、 [https://dawsonlawfirm.com/cruise-ship-accident-what-to-do-if-youre-injured-on-a-cruise-ship/](https://dawsonlawfirm.com/cruise-ship-accident-what-to-do-if-youre-injured-on-a-cruise-ship/)  
75. A More Practical Future for Autonomous Vehicles S\&P Global, 6月 29, 2025にアクセス、 [https://www.spglobal.com/automotive-insights/en/blogs/fuel-for-thought-a-more-practical-future-for-autonomous-vehicles](https://www.spglobal.com/automotive-insights/en/blogs/fuel-for-thought-a-more-practical-future-for-autonomous-vehicles)  
76. “All things equal”: ethical principles governing why autonomous vehicle experts change or retain their opinions in trolley problems—a qualitative study \- Frontiers, 6月 29, 2025にアクセス、 [https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1544272/epub](https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1544272/epub)  
77. Navigating The Ethical Dilemmas Of Self-Driving Cars: Who Decides When Safety Is At Risk? \- Forbes, 6月 29, 2025にアクセス、 [https://www.forbes.com/councils/forbestechcouncil/2024/10/23/navigating-the-ethical-dilemmas-of-self-driving-cars-who-decides-when-safety-is-at-risk/](https://www.forbes.com/councils/forbestechcouncil/2024/10/23/navigating-the-ethical-dilemmas-of-self-driving-cars-who-decides-when-safety-is-at-risk/)
