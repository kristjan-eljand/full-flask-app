# full-flask-app
# Environment setup
**Test if you have python 3.9 or higher**
* `python3 -V`

**If you have older version, install python 3.9 (Linux 18.04 & 20.04)**
* `sudo apt-get update`
* `sudo apt install software-properties-common`
* `sudo add-apt-repository ppa:deadsnakes/ppa`
* `sudo apt-get install python3.9`

Add both old and new version of python to update alternatives.
* `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.[your-old-version] 1`
* `sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2`

Type this command to set the new python version as a default one:
* `sudo update-alternatives --config python3`
The command line prompt will now ask you to select your version -> select the new installation version number.

Check the python version again to see if the upgrade was successful
* `python3 -V`

**Install virtualenv package**
* `sudo apt-get install virtualenv`

**Clone the code repository and go to its main directory**
* `git clone git@github.com:kristjan-eljand/full-flask-app.git`
* `cd full-flask-app`

**Create virtualenv named venv and activate it**
* `virtualenv -p python3.9 venv`
* `source venv/bin/activate`

**Install requirements file**
* `pip install -r requirements.txt`

# Tutorial
## To run the app
* `export FLASK_APP=myapp`
* `export FLASK_ENV=development`
* `flask run`

## General boilerplate elements
1. To enable testing and production with separated configurations, we create an application through function (*application factory*) that lives in `__init__.py` file inside myapp folder [Flask web-page guidelines](https://flask.palletsprojects.com/en/2.0.x/tutorial/factory/).

## Authentication with Auth0
Following [this auth0+Flask tutorial](https://auth0.com/docs/quickstart/webapp/python)
1. Added python-dotenv, authlib and requests to requirements.txt
2. Add .env file with client_id, client_secret, domain and app_secret key, which can be generated by running `openssl rand -hex 32` command in the terminal.

# POOLELI
* Kuidas realiseerida auth0 roles - et oma personaalset lehte näed, kuid ressursile ligi ei saa, kui näiteks makstud pole
* Kas õigem on realiseerida auth0 sessioonipõhiselt või läbi token'i
flask tutorialis pooleli: https://flask.palletsprojects.com/en/2.0.x/tutorial/templates/

# TODO
* Localization - https://auth0.com/docs/customize/internationalization-and-localization/universal-login-internationalization
