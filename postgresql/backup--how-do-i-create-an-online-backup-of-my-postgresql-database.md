# backup

How do I create an online backup of my PostgreSQL database?
// plain

Creating an online backup of a PostgreSQL database is a relatively straightforward process.

1. Connect to the database using `psql`:

```
$ psql -U username -h hostname -d databasename
```

2. Create the backup file using `pg_dump`:

```
$ pg_dump -U username -h hostname -d databasename -f backup_file_name.sql
```

3. Upload the backup file to an online storage service.

4. Create a script to automate the backup process.

The following example script can be used to create an automated backup of a PostgreSQL database:

```bash
#!/bin/bash

# Create a variable containing the current date and time
NOW=$(date +"%Y-%m-%d-%H-%M-%S")

# Create a variable containing the name of the backup file
BACKUP_FILE="backup_$NOW.sql"

# Create the backup file using pg_dump
pg_dump -U username -h hostname -d databasename -f $BACKUP_FILE

# Upload the backup file to an online storage service
aws s3 cp $BACKUP_FILE s3://my-bucket/backups/
```

The script can be scheduled to run periodically using `cron` or another scheduling utility.

## Helpful links

- [PostgreSQL Documentation - pg_dump](https://www.postgresql.org/docs/current/app-pgdump.html)
- [AWS Documentation - Copying files to and from Amazon S3](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)
- [Cron - Wikipedia](https://en.wikipedia.org/wiki/Cron)

onelinerhub: [backup

How do I create an online backup of my PostgreSQL database?](https://onelinerhub.com/postgresql/backup--how-do-i-create-an-online-backup-of-my-postgresql-database)