---
audio: /share-deepresearch/assets/audio/ansible.m4a
category: engineering
date: 2025-10-27
description: AnsibleのYAML管理のベストプラクティスを探求し、煩雑化した設定を整理する方法を提案します。
ga4_metrics:
  avgSessionDuration: 3.297436
  pageViews: 2
  users: 2
layout: topic
prompt: Ansibleの良い書き方について調査したい。YAMLの数が増えて管理が煩雑になっており、どのように整理するのが良いか、事例を集めたい。
supplementary_materials:
- gslide: https://docs.google.com/presentation/d/e/2PACX-1vTZitmYWPpuMp9Njj3oUPQTNbJmVT1sXxWgycAh3uuGR9suRLhDhqvmX__bx89jbtAkwNVehwfmqgvv/pubembed?start=false&loop=false
  title: Ansibleの「良い書き方」
tags:
- リファクタリング
title: Ansibleの「良い書き方」：煩雑化したYAMLを体系的自動化資産に変えるリファクタリング戦略
video: /share-deepresearch/assets/video/ansible.mp4
---

# **Ansibleの「良い書き方」: 煩雑化したYAMLを体系的自動化資産に変えるリファクタリング戦略**

## **導入：自動化のパラドックスと本レポートの目的**

Ansibleは、そのシンプルさとエージェントレスな性質により、IT自動化の標準ツールとなりました。しかし、プロジェクトの成長に伴い、初期のシンプルさはしばしば「YAMLの無秩序な増殖（YAMLスプロール）」という問題に直面します。Playbookが肥大化し、変数ファイルが数十個に及び、どのYAMLがインフラのどの状態を定義しているのか誰も把握できなくなるのです。これは、自動化がもたらすはずの「予測可能性」と「保守性」を根本から脅かすパラドックスです。

ユーザーが直面している「YAMLの数が増えて管理が煩雑になる」という問題は、Ansibleプロジェクトのライフサイクルにおいて普遍的な課題です 1。この問題の根本原因は、技術的なものではなく、構造的なものです。

本レポートは、Red Hat Community of Practice (CoP) 3、Spacelift 4、およびAnsible公式ドキュメント 5 のベストプラクティスに基づき、煩雑化したAnsibleプロジェクトをリファクタリング（再構築）するための体系的な戦略を提示します。目的は、管理不能なYAMLファイルの集合を、テスト可能で、再利用性が高く、宣言的な「自動化資産」へと変革することです。

戦略は以下の4つの主要フェーズで構成されます。

1. **分離 (Isolation):** 環境（本番、ステージング）とシークレット（機密情報）を明確に分離する。  
2. **リファクタリング (Refactoring):** 巨大なPlaybookを「ロール（Roles）」にカプセル化し、責務を分離する。  
3. **オーケストレーション (Orchestration):** Playbookを「何を（What）」行うかの宣言的マニフェストとして再定義する。  
4. **品質保証 (Quality Assurance):** ansible-lintとMoleculeによる自動テストを導入し、保守性を担保する。

このロードマップに従うことで、YAMLの煩雑さを解消し、スケーラブルな自動化基盤を構築することが可能になります。

## **セクション 1: なぜAnsibleプロジェクトは煩雑化するのか（"YAMLスプロール"）**

問題の解決には、まず原因の特定が必要です。プロジェクトが小規模なうちは、単一のPlaybookファイルと静的なインベントリファイルで十分です 4。しかし、対象ホストの増加、環境の多様化（開発、ステージング、本番）、チームメンバーの増加に伴い、以下のようなアンチパターンが発生します。

1. **モノリシックPlaybook（巨大な単一ファイル）:** 全てのロジックを単一のPlaybookのtasks:セクションに詰め込むアプローチです。最初は手軽ですが、すぐに数千行に達し、可読性と保守性が著しく低下します 1。  
2. **環境の混在と条件分岐の乱用:** ステージング環境と本番環境の違いを、when: inventory_hostname in groups\['staging'\]のようなタスクレベルの条件分岐（when）で吸収しようと試みることです。これにより、Playbookは複雑怪奇なロジックの塊となり、どのタスクがどの環境で実行されるのか予測困難になります 5。  
3. **変数の汚染:** group_vars/allファイルに変数を集中させすぎると、意図しない変数（例：ステージング用DBパスワード）が本番環境の実行スコープに読み込まれるリスクが生じます 8。  
4. **コードの重複:** 異なるPlaybook（例：web-setup.ymlとapp-setup.yml）で同じタスク（例：「ntpの設定」や「共通パッケージのインストール」）がコピー＆ペーストされ、修正漏れや不整合（Configuration Drift）の原因となります。

