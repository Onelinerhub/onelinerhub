# How do I restart Sphinxsearch?
// plain

To restart Sphinxsearch, you will need to stop the searchd service and then start it again.

1. Stop the service:
   ```
   sudo service searchd stop
   ```

2. Start the service:
   ```
   sudo service searchd start
   ```

3. Check the status of the service:
   ```
   sudo service searchd status
   ```
   Output:
   ```
   searchd (pid  1187) is running...
   ```

This will restart the Sphinxsearch service.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Ubuntu Manpage for service](http://manpages.ubuntu.com/manpages/xenial/man8/service.8.html)

onelinerhub: [How do I restart Sphinxsearch?](https://onelinerhub.com/sphinxsearch/how-do-i-restart-sphinxsearch)