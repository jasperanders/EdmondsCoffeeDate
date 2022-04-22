import logging
import os
import json


# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = WebClient(token=os.getenv("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)
# You probably want to use a database to store any conversations information ;)
conversations_store = {}
channels_block = []


def fetch_conversations():
    try:
        # Call the conversations.list method using the WebClient
        result = client.conversations_list()
        return result
        # save_conversations(result["channels"])

    except SlackApiError as e:
        logger.error("Error fetching conversations: {}".format(e))


def groups_from_channel_ids(channel_ids):
    """
    Take channel ids, get all users in a channel and append them to nested list. Return this nested list.
    """
    groups = []

    try:
        for id in channel_ids:
            groups.append(client.conversations_members(id).get("members"))

        return groups

    except SlackApiError:
        logger.error("Error fetching users from channels.")


def send_matches_to_user(user_matches: list, user_id):
    """
    user_matches should be a list of matches. They are wrapped in some text and
    send to the user specified.
    """
    matches_names = []
    # generate block from user_matches
    for match in user_matches:
        matches_names.append(get_full_name(match))

    client.chat_postMessage(blocks={}, channel=user_id)


# ==================================== #
# ============ deprecated ============ #
# ==================================== #
# This is no longer used as there is a specific channel select block


# Put conversations into the JavaScript object
def save_conversations(conversations):
    conversation_id = ""
    for conversation in conversations:
        # Key conversation info on its unique ID
        conversation_id = conversation["id"]

        # Store the entire conversation object
        # (you may not need all of the info)
        conversations_store[conversation_id] = conversation


def getChannels():
    fetch_conversations()

    for channel in conversations_store:
        channels_block.append(
            {
                "text": {
                    "type": "plain_text",
                    "text": f"{conversations_store[channel]['name']}",
                    "emoji": True,
                },
                "value": f"{channel}",
            }
        )

    return channels_block


with open("./helper/apidata/sample.json", "w") as outfile:
    json.dump(conversations_store, outfile)
