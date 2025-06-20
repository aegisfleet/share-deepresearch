---
layout: topic
title: "AIビデオ生成技術の最前線：Google Veo 3 徹底解剖"
date: 2025-05-26
prompt: "GoogleのVeo3を使用する際のプロンプトの例を知りたい。特に実写やアニメ調など、映像の質に影響を与えるものをまとめて欲しい。"
category: "ai"
tags: [AIモデル]
audio: "/share-deepresearch/assets/audio/veo3-prompt.mp3"
supplementary_materials:
  - title: "AIビデオ生成技術の最前線：Google Veo 3 徹底解剖"
    url: "/share-deepresearch/topics/veo3-prompt/infographic.html"
---

# **Google Veo 3のポテンシャルを最大限に引き出す：高品質ビデオ生成のためのプロンプトエンジニアリングガイド**

## **1\. Google Veo 3の可能性を活用する：高品質ビデオのためのプロンプトエンジニアリングガイド**

### **Veo 3の可能性への序論**

Google Veo 3は、最先端のテキストからビデオへの変換モデルであり、統合された音声と共に高品質で一貫性のあるビデオクリップを生成する能力を持っています 1。その主な進歩点としては、信憑性のある動き、同期された対話、音楽、サウンドデザイン、リップシンク、そしてカメラの動きの処理が挙げられます 1。Veo 3はVertex AIを通じて利用可能であり 4、プレミアムAIプランの加入者向けにはGoogleの「Flow」インターフェースを通じても提供される可能性があります 1。

出力パラメータに関しては、最大1080pの解像度が言及されていますが 1、Vertex AI API経由のveo-3.0-generate-previewモデルでは、720p解像度、24 FPS、クリップあたり最大8秒の出力となる場合があります 5。この差異は、ユーザーが利用するアクセス方法によって期待すべき品質が変わる可能性があるため、重要な注意点です。Veo 3は、短い視覚的なループではなく、より長く構造化されたシーケンスをサポートします 1。

アクセス方法と機能性の間には関連性が見られます。Veo 3は非常に高度なモデルとして提示されていますが、その全機能（例：1080p出力、Flowインターフェースの高度なツール）はプレミアムサブスクリプションを通じてのみ利用可能である可能性があり 1、これがユーザー体験の階層化を生むかもしれません。具体的には、1ではAI Ultraプラン加入者向けに1080p出力と高度なツールを備えた「Flow」インターフェースが月額$249.99で提供されると言及されている一方で、5（技術ブログ）や4（veo-3.0-generate-preview向けVertex AIドキュメント）ではAPIアクセスに対して720p/8秒の制限が示唆されています。2ではAI ProおよびUltraプランで8秒のビデオが言及されています。これらの出力仕様とアクセス方法（Flow対Vertex AI API）の違いは、「Veo 3」の体験が均一ではない可能性を示唆しています。Googleは、より広範な（ただし制御された）アクセスのためにAPI経由で若干制約のあるバージョンを提供しつつ、最高忠実度で最も統合されたツールセットを最上位の加入者向けに確保しているのかもしれません。これは、計算リソースの管理や、より小規模なユーザーグループでの高度な機能テストを目的としている可能性があります。したがって、ユーザーは自身がアクセスする「Veo 3」（例：Vertex AIプレビュー版対Flowのフルサブスクリプション）が出力能力や付随ツールにおいて異なる場合があることを認識し、自身のアクセスプランの詳細を確認する必要があります。

さらに、1で言及されている「Flow」インターフェースは、SceneBuilderやカメラツールといった機能を備えており、プロンプトがGoogleのエコシステム内でのより大きなクリエイティブワークフローの一部であることを示唆しています。このエコシステムでは、直接操作ツールがプロンプトによる出力を洗練させたり、その上に構築したりする可能性があります。「Flow」はVeo 3を中心に構築されたクリエイティブツールセットであり、ビデオ生成、画像合成、自然言語理解を単一のインターフェースに統合しています 1。これらのツールは、単純なテキストからビデオへの生成を超える能力を示唆しており、シーンの編集、拡張、ショット構成の変更を可能にします。Googleは、プロンプトがアイデアを開始し、GUIベースのツールを通じてさらなる洗練と制御が可能になる、より包括的な映像制作環境を目指していると考えられます。これは、AIによるアセット生成を伴う従来の編集プロセスに似ています。このレポートはプロンプトに焦点を当てていますが、Flowにアクセスできるユーザーは、これらのツールがプロンプト戦略をどのように補完できるかを探求すべきです。例えば、プロンプトで基本的なシーンを生成し、それをSceneBuilderで拡張または変更することで、非常に複雑な複数段階のプロンプトの必要性を減らすことができるかもしれません。

## **2\. 効果的なVeo 3プロンプトの構造：基本原則**

### **不可欠なプロンプト要素の分解（「SACSCAC」フレームワーク）**

GoogleのVertex AIプロンプトガイドで概説されているように、適切に構造化されたプロンプトの基本要素を理解することが重要です 4。これらの要素は、高品質なビデオを生成するための基盤となります。

* **被写体 (Subject):** ビデオの主要な焦点（人物、動物、物体、風景）。外見、感情、服装の詳細描写が品質の鍵となります 7。  
* **アクション (Action):** 被写体が何をしているか。短いクリップでは、明確で簡潔なアクションが不可欠です 6。  
* **コンテキスト/シーン (Context/Scene):** 背景、設定、環境。これにより被写体が現実味を帯び、雰囲気が加わります 6。  
* **スタイル (Style):** 視覚的および芸術的なアプローチ（例：フィルムノワール、カートゥーン、フォトリアリスティック）。これはユーザーのクエリの中心です 6。  
* **（オプションだが品質向上のために推奨）カメラの動き (Camera Motion):** カメラの挙動（例：空撮、ドリーイン、POV）。ダイナミズムと映画的な感覚を加えます 6。  
* **（オプション）構図 (Composition):** ショットのフレーミング（例：ワイドショット、クローズアップ）。視聴者の注意を引きます 6。  
* **（オプション）雰囲気 (Ambiance):** 色、照明、全体的なムード（例：青みがかったトーン、暖かい光、夜）。感情的なインパクトとスタイルにとって重要です 6。

これらの要素を網羅的に記述することで、Veo 3はより具体的で高品質なビデオを生成する可能性が高まります。

### **記述的言語と明確性の力**

プロンプトを作成する際には、平易で明確な言葉と文構造を使用し、過度に複雑または抽象的な言語を避けることが強調されています 7。優れたプロンプトは記述的で明確であるべきです 4。Veoのプロンプトリライターのロジックも支持するように、より詳細なプロンプトは一般的に高品質なビデオをもたらします 4。

VeoのLLMベースのプロンプトリライター 4、特にveo-3.0-generate-previewでは常にオンになっているこの機能 5 は、目に見えない副操縦士のように機能します。これは基本的な記述を強化し、ビデオの説明、カメラの動き、文字起こし、効果音に関する詳細を追加します。これは、ユーザーの入力プロンプトが必ずしもVeo 3が処理する最終的なプロンプトではないことを意味します。AIは積極的にそれを「改善」または「詳細化」しようとします。Googleがこの機能を実装したのは、(a) 詳細度の低いプロンプトを作成する可能性のあるユーザーの出力品質を向上させるため、および (b) Veo 3が最適化されている、より構造化された詳細な形式に単純なユーザーの意図を変換することで、モデルをより効果的にガイドするためであると考えられます。ユーザーは（30語未満でAPIから返された場合）書き換えられたプロンプトから、Veo 3がどのような詳細を有益と見なすかを学ぶことができます。また、非常に短く曖昧なプロンプトでも、この強化機能によりまずまずの結果が得られる可能性がある一方で、正確な制御のためには、リライターをより効果的にガイドするか、既に詳細であれば広範な書き換えをバイパスするため、詳細なユーザープロンプトが依然として優れています。これは「詳細が多いほど品質が向上する」という原則を補強します。

