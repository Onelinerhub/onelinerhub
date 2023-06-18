# How can I install and configure Sphinxsearch on Debian 11?
// plain

1. Install Sphinxsearch using the following command: ```sudo apt-get install sphinxsearch```.
2. Create the Sphinx configuration file ```/etc/sphinxsearch/sphinx.conf``` and set the necessary parameters.
3. Index the data using the command ```indexer --all```.
4. Start the search daemon using the command ```searchd```.
5. Test the search daemon using the command ```search test``` and check the output ```found 2 matches of 2 words```.
6. Connect to the search daemon using the command ```mysql -h127.0.0.1 -P9306``` and check the output ```Welcome to the SphinxQL interface...```.
7. Integrate Sphinxsearch with your application.

## Helpful links

- [Sphinx Documentation](http://sphinxsearch.com/docs/current.html)
- [Debian 11 Installation Guide](https://www.debian.org/releases/bullseye/amd64/install.en.html)

onelinerhub: [How can I install and configure Sphinxsearch on Debian 11?](https://onelinerhub.com/sphinxsearch/how-can-i-install-and-configure-sphinxsearch-on-debian---)