from slackbot.__init__ import cleanup


# ============= Panic ===================== #
# The user can type panic to reset the app
def panic(context, say, logger):
    cleanup(context.get("user_id"))

    say("Oof, sorry for that. Lets try that again.")
