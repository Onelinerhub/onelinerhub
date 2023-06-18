# How do I install SphinxSearch on Debian?
// plain

1. Download and install SphinxSearch from the official website:
    ```
    wget http://sphinxsearch.com/files/sphinx-2.2.11-release.tar.gz
    tar -xzvf sphinx-2.2.11-release.tar.gz
    ```
2. Change the working directory to the extracted folder:
    ```
    cd sphinx-2.2.11-release
    ```
3. Configure and compile the source code:
    ```
    ./configure
    make
    ```
4. Install SphinxSearch:
    ```
    make install
    ```
5. Add SphinxSearch to the system path:
    ```
    export PATH=$PATH:/usr/local/sphinx/bin
    ```
6. Start the SphinxSearch daemon:
    ```
    searchd
    ```
7. To verify the installation, run the `search` command and you should see the following output:
    ```
    search --help
    Sphinx 2.2.11-id64-release (r5161)
    Copyright (c) 2001-2018, Andrew Aksyonoff
    Copyright (c) 2008-2016, Sphinx Technologies Inc (http://sphinxsearch.com)
    ```

## Helpful links
- [SphinxSearch Official Website](http://sphinxsearch.com)
- [SphinxSearch Installation Guide](http://sphinxsearch.com/docs/2.2.11/installation.html)

onelinerhub: [How do I install SphinxSearch on Debian?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-debian)