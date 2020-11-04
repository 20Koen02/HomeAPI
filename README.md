# HomeAPI
**HomeAPI** connects local machines & smart devices to the internet

## 💡 Features
* Turn on a **Wake on LAN** compatible machine
* Fully control **YeeLight** bulbs
* Authentication with **OAuth2** password flow
* Multiple **SQL Databases** supported
* **Fully documented** on the /docs page

## 📝 To Do
* Make **HomeAPI Client** for target machines to turn off the machine
* Turn a machine off with the **HomeAPI Client**
* Support for Xiaomi Mijia Bluetooth **Temperature Humidity Sensor**
* Store Temperature & Humidity data in an **InfluxDB Database**
* Write unit tests for every endpoint
* Configure automatic test runner & codecov

## 🔧 Technologies & Tools
![](https://img.shields.io/badge/Code-Python-informational?style=flat&logo=python&logoColor=white&color=db4949)
![](https://img.shields.io/badge/Tools-Docker-informational?style=flat&logo=docker&logoColor=white&color=db4949)
![](https://img.shields.io/badge/Tools-FastAPI-informational?style=flat&logo=python&logoColor=white&color=db4949)
![](https://img.shields.io/badge/Tools-SQLite-informational?style=flat&logo=sqlite&logoColor=white&color=db4949)


##  Installation

1. Clone the repo
```sh
git clone https://github.com/20Koen02/HomeAPI.git
```
2. Install dependencies
``` 
pip install -r requirements-dev.txt
```
3. Create ***configuration.env*** file into project root
``` 
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database>
POSTGRES_HOST=<host>
JWT_SECRET=<secret>
```
4. Run project
```
uvicorn app.main:app --reload --env-file configuration.env
```
5. Open site  http://127.0.0.1:8000/redoc

##  Deployment

1. Create ***configuration.env*** file into project root
```
POSTGRES_USER=<user>
POSTGRES_PASSWORD=<password>
POSTGRES_DB=<database>
POSTGRES_HOST=homeDB
JWT_SECRET=<secret>
```
**NOTE**: The variable **"POSTGRES_HOST"**  is the name of database service referenced into *docker-compose.yml* file, in case of you wish **change** it you should **modified** the name into *docker-compose.yml* file

2. Deployment **project**
```
sudo docker-compose up -d
```
or

<!--Use this option in case of wish you to recreate the image-->

```
sudo docker-compose up --build --force-recreate -d
```
3. Open site  http://127.0.0.1:8000/redoc
