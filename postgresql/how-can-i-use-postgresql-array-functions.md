# How can I use PostgreSQL array functions?
// plain

PostgreSQL arrays are powerful functions that allow you to store and manipulate data in an organized way. PostgreSQL array functions can be used to manipulate arrays, such as searching, sorting, and slicing. Here is an example of how to use PostgreSQL array functions:

```
-- Create an array of numbers
CREATE TABLE numbers (num INT[]);

-- Insert some values
INSERT INTO numbers (num) VALUES (ARRAY[1,2,3,4,5]);

-- Sort the array
SELECT ARRAY_SORT(num) FROM numbers;

-- Output
{1,2,3,4,5}
```

The code above creates a table called `numbers` with a single column `num` of type `INT[]`, which is an array of integers. Then, we insert some values into the array and use the `ARRAY_SORT` function to sort the array. The output of the code is an array of sorted numbers.

Other PostgreSQL array functions include:

- `ARRAY_AGG`: Aggregates values into an array
- `ARRAY_APPEND`: Appends a value to the end of an array
- `ARRAY_LENGTH`: Returns the length of an array
- `ARRAY_REMOVE`: Removes a value from an array
- `ARRAY_REVERSE`: Reverses the order of an array

For more information on PostgreSQL array functions, please refer to the [PostgreSQL documentation](https://www.postgresql.org/docs/current/arrays.html).

onelinerhub: [How can I use PostgreSQL array functions?](https://onelinerhub.com/postgresql/how-can-i-use-postgresql-array-functions)