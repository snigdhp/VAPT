
**Hijack_Session**                                                                                    
**Concept**
Application developers who develop their own session IDs frequently forget to incorporate the complexity and randomness necessary for security. If the user specific session ID is not complex and random, then the application is highly susceptible to session-based brute force attacks.

**Goals**
Gain access to an authenticated session belonging to someone else.0

in this lesson we are trying to predict the 'hijack cookie' value. The 'hijack cookie' is used to differentiate authenticated and anonymous users of WebGoat.

- Log in to the OWASP Goat Web application and select Lab-1: Hijack Session.

![alt text](<../image/Lab-1 Hijack_Session.md/image-8.png>)

- You will see a login form with Username and Password text fields. Now, intercept this request using Burp Suite

![alt text](<../image/Lab-1 Hijack_Session.md/image.png>)


- Now send this request to Repeater and remove hijack session cookie from Request and send it again to generate new session cookie

![alt text](<../image/Lab-1 Hijack_Session.md/image-1.png>)

- In Repeater click on send button 2 times and generate the multiple session means double hijack  cookie to check the pattern and we found that there is 2 number of gap of session!

![alt text](<../image/Lab-1 Hijack_Session.md/image-2.png>)
![alt text](<../image/Lab-1 Hijack_Session.md/image-3.png>)

- Now copy the new session cookie and paste it on Request body and sent this request to intruder 

![alt text](<../image/Lab-1 Hijack_Session.md/image-4.png>)

- Now, modify the Intruder request by targeting the session cookie and timestamp parameters.
- Set the payload type to Number, and define the payload range from 6244 to 9080, because the original payload is: 1209030689935531689-175416434§6244§. And Click on Start to do the brute force attack

![alt text](<../image/Lab-1 Hijack_Session.md/image-5.png>)
![alt text](<../image/Lab-1 Hijack_Session.md/image-6.png>)
![alt text](<../image/Lab-1 Hijack_Session.md/image-7.png>)






