**Insecure Direct Object References**
Direct Object References
Direct Object References are when an application uses client-provided input to access data & objects.

Examples
Examples of Direct Object References using the GET method may look something like

https://some.company.tld/dor?id=12345

https://some.company.tld/images?img=12345

https://some.company.tld/dor/12345

Other Methods
POST, PUT, DELETE or other methods are also potentially susceptible and mainly only differ in the method and the potential payload.

Insecure Direct Object References
These are considered insecure when the reference is not properly handled and allows for authorization bypasses or disclose private data that could be used to perform operations or access data that the user should not be able to perform or access. Let’s say that as a user, you go to view your profile and the URL looks something like:

https://some.company.tld/app/user/23398

... and you can view your profile there. What happens if you navigate to:

https://some.company.tld/app/user/23399 …​ or use another number at the end. If you can manipulate the number (user id) and view another’s profile, then the object reference is insecure. This of course can be checked or expanded beyond GET methods to view data, but to also manipulate data.

More good reading
Before we go on to practice, here’s some good reading on Insecure Direct Object References:

https://www.owasp.org/index.php/Testing_for_Insecure_Direct_Object_References_(OTG-AUTHZ-004)

https://www.owasp.org/index.php/Top_10-2017_A5-Broken_Access_Control

https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html

https://www.owasp.org/index.php/Top_10_2013-A4-Insecure_Direct_Object_References

http://cwe.mitre.org/data/definitions/639.html


---------------------------------------------------------------------------------------------
Authenticate First, Abuse Authorization Later
Many access control issues are susceptible to attack from an authenticated-but-unauthorized user. So, let’s start by legitimately authenticating. Then, we will look for ways to bypass or abuse Authorization.

The id and password for the account in this case are 'tom' and 'cat' (It is an insecure app, right?).

After authenticating, proceed to the next screen.

- To start the assignment login to the account by given username and password as tom and cat Respective 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image.png>)

---------------------------------------------------------------------------------------------
Observing Differences & Behaviors
A consistent principle from the offensive side of AppSec is to view differences from the raw response to what is visible. In other words (as you may have already noted in the client-side filtering lesson), there is often data in the raw response that doesn’t show up on the screen/page. View the profile below and take note of the differences.

- to Perform this lab intercept this request to Burpsuite and check the server response, and find the value that don’t show above in the profile.
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-1.png>)

- Once the incercept the request send the request body to repeater and click on send button and check the response 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-2.png>)

- We found that in the server response UserId,role is missing, and then click on submit difference button to check answer 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-3.png>) 

---------------------------------------------------------------------------------------------

Guessing & Predicting Patterns
View Your Own Profile Another Way
The application we are working with seems to follow a RESTful pattern so far as the profile goes. Many apps have roles in which an elevated user may access content of another. In that case, just /profile won’t work since the own user’s session/authentication data won’t tell us whose profile they want view. So, what do you think is a likely pattern to view your own profile explicitly using a direct object reference?

- Now we have to have to guess and find the profile to get the profile data as we know in the previous lab we intercept the request we got something in server response profile details 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-4.png>) 

- So we use same profile details to get and manipulate the user details 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-5.png>)

---------------------------------------------------------------------------------------------

Playing with the Patterns
View Another Profile
View someone else’s profile by using the alternate path you already used to view your own profile. Use the 'View Profile' button and intercept/modify the request to view another profile. Alternatively, you may also just be able to use a manual GET request with your browser.

- Here we have to click on view profile button and intercept this request and send to intruder 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-6.png>)

- After getting the request and we have to provide payload position on userid and start brute force attack to using attack type as Number and change the numbers 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-7.png>)

- Hence we got the profile and we are able to access different profile 
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-8.png>)
![alt text](<../image/Lab-2 Insecure Direct Object References.md/image-9.png>)



