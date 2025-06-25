---
audio: /share-deepresearch/assets/audio/github-hosted-runner.mp3
category: engineering
date: 2025-06-24
ga4_metrics:
  avgSessionDuration: 104.53800833333334
  pageViews: 1
  users: 2
layout: topic
prompt: GitHub Actionsで使用できるGitHubホステッドランナーについて、自前でセルフホステッドランナーを用意するより価格的に安いのか比較を行いたい。larger
  runnersも含めてGitHubで使用できるランナーのスペックと同じスペックでクラウドサービスを用いてセルフホステッドランナーを作成した際の価格の調査を行って欲しい。
supplementary_materials:
- title: GitHub Actionsランナー：ホステッド vs セルフホステッド コスト分析
  url: /share-deepresearch/topics/github-hosted-runner/infographic.html
- title: コストと価値の真実：GitHubホステッド vs セルフホステッド 完全比較
  url: /share-deepresearch/topics/github-hosted-runner/reveal.html
tags:
- GitHub Actions
- 自動化
- 開発環境
title: 包括的コスト分析：GitHub ActionsにおけるGitHubホステッドランナー vs. セルフホステッドランナー
---

# **包括的コスト分析：GitHub ActionsにおけるGitHubホステッドランナー vs. セルフホステッドランナー**

## **セクション1：GitHubホステッドランナーエコシステム：比較のベースライン**

GitHub Actionsのコスト構造を評価するにあたり、まずGitHubが提供するフルマネージドサービスであるGitHubホステッドランナーの性能とコストのベースラインを確立することが不可欠です。このサービスを理解することは、セルフホステッド（自己ホスト型）の代替案と正確な「同一条件下での」比較を行うための基礎となります。

### **1.1. ランナーの仕様とサービス階層**

GitHubは、様々なワークロードに合わせて調整された仮想マシン（VM）の階層システムを提供しています。これらの仕様は、ランナーのティア（Standard、Larger、GPU）だけでなく、リポジトリの可視性（パブリックかプライベートか）によっても異なり、これはコスト計画における重要なニュアンスです 1。

* **Standard Runners（プライベートリポジトリ）:** LinuxおよびWindows環境では、2コアCPU、7 GB RAM、14 GB SSDが標準仕様です。macOS環境では、3コア（M1）または4コア（Intel）のCPUが提供されます 1。これらは最も一般的に利用されるランナーです。  
* **Standard Runners（パブリックリポジトリ）:** パブリックリポジトリで利用できる標準ランナーは、プライベートリポジトリ向けよりも高性能で、LinuxおよびWindows環境で4コアCPUと16 GB RAMを備えており、無料で提供されます 1。この点は、パブリックリポジトリに対してセルフホスティングがコスト効率の面で有利になるケースはほとんどないことを示唆しています。  
* **Larger Runners（Linux & Windows）:** GitHub TeamおよびEnterpriseプランでのみ利用可能な高性能オプションです 4。スペックは2コア/8GB RAMから始まり、最大で96コア/384GB RAMまでスケールし、SSDストレージも最大2040 GBと大幅に増加します 4。  
* **Larger Runners（macOS）:** macOS向けには、特定のIntel（12コア/30GB）およびARM/M1（6コア/14GB）構成が用意されています 4。  
* **GPU-Powered Runners:** 機械学習（ML）や人工知能（AI）のワークロード向けに、NVIDIA Tesla T4 GPUを搭載した特殊な4コアランナーも利用可能です 6。

### **1.2. GitHubの価格モデル：分単位の料金、無料枠、そして乗数**

GitHubの価格設定は、柔軟性の高い従量課金制の分単位モデルを採用しています。しかし、最終的なコストは、ユーザーの契約プラン（無料利用枠の分数を決定）と、使用するオペレーティングシステム（コスト乗数を適用）に影響されます。

* **分単位の料金:** 各ランナータイプ（Linux、Windows、macOS、x86、ARM、GPU）には、詳細な分単位の料金が設定されています 7。例えば、標準のLinux 2コアランナーは  
  0.008/分、macOSM1ランナーは0.08/分です。  
* **無料利用枠:** 各GitHubプラン（Free、Pro、Team、Enterprise）には、*プライベートリポジトリの標準ランナー*で使用できる月間の無料分数が含まれています 7。  
* **重要な制限:** 含まれている無料分数は、**Larger Runnersには使用できません**。Larger Runnersは、パブリックリポジトリでの使用であっても、常に課金対象となります 4。これは、Larger Runnersが標準サービスとは根本的に異なるプレミアムティアであることを示しており、パフォーマンスを必要とする組織をターゲットにしていることを意味します。  
* **課金のニュアンス:** ジョブは1分単位で課金され、1分未満は切り上げられます。つまり、31秒のジョブは1分として請求されます 9。さらに、GitHubは内部的に「分単位の乗数」システムを使用しています。WindowsジョブはLinuxジョブの2倍、macOSジョブは10倍の速さで無料枠の分数を消費します 8。例えば、GitHub Teamプラン（無料枠3,000分）のユーザーがmacOSジョブを1分実行すると、無料枠から10分が消費されます。これにより、無料から有料への移行が加速するため、コスト予測においてこの乗数を考慮することが極めて重要です。