異なるAIビデオ生成ガイド（6、7、8）で構造化されたアプローチ（被写体、アクション、コンテキスト、スタイルなど）を一貫して推奨していることは、これがVeoに特有のものではなく、現在の生成AIにおける基本原則であることを示唆しています。GoogleのVeoガイド 4、Flexclipのガイド 7、およびRedditのStable Diffusionガイド 8 はすべて、同様の構造化されたプロンプト要素で一致しています。異なるモデルや一般的なアドバイス向けであるにもかかわらず、主要な構成要素（何、誰、どこで、どのように、どんなスタイルで）は一貫して強調されています。この一致は、現在のAIモデルが、特定のアーキテクチャに関係なく、シーンを論理的で記述的な構成要素に分解するプロンプトから恩恵を受けることを示しています。この構造化された情報は、これらのモデルがシーンを理解し生成するために使用する内部表現により効果的にマッピングされる可能性が高いです。Veo 3に対するこの構造化されたアプローチを習得することは、他のAIビデオ（および画像）生成ツールにも応用可能なスキルを提供するでしょう。これはプロンプトエンジニアリングにおける基礎的なスキルです。

**表1：Veo 3プロンプトの主要要素とその影響**

| 要素 | 説明 | Veoドキュメントからのキーワード/フレーズ例 | 品質/スタイルへの重要性 |
| :---- | :---- | :---- | :---- |
| 被写体 (Subject) | ビデオの主要な焦点となるオブジェクト、人物、動物、または風景。 | 「高齢の白人船乗り、風化した肌、深いしわ」2、「古代の広大な地図」3、「愛らしいゴールデンレトリバーの子犬」6 | 被写体の詳細な描写は、リアリズムとキャラクターの明確性を高める。 |
| アクション (Action) | 被写体が何をしているか。 | 「スパゲッティの山にフォークを突き刺す」2、「古代の海図を熟読している」3、「雪の中を歩いている」6 | 明確なアクションはビデオの物語性を駆動し、ダイナミズムを生む。 |
| コンテキスト/シーン (Context/Scene) | 被写体が置かれている背景や環境。 | 「穏やかにぼやけた海景、桟橋が見える」2、「雑然とした書斎」3、「雪に覆われた牧草地」9 | シーン設定はビデオに深みと雰囲気を加え、被写体を現実世界に位置づける。 |
| スタイル (Style) | ビデオの視覚的、芸術的アプローチ。 | 「リアリスティック、映画的な品質を伴う」2、「歴史冒険もの」3、「カートゥーンスタイルレンダリング」6、「フィルムノワールスタイル」6 | 特定の美的感覚やジャンル感を確立し、ビデオ全体のトーンを決定する。 |
| カメラの動き (Camera Motion) | カメラがどのように動くか。 | 「ミディアムショット、アイレベル」2、「ローアングルショット」3、「ドリーイン」6、「空撮」6 | 映画的な表現力を高め、視覚的な興味を引きつけ、物語の焦点を導く。 |
| 構図 (Composition) | ショットがどのようにフレーミングされているか。 | 「クローズアップ」2、「ワイドショット」6、「エクストリームクローズアップ」6 | 視聴者の視線を誘導し、シーン内の要素の重要性を強調する。 |
| 雰囲気 (Ambiance) | 色彩と光がシーンにどのように貢献しているか。 | 「ノスタルジックで温かい雰囲気、柔らかく自然な照明」2、「温かいランプの光」3、「青みがかったトーン」6、「夜」6 | ビデオの感情的なトーンを設定し、視覚的な一貫性と没入感を生み出す。 |

## **3\. Veo 3で魅力的な実写映像を作成する**

### **フォトリアリズムと映画的美学の達成**

Veo 3で実写映像の品質を高めるには、被写体、環境、そして望ましいスタイルを詳細に記述することが不可欠です。例えば、「風化した肌、深いしわ、親切そうな顔」といった被写体の特徴 2 や、「色あせたニットの青い船乗り帽」「濃い灰色のひげ」といった素材や服装の詳細 2 を具体的に指定します。環境描写も同様に重要で、「穏やかにぼやけた海景、桟橋が見える」「晴れた日の作業中のドック」といった記述がリアリズムを高めます 2。

スタイルを明示的に指定することも効果的です。「スタイルはリアリスティックで、映画的な品質をわずかに帯びている」2 といった直接的な表現や、「1990年代のVHS映像」10、「歴史冒険ものの設定」3 のような特定の時代やジャンルを示唆するキーワードも有効です。これらの詳細な指示は、Veo 3がユーザーの意図を正確に捉え、高品質な実写映像を生成するための鍵となります。

### **特定のムード、時代、キャラクター詳細のプロンプト**

ムードを伝えるには、「全体的な雰囲気はノスタルジックで温かく、柔らかく自然な照明で達成されている」2 のように、感情的なトーンとそれを実現するための照明条件を記述します。時代や設定を指定するには、「歴史冒険ものの設定」3 や「1970年代」6 のように具体的な年代や場所のコンテキストを与えます。

キャラクターのアクションや対話も、映像のリアリティと物語性を深めます。「彼は今、銀のフォークをしっかりと握り、皿のスパゲッティの山に突き刺す...彼はフォークでパスタの大部分を巻き始める」2 といった具体的な動作や、「地図製作者：『この古い海図によれば...』」3 のような対話を含めることで、キャラクターに生命を吹き込みます。これらの要素を組み合わせることで、特定の感情やシナリオを喚起し、魅力的で高品質な実写映像の出力につながります。

### **実写スタイル用のキーワードと修飾子**

実写映像の特定の美的感覚を要求するために、以下のようなキーワードや修飾子が利用できます。

* **一般的:** 「フォトリアリスティック (photorealistic)」、「リアリスティック (realistic)」、「シネマティック (cinematic)」、「映画的な品質 (cinematic quality)」、「ドキュメンタリースタイル (documentary style)」、「フィルムノワールスタイル (film noir style)」6、「映画のワンシーン (movie still)」6。  
* **時代/メディア特有:** 「1990年代VHS映像 (1990s VHS footage)」10、「ヴィンテージ (vintage)」6。  
* **リアリズムのための照明/雰囲気:** 「柔らかく自然な照明 (soft and natural lighting)」2、「温かいランプの光 (warm lamplight)」3、「自然光 (natural daylight)」8、「ゴールデンアワー (golden hour)」8。  
* **映画的な感覚のためのカメラワーク:** 「ミディアムショット、アイレベル (medium shot, eye-level)」2、「ローアングルショット (low-angle shot)」3、「浅い被写界深度 (shallow depth of field)」6。

これらのキーワードは、Veo 3に対して望ましい実写の美学を伝えるための語彙を提供します。

Veo 3のリアリズムは、単一の「リアルにしろ」というキーワードよりも、多数の具体的で一貫性のある詳細を合成する能力に依存しているようです。最も印象的な実写の例（例：スパゲッティを食べる船乗り 2; 地図製作者 3; 街頭インタビュー 10; 製薬会社のCM 10）はすべて、非常に詳細なプロンプトまたは出力の説明に関連付けられています。これは、より多くの詳細がより良く、より具体的な出力につながるという一般的なプロンプトのアドバイス 4 と一致しています。Veo 3は、一般的な「リアリズム」モードを持つのではなく、ユーザーが指定した多数の具体的な詳細を正確にレンダリングすることでリアリズムに優れていると考えられます。これらの詳細が一貫しており、現実世界の物理法則や外観と一致する場合、出力はリアルであると認識されます。曖昧さや詳細の欠如は、モデルが現実的でない方法でギャップを埋めることにつながる可能性があります。したがって、最大限の実写リアリズムを求めるユーザーにとって、主要な戦略は、主要な被写体から微妙な背景の詳細や照明条件に至るまで、すべてのシーン要素を綿密かつ包括的に記述することです。AIに対して、網羅的な詳細を通じて何を望んでいるかを「単に伝えるのではなく、見せる」のです。

