# How can I use ReactJS to create XSS payloads?
// plain

ReactJS is a JavaScript library used for creating user interfaces. It is often used to create interactive web applications. XSS payloads can be created with ReactJS by using the `dangerouslySetInnerHTML` method. This method allows you to insert HTML into a React component, which can be used to inject malicious JavaScript code.

## Example

```javascript
const xssPayload = <div dangerouslySetInnerHTML={{__html: '<script>alert("XSS!")</script>'}} />
ReactDOM.render(xssPayload, document.getElementById('root'));
```
## Output example

`alert("XSS!")`

The code above creates an XSS payload using ReactJS. It uses the `dangerouslySetInnerHTML` method to insert a `<script>` tag into a React component. When the component is rendered, the script is executed, resulting in an alert message with the text "XSS!".

Parts of the code and their functions:
- `const xssPayload`: declares a variable to hold the XSS payload
- `<div dangerouslySetInnerHTML={{__html: '<script>alert("XSS!")</script>'}} />`: uses the `dangerouslySetInnerHTML` method to insert a `<script>` tag into the React component
- `ReactDOM.render(xssPayload, document.getElementById('root'));`: renders the React component, executing the script and displaying the alert message

## Helpful links
- [React Documentation - dangerouslySetInnerHTML](https://reactjs.org/docs/dom-elements.html#dangerouslysetinnerhtml)
- [MDN Web Docs - Writing Secure JavaScript](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Client-side_web_APIs/Security_considerations)

onelinerhub: [How can I use ReactJS to create XSS payloads?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-xss-payloads)