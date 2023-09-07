# Python Async Function Project

This project is designed to deepen your understanding of Python's `async` and `await` syntax, alongside using the `asyncio` module to run concurrent coroutines. You will also learn how to work with the random module and asyncio tasks.

## Learning Objectives

Upon the successful completion of this project, you should be able to explain the following concepts without the help of Google:

- `async` and `await` syntax
- Executing an async program with asyncio
- Running concurrent coroutines
- Creating asyncio tasks
- Utilizing the random module

## Requirements

### General

- Your README.md file should be at the root of your project folder
- Allowed editors: `vi`, `vim`, `emacs`
- All files should be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- Ensure that all your files end with a new line
- All your files should be executable
- Adhere to the `pycodestyle` style (version 2.5.x) for your code
- Use `#!/usr/bin/env python3` as the first line in all your Python files
- All functions and coroutines must be type-annotated
- Modules, functions, and methods must have detailed and descriptive docstrings

### Documentation

- Document all your modules by executing: `python3 -c 'print(__import__("my_module").__doc__)'`
- Document all your functions by executing: `python3 -c 'print(__import__("my_module").my_function.__doc__)'`
- Your documentation should not be a single word; instead, provide detailed sentences explaining the purpose of your modules, classes, or methods

## Tasks

### Task 0: The basics of async

In this task, you will create an asynchronous coroutine named `wait_random` that accepts an integer argument `max_delay` (default value of 10) and waits for a random delay between 0 and `max_delay` seconds before returning the float value of the delay.

Refer to the `0-basic_async_syntax.py` file in the `python_async_function` directory for the implementation details.

### Task 1: Executing multiple coroutines concurrently with async

Here, you will develop an async routine named `wait_n` that takes in two integers, `n` and `max_delay`, and spawns `wait_random` `n` times with the specified `max_delay`.

Find further details in the `1-concurrent_coroutines.py` file located in the `python_async_function` directory.

... (Continue with the other tasks in a similar manner, providing a detailed description of what each task entails)

## Repository

GitHub repository: [holbertonschool-web_back_end](https://github.com/NikkiMerena/holbertonschool-web_back_end.git)
Directory: `python_async_function`

## How to Test the Functionality



## Author

Nikki Alderman

## Acknowledgements

- Python 3.7
- Ubuntu 18.04 LTS
