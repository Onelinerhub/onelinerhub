# How do I zoom in and out of an image using ReactJS?
// plain

Zooming in and out of an image using ReactJS can be done by using the `react-zoom-pan-pinch` library. It provides a `PinchZoomPan` component which takes an image as a prop and allows you to zoom in and out of the image.

```
import React from 'react';
import { PinchZoomPan } from 'react-zoom-pan-pinch';

const App = () => {
  return (
    <PinchZoomPan
      image="https://example.com/image.jpg"
    />
  );
};

export default App;
```

The `PinchZoomPan` component takes several props which can be used to customize the behavior of the zoom and pan. These props include:

* `minScale`: The minimum scale to which the image can be zoomed (defaults to `1`).
* `maxScale`: The maximum scale to which the image can be zoomed (defaults to `3`).
* `pinchThreshold`: The threshold for detecting a pinch gesture (defaults to `0.5`).
* `panThreshold`: The threshold for detecting a pan gesture (defaults to `0.25`).

For more information on using the `PinchZoomPan` component, see the [documentation](https://github.com/davidguandev/react-zoom-pan-pinch).

onelinerhub: [How do I zoom in and out of an image using ReactJS?](https://onelinerhub.com/reactjs/how-do-i-zoom-in-and-out-of-an-image-using-reactjs)