カメラショット、アングル、照明スタイル、さらには感情的な抑揚を伴う対話まで指定できる能力 2 は、ユーザーがテキストを通じてAIの「創造的な」選択を導く「AIシネマトグラファー」またはディレクターの役割を担うことを示しています。プロンプトには、「ミディアムショット、アイレベル」2、「ローアングルショット」3、「温かいランプの光」3、「柔らかく自然な照明」2 といった用語や、「地図製作者：『...』」3 や「感情的な抑揚の注釈付きキャラクター対話」5 のような対話の指示が含まれています。これらはすべて、伝統的に映画セットで人間が行う監督上および撮影上の決定です。Veo 3は、記述的な用語と視覚的なスタイルやカメラワークを関連付けるメタデータやスクリプトを含む可能性のある、膨大な量のビデオデータでトレーニングされていると考えられます。これらの用語を使用することで、ユーザーは本質的にこの学習された相関関係を利用して生成プロセスをガイドしています。高品質な実写ビデオのための効果的なプロンプト作成は、ユーザーが基本的な映画製作と撮影用語を学び、適用することで恩恵を受けるでしょう。ユーザーがプロンプトで「映画の言語を話す」ことができればできるほど、出力の映画的な品質に対する制御が向上します。これはまた、1で指摘されているように、プロンプトエンジニアとクリエイティブディレクターの境界線を曖昧にします。

**表2：Veo 3における実写スタイル用プロンプト修飾子**

| スタイル側面 | キーワード/フレーズ | プロンプト例（一部） | 期待される効果 |
| :---- | :---- | :---- | :---- |
| 全体的なリアリズム | photorealistic, realistic, cinematic quality, detailed textures, natural physics | 「A photorealistic scene of...」, 「...with realistic skin texture and detailed clothing fabric.」 | 現実世界に忠実な視覚的忠実度、信憑性のあるディテール。 |
| 時代設定 | 1970s, historical, vintage, 1990s VHS footage | 「A busy street in the 1970s, vintage cars...」, 「1990s VHS footage of a family gathering.」 | 特定の時代背景やメディアの質感を再現。 |
| ムード/雰囲気 | nostalgic, warm, tense, melancholic, soft and natural lighting, dramatic contrast | 「...creating a nostalgic and warm atmosphere with soft, natural lighting.」, 「A tense standoff under dramatic contrast lighting.」 | 特定の感情的トーンや雰囲気を映像に付与。 |
| キャラクター詳細 | weathered skin, deep wrinkles, expressive eyes, specific clothing items, emotional inflection in dialogue | 「An elderly man with weathered skin and deep wrinkles...」, 「She says with a joyful tone: '...'」 | キャラクターの個性、感情、外見的特徴を明確に表現。 |
| テクスチャ/素材感 | gritty brick wall, weathered wood, metallic sheen, flowing silk | 「A close-up of a gritty brick wall with peeling paint.」, 「Sunlight glinting off a metallic sheen.」 | 物体の表面の質感をリアルに描写し、触覚的な感覚を喚起。 |

## **4\. アニメのビジョンを現実に：Veo 3でのアニメーションスタイルのプロンプト**

### **多様なアニメスタイルの生成戦略**

Veo 3でアニメ調の映像を生成するには、明示的なスタイルキーワードの使用が基本となります。「カートゥーンスタイルレンダリング (cartoon style render)」4 や、「楽しげなカートゥーンスタイルの3Dアニメーションシーン (3D animated scene in a joyful cartoon style)」4 といった一般的な指定が可能です。より具体的なアニメの美的感覚を求める場合、モデルが理解できるようであれば、「スタジオジブリ風 (Studio Ghibli style)」「新海誠風 (Makoto Shinkai style)」といった著名なスタイルを参照することも考えられます（これらのスニペットではVeo 3での明示的な確認はありませんが、11、12、21はこれらがAI画像プロンプトで一般的であり、13はVeo 2が「アニメ」を扱えると示唆しています）。

アニメ特有の特徴を記述することも重要です。「大きな表情豊かな目 (large expressive eyes)」「親しみやすい丸みを帯びたフォルム (friendly, rounded form)」4 といった要素や、伝統的なアニメであれば髪型、衣装のディテール、背景美術のスタイルなども含めることができます。これらのアプローチは、一般的なアニメーションキーワードと典型的なアニメの視覚要素の記述を組み合わせることで、ユーザーの「アニメ調」ビデオの要求に応えます。

### **セルルック、キャラクターデザイン、環境用のキーワード**

アニメ制作において核となるテクニックであるセルルック（セルアニメのような陰影表現）については、Veo 3での明示的な言及はありませんが、「セルルックアニメーション (cel-shaded animation)」「フラットな色と太いアウトライン (flat colors with bold outlines)」といったプロンプトを試す価値があります（一般的なAIアートの知識に基づく）。

キャラクターデザインに関しては、「1girl, solo, two tone hair, black hair, blue hair, long hair, blunt bangs, emerald eyes...」11 のように、詳細な属性を列挙することで特定のキャラクター像を指示できます。

環境描写では、「気まぐれな冬の森 (whimsical winter forest)」「丸みを帯びた雪化粧の木々 (rounded, snow-covered trees)」4 といった具体的な記述が効果的です。他のアニメスタイルでは、「ネオンサインが輝く賑やかな街並み (bustling cityscapes with glowing neon signs)」「桜の咲く穏やかな自然風景 (serene natural landscape with cherry blossoms)」「広大な都市のスカイライン (vast urban skyline)」12 のような表現が考えられます。これらのキーワードは、ユーザーがアニメ特有の視覚要素をプロンプトに組み込むのに役立ちます。

### **アニメ風参照画像を用いたImage-to-Videoの活用**

Veo 3は画像からビデオへの変換機能（Image-to-Video）をサポートしています 1。ユーザーは、アニメ風の静止画（例えば、22でVeo 2向けに提案されているようにImagenを使用して生成または検索したもの）を用意し、Veo 3でそれをアニメーション化することができます。その際、動きや変化をガイドするためのプロンプトを提供します。「入力画像内の被写体とアクションや発話の記述が一致するようにしてください。複数の被写体が存在する場合は、特徴的な記述（例：「赤い帽子の男性」「青いドレスの女性」）を用いて、どのキャラクターがアクションを実行したり話したりしているかを明確に指定してください」4。このテクニックは、優れた参照画像を提供できれば、特定のアニメスタイルを実現するための強力な手段となり、初期の視覚的美学に対するより大きな制御を可能にします。

現在のスニペットに基づくと、Veo 3でのアニメスタイル生成は、特定の監督やスタジオの名前を挙げて完璧な模倣を期待するよりも、ユーザーが一般的なアニメの約束事、キャラクターの特徴、環境要素（例：「大きな表情豊かな目」「カートゥーンスタイルレンダリング」）を記述することに、より依存しているように見えます。Veoに関するスニペットで最も具体的な「アニメーション」の例は、「雪豹のような毛皮を持つかわいい生き物」が「3Dカートゥーンスタイルレンダリング」または「楽しげなカートゥーンスタイル」で描かれるものです 4。13では、プロンプト次第でVeo 2が「アニメ」を生成できると述べられています。11、12、21は、*画像*生成のための詳細なアニメスタイルプロンプトを提供しており、それらのスタイルに典型的な色、照明、キャラクターの特徴、構図の記述に焦点を当てています。Veo特有のスニペットでは、静止画像ほどビデオ生成における直接的なアーティスト/スタジオスタイルの模倣に成功したという証拠は少ないです。Veo 3はビデオの動きと一貫性においてより汎用的に作られている可能性があり、特定のアニメスタイルを実現するには、ユーザーが「宮崎駿風に」のような単一の高度なスタイルキーワードに頼るのではなく、視覚要素（キャラクターデザイン、カラーパレット、背景タイプ、レンダリングスタイルなど）を詳細に記述してスタイルを「構築」する必要があるかもしれません。このモデルは、一部の画像モデルが静止画像に対して行うほど、特定の*ビデオ生成*のためのアニメアーティストに関する詳細なトレーニングを受けていない可能性があります。特定のアニメスタイルを望むユーザーは、そのスタイルを核となる視覚的構成要素（キャラクターの原型、カラーパレット、一般的な設定、レンダリング技術）に分解し、それらをプロンプトで記述する準備をすべきです。適切に選択された参照静止画を用いたImage-to-Videoは、非常に特定のアニメの美的感覚にとってより信頼性の高い道筋となる可能性があります。直接的なスタイル名の指定による実験も依然として価値がありますが、記述的な詳細によってサポートされる必要があるかもしれません。

