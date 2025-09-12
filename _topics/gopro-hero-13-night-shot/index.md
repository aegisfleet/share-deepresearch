---
audio: /share-deepresearch/assets/audio/gopro-hero-13-night-shot.mp3
category: research
date: 2025-07-15
description: GoPro HERO 13を夜間撮影で使う際の最適なセッティングを調べ、手持ちで歩きながら撮影するためのガイド。
ga4_metrics:
  avgSessionDuration: 2.6683956666666666
  pageViews: 3
  users: 2
layout: topic
prompt: GoPro HERO 13を夜間撮影で使う際の最適なセッティングを調べて欲しい。手持ちで歩きながら撮影する想定となる。
supplementary_materials:
- title: GoPro夜間撮影ガイド インフォグラフィック
  url: /share-deepresearch/topics/gopro-hero-13-night-shot/infographic.html
- title: GoPro HERO 13/12 夜間手持ち撮影 完全攻略ガイド
  url: /share-deepresearch/topics/gopro-hero-13-night-shot/reveal.html
tags:
- ガジェット
title: GoPro HERO12/13 完全ガイド：手持ち夜間歩行撮影の最適化
---

# **GoPro HERO12/13 完全ガイド：手持ち夜間歩行撮影の最適化**

## **はじめに**

### **核心的課題：光と安定性の物理的制約**

アクションカメラを用いた夜間撮影、特に手持ちでの歩行撮影は、ビデオグラフィーにおける最も困難なシナリオの一つです。この課題の核心には、根本的に相反する二つの物理的要件が存在します。すなわち、暗いシーンから十分な光を集めるための「低速シャッター」と、歩行による動きを滑らかに補正するための「高速シャッター」です。このレポートの目的は、単一の「魔法の設定」を提示することではありません。むしろ、光学的・物理的な制約を深く理解し、撮影者の技術レベル、ポストプロダクションへの意欲、そして求める最終的な映像表現に応じて、一連の重要なトレードオフを習熟し、情報に基づいた意思決定を下すための戦略的ガイドを提供することにあります。

### **GoPro HERO13に関する前提条件**

本稿は、ユーザーのクエリにあるGoPro HERO13を対象としていますが、執筆時点では同モデルは未発表です。したがって、このガイドは、その直接の前世代機であるGoPro HERO12 Blackの広範な実世界のデータと既知の性能特性に基づいて構築されています 1。ここで論じられるセンサー物理学、光学、そして安定化アルゴリズムの基本原理は、アクションカメラの技術的基盤をなすものであり、次世代機であるHERO13にもほぼ間違いなく適用されるものと想定されます。

### **本レポートの目的**

本レポートは、多層的な戦略ガイドとして構成されています。まず、カメラ内で完結するシンプルかつ効果的な設定から始め、次にGoPro Labsファームウェアを用いた高度な制御、外部ハードウェア（ジンバルやライト）による物理的な解決策、そして最後にプロフェッショナルなポストプロダクションワークフローへと段階的に進んでいきます。これにより、撮影者は自身の特定の撮影条件、技術的スキル、そして望む最終的なルックに応じて、最適なアプローチを選択できるようになることを目指します。

## **セクション1：根本的な制約：なぜ夜間歩行はGoProの「最悪の環境」なのか**

アクションカメラ、特にGoProが夜間の手持ち歩行撮影で苦戦する理由は、単に「暗いから」という単純なものではありません。その背後には、カメラの設計思想に根差した、回避不可能な物理的制約の連鎖が存在します。この「問題の物理学」を理解することは、後述する高度な設定やワークフローの論理的根拠を把握する上で不可欠です。核心となる因果連鎖は、「固定絞り」が「低速シャッター」への依存を強い、それが「モーションブラー」を生み出し、このモーションブラーが最終的にジャイロベースの「HyperSmooth手ブレ補正」を破綻させ、「ジッター（微振動）」を引き起こすというものです 6。

### **1.1. 三脚の一本が欠けた露出の三角形：固定絞り**

