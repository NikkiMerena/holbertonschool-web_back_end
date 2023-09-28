#!/usr/bin/env python3
"""_summary_
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Takes in a password string argument and returns bytes.
    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw.
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password