これらの問題の根本は、Ansibleのパラダイムである「宣言的（Declarative）」な状態定義から逸脱し、手続き型（Imperative）のスクリプト作成に陥っている点にあります。自動化コードは「何を（What）」達成したいかを記述すべきであり、「どのように（How）」実行するかはAnsibleのコアエンジンと、適切にカプセル化された「ロール」が担うべきです 3。

## **セクション 2: 環境の分離 — リファクタリングの第一歩**

YAMLの煩雑さを解消する最も効果的かつ即効性のある第一歩は、環境（Environment）とシークレット（Secrets）を**完全に分離**することです。

### **2.1. 原則：Staging vs Production**

本番環境（Production）とステージング（Staging）環境は、常に分離して管理されるべきです 5。理想的には、開発者やCI/CDプロセスが本番環境のシークレットにアクセスできないようにすべきです 8。この分離は、Playbook内のwhen:句ではなく、インベントリの**ディレクトリ構造**によって実現します 7。

### **2.2. 実践：inventories/ ディレクトリ構造**

Ansibleは、実行時に指定されたインベントリファイル（またはディレクトリ）と同じ階層にあるgroup_vars/およびhost_vars/を自動的に読み込みます。この特性を利用し、環境ごとにインベントリディレクトリを分離します 2。

推奨されるディレクトリレイアウト 11:

```txt
ansible_project/  
├── inventories/  
│   ├── production/  
│   │   ├── hosts               # 本番環境のインベントリファイル  
│   │   ├── group_vars/  
│   │   │   ├── all.yml         # 本番環境 "全体" の変数  
│   │   │   └── webservers.yml  # 本番環境 "webservers" グループの変数  
│   │   └── host_vars/  
│   │       └── prod-web-01.yml  
│   └── staging/  
│       ├── hosts               # ステージング環境のインベントリファイル  
│       ├── group_vars/  
│       │   ├── all.yml         # ステージング環境 "全体" の変数  
│       │   └── webservers.yml  # ステージング環境 "webservers" グループの変数  
│       └── host_vars/  
│           └── staging-web-01.yml  
│  
├── roles/                      # (セクション3で詳述)  
├── collections/                # (セクション5で詳述)  
└── site.yml                    # メインのPlaybook
```

実行方法と効果:  
この構造では、Playbookの実行時に-iフラグで対象環境を指定します。

* ステージング実行: ansible-playbook -i inventories/staging site.yml  
* 本番実行: ansible-playbook -i inventories/production site.yml

このアプローチがなぜ優れているかを、ロジックの連鎖で説明します。

1. **原因:** 単一のgroup_vars/allがグローバルスコープとして機能すると、環境固有の値（例：StagingのDBパスワードとProductionのDBパスワード）が衝突します。  
2. **兆候:** 開発者はこの衝突を避けるため、when: env \== 'staging'のような条件分岐や、--extra-vars 12 による実行時上書きに頼り始めます。結果として、Playbookは複雑化し、実行は不安定になります。  
3. **解決:** inventories/ディレクトリ構造 11 を採用すると、ansible-playbookコマンドは実行時に**指定された環境のgroup_vars/allのみをロード**します。  
4. **結果:** site.yml Playbook自体は、自分が今stagingで実行されているのかproductionで実行されているのかを**意識する必要がなくなります**（when:が不要になる）。Playbookはシンプルさを維持でき 3、変数のスコープはインベントリ層によって完全に隔離されます。

### **2.3. インベントリ管理の高度化**

* **動的インベントリ:** AWS, Azure, GCPなどのクラウド環境やvSphere 13 を利用している場合、静的なインベントリファイル（hosts）の手動管理はすぐに破綻します。**動的インベントリ（Dynamic Inventory）** 4 を活用し、クラウドプロバイダーやCMDBをSSoT（Single Source of Truth）としてインフラの「As-Is（現状）」を自動的に反映させるべきです 3。  
* **戦略的グルーピング:** ホストをその機能（例：webservers, dbservers）や地理（例：dc_tokyo, dc_osaka）に基づいて戦略的にグループ化することが、group_varsによる変数適用の鍵となります 7。

### **2.4. シークレット管理：Ansible Vaultの戦略的利用**

パスワードやAPIキーといったシークレットを、Gitリポジトリに平文で保存することは絶対に許容されません 4。Ansible Vaultはこれらのシークレットを暗号化する標準機能ですが、その**運用方法**が鍵となります。

ベストプラクティス（vars/vault分離パターン） 5:  
group_vars/（またはhost_vars/）内で、暗号化ファイルと非暗号化ファイルを意図的に分離します。

