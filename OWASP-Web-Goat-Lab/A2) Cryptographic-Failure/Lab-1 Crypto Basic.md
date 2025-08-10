**Part-1**

**Concept**
This lesson explains different types of cryptography techniques that are commonly used in web applications.

**Goals**
The goal is to get familiar with the following forms of techniques:

1- **Encoding**

2- **Hashing**

3- **Encryption**

4- **Signing**

5- **Keystores**

6- **Security defaults**

7- **Post quantum crypto**

**Assignments**
After the explanation of an item there will be several assignments.

---------------------------------------------------------------------------------------------

**Base64 Encoding**
Encoding is not really cryptography, but it is used a lot in all kinds of standards around cryptographic functions. Especially Base64 encoding.

Base64 encoding is a technique used to transform all kinds of bytes to a specific range of bytes. This specific range is the ASCII readable bytes. This way you can transfer binary data such as secret or private keys more easily. You could even print these out or write them down. Encoding is also reversible. So if you have the encoded version, you can create the original version.

On wikipedia you can find more details. Basically it goes through all the bytes and transforms each set of 6 bits into a readable byte (8 bits). The result is that the size of the encoded bytes is increased with about 33%.

**Hello ==> SGVsbG8=**
**0x4d 0x61 ==> TWE=**

**Basic Authentication**
Basic authentication is sometimes used by web applications. This uses base64 encoding. Therefore, it is important to at least use Transport Layer Security (TLS or more commonly known as https) to protect others from reading the username password that is sent to the server.

**$echo -n "myuser:mypassword" | base64**
**bXl1c2VyOm15cGFzc3dvcmQ=**

**The HTTP header will look like:**
**Authorization: Basic bXl1c2VyOm15cGFzc3dvcmQ=**

- In my case my Authorization Basic  is **"YWRtaW54OjEyMzQ1Ng=**

![alt text](<../../image/Lab-1 Crypto Basic.md/image.png>)

- Go to https://www.base64decode.org/ and decode the authorization header "YWRtaW54OjEyMzQ1Ng==". 

![alt text](<../../image/Lab-1 Crypto Basic.md/image-1.png>)

![alt text](<../../image/Lab-1 Crypto Basic.md/image-2.png>)

---------------------------------------------------------------------------------------------

**Part-2**

**Other Encoding**
Also other encodings are used.

**URL encoding**
URL encoding is used a lot when sending form data and request parameters to the server. Since spaces are not allowed in a URL, this is then replaced by %20. Similar replacements are made for other characters.

**HTML encoding**
HTML encoding ensures that text is displayed as-is in the browser and not interpreted by the browser as HTML.

**UUEncode**
The Unix-2-Unix encoding has been used to send email attachments.

**XOR encoding**
Sometimes encoding is used as a first and simple obfuscation technique for storing passwords. IBM WebSphere Application Server e.g. uses a specific implementation of XOR encoding to store passwords in configuration files. IBM recommends to protect access to these files and to replace the default XOR encoding by your own custom encryption. However when these recommendations are not followed, these defaults can become a vulnerability.

**Assignment**
Now let’s see if you are able to find out the original password from this default XOR encoded string.

![alt text](<../../image/Lab-1 Crypto Basic.md/image-3.png>)

- As provided the password encoded, we will use XOR encoding to find the password. 

- We can use the following XOR decoder: https://strelitzia.net/wasXORdecoder/wasXORdecoder.html

![alt text](<../../image/Lab-1 Crypto Basic.md/image-4.png>)

- **Introduce the actual password on WebGoat.**

![alt text](<../../image/Lab-1 Crypto Basic.md/image-5.png>) 

-------------------------------------------------------------------------
**Part-3**

**Plain Hashing**
Hashing is a type of cryptography which is mostly used to detect if the original data has been changed. A hash is generated from the original data. It is based on irreversible cryptographic techniques. If the original data is changed by even one byte, the resulting hash is also different.

So in a way it looks like a secure technique. However, it is NOT and even NEVER a good solution when using it for passwords. The problem here is that you can generate passwords from dictionaries and calculate all kinds of variants from these passwords. For each password you can calculate a hash. This can all be stored in large databases. So whenever you find a hash that could be a password, you just look up the hash in the database and find out the password.

Some hashing algorithms should no longer be used: MD5, SHA-1 For these hashes it is possible to change the payload in such a way that it still results in the same hash. This takes a lot of computing power, but is still a feasible option.

**Salted Hashes**
Plain passwords should obviously not be stored in a database. And the same goes for plain hashes. The OWASP Password Storage Cheat Sheet https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html explains what should be used when password related information needs to be stored securely.

