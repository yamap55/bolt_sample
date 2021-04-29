"""main"""
import os
from logging import config

from slack_bolt import App

config.fileConfig("logging.conf", disable_existing_loggers=False)


# ボットトークンと署名シークレットを使ってアプリを初期化します
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"), signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# アプリを起動します
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
