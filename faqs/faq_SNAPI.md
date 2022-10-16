![SNAPI Cover](../assets/snapi_poster.png)

[![Website](https://raw.githubusercontent.com/TheSpaceDevs/Tutorials/b475617700544896da25f3dbf70857c111d93299/assets/badge_snapi_website.svg)](https://spaceflightnewsapi.net/)
[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/Tutorials/b475617700544896da25f3dbf70857c111d93299/assets/badge_snapi_doc.svg)](https://api.spaceflightnewsapi.net/documentation)
[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/p7ntkNA)

# Spaceflight News API - Frequently Asked Questions (FAQ)

## Table of Contents

<!-- Start TOC (do not remove me) -->

* [About](#about)
    * [What is the *Spaceflight News API* (SNAPI)?](#what-is-the-spaceflight-news-api-snapi)
    * [Is SNAPI still under development?](#is-snapi-still-under-development)
* [Free and paid access](#free-and-paid-access)
    * [Is SNAPI free to use?](#is-snapi-free-to-use)
    * [Do I need an API key?](#do-i-need-an-api-key)
* [Data](#data)
    * [What data is available?](#what-data-is-available)
    * [Where does SNAPI get its data from?](#where-does-snapi-get-its-data-from)
    * [How often is the data updated?](#how-often-is-the-data-updated)
    * [What date/time format is used in SNAPI?](#what-datetime-format-is-used-in-snapi)
    * [Which types of news sources are allowed in SNAPI?](#which-types-of-news-sources-are-allowed-in-snapi)
    * [How is the data linked to other APIs?](#how-is-the-data-linked-to-other-apis)
* [API](#api)
    * [How to filter the API response?](#how-to-filter-the-api-response)
    * [How to apply multiple filters?](#how-to-apply-multiple-filters)
    * [How to get more results in a single request?](#how-to-get-more-results-in-a-single-request)
    * [How to paginate through the data?](#how-to-paginate-through-the-data)
    * [How to sort the API response?](#how-to-sort-the-api-response)
* [Help & Contact](#help--contact)
    * [Where do I get help?](#where-do-i-get-help)
    * [How do I report a bug/data mistake?](#how-do-i-report-a-bugdata-mistake)
    * [How do I contact the SNAPI staff?](#how-do-i-contact-the-snapi-staff)

## About

> ### What is the *Spaceflight News API* (SNAPI)?

The Spaceflight News API is a REST API providing space news data including :

- Space-related news articles from numerous websites
- Space-related blog posts from numerous websites
- Daily summary reports from the International Space Station

> ### Is SNAPI still under development?

SNAPI is still maintained and improved regularly. However, most of the upgrades are related to the news sources or
backend improvements, requiring no version bump. New features or data can also be added without bumping the API
version if they are fully compatible.

When a new version is released, the announcement will be made the on the
TSD [Discord server](https://discord.gg/p7ntkNA) and Twitter ([TSD](https://twitter.com/TheSpaceDevs)
, [SNAPI](https://twitter.com/the_snapi)) first.

## Free and paid access

> ### Is SNAPI free to use?

Yes, SNAPI is fully free to use for everyone. However, if you are using SNAPI in a commercial project, we would
appreciate if you consider supporting the project through [Patreon](https://www.patreon.com/thespacedevs) or a
one-time [donation](https://ko-fi.com/derkweijers).

> ### Do I need an API key?

No API key is required to use SNAPI.

## Data

> ### What data is available?

A list of the main data elements available through SNAPI is available on its [website](https://spaceflightnewsapi.net/).
The full list of endpoints is available in the [documentation](https://api.spaceflightnewsapi.net/documentation).

> ### Where does SNAPI get its data from?

When available, the data is imported from RSS feeds or the API of source websites.
Otherwise, it is acquired through automatic web scraping.
Some basic filters are applied during processing to remove irrelevant data.


> ### How often is the data updated?

:warning: ???

> ### What date/time format is used in SNAPI?

All the datetime fields in SNAPI follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, for example
`2022-10-16T07:21:04.448ZZ`. All times are UTC, as indicated by the `Z` at the end of the datetime string.

> ### Which types of news sources are allowed in SNAPI?

All professional space-related news sources are allowed in SNAPI for the `articles` endpoint.
For the `blogs` endpoint, high-quality amateur content is also allowed.

It is possible to suggest new sources to be added to SNAPI by posting in the
[`💬feedback-and-help`](https://discord.com/channels/676725644444565514/1019976345884827750) forum of the TSD
[Discord server](https://discord.gg/p7ntkNA).

> ### How is the data linked to other APIs?

Articles are linked to [Launch Library 2](https://thespacedevs.com/llapi) launches and events through their LL2 ID.

## API

> ### How to filter the API response?

Filters can be applied to an API query by adding `?<field>_<filter>=<value>` to the end of the query.

For example: https://api.spaceflightnewsapi.net/v3/articles?title_contains=NASA

> ### How to apply multiple filters?

Multiple filters can be applied by separating them with `&`.

For example: https://api.spaceflightnewsapi.net/v3/articles?title_contains=NASA&publishedAt_lte=2022-01-01


> ### How to get more results in a single request?

It is possible to increase the number of results per request by using the `_limit=<number>` filter.

> ### How to paginate through the data?

The API supports pagination through the `_start=<number>` filter.

> ### How to sort the API response?

The API response can be sorted by any of the available fields using `_sort=<field>`.

## Help & Contact

> ### Where do I get help?
If you need any help with SNAPI, you can ask in the
[`💬feedback-and-help`](https://discord.com/channels/676725644444565514/1019976345884827750) forum of the TSD
[Discord server](https://discord.gg/p7ntkNA) or email [derk@spaceflightnewsapi.net](mailto:derk@spaceflightnewsapi.net).

> ### How do I report a bug/data mistake?

If you found a bug or data mistake, let the staff know in the
[`💬feedback-and-help`](https://discord.com/channels/676725644444565514/1019976345884827750) forum of the TSD
[Discord server](https://discord.gg/p7ntkNA), or
email [derk@spaceflightnewsapi.net](mailto:derk@spaceflightnewsapi.net).

> ### How do I contact the SNAPI staff?

There are two main ways to contact the SNAPI staff:

- On the [Discord server](https://discord.gg/p7ntkNA).
- By email to [derk@spaceflightnewsapi.net](mailto:derk@spaceflightnewsapi.net).