「楽しげなカートゥーンスタイル」の「走る雪豹」の例 4 は、「楽しげなカートゥーンスタイル」「大きな表情豊かな目」「親しみやすい丸みを帯びたフォルム」といった特徴を持ち、複雑またはニッチなアニメスタイルとは異なる、よりシンプルで普遍的に魅力的なアニメコンテンツを作成したいユーザーにとって良いテンプレートを提供します。雪豹のプロンプト 4 は、望ましい感情的なトーン（「楽しげな」「嬉しそうに跳ね回る」「純粋な喜び」「明るく心温まるトーン」）と視覚的特徴（「かわいい生き物」「大きな表情豊かな目」「親しみやすい丸みを帯びたフォルム」「気まぐれな冬の森」「明るく陽気な色」）を指定する点で非常に詳細です。「カートゥーンスタイル」に対するこのレベルの詳細は、それほど複雑でないアニメーションであっても、具体性が報われることを示唆しています。Veo 3は一般的な「カートゥーン」の外観を実現できますが、そのカートゥーンの*品質*と*具体性*（例：楽しげ対哀愁、ディズニー風対インディーコミック風）は、ユーザーが提供する記述的な形容詞と感情的な手がかりに大きく依存します。ユーザーは単に「カートゥーン」を要求するだけでなく、その感情的な価値、キャラクターの特徴、環境のムードを記述することで、カートゥーンの*種類*を指定すべきです。この例は、あらゆるアニメーションスタイルの要求に対する良い基準となります。

**表3：Veo 3におけるアニメ＆カートゥーンスタイル用プロンプト修飾子**

| スタイル側面 | キーワード/フレーズ | プロンプト例（一部） | 期待される効果 |
| :---- | :---- | :---- | :---- |
| 一般的なアニメ | anime style, Japanese animation, cel-shaded, vibrant colors, dynamic action | 「A dynamic anime style fight scene, cel-shaded characters...」 | 日本のアニメーション特有の視覚的特徴を持つ映像。 |
| 特定のサブジャンル (例：ジブリ風) | Studio Ghibli inspired, hand-drawn painterly illustration, dreamlike atmosphere, lush environments, expressive faces, warm golden hues | 「A Studio Ghibli inspired scene of a magical forest, hand-drawn painterly look, warm golden hues...」 | 特定のアニメスタジオや作品の美的感覚や雰囲気を模倣。 |
| キャラクター特徴 | large expressive eyes, two-tone hair, specific hairstyles (e.g., blunt bangs), unique clothing, chibi style | 「A character with large expressive eyes and vibrant pink hair, wearing a futuristic outfit.」 | アニメキャラクターに典型的な、または特定のスタイルに合わせた外見的特徴。 |
| 環境/背景 | whimsical forest, bustling cityscape with neon signs, serene natural landscape, hyper-detailed backgrounds, painterly feel | 「A whimsical forest with glowing mushrooms and ancient trees, painterly feel.」, 「Bustling cyberpunk cityscape at night, neon signs reflected on wet streets.」 | アニメの世界観を構築する特徴的な背景や環境。 |
| レンダリング/質感 | cel-shaded, flat colors with bold outlines, soft shading, painterly texture, 2D animation, 3D cartoon render | 「2D animation with flat colors and bold outlines.」, 「A cute creature in a 3D cartoon render style.」 | アニメーションの描画スタイルや質感（セルルック、手描き風、3Dカートゥーン調など）。 |

## **5\. Veo 3による高度なシネマトグラフィ：カメラ、照明、構図、テクスチャの習熟**

### **カメラ制御：仮想レンズの演出**

Veo 3で映画的な品質を実現するためには、カメラのショット、動き、レンズ効果を正確に指示することが重要です。

* **特定のショット:** 「クローズアップ (close-up)」、「エクストリームクローズアップ (extreme close-up)」、「ワイドショット (wide shot)」、「ミディアムショット (medium shot)」、「アイレベル (eye-level)」、「POVショット (POV shot)」、「ローアングルショット (low-angle shot)」、「トップダウンショット (top-down shot)」といった基本的なショット指定が可能です 6。  
  * 例：「目に映る都市の反射を捉えたエクストリームクローズアップ。(Extreme close-up of an eye with city reflected in it.)」6  
* **カメラの動き:** 「ドリーイン/トゥ (dolly in/to)」、「トラッキングショット (tracking shot)」、「空撮 (aerial view)」、「ズームイン (zoomed in)」、「スムーズな動き (smooth motion)」、「カメラが漂う (camera drifts)」、「横スクロールドリー (side-scrolling dolly)」といった動きを指定することで、映像にダイナミズムを与えられます 6。  
  * 例：「雨の中、夜のカナダを走るヴィンテージカーからのPOVショット、シネマティック。(A POV shot from a vintage car driving in the rain, Canada at night, cinematic.)」6  
* **レンズ効果と映画的言語:**  
  * 「浅い被写界深度 (shallow depth of field)」は、被写体に焦点を合わせ背景をぼかす効果で、映画的な印象を与えます 6。船乗りの例では、この効果が示唆されています 2。  
  * あるユーザーは、映画的な外観を実現した際に「アナモフィックレンズ (anamorphic lenses)」に言及しており、Veo 3がこれを解釈する可能性を示唆しています 15。  
  * GoogleのVeo 2ガイドでは、「タイムラプス (timelapse)」「空撮 (aerial shot)」「横スクロールドリー (side-scrolling dolly)」といった用語がAIの解釈に実際に影響を与えると述べられています 14。この原則はVeo 3にも適用される可能性が高いです。

これらのカメラ指示を正確に行うことで、単純なシーンをよりダイナミックでプロフェッショナルな見た目に高めることができます。

### **照明テクニック：プロンプトで光を描く**

照明は視覚的な物語性とムード設定の基本であり、Veo 3ではプロンプトを通じて照明条件を細かく制御できます。

* **自然光と環境光:** 「自然光 (natural light)」、「太陽光 (sunlight)」、「木漏れ日 (dappled sunlight)」、「暖かい太陽光 (warm sunlight)」、「柔らかく自然な照明 (soft and natural lighting)」、「午後の半ばの光 (mid afternoon light)」といったキーワードで、現実的な光の状態を再現します 2。  
* **人工光と様式化された光:** 「温かいランプの光 (warm lamplight)」、「不気味な緑のネオンサインの輝き (eerie glow of a green neon sign)」、「ネオンの反射 (neon reflections)」、「被写体へのスポットライト (spotlight on the subject)」、「スタジオ照明 (studio lighting)」、「ボリュームライティング (volumetric lighting)」、「シネマティックライティング (cinematic lighting)」といった指定で、特定の雰囲気やスタイルを強調できます 1。  
  * 例（画像向けだが概念は適用可能）：「夜の街、見事なアストンマーティンスポーツカーのクローズアップデジタルアート...未来的なシンセウェイヴ都市、サイバーパンク、レトロな夕焼け...ボリュームライティング、最高品質、鮮やかな色彩、シャープな焦点、グローバルイルミネーション、シネマティック。(Night city, close up digital art of a stunning Aston Martin sports car... futuristic synthwave city, cyberpunk, retro sunset... volumetric lighting, highest quality, vibrant colors, sharp focus, global illumination, cinematic.)」1  
* **時間帯:** 「日の出/日の入り (sunrise/sunset)」、「ゴールデンアワー (golden hour)」、「夜 (night)」、「夕暮れ (dusk)」を指定することで、特定の時間帯の光を再現します 6。  
* **カラーパレットとムード:** 「クールな青系のトーン (cool blue tones)」、「温かい金色の色調 (warm golden hues)」、「落ち着いたオレンジ系の暖色 (muted orange warm tones)」、「パステルブルーとピンクのトーン (pastel blue and pink tones)」、「薄暗い環境光 (dim ambient lighting)」、「冷たい落ち着いたトーン (cold muted tones)」、「豊かな色彩 (rich colors)」といった色の指定で、映像全体の感情的なトーンを調整します 6。  
  * 例：「雨の中バスに乗る悲しい女性のシネマティッククローズアップショット、クールな青系のトーン、悲しいムード。(Cinematic close-up shot of a sad woman riding a bus in the rain, cool blue tones, sad mood.)」6

