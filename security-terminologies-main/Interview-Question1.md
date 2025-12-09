# Pentesting Interview Q&A Notes

This README contains structured interview questions and concise notes for network/web penetration testing, security fundamentals, and related tooling.

---

## 1. Starting a Pentest – Information Gathering & Enumeration

### Q1. How do you start hacking a target? What are information gathering and enumeration?

**Answer / Notes:**

- I don’t start by attacking directly. First, I do **Information Gathering (Reconnaissance)**:
  - Collect publicly available data **without touching** the target systems.
  - Examples: WHOIS records, DNS records, subdomains, OSINT, emails, technology stack, public IP ranges.
- Next, I move to **Enumeration**:
  - Actively interact with the target systems:
    - Port scanning, service detection, banner grabbing.
    - User enumeration, share enumeration, configuration discovery.
- Together, **recon + enumeration** give a clear map of:
  - Which hosts exist, which ports are open, which services and versions are running, which users and configurations are exposed.
- Only after this mapping do I identify potential weaknesses and plan exploitation.

---

## 2. Phases of Network Penetration Testing

### Q2. What are the typical phases of Network Penetration Testing?

**Answer / Notes:**

1. **Planning & Scope**
   - Define scope, targets, rules of engagement, timelines.
   - Obtain legal approvals and written authorization.

2. **Information Gathering**
   - Passive reconnaissance and OSINT.
   - Discover domains, IP ranges, technologies, public data.

3. **Scanning & Enumeration**
   - Use tools like Nmap/Masscan for port scanning.
   - Service and version detection, OS fingerprinting.
   - Enumerate users, shares, services, and configurations.

4. **Vulnerability Analysis**
   - Map discovered services to known vulnerabilities and misconfigurations.
   - Use vulnerability scanners and manual analysis.

5. **Exploitation**
   - Attempt to exploit validated vulnerabilities.
   - Gain initial access, respecting scope and rules.

6. **Post-Exploitation**
   - Privilege escalation, pivoting, lateral movement (if allowed).
   - Data access, impact demonstration, persistence (controlled and documented).

7. **Reporting**
   - Document findings, impact, PoC steps, and remediation guidance.
   - Provide both technical and management-level summaries.

---

## 3. Nmap Usage

### Q3. Which Nmap flag is used for version detection?

**Answer / Notes:**

- Use **`-sV`** for **Service Version Detection**.
- It probes open ports to determine:
  - Which service is running.
  - Which version (e.g., `Apache httpd 2.4.41`).

### Q4. What is the difference between `-v` and `-V` in Nmap?

**Answer / Notes:**

- **`-v` (lowercase v)** – **Verbosity**
  - Shows more detailed output during scans:
    - Open ports as they are found.
    - Scan progress updates, additional logging.
- **`-V` (uppercase V)** – **Nmap Program Version**
  - Prints Nmap’s own version and exits.
  - Used to check which Nmap release is installed.

---

## 4. SQL Injection & RCE

### Q5. Can SQL Injection lead to Remote Code Execution (RCE)?

**Answer / Notes:**

- **Yes**, SQL Injection **can** lead to RCE, but not always.
- It depends on:
  - Database configuration and privileges.
  - Whether dangerous features are enabled, such as:
    - `xp_cmdshell` on SQL Server.
    - Ability to write files to webroot (web shell).
    - Ability to load extensions or UDFs.
- If the database can:
  - Execute OS commands.
  - Read/write critical system files.
- Then SQLi can escalate from a **database-level issue** to **full server compromise**.

---

## 5. Black-Box vs White-Box Pentesting

### Q6. What is the difference between Black-Box Pentesting and White-Box Pentesting?

**Answer / Notes:**

- **Black-Box Pentesting:**
  - Tester has **no prior internal knowledge** of the system.
  - Only public-facing information is available (websites, public IPs).
  - Simulates an **external attacker**.
  - Focus on discovering vulnerabilities from an outsider’s perspective.

- **White-Box Pentesting:**
  - Tester has **full internal knowledge**:
    - Source code, architecture diagrams, credentials, configs.
  - More like an **internal security review**.
  - Helps identify deeper logic and code-level vulnerabilities efficiently.

---

## 6. Vulnerability Scanners

### Q7. Have you worked with Nessus / Qualys?

**Answer / Notes:**

