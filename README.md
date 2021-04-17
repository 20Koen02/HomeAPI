# 🏠 HomeAPI
![HomeAPI](https://socialify.git.ci/20Koen02/HomeAPI/image?description=1&font=Source%20Code%20Pro&forks=1&issues=1&language=1&logo=data%3Aimage%2Fsvg%2Bxml%2C%253Csvg%20xmlns%3D%27http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%27%20viewBox%3D%270%200%2024%2024%27%20width%3D%2724%27%20height%3D%2724%27%253E%253Cpath%20fill%3D%27none%27%20d%3D%27M0%200h24v24H0z%27%2F%253E%253Cpath%20d%3D%27M20%2020a1%201%200%200%201-1%201H5a1%201%200%200%201-1-1v-9H1l10.327-9.388a1%201%200%200%201%201.346%200L23%2011h-3v9zM7%2011v2a5%205%200%200%201%205%205h2a7%207%200%200%200-7-7zm0%204v3h3a3%203%200%200%200-3-3z%27%20fill%3D%27rgba(255%2C255%2C255%2C1)%27%2F%253E%253C%2Fsvg%253E&owner=1&pattern=Brick%20Wall&pulls=1&stargazers=1&theme=Dark)
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
