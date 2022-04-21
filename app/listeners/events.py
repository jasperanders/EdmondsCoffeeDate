# from app import mode_auto, matchings_amount
from blocks.chat import hello
from blocks.home import homeview
from helper.helper import convert_matchings_to_string, match, cleanup
from __init__ import matchings_amount, mode_auto


# ============== General Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
# @app.event("message")
# @app.event("im_open")
def message(event, context, client, say):
    try:
        user_id = context["user_id"]
        # channel_id = event.get("channel")
        text = event.get("text")

        if mode_auto.get(user_id) is None:
            say(blocks=hello)

        elif not mode_auto.get(user_id) and matchings_amount.get(user_id) is None:
            matchings_amount[user_id] = int(text)
            say(
                f"Ok I will create {matchings_amount.get(user_id)} sets of matches for you. Please provide your teams now."
            )

        elif not mode_auto.get(user_id) and matchings_amount.get(user_id) is not None:
            say(
                f"{convert_matchings_to_string(match(groups_sting=text, matchings_amount=matchings_amount.get(user_id)))}\n Thats it. Thanks and have fun!"
            )
            cleanup(user_id)

    except Exception:
        cleanup(user_id)
        say(
            """Oops, I think something went wrong. MoinPlease don't be angry. You can start over again by typing "start"."""
        )


# ============= Home Openend Event =========== #
# When a use opens the apps homescreen, a greeting and a
# call to action will be shown.
# @app.event("app_home_opened")
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
