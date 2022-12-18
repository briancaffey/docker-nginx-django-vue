# A Django/VueJS project setup with Docker, nginx and gunicorn

List running containers

```
prompt:~$ docker ps
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
a8d1b6462198        sept22_web          "python3 manage.py r…"   About an hour ago   Up About an hour    0.0.0.0:8000->8000/tcp   sept22_web_1
50c3e3947989        postgres            "docker-entrypoint.s…"   2 hours ago         Up About an hour    5432/tcp                 sept22_db_1
```

To start docker with any changes made to Dockerfile:

```
docker-compose up --build
```

To issue a command from terminal to a running docker container:

```
docker exec -it a8d1b6462198 bash
```

Log in to postgres container and open postgres shell:

```
docker exec -it 50c3e3947989 bash
```

