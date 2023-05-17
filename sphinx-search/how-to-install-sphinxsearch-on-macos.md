# How to install Sphinxsearch on MacOS?
// plain

1. Download the latest version of Sphinxsearch from [Sphinxsearch website](http://sphinxsearch.com/downloads/).
2. Unpack the downloaded archive and open the terminal in the directory with the unpacked files.
3. Run the following command to install Sphinxsearch:
```
./configure
make
sudo make install
```
4. After the installation is complete, you can start the search daemon by running the following command:
```
searchd --config /path/to/sphinx.conf
```
5. To verify that Sphinxsearch is running, you can use the following command:
```
ps aux | grep searchd
```
The output should look something like this:
```
root      1234  0.0  0.0  2434456   8372   ??  Ss   11:34AM   0:00.01 searchd --config /path/to/sphinx.conf
```

group: install

onelinerhub: [How to install Sphinxsearch on MacOS?](https://onelinerhub.com/sphinx-search/how-to-install-sphinxsearch-on-macos)