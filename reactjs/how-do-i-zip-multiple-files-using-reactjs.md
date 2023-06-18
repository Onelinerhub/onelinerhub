# How do I zip multiple files using ReactJS?
// plain

Zipping multiple files using ReactJS is a fairly simple task. The following example code block demonstrates how to do so using the `zip-it-up` library:
```
import zipItUp from 'zip-it-up'

const files = [
  'file1.txt',
  'file2.txt',
  'file3.txt'
]

zipItUp(files, 'myZipFile.zip')
```
This will create a zip file named `myZipFile.zip` containing all three files.

The code above is composed of the following parts:
1. Importing the `zip-it-up` library.
2. Creating an array of files to be zipped.
3. Calling the `zipItUp` function with the files array and the desired zip file name.

For more information about zipping files using ReactJS, see the following links:
- [zip-it-up](https://www.npmjs.com/package/zip-it-up)
- [ReactJS Zip Tutorial](https://www.codementor.io/@brijmcq/reactjs-zip-tutorial-5qyhq1gq3)

onelinerhub: [How do I zip multiple files using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-zip-multiple-files-using-reactjs)