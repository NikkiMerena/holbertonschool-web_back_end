#!/usr/bin/env python3
"""Module for BasicAuth class"""

from .auth import Auth
import base64
from typing import TypeVar
from models.user import User
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """BasicAuth class

    This class is used for handling Basic Authentication
    It inherits from the Auth class
    """
    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value.

        Args:
            decoded_base64_authorization_header (str):
            The Base64 decoded string.

        Returns:
            tuple: The user email and password as strings if
            decoded_base64_authorization_header is valid and contains ':'.
            (None, None): If decoded_base64_authorization_header is
            None, not a string, or doesn't contain ':'.
        """
        if decoded_base64_authorization_header is None or \
            not isinstance(decoded_base64_authorization_header, str) or \
                ':' not in decoded_base64_authorization_header:
            return None, None
        decoded_values = decoded_base64_authorization_header.split(':', 1)
        user_email, user_password = decoded_values
        # user_email, user_password =
        # decoded_base64_authorization_header.split(':', 1)
        return user_email, user_password

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """Returns the decoded value of a Base64 string
            base64_authorization_header.

        Args:
            base64_authorization_header (str): The Base64 encoded string.

        Returns:
            str: The decoded value as a UTF8 string if
            base64_authorization_header is valid.
            None: If base64_authorization_header is None,
            not a string, or not valid Base64.
        """
        if base64_authorization_header is None or \
                not isinstance(base64_authorization_header, str):
            return None
        try:
            base64_bytes = base64_authorization_header.encode('utf-8')
            decoded_bytes = base64.b64decode(base64_bytes)
            decoded_str = decoded_bytes.decode('utf-8')
            return decoded_str
        except Exception:
            return None

    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """Extracts the Base64 encoded part of the Authorization header.

        Args:
            authorization_header (str): The Authorization header value.

        Returns:
            str: The Base64 encoded part of the Authorization header if valid.
            None: If the Authorization header is invalid.
        """
        if authorization_header is None or \
                not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split(" ", 1)[1]

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """
    Retrieve a User instance based on email and password.

    :param user_email: The email of the user to retrieve.
    :param user_pwd: The password of the user to retrieve.
    :return: The User instance if found and password
    is correct, otherwise None.
    """
        # Check if user_email or user_pwd is None or not a string
        if not isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None

        # Use the class method search of the User to
        # lookup the list of users based on their email
        users = User.search({"email": user_email})

        # Check if any User instance with email equal to user_email is found
        if not users:
            return None

        # Get the first user instance from the list
        # of users (assuming email is unique)
        user = users[0]

        # Check if user_pwd is the password of the User instance found
        if not user.is_valid_password(user_pwd):
            return None

        # Return the User instance
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieves the User instance for a request."""
        # Get the value of the authorization header
        auth_header = self.authorization_header(request)

        # Extract the base64 authorization header
        base64_auth_header = self.extract_base64_authorization_header
        (auth_header)

        # Decode the base64 authorization header
        decoded_base64_auth_header = self.decode_base64_authorization_header(base64_auth_header)

        # Extract user credentials from the decoded base64 authorization header
        user_email, user_pwd = self.extract_user_credentials(decoded_base64_auth_header)

        # Retrieve the User instance based on user email and password
        user = self.user_object_from_credentials(user_email, user_pwd)

        # Return the User instance
        return user
