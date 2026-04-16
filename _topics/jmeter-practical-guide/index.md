---
audio: /share-deepresearch/assets/audio/jmeter-practical-guide.mp3
category: engineering
date: 2025-09-02
description: JMeterを使用してブラウザ操作のログから堅牢なテストシナリオを作成する方法を解説します。
ga4_metrics:
  avgSessionDuration: 242.21074523921567
  pageViews: 247
  users: 148
layout: topic
prompt: JMeterでブラウザ操作のログを用いてログインから特定のページアクセスを確認するテストシナリオを作成したい。プロキシ経由で取得したログから効率良くテストシナリオを作成するポイントや実装時に良く発生する問題を調査して欲しい。
supplementary_materials:
- title: JMeter：ブラウザ操作ログから堅牢なテストシナリオを作成
  url: /share-deepresearch/topics/jmeter-practical-guide/infographic.html
tags:
- テストツール
title: JMeterプロキシ記録機能を用いた実践的テストシナリオ構築ガイド
video: /share-deepresearch/assets/video/jmeter-practical-guide.mp4
---

# **JMeterプロキシ記録機能を用いた実践的テストシナリオ構築ガイド**

## **序章：プロキシ録画によるシナリオ作成の現実と課題**

Apache JMeterが提供するHTTP(S) Test Script Recorderは、実際のブラウザ操作を記録し、それを基にテストシナリオの雛形を自動生成する強力な機能です 1。特にパフォーマンステストの初学者にとって、この機能はテスト計画を迅速に立ち上げるための魅力的な出発点となります。しかし、その手軽さとは裏腹に、記録されたスクリプトがそのままの状態で実用的なテストとして機能することは稀です。この「理想と現実のギャップ」こそが、多くのテスターが直面する最初の壁となります。

現代のWebアプリケーションは、セキュリティの強化とリッチなユーザー体験の提供を目的として、極めて動的かつ複雑な通信を行っています。具体的には、ログイン状態を維持するためのセッション管理（Cookie）、不正なリクエストを防ぐためのCSRF対策（動的トークン）、そしてページ遷移を伴わずにサーバーと通信を行う非同期通信（AJAX）などが標準的に実装されています 2。これらの技術は、ユーザーが意識することなくシームレスな操作を可能にする一方で、単純な「記録と再生（Record and Replay）」というテストモデルを根本から覆します。JMeterはプロトコルレベルで動作するツールであり、ブラウザのようにJavaScriptを実行して動的なコンテンツを解釈するわけではないため、記録された静的な通信ログを再生するだけでは、アプリケーションの動的な振る舞いに追従できないのです 4。

本レポートは、このギャップを埋めるための専門的な技術ガイドです。単なる操作手順の羅列に留まらず、記録された生のデータをいかにして信頼性の高いテストシナリオへと昇華させるか、そのための体系的なプロセスを解説します。具体的には、記録の準備段階から始まり、記録データの最適化、ログイン成功の鍵となる動的パラメータの処理、そして頻出する問題に対するデバッグ戦略とシナリオの高度化までを網羅します。

このプロセスを理解する上で最も重要なのは、JMeterによるシナリオ作成の本質が、ユーザー操作の「模倣」ではなく、クライアント（ブラウザ）とサーバー間で交わされる通信プロトコルの「解析と再実装」であるという認識です。記録機能は、そのプロトコルを覗き見るための強力なツールに過ぎません。この視点を持つことで、なぜ単純な記録が失敗し、どのような追加作業が不可欠となるのかを根本的に理解し、あらゆるWebアプリケーションに対して堅牢なテストシナリオを構築する能力を身につけることができるでしょう。

---

## **第1部：テストシナリオ作成の土台作り \- 正確なブラウザ操作の記録**

信頼性の高いテストシナリオは、正確な記録から始まります。このセクションでは、JMeterのHTTP(S) Test Script Recorderを正しく設定し、ブラウザの通信を確実にキャプチャするための foundational な手順を詳述します。特に、現代のWebサイトで必須となるHTTPS通信の記録は、多くのユーザーが最初につまずくポイントであり、そのメカニズムと対策を深く理解することが重要です。

### **1.1. HTTP(S) Test Script Recorderのセットアップ**

効率的なシナリオ作成の第一歩は、適切なテスト計画の雛形を用意することです。JMeterのテンプレート機能を利用することで、必要な要素が予め配置された状態で作業を開始できます。

