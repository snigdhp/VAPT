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
