# How do I create a QR code using ReactJS?
// plain

Creating a QR code using ReactJS is relatively simple. The following example code block will create a QR code using the [qrcode.react](https://www.npmjs.com/package/qrcode.react) package.

```
import React from 'react';
import QRCode from 'qrcode.react';

function App() {
  return (
    <QRCode
      value="https://www.example.com"
      size={128}
      bgColor="#FFFFFF"
      fgColor="#000000"
    />
  );
}

export default App;
```

This code will generate a 128x128 pixel white background QR code with a black foreground and the value of the QR code being `https://www.example.com`.

The code is made up of the following parts:

- `import React from 'react'`: imports the React library.
- `import QRCode from 'qrcode.react'`: imports the QRCode library.
- `function App()`: creates a React component.
- `<QRCode`: creates the QR code element.
- `value="https://www.example.com"`: sets the value of the QR code.
- `size={128}`: sets the size of the QR code.
- `bgColor="#FFFFFF"`: sets the background color of the QR code.
- `fgColor="#000000"`: sets the foreground color of the QR code.
- `/>`: closes the QR code element.
- `export default App;`: exports the React component.

For more information on creating QR codes using ReactJS, see the [qrcode.react](https://www.npmjs.com/package/qrcode.react) package documentation.

onelinerhub: [How do I create a QR code using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-create-a-qr-code-using-reactjs)