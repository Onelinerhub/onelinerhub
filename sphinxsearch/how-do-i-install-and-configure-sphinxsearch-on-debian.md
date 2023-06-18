# How do I install and configure Sphinxsearch on Debian?
// plain

1. Install Sphinxsearch on Debian by running `sudo apt-get install sphinxsearch` in the terminal.
2. Create a configuration file for Sphinxsearch in `/etc/sphinxsearch/sphinx.conf`.
3. Configure the file with the following parameters:
    ```
    index test1
    {
        type = plain
        path = /var/lib/sphinxsearch/data/test1
        docinfo = extern
        mlock = 0
        morphology = stem_en, soundex
        min_word_len = 2
        charset_type = utf-8
        charset_table = 0..9, A..Z->a..z, _, a..z, U+C0->U+E7, U+E7->U+C0
    }
    ```
4. Create the data directory for the index `/var/lib/sphinxsearch/data/test1`.
5. Start the Sphinxsearch daemon with `sudo service sphinxsearch start`.
6. Index the data with `indexer --config /etc/sphinxsearch/sphinx.conf --all`.
7. Test the search with `search --config /etc/sphinxsearch/sphinx.conf test`.

## Helpful links
- [Sphinxsearch Installation Guide](http://sphinxsearch.com/docs/current.html#installation)
- [Sphinxsearch Configuration Guide](http://sphinxsearch.com/docs/current.html#conf-overview)

onelinerhub: [How do I install and configure Sphinxsearch on Debian?](https://onelinerhub.com/sphinxsearch/how-do-i-install-and-configure-sphinxsearch-on-debian)