### **1.3. 価値提案：利便性、メンテナンス、セキュリティ**

GitHubホステッドランナーの表示価格には、重要な無形の価値が含まれています。これらは、GitHubによって完全に管理され、パッチ適用、セキュリティ保護、スケーリングが自動的に行われる、ジョブごとに破棄される（エフェメラルな）環境です。これにより、ユーザーのエンジニアリングチームは、インフラストラクチャの運用に関する大きな負担から解放されます。

* **フルマネージド:** GitHubがすべてのマシンのメンテナンスとアップグレードを担当します 1。環境はジョブごとにディスクが再イメージ化されるため、セキュリティと一貫性が保たれます 12。  
* **セキュリティ:** GitHubは、各ジョブにネットワーク分離を提供する多層防御、ゼロトラストのアプローチを採用しています 12。  
* **サポート:** サービスには24時間365日のサポートが含まれており、ユーザーがインフラの問題をトラブルシューティングする必要がありません 12。  
* **シンプルさ:** 主な利点は、セットアップとメンテナンスが不要であることであり、チームはインフラ管理ではなく開発に集中できます 12。

## **セクション2：直接的なコンピュートコストの比較：パブリッククラウドでのセルフホスティング**

このセクションでは、主要なパブリッククラウド（AWS、GCP、Azure）上で同等のVMインスタンスを自己ホストした場合の、純粋なコンピュートコストを「同一条件下」で比較します。ここでは、柔軟な比較のためにオンデマンド価格を使用しますが、リザーブドインスタンスやSavings Plansなどの割引プランがこれらの数値を変更しうることを念頭に置く必要があります。

### **2.1. Linuxランナーの同等インスタンス（x86 & ARM）**

GitHubの各LinuxランナーのvCPU、RAM、アーキテクチャ（x86/ARM）に合致するVMを主要クラウドから選定し、その時間単価を比較します。一見すると、セルフホスティングの方が圧倒的に安価に見えます。例えば、GitHubの標準2コアLinuxランナーの時間単価は$0.48（0.008/分×60分）ですが、AWSの同等インスタンスである‘t4g.medium‘（ARM）は約0.0336/時です 7。しかし、この数値は純粋なコンピュートコストのみを反映しており、後述する総所有コスト（TCO）とは異なることに注意が必要です。

ARMベースのインスタンス（AWS Graviton、GCP Tau T2A、Azure Dplsv5など）は、同等のx86インスタンスと比較して、すべてのクラウドで一貫して30-60%安価です 15。これは、x86アーキテクチャに依存しないワークロード（最新のコンテナ化されたアプリケーションなど）の場合、セルフホスティングにおいてARMを選択することが主要なコスト削減策となることを示唆しています。

**表2.1：Linux VMのオンデマンドコスト比較（時間単価）**

| GitHubランナー仕様 (vCPU/RAM/SSD) | GitHub時間単価 (USD) | AWS同等インスタンス (時間単価 USD) | GCP同等インスタンス (時間単価 USD) | Azure同等インスタンス (時間単価 USD) |
| :---- | :---- | :---- | :---- | :---- |
| **Standard x64** (2-core / 7GB / 14GB) | $0.48 | m6a.large (2/8GB): $0.0864 17 | n2-standard-2 (2/8GB): $0.0971 18 | Standard\_D2s\_v5 (2/8GB): $0.0832 19 |
| **Standard ARM** (2-core / 8GB / 75GB) | $0.30 | t4g.large (2/8GB): $0.0672 20 | t2a-standard-2 (2/8GB): $0.077 21 | Standard\_D2pls\_v5 (2/4GB): $0.068 22 |
| **Larger x64** (4-core / 16GB / 150GB) | $0.96 | m6a.xlarge (4/16GB): $0.1728 23 | n2-standard-4 (4/16GB): $0.1942 24 | Standard\_D4s\_v5 (4/16GB): $0.166 19 |
| **Larger ARM** (4-core / 16GB / 150GB) | $0.60 | t4g.xlarge (4/16GB): $0.1344 14 | t2a-standard-4 (4/16GB): $0.154 21 | Standard\_D4pls\_v5 (4/16GB): $0.137 19 |
| **Larger x64** (8-core / 32GB / 300GB) | $1.92 | m6a.2xlarge (8/32GB): $0.3456 25 | n2-standard-8 (8/32GB): $0.3885 24 | Standard\_D8s\_v5 (8/32GB): $0.333 19 |
| **Larger x64** (16-core / 64GB / 600GB) | $3.84 | m6a.4xlarge (16/64GB): $0.6912 25 | n2-standard-16 (16/64GB): $0.7769 24 | Standard\_D16s\_v5 (16/64GB): $0.666 19 |
| **Larger x64** (32-core / 128GB / 1200GB) | $7.68 | m6a.8xlarge (32/128GB): $1.3824 25 | n2-standard-32 (32/128GB): $1.5539 24 | Standard\_D32s\_v5 (32/128GB): $1.331 19 |
| **Larger x64** (64-core / 256GB / 2040GB) | $15.36 | m6a.16xlarge (64/256GB): $2.7648 25 | n2-standard-64 (64/256GB): $3.1078 24 | Standard\_D64s\_v5 (64/256GB): $2.662 19 |
| **Larger x64** (96-core / 384GB / 2040GB) | $23.04 | m6a.24xlarge (96/384GB): $4.1472 25 | n2-standard-96 (96/384GB): $4.6616 24 | Standard\_D96s\_v5 (96/384GB): $3.994 19 |

