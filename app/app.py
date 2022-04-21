import os
import logging
import ssl as ssl_lib
import certifi
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from listeners.actions import set_auto_mode, set_manual_mode

from listeners.events import message, update_home_tab
from listeners.messages import panic

# take environment variables from .env
load_dotenv()

# logger in a global context
# requires importing logging
logging.basicConfig(level=logging.INFO)


ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
# )

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


# ============ register listeners =============== #
# event listeners
app.event("message")(message)
app.event("im_open")(message)
app.event("app_home_opened")(update_home_tab)

# action listeners
app.action("manual_mode_button")(set_manual_mode)
app.action("auto_mode_button")(set_auto_mode)

# message listeners
app.message("PANIC")(panic)

# Start your app
if __name__ == "__main__":
    # init()
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
