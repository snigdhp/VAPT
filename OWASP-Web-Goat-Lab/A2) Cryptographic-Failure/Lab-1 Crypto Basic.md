**Concept**
This lesson explains different types of cryptography techniques that are commonly used in web applications.

**Goals**
The goal is to get familiar with the following forms of techniques:

**Encoding**

**Hashing**

**Encryption**

**Signing**

**Keystores**

**Security defaults**

**Post quantum crypto**

**Assignments**
After the explanation of an item there will be several assignments.

---------------------------------------------------------------------------------------------

**Base64 Encoding**
Encoding is not really cryptography, but it is used a lot in all kinds of standards around cryptographic functions. Especially Base64 encoding.

Base64 encoding is a technique used to transform all kinds of bytes to a specific range of bytes. This specific range is the ASCII readable bytes. This way you can transfer binary data such as secret or private keys more easily. You could even print these out or write them down. Encoding is also reversible. So if you have the encoded version, you can create the original version.

On wikipedia you can find more details. Basically it goes through all the bytes and transforms each set of 6 bits into a readable byte (8 bits). The result is that the size of the encoded bytes is increased with about 33%.