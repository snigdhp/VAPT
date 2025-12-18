## BFLA – Knowledge Check (OWASP API Security)

---

### Question 1  
**According to the OWASP API Security Project, which of the following is NOT a recommended preventative measure for Broken Function Level Authorization?**

- Implement a consistent and easy-to-analyze authorization module invoked from all your business functions.
- **Make sure that all administrative functions inside a regular controller do not implement authorization checks based on the user's group and role.** ✅ *Correct Answer*
- Ensure that the enforcement mechanism(s) deny all access by default, requiring explicit grants to specific roles for access to every function.
- Review API endpoints against function-level authorization flaws, considering business logic and group hierarchy.

---

### Question 2  
**When testing for BFLA vulnerabilities, what functionality should you look for that could be exploited?**

- Functionality that allows a user to make an unlimited number of requests to the API.
- **Functionality that allows a user to add themselves to any user group.** ✅ *Correct Answer*
- Functionality that allows a user to change their own username or password.
- All of the above.

---

### Question 3  
**What is the primary impact of exploiting a Broken Function Level Authorization vulnerability according to OWASP?**

- An attacker could execute a Denial of Service (DoS) attack.
- An attacker could escalate their privileges to domain admin.
- **An attacker could access unauthorized functionality, with administrative functions being key targets.** ✅ *Correct Answer*
- An attacker could inject malicious scripts into the API.

---

### Question 4  
**According to OWASP, what makes implementing proper authorization checks challenging in modern applications?**

- APIs are structured and predictable.
- There are very few tools available to perform authorization checks.
- **Modern applications have complex user hierarchies and many types of roles or groups.** ✅ *Correct Answer*
- There is a high cost associated with implementing proper authorization checks.

---

### Question 5  
**What is the primary threat associated with Broken Function Level Authorization in API Security?**

- An attacker could manipulate or delete their own data.
- The API could accidentally leak data in a response.
- **An attacker could gain unauthorized access to endpoints they should not have access to.** ✅ *Correct Answer*
- The server could be overwhelmed by too many requests.

---

### Key Takeaway

Broken Function Level Authorization primarily enables **unauthorized access to protected functionality**, often leading to **privilege escalation** and **administrative abuse**.
