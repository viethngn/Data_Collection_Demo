# Heroku Django Starter Template

An utterly fantastic project starter template for Django 2.0.

### Set Up Development Environment

1. Install [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv)
2. run `pyenv install 3.6.3`
3. run `pyenv virtualenv 3.6.3 dev_env`
4. run `pyenv activate idhack_env`


### Set Up Heroku
1. Sign Up at [Heroku](heroku.com)
2. Install [heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)
3. Login to heroku in terminal with help [here](https://devcenter.heroku.com/articles/heroku-cli#getting-started)

### Deployment to Heroku

    $ git clone git@github.com:mimirinsights/id-hack-survey.git
    $ cd id-hack-survey
    $ heroku create
    $ git push heroku master

    $ heroku run python manage.py migrate
    
### Running locally
    $ pip install -r dev-requirements.txt
    $ python manage.py migrate
    $ python manage.py runserver
    
## License: MIT
