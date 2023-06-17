# How do I set up a PostgreSQL HA cluster?
// plain

1. Install PostgreSQL on all of the nodes in the cluster.
2. Create a replication user with appropriate privileges.
```
CREATE USER replication_user WITH REPLICATION PASSWORD 'replication_password';
```
3. Configure the master node's `postgresql.conf` to enable replication.
```
listen_addresses = '*'
wal_level = 'hot_standby'
max_wal_senders = 10
wal_keep_segments = 10
```
4. Configure the slave nodes' `postgresql.conf` to enable streaming replication.
```
hot_standby = 'on'
wal_level = 'hot_standby'
max_wal_senders = 10
wal_keep_segments = 10
```
5. Create the replication slots on the master node.
```
SELECT * FROM pg_create_physical_replication_slot('slave_1');
```
6. Start the replication from the slave nodes.
```
pg_basebackup -h master_node -U replication_user -D /var/lib/postgresql/9.6/main --slot=slave_1
```
7. Configure the slave nodes' `recovery.conf` to enable streaming replication.
```
standby_mode = 'on'
primary_conninfo = 'host=master_node user=replication_user password=replication_password'
primary_slot_name = 'slave_1'
```

## Helpful links
- [PostgreSQL Documentation - Setting up Streaming Replication](https://www.postgresql.org/docs/9.6/warm-standby.html#STREAMING-REPLICATION-SETUP)
- [PostgreSQL Documentation - Setting up Hot Standby](https://www.postgresql.org/docs/9.6/hot-standby.html#HOT-STANDBY-SETUP)

onelinerhub: [How do I set up a PostgreSQL HA cluster?](https://onelinerhub.com/postgresql/how-do-i-set-up-a-postgresql-ha-cluster)