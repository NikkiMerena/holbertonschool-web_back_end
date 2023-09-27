# Authentication and Session Management

This project extends upon `Basic Authentication` to include more advanced features like session-based authentication.

## Resources

- [REST API Authentication Mechanisms - Only the session auth part](https://www.youtube.com/watch?v=501dpx2IjGY)
- [HTTP Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cookie)
- [Flask](https://palletsprojects.com/p/flask/)
- [Flask Cookie](https://flask.palletsprojects.com/en/1.1.x/quickstart/#cookies)

---

## Tasks

### Task 0: Et moi et moi et moi!

- Copy work from the previous project.
- Implement a `GET /users/me` endpoint to retrieve the authenticated User.

### Task 1: Empty Session

- Create a class `SessionAuth` that inherits from `Auth`.

### Task 2: Create a Session

- Implement method `def create_session(self, user_id: str = None) -> str:` to create a session ID for a `user_id`.

### Task 3: User ID for Session ID

- Implement method `def user_id_for_session_id(self, session_id: str = None) -> str:` to return a User ID based on a Session ID.

### Task 4: Session Cookie

- Implement method `def session_cookie(self, request=None):` to return a cookie value from a request.

### Task 5: Before Request

- Update the `@app.before_request` method to include new authentication checks.

### Task 6: Use Session ID for Identifying a User

- Implement method `def current_user(self, request=None):` to return a User instance based on a cookie value.

### Task 7: New View for Session Authentication

- Create a new Flask view that handles all routes for the Session authentication.

### Task 8: Logout

- Implement method `def destroy_session(self, request=None):` to delete the user session / logout.

---
