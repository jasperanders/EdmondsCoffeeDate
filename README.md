# Edmonds Coffee Date Matcher

A matching algorithm for groups of persons, giving the specified number of pairings between persons of different groups, with no meeting repeating.

Uses Edmonds Blossom matching algorithm, implemented by David Eppstein and published "https://code.activestate.com/recipes/221251-maximum-cardinality-matching-in-general-graphs/" on Fri, 12 Sep 2003, just modified for our purposes.

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
