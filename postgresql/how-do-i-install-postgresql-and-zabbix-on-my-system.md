# How do I install PostgreSQL and Zabbix on my system?
// plain

1. Install PostgreSQL:
   - Download and install the PostgreSQL installer from [https://www.postgresql.org/download/](https://www.postgresql.org/download/).
   - Follow the instructions to install PostgreSQL on your system.
   - After installation, open the command line and type `psql -V` to verify the version you have installed.

2. Install Zabbix:
   - Download the Zabbix source code from [https://www.zabbix.com/download](https://www.zabbix.com/download).
   - Extract the source code and navigate to the extracted folder.
   - Run the following command to install Zabbix:
   ```
   ./configure --enable-server --with-postgresql
   make install
   ```
   - After installation, you can run the following command to verify the installation:
   ```
   zabbix_server -V
   ```
   Output: Zabbix server v4.4.7 (revision d4a7e4e).

## Helpful links
- [https://www.postgresql.org/download/](https://www.postgresql.org/download/)
- [https://www.zabbix.com/download](https://www.zabbix.com/download)

onelinerhub: [How do I install PostgreSQL and Zabbix on my system?](https://onelinerhub.com/postgresql/how-do-i-install-postgresql-and-zabbix-on-my-system)