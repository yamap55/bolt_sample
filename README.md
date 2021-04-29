# bolt_sample

本リポジトリは [bolt for python](https://github.com/slackapi/bolt-python) を試すリポジトリになります。
下記の公式のチュートリアルに沿って実装する予定です。

https://slack.dev/bolt-python/ja-jp/tutorial/getting-started

## 環境詳細

- Python : 3.9.4

### 事前準備

- Docker インストール
- VSCode インストール
- VSCode の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone
- `.env` ファイルを作成
  - 下記の環境変数を設定

### .env

```
SLACK_BOT_TOKEN=xoxb-xxxxxx
SLACK_SIGNING_SECRET=xxxx
```

### 開発手順

1. VSCode 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナ image の取得や作成が行われる
5. 起動したら開発可能

## 起動

- ngrok 起動
  - `ngrok http 3000`
-  表示される URL を Slack に設定
  - アプリ設定ページ -> Interactivity & Shortcuts -> URL を設定
  - `http://xxxxxxxx.ngrok.io/slack/events`
- 起動
  - `python main.py`
