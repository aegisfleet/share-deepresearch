# ポちのDeepResearch

![ポちのDeepResearch](assets/images/default-ogp.png)

このリポジトリは、Google Geminiを使用したDeepResearchの結果を共有するためのGitHub Pagesサイトです。

## 構造

```text
.
├── _config.yml      # サイトの設定ファイル
├── _topics/         # 各トピックのMarkdownファイル
│   └── topic-name/  # トピックごとのフォルダ
│       ├── index.md      # トピックのメインコンテンツ
│       └── dashboard.html # トピックの補足資料（SPA等）
├── _layouts/        # HTMLレイアウトテンプレート
├── _includes/       # 再利用可能なHTMLコンポーネント
├── assets/          # 静的ファイル
│   ├── audio/      # 音声ファイル
│   ├── css/        # スタイルシート
│   └── images/     # 画像ファイル
└── index.md        # メインページ
```

## 新しいトピックの追加方法

1. `_topics` フォルダに新しいフォルダを作成します（例：`my-research`）
1. そのフォルダ内に `index.md` を作成し、以下のようなFront Matterを追加します：

```yaml
---
layout: topic
title: "トピックのタイトル"
date: YYYY-MM-DD
category: "ai"  # "ai", "research", "code", "tutorial" のいずれかを指定
tags: [タグ1, タグ2]
audio: "/share-deepresearch/assets/audio/your-audio-file.mp3"  # 音声ファイル（オプション）
supplementary_materials:  # 補足資料（オプション）
  - title: "補足資料のタイトル"
    url: "/share-deepresearch/topics/your-topic/dashboard.html"
---
```

1. Markdownで内容を記述します
1. 必要に応じて、補足資料用のHTMLファイル（`dashboard.html`等）を作成します
1. 音声ファイルがある場合は、`assets/audio/` フォルダに配置します

## ドキュメント作成のワークフロー

DeepResearchの結果をドキュメント化する際の推奨手順は以下の通りです：

1. DeepResearchの結果をGoogleドキュメントにエクスポートします
2. Googleドキュメントから「ダウンロード」→「Markdownとして保存(.md)」を選択し、ダウンロードします
3. ダウンロードしたMarkdownファイルを`_topics/[トピック名]/index.md`として配置します
4. Geminiで作成した音声概要をmp3形式でダウンロードし、`assets/audio/`フォルダに配置します
5. 補足資料が必要な場合は、DeepResearchのレポート右上にある「作成」ボタンからダッシュボードなどを作成し、HTMLとしてエクスポートします
6. エクスポートしたHTMLファイルを`_topics/[トピック名]/dashboard.html`として配置します

このワークフローに従うことで、一貫性のあるドキュメント構造を維持できます。

## プロンプトメモ

- 資料を基にインフォグラフィックなデザインのWebサイトを作成したい。\
スマートフォンでも見れるデザインを前提として、JavaScriptのSPAを作成する。\
文量としては1000行程度のHTMLを想定している。
- スマートフォンを前提としたデザインで、○○を触って覚えるJavaScriptのSPAアプリ

### スライド作成

- Reveal.jsを用いたインフォグラフィックなプレゼン資料、Chart.jsとTailwind CSSを活用する。
- Impress.jsを用いたインフォグラフィックなプレゼン資料、スマートフォンへの表示にも対応することに留意する。

```text
あなたはプロのプレゼンテーションデザイナー兼フロントエンドエンジニアです。
添付されたレポートの内容を元に、プレゼンテーションライブラリ「reveal.js」で動作する、高品質なスライドのHTMLコンテンツを生成してください。

### 最終成果物
- レポートの内容を要約した、一連の`<section>`タグ群。
- 生成された`<section>`タグ群は、後述するreveal.jsのHTMLテンプレート内にそのまま挿入できる形式であること。

### 目的と構成
- **目的**:
    - 添付のレポート内容を、アイコンや多彩なレイアウトを用いて直感的に要約すること。**【最重要】特に、ユーザーがクリック操作をしなくても、スライドが切り替わるだけで各要素が自動的にアニメーション再生され、読み手が映像を見るように一人で学べる体験を創出する。**
- **構成**:
    - 全体で12〜15枚程度のスライドに「起承転結」を意識してまとめる。（**タイトル（背景画像付き）**、アジェンダ、起、承、転、結、**最終スライド（背景画像付き）**）

### デザインと技術仕様
- **カラーテーマ**:
    - 背景はダークグレー（例: `#1a1a1a`）、アクセントカラーはオレンジ（例: `#ff7733`）を基調としたデザインにしてください。リンク、アイコン、グラフの強調色などにオレンジを効果的に使用してください。
