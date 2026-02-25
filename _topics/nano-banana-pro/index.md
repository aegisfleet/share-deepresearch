---
audio: /share-deepresearch/assets/audio/nano-banana-pro.m4a
category: ai
date: 2025-11-26
description: 本レポートは、Googleの最新画像生成モデル「Nano Banana Pro」（正式名称：Gemini 3 Pro Image）を用いて、スライド資料全体の視覚的トーン（雰囲気、照明、配色、描画スタイル）を統一するための技術的アプローチと実践的ワークフローを詳細に調査・分析したものである。
ga4_metrics:
  avgSessionDuration: 173.469446
  pageViews: 4
  users: 3
layout: topic
prompt: Nano Banana Proを使ってスライドの資料を作成したいのだが、生成される画像のスタイル（雰囲気）が毎回違うので、統一させるテクニックを調査して欲しい。
supplementary_materials:
- pdf: /share-deepresearch/topics/nano-banana-pro/slide.pdf
  title: スライド資料
tags:
- AIツール
- Gemini
title: Nano Banana Pro (Gemini 3 Pro Image) を活用したプレゼンテーション資料における視覚的一貫性の確立とスタイル制御に関する包括的技術レポート
video: /share-deepresearch/assets/video/nano-banana-pro.mp4
---

# **Nano Banana Pro (Gemini 3 Pro Image) を活用したプレゼンテーション資料における視覚的一貫性の確立とスタイル制御に関する包括的技術レポート**

## **1\. エグゼクティブサマリー**

企業コミュニケーションや学術発表の現場において、生成AIを活用した資料作成は生産性を劇的に向上させる一方で、成果物の「スタイルの一貫性（Consistency）」の欠如という新たな課題をもたらしている。特にスライド資料（プレゼンテーションデッキ）においては、各スライドが個別の芸術作品として独立しているのではなく、全体として統一されたブランドアイデンティティとナラティブを持つことが不可欠である。本レポートは、Googleの最新画像生成モデル「Nano Banana Pro」（正式名称：Gemini 3 Pro Image）を用いて、スライド資料全体の視覚的トーン（雰囲気、照明、配色、描画スタイル）を統一するための技術的アプローチと実践的ワークフローを詳細に調査・分析したものである。

調査の結果、従来の画像生成モデルが確率的な画素操作に依存していたのに対し、Nano Banana Proは「Gemini 3」の推論エンジンを基盤とした「文脈理解」と「論理的構築」を行う点が決定的に異なることが判明した 1。この特性を活かし、スタイルの統一を図るためには、単なるテキストプロンプトの工夫（Prompt Engineering）を超え、複数の参照画像をアンカーとして利用する「マルチモーダル・アンカー戦略」や、撮影環境を論理的に定義する「仮想スタジオ・プロトコル」の実装が必要不可欠である。

本レポートでは、14枚の画像をコンテキストウィンドウに入力してスタイルを固定する手法 2、構造化されたプロンプト設計、そしてGoogle Workspaceに統合された「Beautify」機能の活用法 4 を中心に、偶発性を排除し、決定論的なビジュアル生成を実現するための体系的なメソドロジーを提言する。

---

## **2\. 序論：生成AI時代のプレゼンテーションデザインにおける課題**

### **2.1 ストキャスティック（確率的）生成とブランドの一貫性**

生成AI、特に拡散モデル（Diffusion Models）を用いた画像生成は、本質的に確率的なプロセスである。ユーザーが「会議室の風景」と入力した際、AIは学習データの中から無数の「会議室」の概念を探索し、ノイズを除去しながら画像を構築する。この過程において、ある時は「自然光が差し込む明るい北欧風のオフィス」が生成され、次の瞬間には「薄暗くドラマチックな映画風の会議室」が生成されるという現象が発生する。これを「スタイルドリフト（Style Drift）」と呼ぶ。

プレゼンテーション資料において、スライドごとに画風が写真調、イラスト調、3Dレンダリング調と変動することは、聴衆の認知負荷を高め、情報の信頼性を損なう要因となる。したがって、プロフェッショナルな資料作成においては、AIの創造性を意図的に抑制し、特定の視覚的ルール（トーン＆マナー）に準拠させる技術が求められる。

### **2.2 Nano Banana Pro (Gemini 3 Pro Image) の位置づけ**