全ての写真・映像技術の基礎には、「露出の三角形」、すなわち絞り（Aperture）、シャッタースピード（Shutter Speed）、ISO感度の三要素の関係性があります。しかし、GoProのレンズはF2.8の固定絞りを採用しており 9、これは露出制御の重要な変数の一つが欠けていることを意味します。この設計上の選択は、すべての露出補正をシャッタースピードとISO感度という残りの二つの柱に依存させることになります。この制約は、しばしば可変絞りや高度なコンピュテーショナルフォトグラフィ技術を搭載し、特定の低照度環境下でアクションカメラを凌駕する性能を発揮することがある最新のスマートフォンと比較する際に、特に顕著になります 10。

### **1.2. 小センサーのアキレス腱：不可避なデジタルノイズ**

センサーサイズとノイズ性能の間には直接的な関係があります。GoProのコンパクトで堅牢なフォームファクターを実現するために不可欠な小型センサーは、ミラーレスカメラやデジタル一眼レフカメラに搭載されている大型センサーと比較して、本質的にデジタルノイズ（映像のザラつき）が発生しやすいという弱点を抱えています 2。

HERO12のビデオ撮影時のISO感度範囲は100から6400ですが 12、専門家やユーザーコミュニティの見解を総合すると、ISO 800または1600を超えると画質は著しく低下し、映像は不快なほどノイジーで「斑点状（splotchy）」かつ「泥のよう（muddy）」になると報告されています 14。これはISO感度の実用的な上限を設定するものであり、ISOを上げることはあくまで「最後の手段」であるべきことを示唆しています 9。

### **1.3. 核心的対立：モーションブラー vs. HyperSmooth手ブレ補正**

この問題こそが、夜間歩行撮影における最大の技術的難関です。HyperSmoothは、カメラのジャイロスコープで動きを検出し、その動きを相殺するように映像フレームをデジタル的にシフトさせる電子式手ブレ補正（EIS）の一種です。このプロセスが正常に機能するためには、分析・整列させるための一連のクリーンでシャープなフレームが必要不可欠です 7。

しかし、夜間歩行時には破滅的な因果連鎖が発生します。

1. 低照度環境下で、カメラの自動露出システムは十分な光を取り込むためにシャッタースピードを遅くします（例：30fps撮影時に1/30秒）1。  
2. この遅いシャッターが開いている間にユーザーが歩行することで、個々のビデオフレームに「モーションブラー（被写体ブレ）」が記録されます 8。  
3. HyperSmoothのアルゴリズムは、この既にブレてしまったフレームを安定させようと試みます。しかし、追跡すべき明確でシャープなアンカーポイントを見つけられないため、補正に失敗し、広く報告されている「ジッター（微振動）」、「ゴースト」、「ワーピング（歪み）」といったアーティファクトを生成してしまうのです 6。

この技術的な説明は、多くのユーザーがこの状況を「GoProにとって最悪の環境」と評する理由を裏付けており 22、激しいモーションブラーのかかった映像を安定化させようとすると、元の揺れた映像よりも見栄えが悪くなることさえあるという事実を浮き彫りにします 22。

## **セクション2：ProTuneの習熟：第一の防衛線**

理論から実践へと移行し、夜間撮影の核心的課題に正面から取り組みます。ここでは、単一の「最適設定」ではなく、求める成果とポストプロダクションへのコミットメントに基づいた、二つの異なるワークフローベースの戦略を提示します。これは、特にカラープロファイルの選択において顕著であり、ノイズをカメラ内で処理するのか、それともポストプロダクションで処理するのかという戦略的な判断を迫るものです。

### **2.1. 基本設定：解像度、アスペクト比、フレームレート**

* **解像度:** **5.3K**または**4K**での撮影を推奨します。5.3Kで撮影する主な利点は、最終的に4Kで書き出す場合でも、より優れたディテールが保持される点にあります 23。  
* **アスペクト比:** ここでは戦略的な選択が求められます。**8:7**はセンサーから最も多くの情報を取得でき、ポストプロダクションで水平（16:9）と垂直（9:16）の両方のフォーマットにリフレームする際の柔軟性が最大になります。しかし、**16:9**は手ブレ補正アルゴリズムが利用できる視野を広げ、結果としてHyperSmoothの性能が大幅に向上します 23。手持ち歩行撮影においては、安定性を優先するなら16:9が優れた選択となることが多いです。  
* **フレームレート:** **24fps**または**30fps**を強く推奨します 1。これは低照度撮影における極めて重要な決定です。低いフレームレートは、より遅いシャッタースピード（例：1/60秒に対して最大1/24秒）を可能にし、各フレームでセンサーにより多くの光を取り込むことができます 9。

