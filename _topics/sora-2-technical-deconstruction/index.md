---
audio: /share-deepresearch/assets/audio/sora-2-technical-deconstruction.m4a
category: research
date: 2025-10-03
description: OpenAIのSora2は、簡単なプロンプトでストーリー性のある動画を生成する技術を持つ。このレポートでは、その仕組みや工夫について詳しく調査する。
ga4_metrics:
  avgSessionDuration: 8.579785
  pageViews: 3
  users: 2
layout: topic
prompt: OpenAIのSora2は簡単なプロンプトでストーリー性のある動画が作成されるが、その仕組や工夫している箇所について調査して欲しい。
tags:
- AIモデル
- 動画生成
title: Sora 2の解体新書：ワールドシミュレーターとしてのアーキテクチャ分析
video: /share-deepresearch/assets/video/sora-2-technical-deconstruction.mp4
---

# **Sora 2の解体新書：ワールドシミュレーターとしてのアーキテクチャ分析**

## **序論：画像生成から世界シミュレーションへ**

生成AIの進化は、静的な画像生成から動的なビデオ生成へと大きな飛躍を遂げている。この文脈において、OpenAIのSora 2は単なる「テキストからビデオへ」の変換ツールではなく、初期段階の「ワールドシミュレーター」として位置づけられるべき存在である。OpenAI自身も、物理世界を理解し、シミュレートするモデルの構築という野心的な目標を掲げている 1。

本レポートが分析する「ストーリー性」（ストーリー性）とは、AIが生成するビデオが物語として成立するための複数の要素を指す。具体的には、時間的整合性（オブジェクトが時間経過と共に正しく振る舞う）、オブジェクトの永続性（理由なくオブジェクトが消失しない）、キャラクターの一貫性（登場人物が視覚的に一貫している）、そして因果関係の妥当性（行動が信憑性のある結果をもたらす）である。これらの要素が組み合わさることで、単なる映像の断片ではなく、一貫した物語性を持つビデオが生まれる。

本稿の目的は、Sora 2が単純なプロンプトから、これほどまでに首尾一貫したストーリー性のあるビデオを生成できる技術的背景を解体し、分析することにある。そのために、まずモデルの心臓部であるアーキテクチャ（Diffusion Transformer）を詳述し、次にデータを表現するための革新的な手法（時空間パッチ）を解説する。さらに、モデルの学習方法と、物語性を生み出す創発的な能力を分析し、最後に競合モデルとの比較を通じて、AIビデオ生成市場におけるSora 2の位置づけを明らかにする。

## **第1章：Sora 2のアーキテクチャの心臓部 \- Diffusion Transformer (DiT)**

Sora 2の卓越した性能の根幹には、その革新的なモデルアーキテクチャ、Diffusion Transformer (DiT) がある。これは、従来の生成モデルで主流であったアーキテクチャからのパラダイムシフトであり、Sora 2の能力を理解する上で最も重要な要素である。

### **1.1 拡散モデルの基礎**

Sora 2の動作原理は、拡散モデル（Diffusion Model）に基づいている 2。このアプローチは、まず元となるデータ（この場合はビデオ）に段階的にノイズを加えていき、最終的に完全なランダムノイズ（静的ノイズ）の状態にする「順方向プロセス」と、その逆の「逆方向プロセス」から成る。モデルが学習するのは後者であり、ランダムノイズの状態から出発し、テキストプロンプトなどの条件付け情報を手がかりに、反復的なデノイズ（ノイズ除去）処理を通じて元のクリーンなデータを復元する 4。

さらに、Sora 2は計算効率を高めるために、潜在拡散モデル（Latent Diffusion Models, LDM）の技術を採用している 5。これは、高解像度のピクセル空間で直接デノイズ処理を行うのではなく、まず視覚エンコーダー（Variational Autoencoder, VAEなど）を用いてビデオデータを低次元の「潜在空間」に圧縮し、その圧縮された空間内で拡散プロセスを実行する手法である 7。これにより、計算負荷が大幅に削減され、より高品質なビデオ生成が可能となる。

### **1.2 Transformer革命：U-Netからのパラダイムシフト**

従来の拡散モデルの多くは、デノイズ処理のニューラルネットワークとしてU-Netと呼ばれるアーキテクチャを採用してきた 5。U-Netはその畳み込み構造により画像生成において大きな成功を収めたが、その一方で、ビデオのように時間軸に沿った長期的な依存関係を捉える能力には限界があった。