1. group_vars/webservers/vars.yml (平文ファイル):  

   ```YAML  
   db_user: web_user
   # vault.yml 内の暗号化変数を「参照」する
   db_password: "{{ vault_db_password }}"
   ```

2. group_vars/webservers/vault.yml (暗号化ファイル: ansible-vault encrypt...):  

   ```YAML  
   vault_db_password: "MySecurePassword"
   ```

この「変数リダイレクション」パターン 10 は、2つの点で優れています。  
第一に、\*\*シークレット自体（vault.yml）とシークレットの存在（vars.yml）\*\*を分離できます。開発者はvars.yml（平文）を見るだけで、db_passwordという変数が存在し、それがvault_db_passwordから供給されることを認識できます。  
第二に、CI/CDパイプラインは--vault-password-fileオプションでvault.ymlを安全に復号し、Playbookはvars.ymlに定義されたdb_passwordという変数名を（暗号化を意識せずに）通常通り使用できます。

## **セクション 3: 責務の分離 — Ansible Rolesによるリファクタリング**

環境が分離されたら、次に着手すべきは、肥大化したtasks:リストを「ロール（Roles）」にカプセル化することです。これは、YAMLの煩雑さを解消する**中核的な戦術**です。

### **3.1. Ansible Roleの解剖学：標準ディレクトリ構造**

ロールは、特定の機能（例：Nginxのセットアップ、DBの構築）に必要な全てのコンポーネント（タスク、変数、ファイル、テンプレート）をカプセル化する「再利用可能なビルディングブロック」です 15。

ansible-galaxy init \<ロール名\>コマンドで生成される標準ディレクトリ構造は、各YAMLファイルの「責務」を明確に定義します。

表 1: Ansibleロールの標準ディレクトリ構造と責務（17 に基づく）

