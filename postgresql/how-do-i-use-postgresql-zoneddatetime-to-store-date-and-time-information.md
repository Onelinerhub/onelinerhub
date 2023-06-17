# How do I use PostgreSQL ZonedDateTime to store date and time information?
// plain

PostgreSQL's `ZonedDateTime` type is a convenient way to store date and time information. It is a combination of a `LocalDateTime` and a `ZoneId` that specifies the timezone associated with the date and time.

For example, to store the date and time for the current moment in the UTC timezone, you can use the following code:

```
import java.time.ZonedDateTime;

ZonedDateTime nowUtc = ZonedDateTime.now(ZoneId.of("UTC"));
System.out.println(nowUtc);
```

This will output something like `2020-04-27T22:30:05.142345Z[UTC]`.

You can also use `ZonedDateTime` to create a `LocalDateTime` object in a specific timezone, or to convert an existing `LocalDateTime` object to a different timezone. For example:

```
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.ZonedDateTime;

LocalDateTime now = LocalDateTime.now();
ZonedDateTime nowUtc = ZonedDateTime.of(now, ZoneId.of("UTC"));
System.out.println(nowUtc);
```

This will output something like `2020-04-27T22:30:05.142345Z[UTC]`.

To store a `ZonedDateTime` in a PostgreSQL database, you can use the `timestamptz` data type. For example:

```
INSERT INTO my_table (created_at) VALUES (timestamptz '2020-04-27T22:30:05.142345Z[UTC]');
```

## Helpful links

* [JavaTime PostgreSQL](https://www.postgresql.org/docs/current/datatype-datetime.html)
* [ZonedDateTime JavaDocs](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/time/ZonedDateTime.html)

onelinerhub: [How do I use PostgreSQL ZonedDateTime to store date and time information?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-zoneddatetime-to-store-date-and-time-information)