#!/usr/bin/env python3
"""_summary_
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database."""

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> bytes:
        """Hash a password and return the salted hash."""
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
        return hashed_password

    def register_user(self, email: str, password: str) -> User:
        """Register a user."""
        try:
            # Try to find a user by email
            user = self._db.find_user_by(email=email)
            # If the user is found, raise a ValueError
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            # If NoResultFound is raised, hash the password
            hashed_password = self._hash_password(password)
            # Add user to the database and return the User object
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """Validates if login credentials are correct."""
        try:
            user = self._db.find_user_by(email=email)
            hashed_password = user.hashed_password
            return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
        except Exception:
            return False

    def _generate_uuid() -> str:
        """
        Generate a string representation of a new UUID
        """
        return str(uuid.uuid4())

    def create_session(self, email: str) -> str:
        """Create a new session for a user."""
        try:
            # Find the user by email
            user = self._db.find_user_by(email=email)

            # Generate a new UUID as session_id
            session_id = str(uuid.uuid4())

            # Update the user’s session_id in the database
            self._db.update_user(user.id, session_id=session_id)

            # Return the session_id
            return session_id
        except NoResultFound:
            return None
