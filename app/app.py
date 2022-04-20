import os
from slack_bolt import App
from slack_sdk.web import WebClient
from slack_bolt.adapter.socket_mode import SocketModeHandler

from dotenv import load_dotenv

from helper.helper import convert_string_to_nested_list, convert_matchings_to_string
from coffedatematching import compute_coffee_dates
from blocks.home import homeview


import ssl as ssl_lib
import certifi


# take environment variables from .env.
load_dotenv()

ssl_context = ssl_lib.create_default_context(cafile=certifi.where())

# app = App(
#     token=os.environ.get("SLACK_BOT_TOKEN"),
#     signing_secret=os.environ.get("SLACK_SIGNING_SECRET"),
# )

app = App(token=os.getenv("SLACK_BOT_TOKEN"))


def start_onboarding(
    user_id: str,
    channel: str,
    client: WebClient,
    groups_sting: str,
    matchings_amount: int = 3,
):

    matches = compute_coffee_dates(
        convert_string_to_nested_list(groups_sting), matchings_amount
    )

    message = {
        "channel": channel,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (convert_matchings_to_string(matches)),
                },
            }
        ],
    }

    # Post the onboarding message in Slack
    client.chat_postMessage(**message)


# ============== Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
@app.event("message")
def message(event, client):
    """Display the onboarding welcome message after receiving a message
    that contains "start".
    """

    channel_id = event.get("channel")
    user_id = event.get("user")
    text = event.get("text")

    return start_onboarding(user_id, channel_id, client, text)


# ============= Home Openend Event =========== #
# When a use opens the apps homescreen, a greeting and a
# call to action will be shown.
@app.event("app_home_opened")
def update_home_tab(client, event, logger):
    try:
        # views.publish is the method that your app uses to push a view to the Home tab
        client.views_publish(
            # the user that opened your app's app home
            user_id=event["user"],
            # the view object that appears in the app home
            view=homeview,
        )

    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")


# ============= React to channel selection in multi select =========== #
# get selection and write to selection
@app.action("multi_select_channel-action")
def get_selection(ack, say):
    print("We got a action!")
    ack()
    say("Edmund is matching for you.")


# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.getenv("SLACK_APP_TOKEN")).start()