### **2.2. 最重要変数：シャッタースピードとISO**

* **シャッタースピード:** 基本的な推奨設定は\*\*Auto（自動）\*\*です。映像に自然なモーションブラーを生み出すための「180度ルール」（シャッタースピード \= 1 / (2 × フレームレート)）は広く知られていますが 1、この特定のユースケースでは、このルールに固執するよりもモーションブラーを最小限に抑えることが重要です。ここでのトレードオフは明確です。遅いシャッター（例：1/48秒）はより多くの光を取り込めますが、モーションブラーが増加し、手ブレ補正が破綻するリスクが高まります。一方、速いシャッターは映像を暗くしますが、HyperSmoothが機能するためのクリーンな基盤を提供します 21。  
* **ISO:** ノイズを制御するために手動で範囲を設定することを推奨します。**ISO Min: 100**は、最もクリーンな画像を得るための普遍的な出発点です 1。  
  **ISO Max: 800**または**1600**が推奨される上限値です 10。この範囲設定は、変化する光条件に対応するための柔軟性をカメラに与えつつ、過度にノイジーな高感度域への移行を防ぎます。

### **2.3. 映像の微調整**

* **EV補正:** **\-0.5**の設定を推奨します 23。これにより映像がわずかにアンダー露出になり、街灯やネオンサイン、店舗の照明など、白飛びしやすい明るいハイライト部分のディテールを保持する上で非常に重要です。  
* **シャープネス:** \*\*Low（低）\*\*設定を強く推奨します 23。カメラ内でのシャープネス処理は、低照度下で見苦しいアーティファクトを生み出す可能性のある不可逆的なプロセスです。よりクリーンで制御された結果を得るためには、ポストプロダクションの最終段階でシャープネスを適用する方が常に望ましいです 26。  
* **ホワイトバランス:** **Auto（自動）と固定ケルビン値の長所と短所を考慮します。Autoは便利ですが、異なる種類（例：ナトリウムランプ、LED、蛍光灯）の街灯の下を歩くと、色の変動が気 distracting になることがあります。ホワイトバランスを4000K**のような値に固定すると 18、クリップ全体で色の一貫性が保たれ、ポストプロダクションでの全体的な色補正が容易になります。

### **2.4. ワークフローを決定づける選択：カラープロファイル**

* **最小限のポストプロダクション向け（現実主義者のプリセット）:** \*\*Natural（ナチュラル）**または**Vibrant（鮮やか）\*\*カラープロファイルの使用を推奨します 17。これは直感に反するかもしれませんが、専門家でないユーザーにとっては重要な推奨事項です。これらのプロファイルはカメラ内でコントラストと彩度を適用し、画像の最も暗い部分を効果的に黒に「潰す」ことで、シャドウ部に潜むセンサー固有のノイズを隠します 9。これにより、シャドウディテールの一部を犠牲にする代わりに、よりクリーンですぐに使える映像が得られます。  
* **最大限のポストプロダクション柔軟性向け（映像作家のプリセット）:** **Flat（フラット）またはGP-Log**の使用について解説します 1。ただし、これは低照度下ではハイリスク・ハイリターンな戦略であることを強く警告しなければなりません。これらのプロファイルは最大限のダイナミックレンジを保持しますが、同時にセンサーが出力するノイズもすべて露呈させます。ユーザーからは、低照度のLog映像はカラーグレーディング中にシャドウ部を持ち上げるとノイズも増幅され、使用不可能なレベルにまで「崩壊する」ことがあると報告されています 17。さらに、GoProの公式ドキュメントでは、GP-Logは暗い環境での使用を推奨しておらず、ISO感度も低い範囲に制限されるため 33、専門家レベルのポストプロダクションノイズリダクション技術なしには、この特定の課題には根本的に不向きです。

**表1：手持ち夜間歩行撮影のための推奨ProTune設定**

