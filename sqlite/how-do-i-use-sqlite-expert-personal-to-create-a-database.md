# How do I use SQLite Expert Personal to create a database?
// plain

SQLite Expert Personal is a free graphical tool used to manage and create SQLite databases. To create a database using SQLite Expert Personal, follow these steps:

1. Open SQLite Expert Personal and select the "Create Database" option from the File menu.
2. Enter a file name for the database and click "Save" to create the database file.
3. Right-click on the newly created database file and select "New Table" from the menu.
4. Enter a name for the table and click "OK".
5. Add columns to the table by entering the column name, data type, and other properties.
6. Click "Save" to create the table.
7. Repeat steps 3-6 to create additional tables for the database.

## Example code


```
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
```

## Output example


Table `Users` created successfully.

onelinerhub: [How do I use SQLite Expert Personal to create a database?](https://onelinerhub.com/sqlite/how-do-i-use-sqlite-expert-personal-to-create-a-database)