**Assignment**
Now let’s see if you can find what passwords matches which plain (unsalted) hashes.

![alt text](<../../image/Lab-1 Crypto Basic.md/image-7.png>)

- Go to WebGoat and copy the first Hash. 

- Open Hashes.com and paste the hash. Click in the button "Submit & Identify". 

![alt text](<../../image/Lab-1 Crypto Basic.md/image-9.png>)

![alt text](<../../image/Lab-1 Crypto Basic.md/image-10.png>)

![alt text](<../../image/Lab-1 Crypto Basic.md/image-11.png>)

-------------------------------------------------------------------------
**Part-4**

**Symmetric encryption**
Symmetric encryption is based on a shared secret that is used for both encryption as well as decryption. Therefore, both parties (that are involved in exchanging secrets) share the same key.

**Example protocols are:**

**AES**

**3DES**

**Asymmetric encryption**
Asymmetric encryption is based on mathematical principles that consist of a key pair. The two keys are usually called a private key and a public key. The private key needs to be protected very well and is only known to one party. All others can freely use the public key. Something encrypted with the private key can be decrypted by all that have the public key, and something encrypted with the public key can only be decrypted with the private key.

**Example protocols are:**

**RSA**

**DSA**

**HTTPS uses both symmetric and asymmetric keys**
Here is a short description of what happens if you open your browser and go to an https site.

Your browser connects to the server and gets the webserver certificate

Your browser checks if it trusts the certificate issuer by checking if the issuer certificate is in its trust store. This trust store is managed by operating system and browser updates. And on some corporate networks it is managed by the company. From the certificate the browser obtains the public key.

The browser now generates random bytes to be used to generate a symmetric key and encrypts this with the public key of the server. So only the server can decrypt it.

At the end of this process both the browser and the webserver will use the exchanged symmetric key (in the asymmetric key exchange process) to encrypt and decrypt messages that are sent back and forth between the browser and the webserver.

Symmetric keys are used because it can be used more easily with large sets of data and requires less processing power in doing so. However, the information on these pages is just for a basic understanding of cryptography. Look on the internet for more detailed information about these topics.


A signature is a hash that can be used to check the validity of some data. The signature can be supplied separately from the data that it validates, or in the case of CMS or SOAP can be included in the same file. (Where parts of that file contain the data and parts contain the signature).

Signing is used when integrity is important. It is meant to be a guarantee that data sent from Party-A to Party-B was not altered. So Party-A signs the data by calculating the hash of the data and encrypting that hash using an asymmetric private key. Party-B can then verify the data by calculating the hash of the data and decrypting the signature to compare if both hashes are the same.

**RAW signatures**

A raw signature is usually calculated by Party-A as follows:

create a hash of the data (e.g. SHA-256 hash)

encrypt the hash using an asymmetric private key (e.g. RSA 2048 bit key)

(optionally) encode the binary encrypted hash using base64 encoding

Party-B will have to get the certificate with the public key as well. This might have been exchanged before. So at least 3 files are involved: the data, the signature and the certificate.

**CMS signatures**

A CMS signature is a standardized way to send data + signature + certificate with the public key all in one file from Party-A to Party-B. As long as the certificate is valid and not revoked, Party-B can use the supplied public key to verify the signature.

**SOAP signatures**

A SOAP signature also contains data and the signature and optionally the certificate. All in one XML payload. There are special steps involved in calculating the hash of the data. This has to do with the fact that the SOAP XML sent from system to system might introduce extra elements or timestamps. Also, SOAP Signing offers the possibility to sign different parts of the message by different parties.

**Email signatures**

Sending emails is not very difficult. You have to fill in some data and send it to a server that forwards it, and eventually it will end up at its destination. However, it is possible to send emails with a FROM field that is not your own email address. In order to guarantee to your receiver that you really sent this email, you can sign your email. A trusted third party will check your identity and issue an email signing certificate. You install the private key in your email application and configure it to sign emails that you send out. The certificate is issued on a specific email address and all others that receive this email will see an indication that the sender is verified, because their tools will verify the signature using the public certificate that was issued by the trusted third party.

**PDF or Word or other signatures**

Adobe PDF documents and Microsoft Word documents are also examples of things that support signing. The signature is also inside the same document as the data so there is some description on what is part of the data and what is part of the metadata. Governments usually send official documents with a PDF that contains a certificate.

**Assignment**
Here is a simple assignment. A private RSA key is sent to you. Determine the modulus of the RSA key as a hex string, and calculate a signature for that hex string using the key. The exercise requires some experience with OpenSSL. You can search on the Internet for useful commands and/or use the HINTS button to get some tips.

