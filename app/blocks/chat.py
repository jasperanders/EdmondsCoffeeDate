from app.helper.slack_api_interaction import getChannels

hello = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": """Glad you made it to the message tab. If you want, I can start to generate coffee dates for you. I will match pairs of people for as many coffee dates as you want. Of course people that work in the same team probably know each other well. I will avoid to match people from the same team. 
            
I can be used in automatic and manual mode.""",
        },
    },
    {"type": "header", "text": {"type": "plain_text", "text": "Automatic Mode"}},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": """
            You can select a number of slack channels from your workspace. After you specified the number of dates you want me to generate I will do so and message everybody involved via a PM.""",
        },
    },
    {"type": "header", "text": {"type": "plain_text", "text": "Manual Mode"}},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": """You can also specify the teams in plaintext.  After you specified the number of dates you want me to generate I will do so and message you all the matches directly.
            
If you choose manual mode, I will give you some additional formatting information.
            """,
        },
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Automatic Mode", "emoji": True},
                "value": "auto",
                "action_id": "auto_mode_button",
            },
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Manual Mode", "emoji": True},
                "value": "manual",
                "action_id": "manual_mode_button",
            },
        ],
    },
]

manual_mode_format_info = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": """You chose *manual mode*. In manual mode you provide the teams in plaintext and I will match them for you. Each person should be their own line, teams are separated by a blank line. It should look something like this:
            
```
Asterix
Obelix

Caesar
Cicero
```

If you want 2 matchings. I will send them to you like this:

```
1.
Asterix & Caesar
Obelix & Cicero

2.
Obleix & Caesar
Asterix & Cicero
```

*Please type the number of matches you want!*
""",
        },
    }
]

auto_mode = [
    {"type": "divider"},
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Ok, let's get started with automatic matching. Start by selecting the channels.",
        },
        "accessory": {
            "action_id": "match_channels",
            "type": "multi_channels_select",
            "placeholder": {"type": "plain_text", "text": "Select channels"},
        },
    },
    # {
    #     "type": "input",
    #     "element": {
    #         "type": "multi_static_select",
    #         "placeholder": {
    #             "type": "plain_text",
    #             "text": "Select options",
    #             "emoji": True,
    #         },
    #         "options": getChannels(),
    #         "action_id": "multi_select_channel-action",
    #     },
    #     "label": {
    #         "type": "plain_text",
    #         "text": "Select teams you want to match.",
    #         "emoji": True,
    #     },
    # },
    # {
    #     "type": "actions",
    #     "elements": [
    #         {
    #             "type": "button",
    #             "text": {"type": "plain_text", "text": "Match!", "emoji": True},
    #             "value": "match",
    #             "action_id": "match_channels",
    #         }
    #     ],
    # },
    {"type": "divider"},
]
