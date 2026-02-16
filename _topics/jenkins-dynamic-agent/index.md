---
audio: /share-deepresearch/assets/audio/jenkins-dynamic-agent.m4a
category: engineering
date: 2025-11-17
description: Jenkinsの動的エージェント機能を活用し、AWS EC2上でCI/CDパイプラインのリソースを最適化するスケーリング戦略を包括的に分析・比較します。
ga4_metrics:
  avgSessionDuration: 364.059153
  pageViews: 3
  users: 3
layout: topic
prompt: Jenkinsで使用するノードをジョブの状況に合わせて動的に増減させたい。ノードはAWSのEC2を利用する想定となっている。どのようなやり方があるか調査して欲しい。
tags:
- Jenkins
title: AWS EC2を利用したJenkins動的エージェントのスケーリング戦略に関する包括的分析レポート
video: /share-deepresearch/assets/video/jenkins-dynamic-agent.mp4
---

# **AWS EC2を利用したJenkins動的エージェントのスケーリング戦略に関する包括的分析レポート**

## **アーキテクチャ戦略：AWSにおける動的Jenkinsエージェント**

### **1.1. 核心的課題：ビルドキューとリソースの浪費**

従来の静的なビルドインフラストラクチャは、効率性の面で根本的な課題を抱えています。開発チームは、ビルドエージェントの数が不足することによる「ビルドキューの長期化」と、エージェントが過剰に存在することによる「アイドルリソースのコスト増」という、二律背反の問題に直面します 1。

この課題を解決する鍵は「弾力性」 (Elasticity) です 3。すなわち、ジョブの要求に応じてインフラストラクチャが起動（スピンアップ）し、ジョブが完了しアイドル状態になると終了（スピンダウン）する仕組みが求められます 2。本レポートは、AWS環境においてこの弾力性を実現するための主要なアーキテクチャパターンを詳細に分析します。

### **1.2. 「EC2エージェント」の再定義：3つのアーキテクチャパターン**

ユーザーの要求である「EC2を利用するノード」 5 は、現代のクラウドネイティブな文脈において、単一の手法を指すものではありません。その管理手法こそが、アーキテクチャを決定づける重要な変数です。AWSにおけるCI（継続的インテグレーション）の進化は、VMの直接制御からコンテナオーケストレーションへと明確な道筋をたどっています 7。

本レポートでは、EC2インスタンスを中核的なコンピュートリソースとして利用する、以下の3つの主要パターンを分析対象とします。

1. パターン1：プラグインによるEC2直接管理 (Plugin-Managed Direct EC2)  
   Jenkinsコントローラーがインフラストラクチャのオーケストレーターとして機能し、EC2 APIを直接呼び出して個々のVMの起動と停止を行います 5。  
2. パターン2：ASGによるEC2フリート管理 (ASG-Managed EC2 Fleet)  
   Jenkinsコントローラーはインフラストラクチャの利用者 (Consumer) となり、EC2 フリート（集団）の管理をAWS Auto Scaling Group (ASG) に委任します 8。  
3. パターン3：オーケストレーターによるEC2管理 (Orchestrator-Managed EC2 \- EKS)  
   Jenkinsコントローラーはコンテナオーケストレーター (Amazon EKS) 上で実行されるアプリケーションの一つとなります。エージェントは一時的なコンテナ (Pod) 2 となり、それらのPodは、クラスターオートスケーラーによってスケーリングされるEC2ノードのクラスター上で実行されます 11。

ユーザーの「EC2ノード」という要求は、これら3つの異なるアーキテクチャモデルすべてにおいて有効です。本レポートの核心的な価値は、これらのモデルがどのように機能し、どのようなトレードオフが存在するかを明確に区別することにあります。

### **1.3. 主要な評価軸**

本レポートは、これらの3つのパターンを、CI/CDインフラストラクチャの選定において最も重要な以下の4つの評価軸に基づいて評価します。

1. **エージェントの起動速度:** ジョブがキューに入ってから実行が開始されるまでの時間 2。  
2. **コストプロファイル:** AWSリソース、特にスポットインスタンスをどれだけ効率的に活用できるか 3。  
3. **スケーラビリティと耐障害性:** 「突発的」 (Spiky) な高負荷のビルド要求をどれだけうまく処理できるか 1。  
4. **管理オーバーヘッドと複雑性:** ソリューションの構築と維持に必要な人的コストと専門知識 1。

## **メソッド1：Amazon EC2プラグインによるEC2直接プロビジョニング**

### **2.1. アーキテクチャの概要**

これは、最も古く、最も直接的なアプローチです 5。このモデルでは、Jenkinsコントローラーにインストールされた ec2-plugin 13 がビルドキューを監視します。利用可能なエージェントリソースを超える負荷を検知すると、プラグインはAWS API ( RunInstances ) を直接呼び出し、あらかじめ指定されたAMI (Amazon Machine Image) から新しいEC2インスタンスを起動します 5。

新しく起動したEC2インスタンスは、OSのブートプロセスを完了した後、JNLPまたはSSHを介してJenkinsコントローラーに接続し、自身をエージェントとして登録します。ジョブが完了し、インスタンスが一定時間アイドル状態になると、プラグインがそのEC2インスタンスを終了（Terminate）します 5。

### **2.2. 詳細な設定方法**

1. **インストール:** Jenkinsのプラグインマネージャーから「Amazon EC2 plugin」を検索し、インストールします 13。  
2. **クラウド設定:** 「Jenkinsの管理」 \-\> 「ノードとクラウドの管理」 \-\> 「クラウドの追加」と進み、「Amazon EC2」を選択します 5。  
3. **認証情報 (Credentials):** AWSへのアクセス認証情報を設定します。この際、ドキュメント 5 では「アクセスキーとシークレットアクセスキー」の使用が明記されています。これは重大なセキュリティアンチパターンであり、本レポートのセクション8で詳述するIAMロールの使用が強く推奨されます。  
4. **AMI設定:** このモデルの成否は、事前に構築された「ゴールデンAMI」に完全に依存します 5。このAMIには、エージェントとして機能するために必要なすべてのソフトウェアがプリインストールされている必要があります。  
   * Java実行環境 (JRE) 15  
   * SSHサーバーと、Jenkinsコントローラーからの接続を許可する公開鍵が設定された ec2-user 13  
   * Git, Maven, Node.js, Dockerなど、ビルドに必要なすべてのツール  
5. **ネットワーキング:** この設定は、最も一般的な失敗要因の一つです。  
   * **セキュリティグループ:** エージェントとして起動するEC2インスタンスのセキュリティグループは、JenkinsコントローラーからのインバウンドSSH (ポート 22\) を許可する必要があります 13。  
   * **JNLP:** JNLP接続を使用する場合、Jenkinsコントローラー側のセキュリティグループは、動的に作成されるエージェントからのインバウンドJNLPトラフィックを許可する必要があります。エージェントのIPは動的であるため、この設定は非常に複雑です。17 によれば、JNLPポートは明示的に設定しない限り「通常ランダムに割り当てられる」ため、ファイアウォールの設定はさらに困難になります。

### **2.3. スケーリングメカニズム：「Idle termination time」パラメータ**

