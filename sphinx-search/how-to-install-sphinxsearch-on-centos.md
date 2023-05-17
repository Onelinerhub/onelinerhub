# How to install Sphinxsearch on CentOS?
// plain

Sphinxsearch is a full-text search engine that can be installed on CentOS. To install Sphinxsearch on CentOS, follow these steps:

1. Install the EPEL repository:
```
sudo yum install epel-release
```

2. Install Sphinxsearch:
```
sudo yum install sphinx
```

3. Start the Sphinxsearch service:
```
sudo systemctl start searchd
```

4. Check the status of the Sphinxsearch service:
```
sudo systemctl status searchd
```

5. Configure Sphinxsearch:
Edit the configuration file `/etc/sphinx/sphinx.conf` to configure Sphinxsearch.

## Helpful links
- [Sphinxsearch Documentation](http://sphinxsearch.com/docs/current.html)
- [How To Install and Configure Sphinx on CentOS 7](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-sphinx-on-centos-7)

group: install

onelinerhub: [How to install Sphinxsearch on CentOS?](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-on-centos)