これらのキーワードを駆使することで、ユーザーは映像の視覚的な雰囲気を巧みに作り上げることができます。

### **構図要素：視聴者の視線を導く**

構図は、カメラの動きや照明ほどスニペットで明示的に詳述されていませんが、制御の暗黙的な要素です。

* **フレーミング:** 「ワイドショット (wide shot)」、「クローズアップ (close-up)」、「エクストリームクローズアップ (extreme close-up)」、「中距離 (medium distance)」といった基本的なフレーミング指示が可能です 6。  
* **被写体の配置:** 「その男性の孤立と絶望を強調するようにシーンはフレーミングされている (The scene is framed to emphasize the isolation and desperation of the man)」6 といった指示や、「深みを加えるために複雑な前景要素を含める (Include intricate foreground elements to add depth)」12 といった指示で、被写体の配置や画面内のバランスを調整できます。

これらの構図に関する指示は、視聴者の注意を特定の要素に引きつけ、物語の意図を効果的に伝えるのに役立ちます。

### **テクスチャと素材の定義：触覚的なリアリズムの追加**

詳細なテクスチャ記述は、フォトリアリズムや特定の様式的効果（VHSなど）にとって不可欠です。

* **一般的な記述子:** 「風化した緑のトレンチコート (weathered green trench coat)」、「ざらざらしたレンガの壁 (gritty brick wall)」、「長い羊毛の毛皮 (long wooly fur)」、「雪に覆われた木々 (snow covered trees)」、「流れるような有機的な形状の白いコンクリート... (white concrete... flowing organic shapes)」、「青々とした緑 (lush greenery)」といった記述で、素材の質感を伝えます 2。  
* **特定の効果:** 「フィルムグレイン (film grain)」1、「VHSテクスチャ (VHS texture)」10。  
* **肌:** 「リアルな肌のテクスチャ (realistic skin texture)」1、「風化した肌、深いしわ (weathered skin, deep wrinkles)」2。

これらの詳細なテクスチャの記述は、映像に触覚的なリアリズムを与え、視覚的な豊かさを増します。

確立された映画製作の専門用語（ショットタイプ、カメラの動き、照明スタイル）を使用したプロンプトが繰り返し成功していることは、Veo 3（そしておそらくその前のVeo 2も、14、14によれば）がこれらの概念を認識し、実装するように訓練されていることを示しています。これは単なるキーワードマッチング以上のものであり、これらの用語の機能的および美的含意を理解することに関わっています。Vertex AIプロンプトガイド 4 や様々な例 2 は、「ミディアムショット」「ドリーイン」「ローアングル」「温かいランプの光」「浅い被写界深度」といった用語で満ちています。1414 はVeo 2について、「『タイムラプス』『空撮』『横スクロールドリー』のような用語を使用すると、AIが動きを解釈しレンダリングする方法に純粋に影響を与える」と明示的に述べています。これは、GoogleがVeoの理解をプロの映画製作の実践に合わせるための意図的な努力を示唆しています。Veoモデルは、映画、テレビ番組、ストック映像の膨大なデータセットでトレーニングされており、しばしばこの専門用語を含むスクリプト、絵コンテ、またはメタデータが付随していると考えられます。AIはこれらの用語を特定の視覚的出力と関連付けることを学習します。基本的な撮影技術と映画製作の言語を学ぶ時間を投資するユーザーは、効果的なVeo 3プロンプトを作成する上で大きな利点を得るでしょう。業界標準の用語を使用してビジョンをより正確に表現できればできるほど、最終的な出力に対する制御が向上し、より高品質で意図的な結果が得られます。これは、単純な記述を超えて、AIの積極的な「演出」へと移行します。

Redditのあるユーザー 15 は、Veo 3の一つの出力が「アナモフィックレンズで作られたように、より映画的に見える」と指摘しました。これは、「アナモフィック」がGoogleから提案されたキーワードのリストにはなかったものの、ユーザーが認識した視覚的品質であったため重要です。ユーザーは、Veo 3の生成物が「アナモフィックレンズ」の外観の特徴を持っていると明示的に言及しました 15。これは、必ずしも彼らが使用した直接的なプロンプトキーワードではなく、出力の観察結果でした（ただし、使用した可能性もあります）。アナモフィックレンズは、楕円形のボケ、水平方向のレンズフレア、特定の深度特性といった独特の視覚的特徴を生み出します。Veo 3は、トレーニングデータにアナモフィックレンズで撮影された映像の十分な例が含まれており、プロンプトにアナモフィック映像と一般的に共起する他の映画的キーワードや記述（特定のジャンル、照明スタイル、構図など）が十分に記述されていれば、このような複雑な視覚的特性を再現できる可能性があります。「アナモフィックレンズ」が認識されるキーワードである可能性も考えられます。これは、特定の機能が公式に文書化されていなくても、ユーザーが様々な記述要素を組み合わせることで、新たな機能を発見したり、微妙なスタイルを実現したりする可能性を示しています。「アナモフィックレンズ」「Arri Alexaで撮影」「35mmフィルムルック」「フィルムグレイン」「ハイパーリアリズム」「ボケの種類」といった用語は、映画業界や他のAI画像ジェネレーターで一般的であり、テストすることを推奨すべきです。23と1はVeo 3についてこれらを明示的にリストしていませんが、15でのユーザーの経験は強力なヒントです。18は画像について「フィルムのような粒子」と「ざらついたポラロイドの美的感覚」に言及しており、これはVeoでテストできる可能性があります。

**表4：Veo 3のための高度な映画的制御キーワード**

| 映画的要素 | キーワード/フレーズ | プロンプト例（一部） | 期待される効果 |
| :---- | :---- | :---- | :---- |
| カメラショット | close-up, extreme close-up, wide shot, medium shot, eye-level, POV shot, low-angle shot, top-down shot | 「Extreme close-up on the character's determined eyes.」 | 特定の視点や焦点距離を模倣し、物語の強調点を変える。 |
| カメラの動き | dolly in, tracking shot, aerial view, zoom, smooth pan, crane shot, handheld style | 「Slow dolly in towards the mysterious object.」, 「Handheld style shot following the character running.」 | 映像にダイナミズム、緊張感、または安定感を与える。 |
| レンズ特性 | shallow depth of field, anamorphic lens, bokeh, lens flare, fisheye lens, macro | 「Shallow depth of field focusing on the foreground subject.」, 「Cinematic shot with anamorphic lens characteristics.」 | 特定のレンズ効果（ボケ、フレア、歪みなど）を再現し、映像の美的感覚を高める。 |
| 照明スタイル | natural daylight, golden hour, studio lighting, dramatic contrast, Rembrandt lighting, neon lighting, volumetric lighting, film noir lighting | 「Golden hour lighting casting long shadows.」, 「Film noir lighting with stark contrasts and shadows.」 | シーンのムード、時間帯、ジャンル感を演出し、被写体の立体感を強調する。 |
| 光の質 | soft light, hard light, diffused light, dappled sunlight, rim lighting | 「Soft, diffused light creating a gentle atmosphere.」, 「Rim lighting outlining the character's silhouette.」 | 光の硬さや拡散具合を調整し、被写体の見え方や質感を変化させる。 |
| カラーパレット | warm tones, cool tones, monochromatic, vibrant colors, pastel colors, desaturated | 「A scene with warm, nostalgic color tones.」, 「Monochromatic black and white for a classic feel.」 | 映像全体の色彩設計を制御し、感情的なトーンや美的スタイルを確立する。 |
| テクスチャ/素材感 | film grain, VHS texture, metallic sheen, rough wood, smooth skin, weathered fabric | 「Subtle film grain for a vintage look.」, 「Close-up showing the rough texture of weathered wood.」 | 映像に特定の質感（フィルム粒子、素材感など）を加え、リアリズムや時代感を高める。 |
| フィルムストック/エミュレーション | 35mm film look, 16mm film look, shot on Arri Alexa (emulation), Technicolor style | 「A scene with the distinct look of 35mm film.」 | 特定のフィルムストックやカメラの視覚的特性を模倣し、特定の映画的美学を追求する。 |