- **Yes**, with **ServiceNow context**:
  - Ingesting Nessus/Qualys scan results into ServiceNow.
  - Using them to populate Vulnerability Response or ITSM records.
  - Driving remediation workflows and dashboards based on scanner findings.

### Q8. What are some open-source alternatives to Nessus or Qualys?

**Answer / Notes:**

- **OpenVAS / Greenbone** – Full-featured open-source vulnerability scanner.
- **Nmap + NSE scripts** – For targeted vulnerability and service checks.
- **Nikto** – Open-source web server vulnerability scanner.

---

## 7. Vulnerability Rating & CVSS

### Q9. How do you rate vulnerabilities? Explain the scoring / framework.

**Answer / Notes:**

- I typically use **CVSS (Common Vulnerability Scoring System)**.
- CVSS provides a **0.0–10.0** score based on:
  - **Exploitability**:
    - Attack vector (network, local).
    - Attack complexity.
    - Required privileges.
    - User interaction.
  - **Impact**:
    - Confidentiality.
    - Integrity.
    - Availability.
- Scores are categorized as:
  - **Low**, **Medium**, **High**, **Critical**.
- Example:
  - RCE on internet-facing server → **CVSS 9.8 (Critical)** → needs immediate remediation.
  - Local privilege escalation on internal system → **CVSS ~6.5 (Medium)** → patch in next maintenance window.

---

## 8. Tools Used in Network Pentesting

### Q10. Name some tools you use in Network Pentesting.

**Answer / Notes:**

**Scanning & Enumeration:**
- `Nmap` – Port scanning, service detection, OS fingerprinting.
- `Masscan` – Very fast port scanner for large IP ranges.
- `Netcat` / `Ncat` – Banner grabbing, simple client/server sockets.

**Vulnerability Scanning:**
- **OpenVAS** – Open-source vulnerability scanning.
- **Nessus / Qualys** – Commercial vulnerability scanners.
- **Nmap NSE Scripts** – Targeted vulnerability checks.

**Passwords / Authentication:**
- **Hydra** – Brute force attacks on FTP, SSH, SMB, etc.
- **CrackMapExec (CME)** – AD / Windows network enumeration and auth spraying.

**Exploitation Frameworks:**
- **Metasploit Framework** – Exploits, payloads, post-exploitation modules.
- **Exploit-DB / searchsploit** – Public exploit repository and CLI.

**Network Sniffing / MITM:**
- **Wireshark** – Network packet capture and protocol analysis.
- **Ettercap** – Man-in-the-middle attacks (ARP spoofing, sniffing).

**Web-Facing Targets:**
- **Nikto** – Web server vulnerability scanning.
- **OWASP ZAP** / **Burp Suite** – Interception proxy, active scanning, fuzzing.
- **Gobuster / Dirb** – Directory and file enumeration (brute-force URLs).

---

## 9. Reporting Vulnerabilities After Pentest

### Q11. How do you report vulnerabilities or security gaps after pentesting?

**Answer / Notes:**

1. **Start with Approach & Methodology**
   - Scope, tools, techniques, and limitations.
   - High-level description of what was tested and how.

2. **For Technical Teams:**
   - Detailed vulnerability description.
   - **CVSS severity** and, for web issues, **OWASP category**.
   - **Steps to reproduce** with payloads and requests/responses.
   - **Evidence**: screenshots, logs, sample output.
   - **Remediation guidance**: configuration changes, code fixes, patches.

3. **For Non-Technical / Management:**
   - Executive summary in plain language.
   - Business impact: data exposure, downtime, potential financial/regulatory risk.
   - Risk levels and remediation **priorities**.
   - Suggested remediation roadmap and timelines.

---

## 10. HTTP Status Codes in Pentesting

### Q12. What HTTP status codes do you monitor during a pentest? Explain some interesting ones.

**Answer / Notes:**

- I watch how **status codes change as I tweak payloads**.

**Examples (Path Traversal & File Access):**
- **200 OK / 206 Partial Content**
  - If an obfuscated traversal payload suddenly returns 200/206 and the body looks like `/etc/passwd` or logs, it indicates:
    - The payload was accepted.
    - I may be reading a real file.

- **403 Forbidden**
  - Means the path/resource exists but access is blocked.
  - I try:
    - Different encodings.
    - Alternate traversal patterns.
    - Path obfuscation.
  - A **403 → 200** change after obfuscation is a classic sign of weak filtering.

- **404 Not Found**
  - Indicates file/resource does not exist at that path.
  - Used to calibrate:
    - Number of `../` needed.
    - Whether traversal is resolving correctly.

