# RESTful Weather Data API

A web application built using the Pyramid web framework, which allows users to retrieve and store weather in differing forms.

*Note: built from the `cookiecutter` template: [SQLAlchemy](https://github.com/Pylons/pyramid-cookiecutter-alchemy)*


### Getting Started
---------------

- Change directory into your newly created project.

    `$ cd weather_api`

- Create a Python virtual environment.

    `$ pipenv shell`

- Install the project in editable mode with its testing requirements.

    `(env)$ pipenv install -e ".[testing]"`

- Configure the database.

    `(env)$ initialize_weather_api_db development.ini`

- Run your project's tests.

    `(env)$ pytest`

- Run your project.

    `(env)$ pserve --reload development.ini`
