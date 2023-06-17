# How do I download PostgreSQL?
// plain

1. Download the latest version of PostgreSQL from the [PostgreSQL download page](https://www.postgresql.org/download/).
2. Select the version of PostgreSQL that you would like to download.
3. Select the platform you would like to install the software on.
4. Follow the instructions to install the software.
5. After installation, open the command line and type `psql -V` to check the version of PostgreSQL installed. The output should be something like `psql (PostgreSQL) 10.5`.
6. To connect to the PostgreSQL server, type `psql -h localhost -U postgres` in the command line.
7. You should be connected to the PostgreSQL server. To test this, type `\l` to list all databases and `\q` to quit the server.

onelinerhub: [How do I download PostgreSQL?](https://onelinerhub.com/postgresql/how-do-i-download-postgresql)