When a valid authentication cookie is received, the system will automatically log in the user.

If a cookie is not sent, but the provided credentials are correct, the system will generate an authentication cookie.

Login attempts will be denied under any other circumstances.

**Please pay close attention to the feedback messages you receive during the attacks.**

Known credentials:

user name                                   password
webgoat                                     webgoat
admin                                       admin

Goal
- Once you have a clear understanding of how the authentication cookie is generated, attempt to spoof the cookie and log in as Tom.

![alt text](<../image/Lab-4 Spoofing an Authentication Cookie.md/image-2.png>)



- Turn on the Interceptor (Burp) 

- Enter the known user credentials (webgoat/admin). 

- What results you can compare: WebGoat and Admin have their own spoofed cookie but as you continue to log in you will notice that the spoof cookie for each login maintains its value. 

**Admin Cookie= NDE1MTc5NjI3MjU3NTg1NTRjNTc2ZTY5NmQ2NDYx**

**WebGoat Cookie= NDE1MTc5NjI3MjU3NTg1NTRjNTc3NDYxNmY2NzYyNjU3Nw=**

What is the encoding Scheme?: https://www.base64decode.org/

- After you encode the spoofed cookies into UTF-8 you will receive the folowing values: 

**Admin= 41517962725758554c576e696d6461**

**WebGoat= 41517962725758554c5774616f67626577**

UTF-8 encodes in HEX values, meaning in 8 BITS. We can use a Converter from HEX to Text (https://codebeautify.org/hex-string-converter). 

**Admin spoofed cookie into text= AQybrWXULWnimda**

**WebGoat spoofed cookie into text= AQybrWXULWtaogbew**

We can see the characteristics of the encoding values, keeping the first part the same and spelling backwards the user name. 

Now go to the section of string reverser on CodeBeautify to reverse the string: 

**Admin= adminWLUXWrbyQA**

**WebGoat= webgoatWLUXWrbyQA**

Now replace on the reversed string Admin or WebGoat into TOM. 

AQybrWXULWmoT

Then go back to the section of String to HEX in CodeBeautify, and encode the above string. 

**41517962725758554c576d6f54**

Go into the Base64Encode Website and Encode the string into UTF-8. 

**NDE1MTc5NjI3MjU3NTg1NTRjNTc2ZDZmNTQ=**

- How do we authenticate the new authentication cookie? 

- Find the corresponding POST request. Forward it to the Repeater (Burp)

![alt text](<../image/Lab-4 Spoofing an Authentication Cookie.md/image-3.png>)

![alt text](<../image/Lab-4 Spoofing an Authentication Cookie.md/image-4.png>)


