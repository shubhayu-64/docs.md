# SnapApp

A low-code application builder with prebuilt industry components. Bringing together the best of low code, Python & Open Source, and Google Cloud.

[![Image of SnapApp](./static/snapapp.png)](https://snapapp.ai)

## Table of Contents 📜
- [SnapApp](#snapapp)
  - [Table of Contents 📜](#table-of-contents-)
  - [Purpose 🎯](#purpose-)
  - [Components 💫](#components-)
  - [Installation 🚀](#installation-)
    - [Setup Local Environment](#setup-local-environment)
  - [Database Migrations](#database-migrations)
  - [Testing](#testing)
  - [Copyright and Licenses 🗒](#copyright-and-licenses-)

## Purpose 🎯

[SnapApp](https://prod.snapapp.ai) is an industry-specific, enterprise-class, low code application builder developed by <a href='https://www.bluevector.ai'>BlueVector.AI</a>.

[![Build](https://github.com/BlueVector-AI/SnapApp/actions/workflows/build.yaml/badge.svg)](https://github.com/BlueVector-AI/SnapApp/actions/workflows/build.yaml)

[![Website](https://img.shields.io/website?label=prod.snapapp.ai&url=https%3A%2F%2Fprod.snapapp.ai)](https://prod.snapapp.ai/)
![Uptime Robot ratio (7 days)](https://img.shields.io/uptimerobot/ratio/m793291991-ce72697d9f30b6ec59e88ec5)
[![](https://img.shields.io/badge/Google%20Cloud%20Console-Prod%20Environment-9cf?logo=google-cloud)](https://console.cloud.google.com/welcome?project=bv-presto-prod)

[![Website](https://img.shields.io/website?label=dev.snapapp.ai&url=https%3A%2F%2Fdev.snapapp.ai)](https://dev.snapapp.ai/)
![Uptime Robot ratio (7 days)](https://img.shields.io/uptimerobot/ratio/m793291986-a4eb8d0694d05fd9d2d21972)
[![](https://img.shields.io/badge/Google%20Cloud%20Console-Dev%20Environment-blue?logo=google-cloud)](https://console.cloud.google.com/welcome?project=bv-presto-dev)

[![Asana](https://img.shields.io/badge/asana-Project%20Management-red?logo=asana&color=FC636B)](https://app.asana.com/0/1202347716179870/list)

[![Bugs](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=bugs&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Code Smells](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=code_smells&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Coverage](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=coverage&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Lines of Code](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=ncloc&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Vulnerabilities](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=vulnerabilities&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Security Rating](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=security_rating&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)
[![Reliability Rating](https://sonar.bluevector.ai/api/project_badges/measure?project=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc&metric=reliability_rating&token=0a128ab42a6a21bb4d32c9b56684450592646022)](https://sonar.bluevector.ai/dashboard?id=BlueVector-AI_presto_AYMXwI69UXrmUdGNlYjc)

[![Mozilla HTTP Observatory Grade](https://img.shields.io/mozilla-observatory/grade-score/prod.snapapp.ai?label=SnapApp%20Prod%20%7C%20Mozilla%20Observatory&logo=mozilla)](https://observatory.mozilla.org/analyze/prod.snapapp.ai)
[![Mozilla HTTP Observatory Grade](https://img.shields.io/mozilla-observatory/grade-score/dev.snapapp.ai?label=SnapApp%20Dev%20%7C%20Mozilla%20Observatory&logo=mozilla)](https://observatory.mozilla.org/analyze/dev.snapapp.ai)

## Components 💫

* <a href='https://www.python.org/downloads/release/python-3110/'>Python 3.11</a>
* <a href='http://flask.pocoo.org/'>Flask</a>
* <a href='https://cloud.google.com/run'>Cloud Run</a>
* <a href='https://cloud.google.com/sql'>Cloud SQL</a>
* <a href='https://cloud.google.com/storage/'>Cloud Storage</a>
* <a href='https://cloud.google.com/secret-manager'>Secrets Manager</a>
* <a href='https://firebase.google.com/'>Cloud Firebase (for authentication)</a>
* <a href='https://cloud.google.com/document-ai'>DocumentAI </a>
* <a href='https://firebase.google.com/docs/firestore'>Firestore </a>
* <a href='https://cloud.google.com/dialogflow'>DialogFlow </a>
* <a href='https://datastudio.google.com/'>Looker / DataStudio </a>
* <a href='https://cloud.google.com/bigquery'>BigQuery </a>
* <a href='https://cloud.google.com/vertex-ai'>Vertex AI </a>

## Installation 🚀

### Setup Local Environment

- Install MySQL 8
- Create a MySQL Database and a User
```sql
CREATE DATABASE dev;
CREATE USER 'dev'@'%' IDENTIFIED BY 'YOUR_DB_PASSWORD';
GRANT ALL ON *.* TO 'dev'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```
- Create a virtual environment and install dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
- In your run configuration, set the following environment variables:
```bash
DB_HOST=localhost;
DB_PASSWORD=YOUR_DB_PASSWORD;
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json;
K_SERVICE=dev;
PROJECT_ID=bv-presto-dev;
```

- Install MongoDB with Homebrew
```bash
brew tap mongodb/brew
brew update
brew install mongodb-community@7.0
```

- To run MongoDB (i.e. the mongod process) as a macOS service, run:
```bash
brew services start mongodb-community@7.0
```

- To stop the MongoDB service, use this command:
```bash
brew services stop mongodb-community@7.0
```

- Connect and Use MongoDB:
```bash
mongosh
```

- Install MongoDB Compass from [here](https://www.mongodb.com/docs/compass/current/install/)

- To connect with local mongodb, use this url:
```
mongodb://localhost:27017
```


When the application runs for the first time, the tables will be automatically created.

## Database Migrations

Yoyo migrations is used to manage database migrations. To create a new migration, run the following command:

```bash
yoyo new --sql
```

Then save your SQL DDL / DML statements in the newly create .sql file under the `/migrations` folder. Please note: do not include the database name in the SQL statements. Otherwise, changes will not be to all databases under all services

## Testing

To run tests in your local environment, set the following environment variables and then run the `pytest` command in your console:

```bash
DB_USER=pytest_db
DB_PASSWORD='YOUR_DB_PASSWORD'
DB_NAME=pytest_db
GOOGLE_APPLICATION_CREDENTIALS=/path/to/credentials.json;
K_SERVICE=pytest_db
GOOGLE_CLOUD_PROJECT=bv-presto-dev
PROJECT_ID=bv-presto-dev
pytest_db_MAPS_API_KEY_BACKEND=<maps api key>
DB_CONNECTION_NAME='test'
SERVICE_URL=localhost
pytest_db_SECRET_KEY='YOUR_RANDOM_SECRET'
PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
```

After setting the environment vars,  run the `pytest` command in your console.

## Copyright and Licenses 🗒

TODO