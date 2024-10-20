# Deploy Web Application to GCP

## Overview

It's a language detector

Simple Python-Flask with HTML frontend that accepts sentence of language input and detects the origin of the language

Backend heavily based on [Detecting languages (basic)](https://cloud.google.com/translate/docs/basic/detecting-language#translate_detect_language-python); using [Translate V2 python client library](https://cloud.google.com/python/docs/reference/translate/latest/google.cloud.translate_v2.client.Client#google_cloud_translate_v2_client_Client_detect_language)

Find out more about [GCP free trial](https://cloud.google.com/free)

## Get started

`git clone https://github.com/jwdjj/gcp-workshop`

or click the following

<a href="https://console.cloud.google.com/cloudshell/open?git_repo=https://github.com/jwdjj/gcp-workshop&page=editor&open_in_editor=README.md">
<img alt="Open in Cloud Shell" src ="http://gstatic.com/cloudssh/images/open-btn.png"></a>

## Run Locally

```
pip install -r requirements.txt
flask --app main run
```

View in your browser, the endppoint should be specified upon running e.g. http://127.0.0.1:5000

## Deploy to GCP

### Pre-requisite

Ensure to enable the following APIs:
- Cloud Translation API (required)
- Cloud Run Admin API (required)
- Cloud Build API
- Artifact Registry API

### Cloud Run

Deploy from [source code](https://cloud.google.com/run/docs/deploying-source-code)

`gcloud run deploy language-detector --source .`

### App Engine

app.yaml is included, modified accordingly then run

`gcloud app deploy`

Note: you can choose to use [standard or flexible](https://cloud.google.com/appengine/docs/the-appengine-environments) accordingly to your use case


## More Learning Resources

* Self-paced labs: [cloudskillsboost.google](https://cloudskillsboost.google)
  * There are also GCP Certifications Learning Paths available for free
* Official documentations: [cloud.google.com](https://cloud.google.com)
  * Tutorials: [cloud.google.com/docs/tutorials](https://cloud.google.com/docs/tutorials)
* GitHub sample code: [github.com/GoogleCloudPlatform](https://github.com/GoogleCloudPlatform)