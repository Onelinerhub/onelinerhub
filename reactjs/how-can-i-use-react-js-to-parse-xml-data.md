# How can I use React.js to parse XML data?
// plain

React.js can be used to parse XML data using the `xmldom` library. The following example code uses `xmldom` to parse an XML string and print out the node name of each node in the XML string:

```
const xmldom = require('xmldom');

const xmlString = `
  <root>
    <node1>
      <child1 />
    </node1>
    <node2>
      <child2 />
    </node2>
  </root>
`;

const doc = new xmldom.DOMParser().parseFromString(xmlString);

const nodes = doc.getElementsByTagName('*');

for (let i = 0; i < nodes.length; i++) {
  console.log(nodes[i].nodeName);
}
```

## Output example

```
root
node1
child1
node2
child2
```

In the example code, the `xmldom` library is imported (1), an XML string is defined (2), the XML string is parsed into a DOM object (3), all nodes in the DOM object are retrieved (4), and the node name of each node is printed out (5).

React.js can also be used to parse XML data using the `xml2js` library. The `xml2js` library can be used to parse XML data into JavaScript objects.

## Helpful links

- [xmldom](https://www.npmjs.com/package/xmldom)
- [xml2js](https://www.npmjs.com/package/xml2js)

onelinerhub: [How can I use React.js to parse XML data?](https://onelinerhub.com/reactjs/how-can-i-use-react-js-to-parse-xml-data)