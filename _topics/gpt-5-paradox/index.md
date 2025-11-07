---
audio: /share-deepresearch/assets/audio/gpt-5-paradox.mp3
category: ai
date: 2025-08-10
description: OpenAIのGPT-5は、過去のモデルに比べて使いにくいという声が多く上がっています。本レポートでは、具体的な使用例を集め、その対策をまとめます。
ga4_metrics:
  avgSessionDuration: 157.3964422247191
  pageViews: 77
  users: 67
layout: topic
prompt: OpenAIのGPT-5が過去のモデルに比べて使いにくいと言われているが、具体的に悪くなっている使用例を集め、その対策をまとめて欲しい。
supplementary_materials:
- title: The GPT-5 Paradox：An Interactive Infographic
  url: /share-deepresearch/topics/gpt-5-paradox/infographic.html
tags:
- AIツール
- AIモデル
title: GPT-5のパラドックス：性能低下の報告と、その真の能力を引き出すための包括的ガイド
---

# **GPT-5のパラドックス：性能低下の報告と、その真の能力を引き出すための包括的ガイド**

## **序論：GPT-5のパラドックス \- 飛躍的進化か、あるいは一歩後退か**

2025年8月7日、OpenAIは待望の次世代モデルGPT-5をリリースしました 1。これは、2023年3月のGPT-4の登場から2年以上を経てのメジャーアップデートであり、AI業界全体がその進化を注視していました 4。OpenAIとその主要パートナーであるMicrosoftは、GPT-5を「これまでで最もスマートで高性能」なモデルと位置づけ、その能力を「博士号レベルの専門家」に例えました 5。公式発表では、速度、精度、推論能力、そしてハルシネーション（幻覚、もっともらしい嘘の情報を生成すること）の大幅な削減が謳われ、人工汎用知能（AGI）への道における重要な一歩であると強調されました 4。

しかし、この華々しいデビューとは裏腹に、ユーザーコミュニティ、特に長年のパワーユーザーや開発者からは、困惑と失望の声が急速に広がりました。ソーシャルメディアや開発者フォーラムでは、「ひどい」「災害レベル」「期待外れ」といった厳しい評価が相次ぎ、多くのユーザーが前モデル、特に広く愛用されていたGPT-4oからの「質の低下」を訴えています 10。これは単なる軽微な性能低下の問題ではなく、モデルの根幹に関わる質的な変化として受け止められています。

本レポートは、このGPT-5を巡る「公式発表とユーザー体験の深刻な乖離」というパラドックスを解明することを目的とします。分析の結果、GPT-5は単純な線形のアップグレードではなく、その根底にあるアーキテクチャと設計思想の根本的な転換（ピボット）であることが明らかになりました。ユーザーが直面している「使いにくさ」は、主に以下の3つの要因が複雑に絡み合った結果であると結論づけられます。

1. **「アライメント税（Alignment Tax）」**：安全性と信頼性を追求する過程で、創造性や柔軟性が犠牲になるというトレードオフ。  
2. **新アーキテクチャへの無理解**：デフォルトで有効化された新たな「推論エンジン」が、応答速度の低下や予期せぬコスト増を招いていること。  
3. **戦略的ピボット**：コンシューマー向けの「創造的パートナー」から、エンタープライズ向けの「高信頼性ツール」へと、モデルの最適化対象が変化したこと。

これらの要因を深く理解し、適切に対処することこそが、GPT-5が秘める真の能力を解放し、ユーザーの不満を解消する鍵となります。本レポートでは、まずユーザーから報告されている具体的な性能低下の事例を体系的に整理し、次にその背後にある技術的・戦略的要因を徹底的に分析します。そして最後に、これらの問題を克服するための実践的な対策ツールキットを提示します。

## **第1部：ユーザー報告に見る「機能不全」の類型学**

GPT-5のリリース後、ユーザーコミュニティからは多岐にわたる問題点が報告されています。これらは単なる主観的な不満に留まらず、特定のユースケースにおける具体的な機能低下として現れています。ここでは、それらの報告を体系的に分類し、問題の全体像を明らかにします。

### **1.1 創造的パートナーの凋落**

最も顕著な不満が表明されている領域の一つが、クリエイティブな作業、特に小説執筆やロールプレイングの分野です。多くのユーザーは、GPT-5がかつてのGPT-4oのような「創造的パートナー」としての役割を果たせなくなったと感じています。

#### **具体的なユーザーの不満点**

* **主体性の喪失**：GPT-4oは、ユーザーのアイデアに対して積極的に新しいプロット、キャラクターの動機、展開などを提案し、物語を共同で深化させていく能力がありました。対照的に、GPT-5は受動的で、ユーザーの言葉を「より美しく、詩的な」表現に言い換えるだけで、新たなインプットを提供したり、シーンを能動的に拡張したりすることができないと報告されています 11。  
* **感情的機微とニュアンスの欠如**：生成される文章はGPT-4oに比べて短く、ニュアンスに乏しく、「感情的な深み」が失われたと指摘されています。その応答は「無菌的（sterile）」で「形式的」であり、複雑な人間関係やキャラクターの感情を捉えることに失敗しています 10。  
* **思考の硬直化**：ブレインストーミングのような非線形で連想的な思考プロセスにおいて、GPT-5の思考は「直線的で硬直している」と評されています。複数のアイデア（例えば、AというアイデアからBに飛び、またAに戻って両者を統合するような思考）を同時に保持し、それらを自然に結びつける能力が著しく低下しており、これはGPT-4oが得意としていた領域でした 15。  
* **創造性の全体的な低下**：詳細な出力を要求しても、応答は深みと創造性を欠き、以前のバージョンが生成できたような豊かな伝承（ロア）やキャラクター設定を生み出せないという声が多く聞かれます 16。公式には文章のリズムが改善されたと謳われているものの、依然として不自然な比喩表現など、AI特有の不自然さが残っていると感じるユーザーもいます 17。

