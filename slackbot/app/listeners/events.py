# from app import mode_auto, matchings_amount
from slackbot.blocks.chat import hello
from slackbot.blocks.home import homeview
from slackbot.blocks.chat import auto_mode
from slackbot.helper.helper import matchings_from_string
from slackbot.__init__ import matchings_amount, mode_auto, cleanup


# ============== General Message Events ============= #
# When a user sends a DM, the event type will be 'message'.
# Here we'll link the message callback to the 'message' event.
# @app.event("message")
# @app.event("im_open")
def message(event, context, client, say):

    user_id = context.get("user_id")
    try:
        # channel_id = event.get("channel")
        text = event.get("text")

        # If mode is not set there was no (meaningful) user interaction. In that case we send the hello block.
        if mode_auto.get(user_id) is None:
            say(blocks=hello)

        # If mode is manual but user has not specified the number of matchings we expect them to come next.
        # so we will react here
        elif (
            mode_auto.get(user_id) is not None and matchings_amount.get(user_id) is None
        ):
            matchings_amount[user_id] = int(text)
            say(
                f"Ok I will create {matchings_amount.get(user_id)} sets of matches for you."
            )

            if mode_auto.get(user_id):
                say(blocks=auto_mode)
            else:
                say("Please provide your teams now.")

        # If mode is manual and amount is set, we expect to get the groups next. Match them and return
        # send the matches back to the user.
        elif not mode_auto.get(user_id) and matchings_amount.get(user_id) is not None:
            say("I am done matching")
            say(
                f"{matchings_from_string(groups_sting=text, matchings_amount=matchings_amount.get(user_id))}\n Thats it. Thanks and have fun!"
            )
            cleanup(user_id)

    except Exception:
        cleanup(user_id)
        say(
            """Oops, I think something went wrong. Please don't be angry. You can start over again by typing "start"."""
        )


# ============= Home Openend Event =========== #
# When a use opens the apps homescreen, a greeting and a call to action will be shown.
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
