# Getting started with Launch Library 2

The Launch Library 2 API enables you to request space related data, be it launches, astronauts or something else.

The API is free for everyone to use, however there are [rate limits](#rate-limits) to prevent abuse and keep it free for everyone.
If you desire a higher limit click [here](../faqs/faq_LL2.md#how-do-i-get-an-api-key) to find out how.

## Introduction

The Launch Library 2 API (LL2 for short) has the following endpoints:

> ### Agencies

> ### Astronauts

> ### Config

Contains standard data used in other endpoints, for example the launch statuses.

> ### Dashboard

Returns a summary of recent data from several endpoints regarding the selected topic.

> ### Docking Event

> ### Event

> ### Expedition

Astronaut expeditions.

> ### Launch

> ### Launcher

> ### Location

Spaceflight related locations.

> ### Pad

Launch pads.

> ### Program

Spaceflight programs, for example the ISS.

> ### Spacecraft

> ### Spacestation

> ### Updates

Important updates to the LL2 data.

The event and launch endpoints both contain previous and upcoming sub-endpoints for easier querying.

## Quickstart

To query data, use GET on the endpoint URLs to which filters and search terms can added.

### All examples here use the development API `lldev`, use `ll` for production.

> ### Filters

Adding filters is done by adding them to the base url.
Here an example is given for finding launches between two dates.

Example base url for upcoming launches:

```
https://lldev.thespacedevs.com/2.2.0/launch/
```

Here two filters are added, a minimum and maximum date and time to get the launches between the two.

Here the minimum is July 16, 1969 and the maximum Jul 20, 1969.
The filtered variable is `net`, which represents the launch datetime.

To filter `net` we add two underscores `__` and the filter terms `gte` (greater-than-or-equal) and `lte` (less-than-or-equal).
Combining these two filters is done using the ampersand symbol `&`.

Before adding these filters a question mark `?` is added after the base url to indicate the start of parameters.
Then the filter parameter name is given with an equals sign `=` with the value following it.

```
https://lldev.thespacedevs.com/2.2.0/launch/?net__gte=1969-07-16T00:00Z&net__lte=1969-07-20T00:00Z
```

Quering this we find out that a Saturn V rocket launched Apollo 11 in this time frame.

> ### Rate limits

The API has a free rate limit of 15 queries an hour.

For paid higher limits click [here](../faqs/faq_LL2.md#how-do-i-get-an-api-key), the following tiers are available:

- 45 per hour (Regular Supporter)
- 210 per hour (Avanced Supporter)
- 500 per hour (Premium Supporter)

## Examples

Querying the upcoming launch endpoint in Python using the requests library:

```python
import requests

launch_upcoming_url = 'https://lldev.thespacedevs.com/2.2.0/launch/upcoming/'

# Requesting data
results = requests.get(launch_upcoming_url)

# Printing resulting dictionary
print(
    results.json()
)
```
