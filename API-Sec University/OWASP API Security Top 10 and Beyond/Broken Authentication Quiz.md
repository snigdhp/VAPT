## Question 1
**Which of the following accurately describes "Broken Authentication" in APIs?**

- API authentication does not allow for multi-factor authentication.
- API authentication only allows for a single method of token generation.
- **API authentication is any weakness within the API authentication process.** *(Correct answer.)*
- API authentication does not require a unique token for user registration.

---

## Question 2
**According to the OWASP, which of the following is NOT considered a direct contributing factor to Broken Authentication in APIs?**

- Lack of additional protection mechanisms for API endpoints handling authentication. 
- Misuse or incorrect implementation of the authentication mechanism.
- **Excessive data exposure through the API**. *(Correct answer.)*
- Implementing an authentication mechanism without considering attack vectors or the appropriate use case.

---

## Question 3
**What can be the potential impact of Broken Authentication in APIs?**

- Attackers can view the source code of the web application.
- **Attackers can gain control of other users' accounts, read their personal data, and perform sensitive actions on their behalf.** *(Correct answer.)*
- Attackers can cause a Denial of Service (DoS) attack.
- Attackers can alter the algorithm used for token generation.

---

## Question 4
**What does a "Predictable Token" refer to in the context of API security?**

- A token that is only valid for a predictable amount of time.
- A token that is reused for multiple users.
- A token that contains sensitive user information.
- **A token obtained through a weak token generation process that can easily be guessed, deduced, or calculated by an attacker.** *(Correct answer.)*

---

## Question 5
**Which of the following is NOT recommended by the OWASP API Security project as a preventative measure against Broken Authentication?**

- Implement an account lockout/captcha mechanisms to prevent brute force attacks.
- Make sure you understand how all possible authentication flows work.
- **Use API keys for user authentication as well as client authentication.** *(Correct answer.)*
- Treat credential recovery/forgot password endpoints with the same protections as login endpoints.