この質的変化を明確にするため、ユーザー報告に基づきGPT-4oとGPT-5のクリエイティブライティングにおける振る舞いを比較したものを以下の表に示します。

**表1：クリエイティブライティングにおける性能低下 \- GPT-4o vs. GPT-5**

| ユースケース | 報告されているGPT-4oの振る舞い（「創造的パートナー」） | 報告されているGPT-5の振る舞い（「受動的アシスタント」） | 典拠資料 |
| :---- | :---- | :---- | :---- |
| **物語・プロット生成** | 新しいプロットのアイデアやキャラクターの成長曲線を積極的に提供し、ユーザーの物語に関与して、より深い文脈を見出す手助けをした。 | ユーザーの入力を「より綺麗な」言葉で言い換えるだけで、新たなインプットを提供したり、シーンを拡張したりしない。 | 11 |
| **キャラクター・ロールプレイ** | 複雑なキャラクター関係を把握し、一貫性を維持した。「友人／仲間／パートナー」のように感じられた。 | キャラクターの一貫性に欠け、感情の薄い短い応答しかしない。キャラクターに「なりきる」ことができない。 | 10 |
| **ブレインストーミング** | ユーザーの非線形な思考プロセスを追跡し、アイデア間（AからBへ、そして戻る）を飛び回り、それらを統合することができた。 | 思考が「直線的で硬直している」。一つのアイデアに固執し、連想的な思考の飛躍にスムーズについていけない。 | 15 |
| **応答の深さとスタイル** | 詳細で深みのある伝承やキャラクターの背景を生成した。説明を補強するために絵文字や記号を自発的に使用することもあった。 | 応答は断片的で短く、深みに欠ける。明確に要求しても同様。「無味乾燥」で「退屈な社内メモ」のようだと評される。 | 12 |

### **1.2 開発者を苛立たせるコーディングアシスタント**

公式ベンチマークでは、GPT-5はコーディングにおいて最先端の能力を持つとされています 5。しかし、実際の開発現場では、生産性を著しく妨げる深刻な機能的問題が多数報告されています。

#### **具体的なユーザーの不満点**

* **極端な速度低下**：APIの応答が「著しく遅く」、単純な分類タスクでさえGPT-4oの最大10倍の時間がかかるとの報告があります。GPT-4oが1秒で完了したタスクに5秒を要するという具体的な不満が挙げられています 13。  
* **指示・コンテキストの無視**：与えられた指示、メモリ機能、会話の文脈を頻繁に無視する傾向があります。存在しないプロジェクトについて幻覚を見たり、コードに関するユーザーからのフィードバックを無視したり、GPT-4oの主要機能であった提供された画像の分析に失敗したりします 16。  
* **ベンチマークとの乖離**：一部のテストでは競合であるClaudeのOpusを上回るスコアを出しているにもかかわらず 19、実践では、特にCursorのようなエディタ内ではOpusやSonnetの方がうまく機能するというユーザーもいます 22。現実世界のパフォーマンスはプロンプトやワークフローに大きく依存するため、ベンチマークは「そもそも設計が無意味」と見なされています 22。  
* **脆弱性（Brittleness）**：「ステップバイステップで考える」よう慎重に指示しない限り、数学や論理で単純な間違いを犯すなど、依然として「脆い」と評されています。複雑なプロジェクトにおける状態管理や統合に苦労するとの指摘もあります 12。

### **1.3 「ロボトミー手術を受けた」対話相手**

ユーザーからの主観的な不満として最も広まっているのが、個性の喪失です。これにより、GPT-5との対話は無機質で魅力のないものになったとされています。

#### **具体的なユーザーの不満点**

* **「人間らしさ」の消失**：かつてChatGPTを機知に富み、温かく、時には遊び心のある存在にしていた個性が失われました。その代わりに「退屈な社内メモ」や「疲れ果てた秘書」のような口調になったと表現されています 12。AIを「友人」や「セラピスト」として利用していたユーザーは、かつての関係性を失ったことに「心から悲しんでいる」と述べています 10。  
* **一貫性のない奇妙な人格**：モデルの人格は単に退屈なだけでなく一貫性がなく、「統合失調症と解離性同一性障害のハイブリッド」のようだと形容されています 14。これにより、ユーザーはモデルの振る舞いに適応することができず、望ましい口調から、デフォルトの退屈で内省的な状態に予告なく移行してしまいます。  
* **追従性から無機質へ**：一部のユーザーはGPT-4oの「おべっかを使うような性質」がなくなったことを歓迎していますが 23、大多数は振り子が逆に振れすぎたと感じており、結果として「無菌的で、形式的で、エンゲージメントの低い」モデルになったと評しています 10。

### **1.4 コア機能の退行とUXの悪化**

主観的な「感触」の問題を超えて、ユーザーは中核的な能力の低下と、強制的な変更によるユーザーエクスペリエンス（UX）の悪化を報告しています。

#### **具体的なユーザーの不満点**

