# How to use xtrabackup in Mariadb?
// plain

XtraBackup is a free open source tool for performing hot backups of MariaDB databases. It can be used to back up a single database, multiple databases, or an entire MariaDB server.

To use XtraBackup, you need to install the XtraBackup package on your MariaDB server.

Once installed, you can use the following command to back up a single database:

```
xtrabackup --backup --target-dir=/backup/dbname
```

This will create a backup of the database in the `/backup/dbname` directory.

To restore the database, you can use the following command:

```
xtrabackup --prepare --target-dir=/backup/dbname
```

This will prepare the backup for restoring.

Finally, you can restore the database using the following command:

```
xtrabackup --copy-back --target-dir=/backup/dbname
```

This will restore the database from the backup.

## Helpful links

- [XtraBackup Documentation](https://www.percona.com/doc/percona-xtrabackup/2.4/index.html)
- [MariaDB Backup and Recovery](https://mariadb.com/kb/en/library/backup-and-recovery/)

onelinerhub: [How to use xtrabackup in Mariadb?](https://onelinerhub.com/mariadb/how-to-use-xtrabackup-in-mariadb)