## **6\. サウンドスケープ：Veo 3におけるオーディオ、対話、音楽のプロンプト**

### **Veo 3のネイティブオーディオ生成能力**

Veo 3は、同期された対話、音楽、サウンドデザインを含む完全なビデオクリップを生成でき、リップシンクも可能です 1。これは、23の執筆時点でSoraのようなモデルに対する大きな利点です。veo-3.0-generate-previewモデルはオーディオをサポートしています 4。このネイティブオーディオ生成能力は、Veo 3でオーディオプロンプトが重要かつ可能である理由の基盤を設定します。

### **対話指定のテクニック**

Veo 3では、プロンプトを通じてキャラクターの対話を生成し、その感情的なニュアンスまで制御することが可能です。

* 対話は引用符で囲み、しばしばキャラクターに帰属させます：「地図製作者：『この古い海図によれば...』」2。  
* 「彼/彼女は言う (he/she says)」の後に引用符で囲まれた対話を続ける形式も有効です 15。  
* 複数の被写体がいるImage-to-Videoの場合、記述的な詳細（例：「赤い帽子の男性が言う...」）を使用して誰が話しているかを明確に指定します 4。  
* 感情的な抑揚をプロンプトで要求できます：「感情的な抑揚の注釈付きキャラクター対話 (Character dialogue with emotional inflection notes)」5。  
  * 例：「探偵が神経質そうなおもちゃのアヒルを尋問する。『君はシャボン玉風呂の夜、どこにいたんだ？！』と彼はアヒル声で言う。オーディオ：探偵の厳しいアヒル声、おもちゃのアヒルからの神経質なキーキー音。(A detective interrogates a nervous-looking rubber duck. ‘Where were you on the night of the bubble bath?\!’ he quacks. Audio: Detective’s stern quack, nervous squeaks from rubber duck.)」2

これらのテクニックにより、物語性のあるビデオに不可欠な明確な対話と、Veo 3の強力な特徴である感情的なトーンの表現が可能になります。

### **環境音と特定の効果音の追加**

環境音と効果音は、リアリズムと没入感を大幅に向上させます。Veo 3では、これらをプロンプトで具体的に指示できます。

* 望ましい音を明確にリストアップします：「オーディオ：羽ばたき、鳥のさえずり、大きく心地よい風のざわめき... (Audio: wings flapping, birdsong, loud and pleasant wind rustling...)」2。  
* 環境効果音と環境音を指定します 5。  
  * 例：「葉の擦れる音、コオロギの鳴き声 (rustling leaves, crickets)」、「穏やかな海の音 (peaceful sounds of the ocean)」、「静かな家の音、クローゼットのドアのきしみ、段ボールの擦れる音 (soft house sounds, the creak of the closet door, cardboard rustling)」2。  
* Vertex AIガイドでは、オーディオを別の文で指定することを推奨しています 4。

これらの指示により、ビデオの世界観を豊かにする音響効果を付加できます。

### **音楽スタイルとムードの誘導**

音楽はビデオの感情的なトーンを設定する上で極めて重要です。Veo 3では、音楽のスタイルやムードもプロンプトで指示できます。

* 音楽スタイルやムードを記述します：「木管楽器が全体を通して使われ、陽気で楽観的なリズムを持ち、無邪気な好奇心に満ちた軽いオーケストラスコア (A light orchestral score with woodwinds throughout with a cheerful, optimistic rhythm, full of innocent curiosity)」2。  
* 音楽が必要かどうかを指定します：「背景に静かな音楽を追加する (Add soft music in the background)」4。  
* 注意：Lyria 2は、楽器、BPMなどを制御できる、テキストプロンプトからの高品質なオーディオコンテンツのためのGoogleのモデルです 3。Veo 3はオーディオを生成しますが、複雑な音楽生成は、統合が可能であるか、ユーザーがサウンドトラックを別途作成している場合、Lyria 2の方が適している可能性があります。このレポートはVeo 3のネイティブ機能に焦点を当てています。

これらの指示により、ビデオの感情的な背景を形成する音楽的要素を制御できます。

Veo 3がプロンプトから直接同期された対話、SFX、音楽を生成する能力 1 は、AIを包括的なストーリーテリングツールへと進化させる重要な一歩です。これにより、基本的なクリップのオーディオを別途調達・編集する必要性が減り、クリエイティブプロセスが合理化されます。複数の情報源 1 が、Veo 3のネイティブオーディオ機能（対話、SFX、音楽を含む）を強調しており、しばしばそれらをプロンプトで指定する方法の具体例を挙げています。これは、サイレントクリップを生成し、オーディオのために大幅なポストプロダクションを必要とする以前の、あるいは一部の現代的なビデオ生成モデルとは対照的です。Googleは、おそらくLyriaに関連するオーディオ生成技術のコンポーネントをVeo 3のパイプラインに直接統合し、モデルが視覚的なシーンとテキストの手がかりに文脈的に関連するオーディオを理解し生成できるようにしたと考えられます。これにより、より完全で魅力的な短いビデオを作成するための障壁が低くなります。ユーザーは対話とサウンドを含むシーンをプロトタイプ化できるため、物語の意図を伝えやすくなります。実写の場合、これはより現実的なインタラクションを意味し、アニメの場合、キャラクターの声やテーマ音楽が初期生成の一部となり得ます。

「感情的な抑揚の注釈付きキャラクター対話」を要求できる能力 5 は、単純なテキスト読み上げを超える高度なオーディオ制御レベルを示唆しています。5（技術ブログ）は、「感情的な抑揚の注釈付きキャラクター対話」のプロンプトについて具体的に言及しています。標準的なテキスト読み上げはしばしば単調に聞こえますが、感情的な抑揚は信憑性のある対話とキャラクターの演技にとって鍵となります。Veo 3の対話用オーディオ生成は、俳優が脚本を解釈する方法と同様に、テキストから感情的な手がかりを理解し再現するように訓練された高度な音声合成モデルを組み込んでいる可能性が高いです。ユーザーは、プロンプト内の対話中または対話と共に、括弧内の感情的な手がかりや記述的な副詞（例：「彼は恐る恐る囁いた」「彼女は怒って叫んだ」「地図製作者（興奮して）：『...』」）を追加することを試みるべきです。これにより、生成されるキャラクターの表現力と品質が大幅に向上する可能性があります。

## **7\. ビジョンの洗練：ネガティブプロンプト、イテレーション、パラメータ**

### **ネガティブプロンプトの効果的な使用**

ネガティブプロンプトは、モデルに生成を控えてほしい内容を記述するテキスト文字列です 4。Vertex AIのガイダンスによれば、「no」や「don't」のような指示的な言葉遣いを避け、代わりに*見たくないもの*を記述します（例：木の場合、ネガティブプロンプト：「都市の背景、人工建造物、暗い、嵐のような、または脅迫的な雰囲気」）4。ネガティブプロンプトは、不要な要素を排除し、出力を微調整するための強力なツールであり、ビデオの品質向上に貢献します。

### **より良い結果を得るためのプロンプトのイテレーションに関するヒント**

AIツールを習得する鍵はイテレーションです。以下のヒントは、体系的なアプローチを提供します。

* 中核となるアイデアから始め、キーワードや修飾子を追加して洗練させます 4。  
* 一度に一つの変数（動き、カメラスタイル、被写体の行動など）を変更して段階的に調整し、何が最も効果的かを体系的に探ります 14。  
* プロンプトが30語未満の場合、APIはVeo 3が使用した書き換えられた（強化された）プロンプトを返すことがあります。これを研究して、AIがどのような詳細を追加するかを学びます 4。  
* よくある間違いを避けます：短いクリップにアクションが多すぎる、一つのプロンプト内にシーンのトランジションがある、カメラの動きが複雑すぎる、独立したアクションを持つ複数の被写体、スタイルが一致しないなど 8。

これらのヒントに従うことで、プロンプトを効果的に改善し、望ましいビデオ品質に近づけることができます。

