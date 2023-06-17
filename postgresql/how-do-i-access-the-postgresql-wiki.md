# How do I access the PostgreSQL wiki?
// plain

1. To access the PostgreSQL wiki, you can go to the [PostgreSQL Wiki](https://wiki.postgresql.org/wiki/Main_Page) page.
2. You can also access the wiki using the `psql` command line. To do so, enter the following command:
```
psql -U postgres -c "\l"
```
This will list all the databases associated with the `postgres` user.
3. You can then enter the `\w` command to get the list of available wiki pages. This will provide a list of all the available wiki pages and their descriptions.
4. You can then use the `\g` command to access a specific wiki page. For example, to access the page for the `CREATE TABLE` command, enter the following command:
```
\g CREATE TABLE
```
This will open the page for the `CREATE TABLE` command.
5. You can also access the wiki using a web browser. To do so, go to the [PostgreSQL Wiki](https://wiki.postgresql.org/wiki/Main_Page) page and search for the page you are interested in.
6. Once you have found the page you are looking for, you can click on the link to open it.
7. Finally, you can also access the PostgreSQL wiki using the `pg_wiki` command line tool. To do so, enter the following command:
```
pg_wiki <wiki_page_name>
```
This will open the page for the specified wiki page.

## Helpful links
- [PostgreSQL Wiki](https://wiki.postgresql.org/wiki/Main_Page)
- [pg_wiki Command Line Tool](https://www.postgresql.org/docs/current/app-pg-wiki.html)

onelinerhub: [How do I access the PostgreSQL wiki?](https://onelinerhub.com/postgresql/how-do-i-access-the-postgresql-wiki)