# Internationalization (i18n) with Flask

This project delves into the implementation of internationalization and localization of a Flask web application. It provides various exercises to explore different aspects of i18n, namely parameterizing templates for various languages, deducing the locale, and localizing timestamps.

## Learning Objectives
- Learn how to parametrize Flask templates to display different languages
- Learn how to infer the correct locale based on URL parameters, user settings, or request headers
- Learn how to localize timestamps

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- Code should adhere to the pycodestyle style (version 2.5)
- The first line of all *.py files should be exactly `#!/usr/bin/env python3`
- All *.py files should be executable
- All modules, classes, functions, and methods should have documentation
- All functions and coroutines must be type-annotated

## Tasks

### Task 0: Basic Flask app
Setting up a basic Flask app in `0-app.py`, with a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

### Task 1: Basic Babel setup
Installation and instantiation of the Babel Flask extension, and configuration of available languages and default locale and timezone using a `Config` class.

### Task 2: Get locale from request
Development of a `get_locale` function with the `babel.localeselector` decorator, using `request.accept_languages` to determine the best match with supported languages.

### Task 3: Parametrize templates
Parameterizing templates using the `_` or `gettext` function, initializing translations, and providing message ID values for each language.

### Task 4: Force locale with URL parameter
Implementing a method to force a particular locale by passing the `locale=fr` parameter to the app’s URLs.

### Task 5: Mock logging in
Mocking a user login system by copying a user table, defining `get_user` and `before_request` functions, and displaying messages in HTML based on user login status.

### Task 6: Use user locale
Modification of the `get_locale` function to use a user’s preferred local if it is supported, with various priorities.

### Task 7: Infer appropriate time zone
Definition of a `get_timezone` function with the `babel.timezoneselector` decorator and logic for inferring time zones based on various parameters.

## Repository
GitHub repository: `holbertonschool-web_back_end`

## Usage
Instructions for task-wise execution can be found within respective task sections.
