import os
import logging
import ssl as ssl_lib
import certifi
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

from app.listeners.actions import (
    set_auto_mode,
    set_manual_mode,
    start_automatic_matching,
)

from app.listeners.events import update_home_tab, message
from app.listeners.messages import panic

# take environment variables from .env
load_dotenv()

# logger in a global context
# requires importing logging
logging.basicConfig(level=logging.DEBUG)


ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

app = App(process_before_response=True, token=os.getenv("SLACK_BOT_TOKEN"))


# ============ register listeners =============== #
# event listeners
app.event("message")(message)
app.event("im_open")(message)
app.event("app_home_opened")(update_home_tab)

# action listeners
app.action("manual_mode_button")(set_manual_mode)
app.action("auto_mode_button")(set_auto_mode)
app.action("match_channels")(start_automatic_matching)

# message listeners
app.message("PANIC")(panic)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
