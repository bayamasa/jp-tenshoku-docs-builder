# YAML スキーマリファレンス

各YAMLファイルのフィールド定義とテンプレート例。Pydanticモデル定義に準拠。

---

## credential.yaml

個人を特定できる機密情報。`.personal/credential.yaml` に配置し、Git管理外とする。

### フィールド定義

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `name_kana` | str | Yes | 氏名ふりがな (例: "やまだ　たろう") |
| `name` | str | Yes | 氏名 (例: "山田　太郎") |
| `birth_day` | str | Yes | 生年月日 (例: "19xx年xx月xx日 (満 xx 歳)") |
| `gender` | str | No | 性別 |
| `cell_phone` | str | No | 携帯電話番号 |
| `email` | str | No | メールアドレス |
| `photo` | str | No | 証明写真ファイルパス |
| `address_kana` | str | No | 現住所ふりがな |
| `address` | str | No | 現住所 |
| `address_zip` | str | No | 郵便番号 |
| `tel` | str | No | 電話番号 |
| `fax` | str | No | FAX番号 |
| `address_kana2` | str | No | 連絡先ふりがな |
| `address2` | str | No | 連絡先 |
| `address_zip2` | str | No | 連絡先郵便番号 |
| `tel2` | str | No | 連絡先電話番号 |
| `fax2` | str | No | 連絡先FAX番号 |

### テンプレート

```yaml
name_kana: "やまだ　たろう"
name: "山田　太郎"
birth_day: "19xx年xx月xx日 (満 xx 歳)"
gender: "男"
cell_phone: "090-1234-5678"
email: "taro.yamada@example.com"
photo: ""

# 現住所
address_kana: "とうきょうとしぶやくじんぐうまえ"
address: "東京都渋谷区神宮前1-2-3 マンション101"
address_zip: "150-0001"
tel: "03-1234-5678"
fax: ""

# 連絡先（現住所以外に連絡を希望する場合のみ記入）
address_kana2: ""
address2: ""
address_zip2: ""
tel2: ""
fax2: ""
```

---

## 職務経歴書 (STAR法)

ファイル: `.personal/work_history.yaml`
モデル: `StarWorkHistory` (`src/jp_tenshoku_docs_builder/work_history/models.py`)

### トップレベル

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `date` | str | Yes | 作成日 (例: "2025年1月1日現在") |
| `summary` | str | No | 職務要約 |
| `highlights` | list[str] | No | 主な実績・強みの箇条書き |
| `experience` | list[StarCompany] | No | 職務経歴 (会社単位) |
| `side_experience` | list[SideCompany] | No | 副業・その他経歴 |
| `technical_skills` | list[SkillCategory] | No | テクニカルスキル |
| `qualifications` | list[Qualification] | No | 資格 |
| `self_pr` | list[SelfPRSection] | No | 自己PR |

**注意**: `name` フィールドはモデル上存在するが、credential.yaml から自動マージされるため、work_history.yaml には記載不要。

### StarCompany

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `company` | str | Yes | 会社名 |
| `period` | str | Yes | 在籍期間 (例: "2020年4月～現在") |
| `business` | str | No | 事業内容 |
| `capital` | str | No | 資本金 |
| `revenue` | str | No | 売上高 |
| `employees` | str | No | 従業員数 |
| `listing` | str | No | 上場区分 (例: "東証プライム", "未上場") |
| `employment_type` | str | No | 雇用形態 (例: "正社員として勤務") |
| `projects` | list[StarProject] | No | プロジェクト一覧 |

### StarProject

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `period` | str | Yes | 期間 (例: "2022年4月～現在") |
| `industry` | str | No | 業界 (例: "保険業界") |
| `name` | str | Yes | プロジェクト名 |
| `situation` | str | Yes | **Situation** - 状況・背景 |
| `task` | str | Yes | **Task** - 課題・目標 |
| `action` | list[str] | Yes | **Action** - 具体的な行動 (箇条書き) |
| `result` | list[str] | Yes | **Result** - 成果・結果 (箇条書き) |
| `environment` | Environment | No | 開発環境 |
| `team_size` | str | No | チーム規模 (例: "全15名") |
| `role` | str | No | 役割 (例: "リーダー") |

### Environment

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `languages` | list[str] | No | プログラミング言語 |
| `os` | list[str] | No | OS |
| `db` | list[str] | No | データベース |
| `frameworks` | list[str] | No | フレームワーク |
| `tools` | list[str] | No | ツール |
| `other` | list[str] | No | その他 |

### SideCompany

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `company` | str | Yes | 会社名/屋号 |
| `period` | str | Yes | 期間 |
| `employment_type` | str | No | 雇用形態 |
| `projects` | list[SideProject] | No | プロジェクト一覧 |

### SideProject

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `period` | str | Yes | 期間 |
| `name` | str | Yes | プロジェクト名 |
| `description` | str | No | 説明 |
| `environment` | Environment | No | 開発環境 |
| `team_size` | str | No | チーム規模 |
| `role` | str | No | 役割 |

### SkillCategory

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `category` | str | Yes | カテゴリ名 (例: "OS", "言語", "DB", "FW") |
| `items` | list[SkillItem] | Yes | スキル項目一覧 |

### SkillItem

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | str | Yes | スキル名 |
| `period` | str | No | 経験期間 (例: "5年0カ月") |
| `level` | str | No | スキルレベル (例: "環境設計・構築が可能") |

### Qualification

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `name` | str | Yes | 資格名 |
| `date` | str | No | 取得日 (例: "2020年6月取得") |

