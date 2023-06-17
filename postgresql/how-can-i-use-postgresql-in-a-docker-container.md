# How can I use PostgreSQL in a Docker container?
// plain

PostgreSQL can be used in a Docker container by following the steps below:

1. Pull the PostgreSQL Docker image from Docker Hub:
```
docker pull postgres
```

2. Run the Docker container using the image:
```
docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

3. Connect to the PostgreSQL instance:
```
docker exec -it some-postgres psql -U postgres
```

4. Create a database:
```
CREATE DATABASE mydb;
```

5. Create a user:
```
CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
```

6. Grant privileges to the user to access the database:
```
GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
```

7. Finally, exit the PostgreSQL instance:
```
\q
```

## Helpful links
- [PostgreSQL Docker Hub](https://hub.docker.com/_/postgres)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

onelinerhub: [How can I use PostgreSQL in a Docker container?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-in-a-docker-container)