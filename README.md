# Steam Watch

Notify me when a train goes past my house

This GitHub Workflow runs every morning and scrapes Real Time Trains using Scrapy to return possible services that look like they might be steam trains.

Then it uses Jinja2 to create a nice message and sends that as an email to subscribers using buttondown.

If you want to run this yourself you can clone the repo and you will need to set up your personal station code called `STATION_CODE` in a secret in the cloned repo, and your own ButtonDown API token `BUTTONDOWN_API_KEY`.

## Real Time Trains Scraper

**No longer supported**

You can run a lot of this locally yourself. You will need [uv](https://docs.astral.sh/uv/) installed and sync'd.

### Running Locally

You can run this to get the output. You can replace KGX with whatever station you're looking at:

```shell
uv run scrapy crawl steam_trains -a station_code=KGX -o steam_trains.json
```

And run the following to generate the message:

```shell
jq '{data: .}' steam_trains.json.json | uv run jinja2 src/templates/ntfy-message.jinja2.txt --format=json
```

## Running Tests

```shell
uv run pytest tests
```

## Open Rail Data

### Running Locally

```shell
uv run python3 -m src.schedule_parser data/pa-full.jsonl | jq '[.[] | select(.tiploc == "CHST")]'
```

## Message Renderer

```shell
uv run python3 -m src.message_render message.jinja2.md data/trains.json data/tiploc.json
```