### SelfPRSection

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `title` | str | Yes | PRタイトル |
| `content` | str | Yes | PR本文 |

### テンプレート

```yaml
date: "2025年1月1日現在"

summary: |
  ここに職務要約を記載。これまでの経歴の概要を3-5行程度で。

highlights:
  - "主な実績・強み1"
  - "主な実績・強み2"
  - "主な実績・強み3"

experience:
  - company: "株式会社○○"
    period: "20xx年xx月～現在"
    business: "事業内容"
    capital: ""
    revenue: ""
    employees: ""
    listing: ""
    employment_type: "正社員として勤務"
    projects:
      - period: "20xx年xx月～現在"
        industry: "業界名"
        name: "プロジェクト名"
        situation: |
          どのような状況・背景があったか。
        task: |
          何を達成する必要があったか。
        action:
          - "具体的に行った行動1"
          - "具体的に行った行動2"
        result:
          - "得られた成果・結果1"
          - "得られた成果・結果2"
        environment:
          languages: ["Python", "TypeScript"]
          os: ["Linux"]
          db: ["PostgreSQL"]
          frameworks: ["FastAPI", "React"]
          tools: ["Docker", "GitHub Actions"]
        team_size: "全5名"
        role: "リーダー"

side_experience:
  - company: "フリーランス"
    period: "20xx年xx月～現在"
    employment_type: "業務委託"
    projects:
      - period: "20xx年xx月～現在"
        name: "プロジェクト名"
        description: |
          プロジェクトの説明。
        environment:
          languages: ["TypeScript"]
          frameworks: ["Next.js"]
        team_size: "1名"
        role: "個人開発"

technical_skills:
  - category: "OS"
    items:
      - name: "Linux"
        period: "5年0カ月"
        level: "環境設計・構築が可能"
  - category: "言語"
    items:
      - name: "Python"
        period: "3年0カ月"
        level: "最適なコード記述が可能"
  - category: "DB"
    items:
      - name: "PostgreSQL"
        period: "3年0カ月"
        level: "環境設計・構築が可能"
  - category: "FW"
    items:
      - name: "FastAPI"
        period: "2年0カ月"
        level: "実務での開発経験あり"

qualifications:
  - name: "普通自動車第一種運転免許"
    date: "20xx年xx月取得"
  - name: "基本情報技術者試験"
    date: "20xx年xx月合格"

self_pr:
  - title: "PRのタイトル"
    content: |
      自己PRの本文をここに記載。
      具体的なエピソードを交えて記載する。
```

---

## 履歴書

ファイル: `.personal/resume.yaml`
モデル: `Resume` (`src/jp_tenshoku_docs_builder/resume/models.py`)

**注意**: 履歴書モデルには `name`, `name_kana`, `birth_day` 等の個人情報フィールドが定義されているが、これらは credential.yaml から自動マージされる。resume.yaml には記載不要。

### フィールド定義

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `date` | str | Yes | 作成日 (例: "2025年1月1日現在") |
| `education` | list[HistoryEntry] | No | 学歴 |
| `experience` | list[HistoryEntry] | No | 職歴 |
| `licences` | list[HistoryEntry] | No | 免許・資格 |
| `commuting_time` | str | No | 通勤時間 (例: "1時間10分") |
| `dependents` | str | No | 扶養家族数 (例: "0人") |
| `spouse` | str | No | 配偶者の有無 (例: "有" / "無") |
| `supporting_spouse` | str | No | 配偶者の扶養義務 (例: "有" / "無") |
| `hobby` | str | No | 趣味・特技 |
| `motivation` | str | No | 志望動機 |
| `request` | str | No | 本人希望記入欄 |

### HistoryEntry

| フィールド | 型 | 必須 | 説明 |
|---|---|---|---|
| `year` | str | No | 年 (例: "2020") |
| `month` | str | No | 月 (例: "4") |
| `value` | str | Yes | 内容 (例: "○○大学 工学部 入学") |

**注意**: 年月が不要な行（例: 「現在に至る」や部署配属の補足行）は `year` と `month` を空文字列にする。

### テンプレート

```yaml
date: "2025年1月1日現在"

# 学歴
education:
  - year: "20xx"
    month: "4"
    value: "○○高等学校 入学"
  - year: "20xx"
    month: "3"
    value: "○○高等学校 卒業"
  - year: "20xx"
    month: "4"
    value: "○○大学 ○○学部 ○○学科 入学"
  - year: "20xx"
    month: "3"
    value: "○○大学 ○○学部 ○○学科 卒業"

# 職歴
experience:
  - year: "20xx"
    month: "4"
    value: "株式会社○○ 入社"
  - year: ""
    month: ""
    value: "○○部に配属、○○業務に従事"
  - year: ""
    month: ""
    value: "現在に至る"

# 免許・資格
licences:
  - year: "20xx"
    month: "xx"
    value: "普通自動車第一種運転免許"
  - year: "20xx"
    month: "xx"
    value: "基本情報技術者試験 合格"

# 通勤時間
commuting_time: "1時間10分"

# 扶養家族数(配偶者を除く)
dependents: "0人"

# 配偶者の有無
spouse: "無"

# 配偶者の扶養義務
supporting_spouse: "無"

# 趣味・特技
hobby: |
  趣味・特技を記載。

# 志望動機
motivation: |
  志望動機を記載。

# 本人希望記入欄
request: |
  勤務地や入社時期等の希望を記載。
```
