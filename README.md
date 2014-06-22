# Gaslight's Sentry

## Development

It's a Django application, so there's a little bit of setup involved
unless you're already Python-ing. You should almost certainly setup
[virtualenv](http://virtualenv.readthedocs.org/en/latest/) if you haven't
already.

TODO: finish
1. clone
1. pip install
1. bin/data
1. sentry run?

## Deploy

We're running on [Heroku](https://sentry.gaslight.co), so deployment is
just a git push away. You'll need access to the application, which lives
in the gaslight heroku organization.

### Setup

1. Add the Heroku remote:
  `git remote add heroku git@heroku.com:gaslight-sentry.git`
1. (optional) Fetch
  `git fetch heroku`
1. Push
  `git push heroku`

