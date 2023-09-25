#!/usr/bin/env python3
"""Auth Management Module
"""

# Importing the request object form the Flask lib.
# This object contains all the info about the incoming HTTP req.
from flask import request

# Importing List from type hinting of a list & TypeVar to create
# generic type var.
from typing import List, TypeVar

# Defining a TypeVar named 'User. This is a generic type that will represent
# the user in the 'current_user' method.
User = TypeVar('User')


# Defining a class named 'Auth'. This class will serve as a template for
# implementing authentication systems
class Auth:
    """Auth class for managing API authentication
    """

    # Defining a method 'require_auth that takes a path (str) and a list of
    # excluded-paths. It returns a boolean value.
    # For now, this method is not fully implemented and always returns False.
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False for now, will be implemented later
        """
        return False

    # Defining a method 'authorization_header' that takes an optional request
    # parameter and returns a string.
    # For now, this method is not fully implemented and always returns None.
    def authorization_header(self, request=None) -> str:
        """ Return None for now, will be implemented later
        """
        return None

    # Defining a method 'current_user' that takes an optional request parameter
    # and returns an object of type 'User'.
    # For now, this method is not fully implemented and always returns None.
    def current_user(self, request=None) -> User:
        """Returns None for now will be implemented later
        """
        return None