- **背景画像**:
    - **タイトルスライドと最終スライド**には、レポートのテーマを象徴する背景画像を挿入してください。
    - 画像の指定には `<section>` タグの `data-background-image="画像URL"` 属性を使用します。
    - テキストの可読性を確保するため、`data-background-opacity="0.2"` のように背景の透明度を適切に調整してください。
    - 画像はUnsplash (`https://images.unsplash.com/`) など、テーマに合った著作権フリーのものを提案してください。
- **レスポンシブ対応と可読性**:
    - PCの横長画面では、`.flex-container`などを用いて要素を効果的に左右に配置してください。
    - スマートフォンの縦長画面では、文字が小さくなりすぎないよう、十分なフォントサイズを確保してください。横並びレイアウトはCSSによって自動的に「縦積み」になることを前提としてコンテンツを構成してください。
- **レイアウト**:
    - 提供されたCSSクラス（`.flex-container`, `.flex-box`, `.comparison-table`など）を効果的に使用し、情報を視覚的に整理してください。
- **アニメーション、アイコン、演出**:
    - **メインアニメーション（ページ遷移時の自動再生）**:
        - 本プレゼンテーションの基本原則です。スライドが表示されたタイミングで、すべての主要な要素（アイコン、`.flex-box`、見出し、テキストブロック等）が時間差で自動的にアニメーション表示されるようにしてください。
        - 提供されたCSSの `.animated` クラスと `.delay-*` クラス（例: `class="animated delay-1"`）をすべての要素に適用し、リッチな登場演出を実現してください。
    - **補助的なアニメーション（クリックで進行）**:
        - 原則としてアニメーションは自動再生とし、ユーザーのクリック操作は不要とします。
        - 話の流れ上、どうしても意図的に情報を一つずつ見せたい場合に限り、例外的に `.fragment` クラスを使用してください。
    - **スライド間の切り替え効果**:
        - スライドが切り替わる際の演出として、`<section>` タグに `data-transition` 属性を追加してください。（例: `data-transition="slide"`）
        - 基本のトランジションは `slide`（横スライド）とし、章の区切りなど、場面転換を強調したい箇所では `convex` や `zoom` などを効果的に使用してください。
    - **アイコンの活用**:
        - 内容を象徴するFont Awesome 6のアイコン（`<i class="...">`）を積極的に使用し、情報を視覚的に補強してください。
- **テキスト**:
    - 各スライドのメッセージは、短い見出しと2〜3文の文章に要約してください。重要なキーワードは`<strong>`タグで強調してください。

### 作成手順
1.  まず、添付のレポートを分析し、上記の構成案と仕様に基づいた各スライドのプランを提案してください。プランには、**PCでのレイアウト概要**と、**スマートフォンでどのように見えるか**の簡単な説明、**スライド遷移時に自動再生されるアニメーション効果**の具体的な提案、そして**タイトルと最終スライドに使用する背景画像のアイデア（テーマと具体的な画像URL案を含む）**を含めてください。
2.  私がそのプランを確認し、承認します。
3.  承認後、そのプランに基づいて、完全な`<section>`タグ群を生成してください。

