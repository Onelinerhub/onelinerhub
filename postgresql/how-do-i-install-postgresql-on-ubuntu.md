# How do I install PostgreSQL on Ubuntu?
// plain

1. Download and install the PostgreSQL package:
   ```
   sudo apt-get install postgresql postgresql-contrib
   ```

2. Create a new PostgreSQL user:
   ```
   sudo -u postgres createuser --interactive
   ```
   This command will prompt you to create a new user. Type in the name of the user you want to create.

3. Create a new database:
   ```
   sudo -u postgres createdb [database name]
   ```

4. Connect to the database:
   ```
   psql -U [username] -d [database name]
   ```

5. Set a password for the user:
   ```
   \password [username]
   ```

6. Grant privileges to the user:
   ```
   GRANT ALL PRIVILEGES ON DATABASE [database name] TO [username];
   ```

7. Exit the PostgreSQL shell:
   ```
   \q
   ```

## Helpful links
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)
- [PostgreSQL Installation Guide](https://www.postgresql.org/docs/current/tutorial-install.html)

onelinerhub: [How do I install PostgreSQL on Ubuntu?](https://onelinerhub.com/postgresql/how-do-i-install-postgresql-on-ubuntu)