**Other Codes I Monitor:**
- **401 / 403 / 404 Patterns**
  - Identify possible authorization issues and IDOR.
- **302 / 307**
  - Understand redirection in login/auth flows and access controls.
- **429 Too Many Requests**
  - Assess rate limiting on login forms, OTP endpoints, and other sensitive actions.

---

## 11. Zero-Day Attacks

### Q13. What is a 0-Day (Zero-Day) attack?

**Answer / Notes:**

- **Zero-Day Vulnerability**:
  - A previously unknown software bug with **no public patch** available.
- **Zero-Day Exploit**:
  - The actual code or technique used to exploit that vulnerability.
- **Zero-Day Attack**:
  - Real-world use of that exploit against a target.
- Because it’s unknown to the vendor and defenders:
  - There are no signatures or patches.
  - Traditional AV/IDS/IPS may fail to detect it.

---

## 12. SSL/TLS-Related Vulnerabilities

### Q14. Mention some SSL/TLS-related vulnerabilities.

**Answer / Notes:**

- Use of **outdated protocols**:
  - SSLv2, SSLv3, TLS 1.0 / 1.1.
- **Weak cipher suites**:
  - RC4, 3DES, export-grade ciphers.
- Poor certificate management:
  - Self-signed certificates in production.
  - Expired certificates.
  - Hostname mismatch (CN/SAN not matching domain).
- Historical issues (examples):
  - BEAST, POODLE, CRIME, Heartbleed, etc.
- Missing HSTS or insecure renegotiation can also be risk factors.

---

## 13. Nmap OS Detection

### Q15. How does Nmap determine the Operating System of the target?

**Answer / Notes:**

- Use **`nmap -O`** or **`nmap -A`** for OS detection.
- Nmap sends crafted TCP/IP probe packets and analyzes:
  - TCP options.
  - Window size.
  - TTL values.
  - ICMP responses.
- It compares the responses to its internal **OS fingerprint database** to infer:
  - OS family and version.
  - With a confidence score.
- Firewalls, load balancers, and middleboxes can affect accuracy.

---

## 14. Pass-the-Hash vs Pass-the-Ticket

### Q16. What is the difference between Pass-the-Hash and Pass-the-Ticket?

**Answer / Notes:**

- **Pass-the-Hash (PtH):**
  - Windows stores a **hash** (scrambled version) of the user’s password.
  - Attacker steals the **NTLM hash**.
  - They reuse the hash directly to authenticate to other machines.
  - They don’t need the actual password, just the hash.

- **Pass-the-Ticket (PtT):**
  - Kerberos uses **tickets** (TGT/TGS) after authentication.
  - Attacker steals a valid **Kerberos ticket** from memory (e.g., LSASS).
  - Loads it on their own machine to impersonate the user and access services.
  - Again, no need to know the actual password, just the ticket.

---

## 15. Reflected XSS vs DOM-Based XSS

### Q17. What is the difference between Reflected XSS and DOM-based XSS? How do you mitigate them?

**Answer / Notes:**

- **Reflected XSS:**
  - User input is sent to the server and **immediately reflected** in the HTML response without proper sanitization.
  - Malicious JS payload is included in server-generated HTML.
  - **Mitigation:**
    - Output encoding of all user input before rendering.
    - Proper server-side input validation.
    - Use safe templating engines.
    - Add a **Content-Security-Policy** to reduce impact if XSS occurs.

- **DOM-Based XSS:**
  - Vulnerability exists entirely in **client-side JavaScript/DOM manipulation**.
  - Attacker-controlled data from the DOM (URL, hash, postMessage, etc.) is passed to dangerous sinks like `innerHTML` and `document.write`.
  - **Mitigation:**
    - Avoid dangerous sinks; use `.textContent` and safe APIs.
    - Treat all data from location/URL as untrusted.
    - Use robust sanitization libraries when HTML is allowed.
    - Reinforce with a strong CSP.

---

## 16. Security Headers & CSP

### Q18. What are important security headers? What is CSP and how does it mitigate XSS?

**Answer / Notes:**

Key security headers:

1. **Strict-Transport-Security (HSTS)**
   - Enforces HTTPS-only connections.
   - Example:
     ```http
     Strict-Transport-Security: max-age=31536000; includeSubDomains
     ```