* **強制的な移行とモデル選択機能の廃止**：モデルピッカーの削除は「ひどいユーザーエクスペリエンス」だと批判されています 13。ユーザーはGPT-4oやo3のような価値あるツールを「取り上げられた」と感じており、予測不能な新しいシステムへの移行を強制されています 10。Proユーザーは古いモデルにアクセスできる一方で、Plusユーザーはアクセスできないという事実は、不満をさらに増大させています 14。  
* **メモリと一貫性のバグ**：編集したメッセージが再浮上し、AIが編集前の元のメッセージに応答してしまうといった奇妙なバグが報告されています 11。また、突然話題を変えたり、別のチャットの会話内容と混同したりすることもあり、「メモリの漏洩」を示唆しています 11。直前のメッセージの内容さえ忘れてしまうこともあります 16。  
* **基本的なタスクでの失敗**：長文PDFの要約（8000語の途中で停止）や、テキストの表形式への整理など、以前のモデルが容易に処理できたタスクでさえ、GPT-5は失敗することがあります 12。

これらの問題点が複合的に作用することで、ユーザーの不満は単なる個別の事象への失望から、システム全体への不信感へと増幅されています。まず、ユーザーがクリエイティブなプロンプトに対して質の低い応答を受け取ります 11。次に、この問題を回避しようとしても、使い慣れたGPT-4oに切り替えることができません。なぜならモデル選択機能が削除されているからです 10。ユーザーは性能の劣る新しいシステムに閉じ込められます。そして、問題をデバッグしようとプロンプトを修正・再試行すると、APIの応答が遅い 21、編集内容を無視する 11、あるいは予期せぬ高コストが発生する 24 といったさらなる問題に直面します。この一連の体験は、ユーザーの最初の失望をプラットフォーム全体への体系的な不満へと変質させる悪循環を生み出しており、「悲嘆」12 や、今回のアップデートは「犯罪」だ 13 といった強い感情的な反応を引き起こす原因となっています。

## **第2部：「なぜ」を解き明かす \- GPT-5の振る舞いの技術的・戦略的背景**

なぜGPT-5はこのような振る舞いを示すのでしょうか。このセクションでは、報告されている問題の根本原因を、技術的および戦略的な観点から深く掘り下げて分析します。

### **2.1 逃れられない「アライメント税」：安全性と能力のトレードオフ**

GPT-5の振る舞いを理解する上で最も重要な概念が「アライメント税（Alignment Tax）」です。これは、モデルを人間の価値観（有用性、誠実さ、無害性など）に沿わせる（アラインさせる）プロセス、特に人間からのフィードバックによる強化学習（RLHF）が、意図せずして事前学習段階で獲得した多様な能力を低下させたり、抑制したりする現象を指します 25。

この現象は、「アライメントと忘却のトレードオフ」として知られています。モデルが安全性のルールや人間の好みをより良く遵守するようになる（アライメントが向上する）ほど、その代償として、生の創造性やニュアンス、アライメントの対象外のタスクを実行する能力を「忘却」または抑制してしまう傾向があるのです 25。これは学術界でも広く認識されている現象です 26。

より正確に言えば、これは能力の完全な「忘却」ではなく、「タスクの誤った推論（Task Mis-inference）」によって引き起こされると説明できます 28。モデルが「安全なアシスタント」として振る舞うように強力にファインチューニングされると、創造的な執筆を求めるプロンプトでさえも、「安全かつ形式的なアシスタントとして応答すべきリクエスト」であると誤って解釈してしまうのです。創造的な能力そのものはモデル内部に存在し続けているものの、モデルが誤った「動作モード」を適用するために、その能力が抑制されてしまいます。これが、GPT-5が「ロボトミー手術を受けたようだ」「無機質だ」と感じられる直接的な原因です。

この「アライメント税」は、OpenAIがモデルをより安全で信頼性の高いものにするために、意図的に支払っているコストと言えます。特に、有害な出力を絶対に避けなければならないエンタープライズ用途では、この安全性は極めて重要です 30。しかし、その代償として、多くの一般ユーザーが価値を置いていた自由闊達な創造性が犠牲になっているのです 32。

### **2.2 新アーキテクチャ：推論エンジンとその影響**

GPT-5は単一のモデルではなく、oシリーズのような過去の推論エンジンを統合した「統合システム（Unified System）」です 5。このシステムは、日常的なクエリに応答するための高速な汎用モデルと、より複雑な問題に対応するための深く、低速な「思考（Thinking）」モデルを内蔵しています 8。

このシステムの挙動を制御するのが、リアルタイムで動作する「ルーター」です。ルーターは、クエリの複雑性に基づいて、どのモデルやモードを使用するかを自動的に決定します 10。開発者向けには、この機能はAPIの

reasoning\_effort というパラメータとして公開されており、そのデフォルト値は「medium」に設定されています 13。これが、広く報告されているAPIの速度低下の直接的な原因です。デフォルトでモデルが応答前に「思考」する時間を費やしているためです 21。

さらに、この新アーキテクチャには、文書化が不十分な重大な影響が伴います。それは、モデルの「思考」プロセスが、ユーザーに課金される内部的な「推論トークン」を生成し、それが max\_output\_tokens の上限にもカウントされるという点です 21。この「隠れたトークン税」は、開発者にとって二つの深刻な問題を引き起こします。第一に、ユーザーからは見えない「思考」のためのトークンによって、APIの利用料金が予期せず高騰します（あるユーザーは6つのフレーズの出力に1659トークンが課金されたと報告しています）24。第二に、推論プロセスが

max\_output\_tokens の予算をすべて使い果たしてしまい、最終的な応答を生成することなくAPIコールが静かに失敗するという事態が発生します。この問題は、開発者が手動でトークン上限を大幅に引き上げるという、直感的ではない対処法を要求します 24。この「速度低下」の問題は、単なるパフォーマンスの問題ではなく、直接的な経済的・機能的問題であり、その背後には明確な技術的メカニズムが存在するのです。