Sora 2の最大の革新は、このU-NetをTransformerアーキテクチャに置き換えたDiffusion Transformer (DiT) を採用した点にある 4。これはSoraの根幹をなすアーキテクチャ上の転換点である 2。Transformerは、自然言語処理の分野で大規模言語モデル（LLM）の成功を支えたアーキテクチャであり、データシーケンス内の長距離にわたる文脈的関係性を捉えることに非常に優れている 4。この特性が、ビデオのフレーム間で一貫性を保つという課題に対して、極めて有効に機能する。

このDiTへの移行は、単なるコンポーネントの置き換え以上の戦略的な意味を持つ。これは、近年の深層学習における二大成功パラダイム、すなわち拡散モデルとTransformerの融合を意味する。ビデオ生成という課題を、Transformerが得意とする「シーケンスモデリング問題」として再定義することにより、OpenAIはLLMで成功を収めた「スケーリング仮説」を視覚ドメインに適用することが可能になった。つまり、十分なデータとスケーラブルなアーキテクチャがあれば、モデルは創発的に汎用的な能力を獲得するという仮説である。したがって、DiTの採用は、単なるビデオ生成ツールではなく、「ワールドシミュレーター」を構築するという壮大な目標に向けた、計算論的な賭けなのである。

### **1.3 ビデオ生成におけるDiTのメカニズム**

Sora 2におけるDiTの動作プロセスは、以下のステップで構成される。まず、入力ビデオデータは後述する「時空間パッチ」のシーケンスに変換される。次に、このパッチシーケンスにノイズが加えられ、Transformerはテキストプロンプトと現在のデノイズステップ（タイムステップ）を条件として、加えられたノイズを予測し、除去するように学習する 2。

この条件付けのプロセスには、計算効率と性能のバランスが取れた適応的レイヤー正規化（adaptive layer normalization, adaLN）のような先進的な技術が用いられていると考えられる 5。これにより、モデルは与えられた指示に忠実でありながら、効率的に高品質なビデオを生成することが可能になる。

### **1.4 解き放たれたポテンシャル：スケーラビリティと汎用性**

DiTアーキテクチャがもたらす最大の利点は、その卓越したスケーラビリティにある。GPTのようなLLMがデータ量と計算能力の増大に伴って性能を飛躍的に向上させたのと同様に、DiTもまたスケーリング則の恩恵を受ける 5。

このスケーラビリティこそが、Soraを単一のカテゴリに特化したモデルではなく、「視覚データのジェネラリストモデル」たらしめている要因である 2。膨大なデータで大規模なTransformerを学習させることで、モデルは特定のタスクを超えた、より汎用的な世界の理解を獲得し始める。これが、Sora 2が多様なスタイルや内容のビデオを生成できる能力の源泉となっている。

## **第2章：時空間パッチ \- 視覚データの統一言語**

Sora 2がDiTアーキテクチャの能力を最大限に引き出すことを可能にしたもう一つの核心技術が、「時空間パッチ（Spacetime Patches）」である。これは、ビデオという連続的で高次元なデータを、Transformerが処理可能な形式に変換するための独創的なアプローチである。

### **2.1 ピクセルからパッチへ：視覚世界のトークン化**

LLMがテキストを「トークン」と呼ばれる離散的な単位に分割して処理するのと同様に、Sora 2はビデオを「パッチ」と呼ばれる視覚的な単位に分割する 2。具体的には、まずビデオ圧縮ネットワークを用いてビデオデータを低次元の潜在空間に圧縮し、その表現をさらに時間軸と空間軸に沿って小さな3次元のブロック、すなわち「時空間パッチ」のシーケンスに分解する 2。

各パッチは、ある瞬間の空間的な情報（フレームの見た目）と、それが時間と共にどう変化するかという時間的な情報の両方を含んでいる。この統一された表現方法は、画像（単一フレームのビデオと見なせる）とビデオを同じフレームワーク内でシームレスに扱うことを可能にし、モデルの汎用性を飛躍的に高めている 2。

### **2.2 ネイティブデータ処理の利点**

このパッチベースのシステムがもたらす決定的な利点は、モデルを固定サイズの入力という制約から解放したことにある。従来の多くのビデオ生成モデルは、学習データを正方形などの標準フォーマットにトリミングまたはリサイズする必要があった 2。この前処理は、元のビデオが持つ構図やアスペクト比を損なうだけでなく、学習データの多様性を制限する要因となっていた。

Sora 2は、時空間パッチを用いることで、ビデオや画像をネイティブの解像度、アスペクト比、デュレーションのまま学習データとして使用できる。その結果、生成されるビデオの構図はより自然で意図的になり、品質が大幅に向上する。OpenAIが公開した比較映像では、正方形にトリミングされたデータで学習したモデルが不自然な構図のビデオを生成するのに対し、Soraは被写体を適切にフレーミングしたビデオを生成していることが示されている 2。