このプラグインが持つスケーリングのロジックは、「 Idle termination time （アイドル終了時間）」という単純なタイマーのみです 18。このパラメータは、エージェントがジョブを実行せずにアイドル状態になってから、EC2インスタンスを終了するまでの猶予時間（分単位）を定義します 18。

しかし、この単純なメカニズムは非常に「壊れやすい」 (Brittle) ことで知られています。19 や 20 では、エージェントが「即座に」あるいは「早すぎるタイミングで」終了してしまうという問題が報告されています。これは、接続メカニズムの設定ミス（プラグインがインスタンスを起動したもののSSH接続に失敗し、即座に終了と判断するケース）や、エージェントの初期化スクリプトにおける競合状態によって引き起こされることが多くあります 20。

### **2.4. 分析と評価**

このアプローチは、Jenkinsコントローラー自体がインフラストラクチャのライフサイクル管理という、本来の責務（CI/CDのオーケストレーション）を超えた役割を担うことになります。結果として、状態管理の不整合（例：19）が発生しやすく、システム全体の堅牢性が低下するアーキテクチャ上の課題を内包しています。JenkinsはCIサーバーであり、インフラの状態管理マネージャーとして設計されていません。この根本的なアーキテクチャ上の欠陥こそが、次世代のアプローチ（メソッド2）が開発された理由です。

* **利点:**  
  * 「1エージェント ＝ 1 VM」というマッピングが概念的に非常にシンプルである。  
* **欠点:**  
  * スケーリングロジックが脆弱で、設定が難しい 20。  
  * セキュリティモデルが古く、静的なアクセスキーの使用を助長する 5。  
  * 効率が悪い（エージェントが必要になるたびにVMの完全な起動時間を待つ必要がある）。  
  * 「ゴールデンAMI」のメンテナンス（ツールのアップデート、セキュリティパッチ適用）に多大なコストがかかる。  
* **特定のユースケース:**  
  * このプラグインは、EC2ベアメタルインスタンスのプロビジョニングにも使用できます 5。これは、ネストされた仮想化が必要な場合や、macOSビルド（EC2 Macインスタンスはベアメタルとして提供される） 23 など、仮想化できない特殊なワークロードに唯一の選択肢となる場合があります。

## **メソッド2：Amazon EC2 Fleetプラグインによるフリート管理**

### **3.1. アーキテクチャの概要：AWS Auto Scalingへの責任委任**

ec2-fleet-plugin 8 は、アーキテクチャの責任分界点を根本的に変更するアプローチです。このモデルでは、Jenkinsは個々のインスタンスを管理することを止めます。

代わりに、Jenkinsコントローラーはビルドキューを監視し、必要に応じてAWS Auto Scaling Group (ASG)、EC2 Fleet、またはSpot Fleetに対し、「スケールアップ（インスタンスを増やす）」または「スケールダウン（インスタンスを減らす）」の指示を出すだけになります 8。

「どのように」スケールするかという複雑なロジック（例：どのインスタンスタイプを選ぶか、どのアベイラビリティゾーン（AZ）に配置するか、SpotインスタンスとOn-Demandインスタンスの比率をどうするか、Spotが中断された場合にどう対処するか）は、すべてAWSのASGサービスが引き受けます 8。

この責任の委任は、Jenkinsを「インフラのコントローラー」から「インフラの利用者」へと変える、より堅牢でクラウドネイティブなスケーリングパターンです。

### **3.2. 詳細な設定方法**

このアプローチは、AWS側での設定とJenkins側での設定の2つのステップで構成されます。

1. **AWS側での設定:**  
   1. **起動テンプレート (Launch Template) の作成:** AMI ID、インスタンスタイプ、セキュリティグループ、キーペアなどを定義します。このステップの重要な点は、単一のタイプではなく、m5.large や c5.large など、*複数*のインスタンスタイプを指定できることです 9。  
   2. **Auto Scaling Group (ASG) の作成:** 作成した起動テンプレートを使用するASGを作成します。ここで、インスタンスの配分戦略（例：70%をSpot、30%をOn-Demand）を定義できます 9。最も重要な設定として、**最小サイズを 0** に、最大サイズを任意の許容上限に設定します 9。  
2. **Jenkins側での設定:**  
   1. **プラグインのインストール:** 「EC2 Fleet Jenkins Plugin」をインストールします 9。  
   2. **認証情報の設定:** JenkinsコントローラーがASGを操作するためのIAM権限（例：autoscaling:DescribeAutoScalingGroups, autoscaling:UpdateAutoScalingGroup 8）を持つIAMロールを、JenkinsコントローラーのEC2インスタンスにアタッチします（詳細はセクション8を参照）。  
   3. **クラウド設定:** 「Jenkinsの管理」 \-\> 「ノードとクラウドの管理」 \-\> 「クラウドの追加」から「Amazon EC2 Fleet」を選択します 26。AWSリージョンを選択し、AWS側で作成した**ASGの名前**を指定します 8。  
   4. **スケーリングパラメータ:** 「Max Idle Minutes Before Scaledown」（スケールダウンまでの最大アイドル時間）や「Maximum Cluster Size」（最大クラスターサイズ）を設定します 9。

### **3.3. 最大の特徴：スポットインスタンスと混合インスタンスによるコスト最適化**

メソッド1に対するこのアプローチの最大の利点は、圧倒的なコスト効率と耐障害性です。

ASGの能力を活用することで、Jenkinsは最小限の設定でSpotインスタンスを安全に利用できます 3。Spotインスタンスは、On-Demand価格と比較して最大90%の割引が適用される可能性があります 3。

さらに、起動テンプレートで複数のインスタンスタイプ（例：m5.large, m5a.large, c5.large, c5a.large）と複数のAZを指定することで、ASGは最も価格が安く、最も利用可能性（空き）のあるSpotプールからインスタンスを調達できます 9。この「多様化」 9 により、特定のSpotプールが中断された場合でも、ビルドが停止するリスクを劇的に低減できます。

### **3.4. 比較表1： *Amazon EC2 Plugin* vs *EC2 Fleet Plugin***

VMベースのアプローチを選択するユーザーのために、両プラグインの主な違いを以下の表にまとめます。

| 機能 | Amazon EC2 Plugin (メソッド1) | Amazon EC2 Fleet Plugin (メソッド2) |
| :---- | :---- | :---- |
| **スケーリングメカニズム** | Jenkinsによる直接管理。EC2 APIを直接呼び出す 5。 | AWSによる管理。ASG / Spot Fleetに委任する 8。 |
| **インスタンス調達** | エージェントテンプレートごとに単一のインスタンスタイプ 8。 | 起動テンプレート経由で複数のインスタンスタイプを混合可能 8。 |
| **Spotインスタンスサポート** | 基本的（起動は可能だが中断に弱い） 5。 | 高度。ASGの配分戦略（Spot/On-Demand混合）を利用可能 9。 |
| **耐障害性** | 低（指定したインスタンスタイプが利用不可の場合、起動に失敗する）。 | 高（複数のインスタンスタイプとAZから調達できる） 9。 |
| **管理モデル** | Jenkinsが**コントローラー**。状態管理の負担が高い 5。 | Jenkinsが**利用者**。ASGに任せるため負担が低い 8。 |

### **3.5. 分析と評価**