![alt text](<../../image/Lab-1 Crypto Basic.md/image-12.png>)

- We will use WebGoat docker container terminal to run the commands. 

- As stated in WebGoat exercise, we have the private key value. 

- In base on the information provided we can create the following echo commands

![alt text](<../../image/Lab-1 Crypto Basic.md/image-13.png>)

- To get the modulus we will need to run the following openssl command: 

**openssl rsa -text -noout -in private.key**

- Now convert the private key into public key

 **openssl rsa -in public.pub -pubin -modulus -noout**

**echo -n "9E84C4997FDF2CCB2BB76C5DECB596EABBF7A79CAA5242DC579F1C0F00503DDF4CC74CB3286E68293B67E5106FEA92BE14CA37A4B7906FFEF9816E915EBC994CB44E871C432A9BE5939FF1B18F38ABA70873FBEEAAD98C81C6690305699E615C3B871E3060EB58FE216032E56E82845FE4839C9BB90609A01F427C918708B85D2167196E4699AD6B1F73617762D81C177A7FCE81658C84720FC6DCF6E60925A8C71D168644E882EB1289C0452C5C0BE3CC527DC21618217976B519BD0A8662FC6AD2997F1D0B6B7E63C4939850079C214AAC5AECF3C8FB6E2C1AF16EA19D15DC1D1A3029E8B99A4C7E1E193CE7516B1084ACF31C446381917E79EE1283199141" | openssl dgst -sign private.key -sha256 -out sign.sha265**

**openssl enc -base64 -in sign.sha265 -out sign.sha265.sha256**

**cat sign.sha256.sha256**

![alt text](<../../image/Lab-1 Crypto Basic.md/image-14.png>)

![alt text](<../../image/Lab-1 Crypto Basic.md/image-15.png>)

![alt text](<../../image/Lab-1 Crypto Basic.md/image-16.png>)

-------------------------------------------------------------------------
**Part-5**

A keystore is a place where you store keys. Besides keystore the term truststore is also used frequently. A truststore is the same thing as a keystore. Only it usually contains only the certificates (so basically only public keys and issuer information) of trusted certificates or certificate authorities.

**File based keystores**
A file based keystore is something that in the end has the keys on a file system. Storing public certificates in a file based keystore is very common

**Database keystores**
Keys and especially public certificates can of course also be stored in a database.

**Hardware keystore**
A hardware keystore is a system that has some sort of hardware which contain the actual keys. This is typically done in high end security environments where the private key is really private. In comparison with file based or database keystores, it is impossible to make a copy of the keystore to send it to some unknown and untrusted environment.

**Certificate authorities that are used to provide you with a server** certificate for your website, also create the private keys for you (as-a-service). However, it is by definition no longer considered a private key. For all keystore types, you should keep the private key private and use a certificate signing request to order your signing or server certificates.

**Managed keystores in operating system, browser and other applications**
When you visit a website and your browser says that the certificates are fine, it means that the certificate used for the website is issued by a trusted certificate authority. But this list of trusted certificate authorities is managed. Some CA’s might be revoked or removed. These updates happen in the background when browser updates are installed. Not only the browser maintains a list of trusted certificate authorities, the operation system does so as well. And the Java runtime also has its own list which is kept in the cacerts file. Updates of the OS and Java JRE keep this list up to date. In corporate environments, these are usually maintained by the company and also contain company root certificates.

**Extra check for website certificates using DNS CAA records**
Some companies inspect all or most internet traffic. Even the ones were you think you have an end-2-end secured connection. This works as follows. An employee opens a browser and googles some information. The browser will use https and go to the site of google. The link looks real and the lock is shown in the browser. However, if you would inspect the certificate, you might notice that it has been issued by one of your companies root CA’s! So you have established an end-2-end secure connection with a server of your company, and that server has the secure connection with google. In order to prevent such man in the middle connections to your server, modern browsers now will also check the DNS CAA records to see whether or not a certain issuer is allowed for a certain website. More information: Wiki DNS CAA

**Free certificates from Let’s encrypt**
Let’s encrypt is a free, automated and open Certificate Authority. It allows you to create valid certificates for the websites that you control. By following and implementing a certain protocol, your identity is checked and a certificate will be issued. The certificates are free of charge and this is done to stimulate the use of authorised certificates and to lower the use of self-signed certificates on the internet. Certificates are valid for 90 days, so they need to be automatically renewed. (Which makes sure that the proof of identity/ownership also takes place frequently)

A big problem in all kinds of systems is the use of default configurations. E.g. default username/passwords in routers, default passwords for keystores, default unencrypted mode, etc.

-------------------------------------------------------------------------