### **2.3 柔軟な出力と制御の実現**

Sora 2はパッチのグリッド上で動作するため、生成時にパッチを任意のグリッド状に配置することで、望むアスペクト比のビデオを直接生成することができる 3。これにより、ワイドスクリーンの1920x1080pから、縦長の1080x1920まで、あらゆるフォーマットのビデオをネイティブに生成することが可能になる 2。

この柔軟性は、YouTubeやTikTokなど、異なるプラットフォームをターゲットとするクリエイターにとって、後処理でのトリミングによる品質劣化を避けることができるという、非常に大きな実用的利点となる。

時空間パッチという概念は、ワールドシミュレーターという壮大な目標を技術的に実現可能にするための基礎的なイノベーションである。それは、ビデオという非構造的で連続的な問題を、Transformerが解決するために設計された構造的でシーケンシャルな問題へと変換する。この「翻訳」プロセスは、単なる効率化にとどまらない。モデルがデータを「知覚」する方法を根本的に変える。ピクセルの集合体としてではなく、イベントと空間的配置の構造化されたシーケンスとして世界を見るようになる。この構造化された知覚こそが、オブジェクトの永続性、因果関係、物理法則といった、シミュレーターに不可欠な高レベルの概念を学習するための前提条件となる。したがって、パッチはピクセルを描くことから世界をモデル化することへの架け橋なのである。

## **第3章：ストーリー性の創発 \- 一貫性と整合性の実現**

ユーザーが求める「ストーリー性」は、Sora 2が単なる映像生成ツールを超えた存在であることを示す最も重要な側面である。この物語性は、プログラムされた機能ではなく、DiTアーキテクチャと時空間パッチが、時間と空間にわたる長距離の依存関係をモデル化することに成功した結果として「創発」する能力である。

### **3.1 長距離の首尾一貫性とオブジェクトの永続性**

一貫した物語には、時間を通じて矛盾のない世界が必要である。Sora 2のTransformerアーキテクチャは、時空間パッチのシーケンス全体にわたって注意（attention）を向けることで、ビデオ内の長距離の依存関係を効果的にモデル化する 1。これが、時間的整合性を維持する核心的なメカニズムである。

その結果、Sora 2はオブジェクトの永続性（object permanence）において顕著な能力を示す。被写体や背景要素が一時的にフレームアウトしたり、他のオブジェクトに隠されたりしても、それらが矛盾なく存在し続けることができる 1。これは、以前のモデルでは非常に困難であった課題であり 11、視聴者がビデオの世界を信頼できるものとして認識するために不可欠な要素である。

### **3.2 キャラクターの一貫性：AIビデオの聖杯**

物語の中心にはキャラクターが存在する。Sora 2は、単一の生成ビデオ内で複数のショットにわたってキャラクターの見た目やスタイルを一貫して維持する能力が向上している 1。OpenAIのCEOであるサム・アルトマンが特に強調する「Cameo」機能は、ユーザー自身や友人をビデオに登場させることができるものであり、これはモデルが高いレベルでキャラクターの一貫性を維持できることの証左である 15。

Sora 2が内部で用いている具体的な技術は公開されていないが、この能力は、参照画像の使用、プロンプトの連鎖的変更、潜在空間での特徴量の制御、あるいはキャラクター固有のLoRA（Low-Rank Adaptation）の学習といった、現在の最先端技術から着想を得ている可能性が高い 16。これらの技術は、AIが特定のキャラクターのアイデンティティを「記憶」し、異なる状況やポーズで再生成することを可能にする。

### **3.3 物理法則と世界の相互作用のシミュレーション**

Sora 2は、オブジェクトが物理世界でどのように存在し、相互作用するかについて、より深い理解を示している 1。これは、単に見た目を模倣するだけでなく、世界の基本的なルールをシミュレートしようとする試みである。例えば、Sora 2が生成したビデオでは、バスケットボールのシュートが外れた場合、ボールはバックボードに当たって跳ね返る。これは、以前のモデルのようにボールが不自然にゴールに吸い込まれるのとは対照的である 19。

この「データ駆動の物理エンジン」とも呼べる能力は 20、特定の物理法則をプログラムとして与えられた結果ではなく、膨大な量の現実世界のビデオデータを学習することで、重力や衝突、流体力学といった現象のパターンをモデルが内的に獲得した創発的な特性である 20。

しかし、このシミュレーション能力にはまだ限界がある。ガラスが割れるような複雑な相互作用、クッキーを一口食べても歯形がつかないといった因果関係の不整合、あるいは左右の空間認識の混同など、物理的に不自然な挙動を示すことも少なくない 1。

