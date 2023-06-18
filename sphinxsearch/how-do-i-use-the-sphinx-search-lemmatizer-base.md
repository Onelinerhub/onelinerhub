# How do I use the Sphinx search lemmatizer_base?
// plain

The Sphinx search lemmatizer_base is a powerful tool for natural language processing (NLP) tasks. It can be used to lemmatize words, which means to reduce them to their root form. This is useful for tasks such as text analysis, where it can help to reduce the size of the dataset and make it easier to work with.

To use the Sphinx search lemmatizer_base, first you need to install the library. This can be done using the pip command:

```
pip install sphinxsearch
```

Once the library is installed, you can use the lemmatizer_base function to lemmatize words. For example, the following code will lemmatize the words "running", "ran" and "run":

```
from sphinxsearch import lemmatizer_base

words = ["running", "ran", "run"]
lemmatized_words = lemmatizer_base(words)

print(lemmatized_words)
```

The output of this code will be:

```
['run', 'run', 'run']
```

The lemmatizer_base function takes a list of strings as input and returns a list of lemmatized words. It works by looking up each word in a dictionary and finding its root form.

The Sphinx search lemmatizer_base is a useful tool for NLP tasks and can help to reduce the size of datasets and make them easier to work with.

## Helpful links

- [Sphinx Search Documentation](https://sphinxsearch.com/docs/current.html)
- [Natural Language Processing with Python](https://www.nltk.org/book/ch02.html)

onelinerhub: [How do I use the Sphinx search lemmatizer_base?](https://onelinerhub.com/sphinxsearch/how-do-i-use-the-sphinx-search-lemmatizer-base)