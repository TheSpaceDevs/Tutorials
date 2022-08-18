# Getting started with Launch Library 2

## Introduction
The Launch Library 2 API (LL2 for short) enables you to request space related data such as launches, astronauts, etc.
A full list of features can be found [here](https://thespacedevs.com/llapi).

To get you started with the API, this tutorial contains some introductionary information together with code examples.

Since the production API `ll` has [rate limits](../../faqs/faq_LL2.md#free-and-paid-access), the [development API](../../faqs/faq_LL2.md#what-is-lldev) `lldev` will be used in this tutorial, however this should <u>only by used for development.</u>

## Quickstart

To query data, endpoint URLs are used.
Filters and search terms can added to these.

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
https://lldev.thespacedevs.com/2.2.0/launch/?net__gte=1969-07-16T01:15:00Z&net__lte=1969-07-20T22:45:00Z
```

Quering this we find out that a Saturn V rocket launched Apollo 11 in this time frame.

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

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L47-L58
