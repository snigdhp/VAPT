# BOLA (API1:2023) — Broken Object Level Authorization

## Intro
**API1:2023 Broken Object Level Authorization (BOLA)** is one of the most prevalent and severe vulnerabilities for APIs. BOLA vulnerabilities occur when an API provider does not have sufficient controls in place to enforce authorization. In other words, API users should only have access to sensitive resources that belong to them. When BOLA is present, an attacker will be able to access the sensitive data of other users.

---

## OWASP Attack Vector Description
Attackers can exploit API endpoints that are vulnerable to broken object-level authorization by manipulating the ID of an object that is sent within the request. Object IDs can be anything from sequential integers, UUIDs, or generic strings. Regardless of the data type, they are easy to identify in the request target (path or query string parameters), request headers, or even as part of the request payload.

---

## OWASP Security Weakness Description
This has been the most common and impactful attack on APIs. Authorization and access control mechanisms in modern applications are complex and widespread. Even if the application implements a proper infrastructure for authorization checks, developers might forget to use these checks before accessing a sensitive object. Access control detection is not typically amenable to automated static or dynamic testing.

---

## OWASP Impacts Description
Unauthorized access can result in data disclosure to unauthorized parties, data loss, or data manipulation. Unauthorized access to objects can also lead to full account takeover.

---

## Summary
If an API endpoint does not have sufficient access controls, it will not perform checks to make sure users can only access their own resources. When these controls are missing, **User A** will be able to obtain **User B’s** resources via API requests.

APIs use some sort of value, like names or numbers, to identify various objects. When an attacker discovers an API's resource IDs, they will attempt to obtain the resources when unauthenticated or authenticated as a different user.

---

## Example Scenario

Imagine that an authenticated user, **Bruce**, sends a GET request:

```http
GET https://herohospital.com/api/v3/users?id=2727

And receives:
{
  "id": "2727",
  "fname": "Bruce",
  "lname": "Wayne",
  "dob": "1975-02-19",
  "username": "bman",
  "diagnosis": "Depression"
}

This is expected (Bruce accessing Bruce’s data). However, if Bruce can access another user’s information using a different resource ID, then a BOLA vulnerability exists.

For example, Bruce sends:
GET https://herohospital.com/api/v3/users?id=2728

And receives:
{
  "id": "2728",
  "fname": "Harvey",
  "lname": "Dent",
  "dob": "1979-03-30",
  "username": "twoface",
  "diagnosis": "Dissociative Identity Disorder"
}
---

## If Bruce is still using his own authorization to access this data, that is a clear indication the API is vulnerable to BOLA.

---