Sora 2の物語生成能力は、意図的に設計されたものではなく、より低レベルな技術的課題、すなわち「時空間にわたる長距離依存性の解決」という課題を克服した副産物である。一貫した物語とは、一貫したキャラクター、オブジェクト、環境が、もっともらしい物理法則に従って時間とともに展開されることを要求する。これらはすべて、長距離依存性の問題に帰着する。DiTアーキテクチャと時空間パッチは、まさにこの問題を解決するために設計されている 2。この低レベルな一貫性の維持に習熟することで、モデルの出力は、我々が高レベルな物語構造として認識する特性を示し始める。つまり、OpenAIは「物語AI」を構築しているのではなく、「一貫性AI」（すなわちワールドシミュレーター）を構築しており、その結果として首尾一貫した物語が生まれているのである。

## **第4章：学習方法論とプロンプト解釈**

Sora 2の驚異的な能力は、そのアーキテクチャだけでなく、モデルを訓練し、導くための洗練された方法論によっても支えられている。膨大なデータセットから、ユーザーの簡潔な指示を忠実に反映した複雑なビデオを生成するまでには、いくつかの重要な工夫が存在する。

### **4.1 燃料：インターネット規模のデータとその論争**

Sora 2のような汎用モデルの学習には、対応するテキストキャプションが付随した膨大な量のビデオデータが不可欠である 2。OpenAIは具体的なデータソースを公表していないが、その多くはインターネットから収集されたものと広く推測されている 22。

このアプローチは、著作権や倫理に関する重大な懸念を引き起こしている。アーティストやクリエイターは、自身の作品が同意なく学習データとして使用されたと考えている 22。権利者が明示的にオプトアウトしない限り著作物を使用するというOpenAIの方針は、大きな論争の的となっている 23。また、ChatGPTなどの同社製品から得られるユーザーデータも、オプトアウトしない限りモデルの学習に使用される可能性がある 24。

### **4.2 「リキャプショニング」技術：単純なプロンプトから詳細なスクリプトへ**

ユーザーのプロンプトに対する忠実度を高めるための重要な革新が、DALL-E 3から継承された「リキャプショニング」技術である 7。

このプロセスでは、ビデオが生成される前に、GPTのような強力な言語モデルがユーザーの短く単純なプロンプトを受け取り、それを自動的に非常に詳細で記述的なキャプションに拡張する 13。これは、専門家レベルのプロンプトエンジニアリングを自動で行うようなものであり、最終的に生成されるビデオが豊かなディテールを持ち、ユーザーの意図をより忠実に反映することを保証する 3。

### **4.3 合成データ仮説：Unreal Engine 5による学習**

Sora 2の学習データには、Unreal Engine 5のようなゲームエンジンで生成された合成データが少なくとも部分的に含まれているという説得力のある仮説が存在する 20。

この戦略には明確な技術的利点がある。合成データは、現実のビデオからは得ることが不可能な、完璧なグラウンドトゥルース（正解）情報を提供する。これには、深度マップ、オブジェクトのセグメンテーション、モーションベクトル、正確な物理データなどが含まれる 26。このようなデータでモデルを学習させることで、3D空間の一貫性や物理的な相互作用の学習を劇的に加速させることができる 21。このアプローチは、Sora 2が示す高度な物理理解やカメラワークを説明する一助となり、既存の物理エンジンを利用してデータ駆動型の物理エンジンをブートストラップするという、非常に効率的な学習方法と言える 20。

OpenAIは、自社の先進的なモデル（リキャプショニングのためのGPT）を用いて、次世代モデル（Sora）の学習データをブートストラップし、強化するというデータ処理の好循環（フライホイール）を構築している。これは競合他社が容易に模倣できない複合的な優位性を生み出す。ビデオ生成モデルの学習における主要なボトルネックの一つは、高品質で詳細なテキストとビデオのペアの不足である 7。OpenAIは、この問題を解決するために、自社の言語モデルを用いて学習データ用の詳細なキャプションを生成する手法を確立した 7。この内部的な相乗効果は、単純なウェブスクレイピングをはるかに超えた、洗練された多層的なデータ戦略の存在を示唆している。

## **第5章：AIビデオ生成市場の比較分析**

Sora 2の技術的進歩を正しく評価するためには、急速に進化するAIビデオ生成市場における競合との比較が不可欠である。各モデルは異なる哲学と強みを持ち、市場は単一の勝者を決めるのではなく、多様なニーズに応える形で棲み分けが進んでいる。

### **5.1 主要プレイヤー：Sora 2、Veo 3、Runway Gen-3**

