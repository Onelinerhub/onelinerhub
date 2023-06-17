# How do I set up PostgreSQL replication?
// plain

**Setting up PostgreSQL replication**

1. Create a master server and a slave server.
2. On the master server, edit the postgresql.conf file and set the following parameters:
   ```
   wal_level = hot_standby
   max_wal_senders = 10
   wal_keep_segments = 8
   ```
3. Restart the master server.
4. On the slave server, edit the postgresql.conf file and set the following parameters:
   ```
   hot_standby = on
   ```
5. Create a recovery.conf file on the slave server with the following content:
   ```
   standby_mode = 'on'
   primary_conninfo = 'host=<master_host> port=<master_port> user=<replication_user> password=<replication_password>'
   trigger_file = '/tmp/postgresql.trigger.5432'
   ```
6. Restart the slave server.
7. On the master server, create a replication user with REPLICATION privilege.

## Helpful links

- [PostgreSQL Documentation: Setting Up Streaming Replication](https://www.postgresql.org/docs/9.3/warm-standby.html#STREAMING-REPLICATION-SETUP)
- [PostgreSQL Documentation: Hot Standby](https://www.postgresql.org/docs/9.3/hot-standby.html)

onelinerhub: [How do I set up PostgreSQL replication?](https://onelinerhub.com/postgresql/how-do-i-set-up-postgresql-replication)