* **利点:**  
  * ASGによる高度なSpotインスタンス活用による、劇的なコスト削減 3。  
  * 複数インスタンスタイプ・複数AZ戦略による、高い耐障害性。  
  * Jenkinsの責務を減らし、より堅牢なクラウドネイティブアーキテクチャを実現。  
* **欠点:**  
  * メソッド1と比較して、AWS側でASGと起動テンプレートを事前に作成する必要があり、初期設定がわずかに複雑になる。  
* **評価:**  
  * コンテナ化されていない、従来のVMベース（AMIベース）のエージェントを実行する必要がある場合、**EC2 Fleet Plugin (メソッド2) は、従来のEC2 Plugin (メソッド1) に対する明確かつ上位の推奨アプローチ**です。

## **メソッド3：オーケストレーター管理スケーリング (Kubernetes \- EKS)**

### **4.1. アーキテクチャの概要：エージェント＝一時的なPod**

これは、現代的かつ最も強力なコンテナネイティブのアーキテクチャです 1。このモデルでは、Jenkinsコントローラー（それ自体もEKSクラスター上で実行可能 28）が kubernetes-plugin 10 を使用します。

ジョブが開始されると、プラグインは**VMを起動しません**。代わりに、Kubernetesの **Pod** と呼ばれるリソースを作成します 2。このPodは podTemplate 30 と呼ばれる定義に基づいて作成され、ビルドに必要な複数のコンテナ（例：Jenkinsコントローラーに接続するための jnlp コンテナと、ビルドを実行するための maven コンテナ）を含みます 2。

作成されたPodは、EKSクラスターを構成する**EC2ノード**のいずれかにスケジュールされます。ビルドが完了すると、そのPodは即座に終了（Terminate）され、破棄されます 10。

このアプローチの最大の利点は、ビルド*環境*とビルド*インフラ*の完全な分離にあります。メソッド1および2では、ビルドツール（Java, Node.js）はAMIに焼き付けられていました 31。チームAがNode 16を、チームBがNode 18を必要とする場合、2つの異なるAMIと2つの異なるASG設定が必要になり、管理が複雑化します。

しかし、メソッド3では、ビルド*環境*は podTemplate 内の単なるコンテナイメージ名（例： image: node:18 ） 2 として定義されます。ビルド*インフラ*は、EKSが管理する汎用的なEC2ノードのプールです。これにより、チームAとチームBは、同じインフラストラクチャプールを共有しながら、オンデマンドで異なるビルド環境（コンテナ）をリクエストでき、管理オーバーヘッドが劇的に削減されます。

### **4.2. 「二重スケーリング」メカニズムの解説**

メソッド3を理解する上で最も重要な概念は、スケーリングのループが2段階存在することです。

1. **エージェント (Pod) スケーリング:** 2  
   * **トリガー:** Jenkinsのビルドジョブがキューに入る。  
   * **アクション:** kubernetes-plugin が即座にPodの定義を作成し、Kubernetes APIに送信する。  
   * **速度:** **ミリ秒〜数秒**（クラスターに空き容量がある場合）。  
2. **インフラストラクチャ (Node) スケーリング:** 32  
   * **トリガー:** 新しいPodをスケジュールしようとしたが、クラスター内の既存のEC2ノードに十分なCPU/メモリの空き容量がない。Podの状態が Pending （保留中）になる 32。  
   * **アクション:** 「クラスターオートスケーラー」と呼ばれるコンポーネントが Pending 状態のPodを検知し、そのPodを受け入れ可能な**新しいEC2インスタンス**をAWSに要求し、クラスターに参加させる。  
   * **速度:** **数分**（新しいEC2 VMが起動し、クラスターに参加するまでの時間）。

この2段階のシステムは、クラスターに余裕がある限りは「即時」のエージェント起動速度を提供し、リソースが不足した場合にのみ「効率的」にインフラ（EC2）をスケールさせるという、両方の利点を兼ね備えています 4。

### **4.3. 詳細な設定方法**

1. **インストール:** Jenkinsのプラグインマネージャーから「Kubernetes」プラグインをインストールします 29。  
2. **クラウド設定:** 「Jenkinsの管理」 \-\> 「ノードとクラウドの管理」 \-\> 「クラウドの追加」から「Kubernetes」を選択します 10。  
3. **クラスター接続:** EKSクラスターの「APIサーバーエンドポイント」のURLを入力します 28。認証は、セクション8で詳述するIAMロール（IRSA）を用いて設定するのが最適です。  
4. **podTemplate の定義:** これが設定の中核です 30。エージェントPodを定義するYAMLスニペットを指定します 2。  
   * label: Jenkinsfile内でジョブがエージェントを指定するためのラベル（例：maven-agent）。これにより、agent { label 'maven-agent' } のように呼び出せます 2。  
   * containers: Pod内で実行するコンテナのリストを定義します。  
     * 1つは、Jenkinsコントローラーと通信するための jnlp コンテナ（例：jenkins/inbound-agent）である必要があります 2。  
     * その他、ビルドツール（例：image: node:18）を含むコンテナを必要なだけ追加できます 2。

### **4.4. 利点：速度、分離性、環境の非結合**

* **速度:** クラスターに容量がある限り、エージェントのプロビジョニング（Podの起動）はほぼ瞬時に完了します 2。  
* **分離性:** 各ビルドは専用のPod内で実行され、他のビルドから完全に隔離されるため、ビルド間の競合（グローバルなツールの汚染など）が防止されます 4。  
* **リソース効率:** 1つの巨大なEC2ノード上に、多数の小さなエージェントPodを「高密度に配置（ビンパッキング）」できます 29。これにより、「1エージェント＝1 VM」モデル（メソッド1, 2）よりもはるかに高いリソース使用率が達成されます。  
* **柔軟性:** 前述の通り、ビルド環境（コンテナイメージ）とインフラ（EC2ノード）を分離できるため、多種多様なビルド要件に単一のクラスターで対応できます。

### **4.5. 分析と評価**

* **利点:**  
  * 非常に高速なエージェントレベルのスケーリング。  
  * 高いリソース密度と、それによるコスト効率。  
  * ビルド環境の定義と管理における圧倒的な柔軟性。  
* **欠点:**  
  * EKSクラスターの運用・管理（ネットワーキング、セキュリティ、アップグレード）という、高いレベルの複雑性と専門知識が要求されます 4。  
* **評価:**  
  * 現代における最先端のソリューションです。コンテナベースのパイプラインを実行する、あるいはパフォーマンスと効率を最大化したい場合には、メソッド3が技術的に最も優れた選択肢となります。ただし、その導入と維持には相応の技術的投資が必要です。

## **5\. 詳細：EKS向けEC2ノードのプロビジョニング（インフラストラクチャ・スケーリング）**

メソッド3のアーキテクチャ（EKS）を選択した場合、次に「インフラストラクチャ・スケーリング（Pending 状態のPodを解決するために、新しいEC2ノードをどのように調達するか）」という問題に直面します 32。これには大きく分けて2つの主流なアプローチが存在します 35。

### **5.1. サブメソッド5.1：従来のアプローチ (EKS \+ Cluster Autoscaler)**

