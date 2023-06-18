# How can I use Sphinxsearch with Django?
// plain

Sphinxsearch can be used with Django to create powerful search functionality for your web application.

To use Sphinxsearch with Django, you will need to install the Django-Sphinx package. This package provides a model-based interface to Sphinxsearch, allowing you to use it in your Django projects.

Once installed, you can use the Django-Sphinx API to access and query Sphinxsearch. Here is an example of how to use the API to search for a keyword:

```python
from django_sphinx_db.models import SphinxSearch

# Search for the keyword 'foo'
results = SphinxSearch.query('foo')
```

The `results` variable will contain a `SphinxResultSet` object, which can be used to access the search results. The `SphinxResultSet` object contains methods such as `get_total_found()` and `get_results()` which can be used to access the search results.

You can also use the Django-Sphinx API to create and manage indexes, add documents to an index, and perform other operations.

For more information on how to use Sphinxsearch with Django, see the [Django-Sphinx documentation](https://django-sphinx.readthedocs.io/en/latest/).

onelinerhub: [How can I use Sphinxsearch with Django?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinxsearch-with-django)