Nano Banana Proは、Google DeepMindが開発したGemini 3モデルを基盤とする画像生成・編集モデルであり、従来の「Gemini 2.5 Flash Image（旧Nano Banana）」の上位版にあたる 2。本モデルの最大の特徴は、単なるテキストから画像への変換（Text-to-Image）ではなく、高度な推論能力と実世界知識（World Knowledge）を組み合わせた「視覚的思考」を行う点にある 3。

具体的には、照明、空間、テクスチャ、被写体のアイデンティティがどのように相互作用するかを「建築的」な感覚で理解しており、ピクセルを操作するのではなく、シーンの照明環境そのものを再構築することが可能である 1。この推論能力こそが、スタイルの統一を実現するための鍵となる。また、最大14枚の参照画像を入力可能なコンテキストウィンドウや、スライド内のテキストレンダリング能力の向上など、プレゼンテーション作成に特化した機能強化が図られている 2。

---

## **3\. アーキテクチャ分析：なぜスタイルは変動するのか、どう制御すべきか**

スタイルの統一技法を論じる前に、Nano Banana Proの内部動作原理と、それが従来のモデルといかに異なるかを理解する必要がある。

### **3.1 推論エンジン「Gemini 3」による解釈プロセス**

Nano Banana Proは、プロンプトを受け取ると即座に描画を開始するのではなく、まず「思考プロセス（Thinking Process）」を経る 3。これは、ユーザーの曖昧な指示を解釈し、不足している情報を補完する段階である。

例えば、「マーケティングの成功を示すスライド背景」というプロンプトに対し、モデルは以下のような推論を行う可能性がある：

* **推論A:** 「成功＝上昇トレンド。マーケティング＝デジタル。よって、サイバーパンク風のネオンカラーで上昇するグラフを描画しよう。」  
* **推論B:** 「成功＝信頼。マーケティング＝ビジネス。よって、落ち着いた青色を基調とした、清潔感のあるオフィスのミニマルな写真にしよう。」

この推論の分岐こそが、スタイル不一致の根源である。ユーザーがスタイルに関する厳密な制約を与えない限り、AIは毎回異なる「正解」を導き出そうとする。したがって、一貫性を保つためには、AIの推論の余地を極限まで狭め、特定の視覚的パラメータを「定数」として与える必要がある。

### **3.2 潜在空間（Latent Space）のナビゲーション**

画像生成モデルの学習データは、多次元の「潜在空間」に分布している。スタイルの一貫性を保つということは、この広大な空間の中で、常に同じ「近傍（Neighborhood）」からサンプリングを行うことを意味する。

Nano Banana Proにおける「Pro」の機能、特に参照画像の入力機能は、このサンプリング位置をテキスト（言語）ではなく、ベクトルデータ（画像）によって直接指定するものである。言語による指示（例：「青くてかっこいい」）は解釈の幅が広いが、画像データは解釈の揺らぎが少ないため、より強力なアンカーとして機能する。

### **3.3 テキストレンダリングと多言語対応の進化**

スライド資料において、図解の中に文字を含めるケースは多い。従来のモデルでは、画像内の文字が判読不能な記号列になることが多かったが、Nano Banana Proはテキストレンダリングのエラー率が極めて低く、多言語に対応している 6。これは、スライド内のインフォグラフィックやチャートを生成する際に、後から画像編集ソフトで文字を乗せる手間を省けるだけでなく、文字のフォントやスタイル自体をデザインの一部として統合できることを意味する。

---

## **4\. コア戦略1：マルチモーダル・アンカー戦略（参照画像の活用）**

Nano Banana Proの最も強力な機能であり、スタイル統一の決定打となるのが、最大14枚の画像を入力できるコンテキストウィンドウの活用である 2。これを「ビジュアル・スタイルガイド」として機能させることで、言葉では表現しきれない微細なニュアンスをモデルに強制することができる。

### **4.1 「スタイル・バイブル（Style Bible）」の構築**

スライド作成プロジェクトを開始する前に、そのプレゼンテーションの視覚的ルールを定義する3〜5枚の画像セット（スタイル・バイブル）を用意する。これを毎回プロンプトと共に入力することで、モデルの出力を特定のスタイル領域に固定する。

**スタイル・バイブルの構成要素:**

