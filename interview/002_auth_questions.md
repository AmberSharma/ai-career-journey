d# Authentication & Authorization - Interview Questions

## 1. Authentication vs Authorization

| Aspect         | Authentication                        | Authorization                              |
|----------------|---------------------------------------|--------------------------------------------|
| **What**       | Verifies **who you are**              | Determines **what you can access**         |
| **When**       | Happens **first**                     | Happens **after** authentication           |
| **Example**    | Logging in with username & password   | Admin can delete users, regular user cannot|
| **HTTP Code**  | `401 Unauthorized` (identity unknown) | `403 Forbidden` (identity known, no access)|

**One-liner:** Authentication confirms identity; Authorization grants permissions.

---

## 2. What is JWT?

JWT (JSON Web Token) is a compact, URL-safe token used to securely transmit information between two parties as a JSON object.

**Structure:** A JWT has three parts separated by dots (`.`):

```
header.payload.signature
```

- **Header** - Algorithm used (e.g., HS256) and token type (JWT).
- **Payload** - Claims/data (e.g., user ID, role, expiry time).
- **Signature** - Created by signing `header + payload` with a secret key. Used to verify the token hasn't been tampered with.

**Key points:**
- JWTs are **signed**, not encrypted -- anyone can read the payload, but only the server can verify/create a valid signature.
- They are **stateless** -- the server does not need to store session data.
- Commonly used in API authentication via the `Authorization: Bearer <token>` header.

---

## 3. Why Does a Token Expire?

Tokens expire to **limit the damage window** if a token is compromised.

**Reasons:**
- **Security** -- A stolen token without expiry gives permanent access. Expiry limits the attacker's window.
- **Revocation is hard** -- Since JWTs are stateless (not stored on the server), there is no easy way to invalidate them. Expiry acts as an automatic invalidation mechanism.
- **Fresh context** -- User roles/permissions may change. Short-lived tokens force re-verification of the user's current state.

**Common pattern:**
- **Access token** -- Short-lived (15-30 minutes). Used for API calls.
- **Refresh token** -- Long-lived (days/weeks). Used to get a new access token without re-login.

---

## 4. Session vs Token

| Aspect            | Session-based                          | Token-based (JWT)                        |
|-------------------|----------------------------------------|------------------------------------------|
| **Storage**       | Server stores session data (memory/DB) | Client stores the token (localStorage/cookie) |
| **Statefulness**  | **Stateful** -- server must track sessions | **Stateless** -- server verifies token on each request |
| **Scalability**   | Harder to scale (session must be shared across servers or use sticky sessions) | Easy to scale (any server can verify the token independently) |
| **Revocation**    | Easy -- delete session from server     | Hard -- token is valid until it expires   |
| **Performance**   | Requires DB/cache lookup per request   | No lookup needed; token is self-contained |
| **Use case**      | Traditional web apps (server-rendered) | SPAs, mobile apps, microservices, APIs   |

**One-liner:** Sessions keep state on the server; Tokens keep state on the client.
