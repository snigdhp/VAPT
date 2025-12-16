# OWASP API Security Top 10 – Evolution (2019 → 2023)

## Why the OWASP API Security Top 10 Was Updated

Since the release of the **OWASP API Security Top 10 in 2019**, API usage has grown exponentially. Alongside this growth:

- API-related data breaches have continued
- New API technologies and architectures have emerged
- APIs have become a primary attack surface

These trends created a strong need for an **updated and relevant Top 10 list**.

### Rising API Attacks & Market Growth

- API attacks have been **consistently increasing**
- Akamai reported **nearly 114 million API attacks in a single day (2021)**
- The global API market was valued at **$2.2 billion in 2021**
- Market size is projected to reach **$41.5 billion by 2031** (20× growth in 10 years)
- In 2022:
  - **Postman** had over **46 million collections**
  - **GitHub** hosted **3 million API-related repositories**

APIs continue to be rapidly adopted, and the **financial and security stakes continue to rise**.

---

## OWASP API Security Top 10 – 2023 Update

To address evolving attack patterns, the OWASP API Security Project released an updated Top 10 list in 2023.

**Inon Shkedy**, OWASP API Security Project Leader, stated:

> *“The OWASP API Top 10 – 2023 version is different from the 2019 version.  
> We aspire to follow the security trends that are relevant to APIs and have been developed in recent years.  
> If you try to hack or protect an API that was developed five years ago (2018), it would make more sense to refer to the 2019 list.”*

---

## OWASP API Security Top 10 – Comparison (2019 vs 2023)

### OWASP API Security Top 10 – 2019

1. **API1:2019** – Broken Object Level Authorization  
2. **API2:2019** – Broken User Authentication  
3. **API3:2019** – Excessive Data Exposure  
4. **API4:2019** – Lack of Resources & Rate Limiting  
5. **API5:2019** – Broken Function Level Authorization  
6. **API6:2019** – Mass Assignment  
7. **API7:2019** – Security Misconfiguration  
8. **API8:2019** – Injection  
9. **API9:2019** – Improper Assets Management  
10. **API10:2019** – Insufficient Logging & Monitoring  

---

### OWASP API Security Top 10 – 2023

1. **API1:2023** – Broken Object Level Authorization  
2. **API2:2023** – Broken Authentication  
3. **API3:2023** – Broken Object Property Level Authorization **(NEW)**  
4. **API4:2023** – Unrestricted Resource Consumption **(NEW)**  
5. **API5:2023** – Broken Function Level Authorization  
6. **API6:2023** – Unrestricted Access to Sensitive Business Flows **(NEW)**  
7. **API7:2023** – Server-Side Request Forgery (SSRF) **(NEW)**  
8. **API8:2023** – Security Misconfiguration  
9. **API9:2023** – Improper Inventory Management  
10. **API10:2023** – Unsafe Consumption of APIs **(NEW)**  

---

## Key Changes Summary

### Newly Introduced in 2023
- Broken Object Property Level Authorization
- Unrestricted Resource Consumption
- Unrestricted Access to Sensitive Business Flows
- Server-Side Request Forgery (SSRF)
- Unsafe Consumption of APIs

### Renamed / Refined
- Broken User Authentication → **Broken Authentication**
- Improper Assets Management → **Improper Inventory Management**

### Removed from 2023
- **Injection**
- **Insufficient Logging & Monitoring** (now treated as a cross-cutting control)

---

## Takeaway

- **2019 list** is more relevant for **legacy APIs**
- **2023 list** reflects **modern API architectures, business logic abuse, and supply-chain risks**
- API security has shifted from **technical flaws** to **authorization, business logic, and consumption risks**

---

# Risk Rating

Each **OWASP API Security risk category** is paired with a **risk rating**.  
These ratings are based on the **OWASP Risk Rating Methodology** (now referenced as the **OWASP Risk Rating Framework**).

The risk rating helps assess:
- How likely a vulnerability is to be exploited
- How severe the technical impact may be
- How common and detectable the weakness is

---

## OWASP API Security Risk Rating Factors

The following table summarizes the **risk factors** used by the OWASP API Security Project.

| Factor | Rating | Description |
|------|--------|-------------|
| **Threat Agents** | API-Specific | Focuses on attackers targeting APIs |
| **Exploitability** | 3 | Easy |
|  | 2 | Average |
|  | 1 | Difficult |
| **Weakness Prevalence** | 3 | Widespread |
|  | 2 | Common |
|  | 1 | Difficult |
| **Weakness Detectability** | 3 | Easy |
|  | 2 | Average |
|  | 1 | Difficult |
| **Technical Impact** | 3 | Severe |
|  | 2 | Moderate |
|  | 1 | Minor |
| **Business Impact** | Business-Specific | Determined by the organization |

