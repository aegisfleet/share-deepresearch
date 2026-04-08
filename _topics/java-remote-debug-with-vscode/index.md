---
audio: /share-deepresearch/assets/audio/java-remote-debug-with-vscode.m4a
category: engineering
date: 2025-11-17
description: Tomcat上で動作するJavaアプリケーションのリモートデバッグをVSCodeで実現するための完全ガイド。ブレイクポイントやステップ実行などの高度なデバッグ機能の設定方法を詳述します。
ga4_metrics:
  avgSessionDuration: 55.68812757142857
  pageViews: 66
  users: 49
layout: topic
prompt: Tomcat上で動作するJavaアプリケーションのリモートデバッグをVSCodeを使用して実現したい。出来ればブレイクポイントやステップ実行ができる環境が良い。どのようなやり方があるか調査して欲しい。
tags:
- Java
- VSCode
title: VSCodeによるTomcat Javaアプリケーションの完全リモートデバッグガイド
video: /share-deepresearch/assets/video/java-remote-debug-with-vscode.mp4
---

# **VSCodeによるTomcat Javaアプリケーションの完全リモートデバッグガイド**

## **第1章: 概要とデバッグアーキテクチャの基礎**

Visual Studio Code (VSCode) を使用して Apache Tomcat 上で動作する Java アプリケーションのリモートデバッグ環境を構築することは、現代の開発ワークフローにおいて不可欠な技術です。このプロセスは、ブレイクポイントでの実行停止、ステップ実行、変数検査といった強力なデバッグ機能を、リモートサーバー上で稼働するアプリケーションに対して直接実行することを可能にします。

本ガイドでは、このリモートデバッグ環境を構築するための2つの主要なアプローチ（手動によるアタッチ設定と、VSCode拡張機能による統合管理）を、アーキテクチャの基礎から体系的に解説します。

### **1.1. リモートデバッグの心臓部：JPDA (Java Platform Debugger Architecture)**

VSCode と Tomcat 間のリモートデバッグは、Java Development Kit (JDK) に標準搭載されている JPDA (Java Platform Debugger Architecture) によって実現されます。JPDA は、デバッグ対象の Java Virtual Machine (JVM) とデバッガ（この場合は VSCode）が通信するための標準仕様です。

このアーキテクチャは、主に以下のコンポーネントで構成されます。

* **JDWP (Java Debug Wire Protocol):** デバッガと JVM が通信するために使用するプロトコルです。  
* **JDI (Java Debug Interface):** デバッガクライアント（VSCode）が JDWP を介して JVM を操作するための高レベル Java API です。

実際にデバッグを有効化する際、Tomcat（JVM）の起動オプションとして、JDWP エージェントをロードするための設定を行います。この設定には、以下のキーコンセプトが含まれます。

1. transport=dt_socket:  
   デバッグ通信のトランスポート（通信手段）として、標準的なTCP/IPソケット（dt_socket = Debug Transport Socket）を使用することを指定します 1。  
2. server=y:  
   JVM（Tomcat）側がデバッグサーバーとして動作し、指定されたポートでデバッガクライアント（VSCode）からの接続要求を「待ち受ける (listen)」モードであることを示します 2。  
3. request = "attach":  
   VSCode のデバッグ構成（launch.json）で使用される設定です。VSCode のデバッグモードには launch と attach があります 5。  
   * **launch**: VSCode が Java プロセスを*新規に起動*し、それにアタッチします。  
   * **attach**: VSCode が、*既に起動・実行中*の外部 Java プロセス（我々のTomcat）に対して接続（アタッチ）しにいきます 5。リモートデバッグでは、この attach モードを使用します。

### **1.2. VSCode：Javaデバッグ環境の基盤構築**

VSCode で Java のリモートデバッグを実現するには、VSCode 本体に加えて、協調して動作する複数の拡張機能で構成される「エコシステム」が必要です。

最も重要なのは、Microsoft が提供する Extension Pack for Java (vscjava.vscode-java-pack) です 8。この拡張機能パックには、Java 開発とデバッグに必要な主要コンポーネントが含まれています 8。

このエコシステムの中核を成すのは、以下の2つの拡張機能です。

1. Language Support for Java™ by Red Hat (redhat.java):  
   この拡張機能は、Java プロジェクトの「頭脳」として機能します 8。Maven (pom.xml) や Gradle (build.gradle) のビルド定義を解析し、プロジェクトのクラスパス、ソースパス、依存ライブラリを正確に理解します。これにより、コードナビゲーション、リファクタリング、自動補完が可能になります。  
2. Debugger for Java (vscjava.vscode-java-debug):  
   この拡張機能が、JPDA/JDWP プロトコルを介した実際のデバッグセッションを管理します 5。ブレイクポイントの管理、ステップ実行、変数検査などを担当します。

これら2つの拡張機能の関係性を理解することは、デバッグのトラブルシューティングにおいて極めて重要です。Debugger for Java は、Language Support for Java by Red Hat を*拡張する*形で動作します 5。

つまり、デバッガがブレイクポイントで停止した際、JVM からは「com.example.MyServlet の 42 行目で停止した」という情報しか送られてきません。Debugger for Java が、ローカルワークスペース内の src/main/java/com/example/MyServlet.java ファイルを開き、該当する 42 行目をハイライトするためには、redhat.java が提供するプロジェクトのソースパス情報が不可欠です。

この連携が失敗すると、デバッグセッション自体は開始できても、「Source code does not match the bytecode（ソースコードがバイトコードと一致しません）」という致命的なエラー（第5章で詳述）が発生します 11。したがって、デバッグ設定に進む前に、まず VSCode のエクスプローラー（Java プロジェクトビュー）が対象の Java プロジェクトを正しく認識し、エラーなくインポートできていることを確認するのが、デバッグ成功の第一歩となります 13。

## **第2章: 手法1：手動設定によるリモートアタッチ（標準的アプローチ）**

