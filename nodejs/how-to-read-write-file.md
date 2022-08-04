# Read/Write File in Nodejs

```javascript
const fs = require('fs');

fs.readFile("./test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

fs.writeFile("./test.txt", "Hello World", (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log("File written successfully!");
});

```
- fs.readFile() - reads file and returns data in callback function
- /test.txt - path of file to read/write
- data - Data read from file
- 'Hello World' - Data to write to file

## Example
```javascript
const fs = require("fs");

fs.readFile("./test.txt", "utf8", (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});

fs.writeFile("./test.txt", "Hello World", (err) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log("File written successfully!");
});
```
```
Hello World
File written successfully!
```


