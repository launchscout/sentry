# Gaslight's [Sentry](https://getsentry.com/welcome/)

![](http://i.imgur.com/UP6TOLm.jpg)

## Development

It's a Django application, so there's a little bit of setup involved
unless you're already Python-ing. You should almost certainly setup
[virtualenv](http://virtualenv.readthedocs.org/en/latest/) if you haven't
already.

You'll need to create a [GitHub OAuth application][ghapp] in order to use the
GitHub accounts on production. You can skip this step if you just want
to run a local instance and won't be cloning production data.

1. `git clone git@github.com:gaslight/sentry.git`
1. `cd sentry`
1. `pip install`
1. (optional) `bin/data`

If you're using production data, you'll have to start the application
with the GitHub OAuth environment variables, like this:

```sh
GITHUB_APP_ID=app_id_goes_here \
GITHUB_API_SECRET=secret_goes_here \
DATABASE_URL=postgres://localhost/sentry_development \
sentry --config=sentry.conf.py start
```

Otherwise, you just need the `DATABASE_URL`:

```sh
DATABASE_URL=postgres://localhost/sentry_development \
sentry --config=sentry.conf.py start
```

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

[ghapp]: https://github.com/settings/applications/

