# OWASP & API Security Overview

## About OWASP

**OWASP (Open Worldwide Application Security Project)** is a nonprofit foundation created to improve application security.  
The OWASP Foundation was launched on **December 1, 2001** and is best known for:

- OWASP Top Ten lists
- Open-source security tools
- Community-driven security projects

OWASP has become a global authority for application security awareness and best practices.

---

## OWASP API Security Top 10

The **OWASP API Security Top 10** identifies the most critical security risks affecting **Application Programming Interfaces (APIs)**.

- **Project Founders:** Erez Yalon, Inon Shkedy  
- **First Release:** December 2019  
- **Latest Version:** OWASP API Security Top 10 – 2023  

The project was initiated in response to the rapid adoption of APIs, evolving attack techniques, and gaps in existing security controls.

---

## Key Drivers Behind the OWASP API Security Top 10

### 1. The Rapid Rise of APIs

APIs power the exchange of one of the world’s most valuable assets: **data**.

Modern businesses no longer need to develop every feature in-house. Instead, they rely on APIs to consume services such as:

- Mapping and GPS
- Payment processing
- Authentication and authorization
- Messaging and communication

Web APIs provided a standardized way to share data across different programming languages and platforms. This dramatically accelerated innovation and adoption, making APIs a **core business enabler** worldwide.

---

### 2. A Major Gap in Security

Traditional security tools were not designed to detect **API-specific vulnerabilities**.

Legacy solutions such as:
- Web application scanners
- Network security monitoring tools
- Enterprise vulnerability management systems  

struggled with API behaviors like JSON payloads, business logic abuse, and authorization flaws. As a result, many organizations were unprepared to defend against API-based attacks, leading to widespread data breaches.

---

### 3. A New Leading Attack Vector

As with many rapidly adopted technologies, **security often lagged behind implementation**.

Public, Internet-facing APIs frequently bypassed existing security controls. Attackers no longer needed to follow the traditional MITRE cyber kill chain. Instead, they could:

- Directly interact with insecure APIs
- Access sensitive business logic
- Exfiltrate data without breaching the internal network

This shift established APIs as a **primary attack surface**.

---

## Purpose of the OWASP API Security Project

In response to:
- Massive API adoption
- Security gaps in API implementations
- A surge in API-related security incidents  

OWASP published the **API Security Top 10** to provide:

- Practical security guidelines
- Industry best practices
- Defensive techniques and tools  

The project is now a widely trusted resource for security professionals and has significantly increased awareness of API security risks.

---

## Notable API Security Incidents (Last 5 Years)

Some of the most high-profile API-related incidents include:

- **2018** – USPS Data Leak  
- **2019** – Venmo Public API Scraping  
- **2021** – Peloton API Data Leak  
- **2021** – Parler API Data Leak  
- **2021** – LinkedIn API Data Leak  
- **2022** – Coinbase Authorization Flaw  
- **2022** – Optus API Data Breach  
- **2022** – Toyota API Exposure  
- **2023** – EatonWorks Toyota Research Disclosure  
- **2023** – T-Mobile API Data Exposure  

These incidents highlight the real-world impact of insecure APIs.

---

## Mapping OWASP API Risks to External Standards

OWASP API Security risks are mapped to **external security standards and references**, including:

- **Common Weakness Enumeration (CWE)** by MITRE
- Other OWASP projects
- **NIST** security guidelines

CWEs provide a standardized way to identify and classify vulnerabilities using unique **CWE-IDs**.

---

## OWASP API Security Top 10 – 2023 Mapping

### API1:2023 – Broken Object Level Authorization (BOLA)
- CWE-285: Improper Authorization  
- CWE-639: Authorization Bypass Through User-Controlled Key  

---

### API2:2023 – Broken Authentication
- CWE-204: Observable Response Discrepancy  
- CWE-307: Improper Restriction of Excessive Authentication Attempts  

---

### API3:2023 – Broken Object Property Level Authorization
- CWE-213: Exposure of Sensitive Information Due to Incompatible Policies  
- CWE-915: Improperly Controlled Modification of Dynamically-Determined Object Attributes  
- API3:2019 – Excessive Data Exposure  
- API6:2019 – Mass Assignment  

---

### API4:2023 – Unrestricted Resource Consumption
- CWE-770: Allocation of Resources Without Limits or Throttling  
- CWE-400: Uncontrolled Resource Consumption  
- CWE-799: Improper Control of Interaction Frequency  
- NIST: Security Strategies for Microservices-based Application Systems  

---

### API5:2023 – Broken Function Level Authorization
- CWE-285: Improper Authorization  
- OWASP Top 10 2013 – A7: Missing Function Level Access Control  
- OWASP Guidance: Forced Browsing  
- OWASP Guidance: Access Control  

---

### API6:2023 – Unrestricted Access to Sensitive Business Flows
- API10:2019 – Insufficient Logging & Monitoring  
- OWASP Automated Threats to Web Applications  

---

### API7:2023 – Server-Side Request Forgery (SSRF)
- CWE-918: Server-Side Request Forgery  
- URL Confusion Vulnerabilities (Snyk)  
- OWASP SSRF Prevention Cheat Sheet  

---

### API8:2023 – Security Misconfiguration
- CWE-2: Environmental Security Flaws  
- CWE-16: Configuration  
- CWE-209: Error Message Information Leak  
- CWE-319: Cleartext Transmission of Sensitive Information  
- CWE-388: Error Handling  
- CWE-444: HTTP Request Smuggling  
- CWE-942: Permissive Cross-Domain Policy  
- NIST Guide to General Server Security  
- OWASP Secure Headers Project  

---

### API9:2023 – Improper Inventory Management
- CWE-1059: Incomplete Documentation  

---

### API10:2023 – Unsafe Consumption of APIs
- CWE-285: Improper Authorization  
- CWE-639: Authorization Bypass Through User-Controlled Key  

---
