# How to Create a Table

```sql
CREATE TABLE tb1(ID INT DEFAULT 1,NAME VARCHAR(20) NOT NULL,AGE INT NOT NULL,PRIMARY KEY (ID));
```

- tbl  - **Name** of the table.
- ID   - **Integer datatype** and provides a default value for a column (i.e ID=1) when none is specified.It is defined as a ***PRIMARY KEY*** which can be useful to uniquely identify each record in the table.
- NAME - **Character dataype** that is varying within 20 bytes and a **mandatory** field to be entered (i.e NOT NULL).
- AGE  - **Integer datatype** and a **mandatory** field to be entered (i.e NOT NULL).