| 設定項目 | 現実主義者のプリセット（手軽でクリーン） | 映像作家のプリセット（最大データと制御） |
| :---- | :---- | :---- |
| **解像度** | 4K | 5.3K |
| **フレームレート(FPS)** | 30 | 24 |
| **アスペクト比** | 16:9 | 8:7 (リフレーム用) または 16:9 (安定性優先) |
| **HyperSmooth** | On | On (またはGyroflow使用時はOff) |
| **シャッター** | Auto | Auto |
| **EV補正** | \-0.5 | \-0.5 |
| **ホワイトバランス** | Auto または 4000K | 4000K または Native |
| **ISO Min** | 100 | 100 |
| **ISO Max** | 800 | 1600 |
| **シャープネス** | Low | Low |
| **カラー** | Natural | Flat または GP-Log (注意が必要) |
| **ビットレート** | High | High |
| **ビット深度** | 10-Bit | 10-Bit |

## **セクション3：ProTuneを超えて：高度な安定化とハードウェア**

このセクションでは、単にトレードオフを管理するのではなく、問題の根本を積極的に排除する解決策を紹介します。これにより、本レポートは単なる設定ガイドから戦略的なマニュアルへと昇華します。まず、ユーザーが意図的に明るさを犠牲にして安定性を優先するという、事前の計算されたトレードオフを可能にする強力なソフトウェア「ハック」としてGoPro Labsを紹介します。次に、問題の物理法則を真に克服する唯一の方法である、物理的な安定化と外部照明という「絶対的な解決策」を提示します。

### **3.1. HyperSmoothの限界：ジッターの深層**

まず、セクション1で解説したジッターの原因（モーションブラーとEISの相互作用）を再確認します。ユーザーからのフィードバックによると、「AutoBoost」モードは、その動的なクロッピングがジッター効果を悪化させる可能性があるため、低照度下では好まれない傾向があります 6。標準の「On」設定が一般的に好まれますが、依然としてモーションブラーに対して脆弱です。ここでの重要な結論は、どれほど高度なカメラ内手ブレ補正モードであっても、ブレたソースフレームからシャープな画像を再構築することはできないということです 6。問題は撮影時点で解決されなければなりません。

### **3.2. GoPro Labsの力：カメラを強制的に制御する**

GoPro Labsファームウェアは、QRコードを介してより深いレベルの制御を可能にする、GoPro公式の無料アップグレードです 26。

* **シャッタースピードの修正:** これが最も重要なソフトウェアソリューションです。\!MEXPX=コマンドを使用して、シャッタースピードの*上限*（または露出時間の*下限*）を設定する方法を解説します 8。例えば、  
  \!MEXPX=120と設定すると、シャッターは1/120秒より遅くなることがなくなります。これにより、HyperSmoothの失敗の原因となる過度なモーションブラーの発生を直接的に防ぎます 8。ユーザーは、これが完全に滑らかな手ブレ補正と引き換えに、より暗い映像を受け入れるという意図的な選択であることを理解する必要があります。1/120、1/240、1/480といった値で実験することを推奨します 8。  
* **ノイズリダクションの修正:** \!MNR01=1コマンドは、カメラ内蔵のノイズリダクションを無効にします 16。これは、最大限の画像ディテール（たとえそれがノイジーであっても）をキャプチャし、ポストプロダクションでより優れたノイズリダクションツールを使用したい上級ユーザー向けのテクニックです。

### **3.3. 究極の解決策：外部ハードウェア**

* **ジンバル:** なぜ物理的なジンバルが最も効果的な解決策であるかを説明します。カメラ本体を物理的に安定させることで、そもそもフレームにモーションブラーが記録されるのを防ぎます 1。これにより、シャッタースピードと手ブレ補正の間の依存関係が断ち切られ、ユーザーはより多くの光を取り込むために低速シャッターを使用し、  
  *かつ*完全に滑らかな映像を得ることが可能になります。  
* **外部照明:** GoPro Light Modのような外部光源の戦略的な使用について論じます 1。シーンに光を追加することは、もう一つの「絶対的な解決策」です。被写体や環境を照らすことで、カメラは自然により速いシャッタースピードを使用できるようになり、問題全体の根本原因を解決します。

**表2：夜間安定化戦略の比較**

| 戦略 | 手ブレ補正品質 | モーションブラー/アーティファクト | 映像の明るさ | 利便性/労力 | 最適なユースケース |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **標準HyperSmooth** | 中〜低 | ジッター/ブラーのリスク大 | 中 | 高 | 明るい都市部でのカジュアルな撮影 |
| **HyperSmooth \+ GoPro Labs (最大シャッター設定)** | 高 | 最小限 | 低 | 中 | 品質と利便性のバランスを求めるプロシューマー |
| **Gyroflow (ポスト補正)** | 非常に高い | 最小限（設定次第） | 中〜高 | 低 | 最高の制御性を求める映像制作者 |
| **物理ジンバル** | 最高 | ほぼゼロ | 高 | 非常に低い | 品質に一切妥協しないプロフェッショナルな撮影 |

