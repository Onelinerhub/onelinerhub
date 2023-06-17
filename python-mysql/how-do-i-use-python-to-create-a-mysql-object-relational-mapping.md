# How do I use Python to create a MySQL Object-Relational Mapping?
// plain

Object-Relational Mapping (ORM) is a technique that allows developers to interact with databases using objects. To use Python to create an ORM, the developer must first install the Python package `SQLAlchemy`. This package provides an interface to interact with various database systems, including MySQL.

Once `SQLAlchemy` is installed, the developer must create a database engine. This can be done by providing the connection string to the database. For example, to create a MySQL engine, the following code can be used:

```
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://username:password@hostname/database')
```

Next, the developer must create a `Declarative Base` object, which will be used to define the classes that will interact with the database. The `Declarative Base` must be passed the `engine` created in the previous step.

```
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engine)
```

Finally, the developer must define the classes that will be used to interact with the database. Each class must be a subclass of the `Base` object created in the previous step. For example, to create a table called `users` with columns `id` and `name`, the following code can be used:

```
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
```

Once the classes have been created, the developer can create the database tables by calling the `create_all` method on the `Base` object.

```
Base.metadata.create_all()
```

Finally, the developer can use the classes to interact with the database. For example, to insert a new user into the database, the following code can be used:

```
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

user = User(name='John Doe')
session.add(user)
session.commit()
```

The above code will insert a new user into the `users` table with the name `John Doe`.

### List of Code Parts with Explanation

- `from sqlalchemy import create_engine`: This imports the `create_engine` function from the `sqlalchemy` package, which is used to create a database engine.
- `engine = create_engine('mysql+pymysql://username:password@hostname/database')`: This creates a database engine using the connection string provided.
- `from sqlalchemy.ext.declarative import declarative_base`: This imports the `declarative_base` function from the `sqlalchemy.ext.declarative` package, which is used to create a `Declarative Base` object.
- `Base = declarative_base(engine)`: This creates a `Declarative Base` object using the engine created in the previous step.
- `class User(Base):`: This creates a class called `User` which is a subclass of the `Base` object.
- `__tablename__ = 'users'`: This specifies the name of the table that the class will interact with.
- `id = Column(Integer, primary_key=True)`: This creates a column called `id` in the `users` table with the data type `Integer` and sets it as the primary key.
- `name = Column(String)`: This creates a column called `name` in the `users` table with the data type `String`.
- `Base.metadata.create_all()`: This creates the tables in the database based on the classes created.
- `from sqlalchemy.orm import sessionmaker`: This imports the `sessionmaker` function from the `sqlalchemy.orm` package, which is used to create a `Session` object.
- `Session = sessionmaker(bind=engine)`: This creates a `Session` object using the engine created in the first step.
- `session = Session()`: This creates a `Session` object using the `Session` object created in the previous step.
- `user = User(name='John Doe')`: This creates a `User` object with the name `John Doe`.
- `session.add(user)`: This adds the `User` object to the `Session`.
- `session.commit()`: This commits the changes to the database.

### Relevant Links

- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/13/)
- [SQLAlchemy Tutorial](https://www.tutorialspoint.com/sqlalchemy/index.htm)

onelinerhub: [How do I use Python to create a MySQL Object-Relational Mapping?](https://onelinerhub.com/python-mysql/how-do-i-use-python-to-create-a-mysql-object-relational-mapping)