# How do I use Sphinx Search to find words using ngram_chars?
// plain

Sphinx Search can be used to find words using ngram_chars. Ngram_chars is a feature that allows Sphinx to index and search words based on their substrings.

For example, the following code block can be used to set up a Sphinx index using ngram_chars:
```
index test
{
    type                    = rt
    path                    = /var/data/test
    ngram_chars             = U+3000..U+2FA1F
    min_prefix_len          = 0
    min_infix_len           = 3
    enable_star             = 1
    expand_keywords         = 1
}
```
This will create an index for the data in the path /var/data/test. It will enable ngram_chars for the range of Unicode characters U+3000..U+2FA1F. It will also set the minimum prefix and infix lengths to 0 and 3 respectively, and enable star and keyword expansion.

When searching with ngram_chars enabled, Sphinx will also look for substrings of the search query. For example, if the search query is "test", Sphinx will also look for "es", "st", and "te".

Here is an example of a Sphinx search query using ngram_chars:
```
SELECT * FROM test WHERE MATCH('@(title,content) test')
```
This query will search the index for the word "test" as well as any substrings of "test".

Here is a list of the parts of the code block and their explanations:
- `index test`: This creates an index called "test".
- `type = rt`: This sets the index type to "rt" (real-time).
- `path = /var/data/test`: This sets the path to the data that will be indexed.
- `ngram_chars = U+3000..U+2FA1F`: This enables ngram_chars for the range of Unicode characters U+3000..U+2FA1F.
- `min_prefix_len = 0`: This sets the minimum prefix length to 0.
- `min_infix_len = 3`: This sets the minimum infix length to 3.
- `enable_star = 1`: This enables star expansion.
- `expand_keywords = 1`: This enables keyword expansion.

Here are some relevant links for more information:
- [Sphinx Documentation - Ngram Chars](https://sphinxsearch.com/docs/current.html#conf-ngram-chars)
- [Sphinx Documentation - Real-Time Indexes](https://sphinxsearch.com/docs/current.html#conf-type)
- [Sphinx Documentation - Star Expansion](https://sphinxsearch.com/docs/current.html#conf-enable-star)
- [Sphinx Documentation - Keyword Expansion](https://sphinxsearch.com/docs/current.html#conf-expand-keywords)

onelinerhub: [How do I use Sphinx Search to find words using ngram_chars?](https://onelinerhub.com/sphinxsearch/how-do-i-use-sphinx-search-to-find-words-using-ngram-chars)