*注：クラウドプロバイダーの価格は、リージョンやオンデマンドの価格変動により異なる場合があります。上記はus-east-1（AWS）、us-central1（GCP）、East US（Azure）などの主要リージョンに基づいています。*

### **2.2. Windowsランナーの同等インスタンス（x86 & ARM）**

Windowsランナーの比較も同様のプロセスをたどりますが、クラウドプラットフォームではWindows Serverのライセンスコストが時間単価に上乗せされるため、ハードウェアが同一でもLinux VMより本質的に高価になります 19。

**表2.2：Windows VMのオンデマンドコスト比較（時間単価）**

| GitHubランナー仕様 (vCPU/RAM/SSD) | GitHub時間単価 (USD) | AWS同等インスタンス (時間単価 USD) | GCP同等インスタンス (時間単価 USD) | Azure同等インスタンス (時間単価 USD) |
| :---- | :---- | :---- | :---- | :---- |
| **Standard x64** (2-core / 7GB / 14GB) | $0.96 | m6a.large: $0.1824 26 | n2-standard-2: $0.1585 24 | Standard\_D2s\_v5: $0.126 19 |
| **Larger x64** (4-core / 16GB / 150GB) | $1.92 | m6a.xlarge: $0.3648 26 | n2-standard-4: $0.3394 24 | Standard\_D4s\_v5: $0.252 19 |
| **Larger x64** (8-core / 32GB / 300GB) | $3.84 | m6a.2xlarge: $0.7296 26 | n2-standard-8: $0.6788 24 | Standard\_D8s\_v5: $0.504 19 |
| **Larger x64** (16-core / 64GB / 600GB) | $7.68 | m6a.4xlarge: $1.4592 26 | n2-standard-16: $1.3575 24 | Standard\_D16s\_v5: $1.008 19 |

### **2.3. macOSの特異性：専用ホストと24時間の最低利用料金**

クラウドでmacOSをホストすることは、LinuxやWindowsとは根本的に異なります。Appleの厳格なライセンス契約により、AWSのようなプロバイダーは、標準的なマルチテナント、分単位課金の仮想macOSインスタンスを提供できません。その代わりに、顧客一人に物理的なMac Mini全体を貸し出す「専用ホスト」モデルを採用しています 27。

このモデルは、特に断続的なCI/CDワークロードにとって、壊滅的なコスト影響をもたらします。Appleのライセンスは24時間の最低リース期間を義務付けているため、一度Macホストを割り当てると、たとえ10分のビルドにしか使用しなくても、丸24時間分の料金が請求されます 29。この「macOSコストトラップ」により、短時間のジョブであってもセルフホスティングのコストがGitHubホステッドの20倍以上になる可能性があります。セルフホスティングが経済的に成り立つのは、24時間のウィンドウのかなりの部分でマシンが利用される場合に限られ、これはほとんどのCIワークフローには当てはまりません。

**表2.3：macOSランナーの断続的ワークロードにおける実効コスト比較**

| GitHubランナー仕様 | GitHub分単価 | 30分ジョブのコスト (GitHub) | セルフホスト同等インスタンス (AWS) | セルフホスト最低請求額 (24時間) | 30分ジョブのコスト (セルフホスト) | コスト倍率 (セルフホスト vs. GitHub) |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| **Standard M1** (3-core/7GB) | $0.08 | $2.40 | mac2.metal (M2 Pro) | \~$37.44 32 | $37.44 | \~15.6倍 |
| **Standard Intel** (4-core/14GB) | $0.08 | $2.40 | mac1.metal (Intel i7) | \~$25.99 29 | $25.99 | \~10.8倍 |
| **Larger M1** (6-core/14GB) | $0.16 | $4.80 | mac2.metal (M2 Pro) | \~$37.44 32 | $37.44 | \~7.8倍 |
| **Larger Intel** (12-core/30GB) | $0.12 | $3.60 | mac1.metal (Intel i7) | \~$25.99 29 | $25.99 | \~7.2倍 |

