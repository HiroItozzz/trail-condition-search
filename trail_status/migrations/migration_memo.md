**修正予定**

### 優先度高

- まさにその通りです！ プロンプト管理をDBに移行すべきですね。

  - 現状の問題点：
    ```python
    site_name = self._guess_site_name_from_data(source_data)  # "okutama_vc" 推測
    site_path = prompts_dir / f"{site_name}.yaml"  # ファイル存在に依存
    ```

  - DBマイグレーション案：

  ```python
  # models/prompt.py
  class PromptTemplate(models.Model):
      name = models.CharField("テンプレート名", max_length=50, unique=True)  # "base", "okutama_vc"
      content = models.TextField("プロンプト内容")
      is_base = models.BooleanField("ベーステンプレート", default=False)
      created_at = models.DateTimeField(auto_now_add=True)

  # models/source.py
  class DataSource(models.Model):
      # 既存フィールド...
      prompt_template = models.ForeignKey(
          PromptTemplate,
          on_delete=models.SET_NULL,
          null=True,
          blank=True,
          verbose_name="専用プロンプト"
      )
  ```

  **メリット**
  - 1. 安定性 - ファイル存在チェック不要
  - 2. 管理性 - Django Adminで編集可能
  - 3. 拡張性 - バージョン管理、A/Bテスト可能
  - 4. 運用性 - デプロイ時にファイル同期不要

  移行の優先度は高いと思います。ファイルベースは本当に不安定ですよね。

* Unfurling… (esc to interrupt)

### 優先度低
- TrailConditionのurl1のデフォルト値