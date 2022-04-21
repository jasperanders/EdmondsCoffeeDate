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

This bot uses the bolt socket mode, you don't need to specify any endpoints in your app. Only make sure you have valid Slack-Tokens.


### Using Flask

!! The bot part of this application doesn't use flask. 
Still, we provide a flask-endpoint that can be used to use the general matching. !!

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
