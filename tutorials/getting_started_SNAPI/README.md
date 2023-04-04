# Getting started with the Spaceflight News API

## Introduction
The Spaceflight News API (SNAPI for short) enables you to request space related news articles, blogs, and reports.
A full list of features can be found [here](https://thespacedevs.com/snapi).

To get you started with the API, this tutorial contains some introduction information together with code examples.
For more detailed documentation on all the endpoints, please refer to the [documentation](https://api.spaceflightnewsapi.net/v4/documentation).

## Quickstart

To query data, endpoint URLs are used.
Filters and search terms can be added to these.

Querying the articles endpoint: https://api.spaceflightnewsapi.net/v4/articles

Adding filters is done by adding them to the base url.


## Examples

### Querying & filtering news articles in Python

> Filtering

You can filter on various properties, for example on the news site that published the article. For example get all the articles published by NASA:
```shell
curl https://api.spaceflightnewsapi.net/v4/articles?news_site=NASA
```

Or maybe you'll want all the articles related to the Artemis I launch:
```shell
curl https://api.spaceflightnewsapi.net/v4/articles?launch=65896761-b6ca-4df3-9699-e077a360c52a
```

> Limiting

By default, you'll get 10 articles in the response. You can change this with the `?limit` query parameter:
```shell
curl https://api.spaceflightnewsapi.net/v4/articles?limit=3
```

> Paginating through all the results

With the `next` key you can paginate through all the results of your query:
```python
next_url = "https://api.spaceflightnewsapi.net/v4/articles?launch=65896761-b6ca-4df3-9699-e077a360c52a"
while next_url:
    # Requesting next data
    next_results = requests.get(next_url).json()
    print(next_results)
    
    # Adding to the original results dictionary
    results['results'] += next_results['results']

    # Updating the next URL
    next_url = next_results['next']
```
