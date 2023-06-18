# How do I install Sphinxsearch on Linux?
// plain

1. Download the latest version of Sphinxsearch from the [Sphinx website](https://sphinxsearch.com/downloads/).
2. Extract the package to a directory of your choice.
3. Change to the extracted directory and run the following command to configure and install Sphinxsearch:
```
./configure
make
make install
```
4. Create a configuration file for Sphinxsearch. The example below assumes the configuration file is named `sphinx.conf`:
```
index test1
{
  type = plain
  path = /var/data/test1
  source = test1_src
  morphology = stem_en
  min_word_len = 3
  charset_type = utf-8
  charset_table = 0..9, A..Z->a..z, _, a..z, U+410..U+42F->U+430..U+44F, U+430..U+44F
}

source test1_src
{
  type = mysql
  sql_host = localhost
  sql_user = root
  sql_pass =
  sql_db = test1
  sql_query_pre = SET NAMES utf8
  sql_query = \
    SELECT id, group_id, UNIX_TIMESTAMP(date_added) AS date_added, title, content \
    FROM documents
}
```
5. Start the Sphinxsearch daemon with the following command:
```
searchd --config sphinx.conf
```
6. Verify that Sphinxsearch is running by connecting to its daemon with the following command:
```
search --config sphinx.conf
```
7. You can now use Sphinxsearch with your application.

onelinerhub: [How do I install Sphinxsearch on Linux?](https://onelinerhub.com/sphinxsearch/how-do-i-install-sphinxsearch-on-linux)