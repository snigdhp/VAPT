## 37. Second-Order SQL Injection
### Q37. What is 2nd-Order SQLi?

**Answer / Notes:**

- First-order SQLi:

    - Injection and exploitation happen in the same request.

- Second-order SQLi:

    - Attacker injects malicious data which is stored in the database.

    - Later, another part of the app uses that stored data in an unsafe query.

    - The injection is triggered at that later point.

**Example**:

Attacker registers with username:

test' ; DROP TABLE users;--


App stores username safely (no immediate error).

Admin panel later uses:

"SELECT * FROM logs WHERE username = '" + storedUsername + "'"


That query is now vulnerable, and the stored malicious username triggers SQLi.

Key point:
You must parameterize both on input and when stored values are reused in SQL.

---
## 38. Secure Password Storage
### Q38. How do you store passwords for applications in the database?

**Answer / Notes:**

Never store plaintext or simply encrypted passwords.

Use a slow, password-specific hashing function:

bcrypt, scrypt, Argon2, or PBKDF2 with high iterations.

Use a unique salt per user.

Optionally use a pepper (application secret) stored separately from DB.

Process:

User chooses password.

System generates random salt.

Computes hash = bcrypt(password + salt).

Store: { user_id, salt, hash, algorithm, parameters }.

---
## 39. Remote Code Execution (RCE)
### Q39. What is RCE? How do you test for RCE? How can it be remediated?

**Answer / Notes:**

RCE (Remote Code Execution):

Attacker can run arbitrary code/commands on the server from a remote location.

Testing (in-scope and safe):

Identify user input that reaches:

eval, system, exec, template engines, deserialization, file handling.

Use non-destructive payloads:

whoami, id, sleep 5 to confirm execution.

Always respect scope and avoid destructive commands.

Remediation:

Avoid dynamic command or code execution with user input.

Replace shell calls with safe library functions.

Apply allow-list validation.

Run services under least privilege and consider sandboxing.

Patch vulnerable libraries/frameworks.

---
## 40. OS Command Injection
### Q40. Explain OS Command Injection.

**Answer / Notes:**

Occurs when an application builds a system command string using untrusted input and passes it to shell functions (system, exec, popen, backticks).

Attacker uses shell metacharacters (;, &&, |) to run additional commands.

Vulnerable example:

os.system("ping -c 4 " + user_input)


If user_input = "127.0.0.1; cat /etc/passwd", both ping and cat /etc/passwd run.

Mitigation:

Avoid shell commands; use library APIs instead.

If shell is absolutely necessary, use safe argument lists and strict allow-list validation.

Run under a low-privilege OS account and use sandboxing/containers.

---
## 41. CORS & CSRF
### Q41. What is CORS and SOP? Does CORS protect against CSRF?

**Answer / Notes:**

SOP (Same-Origin Policy):

Default browser rule: one origin cannot read responses from another origin.

CORS (Cross-Origin Resource Sharing):

Mechanism where a server explicitly allows specific other origins to read its responses via JS.

Implemented with headers like Access-Control-Allow-Origin.

Does CORS protect against CSRF?

No. CORS is not a CSRF defense.

Browsers will still send cookies on cross-site requests unless SameSite or other controls are in place.

CSRF only needs the victim’s browser to send an authenticated request; the attacker doesn’t need to read the response.

Misconfigured CORS can even expose more data to attackers.

---
## 42. XXE (XML External Entity)
### Q42. Explain XXE. What causes this flaw? How do you mitigate it?

**Answer / Notes:**

XXE (XML External Entity):

Vulnerability where XML parsers allow external entities (<!ENTITY>) to be resolved.

Attacker can read local files, perform SSRF, or cause DoS via crafted XML.

Cause:

XML parsers configured with:

DTD processing enabled.

External entity resolution allowed by default.

Example payload:

<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<root>
  <data>&xxe;</data>
</root>


Mitigation:

Disable DTD and external entity resolution.

Use secure parser settings or safe XML APIs.

Validate and sanitize XML input.

Prefer JSON over XML where possible.

---
## 43. Security-Related Request Headers
### Q43. What are some security headers in HTTP requests?

**Answer / Notes:**

Origin

Shows origin of the request; used in CORS and CSRF defenses.

Referer (Referrer)

Indicates the page the user came from; useful for CSRF checks and logging.

Authorization

Carries credentials (Bearer tokens, Basic auth); must be sent only over HTTPS.

Cookie

Sends cookies (including session ID); combined with cookie flags determines security behavior.

X-Requested-With

Often XMLHttpRequest; sometimes used as a weak CSRF indicator (not reliable alone).

X-Forwarded-For / X-Real-IP

Forward client IP through proxies; important for logging and rate limiting.

---
## 44. HTTP Methods
### Q44. What are various HTTP methods?