| ディレクトリ | 責務 |
| :---- | :---- |
| **tasks/** | ロールが実行するタスクのリスト（main.ymlがエントリーポイント）。 |
| **handlers/** | タスクによってnotifyされ、Playの最後に一度だけ実行されるタスク（例：サービス再起動）。 |
| **defaults/** | ロールの\*\*デフォルト（最低優先度）\*\*変数を定義。ロールの「公開API」として機能し、ユーザー（ロール利用者）による上書きを前提とします。 |
| **vars/** | ロールの\*\*内部（高優先度）\*\*変数を定義。ユーザーによる上書きを意図しない、ロール内部のロジックで使用する定数など。 |
| **files/** | 静的なファイルを格納。copyモジュールでそのまま対象ホストにコピーされます。 |
| **templates/** | Jinja2テンプレートファイル（.j2）を格納。templateモジュールで変数をレンダリングした上で対象ホストに配置されます。 |
| **meta/** | ロールのメタデータ（作者、ライセンス）と、**ロール依存関係**（dependencies）を定義します 4。 |

### **3.2. リファクタリング実践：モノリシックPlaybookからロールへ**

1. **特定:** 既存の煩雑なPlaybook（例：site.yml）をレビューし、特定の機能（例：「Webサーバー設定」「DB設定」）に関連するタスク群を特定します。  
2. **抽出:** ansible-galaxy init roles/nginx コマンドでロールの雛形を作成します。  
3. **移行:** 特定したタスク群をroles/nginx/tasks/main.ymlに移動します。関連するハンドラーをhandlers/main.ymlに、テンプレートをtemplates/に、変数をdefaults/main.yml（上書きを許可する場合）またはvars/main.yml（内部定数の場合）に移行します。

### **3.3. 設計原則：defaults/ vs. vars/ の戦略的使い分け**

プロジェクトが煩雑化する大きな原因の一つが、defaults/とvars/の誤用です 3。変数の優先順位が混乱し、意図した値が適用されなくなるためです。

設計ルール:  
ユーザー（ロールの利用者）が上書きすべき値（例：nginx_port: 80）は、必ず defaults/main.yml に定義します。defaults/の変数は最も優先度が低いため、group_vars/やPlaybookのvars:セクションで最も容易に上書きできます。  
対照的に、vars/main.yml は、ロールの内部ロジックでのみ使用し、外部から変更されることを期待しない変数（例：OSファミリーごとに異なるパッケージ名を定義する内部変数）に使用します。

この規律を守ることが、ロールの再利用性と予測可能性を担保します。

### **3.4. Red Hat CoPの設計思想：「Function」と「Component」**

Red Hat Community of Practice (CoP) は、ロールの設計に関するより高度な思想を提示しています 3。

* **Function（機能）:** ロール（Role）として表現されます（例：NTP設定、JBossサーバー）。これはユーザーが利用する単位です。  
* **Component（コンポーネント）:** Functionを構成する部品です。通常はロール内の個別のタスクファイル（例：tasks/install.yml, tasks/configure.yml）として表現されます。

このモデルに従い、roles/nginx/tasks/main.ymlが再び肥大化することを防ぐため、import_tasks（セクション6.3で詳述）を使ってコンポーネント（タスクファイル）を呼び出す形に整理することが推奨されます 3。

## **セクション 4: オーケストレーション — Playbookを「宣言的マニフェスト」に**

ロールへのリファクタリングが完了すると、Playbookの役割は根本的に変わります。煩雑なタスクのスクリプトから、インフラの「あるべき姿」を宣言するマニフェストへと昇華します。

### **4.1. Playbookは「何をするか（What）」、ロールは「どうやるか（How）」**

**最重要ベストプラクティス:** Playbookは、どのホスト（hosts:）に、どのロール（roles:）を適用するかを**宣言するマニフェスト**であるべきです 3。

**アンチパターン:** 1つのPlaybook内でtasks:セクションとroles:セクションを混在させること 3。これはロジックの所在を曖昧にし（タスクがロールの実行前、実行後どちらで動くのか？）、実行順序の予測を困難にします。

「悪い」Playbook（1 での議論）:

```YAML
- name: Configure servers  
  hosts: webservers  
  tasks:  
    - name: Install common packages  
      ansible.builtin.yum:...  
  roles:  
    - nginx  
  post_tasks:  
    - name: Clean up  
      ansible.builtin.shell:...
```

「良い」Playbook（3 の原則を適用）:
ロジックは全てロールにカプセル化し、Playbookはそれらを呼び出すだけ、あるいはPlaybook同士をインポートします。

```YAML
# common.yml (Playbook)
- name: Apply common configuration
  hosts: all
  roles:
    - common  # タスクは 'common' ロールにカプセル化
```

```YAML
# webservers.yml (Playbook)
- name: Configure web servers
  hosts: webservers
  roles:
    - nginx
```

```YAML
# site.yml (スーパーPlaybook) [1, 18]
- import_playbook: common.yml
- import_playbook: webservers.yml
```

Playbookをシンプルに保つ（Keep playbooks as simple as possible）3 ことで、インフラ全体の構成がトップレベルのPlaybook（site.ymlなど）を見れば一目瞭然となります。

### **4.2. 外部ロールと依存関係の管理：requirements.yml**

チーム内やコミュニティ（Ansible Galaxy）で作成された**再利用可能なロール**は、各自のGitリポジトリにコピー＆ペーストしてはいけません。これは依存関係の地獄（脆弱性やパッチの管理が不可能になる）を生みます。

**解決策:** requirements.ymlファイルを使用して、外部ロール（GalaxyまたはプライベートGitリポジトリ）への依存を宣言的に管理します 19。

requirements.yml の例 19:

```YAML
# requirements.yml
roles:
  # Galaxyから
  - src: community.general.nginx
    version: 1.0.0
    name: nginx

  # プライベートGitリポジトリから
  - src: git+https://git.example.com/private/ansible-role-common.git
    version: v1.2.0
    name: our_common_role
```

ansible-galaxy install -r requirements.yml コマンドで、これらのロールを指定したroles_path 19（例：roles/）に一括インストールできます。

## **セクション 5: モダンAnsibleへの進化 — Ansible Collectionsの活用**

Ansible 2.9以降 12、プロジェクトの複雑性を管理するための新しい標準として「コレクション（Collections）」が導入されました。

### **5.1. RolesからCollectionsへ：なぜCollectionsが必要か**

ロール（Roles）は「コードの再利用」という問題を解決しました。しかし、ロールが増えるにつれ、「配布」と「名前空間」という新たな問題が発生しました。例えば、roles/nginxという名前のロールが、組織内の複数チームによって個別に作成され、衝突する可能性があります。

**コレクション（Collections）は、ロール、プラグイン、モジュール、そしてPlaybook自体をもパッケージ化**し、独自の**名前空間**（例：my_org.my_collection.nginx_role）で配布・管理するメカニズムです 1。

### **5.2. コレクションの構造と利点**

コレクションは、Ansibleコンテンツ（ロール、プラグイン、モジュール）を標準化されたディレクトリ構造でパッケージ化します 12。ansible-galaxy collection install... でインストールされます。

利点 12:

1. **名前空間の解決:** my_org.nginx（自組織のNginxロール）とcommunity.nginx（コミュニティのNginxロール）が衝突せず共存できます。  
2. **配布の簡素化:** 関連するロール群（例：foo.coreとfoo.utilities 12）を、単一のバージョン管理された成果物として配布できます。  
3. **保守性の向上:** 組織全体でのコード共有と貢献を促進し、各チームが「車輪の再発明」をすることを防ぎ、メンテナンスの負担を軽減します 12。

### **5.3. リファクタリング戦略**

プロジェクトが複数のリポジトリにまたがり、複数のチームが共通のロールセットに依存し始めた場合 20、それは「ロール」を「コレクション」にリファクタリングする**シグナル**です。

組織の「共通基盤ロール」（例：common_setup, security_hardening）をmy_org.commonコレクションとしてパッケージ化し、各プロジェクトのcollections/requirements.yml 20 でそれを参照するように移行します。

## **セクション 6: コード品質と保守性の自動化**

リファクタリングは一度きりのイベントではありません。作成した資産（ロール、コレクション）の品質を長期的に維持するための「セーフティネット」が不可欠です。

### **6.1. 静的コード解析：ansible-lintの導入**

煩雑なコードベースのリファクタリングが困難なのは、変更が引き起こす\*\*副作用（デグレード）\*\*を恐れるためです。ansible-lintは、この恐怖を取り除くための最初のステップです。

ansible-lintは、Playbook、ロール、コレクションをスキャンし、ベストプラクティスからの逸脱、潜在的なバグ、非推奨モジュールの使用、冪等性（べきとうせい）の欠如などを警告するコマンドラインツールです 21。

* インストールと実行 22: pip3 install ansible-lint または dnf install ansible-lint。プロジェクトのルートディレクトリでansible-lintを実行します。  
* 検出される主要な問題の例 22:  
  * command-instead-of-module: shellやcommandでyumやaptを実行している（専用モジュールを使うべき）。  
  * no-changed-when: shellやcommandにchanged_when:が設定されておらず、冪等性が保証されていない。  
  * name\[play\], name\[casing\]: PlayやTaskに名前が付けられていない、または命名規則（大文字開始）に従っていない 4。  
  * fqcn\[action-core\]: ansible.builtin.yum のような\*\*完全修飾コレクション名（FQCN）\*\*を使用していない。  
* **アクション:** 既存のコードベースにansible-lintを導入し、CI/CDパイプライン（GitLab CI, GitHub Actionsなど）に組み込むことを強く推奨します 4。

### **6.2. 自動テストフレームワーク：Moleculeによるロールのテスト**

ansible-lintが静的解析（文法チェック）であるのに対し、Moleculeは\*\*動的テスト（単体・結合テスト）\*\*のためのフレームワークです 23。

Moleculeは、Docker、Podman、Vagrantなどのドライバーを使用して**一時的なテスト環境**を自動的に構築し、その環境に対してロールを適用（converge）、テスト（verify）し、破棄（destroy）します 24。

Moleculeシナリオのレイアウト 28:

* molecule/default/molecule.yml: テストドライバー（例：Docker）やプロビジョナー（Ansible）の定義。  
* molecule/default/create.yml: テストインスタンス（例：Dockerコンテナ）の作成。  
* molecule/default/converge.yml: **テスト対象のロールを呼び出す**Playbook。  
* molecule/default/verify.yml: ロール適用後の状態を検証するタスク（例：Nginxがポート80でリッスンしているか）。  
* molecule/default/destroy.yml: テストインスタンスの破棄。

Moleculeの導入 28 は、Ansible開発のパラダイムシフトを意味します。これにより、開発者は「本番（またはステージング）環境でPlaybookを実行して動作確認する」という危険なプラクティスから脱却し、**ローカル環境でTDD（テスト駆動開発）ライクな開発サイクル** 24 を回せるようになります。これは、自信を持ってリファクタリングを継続的に行うことを可能にする\*\*最大のイネーブラー（実現要因）\*\*です。

### **6.3. YAMLスタイルガイドと高度な構文**

一貫性は、管理の煩雑さを解消する上で不可欠です。

* **一貫性の強制:** チームでスタイルガイド 6 を定義し、ansible-lintで強制します。  
  * **命名規則:** タスク、Play、変数、ロールの命名規則を統一します 4。タスク名は常にname:で定義し 5、何をしているか（Implerative）ではなく「何を達成するか（Declarative）」を記述します。  
  * **コメントと空白:** 読みやすさのために、ブロック間に空白行を入れ 4、複雑なロジックには#でコメントを追加します 5。  
  * **YAML構文:** true/false（ブール値） 29、数値 29、文字列の引用符の使い分けを理解します。特に、foo: "{{ var }}" のように変数がディクショナリの先頭に来る場合は、YAMLパーサーの誤動作を防ぐため**引用符が必須**です 30。  
* import vs. include の戦略的使い分け:  
  これは、Ansibleの「良い書き方」における非常に高度かつ重要なトピックです 31。どちらもタスクやロールを再利用するために使いますが、動作が根本的に異なります。  
  * **import_\*（静的）:** Playbookの\*\*パース時（解析時）\*\*に処理されます 32。Playbookが実行される前に、全てのタスクリストが静的に展開されます。  
  * **include_\*（動的）:** Playbookの**実行時**に処理されます 32。その行に到達するまで、タスクは読み込まれません。

**表 2: import（静的）とinclude（動的）の比較とユースケース**

| 比較項目 | import_tasks / import_role | include_tasks / include_role |
| :---- | :---- | :---- |
| **処理タイミング** | **静的**（パース時） 32 | **動的**（実行時） 32 |
| **ループ（loop）** | **不可** 34 | **可能** 34 |
| **--list-tasks 表示** | 表示される 31 | 表示されない 31 |
| **notify** | ハンドラーへの通知が**可能** 34 | ハンドラーへの通知が**不可**（動的ハンドラーを除く） 34 |
| **when: の挙動** | 読み込まれるタスクファイル全体に適用 | インクルード文自体に適用 |
| **主なユースケース** | Playbookやロールの**静的な構造化**（例：tasks/main.ymlからtasks/install.ymlを読み込む） | **動的な実行**（例：with_itemsでタスクファイルのリストをループ処理する） |

煩雑さの解消（リファクタリング）においては、まずimport_tasksを使用してロール内のタスクをコンポーネント（3）に**静的に分割**することを推奨します。importは予測可能性と静的解析性（--list-tasks）に優れています。include_\*は、ループ処理など、動的な実行が**真に必要**な場合にのみ限定的に使用すべきです 34。

## **セクション 7: 事例研究とリファクタリングへのロードマップ**

### **7.1. 事例研究：ansible-vsphere-management**

13

このGitHubリポジトリ 19 は、中規模から大規模プロジェクトの優れた実例を提供します。

* 構造分析 13:  
  * **ツールの統合:** Vagrant（デプロイホスト）、Terraform（VMプロビジョニング）、Ansible（構成管理）を明確に分離し、それぞれの強みを活かして連携させています。  
  * **動的インベントリ:** TerraformやvSphereからインベントリを**動的に生成**（例：inventory/vsphere_hosts.inv）し、手動管理を排除しています 13。  
  * **変数管理:** inventory/group_vars/all/accounts.yml（Git-ignoreされ、Vault暗号化を推奨）でシークレットを管理し、inventory/group_vars/all/vsphere_hosts.ymlで構成を管理しています 13。  
  * **オーケストレーション:** vsphere_management.shというシェルスクリプトが、プロビジョニング、デプロイ、クリーンアップのワークフロー全体をラップ（統括）しています 13。  
* **学ぶべき点:** 大規模プロジェクトとは、Ansibleが単体で完結するものではなく、他のIaCツールと連携し、動的インベントリをSSoTとし、厳格な変数・シークレット管理 13 を行う「自動化ワークフロー」全体であることを示しています。

### **7.2. 結論：煩雑なプロジェクトを改善するリファクタリング・ロードマップ**

既存の煩雑なプロジェクトを、「良い書き方」に基づいた体系的な資産へと改善するための段階的なロードマップを提案します。

**フェーズ 1: 安定化（Stabilize）**

1. **VCS導入:** 全てのAnsible資産（Playbook, Roles, Inventory）をGitで管理します 4。  
2. **Lint実行:** ansible-lint 22 を導入し、CIで実行します。まずは既存の警告を修正し、品質のベースラインを確立します。

**フェーズ 2: 環境分離（Isolate）**

1. **インベントリのディレクトリ化:** inventories/stagingとinventories/productionを作成し、インベントリとgroup_varsを環境ごとに完全に分離します 11。これが最も即効性のある改善です。  
2. **Vault適用:** 平文のシークレットを特定し、セクション2.4で解説したvars/vault分離パターン 11 を使用してansible-vaultで暗号化します。

**フェーズ 3: カプセル化（Encapsulate）**

1. **最初のロール抽出:** 最も頻繁に変更される、または最も複雑なタスク群（例：Webサーバー設定）を特定し、ansible-galaxy initで最初のロール（例：roles/web_server）を作成し、タスクを移行します 17。  
2. **テスト作成:** 抽出したロールに対し、Molecule 28 でテストシナリオを作成します。まずはconverge（実行成功）とidempotence（冪等性チェック）のテストを実装します。

**フェーズ 4: 反復と洗練（Iterate & Refine）**

1. **ロールの反復:** フェーズ3を繰り返し、Playbook内のtasks:セクションをゼロにすることを目指します。Playbookを「宣言的マニフェスト」 3 に変換します。  
2. **依存関係の整理:** 共通ロールや外部ロールをrequirements.yml 19 で管理するように移行します。

**フェーズ 5: 組織的スケール（Scale）**

1. **コレクション化:** 複数のプロジェクトやチームで共有されるようになった基盤ロール（例：common, security_hardening）を、内部Ansible Collection 12 としてパッケージ化し、組織の標準資産として配布します。

このロードマップに従うことで、現在の「煩雑なYAML」は、体系的で、テスト可能で、スケーラブルな自動化資産へと確実に変貌します。

#### **引用文献**

1. What Are the Best Practices for Organizing Ansible Playbooks? - Reddit, 10月 27, 2025にアクセス、 [https://www.reddit.com/r/ansible/comments/1fo7vrx/what_are_the_best_practices_for_organizing/](https://www.reddit.com/r/ansible/comments/1fo7vrx/what_are_the_best_practices_for_organizing/)  
2. How to design an Ansible directory structure, 10月 27, 2025にアクセス、 [https://forum.ansible.com/t/how-to-design-an-ansible-directory-structure/16849](https://forum.ansible.com/t/how-to-design-an-ansible-directory-structure/16849)  
3. Good Practices for Ansible - GPA - Red Hat Communities of Practice, 10月 27, 2025にアクセス、 [https://redhat-cop.github.io/automation-good-practices/](https://redhat-cop.github.io/automation-good-practices/)  
4. 50 Ansible Best Practices to Follow \[Tips & Tricks\] - Spacelift, 10月 27, 2025にアクセス、 [https://spacelift.io/blog/ansible-best-practices](https://spacelift.io/blog/ansible-best-practices)  
5. Best Practices - Ansible Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html)  
6. Ansible Best Practices, 10月 27, 2025にアクセス、 [https://labs.demoredhat.com/decks/ansible_best_practices.pdf](https://labs.demoredhat.com/decks/ansible_best_practices.pdf)  
7. Ansible tips and tricks, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/latest/tips_tricks/index.html](https://docs.ansible.com/ansible/latest/tips_tricks/index.html)  
8. General tips — Ansible Community Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#separate-production-and-staging-inventory](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html#separate-production-and-staging-inventory)  
9. 10 habits of great Ansible users - Red Hat, 10月 27, 2025にアクセス、 [https://www.redhat.com/en/blog/10-great-ansible-practices](https://www.redhat.com/en/blog/10-great-ansible-practices)  
10. General tips — Ansible Community Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html](https://docs.ansible.com/ansible/latest/tips_tricks/ansible_tips_tricks.html)  
11. Best Practices — Ansible Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#group-and-host-variables](https://docs.ansible.com/ansible/2.8/user_guide/playbooks_best_practices.html#group-and-host-variables)  
12. 25 Tips for Using Ansible in Large Projects - Thomas C. Foulds, 10月 27, 2025にアクセス、 [https://thomascfoulds.com/2021/09/29/25-tips-for-using-ansible-in-large-projects.html](https://thomascfoulds.com/2021/09/29/25-tips-for-using-ansible-in-large-projects.html)  
13. mrlesmithjr/ansible-vsphere-management - GitHub, 10月 27, 2025にアクセス、 [https://github.com/mrlesmithjr/ansible-vsphere-management](https://github.com/mrlesmithjr/ansible-vsphere-management)  
14. 31\. Best Practices — Ansible AWX community documentation, 10月 27, 2025にアクセス、 [https://ansible.readthedocs.io/projects/awx/en/24.6.1/userguide/best_practices.html](https://ansible.readthedocs.io/projects/awx/en/24.6.1/userguide/best_practices.html)  
15. Ansible Roles: Basics, Creating & Using - Spacelift, 10月 27, 2025にアクセス、 [https://spacelift.io/blog/ansible-roles](https://spacelift.io/blog/ansible-roles)  
16. Mastering Ansible Roles: Structuring, Reusability, and Best Practices. by Athira KK, 10月 27, 2025にアクセス、 [https://iam-athirakk.medium.com/mastering-ansible-roles-structuring-reusability-and-best-practices-6b593e8ac124](https://iam-athirakk.medium.com/mastering-ansible-roles-structuring-reusability-and-best-practices-6b593e8ac124)  
17. Mastering Ansible Project Structure: A Guide to Roles, Templates ..., 10月 27, 2025にアクセス、 [https://medium.com/@kirann.bobby/%EF%B8%8F-mastering-ansible-project-structure-a-guide-to-roles-templates-files-and-more-df27d3abbdcc](https://medium.com/@kirann.bobby/%EF%B8%8F-mastering-ansible-project-structure-a-guide-to-roles-templates-files-and-more-df27d3abbdcc)  
18. Architecture of a complex ansible project, 10月 27, 2025にアクセス、 [https://forum.ansible.com/t/architecture-of-a-complex-ansible-project/27090](https://forum.ansible.com/t/architecture-of-a-complex-ansible-project/27090)  
19. How to arrange structure for the case multiple projects - Get Help - Ansible Forum, 10月 27, 2025にアクセス、 [https://forum.ansible.com/t/how-to-arrange-structure-for-the-case-multiple-projects/2355](https://forum.ansible.com/t/how-to-arrange-structure-for-the-case-multiple-projects/2355)  
20. home - Ansible Lint Documentation, 10月 27, 2025にアクセス、 [https://ansible.readthedocs.io/projects/lint/](https://ansible.readthedocs.io/projects/lint/)  
21. Find mistakes in your playbooks with Ansible Lint - Red Hat, 10月 27, 2025にアクセス、 [https://www.redhat.com/en/blog/ansible-lint](https://www.redhat.com/en/blog/ansible-lint)  
22. Ansible Molecule - Ansible documentation - Read the Docs, 10月 27, 2025にアクセス、 [https://ansible.readthedocs.io/projects/molecule/](https://ansible.readthedocs.io/projects/molecule/)  
23. Developing and Testing Ansible Roles with Molecule and Podman - Part 1 - Red Hat, 10月 27, 2025にアクセス、 [https://www.redhat.com/en/blog/developing-and-testing-ansible-roles-with-molecule-and-podman-part-1](https://www.redhat.com/en/blog/developing-and-testing-ansible-roles-with-molecule-and-podman-part-1)  
24. Unit testing Ansible roles with Molecule - Hetzner Community, 10月 27, 2025にアクセス、 [https://community.hetzner.com/tutorials/testing-ansible-with-molecule/](https://community.hetzner.com/tutorials/testing-ansible-with-molecule/)  
25. Testing with Ansible Molecule - YouTube, 10月 27, 2025にアクセス、 [https://www.youtube.com/watch?v=e3FFxKsfdSo](https://www.youtube.com/watch?v=e3FFxKsfdSo)  
26. Testing Ansible Automation with Molecule Pt. 1 by Phil Critchfield Contino Engineering, 10月 27, 2025にアクセス、 [https://medium.com/contino-engineering/testing-ansible-automation-with-molecule-pt-1-66ab3ea7a58a](https://medium.com/contino-engineering/testing-ansible-automation-with-molecule-pt-1-66ab3ea7a58a)  
27. Unit testing Ansible roles with Molecule Hetzner Community, 10月 27, 2025にアクセス、 [https://community.hetzner.com/tutorials/testing-ansible-with-molecule](https://community.hetzner.com/tutorials/testing-ansible-with-molecule)  
28. Basic Ansible YAML syntax and structure - Red Hat Developer, 10月 27, 2025にアクセス、 [https://developers.redhat.com/learning/learn:ansible:yaml-essentials-ansible/resource/resources:basic-ansible-yaml-syntax-and-structure](https://developers.redhat.com/learning/learn:ansible:yaml-essentials-ansible/resource/resources:basic-ansible-yaml-syntax-and-structure)  
29. Ansible スタイルガイド — Ansible Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/2.9_ja/dev_guide/style_guide/index.html](https://docs.ansible.com/ansible/2.9_ja/dev_guide/style_guide/index.html)  
30. Ansible Import vs. Include: What's the Real Difference? - CIQ, 10月 27, 2025にアクセス、 [https://ciq.com/blog/ansible-import-vs-include-what-is-the-real-difference/](https://ciq.com/blog/ansible-import-vs-include-what-is-the-real-difference/)  
31. Including and Importing - Ansible Documentation, 10月 27, 2025にアクセス、 [https://docs.ansible.com/ansible/2.9/user_guide/playbooks_reuse_includes.html](https://docs.ansible.com/ansible/2.9/user_guide/playbooks_reuse_includes.html)  
32. Difference between include & import in Ansible by Heshan Dharmasena - Medium, 10月 27, 2025にアクセス、 [https://heshandharmasena.medium.com/different-between-include-import-in-ansible-576629795516](https://heshandharmasena.medium.com/different-between-include-import-in-ansible-576629795516)  
33. When you should use roles vs include vs import vs include_roles vs import_roles : r/ansible, 10月 27, 2025にアクセス、 [https://www.reddit.com/r/ansible/comments/ttgdks/when_you_should_use_roles_vs_include_vs_import_vs/](https://www.reddit.com/r/ansible/comments/ttgdks/when_you_should_use_roles_vs_include_vs_import_vs/)
