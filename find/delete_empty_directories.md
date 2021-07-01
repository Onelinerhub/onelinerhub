# Delete all empty subdiretories

```bash
find /home/usr/ -type d -empty -delete
```

- /home/usr/ - Base path to search.
- -type d - Search only directories.
- -empty - Only list empty directories.
- -delete - Delete directories found.