---

## Risk Rating Interpretation

- **Higher scores (3)** indicate greater risk due to ease of exploitation, widespread occurrence, or severe impact.
- **Lower scores (1)** indicate reduced risk due to difficulty, rarity, or limited impact.
- **Business impact is not predefined** and must be evaluated by each organization individually.

---

## Important Clarification

The OWASP API Security Top 10 **does not perform a full risk analysis** for individual organizations.

As stated by the OWASP API Security Project team:

> *“The purpose of the OWASP API Security Top 10 is not to do this risk analysis for you.”*

Instead, the Top 10 provides:
- A **guideline** for identifying API security risks
- A **framework** to help organizations evaluate risk factors
- A **starting point** for performing organization-specific risk assessments

---

## Key Takeaway

- OWASP provides **risk categories and scoring guidance**
- Each organization must:
  - Evaluate **actual business impact**
  - Determine **final risk scores**
  - Apply controls based on its own threat model

---

# OWASP API Security Risk Scores

This section presents the **risk scoring comparison** for the OWASP API Security Top 10 in **2019** and **2023**, based on exploitability, prevalence, detectability, and technical impact.

---

## OWASP API Security Top 10 – 2019 Risk Scores

| Risk | Exploitability | Prevalence | Detectability | Technical Impact | Overall Score |
|-----|---------------|------------|---------------|------------------|---------------|
| API1:2019 – Broken Object Level Authorization | 3 | 3 | 2 | 3 | **11** |
| API2:2019 – Broken User Authentication | 3 | 2 | 2 | 3 | **10** |
| API3:2019 – Excessive Data Exposure | 3 | 2 | 2 | 2 | **9** |
| API4:2019 – Lack of Resources & Rate Limiting | 2 | 3 | 3 | 2 | **10** |
| API5:2019 – Broken Function Level Authorization | 3 | 2 | 1 | 2 | **8** |
| API6:2019 – Mass Assignment | 2 | 2 | 2 | 2 | **8** |
| API7:2019 – Security Misconfiguration | 3 | 3 | 3 | 2 | **11** |
| API8:2019 – Injection | 3 | 2 | 3 | 3 | **11** |
| API9:2019 – Improper Assets Management | 3 | 3 | 2 | 2 | **10** |
| API10:2019 – Insufficient Logging & Monitoring | 2 | 3 | 1 | 2 | **8** |

---

## OWASP API Security Top 10 – 2023 Risk Scores

| Risk | Exploitability | Prevalence | Detectability | Technical Impact | Overall Score |
|-----|---------------|------------|---------------|------------------|---------------|
| API1:2023 – Broken Object Level Authorization | 3 | 3 | 3 | 2 | **11** |
| API2:2023 – Broken Authentication | 3 | 2 | 3 | 3 | **11** |
| API3:2023 – Broken Object Property Level Authorization | 3 | 2 | 3 | 2 | **10** |
| API4:2023 – Unrestricted Resource Consumption | 2 | 3 | 3 | 3 | **11** |
| API5:2023 – Broken Function Level Authorization | 3 | 2 | 3 | 3 | **11** |
| API6:2023 – Unrestricted Access to Sensitive Business Flows | 3 | 3 | 2 | 2 | **10** |
| API7:2023 – Server-Side Request Forgery (SSRF) | 3 | 2 | 3 | 2 | **10** |
| API8:2023 – Security Misconfiguration | 3 | 3 | 3 | 3 | **12** |
| API9:2023 – Improper Inventory Management | 3 | 3 | 2 | 2 | **10** |
| API10:2023 – Unsafe Consumption of APIs | 3 | 2 | 2 | 3 | **10** |

---

## Key Observations

- **Security Misconfiguration (API8:2023)** has the highest overall score (**12**), indicating broad prevalence and severe impact.
- Authorization-related risks (**BOLA, BFLA**) remain consistently high across both versions.
- New 2023 risks focus more on **business logic abuse**, **API consumption risks**, and **supply-chain exposure**.
- Detectability scores increased in 2023, reflecting better tooling but **higher attacker sophistication**.

---

## Takeaway

- **2019 scores** reflect traditional API implementation flaws.
- **2023 scores** emphasize modern API ecosystems, microservices, and third-party integrations.
- Organizations must still calculate **business impact separately** based on their environment.

---

