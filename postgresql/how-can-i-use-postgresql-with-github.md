# How can I use PostgreSQL with GitHub?
// plain

PostgreSQL can be used with GitHub in a few different ways.

The first is by creating a GitHub repository and committing a PostgreSQL database to it. This can be done using the following code block:

```
git init
git add mydatabase.sql
git commit -m "My first commit"
```

The second way is by using GitHub Actions to run PostgreSQL commands. This can be done by creating a workflow file in the `.github/workflows/` directory in the repository and adding the following code block:

```
on: [push]
name: Run PostgreSQL commands
jobs:
  run_postgres:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run PostgreSQL command
        run: psql -U postgres -c 'SELECT * FROM mytable;'
```

The third way is by using the PostgreSQL GitHub Action, which can be used to perform PostgreSQL operations from within a workflow. The following code block shows an example of how to use it:

```
on: [push]
name: Run PostgreSQL commands
jobs:
  run_postgres:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Run PostgreSQL command
        uses: postgres/action@v1
        with:
          host: localhost
          user: postgres
          password: mypassword
          query: SELECT * FROM mytable;
```

The above code will run the `SELECT * FROM mytable;` query on the PostgreSQL database.

In summary, PostgreSQL can be used with GitHub by committing a PostgreSQL database to a repository, using GitHub Actions to run PostgreSQL commands, and using the PostgreSQL GitHub Action.

## Helpful links
- [PostgreSQL GitHub Action](https://github.com/marketplace/actions/postgres-action)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

onelinerhub: [How can I use PostgreSQL with GitHub?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-with-github)