### **Veo 3パラメータの理解 (Vertex AI)**

Vertex AIコンソールまたはAPIで利用可能なこれらのパラメータは、テキストプロンプト自体を超えた別の制御層を提供します。

* **アスペクト比 (Aspect Ratio):** 16:9（横長）または9:16（縦長）。注意：9:16はveo-3.0-generate-previewではサポートされていません 4。  
* **ビデオ長 (Duration):** veo-3.0-generate-previewでは5秒から8秒 4。2でも8秒のビデオが言及されています。  
* **結果の数 (Response Count):** 1から4 4。  
* **シード (Seed):** 生成されるビデオを決定論的にするための数値（0 \- 4294967295）。同じプロンプトと他のパラメータでシードを指定すると、同じビデオが生成されるはずです 4。これは再現性と一貫したイテレーションにとって不可欠です。  
* **人物生成 (Safety Setting):** 人物/顔に対してallow\_adult（デフォルト）またはdisallow 4。

これらのパラメータを適切に設定することで、生成されるビデオの基本的な特性を制御できます。

seedパラメータ 4 は、単に同じビデオを2回取得するためだけのものではありません。プロンプトのバリエーションをA/Bテストするための強力なツールです。シードを一定に保ち、プロンプトの一要素のみを変更することで、ユーザーはその特定の変更の影響をより正確に評価できます。4と4は、他のパラメータを変更せずにリクエストでseed番号を指定すると、モデルが同じビデオを生成するようにガイドすると述べています。この決定論の特性は、あらゆる実験設定において非常に価値があります。特定のスタイルや品質を達成するためにプロンプトを反復処理する際、ランダム性は、プロンプトの変更または単なる確率的変動が異なる出力を引き起こしたかどうかを曖昧にする可能性があります。固定シードはこのランダム性を排除します。ユーザーは、プロンプトを微調整する際に固定シードを使用することが推奨されます。例えば、「温かいランプの光」対「クールなネオンの輝き」の影響をテストするには、同じシードと基本プロンプトを使用し、照明記述子のみを変更します。これにより、プロンプトエンジニアリングに対するより科学的なアプローチが可能になります。

ネガティブプロンプトは主に不要な要素を除外するためのものですが 4、スタイルを微妙に洗練させるためにも使用できます。例えば、「穏やかな自然の風景」を目指す場合、「混沌としていない、工業的でない、人工的な色でない」といったネガティブプロンプトは、ポジティブプロンプトで明示的に要求されていなくても、望ましいムードを壊す要素からAIを遠ざけるのに役立ちます。Vertex AIガイド 4 は、オークの木のネガティブプロンプトの例を挙げています：「- 都市の背景、人工建造物、暗い、嵐のような、または脅迫的な雰囲気」。これらのネガティブな用語は、特定のオブジェクトを除外するだけでなく、望ましくない雰囲気や文体的品質も除外します。概念を否定することで、ユーザーはAIの可能性の空間を狭め、それが*何でないか*を明確に定義することで、望ましい美学へと押し進めることができます。ユーザーはネガティブプロンプトを「車なし」だけでなく、「ぼやけていない」「彩度が高すぎない」、またはヴィンテージな外観を目指す場合は「現代的でない」といった文体的な洗練のためにも考えるべきです。これにより、品質とスタイルの制御に別の次元が加わります。

## **8\. 具体的なプロンプト例：実写とアニメのショーケース**

このセクションでは、これまでの学習内容を具体的な詳細な例に統合します。各例には以下が含まれます。

* **目標:** （例：「雨の中で悲しみを表現するキャラクターのフォトリアリスティックなクローズアップ」、「未来都市でのダイナミックなアニメアクションシーケンス」）。  
* **完全なプロンプト:** SACSCACの要素、カメラ、照明、オーディオ、スタイル固有のキーワードを組み込んだ、綿密に作成されたプロンプト。  
* **内訳と根拠:** 特定のキーワードと構造が選択された理由の説明。以前に議論された原則と関連するスニペットを参照します。  
* **期待される結果:** 予想されるビデオの説明。

### **実写の例（詳細、シネマティック）**

* **目標:** フィルムノワールにインスパイアされた、薄暗く雨に濡れたオフィスにいる刑事の緊迫したシネマティックなクローズアップ。  
* **プロンプト案:** Film noir style. Extreme close-up on a weary detective's face, mid-40s, stubble, deep-set eyes reflecting city lights through a rain-streaked window. He's in a dimly lit, smoky office. Low-key lighting, strong shadows, chiaroscuro effect. Camera slowly pushes in. Sound of gentle rain tapping on glass, distant city sirens. Detective (voice-over, gravelly): 'The city was a maze, and she was the missing piece... or the trap.' Ambiance: melancholic, tense. Negative prompt: bright colors, modern furniture, cheerful.  
* **根拠:** スタイル（「フィルムノワール」）、被写体の詳細、カメラ（「エクストリームクローズアップ」、「ゆっくりとプッシュイン」）、照明（「ローキー」、「キアロスクーロ」）、オーディオ（「雨音」、「サイレン」、トーン付きナレーション）、および洗練のためのネガティブプロンプトを組み合わせています。2、6、3、8、4、6、6の原則に基づいています。  
* **期待される結果:** 雨筋のついた窓ガラス越しに街の灯りが反射する、疲れた中年の刑事の顔の極端なクローズアップ。オフィスは薄暗く、煙が漂い、強い影と明暗のコントラストが特徴的。カメラはゆっくりと顔に寄っていく。ガラスを叩く優しい雨音と遠くのサイレンの音が聞こえ、しゃがれた声のナレーションが流れる。全体的にメランコリックで緊迫した雰囲気の映像。

### **アニメの例（ダイナミック、様式化）**

* **目標:** 夕焼け空の下、牧歌的な風景の上を飛ぶ若い魔女の、活気に満ちたジブリ風のシーン。  
* **プロンプト案:** Anime style, reminiscent of Studio Ghibli. A young witch with messy brown hair and a red bow, wearing a simple dark blue dress, joyfully flies on a wooden broomstick. Below her, a vast, rolling green landscape with patchwork fields and a distant sparkling river. Sky is a brilliant sunset orange and purple. Warm golden hour light. Camera is a dynamic tracking shot, slightly low angle, following her flight. Wind rustles her hair and clothes. Audio: uplifting orchestral score with prominent flute, sound of wind, distant birdsong. Style: hand-drawn painterly illustration, soft yet vibrant colors, dreamlike atmosphere. Negative prompt: 3D render, harsh lines, gloomy.  
* **根拠:** アニメスタイルを参考に指定し、キャラクターと環境、カメラの動き、照明、オーディオ、レンダリングスタイルを詳述しています。12の画像プロンプトのアイデアと11の一般的なアニメプロンプト構造を応用し、Veoのビデオ機能と組み合わせています。  
* **期待される結果:** 赤いリボンをつけた乱れた茶髪の若い魔女が、シンプルな紺色のドレスを着て、木のほうきにまたがり楽しそうに飛んでいる。眼下には広大な緑の丘陵地帯が広がり、パッチワークのような畑や遠くにきらめく川が見える。空は鮮やかなオレンジと紫の夕焼け。温かいゴールデンアワーの光。カメラはダイナミックなトラッキングショットで、ややローアングルから彼女の飛行を追う。風が彼女の髪と服を揺らす。高揚感のあるオーケストラの音楽（フルートが際立つ）、風の音、遠くの鳥のさえずりが聞こえる。手描きの絵画のようなイラスト調で、柔らかくも鮮やかな色彩、夢のような雰囲気の映像。

（完全なレポートでは、実写とアニメの両方について、さまざまなシナリオをカバーするさらに多くの例が作成されます。）

## **9\. 結論：Veo 3で創造的可能性を解き放つ**

Google Veo 3は、テキストプロンプトから高品質なビデオを生成するための強力なツールです。本レポートで概説した主要戦略、すなわち構造化されたプロンプト作成、詳細な記述、映画的言語の活用、具体的なオーディオ指示、そして反復的な洗練プロセスは、ユーザーがこのツールのポテンシャルを最大限に引き出すための道筋を示しています。

