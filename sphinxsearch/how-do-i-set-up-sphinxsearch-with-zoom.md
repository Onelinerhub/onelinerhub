# How do I set up SphinxSearch with Zoom?
// plain

1. Install SphinxSearch:
   ```
   sudo apt-get install sphinxsearch
   ```
2. Configure SphinxSearch:
   - Create a configuration file in `/etc/sphinxsearch/sphinx.conf`
   - Add the following lines to the configuration file:
     ```
     source src1
     {
       type = mysql
       sql_host = localhost
       sql_user = root
       sql_pass =
       sql_db   = zoom
       sql_query = SELECT id, name FROM zoom_table
     }
     ```
     - `src1`: The name of the source
     - `type`: The type of the source, in this case, MySQL
     - `sql_host`: The hostname of the database server
     - `sql_user`: The user to connect to the database
     - `sql_pass`: The password to connect to the database
     - `sql_db`: The name of the database
     - `sql_query`: The SQL query to index the data
3. Index the data:
   ```
   indexer --all
   ```
4. Start the searchd daemon:
   ```
   searchd --config /etc/sphinxsearch/sphinx.conf
   ```
5. Test the search:
   ```
   search --config /etc/sphinxsearch/sphinx.conf "query"
   ```
   Output:
   ```
   id  name
   1   Zoom
   ```
6. Integrate SphinxSearch with Zoom:
   - Use the SphinxSearch API to query the index
   - Use the results to display the relevant data in the Zoom application
7. For more information:
   - [SphinxSearch Documentation](https://sphinxsearch.com/docs/current.html)
   - [Integrating SphinxSearch with Zoom](https://www.example.com/integrating-sphinxsearch-with-zoom)

onelinerhub: [How do I set up SphinxSearch with Zoom?](https://onelinerhub.com/sphinxsearch/how-do-i-set-up-sphinxsearch-with-zoom)