## **セクション4：デジタル暗室：プロフェッショナルなポストプロダクションワークフロー**

このセクションは、可能な限り最高の品質を目指すユーザー向けに設計されており、GoProの自動化されたプロセスを「アンバンドル（分解）」するアプローチを示します。ここでは、撮影から最終的な書き出しまでの一貫したパイプラインを提供し、GoProをより強力なポストプロダクション環境のためのデータ取得ツールとして扱います。HyperSmoothのプロフェッショナルな代替手段としてGyroflowのワークフローを詳述し、挑戦的な低照度Log映像に対して、単純なLUT（ルックアップテーブル）よりも優れたカラースペース変換（CST）を用いた技術的に正しいカラーグレーディングワークフローを提供します。

### **4.1. Gyroflowによるポスト安定化：究極の制御**

まず、Gyroflowに不可欠なクリーンなジャイロスコープデータをカメラが記録するために、HyperSmoothを**OFF**にして撮影するという核となるコンセプトを説明します 22。

無料のGyroflowソフトウェアを使用したステップバイステップガイドは以下の通りです 36：

1. ソフトウェアをダウンロードし、インストールします。  
2. GoProのビデオファイルをインポートします。Gyroflowはカメラ、レンズプロファイル、埋め込まれたジャイロデータを自動的に検出します 36。  
3. 主要なパラメータを調整します：「Smoothness（滑らかさ）」（適用する手ブレ補正の強さ）と「FOV」（クロップ量を制御するため）。  
4. 結果をリアルタイムでプレビューし、安定化されたクリップを書き出します。

このワークフローの利点として、手ブレ補正の「ルック」に対するより詳細な制御、より滑らかで「デジタルっぽさ」の少ない感触の実現、そしてHyperSmoothと比較して最終的により広い視野角を得られる可能性を挙げます 38。主な欠点は、ワークフローに一手間加わることです。

### **4.2. DaVinci Resolveでの低照度映像のカラーグレーディング**

* **暗闇でのLogの問題点:** まずセクション2の警告を再確認します。低照度のLog/Flat映像は非常にノイジーで脆弱です 17。このワークフローの目標は、その脆弱性を管理することです。  
* **LUTを超えて：カラースペース変換（CST）ワークフロー:**  
  1. GoProの公式LUTを単純に適用することが、なぜ本格的なグレーディングの出発点として最適ではないのかを説明します。LUTは「ブラックボックス」であり、データをクリッピングしたり、露出調整にうまく反応しなかったりする可能性があります 39。  
  2. DaVinci Resolveにおける技術的に正しくプロフェッショナルなワークフローを詳述します。最初のステップとして、\*\*カラースペース変換（CST）\*\*ノードを使用します。これにより、映像はソースのカラースペースとガンマ（例：GoPro Wide Gamut / GP-Log）から、DaVinci Wide Gamut / Intermediateのような標準化された広色域の作業空間に変換されます 39。  
  3. すべてのクリエイティブなグレーディング調整（露出、コントラスト、彩度など）は、この堅牢な作業空間内で行われます。  
  4. 最終的なCSTノードがノードツリーの最後に使用され、画像を作業空間から最終的な納品規格（例：Rec.709）に変換します。  
* **ノイズの抑制:** これは非常に重要なステップです。高品質なノイズリダクションツール（有料版のDaVinci Resolve Studioに搭載されているテンポラルノイズリダクションや、Neat Videoのようなサードパーティ製プラグイン）を、ノードツリーの早い段階、通常は最初のCSTの直後に適用することを強調します。これにより、コントラストや彩度の調整がノイズを増幅する*前*に画像をクリーンにします 34。  
* **GP-Log露出の補正:** デフォルトのGP-Logプロファイルには隠れた-2EVの補正が組み込まれており、これが映像がしばしば露出アンダーでノイジーに見える原因であるという高度な知見に触れます。上級ユーザーはGoPro Labsを使用してLOGB値を調整し、グレーディング前により良いベース露出を得ることができます 40。

