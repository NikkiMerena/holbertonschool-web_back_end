#!/usr/bin/env python3
"""Auth Management Module

Contains the Auth class, which serves as a template
for implementing various authentication systems for the API
"""

# Importing the request object form the Flask lib.
# This object contains all the info about the incoming HTTP req.
from flask import request

# Importing List from type hinting of a list & TypeVar to create generic type var.
from typing import List, TypeVar

# Defining a TypeVar named 'User. This is a 
User = TypeVar('User')

class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns False for now, will be implemented later"""
        return False

    def authorization_header(self, request=None) -> str:
        """ Return None for now, will be implemented later
        """
        return None

    def current_user(self, request=None) -> User:
        """Returns None for now will be implemented later
        """
        return None
