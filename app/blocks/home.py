homeblocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": """Hey, I am Edmund. I am here to provide you with excellent coffee date matching.
                    Navigate to the message tab to get started.
                    """,
        },
    },
    {"type": "divider"},
]


homeview = {
    "type": "home",
    "callback_id": "home_view",
    # body of the view
    "blocks": homeblocks,
}