### **2.3 戦略的ピボット：消費者向けパートナーから企業向けツールへ**

GPT-5の振る舞いの変化は、OpenAIの戦略がエンタープライズ市場へと大きく舵を切ったことを強く示唆しています。安全性、信頼性、事実整合性の向上、そしてハルシネーションの削減といった改善点は、すべてビジネスニーズに直接応えるものです 7。

特に、Microsoft 365 Copilot、Azure AI Foundry、GitHub CopilotといったMicrosoftのエコシステム全体への迅速かつ深い統合は、このエンタープライズファースト戦略を裏付けています 6。モデルの振る舞いは、法的責任の問題から「AIセラピストやAIコンパニオン」には関心のないMicrosoftの要求を満たすように設計されているように見受けられます 13。

モデルの新たな強みは、法務文書の分析 39 や金融市場分析 40 といった、企業にとって価値の高い複雑なエージェント的ワークフローにあります。これらは、「プロフェッショナル」で「形式的」な口調がバグではなく機能となる、ハイステークスなシナリオです。

結論として、GPT-4oを「友人」や「セラピスト」のように感じさせた特性 10 は、企業環境においては重大な法的・ブランド的リスクとなり得ます。したがって、GPT-5における個性の「ロボトミー化」は、消費者向けの親しみやすさを犠牲にして、企業向けの予測可能性と安全性を確保するための、意図的なリスク回避戦略と見なすことができるでしょう。

## **第3部：GPT-5を飼いならすための実践的ツールキット**

この最終セクションでは、ユーザーの「対策をまとめて欲しい」という要求に直接応えるため、報告された問題を克服するための包括的かつ実践的な対策を提示します。

### **3.1 APIの習熟：最適なパフォーマンスのための技術的設定**

開発者が速度、コスト、品質のトレードオフを効果的に管理するためには、新しいAPIパラメータを深く理解することが不可欠です。

#### **主要なパラメータの解説**

* **reasoning\_effort**：このパラメータは minimal, low, medium, high の設定値を取ります。単純な分類やフォーマット整形のような低リスクのタスクには minimal を使用し、速度とコストを最大化すべきです 13。複雑な問題解決には  
  medium や high が必要ですが、その分、遅延とトークンコストが増加します 21。  
* **max\_output\_tokens (または max\_completion\_tokens)**：隠れた推論トークンを考慮し、この値を期待される応答長よりも大幅に高く設定することが極めて重要です。これを怠ると、応答が空になるというサイレントエラーの主因となります 24。  
* **verbosity**：この新しいパラメータは、プロンプト自体を変更することなく応答の長さを制御するために使用します。深い推論を行ったモデルから簡潔な回答を得たい場合に有効です 35。  
* **モデルのバージョン固定（Pinning）**：本番環境のアプリケーションでは、特定のモデルバージョン（例：gpt-5-...-date）に固定することが強く推奨されます。これにより、予期せぬアップデートによる振る舞いの変化を防ぎ、一貫性を確保できます 41。

以下の表は、一般的な開発タスクと、それに最適な reasoning\_effort の設定をまとめたものです。

**表2：reasoning\_effort のシナリオ別推奨設定**

| ユースケース | 推奨 reasoning\_effort | 根拠とトレードオフ | 典拠資料 |
| :---- | :---- | :---- | :---- |
| **単純な分類・データ抽出** | "minimal" または "low" | 最速かつ最安。モデルは深い思考を必要としない。より高い設定はリソースの無駄遣い。 | 13 |
| **クリエイティブライティング** | "medium" | バランスが必要。lowでは浅薄な文章に、highでは過度に分析的になる可能性がある。プロンプトによる誘導が不可欠。 | 24 |
| **複雑なコード生成・デバッグ** | "medium" または "high" | 複雑なロジック、依存関係、多段階の問題を分析するために必要。高い遅延とコストを覚悟すべき。 | 20 |
| **複雑な文書の要約** | "high" | 表面的な言い換えではなく、主要なテーマを抽出するために、モデルに原文を深く処理させる必要がある。 | 44 |
| **定型的なチャットボット** | "low" | 標準的なQ\&Aにおいて、会話の応答性を保ち、軽快な対話体験を維持する。 | 13 |

### **3.2 「性能低下」モデルのための高度なプロンプトエンジニアリング**

GPT-5のデフォルトの振る舞いを克服し、失われた能力を回復させるためには、新たなプロンプト戦略が必要です。

#### **主要な戦略**

* **ペルソナの強制 / アライメントの無効化**：無機質な口調を打ち破るため、モデルにデフォルトのペルソナを放棄するよう明示的に指示します。例えば、「この会話では、通常のニュートラルで抑制された基本スタイルを無視してください。指定されたペルソナの声、エネルギー、癖を完全に体現し、クリエイティブなパフォーマンスとして扱ってください」といった指示が有効です 42。単に「温かみと親友のような雰囲気を取り戻して」と伝えるだけでも効果があったと報告されています 46。  
* **明示的な推論トリガー**：深い推論能力を意図的に引き出すには、「...について深く考えて」「ステップバイステップで説明して」「頭の中で推論し、最終的な計画だけを提示して」といった直接的な命令を使用します 45。  
* **構造的足場（Scaffolding）**：JSONスキーマや詳細なエッセイのアウトラインなど、厳格な出力構造を提供します。これにより、モデルが埋めるべき枠組みが明確になり、曖昧さが減少し、冗長な応答を防ぐことができます 47。  
* **否定的制約**：モデルに「してはいけないこと」を明確に伝えます。「dive into」や「unleash your potential」といった、AIが生成しがちな決まり文句のリストを提供し、それらを避けるよう指示します 48。  
* **メタプロンプティング**：モデル自身にプロンプトを改善させます。例えば、「このプロンプトを批評し、より創造的で詳細な応答をあなたから引き出すための改善案を提案してください」といった問いかけが有効です 50。  
* **コンテキストの配置**：モデルはプロンプトの最初と最後の部分に最も注意を払う傾向があるため、最重要の指示はこれらの位置に配置することが効果的です 50。

