# How do I install SphinxSearch on GitHub?
// plain

1. To install SphinxSearch on GitHub, first clone the repository from the official SphinxSearch GitHub page:
```
git clone https://github.com/sphinxsearch/sphinx.git
```
2. Then, navigate to the cloned repository directory:
```
cd sphinx
```
3. Next, configure the build with the following command:
```
./configure
```
4. After the build is successfully configured, compile the source code with the following command:
```
make
```
5. Finally, install SphinxSearch with the following command:
```
sudo make install
```
6. After installation is complete, you can start the SphinxSearch daemon with the following command:
```
searchd --config sphinx.conf
```
7. You can also test the installation by running the following command:
```
search test
```

## Code explanation
**

* `git clone https://github.com/sphinxsearch/sphinx.git` - clones the SphinxSearch repository from the official GitHub page
* `cd sphinx` - navigates to the cloned repository directory
* `./configure` - configures the build
* `make` - compiles the source code
* `sudo make install` - installs SphinxSearch
* `searchd --config sphinx.conf` - starts the SphinxSearch daemon
* `search test` - tests the installation

**## Helpful links**

* [SphinxSearch GitHub Page](https://github.com/sphinxsearch/sphinx)
* [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)

onelinerhub: [How do I install SphinxSearch on GitHub?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-github)