# How do I run the Sphinxsearch indexer?
// plain

1. Install Sphinxsearch:
   ```sh
   sudo apt-get install sphinxsearch
   ```

2. Create a configuration file:
   ```sh
   sudo nano /etc/sphinxsearch/sphinx.conf
   ```

3. Configure the indexer:
   - `indexer`: This is the name of the indexer.
   - `source`: This is the source of the data to be indexed.
   - `path`: This is the directory where the indexer will store the data.
   - `docinfo`: This is the type of information to be indexed.

4. Start the indexer:
   ```sh
   indexer --config /etc/sphinxsearch/sphinx.conf --all
   ```
   Output:
   ```
   Sphinx 2.2.13-id64-release (rel22-r5006)
   Copyright (c) 2001-2015, Andrew Aksyonoff
   Copyright (c) 2008-2015, Sphinx Technologies Inc (http://sphinxsearch.com)

   using config file '/etc/sphinxsearch/sphinx.conf'...
   indexing index 'indexer'...
   collected 0 docs, 0.0 MB
   total 0 docs, 0 bytes
   total 0.007 sec, 0 bytes/sec, 0.00 docs/sec
   ```

5. Monitor the indexer:
   ```sh
   indexer --config /etc/sphinxsearch/sphinx.conf --status
   ```
   Output:
   ```
   Sphinx 2.2.13-id64-release (rel22-r5006)
   Copyright (c) 2001-2015, Andrew Aksyonoff
   Copyright (c) 2008-2015, Sphinx Technologies Inc (http://sphinxsearch.com)

   using config file '/etc/sphinxsearch/sphinx.conf'...
   indexing index 'indexer'...
   collected 0 docs, 0.0 MB
   total 0 docs, 0 bytes
   total 0.007 sec, 0 bytes/sec, 0.00 docs/sec
   ```

6. Stop the indexer:
   ```sh
   indexer --config /etc/sphinxsearch/sphinx.conf --stop
   ```
   Output:
   ```
   Sphinx 2.2.13-id64-release (rel22-r5006)
   Copyright (c) 2001-2015, Andrew Aksyonoff
   Copyright (c) 2008-2015, Sphinx Technologies Inc (http://sphinxsearch.com)

   using config file '/etc/sphinxsearch/sphinx.conf'...
   indexing index 'indexer'...
   collected 0 docs, 0.0 MB
   total 0 docs, 0 bytes
   total 0.007 sec, 0 bytes/sec, 0.00 docs/sec
   ```

7. ## Helpful links
   - [Sphinxsearch Installation Guide](https://sphinxsearch.com/docs/current/installation.html)
   - [Sphinxsearch Configuration Guide](https://sphinxsearch.com/docs/current/conf-indexer.html)

onelinerhub: [How do I run the Sphinxsearch indexer?](https://onelinerhub.com/sphinxsearch/how-do-i-run-the-sphinxsearch-indexer)