#!/usr/bin/env python3
"""Module for BasicAuth class"""

from .auth import Auth
import base64


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
        user_email, user_password = decoded_base64_authorization_header.split(':', 1)
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
