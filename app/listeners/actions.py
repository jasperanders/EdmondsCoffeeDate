from helper.helper import generate_per_user_matches
from helper.slack_api_interaction import (
    groups_from_channel_ids,
    send_matches_to_user,
)
from logic.coffedatematching import compute_coffee_dates
from blocks.chat import manual_mode_format_info
from __init__ import mode_auto, matchings_amount


def set_manual_mode(ack, context, say, logger):
    """
    Set to manual mode if the respective button was pressed. Also send additional
    formatting information.
    """
    mode_auto[context["user_id"]] = False

    ack()
    say(blocks=manual_mode_format_info)


def set_auto_mode(ack, context, say, logger):
    """
    Set to auto mode if the respective button was pressed. Also send select block.
    """
    mode_auto[context["user_id"]] = True

    ack()
    say(
        "Ok, you chose auto mode. Please supply the number of matches you would like me to generate now."
    )


def start_automatic_matching(ack, body, payload, context, say, logger):
    """
    We match people from the channels selected.
    """
    user_id = context.get("user_id")

    # check if nothing is selected and prompt to select some channels
    selected_channels = payload.get("selected_channels")

    groups = groups_from_channel_ids(selected_channels)
    matches = compute_coffee_dates(groups, matchings_amount.get(user_id))
    logger.debug(f"Matches are: {matches}")
    user_matches = generate_per_user_matches(matches)
    logger.debug(f"Matches are: {user_matches}")

    for user in user_matches:
        send_matches_to_user(user_id=user, user_matches=user_matches[user])

    ack()
    say("Done, I send all the messages.")
    logger.info(payload)