2. **Content-Security-Policy (CSP)**
   - Defines which sources are allowed for scripts, images, styles, etc.
   - Acts as a **security rulebook** for the browser.
   - Primary purpose: mitigate **XSS** and similar injection attacks.
   - Example:
     ```http
     Content-Security-Policy: default-src 'self'; script-src 'self' https://trusted.cdn.com
     ```
   - This ensures:
     - Only scripts from the same site or trusted CDN can run.
     - Injected or untrusted external scripts are blocked.

3. **X-Content-Type-Options**
   - Prevents MIME type sniffing.
   - Example:
     ```http
     X-Content-Type-Options: nosniff
     ```

4. **X-Frame-Options**
   - Protects against clickjacking.
   - Examples:
     ```http
     X-Frame-Options: DENY
     X-Frame-Options: SAMEORIGIN
     ```

5. **X-XSS-Protection** (Legacy)
   - Configured old browser XSS filters.
   - Largely deprecated, CSP is preferred.
   - Example:
     ```http
     X-XSS-Protection: 1; mode=block
     ```

6. **Referrer-Policy**
   - Controls how much referrer info is sent.
   - Example:
     ```http
     Referrer-Policy: strict-origin-when-cross-origin
     ```

7. **Cache-Control**
   - Controls caching behavior, important for sensitive pages.
   - Example:
     ```http
     Cache-Control: no-store, no-cache, must-revalidate
     ```

8. **Access-Control-Allow-Origin (CORS)**
   - Defines which origins can access resources via AJAX.
   - Examples:
     ```http
     Access-Control-Allow-Origin: https://example.com
     Access-Control-Allow-Origin: *
     ```

9. **Default Security Headers Bundles**
   - Frameworks (e.g., Helmet for Node.js) often enable:
     - HSTS, CSP, X-Frame-Options, X-Content-Type-Options, Referrer-Policy, etc.

---

## 17. SAST vs DAST

### Q19. What is the difference between SAST and DAST?

**Answer / Notes:**

- **SAST (Static Application Security Testing):**
  - Analyzes **source code or binaries** without running the application.
  - Finds:
    - Hard-coded secrets.
    - Unsafe functions (e.g., raw SQL concatenation).
    - Missing input validation, insecure APIs.
  - Used early in development so devs can fix before deployment.

- **DAST (Dynamic Application Security Testing):**
  - Tests a **running application** from the outside (black-box).
  - Sends real HTTP requests:
    - Tries SQLi, XSS, path traversal, etc.
  - Simulates an attacker interacting with the live app.

---

## 18. Burp Suite – HTTPS Interception & Key Tabs

### Q20. How does Burp Suite intercept HTTPS traffic and what are its main tabs?

**Answer / Notes:**

- **Burp as MITM:**
  - Burp acts as a **man-in-the-middle proxy** between browser and server.
  - Burp generates its own **CA certificate**.
  - You install Burp’s CA in the browser trust store.
  - When you browse via Burp:
    - Burp issues a per-domain certificate signed by its CA.
    - Browser trusts it, allowing Burp to decrypt/encrypt HTTPS traffic.

**Key Tabs / Components:**
- **Dashboard** – High-level overview: issues, alerts, scan progress, activity.
- **Target** – Host list and site map; set in-scope targets.
- **Proxy** – Intercept, view, and modify HTTP(S) traffic between browser and server.
- **Intruder** – Automated attacker/fuzzer; brute force and parameter fuzzing.
- **Repeater** – Manually tweak and resend a single request; compare responses.
- **Collaborator** – Detect out-of-band (OOB) issues like blind XSS, SSRF.
- **Sequencer** – Analyze randomness of tokens (session IDs, CSRF tokens).
- **Decoder** – Encode/decode (Base64, URL, hex, JWT segments, etc.).
- **Comparer** – Diff two requests/responses to highlight differences.
- **Logger** – Detailed HTTP traffic logs for review and auditing.
- **Extensions** – Manage BApps/plug-ins to extend Burp functionality.
- **Learn** – Tutorials and labs for learning Burp and web security.

---

## 19. SQL Injection – Definition & Types

### Q21. What is SQL Injection and what are its main types?

**Answer / Notes:**

**Definition:**
- SQL Injection is a type of attack where an attacker inserts **malicious SQL commands** into input fields.
- If the backend concatenates input directly into SQL and executes it:
  - Attacker can manipulate or retrieve data without proper authorization.
  - Impact can include:
    - Spoofing user identities.
    - Gaining admin privileges.
    - Tampering/deleting data.
    - Dumping entire databases.
    - Potential OS-level access.

