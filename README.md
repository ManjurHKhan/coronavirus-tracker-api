# coronavirus-tracker (API)

## This app is modified to run on GCP appengine


> This is a basic API for tracking development of the new coronavirus (COVID-19, SARS-CoV-2). It's written in python using 🍼 Flask.

[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
![GitHub stars](https://img.shields.io/github/stars/ExpDev07/coronavirus-tracker-api)
![GitHub forks](https://img.shields.io/github/forks/ExpDev07/coronavirus-tracker-api)
![GitHub last commit](https://img.shields.io/github/last-commit/ExpDev07/coronavirus-tracker-api)
![GitHub pull requests](https://img.shields.io/github/issues-pr/ExpDev07/coronavirus-tracker-api)
![GitHub issues](https://img.shields.io/github/issues/ExpDev07/coronavirus-tracker-api)
[![Tweet](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2FExpDev07%2Fcoronavirus-tracker-api)](https://twitter.com/intent/tweet?text=COVID19%20Live%20Tracking%20API:%20&url=https%3A%2F%2Fgithub.com%2FExpDev07%2Fcoronavirus-tracker-api)

## Endpoints

All requests must be made to the base url: ``https://corona-covid-19-map.appspot.com`` (e.g: https://corona-covid-19-map.appspot.com/all). You can try them out in your browser to further inspect responses.

Getting confirmed cases, deaths, and recoveries:
```http
GET /all
```
```json
{
  "confirmed": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "deaths": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "recovered": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "latest": {
    "confirmed": ...,
    "deaths": ...,
    "recovered": ...
  },
  "source": "https://github.com/ManjurHKhan/coronavirus-tracker-api",
  "comment": "Forked from https://github.com/ExpDev07/coronavirus-tracker-api"
}
```

Getting just confirmed:
```http
GET /confirmed
```
```json
{
  "confirmed": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "source": "https://github.com/ManjurHKhan/coronavirus-tracker-api",
  "comment": "Forked from https://github.com/ExpDev07/coronavirus-tracker-api"
}
```

Getting just deaths:
```http
GET /deaths
```
```json
{
  "deaths": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "source": "https://github.com/ManjurHKhan/coronavirus-tracker-api",
  "comment": "Forked from https://github.com/ExpDev07/coronavirus-tracker-api"
}
```


Getting just recoveries:
```http
GET /recovered
```
```json
{
  "recovered": {
    "latest": ...,
    "locations": {
      "Mainland China": [ ... ],
      "US": [...],
      ...
    },
    "last_updated": "2020-03-07T18:08:58.432242Z"
  },
  "source": "https://github.com/ManjurHKhan/coronavirus-tracker-api",
  "comment": "Forked from https://github.com/ExpDev07/coronavirus-tracker-api"
}
```

## Data

The data comes from the [2019 Novel Coronavirus (nCoV) Data Repository, provided
by JHU CCSE](https://github.com/CSSEGISandData/2019-nCoV). It is
programmatically retrieved, re-formatted and stored in the cache for one hour.

## Wrappers

These are the available API wrappers created by the community. They are not neccecarily maintained by any of this project's authors or contributors.

### Java

* [Coronavirus by @mew](https://github.com/mew/Coronavirus).

## Prerequisites

You will need the following things properly installed on your computer.

* [Python 3](https://www.python.org/downloads/) (with pip)
* [Flask](https://pypi.org/project/Flask/)

## Installation

* `git clone https://github.com/ManjurHKhan/coronavirus-tracker-api.git`
* `cd coronavirus-tracker-api`
* `pip3 install`

## Running using GCP dev_appserver.py
* `dev_appserver.py .`
* It will tell you what port to run it on.
## Running / Development

* `python3 main.py`
* Visit your app at [http://localhost:8080](http://localhost:8080).

## Deploying to GCP AppEngine

```bash
# login to be able to deploy the app
$ gcloud auth login

# create new GCP project (change name here)
$ export PROJECT_ID=simple-gae-project-2134
$ gcloud projects create $PROJECT_ID

# set this project to current project
$ gcloud config set project $PROJECT_ID

# check your config
$ gcloud config list

# you need to create the app first in the specific region.
# omit the region to choose it interactivelly.
$ gcloud app create --region=us-east1

# now deploy the code
$ gcloud app deploy

# open app in the browser
$ gcloud app browse

# tail live log
$ gcloud app logs tail -s default
```


### Running Tests

### Linting

### Building

### Deploying

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/ExpDev07"><img src="https://avatars3.githubusercontent.com/u/10024730?v=4" width="100px;" alt=""/><br /><sub><b>ExpDev</b></sub></a><br /><a href="https://github.com/ExpDev07/coronavirus-tracker-api/commits?author=ExpDev07" title="Code">💻</a> <a href="https://github.com/ExpDev07/coronavirus-tracker-api/commits?author=ExpDev07" title="Documentation">📖</a> <a href="#maintenance-ExpDev07" title="Maintenance">🚧</a></td>
    <td align="center"><a href="https://github.com/bjarkimg"><img src="https://avatars2.githubusercontent.com/u/1289419?v=4" width="100px;" alt=""/><br /><sub><b>bjarkimg</b></sub></a><br /><a href="#question-bjarkimg" title="Answering Questions">💬</a></td>
    <td align="center"><a href="https://github.com/Bost"><img src="https://avatars0.githubusercontent.com/u/1174677?v=4" width="100px;" alt=""/><br /><sub><b>Bost</b></sub></a><br /><a href="https://github.com/ExpDev07/coronavirus-tracker-api/commits?author=Bost" title="Documentation">📖</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## License

The data is available to the public strictly for educational and academic research purposes.
