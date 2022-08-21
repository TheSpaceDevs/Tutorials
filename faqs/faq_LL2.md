![LL2 Cover](../assets/ll2_historic_launches.png)

[![Documentation](https://raw.githubusercontent.com/TheSpaceDevs/Tutorials/a10b94f4476ce7a134f9b6e0e75ef761cb35a446/assets/badge_ll2_doc.svg)](https://ll.thespacedevs.com/docs/)
[![Discord](https://img.shields.io/badge/Discord-%237289DA.svg?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/p7ntkNA)

# Launch Library 2 - Frequently Asked Questions (FAQ)

## Table of Contents

<!-- Start TOC (do not remove me) -->

* [About](#about)
    * [What is *Launch Library 2* (LL2)?](#what-is-launch-library-2-ll2)
    * [How is LL2 related to the original Launch Library API?](#how-is-ll2-related-to-the-original-launch-library-api)
    * [Is LL2 still under development?](#is-ll2-still-under-development)
    * [Will there be a Launch Library 3?](#will-there-be-a-launch-library-3)
* [Free and paid access](#free-and-paid-access)
    * [Is LL2 free to use?](#is-ll2-free-to-use)
    * [What is lldev?](#what-is-lldev)
    * [Do I need an API key?](#do-i-need-an-api-key)
    * [How do I get an API key?](#how-do-i-get-an-api-key)
    * [How do I use my API key?](#how-do-i-use-my-api-key)
    * [How do I change my API key?](#how-do-i-change-my-api-key)
* [Data](#data)
    * [What data is available?](#what-data-is-available)
    * [Where does LL2 get its data from?](#where-does-ll2-get-its-data-from)
    * [How often is the data updated?](#how-often-is-the-data-updated)
    * [How are webcasts (`vidURLs`) selected and sorted?](#how-are-webcasts-vidurls-selected-and-sorted)
    * [How to exclude TSD videos from the webcast list?](#how-to-exclude-tsd-videos-from-the-webcast-list)
    * [What is a Launch Service Provider (LSP)?](#what-is-a-launch-service-provider-lsp)
    * [What date/time format is used in LL2?](#what-datetime-format-is-used-in-ll2)
    * [What country code format is used in LL2?](#what-country-code-format-is-used-in-ll2)
    * [Which suborbital launches are allowed in LL2?](#which-suborbital-launches-are-allowed-in-ll2)
    * [Why do launches remain `In Flight` after deployment?](#why-do-launches-remain-in-flight-after-deployment)
    * [How is the data linked to other APIs?](#how-is-the-data-linked-to-other-apis)
* [API](#api)
    * [How to filter the API response?](#how-to-filter-the-api-response)
    * [How to apply multiple filters?](#how-to-apply-multiple-filters)
    * [How to apply filters with multiple values?](#how-to-apply-filters-with-multiple-values)
    * [How to get more results in a single request?](#how-to-get-more-results-in-a-single-request)
    * [How to paginate through the data?](#how-to-paginate-through-the-data)
    * [How to access all the data and related objects?](#how-to-access-all-the-data-and-related-objects)
    * [How to sort the API response?](#how-to-sort-the-api-response)
    * [Why do past items appear in the `upcoming` endpoints?](#why-do-past-items-appear-in-the-upcoming-endpoints)
* [Help & Contact](#help--contact)
    * [Is LL2 down?](#is-ll2-down)
    * [Where do I get help?](#where-do-i-get-help)
    * [How do I report a bug/data mistake?](#how-do-i-report-a-bugdata-mistake)
    * [How do I contact the LL2 staff?](#how-do-i-contact-the-ll2-staff)

## About

> ### What is *Launch Library 2* (LL2)?

Launch Library 2 is a REST API providing space launch data including but not limited to :

- All orbital and some suborbital launches, with related data such as webcasts, launch service providers, etc.
- Spaceflight events
- Space stations with related data such as dockings, expeditions
- Astronauts and their flights
- Launch vehicles, reusable firt stages and spacecraft
- Programs : Apollo, Tiangon, Starship, etc. and their related data

> ### How is LL2 related to the original Launch Library API?

The retirement of the original Launch Library API was decided in December 2019 after the person paying for
its expensive servers decided to leave the project. The remaining active librarians of the original Launch Library API
teamed up with the staff of the Space Launch Now API to merge both efforts into an official successor :
[Launch Library 2](https://thespacedevs.com/llapi). This new API would be managed by a new entity, separate of the
user projects, called [The Space Devs](https://thespacedevs.com).

The creation of The Space Devs was officially announced with the release of LL2 in July 2020, while the original Launch
Library API stopped being updated in autumn 2020 and was discontinued in early 2021.

> ### Is LL2 still under development?

LL2 is still maintained and improved regularly. However, most of the upgrades are related to the admin panel or
performance improvements, requiring no version bump. New features or data can also be added without bumping the LL2
version if they are fully compatible.

When a new version is released, the announcement will be made the TSD [Discord](https://discord.gg/p7ntkNA)
and [Twitter](https://twitter.com/TheSpaceDevs) first.

> ### Will there be a Launch Library 3?

There is no plan for a major version update of the Launch Library API at the moment. However, it is still under
development and updated regularly. If there ever is, news will be announced on the
TSD [Discord](https://discord.gg/p7ntkNA)
and [Twitter](https://twitter.com/TheSpaceDevs) first.

## Free and paid access

> ### Is LL2 free to use?

All the data in Launch Library 2 is free to acess with up to 15 API calls per hour.
An API key is needed for higher access rates.

> ### What is lldev?

The `lldev` prefix (instead of `ll`) in LL2 calls can be used to reach the development API. It is the same API , but
with no rate limits and a limited, stale data set. This should be used during development and testing, but
never in production.

> ### Do I need an API key?

The 15 calls per hour limit should be enough for most uses. If you feel like you need more (for a mobile app for
example),
then consider setting up a cache updated within the 15 calls per hour limit that serves data to your clients instead.

Additionally, it is recommended if real-time data is needed, to perform fewer API calls per hour overall and more
around the time of the launch. Such optimizations of the API calls distribution can reduce the need for a paid API key.

If these measures are not enough, then an API key is needed to get higher access rates.

> ### How do I get an API key?

To get an API key, first choose the tier that satisfies your needs on
our [Patreon](https://www.patreon.com/TheSpaceDevs).
Then head over to our [website](https://thespacedevs.com/supportus) and login with your Patreon account to generate your
key.

> ### How do I use my API key?

To use your API key, add the following header in your request :

- key: `"Authorization"`
- value: `"Token <token>"`, where `<token>` is your API key (without the `<>`).

> ### How do I change my API key?

To change your API key, head over to our [website](https://thespacedevs.com/supportus), login with your Patreon account,
and follow the instructions.

## Data

> ### What data is available?

A list of the main data elements available through LL2 is available on its [web page](https://thespacedevs.com/llapi).
The full list of endpoints is available in the [documentation](https://ll.thespacedevs.com/docs/).

> ### Where does LL2 get its data from?

The day-to-day data in LL2 is added and maintained using public sources of three different types : 1st-party, 2nd-party
and community.
The 1st party data comes directly from space agencies, launch service providers, satellite operators, etc. and is
usually considered the most reliable. The 2nd party data comes from space journalists and news outlets which have proven
reliable over the years. The community data comes from the forums or user reports and is not necessarily reliable.

The historic data in LL2 is sourced from Jonathan McDowell's [GCAT](https://planet4589.org/space/gcat/),
[Gunter's Space Page](https://space.skyrocket.de/index.html), [spacefacts.de](http://www.spacefacts.de/), as well
as other public databases.

> ### How often is the data updated?

The data in LL2 is updated as often as needed, which means multiple times within an hour during launches or events,
and usually a few times per day as new information is available.

> ### How are webcasts (`vidURLs`) selected and sorted?

When available, only official webcasts are provided in LL2. If there are multiple options, the english-speaking hosted
webcasts with the highest quality are prioritized.

The priority value is an increasing number from the main webcasts to the secondary ones. This is done to easily sort
the available webcasts from the most important to the least.

> ### How to exclude TSD videos from the webcast list?

After launches, some vidURLs with the lowest priority value are launch summary videos provided through the TSD YouTube
channel. These are simple edits to cut out the countdown sequence and holds.

To exclude this, it is possible to use the YouTube API to filter out the videos from the
[TSD YouTube channel](https://www.youtube.com/channel/UCCKiR4D6hbgk9lW9UwxZXxg).

> ### What is a Launch Service Provider (LSP)?

A Launch Service Provider (LSP) is a space agency or company that operates a launch (in the economics sense).
It is not always the operator of the rocket, but is the entity responsible for the launch as seen from customers.

> ### What date/time format is used in LL2?

All the datetime fields in LL2 follow the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, for example
`2022-08-18T09:17:04Z`. All times are UTC, as indicated by the `Z` at the end of the datetime string.

> ### What country code format is used in LL2?

LL2 country codes use **comma-separated** [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) codes.

> ### Which suborbital launches are allowed in LL2?

All orbital launch attempts are included in LL2, however the suborbital launches considered must be livestreamed and
meet at least one of the following criteria:

- Target an apogee of at least 100 km
- Carry crew higher than 80 km
- Draw significant public interest

It is possible to suggest suborbital launches to be added to LL2 by asking librarians on the TSD
[Discord](https://discord.gg/p7ntkNA).

To remove suborbital launches from LL2 queries, it is possible to use the `include_suborbital=false` filter.

> ### Why do launches remain `In Flight` after deployment?

Launches where a liftoff was confirmed remain `In Flight` until a confirmation of acquisition of signal of the main
payload is received. If not available (rideshare with many payloads, classified payloads, etc.), the launch is
considered
successful when the launch service provider counts it as such, usually after deployment.

> ### How is the data linked to other APIs?

LL2 launch and event IDs are used in the following APIs:

- [Spaceflight News API](https://spaceflightnewsapi.net/): to link related news articles
- [Flight Club](https://flightclub.io/): to link launch trajectory and telemetry data
- [Launch Dashboard API](https://github.com/shahar603/Launch-Dashboard-API): to link launch telemetry data
- [SpaceX API](https://github.com/r-spacex/SpaceX-API): to link SpaceX-specific launch data

## API

> ### How to filter the API response?

Filters can be applied to an API query by adding `?<filter>=<value>` to the end of the query.

For example: https://ll.thespacedevs.com/2.2.0/launch/upcoming/?lsp__name=SpaceX

> ### How to apply multiple filters?

Multiple filters can be applied by separating them with `&`.

For example: https://ll.thespacedevs.com/2.2.0/launch/upcoming/?lsp__name=SpaceX&is_crewed=true

> ### How to apply filters with multiple values?

Only a handful of filters can be applied with multiple values, such as `spacecraft_config__ids`, `location__ids`,
`lsp__ids`. For these, multiple values can be applied by separating them with `,`.

> ### How to get more results in a single request?

It is possible to increase the number of results per request **up to 100** by using the `limit=<number>` filter.

While it can help minimize the number of overall API calls, keep in mind that increasing the number of results per
request will result in longer API response times.

> ### How to paginate through the data?

The API supports pagination through the `offset=<number>` filter. This filter is automatically applied to the request
URL and provided in the `next` field of the response.

Therefore, regardless of the number of results per request, easy pagination can be done by performing API requests with
the URL in the `next` field until it is empty.

> ### How to access all the data and related objects?

To access all the data and related objects (webcast URLs on the launch endpoint for example), use the
`mode=detailed` filter.

> ### How to sort the API response?

The API response can be sorted by any of the available fields using `ordering=<field>`. To switch from ascending to
descending order, add `-` to the beginnging of the field name: `ordering=-<field>`.

> ### Why do past items appear in the `upcoming` endpoints?
Launches and events remain in the `upcoming` endpoint for 24 hours to allow services to update them with their final
information (launch outcome, mainly) without needing an additional call to the `previous` endpoint.

This behavior can be disabled using the `hide_recent_previous=true` filter.

## Help & Contact

> ### Is LL2 down?

The status of LL2 can be checked [here](https://ll.thespacedevs.com/health_check/). If you notice any issue, please
let the staff know in the [`#ll-feedback-and-help`](https://discord.com/channels/676725644444565514/676726164659634186)
channel on the TSD [Discord](https://discord.gg/p7ntkNA).

> ### Where do I get help?
If you need any help with LL2, you can ask in
the [`#ll-feedback-and-help`](https://discord.com/channels/676725644444565514/676726164659634186) channel of the TSD
[Discord server](https://discord.gg/p7ntkNA) or email [support@thespacedevs.com](mailto:support@thespacedevs.com).

> ### How do I report a bug/data mistake?

If you found a bug or data mistake, let the staff know in
the [`#ll-feedback-and-help`](https://discord.com/channels/676725644444565514/676726164659634186)
or [`#ll-data`](https://discord.com/channels/676725644444565514/738822880875380746) channels on the TSD
[Discord server](https://discord.gg/p7ntkNA), or email [support@thespacedevs.com](mailto:support@thespacedevs.com).

> ### How do I contact the LL2 staff?

There are two main ways to contact the LL2 staff:

- On the [Discord server](https://discord.gg/p7ntkNA).
- By email to [support@thespacedevs.com](mailto:support@thespacedevs.com).