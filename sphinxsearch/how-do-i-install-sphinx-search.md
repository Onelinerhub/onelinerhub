# How do I install Sphinx Search?
// plain

1. Download the latest version of Sphinx Search from [sphinxsearch.com](https://sphinxsearch.com/downloads/).
2. Extract the downloaded package and `cd` into its directory:
```
tar -xzvf sphinx-2.2.11-release.tar.gz
cd sphinx-2.2.11-release
```
3. Run `./configure` with the desired options:
```
./configure --prefix=/usr/local/sphinx --with-mysql
```
4. Compile and install Sphinx Search:
```
make
make install
```
5. Create a configuration file:
```
cp /usr/local/sphinx/etc/sphinx.conf.dist /usr/local/sphinx/etc/sphinx.conf
```
6. Start the searchd daemon:
```
/usr/local/sphinx/bin/searchd --config /usr/local/sphinx/etc/sphinx.conf
```
7. Now you can connect to the searchd daemon and issue queries:
```
/usr/local/sphinx/bin/search --config /usr/local/sphinx/etc/sphinx.conf "test"
```

## Output example

```
Sphinx 2.2.11-id64-release (rel22-r5006)
Copyright (c) 2001-2015, Andrew Aksyonoff
Copyright (c) 2008-2015, Sphinx Technologies Inc (http://sphinxsearch.com)

using config file '/usr/local/sphinx/etc/sphinx.conf'...
index 'test1': query 'test ': returned 0 matches of 0 total in 0.000 sec

```

onelinerhub: [How do I install Sphinx Search?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinx-search)