---
title: CSP Spot Check 1 (database, postman, cookies)
categories: ['CSP', 'Week 26']
tags: ['hacks']
---

- [X] Aashray Reddy, P5, 2.0/2.0
- [X] Q1 = 0.90; Q2 = 0.91; Q3 = 0.92
- [X] Q2 + Q2 + Q3 = 2.0 of 2.0

# database, with database schema change (0.90)

- [X] Show db.Column changes you have made to model/python file in Visual Studio Code
![image](https://github.com/KinetekEnergy/blog/assets/79232996/dedd289a-6822-43a3-a639-e77cd59be590)
- [X] Show initialization data code in VSCode
![image](https://github.com/KinetekEnergy/blog/assets/79232996/dd1c9783-a92e-4253-9916-d60b343cda02)
- [X] Demo delete database and run ./migrate.sh
![image](https://github.com/KinetekEnergy/blog/assets/79232996/56d7ef99-f66f-4ff2-b50c-50c85e2537a0)
- [X] Demo corresponding schema change in SQLite3
![image](https://github.com/KinetekEnergy/blog/assets/79232996/c71bb76a-9514-463d-968a-8b31f8e99989)
- [X] Demo initialization data captured in Column in SQLite3

# postman with /authentication screen (0.91)

- [X] Show /authenticate endpoint code in Visual Studio Code
![image](https://github.com/KinetekEnergy/blog/assets/79232996/80335f7a-59d7-458c-8c62-323ac5484b44)
- [X] Show and Demo /authenticate in Postman…
![image](https://github.com/KinetekEnergy/blog/assets/79232996/f0644992-7e0b-48a7-8a41-1e6539cf1166)
  - [X] Demo calling to endpoint
  - [X] Show JSON data passed in call
  - [X] Show Response window
![image](https://github.com/KinetekEnergy/blog/assets/79232996/ac03cab0-78a3-489d-9232-1f2a368a22a7)
  - [X] Show Cookie acquired window
![image](https://github.com/KinetekEnergy/blog/assets/79232996/37ff3069-3af8-402c-8e78-638538606161)
  - [X] Cut/Copy/Paste Cookie into[ jwt.io](https://jwt.io/) and show decrypting payload
![image](https://github.com/KinetekEnergy/blog/assets/79232996/2fc55228-0f71-4154-962b-cf90554bd904)

# postman with /api screen to access data under authentication (0.92)

- [x] Show /api CRUD code in Visual Studio Code, expecting READ/GET code
- [X] Show and Demo /api READ/GET endpoint in Postman…
![image](https://github.com/KinetekEnergy/blog/assets/79232996/cac56b20-7080-4dc2-8d58-e3bf2555e2fd)
  - [X] Demo calling to endpoint that requires Cookie
![image](https://github.com/KinetekEnergy/blog/assets/79232996/8801239b-d739-4932-9f0d-61e1456d8297)
  - [X] Show Response/Data
  - [X] Demo Deleting cookie
![image](https://github.com/KinetekEnergy/blog/assets/79232996/e0f9a45e-0848-4901-b5a9-c28b2487516f)
  - [X] Demo calling endpoint again
  - [X] Show Response/Failure
![image](https://github.com/KinetekEnergy/blog/assets/79232996/2f653933-fd84-413d-9934-bd37ffd92382)