* **動作原理:** Kubernetes Cluster Autoscaler (CAS) は、クラスター内にインストールされるコンポーネントです 37。CASは Pending 状態のPodを定期的にスキャンし 32、そのPodを受け入れ可能な、**あらかじめ定義されたASG** 37 を見つけます。そして、そのASGの「希望インスタンス数」 (Desired Capacity) を増やすようAWS APIを呼び出します 33。  
* **設定:** c5.large 用のASG、r5.large 用のASGなど、必要なインスタンスタイプごとにASGを事前に作成し、CASがそれらを検出できるように特定のタグを付与する必要があります 37。  
* **分析:** このアプローチは成熟しており、安定しています。しかし、ASGという抽象化に依存するため、本質的な制約を抱えています 35。スケーリング速度はASGの応答速度に律速され、Podの要求リソースに対してASGのインスタンスタイプが大きすぎる（オーバースペックな）場合、リソースの無駄（過剰プロビジョニング）が発生しやすくなります 35。

### **5.2. サブメソッド5.2：現代的なアプローチ (EKS \+ Karpenter)**

* **動作原理:** Karpenterは、AWSネイティブの次世代オートスケーラーです 7。Karpenterも Pending 状態のPodを監視します 41 が、CASとは決定的に異なります。Karpenterは **ASGを一切使用しません** 35。  
* Karpenterは、Pending 状態のPodが要求するリソース（CPU, メモリ, アーキテクチャ, AZなど）を直接確認します。その後、そのPodの要求を**ジャストインタイムで満たす、最も安価で最適なEC2インスタンス**を自ら選定し、EC2 APIを直接呼び出して起動します 35。  
* **利点:**  
  1. **速度:** ASGをバイパスするため、プロビジョニングが非常に高速です（数分ではなく数十秒単位での起動も可能） 36。  
  2. **コストと効率:** Pending 状態のPod群に合わせた「**適切なサイズ（Right-sizing）**」のインフラを動的に調達します 40。SpotインスタンスとOn-Demandインスタンスをインテリジェントに混在させ、コストを最適化します 34。  
  3. **柔軟性:** 事前にASGを定義する必要がなく、KarpenterがAWSの全インスタンスタイプから最適なものを選択します 34。  
* **設定:** KarpenterをHelmチャートでインストールし 43、NodePool というリソース定義でスケーリングのルール（許可するインスタンスタイプ、Spot/On-Demandの比率など）を定義します。

Cluster Autoscaler (CAS) は「グループベース」のスケーリングであり、事前に定義されたVMテンプレート（ASG）に依存します。これに対し、Karpenterは「**ワークロードアウェア**」なスケーリングを実現し、コンテナの要求リソースと、ジャストインタイムで起動されるVMとを直接結びつけます。これにより、クラウドネイティブモデルにおける最後の非効率（ASGによる遅延とリソースの無駄）が解決されます。

### **5.3. 比較表2：EKSノードオートスケーラーの比較: *Cluster Autoscaler* vs *Karpenter***

EKSアーキテクチャ（メソッド3）を採用する上で、EC2インフラのパフォーマンスとコストを決定づける、この2つのオートスケーラーの比較は不可欠です。

| 機能 | Cluster Autoscaler (CAS) | Karpenter |
| :---- | :---- | :---- |
| **スケーリングメカニズム** | 事前に定義されたASGの希望数を増減させる 33。 | Pending 状態のPodに基づき、EC2 APIを直接呼び出す 35。 |
| **プロビジョニング速度** | 遅い（ASGの安定化を待つ必要がある） 39。 | 非常に速い（ASGをバイパスし、数秒～数十秒で起動開始） 36。 |
| **リソース効率** | グループベース。過剰なプロビジョニングが発生しがち 35。 | ワークロードアウェア。Podに合わせた「適切なサイズ」のノードを起動 42。 |
| **コスト最適化** | ASGのSpot/On-Demand混合設定に限定される 36。 | 高度。最適なインスタンスタイプとSpotプールを動的に選定 34。 |
| **設定** | インスタンスタイプごとに多数のASGを管理する必要がある 37。 | NodePool という単一の定義でスケーリングルールを管理 42。 |

## **6\. アーキテクチャの対比：サーバーレスエージェント (AWS Fargate)**

これまでの議論はすべて、最終的にEC2インスタンスを利用する（あるいはEC2インスタンスの*管理*を必要とする）ものでした。ここで、論理的な対比として、「EC2インスタンスの管理を完全に排除する」サーバーレスアプローチを検討します。

### **6.1. サーバーレスの前提：EC2ノード管理の排除**

AWS Fargateは、コンテナ向けのサーバーレスコンピュートエンジンです。ユーザーはコンテナ（タスク）を実行するだけで、AWSがその基盤となるコンピュートリソースを自動的にプロビジョニング・管理します。ユーザーがEC2インスタンスを意識（管理）する必要は一切ありません 6。

### **6.2. オプション6.1：Amazon ECSプラグイン**

このモデルはEKSの代わりにAmazon ECS (Elastic Container Service) を使用します。amazon-ecs プラグイン 46 を導入すると、JenkinsコントローラーはビルドをECSクラスター上の「タスク」として実行できます 48。

このECSクラスターのキャパシティプロバイダーとしてFargateを指定する 45 ことで、ビルドが開始されると、JenkinsはECSに「このタスクをFargateで実行せよ」と指示します。AWSはコンピュートリソースをシームレスに提供し、コンテナを実行、完了後に破棄します 45。

### **6.3. オプション6.2：EKS \+ Fargate プロファイル**

これは、メソッド3 (EKS) とFargateを組み合わせたハイブリッドモデルです。Jenkins側ではメソッド3と全く同じ kubernetes-plugin を使用します 50。

AWS側では、EKSクラスターを作成した後、「Fargateプロファイル」を設定します 51。このプロファイルは、「Kubernetesの jenkins-agents ネームスペースに作成されたPodは、すべてFargateで実行する」といったルールを定義するものです 6。

JenkinsがエージェントPodを作成すると、EKSがそのリクエストを捕捉し、Fargateプロファイルに合致することを確認します。その後、EKSはEC2ノードグループではなく、サーバーレスのFargateキャパシティ上にそのPodをスケジュールします 6。

### **6.4. 分析とトレードオフ（重大な制約事項）**

Fargateは「ノード管理」の問題を解決しますが 6、代わりに「ビルドプロセス」の新たな問題を引き起こします。

* **利点:**  
  * EC2ノードの管理（AMIのパッチ適用、スケーリング、ASG、CAS/Karpenter）が一切不要になります 6。インフラストラクチャの観点からは、最もシンプルなモデルです。  
* **欠点 (重大な制約):**  
  * **Docker-in-Docker (DinD) の禁止:** これが最大の制約です。Fargateタスクは、ホストOSのDockerデーモンにアクセスできません 53。もしビルドプロセス自体が docker build... のようにDockerイメージをビルドする処理を含む場合、そのビルドは失敗します。  
  * **回避策 (Kaniko):** この問題を回避するには、CIプロセス自体を修正し、Dockerデーモンを必要としない「デーモンレス」ビルドツール（例：**Kaniko** 53）を使用するよう、ビルドスクリプトを書き換える必要があります。これは、インフラ（Fargate）の選択が、アプリケーションレベルのCIスクリプトに直接的な変更を強いることを意味し、決して些細な変更ではありません。  
  * **コスト:** Fargateは、最適化されたEC2 Spotインスタンス（メソッド2や3.2）と比較して、一般的にコストが高くなる傾向があります 55。

