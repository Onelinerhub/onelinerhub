# How can I use ReactJS to create a QR code scanner?
// plain

Creating a QR code scanner using ReactJS is relatively straightforward. To get started, you'll need to install the [react-qr-reader](https://www.npmjs.com/package/react-qr-reader) package.

Once the package is installed, you can use the code block below to create the scanner.

```javascript
import React, { useState } from "react";
import QrReader from "react-qr-reader";

function QrScanner() {
  const [result, setResult] = useState("No result");

  const handleScan = (data) => {
    if (data) {
      setResult(data);
    }
  };

  return (
    <div>
      <QrReader
        delay={300}
        onError={(err) => console.log(err)}
        onScan={handleScan}
        style={{ width: "100%" }}
      />
      <p>{result}</p>
    </div>
  );
}

export default QrScanner;
```

This code will create a `QrScanner` component that will render a QR code scanner. When a QR code is scanned, the `handleScan` function will be called with the data from the code, which will then update the `result` state with the data. The `result` state will then be displayed in the `p` tag.

The code has the following parts:

* `import React, { useState } from "react";` - imports the React library and the `useState` hook
* `import QrReader from "react-qr-reader";` - imports the `QrReader` component from the `react-qr-reader` package
* `const [result, setResult] = useState("No result");` - creates a `result` state variable and a function to update it
* `const handleScan = (data) => { ... }` - a function that will be called when a QR code is scanned, it will update the `result` state with the data from the code
* `<QrReader ... />` - renders the QR code scanner
* `<p>{result}</p>` - displays the `result` state

For more information, see the [react-qr-reader](https://www.npmjs.com/package/react-qr-reader) package documentation.

onelinerhub: [How can I use ReactJS to create a QR code scanner?](https://onelinerhub.com/reactjs/how-can-i-use-reactjs-to-create-a-qr-code-scanner)