現在の市場における主要な競合は、OpenAIのSora 2、GoogleのVeo 3、そしてRunwayのGen-3である。Sora 2は、本稿で詳述したように、物理的リアリズムと物語性において業界をリードする存在として位置づけられている 27。GoogleのVeo 3は、その最も強力なライバルであり、特に「ドリーズーム」といった具体的な指示による映画的なカメラ制御と、YouTube ShortsやVertex AIといった広範なGoogleエコシステムとの深い統合に強みを持つ 27。一方、Runwayはこの分野のパイオニアであり、クリエイターがモーションブラシなどのツールを用いてきめ細かな制御を行い、迅速なイテレーションを実現することに重点を置いている 27。

### **5.2 主要ビデオ生成モデルの比較機能分析**

以下の表は、各モデルの技術的特徴と強みをまとめたものである。

| 特徴 | OpenAI Sora 2 | Google Veo 3 | Runway Gen-3 |
| :---- | :---- | :---- | :---- |
| **コアアーキテクチャ** | Diffusion Transformer (DiT) 2 | 推定：Transformerベース、Googleの深層学習技術を活用 27 | 拡散モデルベース、制御可能なモジュールに重点 28 |
| **主要な強み** | 物理的リアリズムと物語の一貫性 19 | 映画的なカメラ制御とエコシステム統合 27 | きめ細かなモーション制御と迅速なイテレーション 27 |
| **ネイティブ音声生成** | あり（同期された対話＆効果音） 19 | あり（ネイティブ音声生成） 27 | なし 27 |
| **カメラ制御** | プロンプトから創発、マルチショットの一貫性が向上 27 | プロンプトの意味論による明示的な制御（例：「タイムラプス」「ドリーズーム」） 27 | ツールによる明示的な制御（例：モーションブラシ、ディレクターモード） 27 |
| **解像度** | 最大1080p 7 | 最大4K 32 | 720p、4Kへのアップスケール可能 32 |
| **主なユースケース** | 短編の映画的ストーリーテリング、世界シミュレーション 28 | クリエイティブ/マーケティング用の高品質クリップ、API利用 28 | SNSコンテンツ、VFX、迅速なプロトタイピング 27 |

この比較から明らかになるのは、市場が単一の「最高の」モデルを求める競争ではなく、異なるユーザーセグメントと製品哲学に向けた戦略的な分岐を示していることである。OpenAIは、クリエイティブなビデオ制作を主要な応用分野としつつ、基盤となるワールドモデルを構築するという「シミュレーション」アプローチを追求している 19。Googleは、既存のクリエイターエコシステムを強化するためのハイエンドな制作ツールとして「映画的ツール」アプローチをとっている 27。そしてRunwayは、特定のエフェクトに対して精密な制御を必要とするアーティストやデザイナーに応える「クリエイティブスイート」として自らを位置づけている 28。これらは単なる機能セットの違いではなく、根本的に異なる製品哲学の現れであり、市場はユーザーがシミュレーターを求めるのか、カメラを求めるのか、あるいは絵筆を求めるのかによってセグメント化されていくことを示唆している。

## **結論：基盤技術としての生成ビデオの未来**

本稿の分析を通じて、OpenAIのSora 2がビデオ生成技術における画期的な進歩であることが明らかになった。その核心には、スケーラブルなDiffusion Transformerアーキテクチャ、柔軟な時空間パッチによるデータ表現、そして自己のAIモデルを活用して学習データを強化するという洗練されたデータ戦略がある。これらの技術的革新の組み合わせが、物理法則を理解し、一貫した物語を紡ぎ出すという創発的な能力を生み出している。

さらに、Soraソーシャルアプリのローンチは 30、OpenAIの戦略が単なるツール提供者から、コンテンツの制作から消費までを包含するプラットフォーム所有者へと移行していることを示している。これはTikTokのような既存のプラットフォームと直接競合するハイリスク・ハイリターンな戦略であり、サム・アルトマンはこれをAGI（汎用人工知能）達成という最終目標のための資金調達に必要な手段として正当化している 36。

しかし、その未来には依然として大きな課題が残されている。物理的に不自然な挙動の克服 2、偽情報や悪用を防ぐための堅牢な安全対策の確保 39、そして学習データと著作権を巡る深刻な倫理的問題の解決 22 は、この技術が社会に広く受け入れられるための必須条件である。

Sora 2は、AIが現実世界を理解し、シミュレートする「汎用ワールドシミュレーター」への道を切り拓いた。この技術が成熟するにつれて、エンターテインメントや教育、科学研究といった分野に計り知れない変革をもたらすポテンシャルを秘めている。その進展は、技術的な挑戦であると同時に、社会的な対話と責任ある実装が求められる、人類にとっての新たなフロンティアである。

#### **引用文献**

