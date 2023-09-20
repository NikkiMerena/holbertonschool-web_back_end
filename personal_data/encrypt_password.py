#!/usr/bin/env python3


import bcrypt

def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    # Generate a salt
    salt = bcrypt.gensalt()

    # Generate a salted, hashed password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