## **7\. 比較分析と戦略的推奨事項**

### **7.1. 主要な評価軸による最終比較**

これまでの分析を、主要な評価軸（速度、コスト、複雑性）で総合的に比較します 1。

* **エージェント起動速度:** メソッド3 (EKS) が最速です（クラスターに空き容量がある限り、Podの起動は数秒） 2。メソッド1と2は、VMの起動時間（数分）を要するため遅くなります 1。  
* **インフラ起動速度:** Pending 状態のPodを解決する速度は、メソッド3.2 (EKS+Karpenter) が最速です 36。  
* **コスト:** Spotインスタンスを最もインテリジェントに活用できる、メソッド2 (EC2 Fleet) とメソッド3.2 (EKS+Karpenter) が最もコスト効率に優れます 3。  
* **複雑性:** 複雑性は 1 \< 2 \< 3 の順に増加します。メソッド3 (EKS) が最も高度な専門知識を要求します 1。

### **7.2. 比較表3：アーキテクチャ全体比較**

本レポートで分析した主要なアーキテクチャ（メソッド1, 2, 3+CAS, 3+Karpenter, およびFargate）を、意思決定のために集約・比較します。

| アーキテクチャ | エージェント起動速度(空き容量あり) | インフラ起動速度(空き容量なし) | コストプロファイル | スケーラビリティ | 管理オーバーヘッド |
| :---- | :---- | :---- | :---- | :---- | :---- |
| **1\. Direct EC2 Plugin** | 非常に遅い (数分) | N/A (同左) | 悪い | 低 | 低 (ただし脆弱) |
| **2\. EC2 Fleet Plugin** | 非常に遅い (数分) | N/A (同左) | 非常に良い (Spot活用) | 中 | 中 (ASGの管理) |
| **3\. EKS \+ CAS** | 速い (数秒) | 遅い (数分) | 良い | 高 | 非常に高い (EKS \+ ASG管理) |
| **4\. EKS \+ Karpenter** | 速い (数秒) | 速い (数十秒～数分) | 非常に良い (Spot \+ Right-sizing) | 非常に高い | 高い (EKS管理、ASG不要) |
| **5\. EKS \+ Fargate** | 速い (数秒) | 即時 (サーバーレス) | 良い (Spot不可) | 高 | 低 (ただしビルド制約あり) |

### **7.3. 戦略的推奨事項（ペルソナ別）**

最終的な選択は、組織の技術的成熟度、ワークロードの特性、およびコスト許容度によって決定されます。

* **推奨1：シンプルさと低負荷を最優先する場合**  
  * **推奨アーキテクチャ:** **Amazon EC2 Plugin (メソッド1)**  
  * **論拠:** 欠点は多いものの、設定が最も単純で理解しやすいアプローチです。ビルド量が少なく、時折クラウドバースト（一時的な負荷分散）が必要になる程度であれば、この方法でも十分機能します。  
* **推奨2：VMベース（非コンテナ）でコストを最適化したい場合**  
  * **推奨アーキテクチャ:** **Amazon EC2 Fleet Plugin (メソッド2)**  
  * **論拠:** これは、従来のVMベース（AMIベース）のエージェントを実行するための、現時点で「最良」の方法です。ASGを活用したSpotインスタンスと混合インスタンスのフリート運用 9 は、このモデルにおいて他に類を見ないコスト効率と耐障害性を提供します。  
* **推奨3：ハイパフォーマンスなコンテナパイプラインを追求する場合**  
  * **推奨アーキテクチャ:** **EKS \+ Karpenter (メソッド3 \+ 5.2)**  
  * **論拠:** これは、現在の最先端 (State-of-the-art) のソリューションです。Kubernetesによる瞬時のエージェントスケーリング 2 と、Karpenterによる超効率的なEC2プロビジョニング 36 を組み合わせます。最も複雑ですが、最もパフォーマンスと効率に優れたアーキテクチャです。  
* **推奨4：「サーバーレスファースト」の組織方針がある場合**  
  * **推奨アーキテクチャ:** **EKS \+ Fargate プロファイル (メソッド6.2)**  
  * **論拠:** 組織の方針としてFargateの利用が推奨・義務付けられている場合 53、このモデルはEC2ノード管理を完全に排除したサーバーレスのエージェントバックエンドを提供します 6。ただし、導入の前提条件として、ビルドプロセスがKanikoなどのデーモンレスツールで動作することを徹底的に検証する必要があります 53。

## **8\. セキュリティとベストプラクティス**

### **8.1. IAM：黄金律（アクセスキーではなくIAMロールを使用する）**

* **問題:** メソッド1のドキュメント 5 や多くの古いチュートリアルは、静的なAWSアクセスキーの使用を前提としています。これは深刻なセキュリティリスクです。このキーが漏洩した場合、攻撃者は長期間有効な認証情報を手に入れ、AWSアカウントを不正に操作できます。  
* **解決策:** **IAMロール**を使用します 57。Jenkinsの*コントローラー*を実行しているEC2インスタンスに、**インスタンスプロファイル (IAMロール)** をアタッチ（割り当て）します 58。  
* **動作原理:** このIAMロールは、Jenkinsコントローラーに対し、その職務（例：メソッド1のための ec2:RunInstances、メソッド2のための autoscaling:UpdateAutoScalingGroup、メソッド3のための eks:DescribeCluster）を実行するために必要な**一時的な、自動ローテーションされる認証情報**を提供します 57。これにより、静的なアクセスキーをコードや設定ファイルに埋め込む必要が完全になくなります。  
* **EKSにおける発展:** メソッド3 (EKS) では、**IAM Roles for Service Accounts (IRSA)** という仕組みを利用することで、この一時的な認証情報のベストプラクティスを、エージェントのPod自体にまで適用できます 61。

### **8.2. ネットワーキング：コントローラーとエージェント間の通信セキュリティ**

* **問題:** メソッド1とメソッド2では、エージェントは外部のEC2インスタンスとして起動し、コントローラーに「接続バック」する必要があります 15。  
  * SSH接続 16: コントローラーのIPが、エージェントのSSHポート(22)にアクセスできる必要があります。  
  * JNLP接続 17: エージェントのIPが、コントローラーのJNLPポートにアクセスできる必要があります。これは、コントローラーのJNLPポートが、動的なIPアドレス範囲（全エージェント）に対して公開されている必要があることを意味し、一般的な障害点でありセキュリティ上の懸念点でもあります 17。  
* EKSのセキュリティ上の利点（接続モデルの反転）:  
  kubernetes-plugin (メソッド3) のアーキテクチャは、このネットワークセキュリティモデルを反転させ、よりシンプルかつ安全なものにします。  
  メソッド1, 2では、エージェントがコントローラーのJNLPポート（インバウンド）に接続する必要がありました 17。これはコントローラーのポートを外部に晒すことを意味します。  
  メソッド3では、kubernetes-plugin 10 がエージェントをインバウンドエージェントとして起動します。Pod内の jnlp コンテナ 10 が、クラスター内部からJenkinsコントローラーに対して接続を開始します。  
  Jenkinsコントローラー自体も同じEKSクラスター内で実行されている場合（一般的なパターン 28）、この通信はすべてクラスター内部のプライベートネットワークで完結できます 10。これにより、JNLPポートをパブリックインターネット（あるいは広範なVPC）に公開する必要がなくなり、セキュリティ体制が大幅に向上します。