1. Sora: Creating video from text \- OpenAI, 10月 3, 2025にアクセス、 [https://openai.com/index/sora/](https://openai.com/index/sora/)  
2. Video generation models as world simulators OpenAI, 10月 3, 2025にアクセス、 [https://openai.com/index/video-generation-models-as-world-simulators/](https://openai.com/index/video-generation-models-as-world-simulators/)  
3. Inside OpenAI Sora: Five Key Technical Details We Learned About ..., 10月 3, 2025にアクセス、 [https://pub.towardsai.net/inside-openai-sora-five-key-technical-details-we-learned-about-the-amazing-video-generation-model-98e510f9b744](https://pub.towardsai.net/inside-openai-sora-five-key-technical-details-we-learned-about-the-amazing-video-generation-model-98e510f9b744)  
4. What is OpenAI's Sora Diffusion Transformer (DiT)? \- Analytics Vidhya, 10月 3, 2025にアクセス、 [https://www.analyticsvidhya.com/blog/2024/05/what-is-openais-sora-diffusion-transformer-dit/](https://www.analyticsvidhya.com/blog/2024/05/what-is-openais-sora-diffusion-transformer-dit/)  
5. Diffusion Transformer: Architecture behind Sora State-of-the-Art Video Generation \- Medium, 10月 3, 2025にアクセス、 [https://medium.com/@humzanaveed/diffusion-transformer-architecture-behind-sora-state-of-the-art-video-generation-cb9f2eee69ec](https://medium.com/@humzanaveed/diffusion-transformer-architecture-behind-sora-state-of-the-art-video-generation-cb9f2eee69ec)  
6. How does Sora work? (An Intuitive explanation) by Bhavya Barri \- Medium, 10月 3, 2025にアクセス、 [https://bhavyabarri.medium.com/how-does-sora-work-an-intuitive-explanation-7e17d3c3691b](https://bhavyabarri.medium.com/how-does-sora-work-an-intuitive-explanation-7e17d3c3691b)  
7. Sora: OpenAI's Video Model Architecture and Use Cases \- ALLPCB, 10月 3, 2025にアクセス、 [https://www.allpcb.com/allelectrohub/sora-openais-video-model-architecture-and-use-cases](https://www.allpcb.com/allelectrohub/sora-openais-video-model-architecture-and-use-cases)  
8. OpenAI Sora's Technical Review \- Jianing Qi, 10月 3, 2025にアクセス、 [https://j-qi.medium.com/openai-soras-technical-review-a8f85b44cb7f](https://j-qi.medium.com/openai-soras-technical-review-a8f85b44cb7f)  
9. Sora: A Review on Background, Technology, Limitations, and Opportunities of Large Vision Models \- arXiv, 10月 3, 2025にアクセス、 [https://arxiv.org/html/2402.17177v1](https://arxiv.org/html/2402.17177v1)  
10. \[2507.13343\] Taming Diffusion Transformer for Real-Time Mobile Video Generation \- arXiv, 10月 3, 2025にアクセス、 [https://arxiv.org/abs/2507.13343](https://arxiv.org/abs/2507.13343)  
11. Diffusion models for video generation \- Blog \- Marvik, 10月 3, 2025にアクセス、 [https://blog.marvik.ai/2024/01/30/diffusion-models-for-video-generation/](https://blog.marvik.ai/2024/01/30/diffusion-models-for-video-generation/)  
12. Open-Sora 2.0 Explained: Architecture, Training, and Why It Matters, 10月 3, 2025にアクセス、 [https://www.louisbouchard.ai/open-sora-2/](https://www.louisbouchard.ai/open-sora-2/)  
13. What Is OpenAI's Sora? How It Works, Examples, Features ..., 10月 3, 2025にアクセス、 [https://www.datacamp.com/blog/openai-announces-sora-text-to-video-generative-ai-is-about-to-go-mainstream](https://www.datacamp.com/blog/openai-announces-sora-text-to-video-generative-ai-is-about-to-go-mainstream)  
14. Spacetime Patches \- Vocab \- Envisioning.io, 10月 3, 2025にアクセス、 [https://www.envisioning.io/vocab/spacetime-patches](https://www.envisioning.io/vocab/spacetime-patches)  
15. Sam Altman's Blog, 10月 3, 2025にアクセス、 [https://blog.samaltman.com/](https://blog.samaltman.com/)  
16. How to Design Consistent AI Characters with Prompts, Diffusion & Reference Control (2025), 10月 3, 2025にアクセス、 [https://medium.com/design-bootcamp/how-to-design-consistent-ai-characters-with-prompts-diffusion-reference-control-2025-a1bf1757655d](https://medium.com/design-bootcamp/how-to-design-consistent-ai-characters-with-prompts-diffusion-reference-control-2025-a1bf1757655d)  
17. Best text-to-video models for character \+ scene consistency? : r/generativeAI \- Reddit, 10月 3, 2025にアクセス、 [https://www.reddit.com/r/generativeAI/comments/1lfzzz3/best\_texttovideo\_models\_for\_character\_scene/](https://www.reddit.com/r/generativeAI/comments/1lfzzz3/best_texttovideo_models_for_character_scene/)  
18. How to Create Consistent Characters with AI \- YouTube, 10月 3, 2025にアクセス、 [https://www.youtube.com/watch?v=K4cW77-\_Q7I](https://www.youtube.com/watch?v=K4cW77-_Q7I)  
19. How is OpenAI's Sora 2 Model Redefining Generative Video AI? Technology Magazine, 10月 3, 2025にアクセス、 [https://technologymagazine.com/news/openais-sora-2-redefining-safe-physics-driven-video-ai](https://technologymagazine.com/news/openais-sora-2-redefining-safe-physics-driven-video-ai)  
20. Many might miss the key paragraph at the end: "Sora serves as a ..., 10月 3, 2025にアクセス、 [https://news.ycombinator.com/item?id=39387789](https://news.ycombinator.com/item?id=39387789)  
21. \#155 Sora: Data-Driven Physics Engine \- Roost.ai, 10月 3, 2025にアクセス、 [https://roost.ai/blog/155-sora-data-driven-physics-engine](https://roost.ai/blog/155-sora-data-driven-physics-engine)  
22. What was Sora trained on? Creatives demand answers. \- Mashable, 10月 3, 2025にアクセス、 [https://mashable.com/article/openai-sora-ai-video-generator-training-data](https://mashable.com/article/openai-sora-ai-video-generator-training-data)  
23. OpenAI takes on TikTok, YouTube Shorts with Sora 2 video app; copyright a potential issue, 10月 3, 2025にアクセス、 [https://m.economictimes.com/tech/artificial-intelligence/openai-takes-on-tiktok-youtube-shorts-with-sora-2-video-app-copyright-a-potential-issue/articleshow/124248340.cms](https://m.economictimes.com/tech/artificial-intelligence/openai-takes-on-tiktok-youtube-shorts-with-sora-2-video-app-copyright-a-potential-issue/articleshow/124248340.cms)  
24. How your data is used to improve model performance OpenAI Help Center, 10月 3, 2025にアクセス、 [https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance](https://help.openai.com/en/articles/5722486-how-your-data-is-used-to-improve-model-performance)  
25. The real progress with Sora is the ability to train on video, not to create video clips\! \- Reddit, 10月 3, 2025にアクセス、 [https://www.reddit.com/r/ChatGPT/comments/1atbzh6/the\_real\_progress\_with\_sora\_is\_the\_ability\_to/](https://www.reddit.com/r/ChatGPT/comments/1atbzh6/the_real_progress_with_sora_is_the_ability_to/)  
26. Explanation of OpenAI's Sora by Jim Fan, NVIDIA's Senior Research Scientist & Lead of AI Agents. Hopefully Meta, Mistral and Stability are cooking up an open source alternative. \- Reddit, 10月 3, 2025にアクセス、 [https://www.reddit.com/r/LocalLLaMA/comments/1aspxox/explanation\_of\_openais\_sora\_by\_jim\_fan\_nvidias/](https://www.reddit.com/r/LocalLLaMA/comments/1aspxox/explanation_of_openais_sora_by_jim_fan_nvidias/)  
27. Sora 2 vs Veo 3 vs Runway Gen‑3: 2025 AI Video Model ..., 10月 3, 2025にアクセス、 [https://skywork.ai/blog/sora-2-vs-veo-3-vs-runway-gen-3-2025-ai-video-generator-comparison/](https://skywork.ai/blog/sora-2-vs-veo-3-vs-runway-gen-3-2025-ai-video-generator-comparison/)  
28. MLA 026 AI Video Generation: Veo 3 vs Sora, Kling, Runway, Stable Video Diffusion, 10月 3, 2025にアクセス、 [https://ocdevel.com/mlg/mla-26](https://ocdevel.com/mlg/mla-26)  
29. Comparing the Best AI Video Generation Models: Sora, VEO3, Runway & More, 10月 3, 2025にアクセス、 [https://stockimg.ai/blog/ai-and-technology/comparing-the-best-ai-video-generation-models-sora-veo3-runway-and-more](https://stockimg.ai/blog/ai-and-technology/comparing-the-best-ai-video-generation-models-sora-veo3-runway-and-more)  
30. OpenAI Launches Sora 2 Social App, Redefining AI-Powered Video Creation \- Hypebeast, 10月 3, 2025にアクセス、 [https://hypebeast.com/2025/10/openai-sora-2-social-app-ai-powered-video-creation-launch](https://hypebeast.com/2025/10/openai-sora-2-social-app-ai-powered-video-creation-launch)  
31. OpenAI Sora app lets you be the hero of AI-generated films: 5 stunning features that will blow your mind, 10月 3, 2025にアクセス、 [https://m.economictimes.com/news/new-updates/openai-sora-app-lets-you-be-the-hero-of-ai-generated-films-5-stunning-features-that-will-blow-your-mind/articleshow/124247361.cms](https://m.economictimes.com/news/new-updates/openai-sora-app-lets-you-be-the-hero-of-ai-generated-films-5-stunning-features-that-will-blow-your-mind/articleshow/124247361.cms)  
32. Veo 3 vs Top AI Video Generators: Sora, Runway, Kling, Seedance, and More Compared, 10月 3, 2025にアクセス、 [https://www.imagine.art/blogs/veo-3-vs-top-ai-video-generators](https://www.imagine.art/blogs/veo-3-vs-top-ai-video-generators)  
33. OpenAI to take on TikTok with its new short-video app Sora, 10月 3, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-news/openai-to-take-on-tiktok-with-its-new-short-video-app-sora/articleshow/124256886.cms](https://timesofindia.indiatimes.com/technology/tech-news/openai-to-take-on-tiktok-with-its-new-short-video-app-sora/articleshow/124256886.cms)  
34. OpenAI’s Sora 2 takes over social media with life-like AI avatars; here's how to make your own ‘cameos’, 10月 3, 2025にアクセス、 [https://indianexpress.com/article/trending/trending-globally/openai-sora-2-how-to-make-your-own-lifelike-ai-cameos-10282168/](https://indianexpress.com/article/trending/trending-globally/openai-sora-2-how-to-make-your-own-lifelike-ai-cameos-10282168/)  
35. OpenAI launches Sora App alongside Sora 2 for improved audio, video generation AI platform, 10月 3, 2025にアクセス、 [https://indianexpress.com/article/technology/artificial-intelligence/openai-launches-sora-app-for-improved-audio-video-generation-ai-platform-10282366/](https://indianexpress.com/article/technology/artificial-intelligence/openai-launches-sora-app-for-improved-audio-video-generation-ai-platform-10282366/)  
36. OpenAI CEO Sam Altman defends the launch of AI video app Sora: ‘I get the vibe here, but…’, 10月 3, 2025にアクセス、 [https://timesofindia.indiatimes.com/technology/tech-news/openai-ceo-sam-altman-defends-the-launch-of-ai-video-app-sora-i-get-the-vibe-here-but/articleshow/124263456.cms](https://timesofindia.indiatimes.com/technology/tech-news/openai-ceo-sam-altman-defends-the-launch-of-ai-video-app-sora-i-get-the-vibe-here-but/articleshow/124263456.cms)  
37. OpenAI launches Sora App: Check features and how to create videos, 10月 3, 2025にアクセス、 [https://m.economictimes.com/tech/artificial-intelligence/openai-launches-sora-app-check-features-and-how-to-create-videos/articleshow/124251552.cms](https://m.economictimes.com/tech/artificial-intelligence/openai-launches-sora-app-check-features-and-how-to-create-videos/articleshow/124251552.cms)  
38. Sam Altman defends OpenAI's Sora rollout: From ‘cure for cancer’ to AI slop videos, 10月 3, 2025にアクセス、 [https://m.economictimes.com/tech/artificial-intelligence/sam-altman-defends-sora-rollout-from-cure-for-cancer-to-ai-slop-videos/articleshow/124270948.cms](https://m.economictimes.com/tech/artificial-intelligence/sam-altman-defends-sora-rollout-from-cure-for-cancer-to-ai-slop-videos/articleshow/124270948.cms)  
39. Everything is fake on Silicon Valley's hottest new social network, 10月 3, 2025にアクセス、 [https://www.washingtonpost.com/technology/2025/10/02/sora-openai-video-face-fake/](https://www.washingtonpost.com/technology/2025/10/02/sora-openai-video-face-fake/)  
40. Launching Sora responsibly OpenAI, 10月 3, 2025にアクセス、 [https://openai.com/index/launching-sora-responsibly/](https://openai.com/index/launching-sora-responsibly/)  
41. The Sora feed philosophy OpenAI, 10月 3, 2025にアクセス、 [https://openai.com/index/sora-feed-philosophy/](https://openai.com/index/sora-feed-philosophy/)