## **セクション3：総所有コスト（TCO）：セルフホスティングの隠れたコストを暴く**

直接的なコンピュートコストの比較だけでは、セルフホスティングの真の経済性は見えません。このセクションでは、セルフホストソリューションの真のTCOを定義する、しばしば過小評価されがちな運用コストと間接コストを分析します。

### **3.1. 人的要因：インフラ管理オーバーヘッドの定量化**

セルフホスティングにおける最大の隠れたコストは、インフラを管理するために必要なエンジニアリング時間です。これは一度きりのセットアップコストではなく、継続的な運用上の負担となります 12。エンジニアは、AMIのメンテナンス、セキュリティパッチの適用、インフラの監視、ランナーAPIの問題のトラブルシューティング、スケーリングソリューションの管理などを継続的に行う必要があります 34。

シニアエンジニアが業務時間の20%から50%をDevOps/インフラ関連のタスクに費やしているという報告もあり 36、インフラが最適化されていない場合、開発チーム全体の時間を奪うことになります 37。開発者一人当たり週に1時間の無駄な時間が、年間で$4,000以上のコストに相当するという試算もあります 12。この「人的コスト」を定量化するために、以下の表では、保守にかかる時間を給与相当額に換算しています。

**表3.1：セルフホステッドランナーフリートの推定年間人的オーバーヘッドコスト**

| フリート規模 (ランナー数) | 推定年間保守時間 (時間) | エンジニア時間単価 (混合) | 年間総人的コスト (USD) |
| :---- | :---- | :---- | :---- |
| 5 | 208 (週4時間) | $75 | $15,600 |
| 20 | 416 (週8時間) | $75 | $31,200 |
| 100 | 1040 (週20時間) | $75 | $78,000 |

*注：保守時間は、パッチ適用、監視、トラブルシューティング、スケーリング管理などを含む保守的な推定値です。*

### **3.2. ネットワーク料金：データエグレス（送出）料金のモデリング**

クラウドプロバイダーは、自社のネットワークからデータが送出される際に料金を請求します（エグレス料金）。CI/CDの文脈では、Dockerイメージのようなアーティファクトを外部レジストリにプッシュする際にこれが発生します。これらの料金はかなりの額になる可能性があり、初期のコスト見積もりでは見落とされがちです。

AWS、GCP、Azureは、通常、小規模な無料枠を超えた後、約$0.08～$0.09/GBから始まる段階的なエグレス料金を設定しています 15。これに対し、GitHubホステッドランナーは

**ネットワークエグレス料金を請求しない**という、認識されにくい大きな金銭的利点があります 12。

例えば、あるチームが1GBのDockerイメージを1日に50回プッシュする一般的なシナリオを考えてみましょう。これは月間約1.5 TBのエグレスに相当します。0.09/GBの料金で、これは月額約135の追加の隠れたコストとなり、小規模なランナーのコンピュートコストを簡単に上回る可能性があります 35。

### **3.3. コンピュート以外のコスト：ストレージ、スケーラビリティ、アイドル容量**

セルフホステッドランナーは、OS、ワークスペース、キャッシュのために永続的なブロックストレージを必要とします。AWS EBS、GCP Persistent Disk、Azure Managed Disksの料金は、GB/月単位で課金され、一般的な150GBのSSDはランナー1台あたり月額$12～$15の追加コストとなり得ます 40。

さらに、ジョブの即時利用可能性を確保するために、しばしばアイドル状態のVMの「ウォームプール」を稼働させることになります。これらのVMは、ジョブが実行されていなくても24時間365日コストが発生します。これは、アクティブなジョブ実行時間のみを請求するGitHubのオンデマンドモデルとは対照的です 35。

このアイドルコストを削減しようとすると、自己ホストの複雑性が増すという悪循環に陥ることがあります。例えば、アイドル容量のコストを削減するためにオートスケーラーを導入すると、そのセットアップと維持の複雑さから人的コストが大幅に増加します 34。コンピュートコストを直接削減するためにスポットインスタンスを利用すると、ジョブ失敗のリスクが導入され、これもまた管理のための人的コストを増加させます 33。

このことから、セルフホスティングは独立したコスト削減策の集合ではなく、トレードオフの相互接続されたシステムであることがわかります。あるコストを最適化しようとすると、別のコストが増加する傾向があるのです。

## **セクション4：データの統合：意思決定フレームワーク**

このセクションでは、定量的なデータと定性的なデータを統合し、ユーザーの意思決定を導くための実践的なツールとモデルを提示します。

### **4.1. 損益分岐点の計算：TCO調整モデル**

セルフホスティングがGitHubホステッドランナーよりもコスト効率が高くなる月間のビルド時間の損益分岐点を分析します。このモデルには、セクション3で詳述したTCO要因（人的コスト、ネットワークコストなど）が組み込まれています。

* GitHubコストの計算式:  
  CostGitHub​=(TotalMinutes−FreeMinutes)×PerMinuteRate  
