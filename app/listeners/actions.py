from blocks.chat import manual_mode_format_info, matching
from __init__ import mode_auto


def set_manual_mode(ack, context, say, logger):
    """
    Set to manual mode if the respective button was pressed. Also send additional
    formatting information.
    """
    ack()

    user_id = context["user_id"]
    mode_auto[user_id] = False
    say(blocks=manual_mode_format_info)


def set_auto_mode(ack, context, say, logger):
    """
    Set to auto mode if the respective button was pressed. Also send select block.
    """
    ack()

    user_id = context["user_id"]
    mode_auto[user_id] = True
    say(blocks=matching)
