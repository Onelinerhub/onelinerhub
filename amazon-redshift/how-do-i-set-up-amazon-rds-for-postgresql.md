# How do I set up Amazon RDS for PostgreSQL?
// plain

1. Create an Amazon Web Services (AWS) account and log into the AWS Management Console.
2. Navigate to the Amazon Relational Database Service (RDS) page and click on the “Create Database” button.
3. Select PostgreSQL as the engine type and choose the desired version.
4. Configure the required settings such as DB instance size, storage type, etc.
5. Create a master username and password for the database.
6. Click on the “Create Database” button.
7. Once the database instance is created, you can connect to it using the provided endpoint and credentials.

Example code to connect to the database:
```
import psycopg2

conn = psycopg2.connect(host="<endpoint>", database="<dbname>", user="<username>", password="<password>")
```

No output.

## Code explanation

- `import psycopg2`: imports the `psycopg2` library which provides the necessary functions to connect to PostgreSQL.
- `conn = psycopg2.connect(host="<endpoint>", database="<dbname>", user="<username>", password="<password>")`: establishes a connection to the PostgreSQL database using the provided endpoint, database name, username and password.

## Helpful links
- [Amazon RDS for PostgreSQL](https://aws.amazon.com/rds/postgresql/)
- [Connecting to an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToInstance.html)

onelinerhub: [How do I set up Amazon RDS for PostgreSQL?](https://onelinerhub.com/amazon-redshift/how-do-i-set-up-amazon-rds-for-postgresql)