* セルフホストTCOの計算式:  
  TCOSelfHosted​=(UsageHours×VMHourlyRate​)+IdleCost+StorageCost+EgressCost+HumanOverheadCost

単純なコンピュートコストの比較では、セルフホスティングは非常に低い使用時間で元が取れるように見えます。しかし、月額数百ドルから数千ドルに及ぶ可能性のある人的オーバーヘッドやその他のTCOコストを考慮に入れると、損益分岐点は劇的に高くなります。

多くの一般的なユースケースでは、これらの「隠れた」TCOコストが直接的なコンピュートコストを上回り、当初は安価に見えたセルフホスティングが、実際にはGitHubのマネージドサービスよりも高価になる「TCOの逆転」現象が起こり得ます。したがって、セルフホスティングへの移行決定は、CI/CDの量だけでなく、組織内部のDevOpsの成熟度を評価することと同義になります。

### **4.2. コストを超えて：定性的スコアカード**

決定は純粋に金銭的なものだけではありません。セキュリティ体制、開発速度、運用管理などの要因が最も重要です。以下のスコアカードは、これらの定性的な側面を視覚的に比較するものです。

**表4.2：定性的意思決定マトリクス（GitHubホステッド vs. セルフホステッド）**

| 評価項目 | GitHubホステッド (評価 1-5) | セルフホステッド (評価 1-5) | 主な考慮事項 |
| :---- | :---- | :---- | :---- |
| **コスト予測性** | ⭐️⭐️⭐️⭐️ | ⭐️⭐️ | GitHubは従量課金で予測しやすい。セルフホストは隠れたコストが多く変動しやすい。 |
| **セットアップと保守の手間** | ⭐️⭐️⭐️⭐️⭐️ | ⭐️ | GitHubはゼロメンテナンス。セルフホストは継続的な人的リソースを必要とする 44。 |
| **セキュリティ責任** | ⭐️⭐️⭐️⭐️⭐️ | ⭐️⭐️ | GitHubはインフラのセキュリティを管理。セルフホストはネットワーク、イメージ、キャッシュの全てが自己責任となる 12。 |
| **パフォーマンスとカスタマイズ** | ⭐️⭐️⭐️ | ⭐️⭐️⭐️⭐️⭐️ | セルフホストはハードウェア、OS、ツールを完全に制御可能 44。GitHubは定義済みの環境のみ。 |
| **スケーラビリティ** | ⭐️⭐️⭐️⭐️ | ⭐️⭐️⭐️ | GitHubは自動でスケール。セルフホストはオートスケーラーの構築と維持に多大な労力を要する 12。 |
| **導入までのスピード** | ⭐️⭐️⭐️⭐️⭐️ | ⭐️⭐️ | GitHubは即時利用可能。セルフホストはインフラのプロビジョニングに時間がかかる。 |

### **4.3. ハイブリッド戦略：両方の長所を活かす最適化**

最適な解決策は、二者択一であることは稀です。洗練されたハイブリッドアプローチは、コスト効率とパフォーマンスを最大化することができます。

* **標準的で頻度の低いワークロード、特にすべてのmacOSビルド**には、GitHubホステッドランナーを使用します。これにより、macOSの24時間最低料金というコストトラップを回避できます。  
* **特定のユースケース**には、セルフホステッドランナーを使用します：  
  * **大量または長時間のジョブ：** 専用の強力なマシンを何時間も稼働させることで、セルフホスティングが安価になります。  
  * **特殊なハードウェア：** GPUやGitHubが提供していないその他の特定のハードウェアを必要とするジョブ。  
  * **厳格なセキュリティ/コンプライアンス：** コードとアーティファクトが組織のプライベートネットワーク（VPC）内に留まる必要がある場合。  
  * **大規模なキャッシュ：** ビルドがGitHubの10GBのキャッシュサイズ制限を超えるキャッシュを必要とする場合 35。

このハイブリッドモデルは、コスト最適化だけでなく、インフラのリスクを軽減する戦略的な方法でもあります。主要なタスクをGitHubに依存することで、自社のセルフホストフリートがダウンした場合でも、開発者はubuntu-latestなどに切り替えて作業を続けることができ、インフラ問題が開発の完全なブロッカーになるのを防ぎます 12。

## **セクション5：戦略的推奨事項と結論**

この最終セクションでは、レポートの調査結果を要約し、異なる組織プロファイルに合わせた明確で実行可能な推奨事項を提供します。

### **5.1. 小規模チームおよびスタートアップ（エンジニア15人未満）への推奨事項**

**推奨事項：** 圧倒的にGitHubホステッドランナーを支持します。

**正当化：** この規模では、セルフホスティングのTCO、特に人的コストは法外に高くなります。CI/CDの分単位料金を節約するよりも、製品開発に費やされるエンジニアリング時間の価値の方がはるかに高いです。多くの場合、無料利用枠で十分です。

