Installation instructions:

1. Run using Docker
Already have a browser and ZAP and/or Burp installed on your machine in this case you can run the WebGoat image directly using Docker.

Every release is also published on DockerHub.

docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 webgoat/webgoat
For some lessons you need the container run in the same timezone. For this you can set the TZ environment variable. E.g.

docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e TZ=America/Boise webgoat/webgoat
If you want to use OWASP ZAP or another proxy, you can no longer use 127.0.0.1 or localhost. but you can use custom host entries. For example:

127.0.0.1 www.webgoat.local www.webwolf.local
Then you can run the container with:

docker run -it -p 127.0.0.1:8080:8080 -p 127.0.0.1:9090:9090 -e WEBGOAT_HOST=www.webgoat.local -e WEBWOLF_HOST=www.webwolf.local -e TZ=America/Boise webgoat/webgoat

---------------------------------------------------------------------------------------------
 Web Application Security Analysis Project

  Objective
This project demonstrates how to analyze and identify common web application vulnerabilities using OWASP ZAP and WebGoat. The goal is to understand how attackers exploit weaknesses such as:
- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Inscure Direct Object References (IDOR)

 Tools & Environment

| Tool          | Purpose |

| 🐱 Kali Linux | Security-focused Linux distro |
| ☠️ WebGoat     | Intentionally vulnerable web app |
| 🕷️ Burpsuite | Vulnerability scanner |
| 🌐 Firefox    | Manual interaction & testing |
| 📸 Snipping Tool / Screenshot | Documentation images |

🔍 Vulnerability Analysis Steps

✅ 1. Burpsuite
	•	Using Firefox proxy and setting up local host as 12.0.0.1 and port Number 8080
	•	Enabling foxy Proxy and intercepting Request through BurpSuite 

✅ 2. Find & Understand Vulnerabilities

    Use Burpsuite alerts to locate vulnerabilities:
	•	SQL Injection – login or user input fields
	•	XSS – search forms or comment inputs
	•	CSRF – user settings or password change forms0
    •   IDOR - Inscure Direct Object References - checking level of authentication 

📘 What I Learned
	•	How to identify web vulnerabilities using an automated scanner
	•	How to manually exploit basic injection and scripting flaws
	•	The importance of secure coding practices and mitigation
	•	Documenting security analysis like a professional