**Prevention:**
- Use **prepared statements / parameterized queries**.
- Avoid building SQL via string concatenation.
- Use stored procedures carefully (not as a magic fix).
- Enforce **least privilege** in database accounts.

**Types of SQL Injection:**

1. **In-Band SQL Injection (same channel):**
   - **Error-Based SQL Injection**
     - Forces DB errors that leak data (table names, columns, users).
   - **Union-Based SQL Injection**
     - Uses `UNION SELECT` to combine attacker queries with the original result.
     - Data appears in the application’s normal responses.

2. **Inferential (Blind) SQL Injection:**
   - **Boolean-Based Blind**
     - Sends conditions like `AND 1=1` vs `AND 1=2`.
     - Observes differences in content, redirects, or response behavior.
   - **Time-Based Blind**
     - Uses functions like `SLEEP()` / `WAITFOR DELAY`.
     - Slow response = condition true, fast = false.
     - Builds data bit-by-bit based on timing.

3. **Out-of-Band SQL Injection:**
   - Database triggers **external connections** (DNS/HTTP) to attacker-controlled servers.
   - Used when no error messages or timing channels are reliable.
   - Exfiltrates data via network calls.

---

## 20. CORS vs Same-Origin Policy (SOP)

### Q22. What is CORS and how does it relate to the Same-Origin Policy?

**Answer / Notes:**

- **Same-Origin Policy (SOP):**
  - Browser default security rule.
  - One origin (protocol + domain + port) **cannot read** responses from another origin.
  - Prevents websites from reading each other’s data silently.

- **CORS (Cross-Origin Resource Sharing):**
  - Server-side mechanism to **relax SOP** for specific trusted origins.
  - Server sends headers like:
    - `Access-Control-Allow-Origin`
    - `Access-Control-Allow-Credentials`
  - Tells browser: “I allow this other origin to access my resources.”

- In simple terms:
  - **SOP** = default rule: sites cannot read other sites’ data.
  - **CORS** = explicit permission granted by the server to certain other sites.

---

## 21. Authentication vs Authorization

### Q24. What is the difference between Authentication and Authorization?

**Answer / Notes:**

- **Authentication**:
  - Confirms **who** the user is.
  - Example: login with username/password, MFA, SSO.

- **Authorization**:
  - Controls **what** the authenticated user can do.
  - Example: role-based access to APIs, pages, and actions.

- Sequence:
  1. First we **authenticate** the user.
  2. Then we **authorize** what actions they can perform.

---

## 22. Path Traversal & LFI

### Q25. What is path traversal and how is it related to LFI?

**Answer / Notes:**

- **Path Traversal**:
  - Attacker uses `../` sequences in file paths to escape the intended directory.
  - Example:
    ```text
    ?file=../../../../etc/passwd
    ```
  - Goal: access arbitrary files on the server.

- **Local File Inclusion (LFI)**:
  - Application takes a filename from user input and **includes/reads** it.
  - Often combined with path traversal to include sensitive files.
  - In some cases can lead to RCE:
    - Log poisoning + file inclusion.
    - Including uploaded malicious files.

---

## 23. CSRF (Cross-Site Request Forgery)

### Q26. What is CSRF, how do you exploit it, and what are the mitigations?

**Answer / Notes:**

- **Definition:**
  - CSRF is an attack where a logged-in user’s browser is **tricked into sending an unwanted request** to a site using their existing cookies/session.
  - Example: change email, change password, transfer funds without user’s consent.

- **Exploitation:**
  - Identify a **state-changing endpoint** that:
    - Relies only on cookies for auth.
    - Has no CSRF protection (no tokens, no origin checks).
  - Create a malicious page with:
    - Auto-submitting form or crafted image/script.
  - When the victim (logged in) visits the page:
    - Browser sends the forged request with valid cookies.
    - The action executes as if the user requested it.

- **Mitigations:**
  - Use **CSRF tokens** (synchronizer tokens) for state-changing operations.
  - Enable **SameSite** cookies where possible.
  - Validate **Origin** and **Referer** headers on sensitive endpoints.
  - Avoid using **GET** for state-changing actions (prefer POST/PUT).
  - Utilize **framework-built CSRF protection** features.

---

# 27. OWASP & OWASP Top 10:2025

