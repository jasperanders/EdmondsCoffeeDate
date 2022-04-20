# Edmonds Coffee Date

## Installation and Running

Install the dependencies with

```
pipenv install
```

Navigate to `app/` and start the bot with 

```
python -m app
```

also forward local dev port using [ngrok](https://ngrok.com). 

```
ngrok http 3000
```

For development you need to update the [Slack Event Subscription Api endpoint](https://api.slack.com/apps/A02GG7SDX35/event-subscriptions?). Use the url that ngrok provides and append `slack/events` to this Api. 


!! The bot part of this application doesn't use flask. Still we provide a flask-endpoint that can be used to use the general matching. !!

Start the flask server with

```
pipenv run flask run
```

Hit the `/v1/matching` endpoint with a `post` containing the groups json.

```
{
    "amount": 2,
    "groups": [
        [
            "Jasper Anders",
            "Hannes von Boetticher"
        ],
        [
            "Pert Gubbi",
            "Bob Senrie"
        ]
    ]
}
```

the answer should look something like this:

```
{
	"matches": [
		{
			"Bob Senrie": "Hannes von Boetticher",
			"Jasper Anders": "Pert Gubbi"
		},
		{
			"Jasper Anders": "Bob Senrie",
			"Pert Gubbi": "Hannes von Boetticher"
		}
	]
}
```
