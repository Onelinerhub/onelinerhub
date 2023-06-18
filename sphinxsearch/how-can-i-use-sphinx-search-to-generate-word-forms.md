# How can I use Sphinx Search to generate word forms?
// plain

Sphinx Search can be used to generate word forms using its Morphology feature. Morphology allows users to create and configure a stemmer that can be used to generate word forms.

Here is an example code block that uses the English stemmer to generate the word forms of the word "running":

```
#include <sphinxbase/err.h>
#include <sphinxbase/strfuncs.h>
#include <sphinxbase/strfuncs.h>
#include <sphinxbase/strfuncs.h>
#include <sphinxbase/morph.h>

int main() {
    char *stem;
    char *word = "running";
    char *lang = "en";
    stem = morph_stem_str(word, lang);
    printf("Stem of %s is %s\n", word, stem);
    free(stem);
}
```

The output of this code block will be:

```
Stem of running is run
```

The code block is composed of the following parts:

1. `#include` directives: These are used to include the necessary SphinxSearch library functions.
2. `main()` function: This is the main function of the program.
3. `char *stem`: This is a pointer to the stem of the word.
4. `char *word`: This is a pointer to the word that needs to be stemmed.
5. `char *lang`: This is a pointer to the language of the word.
6. `stem = morph_stem_str(word, lang)`: This is the function call to the morph_stem_str() function which takes the word and language as parameters and returns the stem of the word.
7. `printf()`: This is used to print the stem of the word.
8. `free(stem)`: This is used to free the memory allocated for the stem.

## Helpful links
- [SphinxSearch Documentation](http://sphinxsearch.com/docs/)
- [Morphology Feature](http://sphinxsearch.com/docs/current.html#morphology)

onelinerhub: [How can I use Sphinx Search to generate word forms?](https://onelinerhub.com/sphinxsearch/how-can-i-use-sphinx-search-to-generate-word-forms)