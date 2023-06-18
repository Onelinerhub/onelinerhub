# How can I create a React.js quiz?
// plain

Creating a React.js quiz can be a great way to test your understanding of the library. Here's how you can do it:

1. Start by creating a React app using `create-react-app` command.

2. Set up the quiz structure in App.js. This will include a title, instructions, and the quiz questions.

```javascript
function App() {
  return (
    <div>
      <h1>React Quiz</h1>
      <p>Answer the following questions to test your React knowledge.</p>
      <ul>
        <li>What is React?</li>
        <li>What is a React component?</li>
        <li>What is the purpose of a React component?</li>
      </ul>
    </div>
  );
}

export default App;
```

3. Create a new component for each question. This component will include a question, answer choices, and a submit button.

```javascript
import React from "react";

class Question1 extends React.Component {
  render() {
    return (
      <div>
        <h3>What is React?</h3>
        <input type="radio" name="q1" value="1" />A library for building user interfaces <br />
        <input type="radio" name="q1" value="2" />A programming language <br />
        <input type="radio" name="q1" value="3" />A framework for web development <br />
        <button>Submit</button>
      </div>
    );
  }
}

export default Question1;
```

4. Create a state object to store the answers. This will be used to keep track of the user's answers.

```javascript
this.state = {
  answers: {
    q1: null,
    q2: null,
    q3: null
  }
};
```

5. Create a function to handle the submit button. This will update the state with the user's answers.

```javascript
handleSubmit = (e) => {
  e.preventDefault();
  this.setState({
    answers: {
      q1: e.target.q1.value,
      q2: e.target.q2.value,
      q3: e.target.q3.value
    }
  });
};
```

6. Finally, create a function to check the answers and display the results.

```javascript
checkAnswers = () => {
  const { answers } = this.state;
  let correct = 0;
  if (answers.q1 === "1") {
    correct++;
  }
  if (answers.q2 === "2") {
    correct++;
  }
  if (answers.q3 === "3") {
    correct++;
  }
  alert(`You got ${correct} out of 3 correct!`);
};
```

Now you have a working React quiz!

## Helpful links

- [Create React App](https://create-react-app.dev/)
- [React Components](https://reactjs.org/docs/components-and-props.html)

onelinerhub: [How can I create a React.js quiz?](https://onelinerhub.com/reactjs/how-can-i-create-a-react-js-quiz)