## **9\. 結論**

### **9.1. アーキテクチャのトレードオフに関する最終総括**

本レポートは、AWS EC2上で動的なJenkinsエージェントを実行するための3つの主要なアーキテクチャパターンを詳述しました。この選択は、単に「EC2を使うか否か」ではなく、「EC2ベースのコンピュートリソースを*どのように管理するか*」という、より深いレベルのアーキテクチャの選択です。

**Direct EC2 Control (メソッド1)** から、**Delegated Fleet Control (メソッド2)** へ、そして **Container-Orchestrated Control (メソッド3)** へと移行するにつれ、「管理のシンプルさ」と引き換えに、「スケーラビリティ」「速度」「コスト効率」を獲得していくという、明確なトレードオフが存在します。

### **9.2. 将来性：「VM as Agent」から「Container as Agent」へ**

調査結果が示す業界のトレンドは、「VM as Agent」（VMそのものがエージェント）モデル（メソッド1, 2）から、「Container as Agent」（コンテナがエージェント）モデル（メソッド3）へと、明確かつ不可逆的に移行しています 1。

* 「VM as Agent」モデルは、起動が遅く 1、リソース効率が悪く、「ゴールデンAMI」という重い管理対象を必要とします。  
* 「Container as Agent」モデルは、起動が速く 2、リソース効率が高く（ビンパッキング）、コンテナイメージによる柔軟な環境定義が可能です 4。

特に、**Karpenter** 40 の登場は、コンテナモデルに残っていた最後の非効率（ASGベースの遅いノードスケーリング）を解消し、**EKS \+ Karpenter** の組み合わせを、技術的に最も優れた高スループットCI/CD基盤として確立させました。

### **9.3. 最終推奨事項**

* 組織がまだコンテナネイティブではなく、AMIベースの運用が中心である場合、**Amazon EC2 Fleet Plugin (メソッド2)** が、堅牢かつコスト効率の高い、推奨されるソリューションです。  
* 組織がコンテナネイティブな開発プロセスにコミットしている、あるいは移行中である場合、**Amazon EKS と Karpenter (メソッド3 \+ 5.2)** への技術的投資が、将来にわたって最高のパフォーマンス、コスト、スケーラビリティを提供する、現時点での最良のアーキテクチャとなります。

#### **引用文献**

