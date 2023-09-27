#!/usr/bin/env python3
""" Model: """

from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """ SessionAuth class for handling user sessions """

    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a Session ID for a user_id

        :param user_id: the user id for which to create the session
        :type user_id: str
        :return: the Session ID created
        :rtype: str
        """
        if user_id is None or not isinstance(user_id, str):
            return None

        session_id = str(uuid.uuid4())  # Generate a Session ID using uuid4()
        self.user_id_by_session_id[session_id] = user_id
        return session_id  # Return the generated Session ID

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        Returns a User ID based on a Session ID

        :param session_id: the session id for which to retrieve the user id
        :type session_id: str
        :return: the User ID associated with the session id
        :rtype: str
        """
        if session_id is None or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)