この章では、最も標準的で、ローカル・リモートを問わずあらゆる Tomcat インスタンスに適用可能な「手動アタッチ」方式をステップバイステップで解説します。この手法は、Tomcat 側でデバッグポートを有効にし、VSCode 側で launch.json ファイルを作成して接続する、という2段階で構成されます。

### **2.1. ステップ1：Tomcatサーバーのデバッグモード有効化 (JPDA設定)**

Tomcat をデバッグモードで起動するには、Tomcat を実行する JVM に対し、JPDA の起動時引数（-agentlib:jdwp=...）を渡す必要があります。

#### **方法A: jpda start コマンド (簡易的)**

Tomcat には、デバッグモードを簡易的に起動するためのラッパースクリプトが同梱されています。CATALINA_HOME/bin ディレクトリで、以下のコマンドを実行します。

* Linux/macOS: $./catalina.sh jpda start 4  
* Windows: > catalina.bat jpda start 4

このコマンドは、Tomcat が内部で定義するデフォルトのJPDA設定（通常は transport=dt_socket, address=8000, server=y, suspend=n）でサーバーを起動します 14。手軽ですが、ポート番号や suspend モードをカスタマイズするには不便です。

#### **方法B: setenv.sh / setenv.bat の利用 (エキスパート推奨)**

Tomcat の設定を恒久的かつ安全に行うためのベストプラクティスは、setenv スクリプトを使用する方法です。Tomcat の起動スクリプト（catalina.sh / catalina.bat）は、CATALINA_HOME/bin ディレクトリ内に setenv.sh（または setenv.bat）という名前のファイルが存在すれば、それを自動的に読み込んで実行します 18。

このアプローチには、catalina.sh 本体を直接編集する方法 20 に比べて、2つの決定的な利点があります。

1. **設定の分離:** サーバー固有の環境変数（CATALINA_OPTS, JPDA_OPTS など）を、Tomcat のコアスクリプトから分離できます 19。これにより、設定の見通しが良くなります。  
2. **移植性と保守性:** Tomcat のバージョンアップ時に catalina.sh が上書きされても、setenv.sh はそのまま残るため、カスタム設定が失われません 19。また、catalina.sh の内部ロジックを誤って破壊するリスクを回避できます（例：stop コマンドの動作に影響を与える 14）。

**setenv.sh の具体的な設定例 (Linux/macOS)**

CATALINA_HOME/bin/setenv.sh という名前で新しいファイルを作成し、以下の内容を記述します。

```Bash
#!/bin/sh

# JDWPトランスポートとしてdt_socketを指定  
export JPDA_TRANSPORT="dt_socket"

# リモート接続を許可するため、全インターフェース(*)でポート8000をリッスン  
# 注意: 'localhost' や '127.0.0.1' にするとリモートから接続不可  
export JPDA_ADDRESS="*:8000"

# 'n' = JVMはデバッガの接続を待たずに即時起動  
# 'y' = JVMはデバッガが接続するまで起動を一時停止  
export JPDA_SUSPEND="n"

# JVM 5.0 (Java 1.5) 以降で推奨される -agentlib 形式  
# [4, 17, 18, 22]  
export JPDA_OPTS="-agentlib:jdwp=transport=$JPDA_TRANSPORT,address=$JPDA_ADDRESS,server=y,suspend=$JPDA_SUSPEND"

# JPDA_OPTS を CATALINA_OPTS (Tomcat起動時に使われるJVMオプション) に追加  
# [22]  
export CATALINA_OPTS="$CATALINA_OPTS $JPDA_OPTS"
```

**注意:** JVM 5.0 (Java 1.5) 以前の古い環境では -Xdebug と -Xrunjdwp が使用されていましたが 1、現代の JVM (1.8以降) では -agentlib:jdwp 形式の使用が強く推奨されます 21。

#### **表1: JPDA -agentlib:jdwp オプション詳細**

上記の設定例に登場する JDWP のオプションは、デバッグ接続の動作を決定する上で極めて重要です。

| オプション | 設定例 | 解説 |
| :---- | :---- | :---- |
| transport | dt_socket | (必須) デバッグ・トランスポートとしてTCP/IPソケットを使用します 2。 |
| server | y | (必須) JVM側がサーバーとして機能し、デバッガの接続を待ち受けます 2。 |
| suspend | n (推奨) | n: JVMはデバッガの接続を待たずに即座に起動します 2。 y: JVMはデバッガが接続してくるまで起動を一時停止します。Tomcat の起動シーケンス自体をデバッグする場合にのみ使用します 15。 |
| address | *:8000 (リモート) | (最重要) 待ち受けるポートとIPアドレスを指定します。 • 8000: ポート8000。Tomcatのデフォルト 3。 • 127.0.0.1:8000: *ローカルホストからのみ*接続を許可します 24。 • *:8000 または 0.0.0.0:8000: *すべてのネットワークインターフェース*で待ち受け、リモートマシンからの接続を許可します。リモートデバッグにはこの設定が必須です 2。 |

setenv.sh（または setenv.bat）を作成したら、jpda start を使用する必要は*ありません*。通常通り、./catalina.sh run や ./startup.sh で Tomcat を起動するだけです。setenv.sh があれば、通常の起動コマンドでもデバッグオプションが自動的に読み込まれます 22。

### **2.2. ステップ2：VSCodeクライアント launch.json のアタッチ設定**

Tomcat サーバーがデバッグポート（例: 8000）を開いて待ち受け状態になったら、次は VSCode 側からそのポートに接続（アタッチ）するための設定を行います。

1. VSCode でデバッグ対象の Java プロジェクト（のソースコード）が含まれるワークスペースを開きます。  
2. アクティビティバーから「実行とデバッグ」ビューを選択します 5。  
3. 「launch.json ファイルを作成します」というリンクをクリックし、表示されるメニューから「Java」を選択します。  
4. これにより、ワークスペースのルートに .vscode/launch.json ファイルが作成されます。  
5. configurations 配列に、以下の attach 設定を追加します 5。

**launch.json の完全な設定例:**

```JSON
{  
  "version": "0.2.0",  
  "configurations":,  
      "timeout": 30000  
    }  
  ]  
}
```

