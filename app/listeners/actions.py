from app.helper.slack_api_interaction import groups_from_channel_ids, send_matches_to_user
from app.logic.coffedatematching import compute_coffee_dates
from blocks.chat import manual_mode_format_info, auto_mode
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
    say(
        "It seems like you didn't select any channel. Please do that before you try to match again."
    )

    selected_channels = payload.get("selected_channels")

    groups = groups_from_channel_ids(selected_channels)
    matches = compute_coffee_dates(groups, matchings_amount.get(user_id))
    user_matches = generate_per_user_matches(matches)

    for user in user_matches:
        send_matches_to_user(user, user_matches[user])

    ack()
    say("Done, I send all the messages.")
    logger.info(payload)
