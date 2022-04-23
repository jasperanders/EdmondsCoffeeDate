# -*- coding: utf-8 -*-
import os
import logging
import ssl as ssl_lib
import certifi
from dotenv import load_dotenv

from slack_bolt import App
from slack_bolt.adapter.aws_lambda import SlackRequestHandler

from app.listeners.actions import set_auto_mode, set_manual_mode, start_automatic_matching

from app.listeners.events import update_home_tab, message
from app.listeners.messages import panic

# take environment variables from .env
# load_dotenv()

# logger in a global context
# requires importing logging
logging.basicConfig(level=logging.DEBUG)


ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
# )

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


# ============ register listeners =============== #
# event listeners
app.event("message")(ack=message)
app.event("im_open")(ack=message)
app.event("app_home_opened")(ack=update_home_tab)

# action listeners
app.action("manual_mode_button")(ack=set_manual_mode)
app.action("auto_mode_button")(ack=set_auto_mode)
app.action("match_channels")(ack=start_automatic_matching)

# message listeners
app.message("PANIC")(ack=panic)


def lambda_handler(event, context):
    slack_handler = SlackRequestHandler(app=app)
    return slack_handler.handle(event, context)
