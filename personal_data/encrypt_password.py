#!/usr/bin/env python3
"""Module for encrypt password"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    # Generate a salt
    salt = bcrypt.gensalt()

    # Generate a salted, hashed password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password

def is_vaild(hashed_password: bytes, passowrd: str) -> bool:
    """ VAlidates tht the provided matches the hashed password."""
    return bcrypt.checkpw(password.encode(), hashed_password)

