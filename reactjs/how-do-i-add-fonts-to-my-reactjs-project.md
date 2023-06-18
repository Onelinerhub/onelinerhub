# How do I add fonts to my ReactJS project?
// plain

Adding fonts to a ReactJS project is simple. The following example will show you how to do it.

First, you need to install the `typeface-package` package which will allow you to add fonts to your project. To do this, run the following command in your project directory:
```
npm install typeface-package
```

Once the package is installed, you will need to import the font into your project. To do this, add the following line of code to your React component:
```
import 'typeface-package/index.css';
```

Next, you will need to add the font to your CSS file. To do this, add the following line of code to your CSS file:
```
@import url('https://fonts.googleapis.com/css?family=Roboto');
```

Finally, you will need to add the font to your HTML elements. To do this, add the following line of code to the HTML element:
```
style={{ fontFamily: 'Roboto' }}
```

Now your React project is set up to use the font.

## Code explanation

1. `npm install typeface-package` - to install the typeface package
2. `import 'typeface-package/index.css';` - to import the font into your project
3. `@import url('https://fonts.googleapis.com/css?family=Roboto');` - to add the font to your CSS file
4. `style={{ fontFamily: 'Roboto' }}` - to add the font to your HTML elements

## Helpful links
- [typeface-package](https://www.npmjs.com/package/typeface-package)
- [Google Fonts](https://fonts.google.com/)

onelinerhub: [How do I add fonts to my ReactJS project?](https://onelinerhub.com/reactjs/how-do-i-add-fonts-to-my-reactjs-project)