1. **カラーパレット・アンカー:** ブランドカラー（コーポレートカラー）を含む抽象的な画像や、配色パレットそのもの。これにより、モデルが使用する色彩空間を制限する 9。  
2. **ライティング・アンカー:** 理想とする照明条件（例：スタジオライティング、自然光、フラットな影なし）を体現した写真やレンダリング画像。  
3. **コンポジション・アンカー:** 情報密度や余白の取り方を示す画像。スライド用画像の場合、テキストを配置するための「ネガティブスペース（余白）」が確保された画像を読み込ませることが重要である。  
4. **オブジェクト/キャラクター・アンカー:** 特定の製品やマスコットキャラクターを登場させる場合、その三面図や別アングルの画像を読み込ませることで、形状の一貫性を保つ（キャラクターの一貫性は最大5体まで保持可能） 10。

### **4.2 具体的なワークフロー：厳格な参照（Strict Reference）**

Nano Banana Proのインターフェース（またはAPI）において、以下の手順で生成を行う 9。

1. **アップロード:** スタイル・バイブルとして選定した画像をアップロードする。  
2. **指示の記述:** アップロードした画像をどのように扱うかを明示的に指示する。単に画像をアップロードするだけでは、AIがそれを「被写体」として認識するのか「スタイル」として認識するのか迷う可能性がある。  
   * *プロンプト例:* 「アップロードした画像1と画像2を\*\*厳格なスタイル参照（Strict Style Reference）\*\*として使用してください。画像3のカラーパレットを適用し、画像1の照明条件とテクスチャ感を再現してください。そのスタイルで、\[新しい被写体\] を描画してください。」  
3. **スタイルの継承:** これにより、例えば「上昇するグラフ」を描画する際にも、アンカー画像にある「マットな質感」や「特定の青色」が自動的に適用される。

### **4.3 事例：ブランドキットの適用**

Sider.AIやAtlabsなどのサードパーティツールを経由する場合や、Google WorkspaceのEnterprise版を使用する場合、企業のブランドアセット（ロゴ、フォント、製品画像）をアップロードし、それを「ブランドキット」として定義することが可能である 9。

ケーススタディ：コーヒーブランドの冬のキャンペーン  
あるコーヒーブランドが冬のキャンペーン資料を作成する際、以下のプロンプトを使用した事例がある 14。

* **参照画像:** 商品の靴の画像3枚。  
* **プロンプト:** 「これらを1つのヒーローショットに組み合わせ、スタジオのソフトボックス照明のように調整し、右下にブランドの透かしを入れ、Webサイトのヒーロー用に2Kでレンダリングせよ。」  
* **結果:** モデルは参照画像の製品形状を維持しつつ、指定された照明スタイル（スタジオ・ソフトボックス）で統合した画像を生成した。これをスライド背景に応用することで、製品写真と背景デザインが完全に調和したスライドを作成できる。

---

## **5\. コア戦略2：セマンティック・プロンプトエンジニアリング（言語による制御）**

参照画像が用意できない場合、あるいは微調整が必要な場合は、言語による制御（プロンプトエンジニアリング）が重要となる。Nano Banana Proにおいては、形容詞を並べる「感覚的」なプロンプトよりも、撮影環境やレンダリング設定を定義する「構造的」なプロンプトが有効である。

### **5.1 「仮想スタジオ」プロトコル**

Nano Banana Proは物理的な光のシミュレーション能力が高いため、プロンプト内で「仮想的な撮影スタジオ」を構築する記述を行うと、出力が安定する 1。

不変のスタイルブロック（Immutable Style Block）:  
スライドの全ページで共通して使用するプロンプトの「定型句」を作成し、全ての生成指示の末尾に付加する。  
スタイルブロックの記述例（ミニマルな企業スライド用）:  
Style: Corporate Minimalist. Lighting: Global illumination, soft shadows, high-key brightness, no harsh contrast. Camera: 50mm lens, f/8 aperture (deep depth of field), isometric view. Texture: Smooth vector art style, matte finish. Color Palette: Cool grey background with accents of \#0055FF. Render: High fidelity, 4K resolution.

このブロックを固定することで、AIは毎回「同じスタジオ、同じカメラ、同じ照明」で撮影するという前提条件を共有することになる。特に「f値（絞り）」の指定は重要である。これを指定しないと、AIが勝手に背景をぼかしたり（被写界深度を浅くしたり）、逆にパンフォーカスにしたりとブレが生じるためである 6。