### Q27. Heard of OWASP? What is it? Name some vulnerabilities from OWASP Top 10 2025.

**Answer / Notes:**

- **OWASP (Open Web Application Security Project)** is a non-profit foundation focused on improving software security.
  - They publish free standards, tools, and guides like OWASP Top 10, ASVS, SAMM.

- **OWASP Top 10:2025** (examples of categories you can mention):
  - **Broken Access Control**
  - **Security Misconfiguration**
  - **Software Supply Chain Failures**
  - **Cryptographic Failures**
  - **Injection**
  - **Insecure Design**
  - **Authentication Failures**
  - **Software or Data Integrity Failures**
  - **Logging & Alerting Failures**
  - **Mishandling of Exceptional Conditions**

**Example (interview):**  
“OWASP is a global non-profit that creates free security standards and tools. Their best-known project is the OWASP Top 10, which summarizes the most critical web application risks such as Injection, Broken Access Control, Security Misconfiguration, Insecure Design, and others that reflect modern AppSec issues.”

---

## 28. VA vs Pentest vs Red Team

### Q28. What is Vulnerability Assessment, Penetration Testing, and Red Teaming? Differences?

**Answer / Notes:**

- **Vulnerability Assessment (VA)**  
  - **Breadth-focused**, mainly automated scanning and manual validation.
  - Goal: **identify, classify, and prioritize** vulnerabilities.
  - Usually limited exploitation; outcome is a vulnerability list with severities.

- **Penetration Testing**
  - **Depth + exploitation**.
  - Simulates an attacker within a defined scope.
  - Proves impact via exploitation and limited post-exploitation.

- **Red Teaming**
  - **Full-scope adversary simulation**.
  - Tests **people, processes, and technology**.
  - Often multi-week/month, stealthy, blue team may not be aware.
  - Aims to see how well detection and response work in practice.

**Example:**  
“If a company wants a list of weaknesses, I’d recommend a vulnerability assessment. If they want to know if someone can actually break in and what they can do, we do a penetration test. If they want to test their entire security posture including SOC detection and response, that’s a red team exercise.”

---

## 29. Brute Forcing Protection

### Q29. How do you handle brute forcing on your application?

**Answer / Notes:**

Controls to mention:

- **Rate limiting / throttling**
  - Limit login attempts per IP / per account.
  - Add delays or temporary blocks after repeated failures.

- **Account lockout or step-up verification**
  - Temporary lock account, or require CAPTCHA / OTP after X failures.

- **MFA (Multi-Factor Authentication)**
  - Even if password is guessed, attacker needs a second factor.

- **Strong password policy & password blacklist**
  - Enforce length, complexity, and block known breached passwords.

- **Monitoring & alerting**
  - Detect abnormal login failures or IP patterns and alert SOC.

- **IP reputation / geo rules**
  - Block or challenge suspicious or high-risk IPs.

**Example:**  
“For login, I combine rate limiting with CAPTCHAs and lockouts after repeated failures, enforce MFA for high-privilege accounts, and monitor login failure patterns to detect credential stuffing.”

---

## 30. Stateful vs Stateless & HTTP State

### Q30. What is stateful and stateless in HTTP context? How does HTTP handle state?

**Answer / Notes:**

- **HTTP is stateless by design**
  - Each request is independent; server doesn’t remember prior requests.

- **Stateful behavior is implemented on top of HTTP** using:
  - **Cookies** (session IDs).
  - **Server-side session stores** (session ID maps to user state).
  - **Tokens** (JWT/access tokens) passed with each request.

- **Stateless design** (REST-style):
  - Server does not keep per-user session.
  - Each request carries all necessary context (e.g., JWT with claims).
  - Easier to scale horizontally (any node can handle any request).

**Example:**  
“HTTP itself is stateless. To remember users, we issue a session cookie after login and store their session server-side. Alternatively, we use stateless JWT tokens where all info is inside the token and validated on each request.”

---

## 31. Hardest XSS to Detect

### Q31. Which of the XSS attacks are hardest to detect and why?

**Answer / Notes:**

- **DOM-based XSS** is generally hardest to detect because:
  - The payload may never reach the server; it is processed entirely in the **browser’s JavaScript**.
  - Server logs and traditional scanners may see a perfectly normal HTTP response.
  - Vulnerabilities live in complex client-side code, front-end frameworks, and dynamic DOM manipulation.

