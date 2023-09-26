#!/usr/bin/env python3
"""Module for BasicAuth class"""

from .auth import Auth


class BasicAuth(Auth):
    """BasicAuth class

    This class is used for handling Basic Authentication
    It inherits from the Auth class
    """
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
