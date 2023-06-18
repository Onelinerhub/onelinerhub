# How do I add an icon to my ReactJS project?
// plain

Adding an icon to a ReactJS project is a simple task. To do so, you must first install the [React-Icons package](https://react-icons.github.io/react-icons/). After that, you can import the icon you want to use in your project.

For example, you can import the `FaCoffee` icon from the `react-icons/fa` package like this:

```javascript
import { FaCoffee } from 'react-icons/fa';
```

Then you can render the icon in your component like this:

```javascript
render() {
  return (
    <div>
      <FaCoffee />
    </div>
  );
}
```

The output of this code will be a coffee icon.

You can also customize the icon by adding props. For example, you can change the size and color of the icon by adding the `size` and `color` props like this:

```javascript
<FaCoffee size={30} color="red" />
```

This will render a red coffee icon with size 30.

You can find more information about React-Icons [here](https://react-icons.github.io/react-icons/).

onelinerhub: [How do I add an icon to my ReactJS project?](https://onelinerhub.com/reactjs/how-do-i-add-an-icon-to-my-reactjs-project)