### **5.2 構造化プロンプト（JSON形式等の活用）**

Nano Banana Proの推論エンジンは、自然言語の長文よりも、構造化されたデータ形式（JSONやMarkdownのリスト形式）を解釈することに長けている場合がある 16。特にAPI経由や高度な生成を行う場合、パラメータを明確に分離することで、AIの「読み落とし」を防ぐことができる。

**スライド生成用プロンプトの構造例:**

#### **Role**

Professional Presentation Designer

#### **Task**

Generate a background image for a slide about "Quarterly Revenue Growth".

#### **Constraints (Do NOT change)**

* Style: Swiss Design Style (Clean, Grid-based)  
* Background Color: Pure White (\#FFFFFF)  
* Object Material: 3D Matte Ceramic  
* Lighting: Softbox from Top-Left  
* Negative Space: Leave the top-left 40% empty for text overlay

#### **Subject Description**

A stylized bar chart growing upwards, represented by simple geometric pillars.

このように「Constraints（制約条件）」と「Subject（被写体）」を明確に区別することで、モデルはスタイルを守りつつ、被写体だけを入れ替えるという動作を正確に実行できるようになる。

### **5.3 ネガティブプロンプトによるノイズ除去**

スライド資料において、不要な要素（ノイズ、過剰な装飾、判読不能な文字）は致命的である。これらを排除するために、「ネガティブプロンプト（何を描かないか）」を定義し、これも全スライドで統一する 18。

**スライド作成における推奨ネガティブプロンプト:**

blur, grain, noise, grunge, distressed texture, low resolution, watermark, text, signature, cartoon, 3D render (if aiming for 2D), uncanny valley, distorted perspective, oversaturated, dark, moody, cinematic vignetting, clutter, messy background.

特に「cinematic（映画風）」や「moody（ムードのある）」という単語は、AI画像生成において人気のあるスタイルだが、ビジネススライドとしては「暗すぎて文字が読めない」「ドラマチックすぎて内容が入ってこない」という結果になりがちであるため、ネガティブプロンプトで明示的に除外することが推奨される。

---

## **6\. コア戦略3：ワークフロー統合とネイティブ機能の活用**

Googleスライド等のGoogle Workspace環境でNano Banana Proを使用する場合、統合された機能を活用することで、より直感的に統一感を出すことができる。

### **6.1 「このスライドを美化（Beautify this slide）」機能**

Googleスライドには、Nano Banana Proをバックエンドに持つ「Beautify this slide（このスライドを美化）」という機能が実装されている（または順次ロールアウトされている） 4。この機能は、スライドに入力された箇条書きのテキストやラフなレイアウトを解析し、瞬時にプロフェッショナルなデザインに変換する。

一貫性を保つための「Beautify」活用法:  
この機能の最大の特徴は、スライドデッキ全体のテーマ（スライドマスター）を参照する点にある。

1. **スライドマスターの設定:** 最初に「テーマの編集」で、使用するフォント、色、背景スタイルを厳密に定義する。  
2. **テキストの入力:** 各スライドにはテキスト情報のみを入力する。  
3. **一括適用:** 各ページで「Beautify」を実行すると、AIはスライドマスターで定義されたルール（＝コンテキスト）に従って図解やレイアウトを生成する。これにより、ユーザーが毎回プロンプトを入力せずとも、デッキ全体で統一されたビジュアルが生成される。

### **6.2 インペインティング（部分編集）による修正**

生成された画像が「惜しい」場合、例えばスタイルは完璧だが不要なオブジェクトがある場合、画像を再生成（Regenerate）するとスタイルが変わってしまうリスクがある。これを防ぐために、**インペインティング（Inpainting）** または「部分編集」機能を使用する 21。

**手法:**

1. 修正したい領域（例：変な形のアイコン）をブラシで選択する。  
2. 修正指示（プロンプト）を入力する（例：「ここをシンプルな歯車のアイコンに置き換えて」）。  
3. **技術的利点:** Nano Banana Proは、選択されていない領域（周囲の背景）のピクセル情報（ライティング、ノイズ、解像度）を解析し、それに完全に馴染むように新しい部分を生成する 1。これにより、スタイルを崩すことなくコンテンツのみを修正できる。

---

## **7\. 高度なテクニックと応用シナリオ**

さらに高いレベルでの統一性を求めるユーザーや、大量の資料を作成するプロフェッショナル向けのテクニックを紹介する。

### **7.1 グリッド（マトリックス）生成法**

スライド内で使用する複数のアイコンやイラスト（例：4つのポイントを説明する図）が必要な場合、これらを1枚ずつ生成するのは非効率であり、スタイルズレの原因となる。

**手法:** 1枚の大きな画像として「4つのアイコンが並んだシート」を生成させる。

* **プロンプト例:** 「白背景に、青い線画スタイルで描かれた4つのアイコンのグリッドシート。左上：電球、右上：握手、左下：グラフ、右下：ターゲット。全てのアイコンは同じ線の太さとスタイルを持つこと。」  
* **メリット:** 1回の推論プロセス（Inference Pass）で生成されるため、照明計算、ノイズシード、画風の適用が完全に同一になる。生成後、トリミングして個別の画像として使用すれば、100%のスタイル一致が保証される 6。これは「1880年代から2025年までのポートレートグリッド」を作成するトレンド 23 と同じ原理の応用である。

### **7.2 シード値（Seed）の固定**

APIを利用する場合や、一部の高度なインターフェースでは「シード値」を指定できる場合がある 24。シード値とは、画像生成の初期ノイズを決定する乱数の種である。

* 同じプロンプト＋同じシード値＝完全に同じ画像。  
* **応用:** プロンプトの一部（被写体）だけを変えて、他のパラメータとシード値を固定することで、構図や雰囲気が非常に似通ったバリエーションを生成できる。ただし、拡散モデルの性質上、被写体が変わるとノイズの影響範囲も変わるため、参照画像（Core Strategy 1）ほど強力な固定力はない点に注意が必要である。

### **7.3 インフォグラフィックとデータビジュアライゼーション**

Nano Banana Proは、Google検索と連携してリアルタイムのデータに基づいたグラフや地図を生成する能力を持つ 9。

* **スタイル統一のコツ:** グラフを生成する際も、必ず「スタイルブロック（配色やフォント指定）」を含めること。「最新の株価チャート」とだけ頼むと、一般的なニュースサイト風のチャートが出てきてしまい、自社のスライドデザインと合わなくなる。  
* **プロンプト:** 「Google検索を使用して最新の金価格の推移を取得し、それを\*\*\[指定したカラーパレット\] を使用したミニマルな折れ線グラフ\*\*として描画せよ。背景は透明（または白）。」

---

## **8\. スタイル別プロンプトテンプレート集**

スライド資料で頻繁に使用されるスタイルについて、Nano Banana Proで再現性が高いプロンプト構成の例を以下に示す。これらをベースに、自社のブランドに合わせてカスタマイズすることを推奨する。

### **8.1 企業向けミニマル（Corporate Minimalist）**

清潔感、信頼、余白を重視するスタイル。

* **キーワード:** Knolling (並べる), Flat lay, High-key lighting, Soft shadows, Isometric, Clean lines, Negative space, Vector style.  
* **プロンプト構成:** arranged in a clean, flat-lay composition on a pure white background. Soft, shadowless studio lighting. Minimalist vector art style with a matte texture. Use a palette of Navy Blue and Light Grey. No gradients, no clutter. Ample negative space for text. 8

### **8.2 テック・フューチャリスティック（Tech / Futuristic）**

革新性、データ、未来感を演出するスタイル。

* **キーワード:** Cyberpunk, Neon, Data flow, Glassmorphism, Dark mode, Glowing edges, Connectivity, Node network.  
* **プロンプト構成:** visualization in a futuristic glassmorphism style. Dark background (Deep Blue/Black) with glowing neon cyan data lines. 3D render with shallow depth of field focusing on the center object. Bokeh effect in the background. High contrast, sharp details.

### **8.3 創造的・手書き風（Creative / Hand-drawn）**

親しみやすさ、アイデア、ブレインストーミングの段階を示すスタイル。

* **キーワード:** Watercolor, Sketch, Pencil drawing, Blueprint, Whiteboard, Rough texture, Organic lines.  
* **プロンプト構成:** A loose, gestural watercolor sketch of. Visible paper texture. Soft pastel colors. Architectural sketch style with pencil outlines. White background. Not photorealistic, artistic interpretation. 27

---

## **9\. トラブルシューティングと品質管理**

### **9.1 顔や文字の崩れへの対処**

Nano Banana Proは文字生成能力が向上しているが、完璧ではない。

* **対策:** 重要なテキスト（タイトルや数値）は、画像生成時に無理に入れ込もうとせず、PowerPointやGoogleスライドのテキストボックス機能で後から乗せる方が、修正も容易であり、検索性も保たれる。その場合、画像側には「テキストを配置するための空白（Negative Space）」を作るように指示することに集中する。

### **9.2 「SynthID」と著作権・透明性**

企業利用において重要なのが、生成された画像の権利と透明性である。Nano Banana Proで生成された全ての画像には、人間の目には見えない電子透かし「SynthID」が埋め込まれている 8。

* **意味:** これにより、その画像がAIによって生成されたものであることが技術的に証明可能となる。社外向けのプレゼンテーションに使用する場合、この透かしは画像の品質（画質）には影響しないため、そのまま使用して問題ないが、著作権補償（Indemnification）の範囲についてはGoogleの最新の規約（商用利用に関する条項）を確認することが推奨される 9。

### **9.3 14枚以上の画像を参照させたい場合**

現在の仕様では14枚が上限である 2。

* **対策:** 複数のスタイル画像を1枚の画像にコラージュ（結合）してからアップロードすることで、実質的な情報量を増やすことが可能である。ただし、モデルがどの部分を参照すべきか混乱しないよう、プロンプトでの指示を明確にする必要がある。

---

## **10\. 結論**

Nano Banana Pro（Gemini 3 Pro Image）を用いてスライド資料のスタイルを統一するためには、AI任せにするのではなく、ユーザーが「クリエイティブ・ディレクター」として明確な制約を与える必要がある。

**本調査における推奨アクションプラン:**

1. **スタイル・バイブルの作成:** プロジェクトごとに、色彩・照明・構図を定義した3〜5枚の参照画像セットを用意し、生成のたびにこれらを「Strict Style Reference」として入力する。  
2. **不変のスタイルブロックの適用:** プロンプトの末尾に、カメラ設定やレンダリングエンジンを指定する定型文を必ず付加する。  
3. **グリッド生成の活用:** アイコンや挿絵は1枚ずつ生成せず、まとめて生成して切り出すことで完全な統一性を確保する。  
4. **ネイティブ機能の活用:** Googleスライドの「Beautify」機能を使い、スライドマスターに基づいた自動生成を行う。

これらの技術を駆使することで、Nano Banana Proは単なる画像生成ツールから、一貫性のあるブランドアセットを生み出す強力なデザインエンジンへと変貌する。AIの確率的なゆらぎ（Stochasticity）を制御し、意図した通りの決定論的な（Deterministic）結果を得ることこそが、次世代のプレゼンテーション作成における核心的スキルとなるであろう。

---

### **付録：スタイル統一のためのチェックリスト**

| 項目 | チェック内容 | 推奨設定・アクション |
| :---- | :---- | :---- |
| **参照画像** | スタイル・バイブルは設定したか？ | 3〜5枚の定義画像をアップロードし、参照指示を行う。 |
| **プロンプト** | スタイルブロックは固定されているか？ | 照明、カメラ、レンダリング設定の記述を全スライドで統一する。 |
| **ネガティブ** | 禁止事項は明記されているか？ | blur, noise, text, 3D 等の不要要素をリスト化して入力。 |
| **コンテキスト** | 前後のスライドとの繋がりは？ | 「Beautify」機能やインペインティングで文脈を維持。 |
| **アセット** | アイコン等は個別生成していないか？ | グリッド生成（Matrix Generation）でまとめて作成・切り出し。 |
| **テキスト** | 画像内の文字は適切か？ | 重要な文字はスライドソフト側で入力し、画像は背景に徹する。 |

以上

#### **引用文献**

1. Gemini 3's Nano Banana Pro photo editing is amazing – here are 3 ..., 11月 26, 2025にアクセス、 [https://www.techradar.com/ai-platforms-assistants/gemini/gemini-3s-nano-banana-pro-photo-editing-is-amazing-here-are-3-ways-to-make-the-most-of-it](https://www.techradar.com/ai-platforms-assistants/gemini/gemini-3s-nano-banana-pro-photo-editing-is-amazing-here-are-3-ways-to-make-the-most-of-it)  
2. Google announces Nano Banana Pro image tool, says it is based on Gemini 3 and fit for professionals, 11月 26, 2025にアクセス、 [https://www.indiatoday.in/technology/news/story/google-announces-nano-banana-pro-image-tool-says-it-is-based-on-gemini-3-and-fit-for-professionals-2823246-2025-11-20](https://www.indiatoday.in/technology/news/story/google-announces-nano-banana-pro-image-tool-says-it-is-based-on-gemini-3-and-fit-for-professionals-2823246-2025-11-20)  
3. Nano Banana Pro aka gemini-3-pro-image-preview is the best available image generation model \- Simon Willison, 11月 26, 2025にアクセス、 [https://simonwillison.net/2025/Nov/20/nano-banana-pro/](https://simonwillison.net/2025/Nov/20/nano-banana-pro/)  
4. Nano Banana Pro: What it is and How to Use it (vs. Nano Banana) \- AiPPT, 11月 26, 2025にアクセス、 [https://www.aippt.com/blog/nano-banana-pro-full-guide](https://www.aippt.com/blog/nano-banana-pro-full-guide)  
5. G2 Maps Where Nano Banana Fever Is Hottest in the U.S., 11月 26, 2025にアクセス、 [https://learn.g2.com/nano-banana-popularity-by-state?hsLang=en](https://learn.g2.com/nano-banana-popularity-by-state?hsLang=en)  
6. Nano Banana Pro by Google: 5 things you need to know about this ..., 11月 26, 2025にアクセス、 [https://www.indiatoday.in/technology/news/story/nano-banana-pro-by-google-5-things-you-need-to-know-about-this-new-ai-image-tool-2823943-2025-11-21](https://www.indiatoday.in/technology/news/story/nano-banana-pro-by-google-5-things-you-need-to-know-about-this-new-ai-image-tool-2823943-2025-11-21)  
7. Nano Banana Pro is Here: Full Review with a Guide \- Higgsfield, 11月 26, 2025にアクセス、 [https://higgsfield.ai/blog/Nano-Banana-Pro-is-Here-Full-Review-and-Guide](https://higgsfield.ai/blog/Nano-Banana-Pro-is-Here-Full-Review-and-Guide)  
8. Gemini 3 Pro Image (Nano Banana Pro) \- Google DeepMind, 11月 26, 2025にアクセス、 [https://deepmind.google/models/gemini-image/pro/](https://deepmind.google/models/gemini-image/pro/)  
9. Nano Banana Pro available for enterprise Google Cloud Blog, 11月 26, 2025にアクセス、 [https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-pro-available-for-enterprise](https://cloud.google.com/blog/products/ai-machine-learning/nano-banana-pro-available-for-enterprise)  
10. How to use Google Nano Banana Pro to create images: A step-by-step guide, 11月 26, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-tips/how-to-use-google-nano-banana-pro-to-create-images-a-step-by-step-guide/articleshow/125515282.cms](https://timesofindia.indiatimes.com/technology/tech-tips/how-to-use-google-nano-banana-pro-to-create-images-a-step-by-step-guide/articleshow/125515282.cms)  
11. Nano Banana Pro: Google's New Dominant Image Generation Model DataCamp, 11月 26, 2025にアクセス、 [https://www.datacamp.com/de/tutorial/nano-banana-pro](https://www.datacamp.com/de/tutorial/nano-banana-pro)  
12. The Ultimate Nano Banana Pro Prompting Guide: Mastering Gemini ..., 11月 26, 2025にアクセス、 [https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image](https://www.atlabs.ai/blog/the-ultimate-nano-banana-pro-prompting-guide-mastering-gemini-3-pro-image)  
13. 10 Nano Banana Pro Prompts that You Must Try\! \- Analytics Vidhya, 11月 26, 2025にアクセス、 [https://www.analyticsvidhya.com/blog/2025/11/nano-banana-pro-prompts/](https://www.analyticsvidhya.com/blog/2025/11/nano-banana-pro-prompts/)  
14. Jimmy Van Houdt, 11月 26, 2025にアクセス、 [https://www.lorem.be/](https://www.lorem.be/)  
15. Image generation with Gemini (aka Nano Banana ) \- Google AI for Developers, 11月 26, 2025にアクセス、 [https://ai.google.dev/gemini-api/docs/image-generation](https://ai.google.dev/gemini-api/docs/image-generation)  
16. Prompt Engineering Best Practices for Nano Banana Pro (2025) \- Skywork.ai, 11月 26, 2025にアクセス、 [https://skywork.ai/blog/ai-image/prompt-engineering-best-practices-nano-banana-pro-2025/](https://skywork.ai/blog/ai-image/prompt-engineering-best-practices-nano-banana-pro-2025/)  
17. NANO BANANA PRO Full Prompt Bank \- Higgsfield, 11月 26, 2025にアクセス、 [https://higgsfield.ai/blog/Nano-Banana-Pro-Full-Prompt-Bank](https://higgsfield.ai/blog/Nano-Banana-Pro-Full-Prompt-Bank)  
18. The Ultimate Guide of Nano Banana Pro Prompt \- GlobalGPT, 11月 26, 2025にアクセス、 [https://www.glbgpt.com/id/hub/the-ultimate-guide-of-nano-banana-pro-prompt/](https://www.glbgpt.com/id/hub/the-ultimate-guide-of-nano-banana-pro-prompt/)  
19. How to Write Negative Prompts in Nano Banana: A Practical Guide \- Sider.AI, 11月 26, 2025にアクセス、 [https://sider.ai/blog/ai-image/how-to-write-negative-prompts-in-nano-banana-a-practical-guide](https://sider.ai/blog/ai-image/how-to-write-negative-prompts-in-nano-banana-a-practical-guide)  
20. AI Tidbits – Record Your Meetings, Beautify Your Slides – AI Levels Up Again \- Gr8 Services, 11月 26, 2025にアクセス、 [https://www.gr8services.ae/blog/ai-tidbits-record-your-meetings-beautify-your-slides-ai-levels-up-again/](https://www.gr8services.ae/blog/ai-tidbits-record-your-meetings-beautify-your-slides-ai-levels-up-again/)  
21. Nano Banana Pro: Next-Gen AI Arrives on Envato, 11月 26, 2025にアクセス、 [https://elements.envato.com/learn/nano-banana-pro](https://elements.envato.com/learn/nano-banana-pro)  
22. How to restore old photos with Google Nano Banana Pro: A prompt guide and expert tips, 11月 26, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-tips/how-to-restore-old-photos-with-google-nano-banana-pro-a-prompt-guide-and-expert-tips/articleshow/125540228.cms](https://timesofindia.indiatimes.com/technology/tech-tips/how-to-restore-old-photos-with-google-nano-banana-pro-a-prompt-guide-and-expert-tips/articleshow/125540228.cms)  
23. How to create AI portraits from the 1880s to 2025 with Gemini Nano Banana Pro: Step-by-step guide, prompts to try and more, 11月 26, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-tips/how-to-create-ai-portraits-from-the-1880s-to-2025-with-gemini-nano-banana-pro-step-by-step-guide-prompts-to-try-and-more/articleshow/125545365.cms](https://timesofindia.indiatimes.com/technology/tech-tips/how-to-create-ai-portraits-from-the-1880s-to-2025-with-gemini-nano-banana-pro-step-by-step-guide-prompts-to-try-and-more/articleshow/125545365.cms)  
24. Nano Banana Pro Image Editing \- Replicate, 11月 26, 2025にアクセス、 [https://replicate.com/google/nano-banana-pro](https://replicate.com/google/nano-banana-pro)  
25. Google Nano Banana Pro explained: What is it, how it works, and more, 11月 26, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-news/google-nano-banana-pro-explained-what-is-it-how-it-works-and-more/articleshow/125481834.cms](https://timesofindia.indiatimes.com/technology/tech-news/google-nano-banana-pro-explained-what-is-it-how-it-works-and-more/articleshow/125481834.cms)  
26. Awesome Nano Banana Pro Prompts \- GitHub, 11月 26, 2025にアクセス、 [https://github.com/ZeroLu/awesome-nanobanana-pro](https://github.com/ZeroLu/awesome-nanobanana-pro)  
27. Nano Banana's Image Reference Is Crazy – Instantly Match Any Art Style\! \- YouTube, 11月 26, 2025にアクセス、 [https://www.youtube.com/watch?v=PL9RyNb2CAI](https://www.youtube.com/watch?v=PL9RyNb2CAI)
