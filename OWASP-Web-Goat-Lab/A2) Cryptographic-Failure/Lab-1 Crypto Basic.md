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