**Answer / Notes:**

GET – Retrieve data (should be safe and idempotent).

POST – Create a resource or perform an action (state-changing; not idempotent).

PUT – Replace a resource at a URI (idempotent).

PATCH – Partially update a resource.

DELETE – Delete a resource.

HEAD – Same as GET but returns only headers.

OPTIONS – Describe communication options (CORS preflight).

TRACE – Diagnostic loopback; usually disabled.

---
## 45. Difference Between GET, POST, PUT
### Q45. What is difference in GET, POST, and PUT requests?

**Answer / Notes:**

GET

Purpose: Read/fetch data.

Data is typically in the URL query string.

Should not change server state; often cached and logged.

POST

Purpose: Create new resources or perform actions.

Data is in the request body.

Not idempotent by definition (multiple POSTs can create multiple items).

PUT

Purpose: Replace existing resource at a specific URI.

Idempotent; sending the same PUT multiple times produces the same final state.

Common in REST APIs for resource updates.

---
## 46. Race Condition
### Q46. Explain Race Condition. How can you test for it?

**Answer / Notes:**

Race condition:

Occurs when the outcome depends on the timing of concurrent operations.

Attackers exploit it to bypass logic, double-spend, or break invariants.

Example:
Multiple parallel requests to redeem the same coupon or withdraw funds, resulting in more money being withdrawn than allowed.

Testing:

Send many concurrent requests:

Use Burp Intruder with parallel threads.

Use custom scripts (threads/promises/async calls).

Observe if:

A coupon can be applied multiple times.

Balance goes negative.

One-time use tokens are reused.

Mitigation:

Use database transactions and locking.

Enforce invariants with DB constraints.

Design operations to be idempotent wherever possible.

---
## 47. Cookie Attributes / Flags
### Q47. Explain Cookie Attributes/Flags.

**Answer / Notes:**

Secure

Cookie only sent over HTTPS connections.

HttpOnly

Cookie not accessible via JavaScript (document.cookie); mitigates theft via XSS.

SameSite

Controls cross-site sending of cookies:

Strict – Only same-site requests.

Lax – Sent on top-level navigations (e.g., link clicks).

None – Sent on all cross-site requests (must be Secure).

Domain

Determines which domain/subdomains receive the cookie (.example.com vs app.example.com).

Path

Restricts cookie to certain URL paths.

Expires / Max-Age

Sets cookie lifetime (session vs persistent cookies).

---
## 48. Threat Modeling
### Q48. What is Threat Modeling / Threat Model?

**Answer / Notes:**

Threat modeling is a structured process to:

Understand the system (components, data flows, trust boundaries).

Identify assets and potential attackers.

Identify threats and abuse cases.

Prioritize risks and plan mitigations.

Typical steps:

Diagram the system and data flows.

Identify threats (often using frameworks like STRIDE).

Rate threats by likelihood and impact.

Define and implement mitigations.

Validate that mitigations work as intended.

---
## 49. SDLC & Security Involvement
### Q49. Are you aware of the SDLC? When in SDLC should you engage with developers?

**Answer / Notes:**

SDLC phases (simplified):

Requirements → Design → Implementation → Testing → Deployment → Maintenance.

Security should be involved from the beginning (“shift left”):

Requirements: define security & compliance requirements.

Design: conduct threat modeling and secure design review.

Implementation: support secure coding, SAST, code reviews.

Testing: DAST, penetration testing, SCA.

Deployment & Maintenance: hardening, monitoring, patching.

---
## 50. CI/CD & Security
### Q50. What is a CI/CD pipeline? Explain its role in security.

**Answer / Notes:**

CI (Continuous Integration):

Automatically build and test code on each commit/merge.

CD (Continuous Delivery/Deployment):

Automatically push builds to staging/production environments.

Security Integration:

Add SAST, SCA, secret scanning in CI stages.

Add DAST, IaC scanning, container image scanning in CD stages.

Use quality gates to fail builds on critical vulnerabilities.

Enforce signed artifacts, review of IaC, and secure deployment configs.

---
## 51. Classifying Web Vulnerabilities by Severity
### Q51. Classify some web vulnerabilities into Low, Medium, High, and Critical. Reason why.

**Answer / Notes:**

Critical

RCE, SQLi with full DB access, auth bypass, unrestricted admin access.

Reason: leads to complete compromise of confidentiality, integrity, and availability.

High

Stored XSS impacting many users, IDOR exposing PII, SSRF into internal network, privilege escalation.

Reason: serious impact; may require user interaction or conditions.

Medium

Reflected XSS on non-critical pages, open redirect, detailed error messages revealing stack traces.

Reason: moderate impact alone; often useful when chained with other issues.

Low

Missing non-critical security headers, verbose version banners without known exploit.

