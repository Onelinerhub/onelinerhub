# How can I convert data from a MySQL database to XML using Python?
// plain

Converting data from a MySQL database to XML using Python is a relatively straightforward process.

The following example code will first connect to a MySQL database, query the database for all data in a specified table, and then write the data to an XML file.

```
import mysql.connector
import xml.etree.ElementTree as ET

# Connect to the database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="database"
)

# Create a cursor object
mycursor = mydb.cursor()

# Execute the query
mycursor.execute("SELECT * FROM table")

# Fetch all the rows
rows = mycursor.fetchall()

# Create the root element
root = ET.Element("root")

# Iterate over the rows
for row in rows:
    # Create the child element
    child = ET.SubElement(root, "child")

    # Iterate over the columns
    for col in row:
        # Create the grandchild element
        grandchild = ET.SubElement(child, "grandchild")
        # Set the text of the grandchild element
        grandchild.text = str(col)

# Create an XML file
xml_file = open("output.xml", "w")

# Write the XML tree to the file
xml_file.write(ET.tostring(root).decode())

# Close the XML file
xml_file.close()
```

The code above will generate an XML file named `output.xml` with the following content:

```
<root>
  <child>
    <grandchild>1</grandchild>
    <grandchild>John</grandchild>
    <grandchild>Doe</grandchild>
  </child>
  <child>
    <grandchild>2</grandchild>
    <grandchild>Jane</grandchild>
    <grandchild>Doe</grandchild>
  </child>
</root>
```

The code consists of the following parts:

1. Importing the necessary modules:
    - `mysql.connector` to connect to the MySQL database
    - `xml.etree.ElementTree` to create the XML tree
2. Connecting to the database
3. Creating a cursor object
4. Executing the query
5. Fetching all the rows
6. Creating the root element
7. Iterating over the rows
8. Creating the child element
9. Iterating over the columns
10. Creating the grandchild element
11. Setting the text of the grandchild element
12. Creating an XML file
13. Writing the XML tree to the file
14. Closing the XML file

For more information, see the following links:
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/)
- [ElementTree - XML Processing with Python](https://docs.python.org/2/library/xml.etree.elementtree.html)

onelinerhub: [How can I convert data from a MySQL database to XML using Python?](https://onelinerhub.com/python-mysql/how-can-i-convert-data-from-a-mysql-database-to-xml-using-python)