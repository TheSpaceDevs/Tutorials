# Migrating to SNAPI v4

With the release of SNAPI v4 a couple of changes are necessary. Although not many or big changes, it's nice to know what
to do when you're planning to move from v3 to v4. This is not a complete list of changes, but it should help you get started.

## Response

In terms of response, not that much has changed:

**v3 response**

```json
[
  {
    "id": 18882,
    "title": "EGS launch team looking forward to working with Artemis II crew",
    "url": "https://www.nasaspaceflight.com/2023/04/egs-launch-team-artemis-ii/",
    "imageUrl": "https://www.nasaspaceflight.com/wp-content/uploads/2023/04/52790060302_221dc6d2af_k-1170x803.jpg",
    "newsSite": "NASASpaceflight",
    "summary": "NASA Exploration Ground Systems (EGS) have been preparing and planning for the Artemis II launch since before the flight crew was announced on April 3. Teams at the Kennedy Space Center (KSC) in Florida are looking forward to working closely with the four astronauts who will be the first to fly to the Moon in over 50 years.",
    "publishedAt": "2023-04-04T15:10:47.000Z",
    "updatedAt": "2023-04-04T16:32:47.052Z",
    "featured": false,
    "launches": [
      {
        "id": "41699701-2ef4-4b0c-ac9d-6757820cde87",
        "provider": "Launch Library 2"
      }
    ],
    "events": []
  }
]
```

**v4 response**

```json
{
  "count": 16199,
  "next": "https://api.spaceflightnewsapi.net/v4/articles/?limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "id": 18882,
      "title": "EGS launch team looking forward to working with Artemis II crew",
      "url": "https://www.nasaspaceflight.com/2023/04/egs-launch-team-artemis-ii/",
      "image_url": "https://www.nasaspaceflight.com/wp-content/uploads/2023/04/52790060302_221dc6d2af_k-1170x803.jpg",
      "news_site": "NASASpaceflight",
      "summary": "NASA Exploration Ground Systems (EGS) have been preparing and planning for the Artemis II launch since before the flight crew was announced on April 3. Teams at the Kennedy Space Center (KSC) in Florida are looking forward to working closely with the four astronauts who will be the first to fly to the Moon in over 50 years.",
      "published_at": "2023-04-04T17:10:47+02:00",
      "updated_at": "2023-04-04T18:32:47.052000+02:00",
      "featured": false,
      "launches": [
        {
          "launch_id": "41699701-2ef4-4b0c-ac9d-6757820cde87",
          "provider": "Launch Library 2"
        }
      ],
      "events": []
    }
  ]
}
```

The list with articles is now returned as `results`, comparable with the Launch Library 2 response. The response now also
includes meta information about the numbers of articles in the database and a shortcut links to help you with pagination
for example.

## Attributes

In terms of article attributes, keys that consist of multiple words are represented in snake_case.

## Documentation

Documentation is available at https://api.spaceflightnewsapi.net/v4/docs/. The OpenAPI json is downloadable, so
you can use frameworks like the [openapi generator](https://openapi-generator.tech/).

## Examples (Python)
### Getting a list of all articles

**v3**
```python
import requests

articles = requests.get(
  "https://api.spaceflightnewsapi.net/v3/articles/").json()
print(articles)
```

**v4**
```python
import requests

response = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles/").json()
print(response["results"])
```

### Searching
**v3**
```python
import requests

articles = requests.get(
  "https://api.spaceflightnewsapi.net/v3/articles?title_contains=nasa").json()
print(articles)
```

**v4**
```python
import requests

# Here we demo title, but this can also be done with summary.
response_contains = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?title_contains='nasa launches sls'").json()
print(response["response_contains"])

response_contains_all = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?title_contains_all='nasa, dragon, spacex'").json()
print(response["response_contains_all"])

response_contains_one = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?title_contains_one='nasa, dragon, spacex'").json()

response_search = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?search=somerandomsearchphrase").json()
```

### Search for articles that have a relation with a launch
**v3**
```python
import requests

response = requests.get(
  "https://api.spaceflightnewsapi.net/v3/articles/launch/41699701-2ef4-4b0c-ac9d-6757820cde87").json()
print(response)
```

**v4**
```python
import requests

response = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?launch=41699701-2ef4-4b0c-ac9d-6757820cde87").json()
print(response["results"])
```

You can now also search for articles that relate to multiple launches:
```python
import requests

response = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?launch=41699701-2ef4-4b0c-ac9d-6757820cde87,d8bd2b25-129b-4ab7-95d9-fb8ad1fdd73e").json()
print(response["results"])
```

If you want to get only articles that have a related launch or event, you can use the `has_launch` and `has_event` parameters:
```python
import requests

response = requests.get(
  "https://api.spaceflightnewsapi.net/v4/articles?has_launch=true").json()
print(response["results"])
```

Above options also work for events.