#### **表2: launch.json 'attach' 主要オプション**

launch.json の各オプションは、VSCode デバッガの動作を制御します。

| オプション | 型 | 解説 |
| :---- | :---- | :---- |
| type | string | (必須) java を指定します 5。 |
| name | string | (必須) デバッグ構成のドロップダウンに表示される任意の名前 28。 |
| request | string | (必須) attach を指定します 5。 |
| hostName | string | (必須) 接続先Tomcatサーバーのホスト名またはIPアドレス 5。 |
| port | number | (必須) 接続先TomcatサーバーのJPDAポート（setenv.sh の JPDA_ADDRESS で設定したポート） 5。 |
| sourcePaths | string | (強く推奨) ソースコードマッピングのためのパス配列 5。詳細は第5章参照。 |
| projectName | string | (推奨) ワークスペースに複数プロジェクトがある場合、ソース検索の基点となるプロジェクト名を指定します。式評価や条件付きブレイクポイントの動作に必要です 5。 |
| timeout | number | デバッガがJVMへの接続を試みるタイムアウト時間（ミリ秒）。デフォルトは 3000ms 5 または 30000ms 5。ネットワークが遅い環境では延長が必要です 31。 |

launch.json ファイルを保存した後、「実行とデバッグ」ビューの上部にあるドロップダウンから、今作成した "Attach to Remote Tomcat" を選択し、緑色の再生ボタン（または F5 キー）を押します 5。

VSCode が Tomcat サーバーの JPDA ポートへの接続に成功すると、デバッグコンソールがアクティブになり、ステータスバーがオレンジ色に変わります。これでリモートデバッグの準備が完了です。

## **第3章: 手法2：統合サーバー拡張機能によるシームレスなデバッグ**

第2章で解説した setenv.sh と launch.json による手動アタッチは、非常に強力で柔軟性が高い一方、特にローカル環境での開発サイクル（コード変更 → ビルド → デプロイ → デバッグ）においては、設定が煩雑です。

VSCode のエコシステムは、このプロセスを自動化し、IDE 内で完結させるためのサーバー統合拡張機能を提供しています。

### **3.1. Tomcat for VS Code (adashen.vscode-tomcat) (旧・非推奨)**

過去、Tomcat for VS Code (adashen.vscode-tomcat) という拡張機能が広く使われていました 32。これは VSCode 内から Tomcat サーバーを追加し、WAR ファイルのデプロイやデバッグの開始を管理する機能を提供します。この拡張機能も、実際のデバッグ実行には Debugger for Java を必要とします 32。

しかし、VSCode の Java サポートエコシステムは成熟と標準化の過程を辿っています。adashen/vscode-tomcat 拡張機能は現在**非推奨 (deprecated)** とされており 34、より近代的で標準化されたアプローチが推奨されています。

この進化の背景には、単一のサーバー（Tomcat）に特化した拡張機能から、Red Hat が主導する **Remote Server Protocol (RSP)** という標準プロトコル 35 に基づくアプローチへの移行があります。RSP は、Tomcat, Karaf, Felix, Jetty など、複数の異なるサーバーランタイムを VSCode から統一されたインターフェースで管理することを可能にします 35。

### **3.2. Community Server Connectors (redhat.vscode-community-server-connector) (推奨)**

現在、ローカルでの Tomcat 統合デバッグに最も推奨されるのは、Red Hat が発行する Community Server Connectors (redhat.vscode-community-server-connector) 拡張機能です 35。

この拡張機能は、第2章で解説した「サーバー側での JPDA 有効化」と「クライアント側での launch.json 設定」という2つの手動プロセスを**完全に抽象化・自動化**します。

**Community Server Connectors によるローカルデバッグ手順:**

1. VSCode の拡張機能マーケットプレイスから Community Server Connectors (redhat.vscode-community-server-connector) をインストールします 38。  
2. コマンドパレット (Ctrl+Shift+P または Cmd+Shift+P) を開き、Servers: Add Local Servers... を検索して実行します 38。  
3. ファイルピッカーが表示されるので、ローカルにインストールされている Tomcat のルートディレクトリ（CATALINA_HOME に相当するディレクトリ）を選択します 38。  
4. VSCode のアクティビティバーに「SERVERS」ビュー（サーバーのアイコン）が追加されます。  
5. 「SERVERS」ビューを開くと、追加した Tomcat サーバーが表示されます。サーバーを右クリックし、「Start」または「Debug」を選択します 39。  
6. デバッグ対象のプロジェクト（WARファイルやMavenプロジェクト）を右クリックし、「Run on Server」または「Debug on Server」を選択して、サーバーにデプロイします 38。

Community Server Connectors を使用する場合、開発者は launch.json ファイルを**一切作成する必要がありません**。

一部の開発者は、この拡張機能でサーバーを起動した後、さらに手動で launch.json を設定してアタッチしようと試み、混乱することがあります 40。しかし、これは根本的な誤解です。

ユーザーが「SERVERS」ビューで「Debug」をクリックすると、Community Server Connectors 拡張機能は*内部的*に以下の処理をすべて自動で行います：

1. Tomcat を起動するための適切な JPDA 引数（-agentlib:jdwp=...）を動的に生成します。  
2. その引数を使って Tomcat をデバッグモードで起動します。  
3. Debugger for Java 拡張機能を呼び出し、Tomcat がリッスンしている動的なデバッグポートに*自動的にアタッチ*します。

この拡張機能は、第2章で解説した手動アタッチの「ヘルパー」ではなく、「完全な代替品」であり、ローカル開発の生産性を劇的に向上させます。

### **3.3. 表3: デバッグ手法の比較（手法1 vs 手法2）**

どちらの手法を選択すべきかは、開発シナリオによって明確に異なります。

