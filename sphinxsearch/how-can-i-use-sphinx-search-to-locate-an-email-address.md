# How can I use Sphinx Search to locate an email address?
// plain

Sphinx Search is a powerful open-source search engine that can be used to locate an email address. It can be used to search through text-based documents such as emails, webpages, and PDFs.

To use Sphinx Search to locate an email address, you will need to install the Sphinx Search software. Once installed, you can use the following example code to search for an email address:

```
indexer --config /usr/local/etc/sphinx.conf --all
search -i -q 'email@example.com'
```

This code will search for the email address `email@example.com` in the documents indexed by Sphinx Search. The output of this code will be a list of the documents containing the searched email address.

The code consists of two parts:

1. `indexer --config /usr/local/etc/sphinx.conf --all`: This part of the code is used to index the documents that will be searched.
2. `search -i -q 'email@example.com'`: This part of the code is used to search for the specified email address.

For more information on using Sphinx Search, please refer to the [Sphinx Search documentation](https://sphinxsearch.com/docs/).

onelinerhub: [How can I use Sphinx Search to locate an email address?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-locate-an-email-address)