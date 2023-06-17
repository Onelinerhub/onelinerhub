# How can I convert XML data to JSON using jQuery?
// plain

This can be done by using jQuery's `$.parseXML()` function, which takes an XML string as an argument and returns a DOM object. The resulting object can then be converted to JSON using the `$.parseJSON()` function.

## Example code

```
// Create an XML string
var xmlString = '<note><to>Tove</to><from>Jani</from><heading>Reminder</heading><body>Don't forget me this weekend!</body></note>';

// Parse the XML string
var xmlDoc = $.parseXML(xmlString);

// Convert the XML DOM object to JSON
var jsonString = $.parseJSON(xmlDoc);
```
## Output example

```
{
  "note": {
    "to": "Tove",
    "from": "Jani",
    "heading": "Reminder",
    "body": "Don't forget me this weekend!"
  }
}
```

## Code explanation

* `$.parseXML()` - Takes an XML string as an argument and returns a DOM object.
* `$.parseJSON()` - Takes a DOM object as an argument and returns a JSON string.

## Helpful links
* [jQuery.parseXML()](https://api.jquery.com/jQuery.parseXML/)
* [jQuery.parseJSON()](https://api.jquery.com/jQuery.parseJSON/)

onelinerhub: [How can I convert XML data to JSON using jQuery?](https://onelinerhub.com/jquery/how-can-i-convert-xml-data-to-json-using-jquery)