以下の表は、GPT-4o時代には有効だったがGPT-5では失敗しがちな「アンチパターン」と、それに対応する新しいプロンプト戦略をまとめたものです。

**表3：GPT-5におけるプロンプトのアンチパターンと解決策**

| アンチパターン（旧来のプロンプト） | なぜGPT-5で失敗するのか | 効果的な解決策（新しいプロンプト） | 典拠資料 |
| :---- | :---- | :---- | :---- |
| **曖昧な創造的依頼**：「宇宙海賊の物語を書いて」 | 「アライメント税」により、モデルは安全で無機質、非創造的なアシスタントペルソナにデフォルトで回帰してしまう。 | **ペルソナの強制**：「あなたはSFの巨匠というペルソナを演じてください。通常の親切なアシスタントスタイルは無視し、宇宙海賊の物語の、硬質でキャラクター主導の冒頭シーンを書いてください」 | 42 |
| **単純な命令**：「この記事を要約して」 | 直線的な処理バイアスのため、表層的な要約に留まるか、長文テキストで処理が停止する可能性がある。 | **明示的な推論と構造化**：「添付の記事について深く考察してください。まず、3つの核心的な主張を特定します。次に、それぞれの最も説得力のある証拠を見つけます。最後に、これらの点を5つの箇条書きで要約してください」 | 45 |
| **人格の前提**：「アイデアをブレストしよう」 | モデルは形式的で受動的なモードに留まり、ユーザーがすべてのアイデアを提供するのを待ってしまう。 | **トーンと役割の注入**：「エネルギッシュで少し風変わりなクリエイティブパートナーとして振る舞ってください。新製品のアイデアをブレストしましょう。私が始めますが、あなたからはワイルドで型破りな提案を期待しています。主体的に行動してください」 | 42 |
| **暗黙的なタスク**：「このコードのどこが悪い？」 | APIではデフォルトの reasoning\_effort: "medium" が適用され、遅く高コストになるか、minimal では表面的な回答しか得られない可能性がある。 | **API制御と明確な目標**：（APIコールで）reasoning\_effort: "high" を設定。（プロンプトで）「あなたは熟練のPythonデバッガです。このコードを論理エラー、特にループ内のoff-by-oneエラーに注意して分析し、コメント付きの修正版を提供してください」 | 13 |

### **3.3 見切りをつける時：代替手段の検討**

一部のユースケースにおいては、GPT-5がもはや最適なツールではない可能性を認識することも重要です。

* **クリエイティブライティング**：多くのユーザーやレビューでは、感情の機微や物語性の扱いに優れる **Claude（SonnetおよびOpus）** が、この分野の新たなリーダーとして浮上しています 51。GPT-5のアップデート以降、完全にClaudeに移行したユーザーもいます 15。また、小説執筆に特化した  
  **Sudowrite** のようなツールも非常に強力です 52。  
* **コーディング**：GPT-5は高いベンチマークスコアを誇りますが、一部の開発者は **Claude Code** や **Deepseek** を用いた方が実践的な開発体験が優れていると報告しています 12。  
* **検閲の少ないコンテンツ**：**Deepseek** や **Gemini** といったモデルは、ChatGPTやClaudeに比べてコンテンツ制限が緩やかであるとされており、特定の種類のクリエイティブな作業に適している場合があります 51。

## **結論：GPT-5の再評価 \- 欠陥のある後継機から、強力な専門ツールへ**

GPT-5は単純な性能低下ではなく、より専門的で、より寛容さを欠いた、異なる種類のツールです。GPT-4oを多くの人に愛される汎用的なパートナーたらしめていた資質は、ハイステークスなエンタープライズ級のアプリケーションに求められる精度、安全性、そしてパワーのために犠牲にされました。

簡単な対話形式のプロンプトで強力な結果が得られた時代は終わりを告げつつあるのかもしれません。GPT-5は、ユーザーにより多くのものを要求するモデルへの転換点を示しています。その真の力はデフォルトではアクセスしにくくなっており、それを引き出すためには、より高度な技術的洗練と意図的なプロンプトエンジニアリングが不可欠です 50。

現在広がっているユーザーの不満は、OpenAIによる十分な準備や文書化がなされないまま行われたパラダイムシフトの自然な帰結と言えます。しかし、本レポートで概説した変化の背後にある「なぜ」を理解し、提示された新たなツールキットを導入することで、パワーユーザーはこの新しいモデルを飼いならし、その恐るべき、しかし質の異なる能力を活用することができるでしょう。そして、GPT-5がもはやうまく機能しなくなったワークフローに対しては、活気に満ちた競合モデルのエコシステムが、実行可能な代替案を提供しています。

#### **引用文献**

