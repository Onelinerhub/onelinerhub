# How do I install PostgreSQL?
// plain

1. Download PostgreSQL from [PostgreSQL website](https://www.postgresql.org/download/).
2. Install the downloaded package with the command: ```sudo apt-get install postgresql-12```.
3. After installation, create a user and database with the following commands:

```
sudo -u postgres createuser -s <username>
sudo -u postgres createdb <dbname>
```

4. Connect to the database with the command: ```psql -U <username> -d <dbname>```.
5. Create tables and add data to the database with SQL commands.
6. To stop the database, use the command: ```sudo service postgresql stop```.
7. To start the database, use the command: ```sudo service postgresql start```.

onelinerhub: [How do I install PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-install-postgresql)