1. Using Dynamic Build Agents To Automate Scaling In Jenkins ..., 11月 17, 2025にアクセス、 [https://octopus.com/blog/jenkins-dynamic-build-agents](https://octopus.com/blog/jenkins-dynamic-build-agents)  
2. Jenkins on Kubernetes: Dynamic Agents & Effortless Scalability for Modern CI/CD, 11月 17, 2025にアクセス、 [https://dev.to/alex\_aslam/jenkins-on-kubernetes-dynamic-agents-effortless-scalability-for-modern-cicd-2ff3](https://dev.to/alex_aslam/jenkins-on-kubernetes-dynamic-agents-effortless-scalability-for-modern-cicd-2ff3)  
3. Jenkins on Fargate and ec2 Spotfleet by Chetan Patel \- Medium, 11月 17, 2025にアクセス、 [https://medium.com/@chetlo/jenkins-on-fargate-and-ec2-spotfleet-b6fd62e98fdb](https://medium.com/@chetlo/jenkins-on-fargate-and-ec2-spotfleet-b6fd62e98fdb)  
4. Jenkins Integration in Kubernetes (Dynamic Agents) \- Comtrade 360, 11月 17, 2025にアクセス、 [https://www.comtrade360.com/insights/jenkins-integration-in-kubernetes-dynamic-agents/](https://www.comtrade360.com/insights/jenkins-integration-in-kubernetes-dynamic-agents/)  
5. Amazon EC2 Jenkins plugin, 11月 17, 2025にアクセス、 [https://plugins.jenkins.io/ec2/](https://plugins.jenkins.io/ec2/)  
6. How to Use Jenkins Effectively With ECS/EKS Cluster \- DZone, 11月 17, 2025にアクセス、 [https://dzone.com/articles/use-jenkins-effectively-with-ecseks-cluster](https://dzone.com/articles/use-jenkins-effectively-with-ecseks-cluster)  
7. Scaling Effortlessly: How Jenkins, Karpenter and EKS Redefines CI/CD \- Chariot Solutions, 11月 17, 2025にアクセス、 [https://chariotsolutions.com/blog/post/scaling-effortlessly-how-jenkins-karpenter-and-eks-redefines-ci-cd/](https://chariotsolutions.com/blog/post/scaling-effortlessly-how-jenkins-karpenter-and-eks-redefines-ci-cd/)  
8. EC2 Fleet \- Jenkins Plugins, 11月 17, 2025にアクセス、 [https://plugins.jenkins.io/ec2-fleet/](https://plugins.jenkins.io/ec2-fleet/)  
9. Cost Optimize your Jenkins CI/CD pipelines using EC2 Spot ..., 11月 17, 2025にアクセス、 [https://aws.amazon.com/blogs/compute/cost-optimize-your-jenkins-ci-cd-pipelines-using-ec2-spot-instances/](https://aws.amazon.com/blogs/compute/cost-optimize-your-jenkins-ci-cd-pipelines-using-ec2-spot-instances/)  
10. Kubernetes Jenkins plugin, 11月 17, 2025にアクセス、 [https://plugins.jenkins.io/kubernetes/](https://plugins.jenkins.io/kubernetes/)  
11. EC2 vs. EKS: My 3-Tier App Showdown in the AWS Cloud by Breezepatel Medium, 11月 17, 2025にアクセス、 [https://medium.com/@breezepatel3301/ec2-vs-eks-my-3-tier-app-showdown-in-the-aws-cloud-485e5eb52038](https://medium.com/@breezepatel3301/ec2-vs-eks-my-3-tier-app-showdown-in-the-aws-cloud-485e5eb52038)  
12. Architecting for Scale \- Jenkins, 11月 17, 2025にアクセス、 [https://www.jenkins.io/doc/book/scaling/architecting-for-scale/](https://www.jenkins.io/doc/book/scaling/architecting-for-scale/)  
13. Jenkins on AWS, 11月 17, 2025にアクセス、 [https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/](https://www.jenkins.io/doc/tutorials/tutorial-for-installing-jenkins-on-AWS/)  
14. Setup Jenkins With AWS EC2 Instance by Saad Hasan \- Medium, 11月 17, 2025にアクセス、 [https://saedhasan.medium.com/setup-jenkins-with-aws-ec2-instance-f3baa69f7d05](https://saedhasan.medium.com/setup-jenkins-with-aws-ec2-instance-f3baa69f7d05)  
15. Using Jenkins agents, 11月 17, 2025にアクセス、 [https://www.jenkins.io/doc/book/using/using-agents/](https://www.jenkins.io/doc/book/using/using-agents/)  
16. Jenkins Master-Slave Architecture and Agents Day 28 of 90 Days of DevOps \- Ajit Fawade, 11月 17, 2025にアクセス、 [https://ajitfawade.medium.com/jenkins-master-slave-architecture-and-agents-day-28-of-90-days-of-devops-28e3775e50a1](https://ajitfawade.medium.com/jenkins-master-slave-architecture-and-agents-day-28-of-90-days-of-devops-28e3775e50a1)  
17. Amazon EC2 Plugin \- Jenkins, 11月 17, 2025にアクセス、 [https://wiki.jenkins-ci.org/JENKINS/Amazon-EC2-Plugin.html](https://wiki.jenkins-ci.org/JENKINS/Amazon-EC2-Plugin.html)  
18. Why does Jenkins' Amazon EC2 Plugin not terminate some VMs when they are idle for X minutes on AWS US-east-1?, 11月 17, 2025にアクセス、 [https://devops.stackexchange.com/questions/3749/why-does-jenkins-amazon-ec2-plugin-not-terminate-some-vms-when-they-are-idle-fo](https://devops.stackexchange.com/questions/3749/why-does-jenkins-amazon-ec2-plugin-not-terminate-some-vms-when-they-are-idle-fo)  
19. Jenkins EC2 plugin starts and stops instance immediately when building the job, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/56487947/jenkins-ec2-plugin-starts-and-stops-instance-immediately-when-building-the-job](https://stackoverflow.com/questions/56487947/jenkins-ec2-plugin-starts-and-stops-instance-immediately-when-building-the-job)  
20. EC2 node terminates prematurely after Jenkins upgrade : r/jenkinsci \- Reddit, 11月 17, 2025にアクセス、 [https://www.reddit.com/r/jenkinsci/comments/b90k86/ec2\_node\_terminates\_prematurely\_after\_jenkins/](https://www.reddit.com/r/jenkinsci/comments/b90k86/ec2_node_terminates_prematurely_after_jenkins/)  
21. Nested Virtualization in aws bare Metal c5 instances \[closed\] \- Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/62558791/nested-virtualization-in-aws-bare-metal-c5-instances](https://stackoverflow.com/questions/62558791/nested-virtualization-in-aws-bare-metal-c5-instances)  
22. Question: What do you guys have your Jenkins jobs running on? ec2? k8s? etc? : r/jenkinsci, 11月 17, 2025にアクセス、 [https://www.reddit.com/r/jenkinsci/comments/wrw4hl/question\_what\_do\_you\_guys\_have\_your\_jenkins\_jobs/](https://www.reddit.com/r/jenkinsci/comments/wrw4hl/question_what_do_you_guys_have_your_jenkins_jobs/)  
23. Scaling out iOS builds on AWS with EC2 mac \- Jenkins, 11月 17, 2025にアクセス、 [https://www.jenkins.io/blog/2022/10/03/scaling-out-iOS-builds-on-AWS-with-EC2-mac/](https://www.jenkins.io/blog/2022/10/03/scaling-out-iOS-builds-on-AWS-with-EC2-mac/)  
24. Releases · jenkinsci/ec2-fleet-plugin \- GitHub, 11月 17, 2025にアクセス、 [https://github.com/jenkinsci/ec2-fleet-plugin/releases](https://github.com/jenkinsci/ec2-fleet-plugin/releases)  
25. EC2 Fleet and Spot Fleet \- Amazon Elastic Compute Cloud, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Fleets.html)  
26. Deploy Jenkins agents using EC2 Spot instances by Sai Dilip \- Medium, 11月 17, 2025にアクセス、 [https://medium.com/sai-ops/deploy-jenkins-agents-using-ec2-spot-instances-44b02f68cd](https://medium.com/sai-ops/deploy-jenkins-agents-using-ec2-spot-instances-44b02f68cd)  
27. Did You Know That There Is an Amazon EC2 Spot Fleet Plugin for Jenkins? \- YouTube, 11月 17, 2025にアクセス、 [https://www.youtube.com/watch?v=8gGItacZjps](https://www.youtube.com/watch?v=8gGItacZjps)  
28. Orchestrate Jenkins Workloads using Dynamic Pod Autoscaling with Amazon EKS AWS DevOps & Developer Productivity Blog, 11月 17, 2025にアクセス、 [https://aws.amazon.com/blogs/devops/orchestrate-jenkins-workloads-using-dynamic-pod-autoscaling-with-amazon-eks/](https://aws.amazon.com/blogs/devops/orchestrate-jenkins-workloads-using-dynamic-pod-autoscaling-with-amazon-eks/)  
29. Scaling Jenkins on Kubernetes, 11月 17, 2025にアクセス、 [https://www.jenkins.io/doc/book/scaling/scaling-jenkins-on-kubernetes/](https://www.jenkins.io/doc/book/scaling/scaling-jenkins-on-kubernetes/)  
30. Kubernetes plugin \- Jenkins, 11月 17, 2025にアクセス、 [https://www.jenkins.io/doc/pipeline/steps/kubernetes/](https://www.jenkins.io/doc/pipeline/steps/kubernetes/)  
31. Install & Configure Jenkins using Amazon EC2 — Linux 2 AMI by Virat bhavsar Medium, 11月 17, 2025にアクセス、 [https://medium.com/@bvirat/install-configure-jenkins-using-amazon-ec2-linux-2-ami-83b33791b4bc](https://medium.com/@bvirat/install-configure-jenkins-using-amazon-ec2-linux-2-ami-83b33791b4bc)  
32. EKS Cluster Autoscaler: 6 Best Practices For Effective Autoscaling \- Cast AI, 11月 17, 2025にアクセス、 [https://cast.ai/blog/eks-cluster-autoscaler-6-best-practices-for-effective-autoscaling/](https://cast.ai/blog/eks-cluster-autoscaler-6-best-practices-for-effective-autoscaling/)  
33. Chapter 3: Cluster Autoscaling \- Kubernetes Guides \- Apptio, 11月 17, 2025にアクセス、 [https://www.apptio.com/topics/kubernetes/autoscaling/cluster/](https://www.apptio.com/topics/kubernetes/autoscaling/cluster/)  
34. EKS Auto Mode & Karpenter: Supercharge your Kubernetes Management \- nOps, 11月 17, 2025にアクセス、 [https://www.nops.io/blog/revolutionizing-kubernetes-management-with-eks-auto-mode-karpenter/](https://www.nops.io/blog/revolutionizing-kubernetes-management-with-eks-auto-mode-karpenter/)  
35. Karpenter vs. Cluster Autoscaler \- Kubernetes Scaling Tools \- Spacelift, 11月 17, 2025にアクセス、 [https://spacelift.io/blog/karpenter-vs-cluster-autoscaler](https://spacelift.io/blog/karpenter-vs-cluster-autoscaler)  
36. Cluster Autoscaler Vs Karpenter: The Essential Guide \- nOps, 11月 17, 2025にアクセス、 [https://www.nops.io/blog/karpenter-vs-cluster-autoscaler-vs-nks/](https://www.nops.io/blog/karpenter-vs-cluster-autoscaler-vs-nks/)  
37. Cluster AutoScaler Setup on AWS EKS: A Comprehensive Guide \- DevOpsCube, 11月 17, 2025にアクセス、 [https://devopscube.com/cluster-autoscaler/](https://devopscube.com/cluster-autoscaler/)  
38. Cluster Autoscaler \- Amazon EKS \- AWS Documentation, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/eks/latest/best-practices/cas.html](https://docs.aws.amazon.com/eks/latest/best-practices/cas.html)  
39. Amazon EKS Autoscaling: Optimize with Karpenter & Autoscaler \- StormIT, 11月 17, 2025にアクセス、 [https://www.stormit.cloud/blog/aws-eks-autoscaling/](https://www.stormit.cloud/blog/aws-eks-autoscaling/)  
40. Scale cluster compute with Karpenter and Cluster Autoscaler \- Amazon EKS, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html)  
41. Implementing Karpenter on EKS and Autoscaling Your Cluster for Optimal Performance, 11月 17, 2025にアクセス、 [https://dhruv-mavani.medium.com/implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance-f01a507a8f70](https://dhruv-mavani.medium.com/implementing-karpenter-on-eks-and-autoscaling-your-cluster-for-optimal-performance-f01a507a8f70)  
42. EKS Karpenter: Deep Dive \- stormforge.io, 11月 17, 2025にアクセス、 [https://stormforge.io/kubernetes-autoscaling/eks-karpenter/](https://stormforge.io/kubernetes-autoscaling/eks-karpenter/)  
43. Karpenter \- Amazon EKS \- AWS Documentation, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html](https://docs.aws.amazon.com/eks/latest/best-practices/karpenter.html)  
44. Getting Started with Karpenter, 11月 17, 2025にアクセス、 [https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/](https://karpenter.sh/docs/getting-started/getting-started-with-karpenter/)  
45. Building a serverless Jenkins environment on AWS Fargate, 11月 17, 2025にアクセス、 [https://aws.amazon.com/blogs/devops/building-a-serverless-jenkins-environment-on-aws-fargate/](https://aws.amazon.com/blogs/devops/building-a-serverless-jenkins-environment-on-aws-fargate/)  
46. jenkinsci/amazon-ecs-plugin: Amazon EC2 Container Service Plugin for Jenkins \- GitHub, 11月 17, 2025にアクセス、 [https://github.com/jenkinsci/amazon-ecs-plugin](https://github.com/jenkinsci/amazon-ecs-plugin)  
47. Amazon Elastic Container Service (ECS) / Fargate \- Jenkins Plugins, 11月 17, 2025にアクセス、 [https://plugins.jenkins.io/amazon-ecs](https://plugins.jenkins.io/amazon-ecs)  
48. Amazon Elastic Container Service (ECS) / Fargate Jenkins plugin, 11月 17, 2025にアクセス、 [https://plugins.jenkins.io/amazon-ecs/](https://plugins.jenkins.io/amazon-ecs/)  
49. Jenkins with AWS Fargate using ECS-Fargate plugin \- Stack Overflow, 11月 17, 2025にアクセス、 [https://stackoverflow.com/questions/66705333/jenkins-with-aws-fargate-using-ecs-fargate-plugin](https://stackoverflow.com/questions/66705333/jenkins-with-aws-fargate-using-ecs-fargate-plugin)  
50. Jenkins on AWS: A Deep Dive into CI/CD Best Practices by Vagharsh Kandilian \- Medium, 11月 17, 2025にアクセス、 [https://medium.com/@vagharshkandilian/jenkins-on-aws-a-deep-dive-into-ci-cd-best-practices-b5b57665030a](https://medium.com/@vagharshkandilian/jenkins-on-aws-a-deep-dive-into-ci-cd-best-practices-b5b57665030a)  
51. Get started with AWS Fargate for your cluster \- Amazon EKS, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html](https://docs.aws.amazon.com/eks/latest/userguide/fargate-getting-started.html)  
52. EKS Fargate Profile setup EKS Tutorial for Beginners \- 7 \- YouTube, 11月 17, 2025にアクセス、 [https://www.youtube.com/watch?v=KahZJkMpcEw](https://www.youtube.com/watch?v=KahZJkMpcEw)  
53. Deploy a Jenkins on AWS (with fargate): ECS or EKS : r/jenkinsci \- Reddit, 11月 17, 2025にアクセス、 [https://www.reddit.com/r/jenkinsci/comments/13i83jj/deploy\_a\_jenkins\_on\_aws\_with\_fargate\_ecs\_or\_eks/](https://www.reddit.com/r/jenkinsci/comments/13i83jj/deploy_a_jenkins_on_aws_with_fargate_ecs_or_eks/)  
54. How to build container images with Amazon EKS on Fargate, 11月 17, 2025にアクセス、 [https://aws.amazon.com/blogs/containers/how-to-build-container-images-with-amazon-eks-on-fargate/](https://aws.amazon.com/blogs/containers/how-to-build-container-images-with-amazon-eks-on-fargate/)  
55. difference between EKS, ECS and Autoscaling for a simple backend server : r/aws \- Reddit, 11月 17, 2025にアクセス、 [https://www.reddit.com/r/aws/comments/mqbcg3/difference\_between\_eks\_ecs\_and\_autoscaling\_for\_a/](https://www.reddit.com/r/aws/comments/mqbcg3/difference_between_eks_ecs_and_autoscaling_for_a/)  
56. Using Karpenter With EKS Fargate To Cut Costs On EKS Infrastructure \- CloudZero, 11月 17, 2025にアクセス、 [https://www.cloudzero.com/blog/using-karpenter-with-eks-fargate/](https://www.cloudzero.com/blog/using-karpenter-with-eks-fargate/)  
57. Security best practices \- AWS Prescriptive Guidance, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html](https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-aws-provider-best-practices/security.html)  
58. Security best practices in IAM \- AWS Identity and Access Management, 11月 17, 2025にアクセス、 [https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)  
59. Question about AWS Access and Secret keys vs. Roles? \- Reddit, 11月 17, 2025にアクセス、 [https://www.reddit.com/r/aws/comments/o6phoz/question\_about\_aws\_access\_and\_secret\_keys\_vs\_roles/](https://www.reddit.com/r/aws/comments/o6phoz/question_about_aws_access_and_secret_keys_vs_roles/)  
60. Setting up Jenkins to Access AWS Accounts Securely Using IAM ..., 11月 17, 2025にアクセス、 [https://medium.com/@miriyalasurendra99/setting-up-jenkins-to-access-aws-accounts-securely-using-iam-roles-9c7dcb6fd7ef](https://medium.com/@miriyalasurendra99/setting-up-jenkins-to-access-aws-accounts-securely-using-iam-roles-9c7dcb6fd7ef)  
61. How To Authenticate to AWS with the Pipeline AWS Plugin \- CloudBees Documentation, 11月 17, 2025にアクセス、 [https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/client-and-managed-controllers/how-to-authenticate-to-aws-with-the-pipeline-aws-plugin](https://docs.cloudbees.com/docs/cloudbees-ci-kb/latest/client-and-managed-controllers/how-to-authenticate-to-aws-with-the-pipeline-aws-plugin)  
62. Jenkins controller \<---\> agent communication with Docker Swarm \- Ask a question, 11月 17, 2025にアクセス、 [https://community.jenkins.io/t/jenkins-controller-agent-communication-with-docker-swarm/23777](https://community.jenkins.io/t/jenkins-controller-agent-communication-with-docker-swarm/23777)
