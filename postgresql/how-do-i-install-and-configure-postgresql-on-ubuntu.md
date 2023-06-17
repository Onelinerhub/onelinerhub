# How do I install and configure PostgreSQL on Ubuntu?
// plain

1. Install PostgreSQL on Ubuntu:
   ```
   sudo apt-get install postgresql postgresql-contrib
   ```
2. Create a New Database and User:
   ```
   sudo -u postgres psql
   CREATE DATABASE mydb;
   CREATE USER myuser WITH PASSWORD 'mypass';
   GRANT ALL PRIVILEGES ON DATABASE mydb TO myuser;
   ```
3. Configure PostgreSQL:
   - Edit the `pg_hba.conf` file to control the authentication method.
   - Edit the `postgresql.conf` file to configure the parameters of the server.
4. Restart the PostgreSQL Service:
   ```
   sudo /etc/init.d/postgresql restart
   ```
5. Connect to the Database:
   ```
   psql -h localhost -U myuser mydb
   ```

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [Installing and Using PostgreSQL on Ubuntu](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)

onelinerhub: [How do I install and configure PostgreSQL on Ubuntu?](https://onelinerhub.com/postgresql/how-do-i-install-and-configure-postgresql-on-ubuntu)