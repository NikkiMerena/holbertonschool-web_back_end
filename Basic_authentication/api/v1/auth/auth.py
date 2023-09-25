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
        """Determine if authentication is required for a given path.
        
        :param path: string representing the path of the request
        :param excluded_paths: list of strings representing the paths that don't need authentication
        :return: True if the path requires authentication, False otherwise
        """
        # Returns True if path is None
        if path is None:
            return True

        # Ensure path is formatted with a trailing slash
        if not path.endswith('/'):
            path += '/'

        # Returns rue if excluded_paths is None or empty
        if excluded_paths is None or len(excluded_paths) == 0:
            return True

        # Returns False if the formatted path is in excluded_paths
        return path not in excluded_paths

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
