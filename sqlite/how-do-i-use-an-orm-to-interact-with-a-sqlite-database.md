# How do I use an ORM to interact with a SQLite database?
// plain

An ORM (Object Relational Mapper) is a tool used to interact with a database, such as a SQLite database. It allows you to map objects in your application to tables in the database, and allows for easy manipulation of the data.

Here is an example of how to use an ORM to interact with a SQLite database:

```
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///my_database.db', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

Base.metadata.create_all(engine)
```

This code creates a `User` class which is mapped to the `users` table in the `my_database.db` SQLite database. We can then use this class to easily interact with the database. For example, to create a new user in the database:

```
user = User(username='John', password='password123')
session.add(user)
session.commit()
```

This code creates a new `User` object and adds it to the database.

## Code explanation

- `create_engine`: creates an engine which is used to connect to the database
- `declarative_base`: creates a base class which is used for mapping classes to tables
- `Column`: creates a column in the table
- `create_all`: creates the tables in the database
- `add`: adds a new object to the database
- `commit`: commits the changes to the database

## Helpful links
- [SQLAlchemy Quick Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [SQLite Tutorial](https://www.sqlitetutorial.net/)

onelinerhub: [How do I use an ORM to interact with a SQLite database?](https://onelinerhub.com/sqlite/how-do-i-use-an-orm-to-interact-with-a-sqlite-database)