# How do I use PostgreSQL with Maven?
// plain

Maven is a build automation tool for Java projects. PostgreSQL is an open source relational database. It is possible to use PostgreSQL with Maven.

The first step is to add the PostgreSQL JDBC driver dependency to the project's pom.xml file. This can be done by adding the following lines to the ```<dependencies>``` section:

```xml
<dependency>
  <groupId>org.postgresql</groupId>
  <artifactId>postgresql</artifactId>
  <version>9.4-1206-jdbc42</version>
</dependency>
```

The next step is to configure the database connection. This can be done by adding the following lines to the ```<properties>``` section of the pom.xml file:

```xml
<properties>
  <db.driver>org.postgresql.Driver</db.driver>
  <db.url>jdbc:postgresql://localhost:5432/mydb</db.url>
  <db.username>postgres</db.username>
  <db.password>password</db.password>
</properties>
```

The last step is to add the code to access the database. This can be done by adding the following lines to the code:

```java
String url = System.getProperty("db.url");
String username = System.getProperty("db.username");
String password = System.getProperty("db.password");

Class.forName(System.getProperty("db.driver"));
Connection connection = DriverManager.getConnection(url, username, password);
```

This code will create a connection to the database using the parameters configured in the pom.xml file.

## Helpful links

- [Maven](https://maven.apache.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [PostgreSQL JDBC Driver](https://jdbc.postgresql.org/)

onelinerhub: [How do I use PostgreSQL with Maven?](https://onelinerhub.com/postgresql/how-do-i-use-postgresql-with-maven)