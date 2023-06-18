# How do I update SphinxSearch on Ubuntu?
// plain

Updating SphinxSearch on Ubuntu is relatively easy. The following steps should be followed:

1. Install SphinxSearch using `sudo apt-get install sphinxsearch`.
2. Stop the running SphinxSearch daemon using `sudo service sphinxsearch stop`.
3. Download the latest version of SphinxSearch from [sphinxsearch.com](https://sphinxsearch.com/downloads/).
4. Unpack the downloaded archive using `tar -xzf sphinx-<version>.tar.gz`
5. Change the working directory to the unpacked directory using `cd sphinx-<version>`.
6. Install the new version of SphinxSearch using `./configure && make && sudo make install`.
7. Start the SphinxSearch daemon using `sudo service sphinxsearch start`.

```
sudo apt-get install sphinxsearch
sudo service sphinxsearch stop
tar -xzf sphinx-<version>.tar.gz
cd sphinx-<version>
./configure && make && sudo make install
sudo service sphinxsearch start
```

## Output example

```
Reading package lists... Done
Building dependency tree
Reading state information... Done
Sphinxsearch is already the newest version (2.2.11-release).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

onelinerhub: [How do I update SphinxSearch on Ubuntu?](https://onelinerhub.com/sphinxsearch/how-do-i-update-sphinxsearch-on-ubuntu)