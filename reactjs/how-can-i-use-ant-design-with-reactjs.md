# How can I use Ant Design with ReactJS?
// plain

Ant Design is a React UI library that provides a set of high-quality components and demos for building rich, interactive user interfaces. It is written in TypeScript and supports the latest version of React (16.8+).

To use Ant Design with React, you need to install the antd package from npm.

```
npm install antd
```

Once you have installed the package, you can import components from antd into your React component.

```
import { Button } from 'antd';
```

You can then use the imported components in your JSX code.

```
<Button type="primary">Click me!</Button>
```

This will render a primary button with the text "Click me!" on the page.

If you want to customize the look and feel of the components, you can use the Ant Design Less variables. You can find the list of Less variables [here](https://github.com/ant-design/ant-design/blob/master/components/style/themes/default.less).

To use the Less variables, you can import the style file into your React component.

```
import 'antd/dist/antd.css';
```

You can then override the Less variables in your own CSS file.

```
@primary-color: #1DA57A;
```

This will change the primary color of the Ant Design components to the color specified.

## Helpful links
- [Ant Design](https://ant.design/)
- [Ant Design React](https://ant.design/docs/react/introduce)
- [Ant Design Less Variables](https://github.com/ant-design/ant-design/blob/master/components/style/themes/default.less)

onelinerhub: [How can I use Ant Design with ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-ant-design-with-reactjs)