**Example:**  
“Stored and reflected XSS often show up in server responses and logs, so scanners and testers find them faster. DOM-based XSS hides in client-side JS, making it much harder to spot without dedicated client-side analysis and manual testing.”

---

## 32. Whitelisting vs Blacklisting

### Q32. Do you prefer blacklisting or whitelisting? Why?

**Answer / Notes:**

- **Blacklisting** (denylist)
  - Block known bad patterns (e.g., `<script>`, `DROP TABLE`).
  - Easy to bypass with encoding and new payload variations.

- **Whitelisting** (allowlist)
  - Define exactly what is allowed (e.g., numbers only, strict regex for email).
  - Stronger security posture because anything unexpected is rejected.

**Preferred:**  
- **Whitelisting for input validation** whenever possible.
- Blacklists can be used as **additional layers**, but not the sole defense.

**Example:**  
“For a phone number field, I allow only digits and maybe `+`. If I try to block only bad patterns, attackers can always find a new encoding that bypasses my blacklist.”

---

## 33. CSRF Investigation

### Q33. When investigating a CSRF attack, what are the things you look for?

**Answer / Notes:**

Key things to examine:

- **Endpoint nature**
  - Is it state-changing (money transfer, profile update, password change)?

- **Presence of CSRF protections**
  - CSRF token in form/body/header.
  - Server-side validation of that token.

- **HTTP method**
  - Are sensitive operations using GET (bad) or POST/PUT/DELETE?
  - Are they idempotent or not?

- **Cookie configuration**
  - `SameSite` attribute.
  - `Secure` and `HttpOnly` flags.

- **Origin & Referer headers**
  - Do requests from attack PoC show a foreign origin?
  - Does the server verify them?

- **Exploit PoC**
  - A simple HTML/JS PoC demonstrating that an action can be triggered without user intent.

**Example:**  
“I’ll replicate the reported issue using a malicious HTML page, observe whether the request includes any CSRF token and whether the server validates origin/referrer. If the action succeeds without any of these checks, it’s a confirmed CSRF vulnerability.”

---

## 34. CSRF with PUT

### Q34. Can you perform a CSRF attack if the HTTP method is PUT, considering there is no CSRF prevention? Explain.

**Answer / Notes:**

- **Yes.** CSRF is about the browser sending an authenticated request, not about the method itself.
- If:
  - Browser can send a **PUT** request (e.g., via XHR/fetch or misconfigured CORS).
  - The application uses cookies for auth and has **no CSRF token / SameSite / origin checks**.
- Then a malicious website can trick a logged-in browser into sending a PUT request that changes state.

**Nuance:**  
- HTML forms natively support only GET/POST, but JavaScript (XHR/fetch) can send PUT/DELETE when allowed by CORS or same-origin.

**Example:**  
“If `/user/email` is a PUT endpoint and relies only on a session cookie, a malicious page can send a cross-site PUT request (if CORS is misconfigured) and change the user’s email without any CSRF token. That’s still a CSRF vulnerability.”

---

## 35. Identifying Web Server Type

### Q35. How do you determine if the website is hosted on IIS, Apache, Nginx, etc.?

**Answer / Notes:**

Approaches:

- **HTTP Response Headers**
  - Check the `Server:` header (if not masked):
    - `Server: nginx`
    - `Server: Apache/2.4.57`
    - `Server: Microsoft-IIS/10.0`

- **Error / Default pages**
  - Default 404/500 pages are often recognizable (e.g., IIS style error page).

- **Fingerprinting tools**
  - Use **Nmap with `-sV`**.
  - Tools like **WhatWeb**, **Wappalyzer**.

- **Behavior**
  - Some subtle behaviors (header order, TLS extensions) can hint server type (used by advanced tools).

**Example:**  
“I first check the `Server` header, then confirm using Nmap service detection or WhatWeb. If headers are hidden, I look at error pages and behavior to fingerprint the stack.”

---

## 36. Prepared Statements & Parameterized Queries

### Q36. What are prepared statements and parameterized queries (in context of SQLi)?

**Answer / Notes:**

- **Parameterized query / prepared statement:**
  - SQL query with a **fixed structure**.
  - User inputs are passed as **parameters**, never concatenated into the SQL string.

**Bad example (vulnerable):**
```sql
query = "SELECT * FROM users WHERE username = '" + userInput + "'";

**Good example (vulnerable):**
query = "SELECT * FROM users WHERE username = ?";
stmt  = conn.prepareStatement(query);
stmt.setString(1, userInput);