## **結論：夜間歩行のための段階的推奨事項**

本レポート全体を統合し、簡潔で実行可能な要約を提供します。光、ノイズ、安定性の間の回避不可能なトレードオフを再度強調し、異なるユーザープロファイルに合わせた3つの明確な段階的推奨事項を提示します。

* Tier 1：エンスージアスト向け（最小限の労力で最高の画質を）:  
  これは、カメラから直接良好な結果を得るための「設定して撮るだけ」のアプローチです。  
  * **戦略:** セクション2の「現実主義者のプリセット」を使用します。明るい都市部を歩くことに集中します。  
  * **主要設定:** 4K30, 16:9, HyperSmooth On, EV \-0.5, ISO Max 800, シャープネス Low, カラー Natural 23。  
* Tier 2：プロシューマー向け（優れたカメラ内制御）:  
  このアプローチは、わずかな初期設定でTier 1よりも大幅に優れた結果を得るためにGoPro Labsを活用します。  
  * **戦略:** GoPro Labsファームウェアをインストールします。QRコードを使用して最大シャッタースピードを設定します（例：\!MEXPX=120）。ProTune設定で撮影し、ポストプロダクションで基本的な色補正を行います。  
  * **主な利点:** ソースでのモーションブラーを防ぐことで優れた手ブレ補正を提供し、外部ハードウェアなしで品質と利便性の最高のバランスを実現します。  
* Tier 3：完璧主義者向け（究極の品質）:  
  これは、カメラから可能な限り最高の画質を引き出すための、妥協のないワークフローです。  
  * **戦略:** **物理的なジンバル**を使用してソースでの動きを排除します 6。「映像作家のプリセット」（GP-Log、シャープネスLowなど）で撮影します。セクション4で詳述したように、すべての手ブレ補正、ノイズリダクション、カラーグレーディングをポストプロダクションで処理します。ジンバルが利用できない場合は、Gyroflowワークフロー（HyperSmooth Off）を使用します。可能な限り外部照明を追加します 10。このアプローチは、最もクリーンで、最もディテール豊かで、最も専門的に制御された結果を生み出します。

#### **引用文献**

