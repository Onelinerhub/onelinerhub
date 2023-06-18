# How do I add a Sphinx search bar to my website?
// plain

Adding a Sphinx search bar to your website is relatively easy. To do so, you'll need to install the Sphinx search engine on your server and then create a search form on your website.

First, install the Sphinx search engine on your server. You can find the installation instructions [here](http://sphinxsearch.com/docs/current.html).

Then, create a search form on your website. You can use the below example code to create a simple search form:

```
<form action="search.php" method="get">
    <input type="text" name="q" />
    <input type="submit" value="Search" />
</form>
```

The form will send the query to the `search.php` page. To process the search query with Sphinx, you'll need to write some code on the `search.php` page. You can find an example of this code [here](https://www.binarytides.com/sphinx-search-php-mysql/).

Once you have the search form and the `search.php` page set up, your website should be able to process search queries with Sphinx.

onelinerhub: [How do I add a Sphinx search bar to my website?](https://onelinerhub.com/sphinxsearch/how-do-i-add-a-sphinx-search-bar-to-my-website)