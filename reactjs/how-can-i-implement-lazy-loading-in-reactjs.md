# How can I implement lazy loading in ReactJS?
// plain

Lazy loading is a technique used to improve the performance of a React application by only loading the components that are necessary for the current view. To implement lazy loading in ReactJS, you need to use React.lazy and Suspense.

React.lazy allows you to render a dynamic import as a regular component. It takes a function that must call a dynamic import(). This will return a Promise which resolves to a module with a default export containing a React component.

## Example code

```
const OtherComponent = React.lazy(() => import('./OtherComponent'));

function MyComponent() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <OtherComponent />
      </Suspense>
    </div>
  );
}
```

The Suspense component lets you specify what to render while waiting for the component to load. It takes a fallback prop, which can be a React fragment, string, or any other React component.

## Code explanation

1. React.lazy: This is used to render a dynamic import as a regular component.
2. import(): This is used to return a Promise which resolves to a module with a default export containing a React component.
3. Suspense: This is used to specify what to render while waiting for the component to load.
4. fallback: This is used to specify what to render while waiting for the component to load.

## Helpful links
- [React.lazy](https://reactjs.org/docs/code-splitting.html#reactlazy)
- [Suspense](https://reactjs.org/docs/code-splitting.html#suspense)

onelinerhub: [How can I implement lazy loading in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-implement-lazy-loading-in-reactjs)