| 比較項目 | 手法1: 手動アタッチ (launch.json) | 手法2: 拡張機能 (Community Server Connectors) |
| :---- | :---- | :---- |
| **主な用途** | 既に起動中の**リモートサーバー**（開発、ステージング環境、コンテナ）への接続 42。 | **ローカル開発サイクル**の高速化 36。 |
| **Tomcatの制御** | VSCodeの**外部**で手動起動（catalina.sh 等）。 | VSCodeの**内部**からサーバーを起動・停止・デバッグ 35。 |
| **デプロイ** | 手動（.war のコピー、Tomcat Manager等）。 | VSCode内からプロジェクトをデプロイ（発行）可能 35。 |
| **設定の複雑さ** | 高。setenv.sh と launch.json の両方を正確に設定する必要がある 5。 | 低。GUI操作でサーバーを追加するだけ 38。 |
| **柔軟性** | 高。任意のJPDAパラメータ、SSHトンネル 24 等、複雑なネットワーク構成に対応可能。 | 低。拡張機能がサポートする構成（主にローカル）に限られる。 |

## **第4章: 実践：デバッグ機能の活用**

Tomcat サーバーへのアタッチが成功すると、VSCode のデバッグインターフェースがアクティブになり、Java アプリケーションの実行フローを詳細に制御・検査できるようになります。

### **4.1. ブレイクポイントの完全活用**

ブレイクポイントは、デバッガに実行を一時停止させたいコード行を指示するマーカーです。

* 行ブレイクポイント (Line Breakpoints):  
  最も基本的なブレイクポイントです。エディタの行番号の左側（ガターマージン）をクリックするか、対象の行にカーソルを置いて F9 キーを押すことで、赤い円のアイコン（ブレイクポイント）を設定・解除できます 44。例えば、サーブレットの doGet や doPost メソッドの先頭行に設定します 39。  
* 高度なブレイクポイント:  
  VSCode の Java デバッガは、より高度なブレイクポイントもサポートしています 5。  
  * 条件付きブレイクポイント (Conditional Breakpoints):  
    ガターマージンのブレイクポイントを右クリックし、「条件付きブレイクポイントを追加」を選択します。ここで、true と評価された場合のみ実行を停止する Java の式を入力できます（例: request.getParameter("user").equals("admin")） 44。これにより、特定の条件が満たされた場合のみデバッグが可能になります。  
  * ログポイント (Logpoints):  
    「ログポイントを追加」を選択すると、実行を停止する代わりに、指定したメッセージや式の結果をデバッグコンソールに出力できます 5。これは、コードに System.out.println を埋め込んで再デプロイする手間を省くための強力な機能です。  
  * データブレイクポイント (Data Breakpoints):  
    デバッグセッションがアクティブな状態で、「変数」ビューに表示されている特定のフィールド（クラスのメンバー変数など）を右クリックし、「値が変更されたときに中断 (Break on Value Change)」を選択します 5。これにより、その変数の値が変更された瞬間にデバッガが自動的に停止します。

### **4.2. 実行フローの制御（ステップ実行）**

ブレイクポイントで実行が一時停止すると、VSCode のウィンドウ上部（または設定した位置）に「デバッグツールバー」が表示されます 44。このツールバーを使用して、プログラムの実行フローを一行ずつ制御します。

* 続行 (Continue) (F5):  
  実行を再開します。プログラムは、次のブレイクポイントに到達するか、終了するまで実行されます 39。  
* ステップオーバー (Step Over) (F10):  
  現在の行を実行し、同じメソッド内の次の行で停止します。もし現在の行にメソッド呼び出しが含まれていても、そのメソッドの中には入らず、メソッド全体を実行して次の行に進みます 5。  
* ステップイン (Step Into) (F11):  
  現在の行にメソッド呼び出しが含まれている場合、そのメソッドの内部に入り、呼び出されたメソッドの最初の行で停止します 5。  
* ステップアウト (Step Out) (Shift+F11):  
  現在実行中のメソッドの残りの行をすべて実行し、このメソッドを呼び出した元の場所（コールスタックの一つ上）の次の行で停止します 5。  
* 再起動 (Restart) (Ctrl+Shift+F5):  
  現在のデバッグセッションを終了し、launch.json の設定に基づいて新しいセッションを開始します（リモートアタッチの場合、再接続を行います） 44。  
* 停止 (Stop) (Shift+F5):  
  デバッグセッションを終了します 44。リモートアタッチの場合、Tomcat サーバー自体は停止せず、デバッガがJVMから切断（デタッチ）されるだけです。

### **4.3. 状態の検査と評価**

実行が一時停止している間、アプリケーションの現在のメモリ状態を詳細に調査できます。

* 変数 (Variables) ビュー:  
  デバッグサイドバーの「変数」パネルには、現在のスコープ（ローカル変数、メソッドの引数、this）がツリー形式で表示されます 5。値を展開して、オブジェクトのフィールドを深く掘り下げて確認できます。  
* ウォッチ (Watch) ビュー:  
  「ウォッチ」パネルに特定の変数名や式（例: request.getSession().getId()）を登録しておくと、ステップ実行するたびにその式の値が自動的に再評価され、常に最新の値が表示されます 44。  
* デバッグコンソール (Debug Console):  
  このコンソールは、対話型（REPL）の実行環境として機能します 5。現在のスコープにある変数を使用したり、myObject.calculateValue() のようなメソッドを動的に呼び出したりして、その結果を即座に確認できます。

## **第5章: 重大エラーへの対処：トラブルシューティングガイド**

リモートデバッグは、ネットワーク、サーバー設定、クライアント設定、ソースコードの同期など、複数の要素が正確に連携する必要があるため、問題が発生しやすいポイントがいくつか存在します。ここでは、最も一般的な2つの重大エラーについて、原因の特定と体系的な解決策を詳述します。

### **5.1. 接続失敗：「Connection refused」 / 「Connection timed out」**

launch.json を実行（F5）した際に、VSCode が Tomcat へのアタッチに失敗するケースです。エラーメッセージによって原因がほぼ特定できます。

#### **ケースA: 「Connection refused (接続が拒否されました)」**

