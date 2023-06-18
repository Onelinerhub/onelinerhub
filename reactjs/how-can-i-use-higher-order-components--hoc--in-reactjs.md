# How can I use Higher Order Components (HOC) in ReactJS?
// plain

Higher Order Components (HOC) are a powerful tool for reusing component logic in React. HOCs are a pattern that emerged from React’s compositional nature. They are a function that takes a component and returns a new component.

An example of a HOC is `withCounter` which takes a component and returns a new component that has a counter.

```
const withCounter = (WrappedComponent) => {
  class WithCounter extends React.Component {
    constructor(props) {
      super(props)
      this.state = {
        count: 0
      }
    }

    incrementCount = () => {
      this.setState(prevState => {
        return { count: prevState.count + 1 }
      })
    }

    render() {
      return <WrappedComponent
        count={this.state.count}
        incrementCount={this.incrementCount}
        {...this.props}
      />
    }
  }
  return WithCounter
}
```

In this example, the HOC `withCounter` takes a component `WrappedComponent` as an argument and returns a new component `WithCounter`. The `WithCounter` component has a state of `count` which is initialized to 0 and an `incrementCount` function which increments the `count` state. The `WithCounter` component then renders `WrappedComponent` with the `count` and `incrementCount` functions as props.

## Helpful links
- [React Higher Order Components Explained](https://blog.bitsrc.io/react-higher-order-components-explained-cf2e1f9e7d9f)
- [React Higher Order Components Tutorial](https://www.robinwieruch.de/react-higher-order-components)

onelinerhub: [How can I use Higher Order Components (HOC) in ReactJS?](https://onelinerhub.com/reactjs/how-can-i-use-higher-order-components--hoc--in-reactjs)