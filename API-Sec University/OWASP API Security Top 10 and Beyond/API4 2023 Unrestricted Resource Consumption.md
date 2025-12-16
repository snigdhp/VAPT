# API4:2023 — Unrestricted Resource Consumption

## Intro
**API4:2023 Unrestricted Resource Consumption** is an API issue where the provider does not have safeguards in place to prevent excessive use of their API. When there are no restrictions for resource consumption, the API provider could become a victim of **Denial of Service (DoS)** attacks or experience unnecessary financial costs.

This is an updated version of **API4:2019 Lack of Resources and Rate Limiting**.

---

## OWASP Attack Vector Description
Exploitation requires simple API requests. Multiple concurrent requests can be performed from a single local computer or by using cloud computing resources. Most automated tools available are designed to cause DoS via high loads of traffic, impacting APIs’ service rate.

---

## OWASP Security Weakness Description
It's common to find APIs that do not limit client interactions or resource consumption. Crafted API requests (such as including parameters that control the number of resources to be returned) and performing response status/time/length analysis should allow identification of the issue. The same is valid for batched operations.

Although threat agents don't have visibility over cost impact, this can be inferred based on service providers’ (e.g., cloud provider) business/pricing model.

---

## OWASP Impacts Description
Exploitation can lead to DoS due to resource starvation, but it can also lead to operational cost increases such as:
- Higher CPU demand
- Increased cloud storage needs
- Other infrastructure scaling costs

---

## When an API is Vulnerable (OWASP Criteria)
An API is vulnerable if at least one of the following limits is missing or set inappropriately (e.g., too low/high):

- Execution timeouts
- Maximum allocable memory
- Maximum number of file descriptors
- Maximum number of processes
- Maximum upload file size
- Number of operations to perform in a single API client request (e.g., GraphQL batching)
- Number of records per page to return in a single request-response
- Third-party service providers' spending limit

---

## Summary
Every API request has a technical and financial cost. When API providers do not enforce limitations on resource consumption, there is an increased risk of:
- Denial of Service (DoS)
- Distributed Denial of Service (DDoS)
- Unnecessary financial costs
- Degraded quality of service for other users

Rate limiting also plays an important role in the **monetization and availability** of APIs. Many API providers monetize their APIs by limiting requests and allowing paid customers to request more information.

Some API providers have infrastructure that automatically scales with the number of requests. In these cases, an unlimited number of requests can lead to a significant and easily preventable increase in infrastructure costs.

---

## OWASP Preventative Measures
- Docker makes it easy to limit memory, CPU, number of restarts, file descriptors, and processes.
- Implement a limit on how often a client can call the API within a defined timeframe.
- Notify the client when the limit is exceeded by providing the limit number and the time at which the limit will be reset.
- Add proper server-side validation for query string and request body parameters, specifically the ones that control the number of records to be returned in the response.
- Define and enforce maximum size of data on all incoming parameters and payloads such as maximum length for strings and maximum number of elements in arrays.

---
## Impacts Description (Additional)

- Exploitation can lead to **Denial of Service (DoS)**.
- **Economic impact** due to higher infrastructure demands.

---
## Additional Resources
- "Availability" — Web Service Security Cheat Sheet
- "DoS Prevention" — GraphQL Cheat Sheet
- "Mitigating Batching Attacks" — GraphQL Cheat Sheet
- CWE-770: Allocation of Resources Without Limits or Throttling
- CWE-400: Uncontrolled Resource Consumption
- CWE-799: Improper Control of Interaction Frequency
- "Rate Limiting (Throttling)" — Security Strategies for Microservices-based Application Systems, NIST