Reason: low direct impact; mainly assists in reconnaissance and attack chaining.

---
## 52. MD5 vs Strong Hashes
### Q52. Known that MD5 is not the most secure hashing algorithm, why don’t we always use SHA-256 or others?

**Answer / Notes:**

Context matters:

For non-security uses (e.g., simple file checksums), MD5 may still be used for speed and tool compatibility.

For security-sensitive operations:

MD5 is broken (collisions, preimage attacks) and should be avoided.

For passwords, even raw SHA-256 is not ideal:

Fast hashes are easier to brute force.

We prefer bcrypt/scrypt/Argon2/PBKDF2 which are slow and tunable.

Why not always SHA-256?

Legacy systems and protocols may rely on MD5.

For passwords, we use dedicated password-hashing functions, not just SHA-256.

For some internal, non-security validations, MD5 can be “good enough” as a checksum.

---
## 53. Nginx Fronting Multiple Microservices
### Q53. Internet-facing Nginx is in front of multiple applications (microservice architecture) via different subdomains. What can go wrong?

**Answer / Notes:**

Potential risks:

Misconfigured virtual hosts / routing

Requests go to wrong backend, causing data leakage across services.

Over-broad cookie scope

Cookies scoped to .example.com might be sent to all subdomains, enabling cross-application attacks.

Overly permissive CORS between subdomains

One compromised subdomain can read sensitive data from others.

Single point of failure

Compromised Nginx or config impacts all services behind it.

Header mishandling

Incorrect trust in Host, X-Forwarded-For, etc., can enable host header injection, cache poisoning, SSRF routing.

TLS misconfiguration

Wrong certs for subdomains, missing SNI, weak cipher suites.

---
## 54. SSL Certificate vs Injection Attacks
### Q54. Can server SSL certificate prevent injection attacks (e.g., SQLi)? Explain.

**Answer / Notes:**

No. SSL/TLS:

Ensures confidentiality and integrity of data in transit.

Authenticates the server to the client.

Injection attacks exploit how the server processes input, not the transport channel.

A site can be fully HTTPS with a valid certificate and still be vulnerable to SQLi, XSS, and command injection.

---
## 55. XSS but Blank Popup
### Q55. An attacker is trying to extract session cookie using XSS, but a blank popup is shown. What could be the reason?

**Answer / Notes:**

Most likely, the session cookie is marked HttpOnly.

document.cookie cannot access HttpOnly cookies.

alert(document.cookie) will show only non-HttpOnly cookies or be empty.

So even though XSS exists, the session cookie cannot be directly read by JavaScript.

---
## 56. Secure PDF Download
### Q56. Web application allows user to download their account statement in PDF. How can you securely implement this?

**Answer / Notes:**

Key principles:

Strong authorization checks

Ensure the authenticated user is allowed to access that statement (no IDOR).

No sensitive data in URL

Avoid embedding account numbers or tokens directly in query parameters where possible.

Transport security

Always use HTTPS for downloads.

PDF generation security

Generate PDFs server-side with trusted templates.

Sanitize any user-supplied data included in the PDF.

Avoid or limit active content (JavaScript, external references).

Short-lived signed URLs (optional)

For emailed links, use signed, expiring URLs.

Audit logging

Log who downloaded which statement and when.

---
##  57. STRIDE
### Q57. What is STRIDE?

**Answer / Notes:**

STRIDE is a threat modeling mnemonic that categorizes threats as:

S – Spoofing (pretending to be someone else)

T – Tampering (modifying data)

R – Repudiation (denying having performed an action)

I – Information disclosure (data leaks)

D – Denial of service (making service unavailable)

E – Elevation of privilege (gaining higher access)

Used to systematically think through what can go wrong for each component or data flow.

---
## 58. CIA Triad
### Q58. What is the CIA triad?

**Answer / Notes:**

C – Confidentiality

Prevent unauthorized access to information.

Controls: encryption, access controls, data classification.

I – Integrity

Ensure data is accurate, complete, and not tampered with.

Controls: hashing, digital signatures, checksums, integrity checks.

A – Availability

Ensure systems and data are accessible when needed.

Controls: redundancy, backups, failover, DDoS protection.

Example:
“For an online banking system, confidentiality protects account data, integrity ensures transactions can’t be altered silently, and availability ensures customers can access their accounts when needed.”

---

### 1. Basic definitions

## Brute Force Attack

- Attacker tries many passwords against a single user account.
    - Focus is: one username, lots of passwords.

Example: Trying Password1!, Password2!, Summer2024!, Qwerty@123, etc. repeatedly on user1@example.com.

- Password Spraying Attack

Attacker tries a few common passwords against many user accounts.
    - Focus is: many usernames, few passwords.

Example: Trying Welcome@123 on 500 different usernames, then Password@123 on the same 500, and so on.