* **エラーメッセージ (例):** Failed to connect to remote VM. Connection refused. 2  
* **現象:** デバッグ実行後、即座にエラーが表示される。  
* **意味:** VSCode からの TCP 接続要求が Tomcat サーバーに到達したが、サーバー（OS または JVM）がそのポートでの接続を*即座に拒否*したことを示します。  
* 原因1 (最重要): address のバインディングミス。  
  Tomcat の setenv.sh (または JPDA_OPTS) が、address=127.0.0.1:8000 または address=localhost:8000 と設定されています 24。この設定は、JVM がローカルホスト (自分自身) からの接続のみを受け入れることを意味します。VSCode が動作しているリモートマシンからの接続は、すべて「拒否」されます。  
  * **解決策:** Tomcat の setenv.sh を編集し、JPDA_ADDRESS を *:8000 または 0.0.0.0:8000 に変更します 2。これにより、Tomcat はすべてのネットワークインターフェース（IPアドレス）からの接続を受け入れるようになります。  
* 原因2: ポートの不一致。  
  launch.json の port (例: 8000) と、Tomcat が JPDA_ADDRESS でリッスンしているポート (例: 8001) が一致していません。

#### **ケースB: 「Connection timed out (接続がタイムアウトしました)」**

* **エラーメッセージ (例):** Failed to connect to remote VM. Connection timed out. 1  
* **現象:** デバッグ実行後、launch.json の timeout で設定された時間（例: 30秒）が経過した後に、エラーが表示される。  
* **意味:** VSCode からの TCP 接続要求パケットが送信されましたが、応答がないままタイムアウトしました。これは、パケットがサーバーに到達しなかった（ネットワーク的にブロックされた）か、サーバーには到達したが応答が返ってこなかった（ネットワークが極端に遅い）ことを示します。  
* 原因1 (最重要): ファイアウォール。  
  Tomcat サーバーが動作している OS のファイアウォール（Linux の iptables / firewalld / ufw など）や、クラウドプロバイダー（AWS, Azure, GCP）のネットワークセキュリティグループが、JPDA_ADDRESS で指定されたポート（例: 8000）への着信 TCP 接続をブロック（DROP）しています 1。  
  * **解決策:** サーバーのファイアウォール設定を確認し、デバッグポート（例: 8000）への TCP 接続を、VSCode が動作しているマシンの IP アドレスから許可します（例: sudo ufw allow 8000/tcp 24）。  
* 原因2: ネットワーク遅延とVSCodeのタイムアウト。  
  VPN 経由や海外拠点への接続など、ネットワーク遅延（レイテンシ）が非常に大きい環境では、VSCode デバッガのデフォルトの接続タイムアウト時間（例: 3000ms 5）が短すぎて、接続が成功する前にタイムアウトしてしまうことがあります 31。  
  * **解決策:** launch.json の timeout 値を、十分な長さ（例: 30000 や 60000 ミリ秒）に延長します 5。

#### **体系的診断フロー**

1. **[サーバー側]** Tomcat サーバーに SSH などでログインし、netstat -an | grep 8000（または JPDA_ADDRESS のポート）を実行します。0.0.0.0:8000 または *:8000 が LISTEN 状態であることを確認します 24。  
   * 127.0.0.1:8000 で LISTEN していた場合 → **ケースA（address バインディングミス）** です。setenv.sh を修正してください。  
2. **[クライアント側]** VSCode を実行しているマシン（ローカルマシン）のターミナルから、telnet <server_ip> 8000 24 または nc -zv <server_ip> 8000 を実行します。  
3. telnet が "Connection refused" と即座に返してきた場合 → **ケースA（address バインディングミス）** です。（netstat の確認が漏れています）。  
4. telnet が応答なくハングアップし、最終的に "Timeout" と表示された場合 → **ケースB（ファイアウォール）** です。サーバーのファイアウォール設定を確認してください。  
5. telnet が即座に接続できた（画面が真っ黒になるか、接続成功のメッセージが出る）場合 → ネットワークとサーバー設定は正常です。VSCode が失敗する原因は、**ケースB（VSCodeのtimeout値）** であるか、launch.json の hostName や port のタイプミスです。

### **5.2. デバッグ開始後：「Source code does not match the bytecode」**

* **エラーメッセージ:** Source code does not match the bytecode 11  
* **現象:** Tomcat への接続には成功し、ブレイクポイントで停止もするが、VSCode が該当のソースコードを開いた際にこの警告を表示し、ステップ実行が期待通りに動作しない（ハイライトが予期しない場所に飛ぶ、変数が表示できないなど）。  
* **意味:** このエラーはただ一つの事実を示しています。現在 VSCode が開いているソースコード（.java ファイル）と、Tomcat が実行しているバイトコード（.class ファイル）の**バージョンが一致していない**、つまり「古い」か「異なる」コードを見ている、ということです 11。

この不一致が発生する原因は、主に3つあります。

1. 原因1 (ビルド・デプロイ不一致):  
   最も一般的な原因です。開発者がローカルでソースコード（.java）を変更した後、プロジェクトのビルド（例: mvn clean install 11）や、ビルドされた成果物（.war や .class ファイル）の Tomcat への再デプロイを忘れています 11。開発者の手元にあるソースは最新ですが、サーバーが実行しているのは古いバイトコードのままです。  
   * Tomcat のキャッシュ（work や temp ディレクトリ）や、Maven のローカルリポジトリ（.m2）が古いバージョンの JAR を掴んでいる可能性も考えられます 48。  
2. 原因2 (ソースマッピング不一致):  
   サーバー上のバイトコードは最新でも、VSCode の launch.json 設定に不備があるケースです。sourcePaths 5 が設定されていないか、間違ったローカルディレクトリ（例: 別のブランチや古いバージョンのソース）を指しています。デバッガは停止しましたが、VSCode がどのローカルファイルを開けばよいか分からないか、間違ったファイルを開いています。  
3. 原因3 (難読化):  
   デプロイ用のビルドプロセスが、ProGuard や R8 (minifyEnabled=true) によって難読化・最適化されています 49。このプロセスにより、ソースコードの行番号情報や変数名が失われるため、デバッガはバイトコードとソースコードをマッピングできなくなります。