1. Please recommend low light settings for hero 12\. : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1ctk1wg/please\_recommend\_low\_light\_settings\_for\_hero\_12/](https://www.reddit.com/r/gopro/comments/1ctk1wg/please_recommend_low_light_settings_for_hero_12/)  
2. GoPro Hero 12 Black review: edging closer to perfection TechRadar, 7月 15, 2025にアクセス、 [https://www.techradar.com/cameras/action-cameras/gopro-hero-12-black-review](https://www.techradar.com/cameras/action-cameras/gopro-hero-12-black-review)  
3. GoPro Hero 12 After 6 Months \- Not Worth It? \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=clSsX6EYl1I](https://www.youtube.com/watch?v=clSsX6EYl1I)  
4. GoPro HERO 12 Review – Is it Worth Buying in 2025?, 7月 15, 2025にアクセス、 [https://www.nomadasaurus.com/gopro-hero-12-review/](https://www.nomadasaurus.com/gopro-hero-12-review/)  
5. GoPro Hero12 Black Review: This tiny action camera provides a plethora of creative features \- DPReview, 7月 15, 2025にアクセス、 [https://www.dpreview.com/reviews/gopro-hero12-black-review-this-tiny-action-provides-a-plethora-of-creative-features](https://www.dpreview.com/reviews/gopro-hero12-black-review-this-tiny-action-provides-a-plethora-of-creative-features)  
6. GoPro Hero 12 \- Preferred Low light Settings : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/16s0a16/gopro\_hero\_12\_preferred\_low\_light\_settings/](https://www.reddit.com/r/gopro/comments/16s0a16/gopro_hero_12_preferred_low_light_settings/)  
7. Hero9 Hypersmooth low light test... Still not as it should be. \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/question/0D53b00008BtNbHCAV/hero9-hypersmooth-low-light-test-still-not-as-it-should-be?language=en\_US](https://community.gopro.com/s/question/0D53b00008BtNbHCAV/hero9-hypersmooth-low-light-test-still-not-as-it-should-be?language=en_US)  
8. How To Fix Lowlight HyperSmooth on your GoPro Abe Kislevitz, 7月 15, 2025にアクセス、 [https://abekislevitz.com/fix-lowlight-hypersmooth-on-your-gopro/](https://abekislevitz.com/fix-lowlight-hypersmooth-on-your-gopro/)  
9. The Absolute Best GoPro Low Light Settings \[2023 Update\] \- Veedyou, 7月 15, 2025にアクセス、 [https://www.veedyou.com/gopro-low-light/](https://www.veedyou.com/gopro-low-light/)  
10. looking for night settings, for climbing, running in low light areas.. gopro hero12 \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1egtqps/looking\_for\_night\_settings\_for\_climbing\_running/](https://www.reddit.com/r/gopro/comments/1egtqps/looking_for_night_settings_for_climbing_running/)  
11. What settings are best for the GoPro 12 in a dark / poorly lit room? Currently there is very much noise on the video.... I am using the GoPro 12 with the Max Lens mod 2.0. \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/question/0D58a0000ATzxOTCQZ/what-settings-are-best-for-the-gopro-12-in-a-dark-poorly-lit-room-currently-there-is-very-much-noise-on-the-video-i-am-using-the-gopro-12-with-the-max-lens-mod-20?language=en\_US](https://community.gopro.com/s/question/0D58a0000ATzxOTCQZ/what-settings-are-best-for-the-gopro-12-in-a-dark-poorly-lit-room-currently-there-is-very-much-noise-on-the-video-i-am-using-the-gopro-12-with-the-max-lens-mod-20?language=en_US)  
12. GoPro HERO12 Black review: The best GoPro to date \- Videomaker, 7月 15, 2025にアクセス、 [https://www.videomaker.com/reviews/cameras/gopro-hero12-black-review-the-best-gopro-to-date/](https://www.videomaker.com/reviews/cameras/gopro-hero12-black-review-the-best-gopro-to-date/)  
13. HERO12/11/10/9 Black: ISO Settings And Tips \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/article/HERO9-10-11-Black-ISO-Settings-And-Tips?language=en\_US](https://community.gopro.com/s/article/HERO9-10-11-Black-ISO-Settings-And-Tips?language=en_US)  
14. HERO12 Settings Guide Released : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/18hpnu7/hero12\_settings\_guide\_released/](https://www.reddit.com/r/gopro/comments/18hpnu7/hero12_settings_guide_released/)  
15. Question Detail \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/question/0D53b00008BtFjSCAV/terrible-highiso-noise-reduction?language=en\_US](https://community.gopro.com/s/question/0D53b00008BtFjSCAV/terrible-highiso-noise-reduction?language=en_US)  
16. Hi, first video on Hero 12 Black, it seems very noise: settings: 10 bit Standard, 16:9, 5.3k, 30fps, linear, Hypersmooth ON comp VE \-0.5, iso range 100-1600, sharpness low. What could I have done wrong? : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1dh5ntj/hi\_first\_video\_on\_hero\_12\_black\_it\_seems\_very/](https://www.reddit.com/r/gopro/comments/1dh5ntj/hi_first_video_on_hero_12_black_it_seems_very/)  
17. Best GoPro Night & Low Light Settings // No Noise \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=83PphFmaf18](https://www.youtube.com/watch?v=83PphFmaf18)  
18. GoPro Hero 12 Black Complete Beginners Guide & Best Settings \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=ZBoZeI-4w8s](https://www.youtube.com/watch?v=ZBoZeI-4w8s)  
19. Hypersmooth setting for lowight \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/question/0D53b00008BtGzRCAV/hypersmooth-setting-for-lowight?language=en\_US](https://community.gopro.com/s/question/0D53b00008BtGzRCAV/hypersmooth-setting-for-lowight?language=en_US)  
20. Shutter speed and ISO : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/18wu3xr/shutter\_speed\_and\_iso/](https://www.reddit.com/r/gopro/comments/18wu3xr/shutter_speed_and_iso/)  
21. GoPro Hero 12 LOW LIGHT Video Use THESE SETTINGS for Best Results \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=\_gUKzdUWJ6Y](https://www.youtube.com/watch?v=_gUKzdUWJ6Y)  
22. How much better is the stabilization on the newer GoPros : r/gopro, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1arkunz/how\_much\_better\_is\_the\_stabilization\_on\_the\_newer/](https://www.reddit.com/r/gopro/comments/1arkunz/how_much_better_is_the_stabilization_on_the_newer/)  
23. HERO12 Video Settings Guide Abe Kislevitz, 7月 15, 2025にアクセス、 [https://abekislevitz.com/hero12-video-settings-guide/](https://abekislevitz.com/hero12-video-settings-guide/)  
24. GoPro Hero 12 The Absolute BEST Settings \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=sUDBM8lujpU](https://www.youtube.com/watch?v=sUDBM8lujpU)  
25. GoPro Tutorial: How to add Motion Blur (Speed effect) \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=0dQV1JT-9DU](https://www.youtube.com/watch?v=0dQV1JT-9DU)  
26. GoPro Hero 12 \- How to Shoot in LOW LIGHT Settings Guide \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=TZpiDeSQM\_Q](https://www.youtube.com/watch?v=TZpiDeSQM_Q)  
27. GoPro BEST Low LIGHT / NIGHT Settings \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=-Aq-8NUv6I8](https://www.youtube.com/watch?v=-Aq-8NUv6I8)  
28. Your GoPro 12 videos suck? EASY step-by-step SETTINGS Guide\! \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=pUbFc8eeCj8](https://www.youtube.com/watch?v=pUbFc8eeCj8)  
29. Celebrating International Dark Sky Week with GoPro \+ HERO12 Black, 7月 15, 2025にアクセス、 [https://gopro.com/en/us/news/hero12-night-photography-guide](https://gopro.com/en/us/news/hero12-night-photography-guide)  
30. Advanced Protune Controls Explained \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/article/Advanced-Protune-Controls-Explained?language=en\_US](https://community.gopro.com/s/article/Advanced-Protune-Controls-Explained?language=en_US)  
31. I prefer the flat color mode : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1h8yp3z/i\_prefer\_the\_flat\_color\_mode/](https://www.reddit.com/r/gopro/comments/1h8yp3z/i_prefer_the_flat_color_mode/)  
32. How To Use Night Photo & Night Lapse \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/article/How-to-Use-Night-Photo-Night-Lapse?language=en\_US](https://community.gopro.com/s/article/How-to-Use-Night-Photo-Night-Lapse?language=en_US)  
33. HERO12 Black: 10-Bit Log Encoding \- GoPro Support, 7月 15, 2025にアクセス、 [https://community.gopro.com/s/article/10-Bit-Log-Encoding?language=en\_US](https://community.gopro.com/s/article/10-Bit-Log-Encoding?language=en_US)  
34. GoPro Hero12 \- Page 4 \- Cameras \- EOSHD Forum, 7月 15, 2025にアクセス、 [https://www.eoshd.com/comments/topic/76150-gopro-hero12/page/4/](https://www.eoshd.com/comments/topic/76150-gopro-hero12/page/4/)  
35. When to use Gyroflow stabilization (guide) : r/videography \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/videography/comments/1bnzknd/when\_to\_use\_gyroflow\_stabilization\_guide/](https://www.reddit.com/r/videography/comments/1bnzknd/when_to_use_gyroflow_stabilization_guide/)  
36. How to Use Gyroflow for FPV Drone Video Stabilization: A Step-by ..., 7月 15, 2025にアクセス、 [https://oscarliang.com/gyroflow/](https://oscarliang.com/gyroflow/)  
37. The ULTIMATE Setup Guide For Gyroflow \- NoirFPV, 7月 15, 2025にアクセス、 [https://noirfpv.com/gyroflow-setup/](https://noirfpv.com/gyroflow-setup/)  
38. Ultra wide linear footage GoPro 11 using Gyroflow \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/17gkdv1/ultra\_wide\_linear\_footage\_gopro\_11\_using\_gyroflow/](https://www.reddit.com/r/gopro/comments/17gkdv1/ultra_wide_linear_footage_gopro_11_using_gyroflow/)  
39. Color grading GP-Log : r/gopro \- Reddit, 7月 15, 2025にアクセス、 [https://www.reddit.com/r/gopro/comments/1jm5i31/color\_grading\_gplog/](https://www.reddit.com/r/gopro/comments/1jm5i31/color_grading_gplog/)  
40. Gopro Log Is Too Dark, Here's How To Fix It \- YouTube, 7月 15, 2025にアクセス、 [https://www.youtube.com/watch?v=vHJp6Mczrek](https://www.youtube.com/watch?v=vHJp6Mczrek)
