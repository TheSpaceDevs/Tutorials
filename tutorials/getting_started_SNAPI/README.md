# Getting started with the Spaceflight News API

## Introduction
The Spaceflight News API (SNAPI for short) enables you to request space related news articles, blogs, and reports.
A full list of features can be found [here](https://thespacedevs.com/snapi).

To get you started with the API, this tutorial contains some introduction information together with code examples.
For more detailed documentation on all the endpoints, please refer to the [documentation](https://api.spaceflightnewsapi.net/documentation).

## Quickstart

To query data, endpoint URLs are used.
Filters and search terms can be added to these.

Querying the articles endpoint: https://api.spaceflightnewsapi.net/v3/articles

Adding filters is done by adding them to the base url.


## Examples

### Querying & filtering news articles in Python

> Filtering

Here two filters are added, a minimum and maximum date and time to get the launches between the two.

The time frame of the minimum and maximum are a month ago and now.
The filtered variable is `net`, which represents the launch datetime.

To filter `net` we add two underscores `__` and the filter terms `gte` (greater-than-or-equal) and `lte` (less-than-or-equal).
Combining these two filters is done using the ampersand symbol `&`.

Before adding these filters a question mark `?` is added after the base url to indicate the start of parameters.
Then the filter parameter name is given with an equals sign `=` with the value following it.

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L7-L12

> Setting response mode

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L23-L24

> Limiting

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L26-L27

> Ordering

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L29-L30

> Assembling query URL

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L32-L36

> Paginating through all the results

https://github.com/TheSpaceDevs/Tutorials/blob/60256f360d409f7938f52a11fde0615e4abb131e/tutorials/getting_started_LL2/launches_past_month.py#L47-L58
