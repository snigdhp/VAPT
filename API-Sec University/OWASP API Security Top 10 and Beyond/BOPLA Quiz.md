## Question 1
**Which of the following best describes an "Excessive Data Exposure" vulnerability?**

- The API allows unrestricted access to all the data in the database.
- **The API responds with more information than needed to fulfill a request.** *(Correct answer.)*
- The API does not authenticate user requests.
- The API stores sensitive data in plaintext.

---

## Question 2
**What could be a consequence of "Mass Assignment" vulnerability?**

- It could allow a user to execute arbitrary code.
- It could lead to a denial of service attack.
- **It could allow a user to escalate privileges or edit object properties.** *(Correct answer.)*
- It could lead to an information disclosure within a compromised JWT.

---

## Question 3
**When an API exposes an object, which of the following is NOT a recommended preventative measure?**

- **Use generic methods such as `to_json()` and `to_string()`.** *(Correct answer.)*
- Cherry-pick specific object properties you specifically want to return.
- Implement a schema-based response validation mechanism as an extra layer of security.
- Keep returned data structures to the bare minimum, according to the business/functional requirements for the endpoint.

---

## Question 4
**What is the potential impact of unauthorized access to an API endpoint due to broken object property level authorization?**

- **Data disclosure to unauthorized parties, data loss, or data manipulation.** *(Correct answer.)*
- The application could crash, leading to a denial of service.
- The attacker could perform remote code execution.
- The provider could perform a local file inclusion attack.

---

## Question 5
**How can you detect if an API endpoint is vulnerable to excessive data exposure?**

- By sending a large number of requests in a short period of time and checking if the server crashes.
- By reviewing the web page's HTML to find security flaws.
- **By sending requests to the target API endpoints and reviewing the information sent in response.** *(Correct answer.)*
- By analyzing the HTTP request headers for sensitive information.
