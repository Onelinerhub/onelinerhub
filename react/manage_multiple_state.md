# How to make reusable React Hooks to manage multiple state

```JSX
// save file as /hook/useMultiState.js (or .ts)

import { useReducer } from "react"

const useMultiState = (initialStates) => {
  const reducer = (states, payload) => ({ ...states, ...payload })
  return useReducer(reducer, initialStates)
}
export default useMultiState

// usage
const [state, setState] = useMultiState(initialStates)
```

- state - reactive variable to access current state
- setState - method to update state
- initialStates - object that will be our initial state

## Example Usage
```JSX
import React, {useEffect} from 'react'
import useMultiState from './hook/useMultiState';

const App = ()=>{
// init all state with our hook
const [state, setState] = useMultiState({
    name: 'Bro',
    email: 'valid@mail.com',
    phone: '08123455',
    isValid: false
})

// just example for update state on component mount
useEffect(() => {
    // update only state you want to updae
    setState({
        isValid: true,
        phone: '+628123456789'
    })

}, [])

// render the state on paragraph
return (
    <p>Name: {state.name}</p>
    <p>Email: {state.email}</p>
    <p>Phone: {state.phone}</p>
    <p>Status: {state.isValid?'valid':'invalid'}</p>
)
export default App
```

PS: Use this custom hook only for manage multiple state. If you just handle one or two states, use default `useState` hook instead