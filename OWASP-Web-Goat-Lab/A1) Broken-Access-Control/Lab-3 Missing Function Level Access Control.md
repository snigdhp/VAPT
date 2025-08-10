**Missing Function Level Access Control**
Access control, like preventing XSS with output encoding, can be tricky to maintain. One must ensure it is adequately enforced throughout the entire application, thus in every method/function.

IDOR vs Missing Function Level Access Control
The fact is many people (including the author of this lesson) would combine function level access control and IDOR into 'Access Control.' For the sake of OWASP Top 10 and these lessons, we will make a distinction. The distinction most made is that IDOR is more of a 'horizontal' or 'lateral' access control issue, and missing function level access control 'exposes functionality.' Even though the IDOR lesson here demonstrates how functionality may also be exposed (at least to another user in the same role), we will look at other ways functionality might be exposed.




---------------------------------------------------------------------------------------------
Relying on obscurity
One could rely on HTML, CSS, or javascript to hide links that users don’t normally access. In the past, a network router tried to protect (hide) admin functionality with javascript in the UI: https://www.wired.com/2009/10/routers-still-vulnerable.

Finding hidden items
There are usually hints to finding functionality the UI does not openly expose in:

HTML or javascript comments

Commented out elements

Items hidden via CSS controls/classes

Your mission
Find two invisible menu items in the menu below that are or would be of interest to an attacker/malicious user and submit the labels for those menu items (there are no links right now in the menus).

- Here we need to find hidden items in the HTML code by click on inspect menu 

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image.png>)

- And we found that hidden items are Users and Config Respectively

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/Screenshot 2025-08-04 011702.png>)

---------------------------------------------------------------------------------------------
Try it
As the previous page described, sometimes applications rely on client-side controls to control access (obscurity). If you can find invisible items, try them and see what happens. Yes, it can be that simple!

Gathering User Info
Often data dumps originate from vulnerabilities such as SQL injection, but they can also come from poor or lacking access control.

It will likely take multiple steps and multiple attempts to get this one:

Pay attention to the comments and leaked info.

You’ll need to do some guessing too.

You may need to use another browser/account along the way.

Start with the information you already gathered (hidden menu items) to see if you can pull the list of users and then provide the 'hash' for Jerry’s account.

- Here in this Lab we need to get the hash id of jeery account

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-1.png>)

- So by Intercepting the Request by click on submit button and this Post Request to Repeater 

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-2.png>)

- Here we are on Repeater Request and by clicking on Send button we checking the Server Response

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-3.png>)

- Now we are POST Header Method as we know we know we found hidden items as users so change the value of **user-hash** to **users** , **POST** Method into **GET** Changing the content **x-www-form-urlencoded** type as **application/json** , Here found the Jerry User-hash id 

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-4.png>)
![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-5.png>)

---------------------------------------------------------------------------------------------
The company fixed the problem, right?
The company found out the endpoint was a bit too open, they made an emergency fixed and not only admin users can list all users.

Start with the information you already gathered (hidden menu items) to see if you can pull the list of users and then provide the 'hash' for Jerry’s account.

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-6.png>)

- Here is we need to intercept the request to get the jerry hash account

![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-7.png>)

- Now we need to manipulate the Request body to get the Jerry user-Hash id 
- Here on the Request i manipulate the request **POST** into **GET** and header change as **user-hash-fix** to **users** , application type into **application/json** and Your payload should resemble something like this of admin user account access


![alt text](<../image/Lab-3 Missing Function Level Access Control.md/image-8.png>)