#### **解決チェックリスト**

1. クリーン＆再デプロイ:  
   a. VSCode (またはターミナル) で mvn clean install (または gradle clean build) を実行し、プロジェクトをクリーンビルドします 11。  
   b. Tomcat サーバーを停止します。  
   c. Tomcat の work および temp ディレクトリの内容を完全に削除し、古いコンパイル済みJSPや一時ファイルを消去します 48。  
   d. (a) でビルドした最新の .war ファイルを webapps ディレクトリにコピー（再デプロイ）します。  
   e. Tomcat サーバーを再起動します。  
   f. VSCode でデバッグセッションを再アタッチします。  
2. sourcePaths の確認:  
   launch.json を開き、sourcePaths のエントリが、デバッグ対象モジュールの src/main/java ディレクトリを正しく指していることを確認します 30。  
3. 難読化の無効化:  
   デバッグ対象のビルド（.war）を作成する際、pom.xml や build.gradle の設定を確認し、難読化（minifyEnabled など）が無効になっていることを確認します 49。  
4. IDEキャッシュのクリア:  
   VSCode のコマンドパレット (Ctrl+Shift+P) で Java: Clean the Java language server workspace を実行し、Java 言語サーバーのキャッシュをクリアします。これにより、VSCode が保持しているプロジェクト構造のインデックスが再構築されます 11。

## **第6章: 結論と推奨プラクティス**

本ガイドでは、Visual Studio Code を使用して Apache Tomcat 上の Java アプリケーションをリモートデバッグするための技術的な基礎と、2つの主要な実践手法、および重大なトラブルシューティングについて詳述しました。

### **手法の総括**

VSCode による Tomcat のリモートデバッグは、強力かつ柔軟に実現可能です。

1. 手法1: 手動アタッチ (launch.json):  
   Tomcat 側で setenv.sh を設定し 19、VSCode 側で launch.json を設定する 5、最も伝統的で柔軟な方法です。ネットワーク構成が複雑なリモートサーバーへの接続に適しています。  
2. 手法2: 統合拡張機能 (Community Server Connectors):  
   Red Hat が提供する Community Server Connectors 36 を使用し、VSCode の GUI 内でサーバーの起動、デプロイ、デバッグを完結させるモダンな方法です。ローカル開発サイクルに最適です 38。

### **エキスパートによる推奨事項**

開発シナリオに基づき、以下の手法を使い分けることを強く推奨します。

* ローカル開発サイクル（個人開発環境）:  
  手法2: Community Server Connectors の使用を推奨します。launch.json や setenv.sh の手動設定を一切不要にし 38、ビルド・デプロイ・デバッグのサイクルを IDE 内でシームレスに実行できます。これにより、設定ミスやデプロイ忘れによる「ソース不一致」エラー 11 を根本的に防止でき、開発生産性が最大化されます。  
* リモート環境（開発、ステージング、コンテナ環境）:  
  手法1: 手動アタッチ が唯一かつ最適な選択肢です。共有のリモートサーバーや、Docker/Kubernetes 上のコンテナ 41 内で既に稼働中の Tomcat に接続する場合、この手法が必要となります。成功の鍵は、サーバー側の setenv.sh による JPDA_ADDRESS の設定（*:port または 0.0.0.0:port） 24 と、サーバーOSおよびネットワークのファイアウォール設定（ポート開放） 31 にあります。

### **成功への最終チェックリスト**

VSCode での Tomcat リモートデバッグを成功させるため、以下の6点を確認してください。

1. **** Extension Pack for Java がインストールされ、Java プロジェクトが正しく認識されていますか？ 8  
2. **** JPDA が有効化され、address オプションがリモート接続を許可する *:port または 0.0.0.0:port になっていますか？（127.0.0.1 ではありませんか？） 24  
3. **[Network]** Tomcat サーバーのファイアウォール（OS, クラウド）は、その JPDA port への着信 TCP 接続を許可していますか？ 31  
4. **** launch.json の hostName と port は、Tomcat サーバーの IP および JPDA ポートと正確に一致していますか？ 5  
5. **** Tomcat にデプロイされているバイトコード（.class, .war）は、VSCode で開いているローカルのソースコード（.java）と*完全に*一致していますか？（ビルド/デプロイは最新ですか？） 11  
6. **** launch.json の sourcePaths は、その最新のソースコードが格納されているローカルディレクトリ（src/main/java など）を正しく指していますか？ 30

#### **引用文献**

