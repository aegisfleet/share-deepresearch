---
audio: /share-deepresearch/assets/audio/deepagents.m4a
video: /share-deepresearch/assets/video/deepagents.mp4
category: ai
date: 2026-03-12
description: LangChainが提供するAIエージェント構築のための包括的なフレームワーク「Deep Agents」についてのレポートです。ファイルシステムアクセス、サブエージェント、プランニングなどの機能が組み込まれています。
layout: topic
prompt: 指示書に従い https://github.com/langchain-ai/deepagents のレポートを追加して。本日は2026-03-12。
supplementary_materials:
  - title: インフォグラフィック
    url: /share-deepresearch/topics/deepagents/infographic.html
  - title: プレゼンテーション
    url: /share-deepresearch/topics/deepagents/reveal.html
tags:
- LangChain
- DeepAgents
- AI Agent
- LangGraph
title: LangChain Deep Agents：包括的なAIエージェント構築フレームワーク
---

# LangChain Deep Agents：包括的なAIエージェント構築フレームワーク

## 概要

Deep Agentsは、LangChainおよびLangGraph上に構築された、AIエージェントのための「batteries-included（必要なものがすべて揃った）」ハーネスです。プロンプト、ツール、コンテキスト管理を自前で配線する代わりに、すぐに動作するエージェントを取得し、必要な部分だけをカスタマイズすることができます。

## 主な機能

Deep Agentsには、エージェントが自律的に複雑なタスクを処理するために必要な機能がデフォルトで組み込まれています。

*   **プランニング機能**: `write_todos`ツールを使用して、タスクの分解と進捗状況の追跡を行います。
*   **ファイルシステムアクセス**: `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep`などのツールを備え、ファイルの読み書きによるコンテキストの把握やコードの編集が可能です。
*   **シェルアクセス**: `execute`ツールを使用して、サンドボックス環境内でコマンドを実行できます。
*   **サブエージェント**: `task`ツールを使用して、独立したコンテキストウィンドウを持つサブエージェントに作業を委任できます。
*   **スマートなデフォルト設定**: これらのツールを効果的に使用する方法をLLMに教えるプロンプトが最初から設定されています。
*   **コンテキスト管理**: 会話が長くなった場合の自動要約機能や、大量の出力をファイルに保存する機能が備わっています。

## 使用方法

### インストール

Deep AgentsはPythonパッケージとして提供されており、`pip`または`uv`を使用して簡単にインストールできます。

```bash
pip install deepagents
# または
uv add deepagents
```

### クイックスタート

以下のコードは、Deep Agentsを使用してLangGraphについてリサーチし、要約を作成する簡単な例です。

```python
from deepagents import create_deep_agent

agent = create_deep_agent()
result = agent.invoke({"messages": [{"role": "user", "content": "Research LangGraph and write a summary"}]})
```

エージェントは自律的に計画を立て、ファイルを読み書きし、自身のコンテキストを管理します。必要に応じて、ツールの追加、プロンプトのカスタマイズ、モデルの変更が可能です。

### カスタマイズ

Deep Agentsは高い拡張性を備えており、独自の要件に合わせて動作を調整できます。

```python
from langchain.chat_models import init_chat_model

agent = create_deep_agent(
    model=init_chat_model("openai:gpt-4o"),
    tools=[my_custom_tool],
    system_prompt="You are a research assistant.",
)
```

また、MCP（Model Context Protocol）は`langchain-mcp-adapters`を通じてサポートされています。

## CLIツールの提供

Deep Agentsはコマンドラインインターフェース（CLI）も提供しており、ウェブ検索、リモートサンドボックス、永続的なメモリ、Human-in-the-loop（人間の承認プロセス）などをサポートしています。

```bash
curl -LsSf https://raw.githubusercontent.com/langchain-ai/deepagents/main/libs/cli/scripts/install.sh | bash
```

## LangGraphネイティブ

`create_deep_agent`関数は、コンパイルされたLangGraphのグラフを返します。これにより、ストリーミング、LangGraph Studio、チェックポインターなど、LangGraphのすべての機能をシームレスに利用できます。

## なぜDeep Agentsを使用するのか？

*   **100%オープンソース**: MITライセンスの下で公開されており、完全に拡張可能です。
*   **プロバイダー非依存**: ツール呼び出しをサポートする任意のLLM（フロンティアモデル、オープンソースモデル問わず）で動作します。
*   **LangGraphベース**: ストリーミング、永続化、チェックポイント機能を備えた、本番環境対応のランタイム上に構築されています。
*   **オールインワン**: プランニング、ファイルアクセス、サブエージェント、コンテキスト管理がすぐに機能します。
*   **数秒で開始可能**: `uv add deepagents`を実行するだけで、すぐに動作するエージェントが手に入ります。
*   **数分でカスタマイズ**: 必要に応じてツールの追加、モデルの変更、プロンプトの調整が容易です。

## セキュリティに関する考慮事項

Deep Agentsは「LLMを信頼する（trust the LLM）」モデルに従っています。エージェントは、提供されたツールが許可するすべての操作を実行できます。そのため、モデルが自制することを期待するのではなく、ツールやサンドボックスレベルで厳密な境界を強制する必要があります。

## まとめ

Deep Agentsは、LangChainとLangGraphの強力な基盤の上に、複雑なエージェント的タスクを処理するための実践的なツール群を統合した、非常に実用的なフレームワークです。Claude Codeからインスピレーションを得て開発され、その汎用性をさらに高めることを目指しています。
