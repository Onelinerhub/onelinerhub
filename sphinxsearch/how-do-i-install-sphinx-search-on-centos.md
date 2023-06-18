# How do I install Sphinx Search on CentOS?
// plain

1. Install the `epel-release` package:
    ```
    sudo yum install epel-release
    ```

2. Install `Sphinx` and `MySQL` development packages:
    ```
    sudo yum install sphinx sphinx-devel mysql-devel
    ```

3. Create a Sphinx configuration file:
    ```
    cp /usr/local/etc/sphinx.conf.dist /usr/local/etc/sphinx.conf
    ```

4. Edit the configuration file to set the database connection details:
    ```
    vi /usr/local/etc/sphinx.conf
    ```

5. Start the Sphinx daemon:
    ```
    /usr/local/bin/searchd --config /usr/local/etc/sphinx.conf
    ```

6. Verify that the daemon is running:
    ```
    ps ax | grep searchd
    ```
    Output:
    ```
    2415 ?        S      0:00 /usr/local/bin/searchd --config /usr/local/etc/sphinx.conf
    ```

7. Index the database:
    ```
    /usr/local/bin/indexer --config /usr/local/etc/sphinx.conf --all
    ```

## Helpful links
- [Sphinx Documentation](https://sphinxsearch.com/docs/)
- [CentOS Documentation](https://wiki.centos.org/Documentation)

onelinerhub: [How do I install Sphinx Search on CentOS?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinx-search-on-centos)