1. Eclipse Community Forums: Eclipse Platform » Remote debugging into Tomcat/Linux/x64 from Win7 x64, 11月 17, 2025にアクセス、 [https://www.eclipse.org/forums/index.php/t/162363/](https://www.eclipse.org/forums/index.php/t/162363/)  
2. Eclipse debug issue : Failed to connect to remote VM. Connection refused. Connection refused - PTC Community, 11月 17, 2025にアクセス、 [https://community.ptc.com/t5/ThingWorx-Developers/Eclipse-debug-issue-Failed-to-connect-to-remote-VM-Connection/td-p/892102](https://community.ptc.com/t5/ThingWorx-Developers/Eclipse-debug-issue-Failed-to-connect-to-remote-VM-Connection/td-p/892102)  
3. Unable to connect to tomcat 9 for remote debugging via eclipse - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/74261070/unable-to-connect-to-tomcat-9-for-remote-debugging-via-eclipse](https://stackoverflow.com/questions/74261070/unable-to-connect-to-tomcat-9-for-remote-debugging-via-eclipse)  
4. Remote debugging Tomcat with Eclipse - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/3835612/remote-debugging-tomcat-with-eclipse](https://stackoverflow.com/questions/3835612/remote-debugging-tomcat-with-eclipse)  
5. Running and debugging Java - Visual Studio Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/java/java-debugging](https://code.visualstudio.com/docs/java/java-debugging)  
6. Debugger for Java - Visual Studio Marketplace, 11月 17, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-debug)  
7. Running and debugging Java - vscode-docs-arc, 11月 17, 2025にアクセス、 [https://vscode-docs-arc.readthedocs.io/en/latest/java/java-debugging/](https://vscode-docs-arc.readthedocs.io/en/latest/java/java-debugging/)  
8. Extension Pack for Java - Visual Studio Marketplace, 11月 17, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack](https://marketplace.visualstudio.com/items?itemName=vscjava.vscode-java-pack)  
9. Getting Started with Java in VS Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/java/java-tutorial](https://code.visualstudio.com/docs/java/java-tutorial)  
10. How to Use Visual Studio Code With Java? Baeldung, 11月 17, 2025にアクセス、 [https://www.baeldung.com/java-visual-studio-code](https://www.baeldung.com/java-visual-studio-code)  
11. java - 'Source code does not match the bytecode' when debugging ..., 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/39990752/source-code-does-not-match-the-bytecode-when-debugging-on-a-device](https://stackoverflow.com/questions/39990752/source-code-does-not-match-the-bytecode-when-debugging-on-a-device)  
12. 'Source code does not match the bytecode' use IDEA debug JdbcTemplate - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/45807888/source-code-does-not-match-the-bytecode-use-idea-debug-jdbctemplate](https://stackoverflow.com/questions/45807888/source-code-does-not-match-the-bytecode-use-idea-debug-jdbctemplate)  
13. Managing Java Projects in VS Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/java/java-project](https://code.visualstudio.com/docs/java/java-project)  
14. Using setenv.sh to configure tomcat env AND Debugging - Liferay.Dev, 11月 17, 2025にアクセス、 [https://liferay.dev/b/using-setenv-sh-to-configure-tomcat-env-and-debugging](https://liferay.dev/b/using-setenv-sh-to-configure-tomcat-env-and-debugging)  
15. How to start debug mode from command prompt for apache tomcat server? - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/16689274/how-to-start-debug-mode-from-command-prompt-for-apache-tomcat-server](https://stackoverflow.com/questions/16689274/how-to-start-debug-mode-from-command-prompt-for-apache-tomcat-server)  
16. eclipse - debugging java application deployed in tomcat - Stack ..., 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/7677060/debugging-java-application-deployed-in-tomcat](https://stackoverflow.com/questions/7677060/debugging-java-application-deployed-in-tomcat)  
17. How to enable Tomcat debugging - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/45307947/how-to-enable-tomcat-debugging](https://stackoverflow.com/questions/45307947/how-to-enable-tomcat-debugging)  
18. How do I edit catalina.bat to make remote debugging work ? (Tomcat forum at Coderanch), 11月 17, 2025にアクセス、 [https://coderanch.com/t/691509/application-servers/edit-catalina-bat-remote-debugging](https://coderanch.com/t/691509/application-servers/edit-catalina-bat-remote-debugging)  
19. How can I configure TomCat Java options in a config file? - Server Fault, 11月 17, 2025にアクセス、 [https://serverfault.com/questions/79641/how-can-i-configure-tomcat-java-options-in-a-config-file](https://serverfault.com/questions/79641/how-can-i-configure-tomcat-java-options-in-a-config-file)  
20. Remote Debugging of Java Applications and Debugging Tomcat-Deployed Web Apps using IntelliJ IDEA by Shamodya Hashantha Medium, 11月 17, 2025にアクセス、 [https://medium.com/@shamodya/remote-debugging-of-java-applications-and-debugging-tomcat-deployed-web-apps-using-intellij-idea-fa3d6e5aedfb](https://medium.com/@shamodya/remote-debugging-of-java-applications-and-debugging-tomcat-deployed-web-apps-using-intellij-idea-fa3d6e5aedfb)  
21. How to Remotely Debug Application Running on Tomcat From Within Intellij IDEA, 11月 17, 2025にアクセス、 [https://trifork.nl/blog/how-to-remotely-debug-application-running-on-tomcat-from-within-intellij-idea/](https://trifork.nl/blog/how-to-remotely-debug-application-running-on-tomcat-from-within-intellij-idea/)  
22. Debugging with JPDA and Apache Tomcat - JVM Host, 11月 17, 2025にアクセス、 [https://www.jvmhost.com/articles/debugging-with-jpda-and-apache-tomcat/](https://www.jvmhost.com/articles/debugging-with-jpda-and-apache-tomcat/)  
23. Starting Tomcat with remote debugging (jdwp) when installed as a windows service, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/1406320/starting-tomcat-with-remote-debugging-jdwp-when-installed-as-a-windows-service](https://stackoverflow.com/questions/1406320/starting-tomcat-with-remote-debugging-jdwp-when-installed-as-a-windows-service)  
24. java - Remote debugging(NOT localhost) tomcat using eclipse ..., 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/53651215/remote-debuggingnot-localhost-tomcat-using-eclipse-connection-refused-from-re](https://stackoverflow.com/questions/53651215/remote-debuggingnot-localhost-tomcat-using-eclipse-connection-refused-from-re)  
25. Java remote debugging (JPDA) not working for me in Tomcat 9 - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/54373166/java-remote-debugging-jpda-not-working-for-me-in-tomcat-9](https://stackoverflow.com/questions/54373166/java-remote-debugging-jpda-not-working-for-me-in-tomcat-9)  
26. How to run Apache Tomcat 8 in debug mode? - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/30011505/how-to-run-apache-tomcat-8-in-debug-mode](https://stackoverflow.com/questions/30011505/how-to-run-apache-tomcat-8-in-debug-mode)  
27. Using VS Code to Debug Java Applications, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/blogs/2017/09/28/java-debug](https://code.visualstudio.com/blogs/2017/09/28/java-debug)  
28. Java code in vscode not respecting breakpoints set in another thread, but it will break if set in the main thread - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/75304937/java-code-in-vscode-not-respecting-breakpoints-set-in-another-thread-but-it-wil](https://stackoverflow.com/questions/75304937/java-code-in-vscode-not-respecting-breakpoints-set-in-another-thread-but-it-wil)  
29. Running and debugging Java - Visual Studio Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/java/java-debugging#_attach-to-a-remote-java-application](https://code.visualstudio.com/docs/java/java-debugging#_attach-to-a-remote-java-application)  
30. Attach source in remote debug · Issue #729 · microsoft/vscode-java-debug - GitHub, 11月 17, 2025にアクセス、 [https://github.com/microsoft/vscode-java-debug/issues/729](https://github.com/microsoft/vscode-java-debug/issues/729)  
31. eclipse - Tomcat : Unable to connect for remote debugging - Stack ..., 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/13410927/tomcat-unable-to-connect-for-remote-debugging](https://stackoverflow.com/questions/13410927/tomcat-unable-to-connect-for-remote-debugging)  
32. Is there a way to debug Tomcat Java application from Visual Studio Code - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/44628572/is-there-a-way-to-debug-tomcat-java-application-from-visual-studio-code](https://stackoverflow.com/questions/44628572/is-there-a-way-to-debug-tomcat-java-application-from-visual-studio-code)  
33. Tomcat for Java - Visual Studio Marketplace, 11月 17, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=adashen.vscode-tomcat](https://marketplace.visualstudio.com/items?itemName=adashen.vscode-tomcat)  
34. adashen/vscode-tomcat - GitHub, 11月 17, 2025にアクセス、 [https://github.com/adashen/vscode-tomcat](https://github.com/adashen/vscode-tomcat)  
35. Community Server Connectors - Visual Studio Marketplace, 11月 17, 2025にアクセス、 [https://marketplace.visualstudio.com/items?itemName=redhat.vscode-community-server-connector](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-community-server-connector)  
36. Working with Application Servers in VS Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/java/java-tomcat-jetty](https://code.visualstudio.com/docs/java/java-tomcat-jetty)  
37. Deploying projects to Apache Felix, Tomcat, and Karaf in VS Code ..., 11月 17, 2025にアクセス、 [https://developers.redhat.com/blog/2020/04/09/deploying-projects-to-apache-felix-tomcat-and-karaf-in-vs-code](https://developers.redhat.com/blog/2020/04/09/deploying-projects-to-apache-felix-tomcat-and-karaf-in-vs-code)  
38. How to start a Tomcat 8.5 server on VSC using Community Server Connector extension, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/74388409/how-to-start-a-tomcat-8-5-server-on-vsc-using-community-server-connector-extensi](https://stackoverflow.com/questions/74388409/how-to-start-a-tomcat-8-5-server-on-vsc-using-community-server-connector-extensi)  
39. Run and Debug Java Web Application in Tomcat using VS Code in 2025 - YouTube, 11月 17, 2025にアクセス、 [https://www.youtube.com/watch?v=lO-pavgTewo](https://www.youtube.com/watch?v=lO-pavgTewo)  
40. How to attach debuger to a Community Server Connector / Tomcat #1240 - GitHub, 11月 17, 2025にアクセス、 [https://github.com/microsoft/vscode-java-debug/discussions/1240](https://github.com/microsoft/vscode-java-debug/discussions/1240)  
41. Run and Debug Java Web Application in Tomcat using VS Code - YouTube, 11月 17, 2025にアクセス、 [https://www.youtube.com/watch?v=RiPot1ne8rI](https://www.youtube.com/watch?v=RiPot1ne8rI)  
42. How To Use Visual Studio Code for Remote Development via the Remote-SSH Plugin, 11月 17, 2025にアクセス、 [https://www.digitalocean.com/community/tutorials/how-to-use-visual-studio-code-for-remote-development-via-the-remote-ssh-plugin](https://www.digitalocean.com/community/tutorials/how-to-use-visual-studio-code-for-remote-development-via-the-remote-ssh-plugin)  
43. VSCode Remote development on Digitalocean by Narongsak Keawmanee Medium, 11月 17, 2025にアクセス、 [https://medium.com/@klogic/vscode-remote-development-on-digitalocean-d7d65e1656ef](https://medium.com/@klogic/vscode-remote-development-on-digitalocean-d7d65e1656ef)  
44. Debug code with Visual Studio Code, 11月 17, 2025にアクセス、 [https://code.visualstudio.com/docs/editor/debugging](https://code.visualstudio.com/docs/editor/debugging)  
45. Problem with simple remote debug testcase (Java in General forum at Coderanch), 11月 17, 2025にアクセス、 [https://coderanch.com/t/641658/java/simple-remote-debug-testcase](https://coderanch.com/t/641658/java/simple-remote-debug-testcase)  
46. Remote Debugging - Unable to connect to the localhost:8080 - IDEs Support (IntelliJ Platform) JetBrains, 11月 17, 2025にアクセス、 [https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000399204-Remote-Debugging-Unable-to-connect-to-the-localhost-8080](https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000399204-Remote-Debugging-Unable-to-connect-to-the-localhost-8080)  
47. eclipse: remote debugging a tomcat server behind a firewall - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/6717396/eclipse-remote-debugging-a-tomcat-server-behind-a-firewall](https://stackoverflow.com/questions/6717396/eclipse-remote-debugging-a-tomcat-server-behind-a-firewall)  
48. VS Code debugger ignores code changes - IDE & Build - openHAB Community, 11月 17, 2025にアクセス、 [https://community.openhab.org/t/vs-code-debugger-ignores-code-changes/122755](https://community.openhab.org/t/vs-code-debugger-ignores-code-changes/122755)  
49. Source code does not match the bytecode for Android's View.java - Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/63556563/source-code-does-not-match-the-bytecode-for-androids-view-java](https://stackoverflow.com/questions/63556563/source-code-does-not-match-the-bytecode-for-androids-view-java)  
50. Source code does not match the bytecode OPC UA SDK for Java - Prosys Forum, 11月 17, 2025にアクセス、 [https://forum.prosysopc.com/forum/opc-ua-java-sdk/source-code-does-not-match-the-bytecode/](https://forum.prosysopc.com/forum/opc-ua-java-sdk/source-code-does-not-match-the-bytecode/)
