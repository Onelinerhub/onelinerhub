# How do I install SphinxSearch on Ubuntu 20.04?
// plain

1. Download the latest version of SphinxSearch from [sphinxsearch.com](https://sphinxsearch.com/downloads/).
2. Extract the files in the downloaded archive:
```
tar -xzvf sphinx-<version>.tar.gz
```
3. Change directory to the extracted folder:
```
cd sphinx-<version>
```
4. Configure the build:
```
./configure --prefix=/usr/local/sphinx
```
5. Compile and install SphinxSearch:
```
make
sudo make install
```
6. Start the searchd daemon:
```
/usr/local/sphinx/bin/searchd --config /path/to/sphinx.conf
```
7. Verify the installation by using the SphinxQL client:
```
/usr/local/sphinx/bin/sphinxql -h127.0.0.1 -p9306
```

## Code explanation
**
- `tar -xzvf sphinx-<version>.tar.gz`: Extract the files in the downloaded archive.
- `cd sphinx-<version>`: Change directory to the extracted folder.
- `./configure --prefix=/usr/local/sphinx`: Configure the build.
- `make`: Compile the source code.
- `sudo make install`: Install SphinxSearch.
- `/usr/local/sphinx/bin/searchd --config /path/to/sphinx.conf`: Start the searchd daemon.
- `/usr/local/sphinx/bin/sphinxql -h127.0.0.1 -p9306`: Verify the installation by using the SphinxQL client.

**Output (if any) of Example Code:**
None.

onelinerhub: [How do I install SphinxSearch on Ubuntu 20.04?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-ubuntu------)