### **5.2. 成長中の組織（エンジニア15～100人）への推奨事項**

**推奨事項：** まずGitHubホステッドランナーから始めます。コストが重要な閾値（例：月額$1,000～$2,000）を超えたら、**最も量が多く、安定的で、macOS以外のワークロードに限定して**セルフホスティングのパイロットプロジェクトを開始します。

**正当化：** このグループにとって、損益分岐点分析が最も重要になります。コストの圧力を感じている一方で、開発速度に影響を与えることなく完全なセルフホストフリートのTCOを吸収するための専任リソースがない可能性があります。ハイブリッドアプローチが理想的です。

### **5.3. 大企業（エンジニア100人以上）への推奨事項**

**推奨事項：** ハイブリッド戦略がほぼ確実に最もコスト効率が高いです。リザーブドインスタンスやSavings Plansを活用して、ベースラインとなるLinux/Windowsワークロード用にセルフホステッドランナーのフリートを積極的に管理します。

**正当化：** この規模では、CI/CDの実行量が多いため、GitHubホステッドランナーの分単位コストが重要な費用項目となります。組織には、セルフホストインフラを効率的に管理できる専任のプラットフォーム/DevOpsチームが存在する可能性が高く、相対的な「人的コスト」が低くなります。セキュリティやコンプライアンスの要件から、特定のプロジェクトでセルフホスティングが義務付けられることもあります。それでもなお、macOSやバースト/フェイルオーバー容量としてGitHubホステッドランナーを使用すべきです。

### **5.4. 最終結論：運用上の優先順位に関する戦略的評価**

GitHubホステッドランナーとセルフホステッドランナーの選択は、単なる費用項目の比較ではありません。それは、組織が最も価値のあるリソース、すなわちエンジニアリング時間をどこに投資するかという戦略的な決定です。

GitHubホステッドランナーは、開発者のベロシティと運用のシンプルさへの投資を意味します。一方、セルフホスティングは、直接的なコスト削減とインフラの制御への投資であり、その対価としてエンジニアリングの複雑性と運用オーバーヘッドを支払うことになります。「より安価な」選択肢は、組織の規模、成熟度、そして戦略的な優先順位に完全に依存するのです。

#### **引用文献**

