# Gemini DeepResearch Share

このリポジトリは、Google Geminiを使用したDeepResearchの結果を共有するためのGitHub Pagesサイトです。

## 構造

```
.
├── _config.yml      # サイトの設定ファイル
├── _topics/         # 各トピックのMarkdownファイル
├── _layouts/        # HTMLレイアウトテンプレート
├── _includes/       # 再利用可能なHTMLコンポーネント
├── assets/         # 静的ファイル（画像、CSS等）
└── index.md        # メインページ
```

## 新しいトピックの追加方法

1. `_topics` フォルダに新しいMarkdownファイルを作成します
2. ファイルの先頭に以下のようなFront Matterを追加します：

```yaml
---
layout: topic
title: "トピックのタイトル"
date: YYYY-MM-DD
tags: [タグ1, タグ2]
---
```

3. Markdownで内容を記述します

## ローカルでの開発

1. Rubyをインストール
2. 必要なgemをインストール：
   ```
   gem install bundler
   bundle install
   ```
3. ローカルサーバーを起動：
   ```
   bundle exec jekyll serve
   ```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。