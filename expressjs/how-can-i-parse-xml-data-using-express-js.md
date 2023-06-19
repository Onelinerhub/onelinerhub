# How can I parse XML data using Express.js?
// plain

Parsing XML data using Express.js is possible with the help of the [xml2js](https://www.npmjs.com/package/xml2js) package.

Below is an example code block that parses an XML string and prints the output to the console:

```
const xml2js = require('xml2js');
const xml = `<root>
  <person>
    <name>John</name>
    <age>30</age>
  </person>
</root>`;

const parseString = xml2js.parseString;
parseString(xml, (err, result) => {
  if (err) {
    console.error(err);
  } else {
    console.log(result);
  }
});
```

## Output example

```
{
  root: {
    person: [
      {
        name: [ 'John' ],
        age: [ '30' ]
      }
    ]
  }
}
```

The code above consists of the following parts:
1. `const xml2js = require('xml2js');` - This imports the xml2js package.
2. `const xml = `<root> ... </root>`;` - This defines the XML string to be parsed.
3. `const parseString = xml2js.parseString;` - This retrieves the parseString function from the xml2js package.
4. `parseString(xml, (err, result) => { ... });` - This calls the parseString function to parse the XML string and print the result to the console.

## Helpful links
- [xml2js](https://www.npmjs.com/package/xml2js)
- [Express.js](https://expressjs.com/)

onelinerhub: [How can I parse XML data using Express.js?](https://onelinerhub.com/expressjs/how-can-i-parse-xml-data-using-express-js)