# How do I use PostgreSQL's interval data type?
// plain

PostgreSQL's interval data type is used to store and manipulate time intervals. It is useful when you need to store a length of time as a single value, such as the duration of a movie.

An interval value is specified using the syntax `INTERVAL 'value' unit`, where `value` is the length of the interval and `unit` is the unit of time such as `DAY`, `MONTH`, `YEAR` etc. For example, `INTERVAL '3 DAYS'` represents a length of time of 3 days.

Let's look at an example of how to use the interval data type. We will create a table called `movies` with a column called `duration` that stores the duration of the movie in days as an interval.

```
CREATE TABLE movies (
  title VARCHAR(50),
  duration INTERVAL
);
```

We can then insert a movie into the table with a duration of 3 days:

```
INSERT INTO movies (title, duration)
VALUES ('The Godfather', INTERVAL '3 DAYS');
```

We can also retrieve the duration of the movie by using a `SELECT` statement:

```
SELECT title, duration
FROM movies;
```

## Output example

```
title          | duration
--------------+------------
The Godfather | 3 days
```

## Code explanation

* `CREATE TABLE` - used to create a table with a column of type `INTERVAL`
* `INSERT INTO` - used to insert a movie with a duration as an interval
* `SELECT` - used to retrieve the duration of a movie

## Helpful links
* [PostgreSQL Documentation - Interval Data Type](https://www.postgresql.org/docs/current/datatype-datetime.html#DATATYPE-INTERVAL)

onelinerhub: [How do I use PostgreSQL's interval data type?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-s-interval-data-type)