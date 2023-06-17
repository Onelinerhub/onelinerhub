# How can I use Python and MySQL to generate a PDF?
// plain

Using Python and MySQL you can generate a PDF by first connecting to your MySQL database, executing a query, and then using the results to generate a PDF.

Example code block:
```
# Import libraries
import mysql.connector
import fpdf

# Connect to the MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="mydatabase"
)

# Create a cursor object and execute a query
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")

# Fetch all the results from the query
result = mycursor.fetchall()

# Create a PDF object
pdf = fpdf.FPDF(format='letter')

# Add a page
pdf.add_page()

# Add a table to the PDF
pdf.set_font("Arial", size=12)
col_width = pdf.w / 4
row_height = pdf.font_size

# Create the table header
for i in range(len(mycursor.description)):
    pdf.cell(col_width, row_height, txt=mycursor.description[i][0], border=1)

# Create the table rows
for row in result:
    pdf.ln(row_height)
    for item in row:
        pdf.cell(col_width, row_height, txt=item, border=1)

# Save the PDF
pdf.output("customers.pdf")
```

This code will generate a PDF file called `customers.pdf` with a table containing the data from the `customers` table in the `mydatabase` MySQL database.

Parts of the code and their explanations:
1. `import mysql.connector` and `import fpdf`: The first two lines of the code import the necessary libraries for connecting to the MySQL database and generating the PDF.
2. `mydb = mysql.connector.connect(host="localhost", user="user", passwd="password", database="mydatabase")`: This line of code connects to the MySQL database.
3. `mycursor.execute("SELECT * FROM customers")`: This line of code executes a query to select all the data from the `customers` table in the `mydatabase` database.
4. `pdf = fpdf.FPDF(format='letter')`: This line of code creates a PDF object.
5. `for i in range(len(mycursor.description)): pdf.cell(col_width, row_height, txt=mycursor.description[i][0], border=1)`: This loop creates the header of the table in the PDF.
6. `for row in result: pdf.ln(row_height); for item in row: pdf.cell(col_width, row_height, txt=item, border=1)`: This loop adds the data from the query result to the table in the PDF.
7. `pdf.output("customers.pdf")`: This line of code saves the PDF as `customers.pdf`.

## Helpful links
- [MySQL Connector/Python Documentation](https://dev.mysql.com/doc/connector-python/en/)
- [PyFPDF Documentation](https://pyfpdf.readthedocs.io/en/latest/)

onelinerhub: [How can I use Python and MySQL to generate a PDF?](https://onelinerhub.com/python-mysql/how-can-i-use-python-and-mysql-to-generate-a-pdf)