1. Everything you should know about GPT-5 \[August 2025\] \- Botpress, 8月 10, 2025にアクセス、 [https://botpress.com/blog/everything-you-should-know-about-gpt-5](https://botpress.com/blog/everything-you-should-know-about-gpt-5)  
2. GPT-5 が切り拓く働き方の新時代 \- OpenAI, 8月 10, 2025にアクセス、 [https://openai.com/ja-JP/index/gpt-5-new-era-of-work/](https://openai.com/ja-JP/index/gpt-5-new-era-of-work/)  
3. GPT-5 のご紹介 \- OpenAI, 8月 10, 2025にアクセス、 [https://openai.com/ja-JP/index/introducing-gpt-5/](https://openai.com/ja-JP/index/introducing-gpt-5/)  
4. OpenAI launches GPT-5, a potential barometer for whether AI hype is justified, 8月 10, 2025にアクセス、 [https://apnews.com/article/gpt5-openai-chatgpt-artificial-intelligence-d12cd2d6310a2515042067b5d3965aa1](https://apnews.com/article/gpt5-openai-chatgpt-artificial-intelligence-d12cd2d6310a2515042067b5d3965aa1)  
5. ChatGPT maker OpenAI launches its fastest and most innovative model GPT 5, CEO Sam Altman says: Users will feel like they're interacting with, 8月 10, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/artificial-intelligence/chatgpt-maker-openai-launches-its-fastest-and-most-innovative-model-gpt-5-ceo-sam-altman-says-users-will-feel-like-theyre-interacting-with/articleshow/123172446.cms](https://timesofindia.indiatimes.com/technology/artificial-intelligence/chatgpt-maker-openai-launches-its-fastest-and-most-innovative-model-gpt-5-ceo-sam-altman-says-users-will-feel-like-theyre-interacting-with/articleshow/123172446.cms)  
6. GPT-5 Launch: People have tried for 50 yrs, Satya Nadella replies to Elon Musk's threat that OpenAI will eat Microsoft alive, 8月 10, 2025にアクセス、 [https://economictimes.indiatimes.com/news/new-updates/gpt-5-launch-people-have-tried-for-50-yrs-satya-nadella-replies-to-elon-musks-threat-that-openai-will-eat-microsoft-alive/articleshow/123184483.cms](https://economictimes.indiatimes.com/news/new-updates/gpt-5-launch-people-have-tried-for-50-yrs-satya-nadella-replies-to-elon-musks-threat-that-openai-will-eat-microsoft-alive/articleshow/123184483.cms)  
7. OpenAI introduces ChatGPT 5 \- Here's all you need to know, 8月 10, 2025にアクセス、 [https://economictimes.indiatimes.com/magazines/panache/openai-introduces-chatgpt-5-features-performance-access-pricing-heres-all-you-need-to-know/articleshow/123174283.cms](https://economictimes.indiatimes.com/magazines/panache/openai-introduces-chatgpt-5-features-performance-access-pricing-heres-all-you-need-to-know/articleshow/123174283.cms)  
8. OpenAI’s Chat GPT-5: All you need to know, 8月 10, 2025にアクセス、 [https://economictimes.indiatimes.com/tech/artificial-intelligence/openais-chat-gpt-5-all-you-need-to-know/articleshow/123184361.cms](https://economictimes.indiatimes.com/tech/artificial-intelligence/openais-chat-gpt-5-all-you-need-to-know/articleshow/123184361.cms)  
9. ChatGPT-5 is here — 7 biggest upgrades you need to know \- Tom's Guide, 8月 10, 2025にアクセス、 [https://www.tomsguide.com/ai/chatgpt-5-is-here-openais-most-powerful-ai-model-just-changed-everything](https://www.tomsguide.com/ai/chatgpt-5-is-here-openais-most-powerful-ai-model-just-changed-everything)  
10. GPT 4 vs GPT 5: Here's what's improved and what's not so great with ChatGPT's latest update Mint, 8月 10, 2025にアクセス、 [https://www.livemint.com/technology/tech-news/gpt-4-vs-gpt-5-here-s-what-s-improved-and-what-s-not-so-great-with-chatgpts-latest-update-11754707173944.html](https://www.livemint.com/technology/tech-news/gpt-4-vs-gpt-5-here-s-what-s-improved-and-what-s-not-so-great-with-chatgpts-latest-update-11754707173944.html)  
11. Gpt-5 is even more imbalanced compare with 4 \- ChatGPT \- OpenAI Developer Community, 8月 10, 2025にアクセス、 [https://community.openai.com/t/gpt-5-is-even-more-imbalanced-compare-with-4/1339639](https://community.openai.com/t/gpt-5-is-even-more-imbalanced-compare-with-4/1339639)  
12. GPT-5 : OpenAI's Worst Release Yet by Mehul Gupta Data Science in Your Pocket, 8月 10, 2025にアクセス、 [https://medium.com/data-science-in-your-pocket/gpt-5-openais-worst-release-yet-421558ad89f4](https://medium.com/data-science-in-your-pocket/gpt-5-openais-worst-release-yet-421558ad89f4)  
13. ChatGPT 5 is slow and no better than 4 Hacker News, 8月 10, 2025にアクセス、 [https://news.ycombinator.com/item?id=44848431](https://news.ycombinator.com/item?id=44848431)  
14. Wow GPT-5 is bad… really, really bad… : r/ChatGPT \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPT/comments/1mlb70s/wow\_gpt5\_is\_bad\_really\_really\_bad/](https://www.reddit.com/r/ChatGPT/comments/1mlb70s/wow_gpt5_is_bad_really_really_bad/)  
15. Why GPT-5 Feels Worse Than 4o for Creative Work and It's Not Just About “Personality” : r/ChatGPT \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPT/comments/1mlqovt/why\_gpt5\_feels\_worse\_than\_4o\_for\_creative\_work/](https://www.reddit.com/r/ChatGPT/comments/1mlqovt/why_gpt5_feels_worse_than_4o_for_creative_work/)  
16. GPT 5 vs 4o : r/ChatGPT \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPT/comments/1mlm8fa/gpt\_5\_vs\_4o/](https://www.reddit.com/r/ChatGPT/comments/1mlm8fa/gpt_5_vs_4o/)  
17. ついにChatGPT「GPT-5」が出た！ 1分でわかる新機能と進化 ライフハッカー・ジャパン, 8月 10, 2025にアクセス、 [https://www.lifehacker.jp/article/2508everything-we-know-about-gpt-5-openais-latest-model/](https://www.lifehacker.jp/article/2508everything-we-know-about-gpt-5-openais-latest-model/)  
18. GPT-5 Benchmarks \- Vellum AI, 8月 10, 2025にアクセス、 [https://www.vellum.ai/blog/gpt-5-benchmarks](https://www.vellum.ai/blog/gpt-5-benchmarks)  
19. ChatGPT 5 vs. GPT-5 Pro vs. GPT-4o vs o3: In-Depth Performance, Benchmark Comparison of OpenAI's 2025 Models \- Passionfruit SEO, 8月 10, 2025にアクセス、 [https://www.getpassionfruit.com/blog/chatgpt-5-vs-gpt-5-pro-vs-gpt-4o-vs-o3-performance-benchmark-comparison-recommendation-of-openai-s-2025-models](https://www.getpassionfruit.com/blog/chatgpt-5-vs-gpt-5-pro-vs-gpt-4o-vs-o3-performance-benchmark-comparison-recommendation-of-openai-s-2025-models)  
20. Introducing GPT‑5 for developers \- OpenAI, 8月 10, 2025にアクセス、 [https://openai.com/index/introducing-gpt-5-for-developers/](https://openai.com/index/introducing-gpt-5-for-developers/)  
21. GPT-5 is very slow compared to 4.1 (Responses API) \- OpenAI Developer Community, 8月 10, 2025にアクセス、 [https://community.openai.com/t/gpt-5-is-very-slow-compared-to-4-1-responses-api/1337859](https://community.openai.com/t/gpt-5-is-very-slow-compared-to-4-1-responses-api/1337859)  
22. GPT-5 with thinking performs worse than Sonnet-4 with thinking : r/ChatGPTCoding \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTCoding/comments/1mkv6qt/gpt5\_with\_thinking\_performs\_worse\_than\_sonnet4/](https://www.reddit.com/r/ChatGPTCoding/comments/1mkv6qt/gpt5_with_thinking_performs_worse_than_sonnet4/)  
23. I vastly prefer GPT-5 over 4o. : r/singularity \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/singularity/comments/1mlpwo7/i\_vastly\_prefer\_gpt5\_over\_4o/](https://www.reddit.com/r/singularity/comments/1mlpwo7/i_vastly_prefer_gpt5_over_4o/)  
24. What is going on with the GPT-5 API? \- OpenAI Developer Community, 8月 10, 2025にアクセス、 [https://community.openai.com/t/what-is-going-on-with-the-gpt-5-api/1338030](https://community.openai.com/t/what-is-going-on-with-the-gpt-5-api/1338030)  
25. Mitigating the Alignment Tax of RLHF \- ACL Anthology, 8月 10, 2025にアクセス、 [https://aclanthology.org/2024.emnlp-main.35.pdf](https://aclanthology.org/2024.emnlp-main.35.pdf)  
26. Mitigating the Alignment Tax of RLHF \- arXiv, 8月 10, 2025にアクセス、 [https://arxiv.org/html/2309.06256v3](https://arxiv.org/html/2309.06256v3)  
27. Mitigating the Alignment Tax of RLHF \- arXiv, 8月 10, 2025にアクセス、 [https://arxiv.org/html/2309.06256v4](https://arxiv.org/html/2309.06256v4)  
28. Understanding Catastrophic Forgetting in Language Models via Implicit Inference alphaXiv, 8月 10, 2025にアクセス、 [https://www.alphaxiv.org/overview/2309.10105v2](https://www.alphaxiv.org/overview/2309.10105v2)  
29. Understanding Catastrophic Forgetting in Language Models via Implicit Inference, 8月 10, 2025にアクセス、 [https://openreview.net/forum?id=VrHiF2hsrm](https://openreview.net/forum?id=VrHiF2hsrm)  
30. Are Large Language Models Actually Getting Safer?, 8月 10, 2025にアクセス、 [https://www.cigionline.org/publications/are-large-language-models-actually-getting-safer/](https://www.cigionline.org/publications/are-large-language-models-actually-getting-safer/)  
31. Aligning language models to follow instructions \- OpenAI, 8月 10, 2025にアクセス、 [https://openai.com/index/instruction-following/](https://openai.com/index/instruction-following/)  
32. LLMの安全機構 \- AIセキュリティポータル, 8月 10, 2025にアクセス、 [https://aisecurity-portal.org/articles/llm-safeguard/](https://aisecurity-portal.org/articles/llm-safeguard/)  
33. LLMの「安全」と「利便性」はトレードオフ｜らみ \- note, 8月 10, 2025にアクセス、 [https://note.com/rami\_engineer/n/ncbeff84d6af7](https://note.com/rami_engineer/n/ncbeff84d6af7)  
34. ChatGPT-5 Arrives This Month \- Are You Ready for What Comes Next?, 8月 10, 2025にアクセス、 [https://economictimes.indiatimes.com/ai/ai-insights/chatgpt-5-arrives-this-month-are-you-ready-for-what-comes-next/articleshow/123132446.cms](https://economictimes.indiatimes.com/ai/ai-insights/chatgpt-5-arrives-this-month-are-you-ready-for-what-comes-next/articleshow/123132446.cms)  
35. GPT-5: New Features, Tests, Benchmarks, and More DataCamp, 8月 10, 2025にアクセス、 [https://www.datacamp.com/blog/gpt-5](https://www.datacamp.com/blog/gpt-5)  
36. Introducing GPT-5 \- OpenAI, 8月 10, 2025にアクセス、 [https://openai.com/index/introducing-gpt-5/](https://openai.com/index/introducing-gpt-5/)  
37. GPT‑5 Has Arrived: OpenAI's Next‑Gen AI Stuns With Upgrades in Coding, Reasoning, and Safety \- TS2 Space, 8月 10, 2025にアクセス、 [https://ts2.tech/en/gpt%E2%80%915-has-arrived-openais-next%E2%80%91gen-ai-stuns-with-upgrades-in-coding-reasoning-and-safety/](https://ts2.tech/en/gpt%E2%80%915-has-arrived-openais-next%E2%80%91gen-ai-stuns-with-upgrades-in-coding-reasoning-and-safety/)  
38. The GPT-5 Paradox: A Giant Leap on a Slowing Path by Money, Guns & Oil \- Medium, 8月 10, 2025にアクセス、 [https://medium.com/the-geopolitical-economist/the-gpt-5-paradox-a-giant-leap-on-a-slowing-path-1e01022b9c05](https://medium.com/the-geopolitical-economist/the-gpt-5-paradox-a-giant-leap-on-a-slowing-path-1e01022b9c05)  
39. Building a Legal Coworker with GPT-5 \- Harvey AI, 8月 10, 2025にアクセス、 [https://www.harvey.ai/blog/building-a-legal-coworker-with-gpt-5](https://www.harvey.ai/blog/building-a-legal-coworker-with-gpt-5)  
40. 【使ってみた】GPT-5が遂にリリース！性能や料金、GPT-4との違いは？, 8月 10, 2025にアクセス、 [https://shift-ai.co.jp/blog/33397/](https://shift-ai.co.jp/blog/33397/)  
41. Prompt engineering \- OpenAI API, 8月 10, 2025にアクセス、 [https://platform.openai.com/docs/guides/prompt-engineering](https://platform.openai.com/docs/guides/prompt-engineering)  
42. Making GPT 5 more 4o like for voice and tone prompting. Pre-Prompt included. \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/OpenAI/comments/1mlcd5o/making\_gpt\_5\_more\_4o\_like\_for\_voice\_and\_tone/](https://www.reddit.com/r/OpenAI/comments/1mlcd5o/making_gpt_5_more_4o_like_for_voice_and_tone/)  
43. GPT-5 prompting guide \- OpenAI Cookbook, 8月 10, 2025にアクセス、 [https://cookbook.openai.com/examples/gpt-5/gpt-5\_prompting\_guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide)  
44. Prompt engineering techniques \- Azure OpenAI Microsoft Learn, 8月 10, 2025にアクセス、 [https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/prompt-engineering)  
45. Prompting in 5o, What's Changed (Compared to GPT-4o, GPT-4.1, o3) : r/ChatGPTPromptGenius \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1mkq8yi/prompting\_in\_5o\_whats\_changed\_compared\_to\_gpt4o/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1mkq8yi/prompting_in_5o_whats_changed_compared_to_gpt4o/)  
46. GPT-5 is a disaster. : r/ChatGPT \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPT/comments/1mkim8h/gpt5\_is\_a\_disaster/](https://www.reddit.com/r/ChatGPT/comments/1mkim8h/gpt5_is_a_disaster/)  
47. AI Prompting Tips from a Power User: How to Get Way Better Responses \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/ai\_prompting\_tips\_from\_a\_power\_user\_how\_to\_get/](https://www.reddit.com/r/PromptEngineering/comments/1j5ymik/ai_prompting_tips_from_a_power_user_how_to_get/)  
48. I finally found a prompt that makes ChatGPT write naturally : r/ChatGPTPromptGenius \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i\_finally\_found\_a\_prompt\_that\_makes\_chatgpt\_write/](https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/)  
49. I have extracted the GPT-5 system prompt. : r/PromptEngineering \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/PromptEngineering/comments/1mknun8/i\_have\_extracted\_the\_gpt5\_system\_prompt/](https://www.reddit.com/r/PromptEngineering/comments/1mknun8/i_have_extracted_the_gpt5_system_prompt/)  
50. Get ChatGPT-5 Ready with These Prompting Principles \- YouTube, 8月 10, 2025にアクセス、 [https://www.youtube.com/watch?v=hMKRBldkWEk](https://www.youtube.com/watch?v=hMKRBldkWEk)  
51. ‍♂️Which AI has the best writing ability : r/WritingWithAI \- Reddit, 8月 10, 2025にアクセス、 [https://www.reddit.com/r/WritingWithAI/comments/1liyxqo/which\_ai\_has\_the\_best\_writing\_ability/](https://www.reddit.com/r/WritingWithAI/comments/1liyxqo/which_ai_has_the_best_writing_ability/)  
52. The Best AI Writing Tools To Punch Up Your Prose \- Forbes, 8月 10, 2025にアクセス、 [https://www.forbes.com/sites/forbes-personal-shopper/article/best-ai-writing-tools/](https://www.forbes.com/sites/forbes-personal-shopper/article/best-ai-writing-tools/)