Veo 3の能力は目覚ましいものがありますが、最終的な出力の品質とインパクトは、ユーザーの創造性と、そのビジョンをプロンプトで明確に表現する能力に大きく左右されます。実写風のリアリズムを追求するにしても、特定のアニメスタイルを再現するにしても、被写体、アクション、コンテキスト、スタイル、カメラワーク、照明、雰囲気を詳細に記述することが不可欠です。特に、Veo 3が映画製作の専門用語を理解し、それに応じて映像を生成する能力は、ユーザーが「AIシネマトグラファー」としての役割を果たすことを可能にします。

さらに、Veo 3のネイティブなオーディオ生成機能は、対話、効果音、音楽を映像と同期させることで、物語性を飛躍的に高めます。感情的な抑揚を含む対話の指定や、環境音、音楽のムードをプロンプトに組み込むことで、より完全で没入感のあるビデオ体験を創出できます。

ネガティブプロンプトによる不要な要素の排除、シード値を利用した制御された実験、そしてAPIパラメータの調整は、生成プロセスをさらに洗練させるための重要な手段です。AIビデオ生成技術は急速に進化しており、継続的な実験と学習が、この分野での習熟度を高める鍵となるでしょう。

最後に、1で触れられているように、これらの強力なツールは映画製作のあり方を変えつつあり、創造性と効率性のバランス、そしてAI時代のアーティストの役割について、重要な問いを投げかけています。Veo 3を使いこなすことは、技術的なスキルだけでなく、変化するメディア環境における創造的な適応力も養うことになるでしょう。

#### **引用文献**

1. Google DeepMind Veo 3 and Flow Unveiled for AI "Filmmaking" CineD, 5月 26, 2025にアクセス、 [https://www.cined.com/google-deepmind-unveils-veo-3-and-flow-for-ai-filmmaking/](https://www.cined.com/google-deepmind-unveils-veo-3-and-flow-for-ai-filmmaking/)  
2. Gemini AI video generator powered by Veo 3 \- Google Gemini, 5月 26, 2025にアクセス、 [https://gemini.google/overview/video-generation/](https://gemini.google/overview/video-generation/)  
3. Announcing Veo 3, Imagen 4, and Lyria 2 on Vertex AI Google ..., 5月 26, 2025にアクセス、 [https://cloud.google.com/blog/products/ai-machine-learning/announcing-veo-3-imagen-4-and-lyria-2-on-vertex-ai](https://cloud.google.com/blog/products/ai-machine-learning/announcing-veo-3-imagen-4-and-lyria-2-on-vertex-ai)  
4. Veo AI Video Generator Generative AI on Vertex AI \- Google Cloud, 5月 26, 2025にアクセス、 [https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos](https://cloud.google.com/vertex-ai/generative-ai/docs/video/generate-videos)  
5. Unlock Google Veo 3 Today: 3 Insider Methods You Can't Afford to ..., 5月 26, 2025にアクセス、 [https://dev.to/fallon\_jimmy/unlock-google-veo-3-today-3-insider-methods-you-cant-afford-to-miss-3n77](https://dev.to/fallon_jimmy/unlock-google-veo-3-today-3-insider-methods-you-cant-afford-to-miss-3n77)  
6. Vertex AI video generation prompt guide Generative AI on Vertex AI ..., 5月 26, 2025にアクセス、 [https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide](https://cloud.google.com/vertex-ai/generative-ai/docs/video/video-gen-prompt-guide)  
7. How to write effective text prompts to generate AI videos? FlexClip ..., 5月 26, 2025にアクセス、 [https://help.flexclip.com/en/articles/10326783-how-to-write-effective-text-prompts-to-generate-ai-videos](https://help.flexclip.com/en/articles/10326783-how-to-write-effective-text-prompts-to-generate-ai-videos)  
8. AI Video Prompt Writing: Structured Templates and Description for ..., 5月 26, 2025にアクセス、 [https://www.reddit.com/r/StableDiffusion/comments/1j4yhlb/ai\_video\_prompt\_writing\_structured\_templates\_and/](https://www.reddit.com/r/StableDiffusion/comments/1j4yhlb/ai_video_prompt_writing_structured_templates_and/)  
9. Transforming Styles and Environments with Sora Create AI Videos \- TikTok, 5月 26, 2025にアクセス、 [https://www.tiktok.com/@openai/video/7337000211228708139](https://www.tiktok.com/@openai/video/7337000211228708139)  
10. I write about AI for a living and I haven't seen AI video as realistic as ..., 5月 26, 2025にアクセス、 [https://www.techradar.com/computing/artificial-intelligence/i-write-about-ai-for-a-living-and-i-havent-seen-ai-video-as-realistic-as-veo-3-before-here-are-the-9-best-examples](https://www.techradar.com/computing/artificial-intelligence/i-write-about-ai-for-a-living-and-i-havent-seen-ai-video-as-realistic-as-veo-3-before-here-are-the-9-best-examples)  
11. Anime Prompts \- PromptHero, 5月 26, 2025にアクセス、 [https://prompthero.com/anime-prompts](https://prompthero.com/anime-prompts)  
12. 2 prompts that worked amazingly to create anime style images in the style of Studio Ghibli, Makoto Shinkai. Images are in the comments. : r/ChatGPTPromptGenius \- Reddit, 5月 26, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1j8eyos/2\_prompts\_that\_worked\_amazingly\_to\_create\_anime/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1j8eyos/2_prompts_that_worked_amazingly_to_create_anime/)  
13. Google Veo 2 Video Generator Turn Text & Images to Video ..., 5月 26, 2025にアクセス、 [https://getimg.ai/models/google-veo-2](https://getimg.ai/models/google-veo-2)  
14. Google Veo 2: Video Prompting Guide — Shep Bryan, 5月 26, 2025にアクセス、 [https://www.shepbryan.com/blog/google-veo-2-video-prompt-guide](https://www.shepbryan.com/blog/google-veo-2-video-prompt-guide)  
15. Tried out Googles new Veo 3 AI to make a quick cinematic shot ..., 5月 26, 2025にアクセス、 [https://www.reddit.com/r/cinematography/comments/1kus1hj/tried\_out\_googles\_new\_veo\_3\_ai\_to\_make\_a\_quick/](https://www.reddit.com/r/cinematography/comments/1kus1hj/tried_out_googles_new_veo_3_ai_to_make_a_quick/)  
16. Make Your Photos Look Breathtaking With These 10 AI Image Styles & Filters, 5月 26, 2025にアクセス、 [https://felloai.com/2025/04/make-your-photos-look-breathtaking-with-these-10-ai-image-styles-filters/](https://felloai.com/2025/04/make-your-photos-look-breathtaking-with-these-10-ai-image-styles-filters/)  
17. cinematic global illumination prompts \- PromptHero, 5月 26, 2025にアクセス、 [https://prompthero.com/search?model=All+models\&q=cinematic+global+illumination](https://prompthero.com/search?model=All+models&q=cinematic+global+illumination)  
18. glass textures prompts \- PromptHero, 5月 26, 2025にアクセス、 [https://prompthero.com/search?q=glass+textures](https://prompthero.com/search?q=glass+textures)  
19. sitting on park bench prompts \- PromptHero, 5月 26, 2025にアクセス、 [https://prompthero.com/search?q=sitting+on+park+bench\&source=3f935646aa7](https://prompthero.com/search?q=sitting+on+park+bench&source=3f935646aa7)  
20. Google's Veo 3: A Guide With Practical Examples \- DataCamp, 5月 26, 2025にアクセス、 [https://www.datacamp.com/tutorial/veo-3](https://www.datacamp.com/tutorial/veo-3)  
21. Makoto Shinkai prompts \- PromptHero, 5月 26, 2025にアクセス、 [https://prompthero.com/search?q=Makoto+Shinkai](https://prompthero.com/search?q=Makoto+Shinkai)  
22. Generate video using Veo Gemini API Google AI for Developers, 5月 26, 2025にアクセス、 [https://ai.google.dev/gemini-api/docs/video](https://ai.google.dev/gemini-api/docs/video)  
