## Question 1
**Which of the following is NOT a recommended preventative measure for limiting resource consumption in APIs?**

- Implement server-side validation for query string and request body parameters.
- Notify the consumer when the limit is exceeded, providing the limit number and the time at which the limit will be reset.
- **Allow an unlimited number of elements in request arrays.** *(Correct answer.)*
- Limit how often a consumer can call the API within a defined timeframe.

---

## Question 2
**Which of the following best describes the threat associated with the lack of rate limiting?**

- The API allows unauthorized access to sensitive data.
- **The API allows uncontrolled interactions or resource consumption which can lead to Denial of Service (DoS) or increased financial costs.** *(Correct answer.)*
- The API responds with improper HTTP headers.
- The API exposes unnecessary data in its response.

---

## Question 3
**Why is rate limiting important for the monetization and availability of APIs?**

- Rate limiting allows API providers to control the flow of their data.
- **Rate limiting prevents unauthorized access to the API.** *(Correct answer.)*
- Rate limiting secures data transfer between the consumer and the API provider.
- Rate limiting allows for secure storage of data in the API's database.

---

## Question 4
**In regards to API rate limiting, what is indicated by an HTTP 429 response status code?**

- The consumer is not authorized to make the request.
- The consumer has requested too many resources.
- The consumer has requested unprocessable content.
- **The consumer has made too many requests.** *(Correct answer.)*

---

## Question 5
**According to OWASP, what is the primary consequence of not implementing API rate limiting?**

- Unauthorized access to data.
- Consumers will be able to automate requests to business flows and create spam.
- **DoS due to resource starvation or a negative impact to the service provider's billing.** *(Correct answer.)*
- Data leakage due to insecure data transfer methods.