1. About GitHub-hosted runners, 6月 24, 2025にアクセス、 [https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-github-hosted-runners/about-github-hosted-runners)  
2. Choosing the runner for a job \- GitHub Docs, 6月 24, 2025にアクセス、 [https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job](https://docs.github.com/en/actions/writing-workflows/choosing-where-your-workflow-runs/choosing-the-runner-for-a-job)  
3. Types of Runners \- KodeKloud Notes, 6月 24, 2025にアクセス、 [https://notes.kodekloud.com/docs/GitHub-Actions-Certification/Self-Hosted-Runner/Types-of-Runners](https://notes.kodekloud.com/docs/GitHub-Actions-Certification/Self-Hosted-Runner/Types-of-Runners)  
4. GitHub Actions Price Calculator \- Depot, 6月 24, 2025にアクセス、 [https://depot.dev/github-actions-price-calculator](https://depot.dev/github-actions-price-calculator)  
5. Larger custom GitHub Actions runners \- RunsOn, 6月 24, 2025にアクセス、 [https://runs-on.com/github-actions/larger-runners/](https://runs-on.com/github-actions/larger-runners/)  
6. About larger runners \- GitHub Docs, 6月 24, 2025にアクセス、 [https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners](https://docs.github.com/en/actions/using-github-hosted-runners/using-larger-runners/about-larger-runners)  
7. About billing for GitHub Actions, 6月 24, 2025にアクセス、 [https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions](https://docs.github.com/en/billing/managing-billing-for-your-products/about-billing-for-github-actions)  
8. About billing for GitHub Actions, 6月 24, 2025にアクセス、 [https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions](https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions)  
9. How to reduce spend in GitHub Actions \- Blacksmith, 6月 24, 2025にアクセス、 [https://www.blacksmith.sh/blog/how-to-reduce-spend-in-github-actions](https://www.blacksmith.sh/blog/how-to-reduce-spend-in-github-actions)  
10. GitHub Actions: Complete 2025 Guide With Quick Tutorial \- Octopus Deploy, 6月 24, 2025にアクセス、 [https://octopus.com/devops/github-actions/](https://octopus.com/devops/github-actions/)  
11. GitHub's plans, 6月 24, 2025にアクセス、 [https://docs.github.com/get-started/learning-about-github/githubs-products](https://docs.github.com/get-started/learning-about-github/githubs-products)  
12. When to choose GitHub-Hosted runners or self-hosted runners with GitHub Actions, 6月 24, 2025にアクセス、 [https://github.blog/enterprise-software/ci-cd/when-to-choose-github-hosted-runners-or-self-hosted-runners-with-github-actions/](https://github.blog/enterprise-software/ci-cd/when-to-choose-github-hosted-runners-or-self-hosted-runners-with-github-actions/)  
13. Choosing GitHub Runners vs Self-Hosted Runners \- Arnica.io, 6月 24, 2025にアクセス、 [https://www.arnica.io/blog/github-hosted-or-self-hosted-runners](https://www.arnica.io/blog/github-hosted-or-self-hosted-runners)  
14. EC2 On-Demand Instance Pricing – Amazon Web Services, 6月 24, 2025にアクセス、 [https://aws.amazon.com/ec2/pricing/on-demand/](https://aws.amazon.com/ec2/pricing/on-demand/)  
15. AWS vs Azure vs GCP: Pricing Comparison to Help You Choose \- DevZero, 6月 24, 2025にアクセス、 [https://www.devzero.io/blog/aws-azure-google-price-comparison](https://www.devzero.io/blog/aws-azure-google-price-comparison)  
16. Cloud Pricing Comparison: AWS vs. Azure vs. Google Cloud Platform in 2025 \- Cast AI, 6月 24, 2025にアクセス、 [https://cast.ai/blog/cloud-pricing-comparison/](https://cast.ai/blog/cloud-pricing-comparison/)  
17. m6a.large pricing and specs \- Amazon EC2 Instance Comparison \- Vantage, 6月 24, 2025にアクセス、 [https://instances.vantage.sh/aws/ec2/m6a.large](https://instances.vantage.sh/aws/ec2/m6a.large)  
18. Google Compute Engine Machine Type n2-standard-2, 6月 24, 2025にアクセス、 [https://gcloud-compute.com/n2-standard-2.html](https://gcloud-compute.com/n2-standard-2.html)  
19. CloudPrice: Azure, AWS, GCP Instance Comparison, 6月 24, 2025にアクセス、 [https://cloudprice.net/](https://cloudprice.net/)  
20. t4g.large pricing and specs \- Amazon EC2 Instance Comparison \- Vantage, 6月 24, 2025にアクセス、 [https://instances.vantage.sh/aws/ec2/t4g.large](https://instances.vantage.sh/aws/ec2/t4g.large)  
21. Pricing Compute Engine: Virtual Machines (VMs) Google Cloud ..., 6月 24, 2025にアクセス、 [https://cloud.google.com/compute/all-pricing](https://cloud.google.com/compute/all-pricing)  
22. D2pls v5 pricing and specs \- Vantage, 6月 24, 2025にアクセス、 [https://instances.vantage.sh/azure/vm/d2pls-v5](https://instances.vantage.sh/azure/vm/d2pls-v5)  
23. m6a.xlarge specs and pricing AWS \- CloudPrice, 6月 24, 2025にアクセス、 [https://cloudprice.net/aws/ec2/instances/m6a.xlarge](https://cloudprice.net/aws/ec2/instances/m6a.xlarge)  
24. GCPinstances \- GCP Compute Engine Instance Comparison (by DoiT International), 6月 24, 2025にアクセス、 [https://gcpinstances.doit.com/](https://gcpinstances.doit.com/)  
25. m6a.2xlarge Pricing and Specs: AWS EC2, 6月 24, 2025にアクセス、 [https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/m6a.2xlarge](https://costcalc.cloudoptimo.com/aws-pricing-calculator/ec2/m6a.2xlarge)  
26. Amazon EC2 Instance Comparison, 6月 24, 2025にアクセス、 [https://instances.vantage.sh/](https://instances.vantage.sh/)  
27. How does the billing system work for macOS instances in cloud services? Is it possible to pay on an hourly basis, or are there other pricing models available? AWS re:Post, 6月 24, 2025にアクセス、 [https://repost.aws/questions/QUIU1iQmo1SJG8NIxA0bKJ8w/how-does-the-billing-system-work-for-macos-instances-in-cloud-services-is-it-possible-to-pay-on-an-hourly-basis-or-are-there-other-pricing-models-available](https://repost.aws/questions/QUIU1iQmo1SJG8NIxA0bKJ8w/how-does-the-billing-system-work-for-macos-instances-in-cloud-services-is-it-possible-to-pay-on-an-hourly-basis-or-are-there-other-pricing-models-available)  
28. Start an Amazon EC2 Mac instance \- Community.aws, 6月 24, 2025にアクセス、 [https://community.aws/content/2duUEgh4u4TIDqfECiDkEbrn2Iw/ec2-mac-01-start-an-ec2-mac-instance](https://community.aws/content/2duUEgh4u4TIDqfECiDkEbrn2Iw/ec2-mac-01-start-an-ec2-mac-instance)  
29. Mac Mini cost : r/aws \- Reddit, 6月 24, 2025にアクセス、 [https://www.reddit.com/r/aws/comments/r5n4m8/mac\_mini\_cost/](https://www.reddit.com/r/aws/comments/r5n4m8/mac_mini_cost/)  
30. Billing and cost Mac m2 Istance AWS re:Post, 6月 24, 2025にアクセス、 [https://repost.aws/questions/QURgjEEC8GTeKiGfJ8b46rkA/billing-and-cost-mac-m2-istance](https://repost.aws/questions/QURgjEEC8GTeKiGfJ8b46rkA/billing-and-cost-mac-m2-istance)  
31. What you need to know about AWS's new EC2 Mac instances \- Pluralsight, 6月 24, 2025にアクセス、 [https://www.pluralsight.com/resources/blog/cloud/what-you-need-to-know-about-awss-new-ec2-mac-instances](https://www.pluralsight.com/resources/blog/cloud/what-you-need-to-know-about-awss-new-ec2-mac-instances)  
32. AWS spins up more cloudy Mac Minis, now with M2 Pro silicon \- The Register, 6月 24, 2025にアクセス、 [https://www.theregister.com/2023/09/20/aws\_ec2\_m2\_pro\_mac/](https://www.theregister.com/2023/09/20/aws_ec2_m2_pro_mac/)  
33. Self-hosted GitHub Actions runners aren't free \- Depot, 6月 24, 2025にアクセス、 [https://depot.dev/blog/self-hosting-github-actions](https://depot.dev/blog/self-hosting-github-actions)  
34. The true cost of self-hosted GitHub Actions \- Separating fact from fiction \- RunsOn, 6月 24, 2025にアクセス、 [https://runs-on.com/blog/true-cost-of-self-hosted-runners/](https://runs-on.com/blog/true-cost-of-self-hosted-runners/)  
35. Non-obvious ways self-hosting GitHub Actions can increase CI cost. BuildPulse Blog, 6月 24, 2025にアクセス、 [https://buildpulse.io/blog/unobvious-pitfalls-of-github-actions-hosted-runners](https://buildpulse.io/blog/unobvious-pitfalls-of-github-actions-hosted-runners)  
36. As a Sr. S.Eng, how much time do you spend, in %, on DevOps related tasks? \- Reddit, 6月 24, 2025にアクセス、 [https://www.reddit.com/r/ExperiencedDevs/comments/1cbwgkd/as\_a\_sr\_seng\_how\_much\_time\_do\_you\_spend\_in\_on/](https://www.reddit.com/r/ExperiencedDevs/comments/1cbwgkd/as_a_sr_seng_how_much_time_do_you_spend_in_on/)  
37. When to Hire Your First DevOps Engineer: A Startup Guide \- Qovery, 6月 24, 2025にアクセス、 [https://www.qovery.com/blog/when-to-hire-your-first-devops-engineer-a-startup-guide/](https://www.qovery.com/blog/when-to-hire-your-first-devops-engineer-a-startup-guide/)  
38. Cloud Pricing Comparison 2025: Compute, Storage, and Networking emma Blog, 6月 24, 2025にアクセス、 [https://www.emma.ms/blog/cloud-pricing-comparison-compute-storage-and-networking](https://www.emma.ms/blog/cloud-pricing-comparison-compute-storage-and-networking)  
39. Data Egress Cost Analysis \- AWS vs GCP vs Azure \- Sprinkle Data, 6月 24, 2025にアクセス、 [https://www.sprinkledata.com/blogs/an-analysis-of-data-egress-cost-and-how-sprinkle-saves-on-it](https://www.sprinkledata.com/blogs/an-analysis-of-data-egress-cost-and-how-sprinkle-saves-on-it)  
40. High-Performance Block Storage– Amazon EBS Pricing \- AWS, 6月 24, 2025にアクセス、 [https://aws.amazon.com/ebs/pricing/](https://aws.amazon.com/ebs/pricing/)  
41. Disk and image pricing Google Cloud, 6月 24, 2025にアクセス、 [https://cloud.google.com/compute/disks-image-pricing](https://cloud.google.com/compute/disks-image-pricing)  
42. Managed Disks pricing \- Microsoft Azure, 6月 24, 2025にアクセス、 [https://azure.microsoft.com/en-us/pricing/details/managed-disks/](https://azure.microsoft.com/en-us/pricing/details/managed-disks/)  
43. Working on a project that cuts CI costs by 50%. Looking for insights and feedback\! \- Reddit, 6月 24, 2025にアクセス、 [https://www.reddit.com/r/devops/comments/16ht2xt/working\_on\_a\_project\_that\_cuts\_ci\_costs\_by\_50/](https://www.reddit.com/r/devops/comments/16ht2xt/working_on_a_project_that_cuts_ci_costs_by_50/)  
44. GitLab CI Runners: Self-Hosted vs. Shared Runners (Pros and Cons \- DEV Community, 6月 24, 2025にアクセス、 [https://dev.to/alex\_aslam/gitlab-ci-runners-shared-vs-self-hosted-which-one-saves-your-sanity-4feb](https://dev.to/alex_aslam/gitlab-ci-runners-shared-vs-self-hosted-which-one-saves-your-sanity-4feb)