---
## 2. Key differences (at a glance)

## Aspect	Brute Force Attack	Password Spraying Attack
## Target pattern	Single / few accounts	Large number of accounts
## Password variety	Many different passwords	Few common passwords
## Goal	Crack specific account(s)	Get any valid account (even low-value)
## Lockout risk	High (many failed attempts on same user)	Lower (few attempts per user, bypasses lockout policies)
## Detection profile	Easy to spot on per-user failed login trends	Harder; failures spread across many users
## Typical passwords used	Wordlists, permutations, full brute force	Very common, weak, or default passwords
## Noise level	Noisy on that account	“Low and slow”; looks like normal user errors

---
## 3. Why password spraying is dangerous

- Most organizations use account lockout or throttling (e.g., 5 failed attempts → lockout).
    - Brute force hits that limit quickly on one account.
- Password spraying stays under the threshold per account (e.g., 1–2 attempts per user), so:
    - It avoids lockouts.
- It is harder for SOC to detect via simple “failed login per user” alerts.
    - It often succeeds because many users share common passwords (Welcome@123, Company@2025, etc.).

---
## 4. Typical detection indicators

- Brute Force

    - High number of failed attempts for a single username.
    - Source IP may be single or a small set.
    - Short time window, very bursty traffic.
    - Password Spraying
    - Low number of failures per user, but:
    - Same password attempted across many accounts.
    - Similar timing and source(s).
    - Patterns more visible if you analyze by:
    - “Failed login count per source IP” or “Same password hash in failed attempts across multiple usernames”.

---
## 5. Mitigation strategies (for both)

## High-level defenses:

##Strong password policy

## Enforce length + complexity + no reuse of known breached passwords.

## Account lockout / throttling

## Progressive delays, CAPTCHAs, or lockout after several failures.

## Multi-Factor Authentication (MFA)

## Even if password is compromised, attacker cannot easily log in.

## Login anomaly detection

## Monitor by IP, device, geolocation, impossible travel, and common password patterns.

## User education

## Avoid “Welcome123”, “Password@123”, “CompanyName@2025” style passwords.

## Protocol hardening

## Disable legacy protocols that don’t support modern auth (e.g., old IMAP/POP/SMTP auth).

--- 

### 6. One-liner difference for interview

Brute force: Many passwords against one user.

Password spraying: A few common passwords against many users to evade lockouts.

---
## 1. Quick recap: what is rate limiting in this context?

In authentication, rate limiting means:
“Do not allow more than X login attempts in Y time window.”

It can be applied on different keys:

Per user account (e.g., max 5 failed attempts per user per 10 minutes)

Per IP address / client (e.g., max 20 login attempts per IP per minute)

Per IP + user combination

Global / per subnet / per country, etc.

Often combined with lockout, CAPTCHA, or exponential backoff.

## 2. How brute force interacts with rate limiting

Brute Force = many passwords on one account.

If you have per-account rate limiting / lockout, brute force is:

Very likely to hit the limit quickly.

Easy to detect: “user A has 100 failed logins in 2 minutes.”

Mitigation: account lockout, delay, or CAPTCHA after N failures.

So:

Brute force is noisy and rate limiting on a single account is usually enough to slow or block it.

3. How password spraying interacts with rate limiting

- Password Spraying = few passwords on many accounts.

- Attack strategy is explicitly designed to bypass simple rate limits, like:

- “Max 5 failed attempts per user per 10 minutes”

Example:

- Attacker has 1000 usernames.

- They try Welcome@123 once on each username.

- Per-user failures = 1 → below the per-account limit.

- They wait, then try another common password on all accounts.

- Unless you also have per-IP / per-origin rate limiting, the spray may:

- Not trigger per-user lockouts.

- Look like normal user mistakes (1–2 wrong passwords).
    - Password spraying is a low-and-slow technique to stay under basic rate limits and lockout thresholds.

## 4. How good rate limiting should be designed (to handle both)

- To handle both brute force and password spraying you want:
    - Per-account limits

- Protects individual users from brute forcing.
    - Per-IP / per-client limits

- Limits total attempts from a single source.
    - Makes password spraying harder from a single IP.

- Behavioral / anomaly checks

    - Many usernames from same IP in a short time window.

    - Same password tried across many accounts.

    - Geo / ASN-based heuristics (suspicious networks).

    - Additional controls beyond rate limiting

    - MFA

    - CAPTCHA on suspicious patterns

    - Device fingerprinting, impossible travel, etc.

---
## 5. One-liner for interview

Brute force vs rate limit: Brute force is usually blocked by simple per-account rate limiting or lockout.

Password spraying vs rate limit: Password spraying is designed to stay under per-account limits, so you need smarter rate limiting (per-IP, behavioral) and MFA to stop it.