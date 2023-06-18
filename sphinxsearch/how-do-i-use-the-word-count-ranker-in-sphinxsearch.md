# How do I use the word count ranker in SphinxSearch?
// plain

The Word Count Ranker in SphinxSearch is a ranking algorithm that assigns a score to each document based on how many times a given word appears in it. To use the Word Count Ranker, you must first set the `ranker` option in your SphinxSearch configuration file to `wordcount`:

```
ranker = wordcount
```

Once this is set, the ranker will be used when performing a search. The algorithm works by counting the number of times a given word appears in each document, and then assigning a score to each document based on that count.

For example, if you have two documents, one with the word "cat" appearing three times, and one with the word "cat" appearing five times, the document with the word "cat" appearing five times will be given a higher score.

The Word Count Ranker also supports advanced features such as boosting and field weights. Boosting allows you to increase the relevance of certain words by increasing their weight in the ranking algorithm. Field weights allow you to assign different weights to different fields in your documents, so that words in certain fields are given more importance than words in other fields.

Here is an example of how to use boosting and field weights in the Word Count Ranker:

```
ranker = wordcount
field_weights = title^2, content^1
boost = cat^3
```

In this example, the word "cat" will be given three times the weight of other words, and the title field will be given twice the weight of the content field.

## Helpful links

- [SphinxSearch Documentation](http://sphinxsearch.com/docs/current.html)
- [Word Count Ranker Documentation](http://sphinxsearch.com/docs/current.html#conf-ranker)
- [Boosting and Field Weights Documentation](http://sphinxsearch.com/docs/current.html#conf-field-weights)

onelinerhub: [How do I use the word count ranker in SphinxSearch?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-word-count-ranker-in-sphinxsearch)