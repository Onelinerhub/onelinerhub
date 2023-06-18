# How do I upgrade Sphinx Search?
// plain

1. The first step is to install the latest version of Sphinx Search. This can be done using the command line:
```
$ sudo apt-get install sphinxsearch
```

2. Once the installation is complete, you will need to configure Sphinx Search. This can be done by editing the Sphinx configuration file, located in `/etc/sphinxsearch/sphinx.conf`.

3. After the configuration is complete, you will need to rebuild the index. This can be done with the following command:
```
$ indexer --all
```

4. Once the index is rebuilt, you will need to start the Sphinx Search daemon. This can be done with the following command:
```
$ searchd
```

5. Finally, you will need to test the installation to make sure everything is working correctly. This can be done with the following command:
```
$ search <query>
```

6. If the query returns the expected results, then the upgrade is complete.

7. For more information on upgrading Sphinx Search, please refer to the [Sphinx Search Documentation](http://sphinxsearch.com/docs/current.html).

onelinerhub: [How do I upgrade Sphinx Search?](https://onelinerhub.com/sphinxsearch/how-do-i-upgrade-sphinx-search)