# How to install Sphinxsearch on Ubuntu?
// plain

1. Install Sphinxsearch on Ubuntu by running the following command in the terminal:
```
sudo apt-get install sphinxsearch
```
2. After the installation is complete, you can start the Sphinxsearch service by running the following command:
```
sudo service sphinxsearch start
```
3. To configure Sphinxsearch, you need to edit the configuration file located at `/etc/sphinxsearch/sphinx.conf`.
4. You can also use the `searchd` command to control the Sphinxsearch service. For example, to stop the service, you can run the following command:
```
searchd --stop
```
5. For more information about installing and configuring Sphinxsearch on Ubuntu, please refer to the [official documentation](http://sphinxsearch.com/docs/current.html).

group: install

onelinerhub: [How to install Sphinxsearch on Ubuntu?](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-on-ubuntu)