1. JMeterを起動し、メニューバーから \[File\] \-\> を選択します。  
2. テンプレート選択ダイアログで \`\` を選択し、\[Create\] ボタンをクリックします 1。

これにより、スレッドグループ、HTTP(S) Test Script Recorder、結果をツリーで表示リスナーなど、記録に必要な基本的な要素が一式含まれたテスト計画が生成されます。

次に、HTTP(S) Test Script Recorderの主要な設定を行います。

* **Port**: JMeterがプロキシサーバーとして待ち受けるポート番号を指定します。デフォルトは 8888 ですが、他のアプリケーションと競合しない任意のポートに変更可能です 6。  
* **Target Controller**: 記録されたHTTPリクエスト（サンプラー）が配置される場所を指定します。テンプレートを使用した場合、Test Plan \> Thread Group \> Recording Controller が自動的に設定されており、記録された操作がこのコントローラ配下に整理されます 6。

### **1.2. ブラウザとJMeterの連携：プロキシ設定**

JMeterがブラウザの通信を傍受（インターセプト）できるように、ブラウザ側の設定を変更します。これにより、ブラウザから送信されるすべてのHTTP/HTTPSリクエストは、一度JMeterを経由してから目的のサーバーに到達するようになります 7。

1. 使用するブラウザ（例：Firefox）のネットワーク設定を開きます。  
2. プロキシ設定を「手動でプロキシを設定する」に変更します。  
3. HTTPプロキシのホストとして localhost（またはJMeterを実行しているマシンのIPアドレス）、ポートにJMeterで設定したポート番号（例：8888）を入力します 1。  
4. 「すべてのプロトコルでこのプロキシを使用する」オプションを有効にします 1。

この設定はテスト記録時のみ必要です。記録が完了したら、必ず元の設定に戻してください。

### **1.3. HTTPS通信の壁を越える：SSL証明書のインポート**

現代のWebサイトのほとんどはHTTPSで通信しており、これを記録するためには追加のステップが必要です。このステップは、JMeterの動作原理を理解する上で最初の重要な関門となります。

問題の背景  
HTTPS通信はSSL/TLSによって暗号化されています。JMeterがこの通信内容を記録するためには、ブラウザとサーバーの間に「中間者（Man-in-the-Middle）」として割り込み、通信を一度復号（解読）する必要があります。しかし、ブラウザはセキュリティ上の理由から、通信相手が正規のサーバーではなく、信頼できない第三者（この場合はJMeter）であることを検知し、接続を拒否します。これがSSL証明書エラーの正体です 8。  
解決策：JMeterのルートCA証明書の信頼  
この問題を解決するには、ブラウザに対して「このテスト中に限り、JMeterという中間者を特別に信頼する」と明示的に許可を与える必要があります。そのための手順が、JMeterが生成する一時的なルートCA証明書のインポートです。

1. JMeterのHTTP(S) Test Script Recorder画面で \`\` ボタンを初めてクリックすると、JMeterのbinディレクトリ内に ApacheJMeterTemporaryRootCA.crt という証明書ファイルが自動的に生成されます 1。  
2. この .crt ファイルを、使用するブラウザの証明書ストアに「信頼されたルート証明機関」としてインポートします 7。

**Firefoxでのインポート手順例**:

1. Firefoxの \[設定\] を開き、「プライバシーとセキュリティ」セクションに移動します。  
2. \[証明書を表示...\] ボタンをクリックします。  
3. \[認証局証明書\] タブを選択し、\[インポート...\] ボタンをクリックします。  
4. binディレクトリにある ApacheJMeterTemporaryRootCA.crt ファイルを選択します。  
5. 表示されるダイアログで、「この認証局によるウェブサイトの識別を信頼する」にチェックを入れ、\[OK\] をクリックします 7。

この証明書の有効期間はデフォルトで7日間です。期限が切れた場合は、binディレクトリ内の証明書ファイルを削除し、再度レコーダーを起動して再生成・再インポートする必要があります 8。

関連エラーと対策  
javax.net.ssl.SSLException などのSSL関連エラーが発生した場合、証明書のインポート不備以外にも、JMeterを実行しているJavaのバージョンが古いことが原因である可能性があります。特に古い暗号化方式にしか対応していないJava環境では、現代的なサーバーとのTLSハンドシェイクに失敗することがあります。Java 8以降の最新バージョンを使用することが推奨されます 10。また、対象サーバー側の証明書チェーンに問題がある場合もエラーが発生することがあります 11。

---

## **第2部：効率化の鍵 \- 録画データのクリーンアップと構造化**

ブラウザ操作を記録した直後のデータは、テストシナリオとして利用するには冗長で、本質的でない情報（ノイズ）を大量に含んでいます。このセクションでは、記録されたデータを効率的に整理し、分析しやすく、かつメンテナンス性の高い構造へと変換するための二つの重要なテクニック、「フィルタリング」と「グループ化」について詳述します。これらの工程は、単なるデータ整理ではなく、テストの目的、すなわち「何を測定したいのか」を明確に定義する設計行為そのものです。

### **2.1. ノイズの除去：リクエストフィルタリングによるシナリオの純度向上**

課題  
デフォルト設定のまま記録を行うと、Webページの表示に必要なすべてのコンポーネントが記録されます。これには、アプリケーションの性能とは直接関係のない静的リソース（画像、CSS、JavaScriptファイル）や、外部のサードパーティサービス（Google Analytics、広告配信ネットワーク、SNSウィジェットなど）へのリクエストが含まれます 7。これらの「ノイズ」は、テストスクリプトを不必要に複雑にし、本来測定したいサーバーサイドのパフォーマンス指標を歪める原因となります。  
解決策：Requests Filteringの活用  
HTTP(S) Test Script Recorderには、記録するリクエストを選択的にフィルタリングする機能が備わっています。記録を開始する前にこの設定を適切に行うことで、生成されるシナリオの純度を劇的に高めることができます。

* URL Patterns to Exclude（除外パターン）:  
  この機能は、特定のパターンに一致するURLのリクエストを記録対象から除外します。静的リソースを除外する際に最も効果的です 7。正規表現を用いることで、柔軟なフィルタリングが可能です。  
  * 推奨設定例: 以下の正規表現をAddボタンで追加することで、一般的な静的ファイルの拡張子を持つリクエストを一括で除外できます。  
    (?i).\*\\.(bmp|css|js|gif|ico|jpe?g|png|swf|woff|woff2|svg)  
    (i)は、大文字・小文字を区別しないことを意味します。  
* URL Patterns to Include（包含パターン）:  
  こちらは、特定のパターンに一致するURLのリクエストのみを記録対象とします。テスト対象のアプリケーションがホストされているドメインのみを指定することで、意図しないすべての外部ドメインへの通信を排除できます 7。  
  * 推奨設定例: テスト対象のドメインが example.com の場合、以下のように設定します。  
    .\*\\.example\\.com.\*

これらのフィルタリングは、テストのスコープを「サーバーサイドの動的コンテンツ生成能力」に絞り込むための重要なステップです。クライアントサイドのレンダリングや静的コンテンツの配信能力は、通常、パフォーマンステストの主目的とは異なるため、これらを意図的に除外することで、より正確で意味のある測定結果を得ることができます。

### **2.2. 操作の論理的グループ化：トランザクションコントローラ**

目的  
ユーザーが行う一連の操作、例えば「商品を検索し、詳細ページを表示し、カートに入れる」という流れは、技術的には複数のHTTPリクエストから構成されています。しかし、パフォーマンスを評価する上で重要なのは、個々のリクエストの応答時間だけでなく、この一連の操作全体が完了するまでの時間、すなわちユーザー体験に基づいた処理時間です。トランザクションコントローラは、これらの複数のリクエストを一つの論理的な単位（トランザクション）としてグループ化し、その総実行時間を測定するための要素です 14。  
**設定方法**

1. スレッドグループを右クリックし、追加 \-\> ロジックコントローラ \-\> トランザクションコントローラを選択します。  
2. 名前フィールドに、その操作を表す分かりやすい名前（例：「01\_ログイン」「02\_商品検索」）を付けます。  
3. 関連する一連のHTTPリクエストサンプラーを、このトランザクションコントローラの下にドラッグ＆ドロップで移動させます。

重要オプション：Generate parent sample  
このチェックボックスを有効にすることが強く推奨されます 14。有効にすると、  
集計レポートなどのリスナーで、トランザクションコントローラ配下の個々のリクエスト結果は表示されず、トランザクション全体（親サンプル）の結果のみが一行にまとめて表示されます。これにより、レポートが簡潔になり、「ログイン処理の平均応答時間は1.5秒」といった、ビジネスレベルで意味のある分析が可能になります。

記録時の自動グループ化  
HTTP(S) Test Script RecorderのGrouping設定でPut each group in a new transaction controllerを選択すると、記録中にユーザーの一回の操作（クリックなど）によって発生した複数のリクエストが、自動的に一つのトランザクションコントローラにまとめられます 14。これは、記録後の手作業を大幅に削減する非常に便利な機能です。  
これらの構造化作業を通じて、テストシナリオは単なる通信ログの羅列から、ユーザーの行動フローを忠実に再現した、分析可能でメンテナンス性の高い設計図へと進化します。

**Table 1: HTTP(S) Test Script Recorder 推奨初期設定**

| 設定項目 | タブ | 推奨値/設定 | 理由 |
| :---- | :---- | :---- | :---- |
| Port | Global Settings | 8888 (または未使用のポート) | 標準的な初期値であり、覚えやすい。 |
| Target Controller | Test Plan Content | Test Plan \> Thread Group \> Recording Controller | 記録されたステップを特定のコントローラ配下に整理し、主となるテストロジックから分離する。 |
| Grouping | Test Plan Content | Put each group in a new transaction controller | ユーザーの単一アクションによってトリガーされたリクエスト群を自動的にグループ化し、可読性とメトリクスの質を向上させる。 |
| URL Patterns to Exclude | Requests Filtering | \`(?i).\*.(css | js |
| URL Patterns to Include | Requests Filtering | .\*\\.your-target-domain\\.com.\* | テスト対象を自社のアプリケーションに限定し、外部の解析ツールや広告などへのリクエストをすべて除外する。 |

---

## **第3部：最重要課題 \- ログイン処理を成功させるための核心技術**

記録されたシナリオ、特にログインを含むものが再生時に失敗する最大の理由は、Webアプリケーションの「動的な」性質にあります。サーバーは、セキュリティを確保し、ユーザーごとに状態を管理するために、アクセスごとに変化する情報をやり取りします。このセクションでは、この動的な振る舞いに追従し、ログイン処理を成功させるための3つの核心技術、「セッション維持」「動的パラメータの相関化」「非同期通信への対応」について、具体的な実装方法と共に詳述します。これらの技術をマスターすることが、実用的なテストシナリオを作成する上で最も重要です。

### **3.1. セッションの維持：HTTPクッキーマネージャ**

役割と重要性  
HTTPプロトコル自体はステートレスであり、個々のリクエストは互いに独立しています。サーバーが「どのリクエストがどのユーザーからのものか」を識別し、ログイン状態を維持するために用いるのがCookieです。サーバーはログイン成功時にセッションIDを含むCookieをレスポンスで返し、ブラウザは以降のリクエストでそのCookieを送信することで、自身を証明します。  
HTTPクッキーマネージャは、このブラウザの動作をJMeterで自動的にシミュレートするための要素です 16。スレッドグループ配下に追加するだけで、サーバーから受信したCookieをスレッドごとに管理し、後続のリクエストに自動的に付与してくれます 6。

設定  
通常は、スレッドグループを右クリックし、追加 \-\> 設定エレメント \-\> HTTPクッキーマネージャを選択して追加するだけで十分です 16。  
重要オプション：Clear cookies each iteration?  
このオプションは、負荷テストのシナリオを定義する上で極めて重要です。「繰り返しごとにクッキーを破棄しますか？」にチェックを入れると、スレッド（仮想ユーザー）がループ処理を行うたびに、保存されているCookieがすべてクリアされます 18。これは、ループの各反復が「新しいユーザーによる初回アクセス」としてシミュレートされることを意味し、ログインシナリオでは通常、この設定が推奨されます。チェックを外した場合、同じユーザーがセッションを維持したまま繰り返し操作を行うシナリオとなります。

### **3.2. 動的パラメータの相関化 (Correlation)**

問題の核心  
これこそが、記録されたログインシナリオが失敗する最も一般的かつ根本的な原因です。CSRF（Cross-Site Request Forgery）攻撃を防ぐため、多くのWebアプリケーションは、フォームの送信時にCSRFトークンと呼ばれる一意で推測困難な値を要求します 2。このトークンは、フォームページが表示されるたびにサーバーで新たに生成され、HTML内の隠しフィールド（  
\<input type="hidden"\>）などに埋め込まれてクライアントに送信されます。

記録されたスクリプトには、記録時に使用された**静的で古いトークン**がハードコーディングされています。この古いトークンを使ってリクエストを再生しても、サーバーはそれを無効なリクエストとして拒否するため、ログインは失敗します 18。

解決策：相関化 (Correlation)  
相関化とは、「あるリクエストのレスポンスから動的な値を取得し、それを変数に格納して、後続のリクエストで使用する」一連のプロセスのことです 2。これにより、テスト実行時に毎回新しいトークンを動的に扱えるようになります。  
**正規表現抽出を用いた相関化のステップ・バイ・ステップ**:

1. 動的パラメータの特定:  
   結果をツリーで表示リスナーを使用し、ログイン情報をPOSTするリクエストの一つ前のリクエスト（通常はログインフォームを表示するGETリクエスト）の応答データタブを確認します。HTMLソースコードの中から、CSRFトークンを含む箇所を探します。  
   * **例**: \<input type="hidden" name="\_csrf\_token" value="Me9JgsIM8O3k2csGlJytMoQqoRvdvFARvNbNl4uf3Oo"\> 18  
2. 抽出器（Extractor）の追加:  
   トークンを返してくるリクエスト（上記のGETリクエスト）を右クリックし、追加 \-\> 後処理 \-\> 正規表現抽出 を選択します 21。  
3. 正規表現抽出の設定:  
   以下の表（Table 2）を参考に、各項目を設定します。  
4. 変数の利用:  
   ログイン情報をPOSTするリクエストのパラメータ設定画面で、記録時にハードコーディングされたトークンの値を、先ほど参照名で定義した変数に置き換えます。  
   * **例**: \_csrf\_token パラメータの値を ${csrf\_token} に変更します 21。

このプロセスにより、JMeterはテスト実行時にサーバーから送られてくる最新のトークンを自動的に取得し、次のリクエストに含めることができるようになります。

他の抽出方法  
レスポンスがJSON形式の場合はJSON Extractorが、HTML構造が複雑で正規表現が書きにくい場合はCSS Selector Extractorが有効な選択肢となります。一般的に、パフォーマンスは正規表現が最も優れています 23。

### **3.3. 非同期通信（AJAX）への対応**

課題  
ログインフォームでユーザーIDを入力した際、パスワード入力欄にフォーカスが移る前に、バックグラウンドでIDの存在チェックが行われるなど、現代のWebアプリケーションはAJAX（Asynchronous JavaScript and XML）を多用しています 3。これらのリクエストはページ全体の再読み込みを伴わないためユーザーには意識されにくいですが、サーバーとの重要な通信であり、テストシナリオには不可欠です。  
JMeterの記録機能はこれらのAJAXリクエストもHTTPリクエストとしてキャプチャしますが 4、ブラウザがこれらのリクエストを

**並列**に実行するのに対し、JMeterのデフォルトの動作は**直列**です。これにより、実際の負荷とは異なるパターンでサーバーにリクエストが送信されてしまう可能性があります 15。

解決策：Parallel Controllerの活用  
より現実に近い負荷をシミュレートするためには、これらのAJAXリクエストを並列実行させる必要があります。JMeterのプラグインマネージャからインストールできるbzm \- Parallel Controllerは、この目的のために設計されています 5。

1. JMeterプラグインマネージャ (Options \-\> Plugins Manager) を使って Parallel Controller をインストールします。  
2. テスト計画にParallel Controllerを追加します。  
3. 並列で実行させたいAJAXリクエストを、このコントローラ配下に配置します 26。

これにより、コントローラ配下のリクエストが同時に送信され、ブラウザの挙動をより忠実に再現できます。どのリクエストがAJAXであるかは、ブラウザの開発者ツールのネットワークタブで、通信タイプをXHRやFetchにフィルタリングすることで特定できます 4。

**Table 2: 動的パラメータ（CSRFトークン）相関化のための正規表現抽出設定**

| 設定項目 | 設定例 | 解説 |
| :---- | :---- | :---- |
| Apply to | Main sample only | 抽出ロジックを親サンプラーのメインレスポンスにのみ適用します。 |
| Field to check | Body | 正規表現をHTMLのレスポンスボディに対して実行することを指定します。 |
| Name of created variable（参照名） | csrf\_token | 抽出した値を格納する変数名。後続のリクエストで${csrf\_token}として参照します。 |
| Regular Expression（正規表現） | name="\_csrf\_token" value="(.+?)" | 目的の値を抽出するためのパターン。name属性で対象を絞り込み、value属性の値を(.+?)でキャプチャします。?は非貪欲マッチを意味し、最短の一致を見つけます。 |
| Template（テンプレート） | $1$ | 正規表現内の最初のキャプチャグループ（( )で囲まれた部分）の内容を変数値として使用することを指定します。 |
| Match No.（一致番号） | 1 | ページ内で最初に見つかった一致を使用します。 |
| Default Value（初期値） | CSRF\_TOKEN\_NOT\_FOUND | 抽出に失敗した場合に変数に設定される値。デバッグに極めて重要で、この値がリクエストで送信されていたら抽出が失敗していると判断できます。 |

---

## **第4部：問題解決のためのデバッグ戦略**

精心に準備したはずのシナリオが期待通りに動作しないことは、テスト作成プロセスにおいて日常茶飯事です。重要なのは、闇雲に設定を変更するのではなく、体系的なアプローチで問題の原因を特定し、解決することです。このセクションでは、科学的なデバッグプロセスを確立するための具体的な戦略と、そのために不可欠なJMeterの機能について解説します。デバッグの本質は「推測」ではなく、「観測と比較」です。

### **4.1. 体系的なトラブルシューティング**

シナリオが失敗した場合、まず原因を切り分けることから始めます。問題は大きく3つの領域に分類できます 22。

1. **対象システムのセットアップ不備**:  
   * **症状**: そもそもどのリクエストも成功しない、特定のリクエストで予期せぬエラーページが返ってくる。  
   * **原因**: テスト環境のサーバーが起動していない、デプロイに失敗している、テストに使用しているアカウントが無効化されている、テストデータ（商品など）が削除されている、などが考えられます 22。  
   * **対処法**: まずはJMeterから離れ、通常のブラウザで同じ操作が手動で成功するかを確認します。これが最も基本的で重要な切り分けです 22。  
2. **JMeter側の設定不足・不備**:  
   * **症状**: ログインが失敗する、特定のアクションがエラーになる、ループの2回目以降で失敗する。  
   * **原因**: これが最も一般的な原因であり、本レポートで解説してきたCookie管理の不備、動的パラメータの相関化失敗、必須ヘッダの欠落などが該当します。  
   * **対処法**: 次のセクションで詳述する「ブラウザとの比較分析」を徹底的に行います。  
3. **JMeterでは再現困難な処理**:  
   * **症状**: 特定の操作（例：クレジットカード情報のトークン化処理）で、ブラウザとのリクエスト差分が見つからないにも関わらず失敗する。  
   * **原因**: クライアントサイドで非常に複雑なJavaScriptロジックが実行され、その結果をサーバーに送信している場合、プロトコルレベルで動作するJMeterではそのロジックを再現できません 22。  
   * **対処法**: このような場合は、該当部分をテストシナリオから除外するか、開発チームと協力してテスト用のスタブ（代替応答を返す簡易サーバー）を用意するなどの対応が必要になります。

また、基本的な確認として、JMeterのログビューア（オプション \-\> ログビューアを表示）にエラーが出力されていないかを確認することも忘れてはなりません。CSVファイルのパス間違いや、設定値に含まれた不要な半角スペースなども、予期せぬ動作の原因となり得ます 22。

### **4.2. 「正解」との比較：結果をツリーで表示リスナーの徹底活用**

結果をツリーで表示リスナーは、単にテスト結果の成否を見るだけでなく、JMeterにおける最も強力なデバッグツールです。その真価は、JMeterが送信したリクエストとサーバーからのレスポンスを詳細に「観測」できる点にあります。

**比較分析ワークフロー**:

1. **「失敗」の観測**: JMeterでシナリオを実行し、結果をツリーで表示リスナーで赤く表示された失敗リクエストを選択します。リクエストタブを開き、JMeterが実際に送信したリクエストヘッダ、ボディ（パラメータ）、パス、Cookieなどを詳細に確認します 18。  
2. **「成功」の観測**: ブラウザの開発者ツール（F12キーで起動）のNetworkタブを開いた状態で、手動で同じ操作を成功させます。失敗したJMeterのリクエストに対応する、成功したブラウザのリクエストを選択し、その詳細（Headers, Payload, Cookiesなど）を確認します 22。  
3. **「差分」の特定**: JMeterの「失敗リクエスト」とブラウザの「成功リクエスト」を並べて、以下の観点で徹底的に比較します。  
   * **リクエストパラメータ**: 送信されているパラメータの数、名前、値は完全に一致しているか？特に、動的トークンの値が異なっている場合、相関化が失敗している可能性が高いです。  
   * **リクエストヘッダ**: Content-Type, Referer, X-Requested-With (AJAXリクエストで重要) など、必須のヘッダが欠落していないか？  
   * **Cookie**: 送信されているCookieの内容は正しいか？セッションIDは含まれているか？  
   * **URL/パス**: リダイレクトなどが正しく処理されず、意図しないURLにリクエストを送っていないか？

この「観測と比較」のプロセスを通じて、「ブラウザはX-CSRF-Tokenヘッダを送信しているが、JMeterは送信していない」といった具体的な差分が明らかになります。この差分こそが修正すべき問題点であり、推測に頼らない確実なデバッグを可能にします。

### **4.3. 変数の状態を可視化する：Debug Sampler**

相関化処理が正しく行われているかを確認する上で、Debug Samplerは非常に有効なツールです。これは、実行された時点でのJMeterの内部状態（すべての変数とプロパティの値）をスナップショットとして表示するサンプラーです 29。

使い方:  
正規表現抽出などの後処理（Post-Processor）で変数を設定した後、その変数が正しく値を取得できているか確認したい箇所にDebug Sampler（追加 \-\> Sampler \-\> Debug Sampler）を配置します。  
テスト実行後、結果をツリーで表示リスナーでDebug Samplerの応答データを見ると、csrf\_token=Me9JgsIM8O3k...のように、変数が期待通りの値で設定されているか、あるいはcsrf\_token=CSRF\_TOKEN\_NOT\_FOUNDのように、初期値のままで抽出に失敗しているか、が一目瞭然となります 29。

### **4.4. アサーションによる検証**

デバッグが完了し、シナリオが正常に動作するようになったら、その状態が維持されていることを自動的に検証するためにアサーションを追加します。応答アサーション（追加 \-\> アサーション \-\> 応答アサーション）を使い、ログイン成功後のページに必ず含まれるべきテキスト（例：「ようこそ、〇〇さん」「ログアウト」ボタン）が存在するかをチェックします 18。これにより、将来的なアプリケーションの変更でシナリオが意図せず失敗するようになった場合に、早期に問題を検知できます。

**Table 3: ログインシナリオ実行時エラーのトラブルシューティングガイド**

| 症状 | 考えられる原因 | 調査・デバッグ方法 |
| :---- | :---- | :---- |
| ログイン後のページで「セッションがありません」等のエラーが表示される。 | 1\. HTTPクッキーマネージャが追加されていない。 2\. Cookieが正しく送信されていない。 | 1\. スレッドグループ配下にHTTPクッキーマネージャが存在するか確認する。 2\. 結果をツリーで表示リスナーのリクエストタブで、Cookie DataにセッションIDが含まれているか確認する。ブラウザの成功リクエストと比較する。 |
| ログインのPOSTリクエストで403 Forbiddenエラーが返ってくる。 | CSRFトークンの相関化が失敗している、またはトークンが送信されていない。 | 1\. Debug Samplerを使い、POSTリクエスト直前のトークン用変数（例：${csrf\_token}）が初期値（例：TOKEN\_NOT\_FOUND）のままになっていないか確認する。 2\. 正規表現抽出の設定（正規表現、テンプレート等）が正しいか見直す。 3\. ブラウザの開発者ツールと比較し、トークンがリクエストボディではなく、リクエストヘッダで送信されていないか確認する。 |
| ループ（繰り返し）の2回目以降でログインに失敗する。 | HTTPクッキーマネージャのClear cookies each iteration?がオフになっている。 | 1回目のループで取得したセッション情報が2回目以降も使われ、サーバー側で無効なセッションとして扱われている可能性がある。Clear cookies each iteration?にチェックを入れて、毎回新しいセッションで開始されるようにする 18。 |
| レスポンスは200 OKだが、期待したページではなくログインページに戻される。 | 1\. ログインのパラメータ（ユーザー名/パスワード）が間違っている。 2\. 隠された動的パラメータ（トークン以外）の相関化が漏れている。 | 1\. JMeterのパラメータ設定と、使用しているテストデータ（CSVファイルなど）が正しいか確認する。 2\. ブラウザとJMeterのリクエストパラメータを再度徹底的に比較し、見落としている動的パラメータがないか確認する 22。 |

---

## **第5部：シナリオの発展と再利用性の向上**

正しく動作するログインシナリオが完成したら、次はそのシナリオをより実践的で、メンテナンスしやすく、そして再利用可能な「資産」へと昇華させる段階です。このセクションでは、テストデータを外部ファイルから供給するデータ駆動テスト、現実的なユーザー行動を模倣するためのタイマーの導入、そしてスクリプトの部品化による再利用性の向上といった、より高度なテクニックについて解説します。これらの手法は、テストの信頼性を高めると同時に、長期的な運用コストを大幅に削減します。

### **5.1. データ駆動テストへの移行：CSV Data Set Config**

目的  
テストシナリオに単一のユーザー情報（例：testuser/password）をハードコーディングするのは、現実的ではありません。実際のシステムは多数のユーザーによって利用されるため、複数の異なるユーザーでテストを行う必要があります。CSV Data Set Configは、ユーザーIDやパスワードといったテストデータを外部のCSVファイルから読み込み、テスト実行時に動的に割り当てるための設定エレメントです 30。  
**設定手順**

1. CSVファイルの準備:  
   username,password のようなヘッダ行を持つCSVファイルを作成し、テストに使用するユーザーデータを複数行にわたって記述します。  
   例: users.csv  
   コード スニペット  
   user01,pass01  
   user02,pass02  
   user03,pass03

2. CSV Data Set Configの追加:  
   スレッドグループを右クリックし、追加 \-\> 設定エレメント \-\> CSV Data Set Config を選択します 30。  
3. **主要項目の設定** 32:  
   * **Filename**: 作成したCSVファイルへのパス（例：users.csv）を指定します。JMXファイルと同じディレクトリにあれば、ファイル名のみで構いません 33。  
   * **Variable Names (comma-delimited)**: CSVファイルの各列に対応する変数名をカンマ区切りで指定します（例：username,password）。ここで指定した変数名で、後続のサンプラーから値を参照できます 30。  
   * **Sharing mode**: 複数のスレッド（仮想ユーザー）がCSVファイルのデータをどのように使用するかを定義します。  
     * All threads (デフォルト): 全てのスレッドで一つのCSVファイルを共有し、各スレッドは順番に次の行を読み込みます。10ユーザーで実行する場合、1番目のユーザーが1行目、2番目のユーザーが2行目...と読み進めます 33。  
     * Current thread: 各スレッドが独立してCSVファイルを最初から読み込みます。  
4. 変数の利用:  
   HTTPリクエストサンプラーのパラメータ設定で、ハードコーディングされていた値を、CSVから読み込んだ変数に置き換えます。  
   * 例: ユーザー名フィールドの値を ${username}、パスワードフィールドの値を ${password} に変更します。

これにより、スクリプト本体を変更することなく、テストデータを簡単に追加・変更できるようになり、テストの網羅性とメンテナンス性が大幅に向上します。

### **5.2. 現実的なユーザー行動のシミュレーション：タイマー**

目的  
実際のユーザーは、ページの内容を読んだり、次に行う操作を考えたりするため、クリックや入力の間に必ず間（ま）があります。これを「思考時間（Think Time）」と呼びます 35。タイマーをシナリオに挿入しないと、JMeterは可能な限りの最高速度でリクエストを連続送信し、サーバーに対して非現実的で過剰な負荷をかけてしまいます。現実的な負荷をシミュレートするためには、タイマーを用いて意図的に遅延を挿入することが不可欠です。  
代表的なタイマーの種類と使い分け  
タイマーは、適用したいサンプラーの子要素として追加するか、複数のサンプラーに適用したい場合はそれらと同じ階層に配置します 37。

* Constant Timer（固定タイマー）:  
  最もシンプルなタイマーで、指定したミリ秒だけ常に待機します 38。テスト結果の再現性を重視する場合に適しています。  
* Uniform Random Timer（一様ランダムタイマー）:  
  固定の遅延時間に加え、指定した範囲内のランダムな時間を加算します 35。例えば、「固定遅延 3000ms」「ランダム遅延最大値 2000ms」と設定すると、3000msから5000msの間でランダムな待機時間が発生します。これにより、全ユーザーが同じ間隔で行動する不自然さをなくし、より現実的なばらつきを再現できます 41。  
* Gaussian Random Timer（ガウシアンランダムタイマー）:  
  正規分布（ガウス分布）に基づいて遅延時間を生成します。多くのユーザーが平均的な思考時間を持ちつつ、一部のユーザーは非常に短いか、あるいは非常に長い思考時間を持つ、といった自然なばらつきを最もよくシミュレートできるタイマーです 39。

### **5.3. シナリオのモジュール化と再利用**

目的  
大規模なテストプロジェクトでは、複数のテストシナリオで「ログイン」「商品検索」「ログアウト」といった共通の操作シーケンスが必要になることが頻繁にあります。これらの共通処理を「部品（モジュール）」として作成し、様々なシナリオから呼び出して再利用することで、開発効率を飛躍的に向上させ、メンテナンスコストを削減します。  
このアプローチは、アプリケーションの仕様変更に強いという大きな利点をもたらします。例えば、ログイン処理の仕様が変更された場合、モジュール化されていなければ、ログイン処理を含むすべてのテストシナリオを個別に修正する必要があります。しかし、ログイン処理がモジュール化されていれば、そのモジュールを一つ修正するだけで、それを呼び出しているすべてのシナリオが自動的に更新されます 44。

実現方法  
JMeterでは、Test FragmentとModule ControllerまたはInclude Controllerを組み合わせてモジュール化を実現します。

1. Test Fragment（テストフラグメント）の作成:  
   テスト計画直下を右クリックし、追加 \-\> Test Fragment \-\> Test Fragment を選択します。テストフラグメントは、スレッドグループのようにサンプラーやコントローラを配置できますが、それ自体は単独では実行されません。ここに、ログイン処理のような共通化したい一連のサンプラーを配置します 44。  
2. **モジュールの呼び出し**:  
   * **Module Controller（モジュールコントローラ）**: 同じテスト計画内にあるテストフラグメントを呼び出す場合に使用します。Module Controllerを追加し、ドロップダウンリストから呼び出したいテストフラグメントを選択します 14。  
   * **Include Controller（インクルードコントローラ）**: 別のJMXファイルとして保存されたテストフラグメントを呼び出す場合に使用します。これにより、プロジェクト全体で共有される共通のログインモジュール（例：login\_module.jmx）を作成し、様々なテスト計画からインクルードして利用できます 44。

このようなモジュール化のアプローチを取り入れることで、JMeterのテストスクリプトは単なる使い捨ての道具から、継続的に保守・改善される「ソフトウェア資産」へとその価値を高めることができます。

---

## **結論：堅牢なテストシナリオを構築するための原則**

本レポートでは、Apache JMeterのプロキシ記録機能を出発点として、現代の動的なWebアプリケーションに対する信頼性の高いテストシナリオを構築するための一連のプロセスを体系的に解説しました。単なるブラウザ操作の記録が、いかにしてノイズ除去、構造化、状態管理、動的パラメータ対応、そしてデバッグという工程を経て、現実的でメンテナンス可能なテストスクリプトへと進化するかを示しました。

このプロセスを通じて明らかになった、堅牢なテストシナリオを構築するための核心的な原則は、以下のチェックリストに集約できます。

* **賢く記録する (Record Smart)**: 記録を開始する前に、HTTP(S) Test Script Recorderのフィルタリング機能を最大限に活用し、静的リソースやサードパーティへのリクエストを積極的に除外する。これにより、分析と修正の対象となるデータの量を劇的に削減し、作業効率を根本から改善する。  
* **論理的に構造化する (Structure Logically)**: 個々のHTTPリクエストの羅列ではなく、トランザクションコントローラを用いて「ログイン」「商品検索」といったユーザーのビジネスアクション単位でシナリオをグループ化する。これにより、テストの可読性が向上し、ビジネス価値の高いパフォーマンス指標を取得できる。  
* **状態を管理する (Manage State)**: HTTPクッキーマネージャを必ず追加し、アプリケーションのセッション管理メカニズムを正しくシミュレートする。特に、Clear cookies each iteration?オプションの意図を理解し、テストシナリオの目的に応じて適切に設定する。  
* **動的な要素はすべて相関化する (Correlate Everything Dynamic)**: 「記録された値はすべて静的で、期限切れである」という前提に立つ。CSRFトークンやセッションIDなど、サーバーから動的に発行されるすべての値を特定し、正規表現抽出などの後処理（Post-Processor）を用いて確実に相関化（抽出と置換）を行う。これは、現代的なWebアプリケーションのテストを成功させる上で最も重要なステップである。  
* **体系的にデバッグする (Debug Systematically)**: 問題が発生した際は、推測に頼るのではなく、科学的なアプローチを取る。正常に動作するブラウザを「正解」とし、結果をツリーで表示リスナーを用いてJMeterのリクエストと比較し、その「差分」を特定する。Debug Samplerを活用して、変数の状態を可視化し、仮説を検証する。  
* **現実性を追求する (Simulate Realism)**: 実際のユーザーの「思考時間」を模倣するために、タイマーを適切に配置する。また、CSV Data Set Configを用いてテストデータを外部化し、複数のユーザーパターンでテストを実行することで、より現実的な負荷状況を再現する。  
* **保守性を考慮して構築する (Build for Maintenance)**: 共通の操作シーケンスはテストフラグメントとしてモジュール化し、Module/Include Controllerで再利用する。これにより、テストスクリプトを単発の成果物ではなく、継続的に保守・改善が可能な「ソフトウェア資産」として扱う。

最終的に、JMeterの記録機能は、あくまでシナリオ作成のプロセスを加速させるための強力な「初期ドラフト作成ツール」に過ぎません。真に価値のあるテストシナリオを構築する鍵は、記録された通信ログを注意深く「解析」し、対象アプリケーションの通信プロトコルとビジネスロジックを深く理解し、それをJMeterの各種要素を駆使して「再実装」する、一種の開発マインドセットを持つことにあります。この原則を指針とすることで、いかなる複雑なWebアプリケーションに対しても、信頼性と再現性の高いパフォーマンステストを設計・実行することが可能となるでしょう。

#### **引用文献**

1. 26\. Apache JMeter HTTP(S) テスト スクリプト レコーダー, 9月 2, 2025にアクセス、 [https://jp.jmeter.net/usermanual/jmeter\_proxy\_step\_by\_step.html](https://jp.jmeter.net/usermanual/jmeter_proxy_step_by_step.html)  
2. Apache JMeterを使用したパフォーマンスのテスト, 9月 2, 2025にアクセス、 [https://docs.oracle.com/cloud/help/ja/analytics-cloud/ACABI/GUID-85489DF3-2BCD-4301-8A1F-F914FDE93069.htm](https://docs.oracle.com/cloud/help/ja/analytics-cloud/ACABI/GUID-85489DF3-2BCD-4301-8A1F-F914FDE93069.htm)  
3. Ajax（非同期通信） 使い方基本 \#JavaScript \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/tatsukikane/items/cfec97bc655b67494d5a](https://qiita.com/tatsukikane/items/cfec97bc655b67494d5a)  
4. How to execute Ajax requests in JMeter? \- Stack Overflow, 9月 2, 2025にアクセス、 [https://stackoverflow.com/questions/41423360/how-to-execute-ajax-requests-in-jmeter](https://stackoverflow.com/questions/41423360/how-to-execute-ajax-requests-in-jmeter)  
5. How to make jmeter to wait until full page load \- Super User, 9月 2, 2025にアクセス、 [https://superuser.com/questions/1470677/how-to-make-jmeter-to-wait-until-full-page-load](https://superuser.com/questions/1470677/how-to-make-jmeter-to-wait-until-full-page-load)  
6. 【Jmeter】「使い方忘れた。。」となった時に見たい最低限の使い方 Study Infra, 9月 2, 2025にアクセス、 [https://study-infra.com/jmeter-start/](https://study-infra.com/jmeter-start/)  
7. JMeterを活用したパフォーマンステストの実践ガイド \#負荷試験 \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/comware\_park/items/87c702bf197e99ac62ed](https://qiita.com/comware_park/items/87c702bf197e99ac62ed)  
8. Apache JMeterのインストールとシナリオ作成 \#apachejmeter \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/xyz666/items/4d06dadbf76583626c63](https://qiita.com/xyz666/items/4d06dadbf76583626c63)  
9. Apache JMeterを使う② HTTPプロキシサーバを利用したリクエストの記録 \- note, 9月 2, 2025にアクセス、 [https://note.com/honest\_kudu5817/n/n1f4e58825858](https://note.com/honest_kudu5817/n/n1f4e58825858)  
10. JMeterで「javax.net.ssl.SSLException / fatal alert: protocol\_version」が出た場合の対処法, 9月 2, 2025にアクセス、 [https://ptune.jp/tech/sslexception/](https://ptune.jp/tech/sslexception/)  
11. SSL証明書エラー/警告の原因・理由と対処方法 \- SEの道標, 9月 2, 2025にアクセス、 [https://milestone-of-se.nesuke.com/troubleshoot/ssl-cert-error/](https://milestone-of-se.nesuke.com/troubleshoot/ssl-cert-error/)  
12. 【18の方法】「この接続ではプライバシーが保護されません」エラーを解決するには \- Kinsta, 9月 2, 2025にアクセス、 [https://kinsta.com/jp/blog/your-connection-is-not-private/](https://kinsta.com/jp/blog/your-connection-is-not-private/)  
13. JMeterのベストプラクティス (前編) Test-Hack Knowledge and Technology in 3 minutes, 9月 2, 2025にアクセス、 [https://test-hack.com/jmeter-best-practices/](https://test-hack.com/jmeter-best-practices/)  
14. コンポーネント リファレンス\_Apache JMeter, 9月 2, 2025にアクセス、 [https://jp.jmeter.net/usermanual/component\_reference.html](https://jp.jmeter.net/usermanual/component_reference.html)  
15. Re: JMeter doesn't wait until ajax-call is finished? \- Apache Mail Archives, 9月 2, 2025にアクセス、 [https://lists.apache.org/thread/rmzk061q4t82vo0j1zqg5jwnt98jnwvp](https://lists.apache.org/thread/rmzk061q4t82vo0j1zqg5jwnt98jnwvp)  
16. JMeterを使ってCookieの値を複数のスレッドグループで共有する \- SHIFT Group 技術ブログ, 9月 2, 2025にアクセス、 [https://note.shiftinc.jp/n/n463981533c4b](https://note.shiftinc.jp/n/n463981533c4b)  
17. そのテストにパワフルに使用できます。JMeter を使用しての XPages アプリケーションのテストについて \- HCL Notes and Domino Application Development Documentation Wiki, 9月 2, 2025にアクセス、 [https://ds-infolib.hcltechsw.com/ldd/ddwiki.nsf/page.xsp?documentId=F8EF4793FEFB7A6585257D3D0005049D\&action=openDocument](https://ds-infolib.hcltechsw.com/ldd/ddwiki.nsf/page.xsp?documentId=F8EF4793FEFB7A6585257D3D0005049D&action=openDocument)  
18. シナリオ作成\#4\_動的パラメータを取り込み、エラーを解消させる ..., 9月 2, 2025にアクセス、 [https://ptune.jp/tech/capture-dynamic-parameters-and-eliminate-errors/](https://ptune.jp/tech/capture-dynamic-parameters-and-eliminate-errors/)  
19. 明日楽するために使えるようになりたい。JMeterの基本的な使い方。 そるでぶろぐ, 9月 2, 2025にアクセス、 [https://devlog.arksystems.co.jp/2019/01/23/6596/](https://devlog.arksystems.co.jp/2019/01/23/6596/)  
20. Apache JMeter の基本的な使い方に関して（その２） \- 丸ノ内テックブログ, 9月 2, 2025にアクセス、 [https://marunouchi-tech.i-studio.co.jp/4554/](https://marunouchi-tech.i-studio.co.jp/4554/)  
21. JMeterでCSRF対策を突破して負荷をかける方法 \- Taste of Tech ..., 9月 2, 2025にアクセス、 [https://acro-engineer.hatenablog.com/entry/2019/05/08/120000](https://acro-engineer.hatenablog.com/entry/2019/05/08/120000)  
22. シナリオ作成\#ex2\_シナリオが正しく動作しないときの調査方法 ..., 9月 2, 2025にアクセス、 [https://ptune.jp/tech/how-to-investigate-when-a-scenario-does-not-work-properly/](https://ptune.jp/tech/how-to-investigate-when-a-scenario-does-not-work-properly/)  
23. JMeter \- Response Data Extractors \- Comparison \- Vinsguru, 9月 2, 2025にアクセス、 [https://www.vinsguru.com/jmeter-response-data-extractors-comparison/](https://www.vinsguru.com/jmeter-response-data-extractors-comparison/)  
24. How to extract data from Json response using JMeter \- Load Testing Blog, 9月 2, 2025にアクセス、 [https://blog.octoperf.com/how-to-extract-data-from-json-response-using-jmeter/](https://blog.octoperf.com/how-to-extract-data-from-json-response-using-jmeter/)  
25. Ajax(非同期通信)についてわかりやすさ重視でまとめてみた(Rails使用のデモ付) \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/motoki0208/items/409ccf256e84017ea307](https://qiita.com/motoki0208/items/409ccf256e84017ea307)  
26. How to Load Test Asynchronous HTTP Requests with JMeter Blazemeter, 9月 2, 2025にアクセス、 [https://www.blazemeter.com/blog/async-requests-jmeter](https://www.blazemeter.com/blog/async-requests-jmeter)  
27. How to Use the Parallel Controller in JMeter \- BlazeMeter, 9月 2, 2025にアクセス、 [https://www.blazemeter.com/blog/parallel-controller-in-jmeter](https://www.blazemeter.com/blog/parallel-controller-in-jmeter)  
28. 【負荷テスト】JMeterシナリオ作成入門 番外編\_シナリオが正しく動作しないときの調査方法, 9月 2, 2025にアクセス、 [https://www.youtube.com/watch?v=rZPQVpUU9Dw](https://www.youtube.com/watch?v=rZPQVpUU9Dw)  
29. JMeterの変数と関数について : 概要、便利な関数、ハマりどころ ..., 9月 2, 2025にアクセス、 [https://qiita.com/malbare932/items/b94223e1ebf2653e7b65](https://qiita.com/malbare932/items/b94223e1ebf2653e7b65)  
30. 【JMeter】CSVからデータを読み込みその値をシナリオで使用する \- BBH, 9月 2, 2025にアクセス、 [https://bbh.bz/2020/04/09/jmeter-get-value-from-csv/](https://bbh.bz/2020/04/09/jmeter-get-value-from-csv/)  
31. How to Use JMeter CSV Data Set Config in Sharing Mode \- BlazeMeter, 9月 2, 2025にアクセス、 [https://www.blazemeter.com/blog/jmeter-csv-dataset-config](https://www.blazemeter.com/blog/jmeter-csv-dataset-config)  
32. シナリオ作成\#6\_入力パラメータを外部ファイルから読み込む ..., 9月 2, 2025にアクセス、 [https://ptune.jp/tech/read-input-parameters-from-external-file/](https://ptune.jp/tech/read-input-parameters-from-external-file/)  
33. CSV Data Set Config \- JMeter VN, 9月 2, 2025にアクセス、 [https://jmetervn.com/2016/10/24/csv-data-set-config/](https://jmetervn.com/2016/10/24/csv-data-set-config/)  
34. JMeterで最低限の負荷試験 \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/tanaka512/items/6fb4b697d120bf7fca4b](https://qiita.com/tanaka512/items/6fb4b697d120bf7fca4b)  
35. A Comprehensive Guide to Using JMeter Timers \- BlazeMeter, 9月 2, 2025にアクセス、 [https://www.blazemeter.com/blog/jmeter-timer](https://www.blazemeter.com/blog/jmeter-timer)  
36. Unveiling the Power of Think Time: Efficient Recordings in JMeter For API Performance Testing by Darmawan Hadiprasetyo Medium, 9月 2, 2025にアクセス、 [https://medium.com/@dhadiprasetyo/unveiling-the-power-of-think-time-efficient-recordings-in-jmeter-for-api-performance-testing-88770eaeb04d](https://medium.com/@dhadiprasetyo/unveiling-the-power-of-think-time-efficient-recordings-in-jmeter-for-api-performance-testing-88770eaeb04d)  
37. 今さら聞けない Apache JMeter の基本 \#ベンチマーク \- Qiita, 9月 2, 2025にアクセス、 [https://qiita.com/aidy91614/items/d96ca0261665abc54f7d](https://qiita.com/aidy91614/items/d96ca0261665abc54f7d)  
38. Timers in JMeter \- Tutorialspoint, 9月 2, 2025にアクセス、 [https://www.tutorialspoint.com/timers-in-jmeter](https://www.tutorialspoint.com/timers-in-jmeter)  
39. Looking at the uses of JMeter Timers \- Load Testing Blog, 9月 2, 2025にアクセス、 [https://blog.octoperf.com/looking-at-the-uses-of-jmeter-timers/](https://blog.octoperf.com/looking-at-the-uses-of-jmeter-timers/)  
40. JMeter \- Uniform Random Timer \- PerfMatrix, 9月 2, 2025にアクセス、 [https://www.perfmatrix.com/jmeter-uniform-random-timer/](https://www.perfmatrix.com/jmeter-uniform-random-timer/)  
41. JMeter Beginner Tutorial 18 \- TIMERS (How to add Think Time) \- YouTube, 9月 2, 2025にアクセス、 [https://www.youtube.com/watch?v=EUgLRmlkTGQ](https://www.youtube.com/watch?v=EUgLRmlkTGQ)  
42. JMeter Timers Loadium, 9月 2, 2025にアクセス、 [https://loadium.com/blog/jmeter-timers](https://loadium.com/blog/jmeter-timers)  
43. JMeter Timers \- Constant, BeanShell And Guassian Random Timer \- Software Testing Help, 9月 2, 2025にアクセス、 [https://www.softwaretestinghelp.com/jmeter-timers/](https://www.softwaretestinghelp.com/jmeter-timers/)  
44. How to create reusable test fragment in jmeter \- Oodles Technologies, 9月 2, 2025にアクセス、 [https://www.oodlestechnologies.com/blogs/how-to-create-reusable-test-fragment-in-jmeter/](https://www.oodlestechnologies.com/blogs/how-to-create-reusable-test-fragment-in-jmeter/)  
45. Modularisation in JMeter \- Load Testing Blog \- OctoPerf, 9月 2, 2025にアクセス、 [https://blog.octoperf.com/modularisation-in-jmeter/](https://blog.octoperf.com/modularisation-in-jmeter/)  
46. Reusable components in JMeter – Part 2, Include Controller Technical Software Testing, 9月 2, 2025にアクセス、 [https://martijndevrieze.net/2016/02/15/reusable-components-in-jmeter-part-2-include-controller/](https://martijndevrieze.net/2016/02/15/reusable-components-in-jmeter-part-2-include-controller/)  
47. JMeter Intermediate Tutorial 7 \- How to use Module Controller and Include Controller, 9月 2, 2025にアクセス、 [https://www.youtube.com/watch?v=jKiZ1efpE5w](https://www.youtube.com/watch?v=jKiZ1efpE5w)