### SPAのイメージ
<!doctype html>
<html lang="ja">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">

    <title>DeepResearch Report Summary</title>

    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/reset.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/reveal.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/theme/black.min.css" id="theme">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.8.0/styles/monokai.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=Roboto:wght@300;400;700&display=swap" rel="stylesheet">

    <style>
        :root {
            --main-background-color: #1a1a1a;
            --box-background-color: #2d2d2d;
            --text-color: #e0e0e0;
            --heading-color: #ffffff;
            --accent-color: #ff7733;
            --accent-color-hover: #ff9966;

            --r-background-color: var(--main-background-color);
            --r-main-font: 'Roboto', sans-serif;
            --r-code-font: 'Fira Code', monospace;
            --r-heading-font: 'Roboto', sans-serif;
            --r-heading-text-transform: none;
            --r-heading-font-weight: 700;
            --r-main-color: var(--text-color);
            --r-heading-color: var(--heading-color);
            --r-link-color: var(--accent-color);
            --r-link-color-hover: var(--accent-color-hover);
        }

        .reveal { font-size: 32px; }
        .reveal h1 { font-size: 2.8em; }
        .reveal h2 { font-size: 2.0em; }
        .reveal h3 { font-size: 1.4em; }
        .reveal p { font-size: 0.9em; line-height: 1.7; }
        .reveal ul, .reveal ol { margin-top: 20px; }
        .reveal li { line-height: 1.7; }

        .reveal .subtitle { font-size: 1.2em; font-weight: 300; color: var(--accent-color); margin-top: 20px; }
        .reveal .left-align { text-align: left; }
        .reveal .small-text { font-size: 0.7em; }
        .reveal strong { color: var(--accent-color); font-weight: 700; }

        .flex-container { display: flex; justify-content: space-around; align-items: center; gap: 20px; }
        .flex-box { flex: 1; background: var(--box-background-color); padding: 25px; border-radius: 10px; text-align: center; }
        .flex-box i { font-size: 3em; color: var(--accent-color); margin-bottom: 20px; }

        .comparison-table { width: 100%; border-collapse: collapse; margin-top: 30px; font-size: 0.8em; }
        .comparison-table th, .comparison-table td { border: 1px solid rgba(255, 255, 255, 0.2); padding: 15px; text-align: left; }
        .comparison-table th { background-color: var(--accent-color); color: #000; }
        .comparison-table td:first-child { font-weight: bold; color: var(--accent-color); }

        @media (max-width: 768px) {
            .reveal {
                font-size: 40px;
            }
            .reveal h1 { font-size: 2.2em; }
            .reveal h2 { font-size: 1.7em; }
            .reveal h3 { font-size: 1.3em; }
            .reveal p { font-size: 1.3em; line-height: 1.65; }
            .reveal li { font-size: 1.3em; line-height: 1.65; }

            .flex-container {
                flex-direction: column;
                gap: 25px;
            }

            .flex-box i {
                font-size: 2.5em;
                margin-bottom: 15px;
            }

            .comparison-table { font-size: 1.2em; }

            .flex-container i.fa-arrow-right-long {
                transform: rotate(90deg);
                margin: 20px 0;
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translate3d(0, 40px, 0);
            }
            to {
                opacity: 1;
                transform: translate3d(0, 0, 0);
            }
        }

        .animated {
            opacity: 0;
        }

        .reveal .slides section.present .animated {
            opacity: 1;
            animation-fill-mode: both;
            animation-name: fadeInUp;
            animation-duration: 1.0s;
        }

        .reveal .slides section.present .animated.delay-1 { animation-delay: 0.2s; }
        .reveal .slides section.present .animated.delay-2 { animation-delay: 0.4s; }
        .reveal .slides section.present .animated.delay-3 { animation-delay: 0.6s; }
        .reveal .slides section.present .animated.delay-4 { animation-delay: 0.8s; }
        .reveal .slides section.present .animated.delay-5 { animation-delay: 1.0s; }

    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-background-color="var(--main-background-color)">
                <h1>スライドタイトル</h1>
                <p>このテンプレートはダークグレーとオレンジを基調としています。<br>スマートフォンで表示すると、文字が大きくなり、レイアウトが縦に変わります。</p>
            </section>
        </div>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/reveal.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/plugin/notes/notes.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/plugin/markdown/markdown.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/reveal.js/4.6.1/plugin/highlight/highlight.min.js"></script>
    <script>
        Reveal.initialize({
            hash: false, 
            hash: true,
            width: 1920,
            height: 1080,
            margin: 0.04,
            minScale: 0.2,
            maxScale: 2.0,
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes ]
        });
    </script>
</body>
</html>
```

## ローカルでの開発

1. Rubyをインストール
1. 必要なgemをインストール：

```bash
gem install bundler
bundle install
```

1. ローカルサーバーを起動：

```bash
bundle exec jekyll serve --config _config_dev.yml
```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。
