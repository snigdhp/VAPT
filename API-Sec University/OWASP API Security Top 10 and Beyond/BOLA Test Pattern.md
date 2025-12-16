## BOLA Test Patterns (Examples)

| Type | Valid request | BOLA test |
|------|--------------|-----------|
| **Predictable ID** | `GET /api/v1/account/2222`<br>`Token: UserA_token` | `GET /api/v1/account/3333`<br>`Token: UserA_token` |
| **ID combo** | `GET /api/v1/UserA/data/2222`<br>`Token: UserA_token` | `GET /api/v1/UserB/data/3333`<br>`Token: UserA_token` |
| **Integer as ID** | `POST /api/v1/account/`<br>`Token: UserA_token`<br>Body: `{"Account": 2222}` | `POST /api/v1/account/`<br>`Token: UserA_token`<br>Body: `{"Account": 3333}` |
| **Email as user ID** | `POST /api/v1/user/account`<br>`Token: UserA_token`<br>Body: `{"email": "UserA@email.com"}` | `POST /api/v1/user/account`<br>`Token: UserA_token`<br>Body: `{"email": "UserB@email.com"}` |
| **Group ID** | `GET /api/v1/group/CompanyA`<br>`Token: UserA_token` | `GET /api/v1/group/CompanyB`<br>`Token: UserA_token` |
| **Group and user combo** | `POST /api/v1/group/CompanyA`<br>`Token: UserA_token`<br>Body: `{"email": "userA@CompanyA.com"}` | `POST /api/v1/group/CompanyB`<br>`Token: UserA_token`<br>Body: `{"email": "userB@CompanyB.com"}` |
| **Nested object** | `POST /api/v1/user/checking`<br>`Token: UserA_token`<br>Body: `{"Account": 2222}` | `POST /api/v1/user/checking`<br>`Token: UserA_token`<br>Body: `{"Account": {"Account": 3333}}` |
| **Multiple objects** | `POST /api/v1/user/checking`<br>`Token: UserA_token`<br>Body: `{"Account": 2222}` | `POST /api/v1/user/checking`<br>`Token: UserA_token`<br>Body: `{"Account": [2222, 3333, 5555]}` |
| **Predictable token** | `POST /api/v1/user/account`<br>`Token: UserA_token`<br>Body: `{"data": "DfIkidf7jSdfaiacaa"}` | `POST /api/v1/user/account`<br>`Token: UserA_token`<br>Body: `{"data": "DfIkidf7jSdfa2dfaa"}` |

---
![alt text][def]

[def]: image.png