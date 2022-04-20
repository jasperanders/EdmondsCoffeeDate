from helper.getChannels import getChannels

homeblocks = [
    {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "Hey, I am Edmund. I am here to provide you with excellent coffee date matching.",
        },
    },
    {"type": "divider"},
    {
        "type": "input",
        "element": {
            "type": "multi_static_select",
            "placeholder": {
                "type": "plain_text",
                "text": "Select options",
                "emoji": True,
            },
            "options": getChannels(),
            "action_id": "multi_select_channel-action",
        },
        "label": {
            "type": "plain_text",
            "text": "Select teams you want to match.",
            "emoji": True,
        },
    },
    {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {"type": "plain_text", "text": "Match!", "emoji": True},
                "value": "click_me_123",
                "action_id": "actionId-0",
            }
        ],
    },
    {"type": "divider"},
]


homeview = {
    "type": "home",
    "callback_id": "home_view",
    # body of the view
    "blocks": homeblocks,
}
