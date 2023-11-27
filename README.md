# mecab-userdic-build

github actions 上で mecab のユーザ辞書 (`user.dic`) を作成する

- `dict_words` 配下に csv を作成
  - `略称,正式名称` の形式
- pull requestを作成
- main branchにマージ
- [.github/workflows/build_userdic.yml](.github/workflows/build_userdic.yml) を実行
  - `dict_words` の csv に必要な情報を追加し、エントリを作成
  - 単語のコスト値・文脈IDを推定
- 成果物としてアップロード