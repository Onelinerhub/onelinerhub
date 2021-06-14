# Create dump (backup) for all databases

```bash
mysqldump --all-databases > backup.sql
```

- --all-databases - this option will make sure all databases on the server are dumped
- backup.sql - name of dump file

group: dump
