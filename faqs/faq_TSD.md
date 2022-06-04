![TSD Cover](../assets/tsd_cover.png)

# The Space Devs - Frequently Asked Questions (FAQ)

## Table of Contents

<!-- Start TOC (do not remove me) -->

* [About](#about)
    * [What is *The Space Devs* (TSD) ?](#what-is-the-space-devs-tsd)
    * [How is TSD managed?](#how-is-tsd-managed)
    * [How is TSD funded?](#how-is-tsd-funded)
* [APIs](#apis)
    * [Which APIs are available?](#which-apis-are-available)
    * [Are the APIs free to use?](#are-the-tsd-apis-free-to-use)
* [Partners](#partners)
    * [What is a TSD partner?](#what-is-a-tsd-partner)
    * [How do I become a TSD partner?](#how-do-i-become-a-tsd-partner)
* [Users](#users)
    * [What is a *verified* TSD user?](#what-is-a-verified-tsd-user)
    * [How do I become a *verified* TSD user?](#how-do-i-become-a-verified-tsd-user)
* [Staff](#staff)
    * [What does the TSD staff do?](#what-does-the-tsd-staff-do)
    * [How do I become a TSD staff member?](#how-do-i-become-a-tsd-staff-member)
* [Contact](#contact)
    * [How do I contact the TSD staff?](#how-do-i-contact-the-tsd-staff)

<!-- End TOC (do not remove me) -->

## About

### What is *The Space Devs* (TSD)?

*The Space Devs* (TSD) is a group of space enthusiast developers and librarians working on APIs to improve public
knowledge and accessibility of spaceflight information. It was created in 2020 by core staff members of Space Launch
Now, the Spaceflight News API and the original Launch Library API with the following objectives:

- Maintain and promote the Launch Library 2 and Spaceflight News APIs.
- Integrate with third-party APIs and services ([TSD partners](#partners)).
- Unite its users into a community of space enthusiast developers ([TSD users](#users)).

*The Space Devs* is **not** affiliated with any space agencies or spaceflight companies.

### How is TSD managed?

Management of *The Space Devs* is handled by a core staff team of developers and librarians involved in the project
foundation in 2020 and its predecessors as staff members of the original Launch Library and Space Launch Now APIs.

A crucial management goal is to ensure that the APIs are and remain **financially sustainable in the long-term**, even
while being **free to use**. This is what the original Launch Library API failed to achieve and the reason this goal is
of utmost importance for Launch Library 2, and *The Space Devs* in general. It comes with implications on access rates
explained in more details [here](#are-the-tsd-apis-free-to-use).

### How is TSD funded?

*The Space Devs* is **not** a company aiming to make profit. Its only purpose is to provide up-to-date data through APIs
accessible for free while also covering its expenses.

100% of its funding comes from the community through [Patreon](https://www.patreon.com/TheSpaceDevs) subscriptions.
These subscriptions are also a way to access the Launch Library 2 API at higher rates than at the free tier. More
details [here](#are-the-tsd-apis-free-to-use).

## APIs

### Which APIs are available?

*The Space Devs* currently handles and provides two APIs first-hand:

- [Launch Library 2 (LL2)](https://thespacedevs.com/llapi) : Launch Library 2 is a REST API for rocket launch data. As
  the official successor of the original Launch Library API, which it replaced in 2020, it keeps its core features
  whilst also including everything the broader Space Launch Now API had to offer. The result is a large database
  delivering a more complete experience for each rocket launch and space event. Since 2021, all orbital rocket launches
  since Sputnik-1 in 1957 are included in the database.

  A complete list of features and documentation links are available on the TSD
  website [here](https://thespacedevs.com/llapi). A dedicated FAQ is available [here](faq_LL2.md).


- [Spaceflight News API (SNAPI)](https://thespacedevs.com/snapi) : The Spaceflight News API is a REST API that provides
  space news articles, which are automatically detected. These are then manually linked to relevant Launch
  Library 2 `launch` and `event` objects, allowing for *related-news* sections on launch and event pages or *view
  launch* and *view event* links on news articles.

  A complete list of features and documentation links are available on the TSD
  website [here](https://thespacedevs.com/snapi). A dedicated FAQ is available [here](faq_SNAPI.md).

Two other APIs are provided by TSD partners :

- [Launch Dashboard API (LDAPI)](https://github.com/shahar603/Launch-Dashboard-API) : The Launch Dashboard API is an
  Open Source
  REST API of rocket launch telemetry. All the data is acquired through optical character recognition (OCR) of launch
  webcasts. The data is then processed by a physics simulator, filtered to remove anomalies and annotated before
  becoming available to API requests.

  More information about the API and can be found on the GitHub
  repository [here](https://github.com/shahar603/Launch-Dashboard-API).


- [Flight Club API](https://flightclub.io) : The Flight Club API is a REST API providing access to flight club data and
  calculators.

  You can find more information about Flight Club [here](https://flightclub.io) and the API
  documentation [here](https://api.flightclub.io/swagger-ui.html).

### Are the TSD APIs free to use?

Both Launch Library 2 and the Spaceflight News API are **free to use**.

***However***, server costs still need to be covered by TSD. For this purpose and to avoid abuse, access to **Launch
Library 2**, our most popular and therefore most expensive API, is limited to **15 calls per hour**. This limit is
sufficient for hobbyists and small projects. If you want higher rates, to refresh data more often close to launches or
to support a larger project, it is possible to increase this limit by using an API key (see how to acquire one
[here](faq_LL2.md#how-do-i-get-an-api-key) and how to use it [here](faq_LL2.md#how-do-i-use-my-api-key)).

Whether you need higher rates than the free tier or not, we **heavily** encourage you to cache the output on your side
and avoid having user clients query TSD APIs directly.

## Partners

### What is a TSD partner?

### How do I become a TSD partner?

## Users

### What is a *verified* TSD user?

### How do I become a *verified* TSD user?

## Staff

### What does the TSD staff do?

### How do I become a TSD staff member?

## Contact

### How do I contact the TSD staff?


