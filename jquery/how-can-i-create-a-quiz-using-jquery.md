# How can I create a quiz using jQuery?
// plain

Creating a quiz using jQuery is relatively simple and can be done in a few steps.

First, create the HTML structure for the quiz. This includes the questions and answer choices.

```
<div id="quiz">
  <h2>Quiz</h2>
  <div id="question1">
    <h3>Question 1</h3>
    <ul>
      <li><input type="radio" name="question1" value="A">A</li>
      <li><input type="radio" name="question1" value="B">B</li>
      <li><input type="radio" name="question1" value="C">C</li>
      <li><input type="radio" name="question1" value="D">D</li>
    </ul>
  </div>
</div>
```

Next, create the jQuery functions to handle the quiz logic. This includes functions to check the answers and to display the results.

```
function checkAnswer() {
  if ($('input[name=question1]:checked').val() == 'A') {
    alert('Correct!');
  } else {
    alert('Incorrect!');
  }
}

function showResult() {
  alert('You scored ' + score + ' out of 10!');
}
```

Then, create event listeners to handle user input. This includes listeners to respond when the user selects an answer and when they submit their quiz.

```
$('input[name=question1]').change(checkAnswer);
$('#submit-quiz').click(showResult);
```

Finally, add some styling to the quiz to make it look nice.

```
#quiz h2 {
  font-size: 1.5em;
  font-weight: bold;
}

#quiz ul {
  list-style-type: none;
}
```

No output.

### Explanation of Code Parts

- `$('input[name=question1]').change(checkAnswer);`: This jQuery statement adds an event listener for when the user selects an answer to the first question. When the user selects an answer, the `checkAnswer()` function will be called.
- `$('#submit-quiz').click(showResult);`: This jQuery statement adds an event listener for when the user submits their quiz. When the user submits the quiz, the `showResult()` function will be called.
- `#quiz h2 { font-size: 1.5em; font-weight: bold; }`: This CSS statement styles the quiz title to be bold and 1.5 times the normal font size.

### Relevant Links

- [jQuery](https://jquery.com/)
- [jQuery Events](https://api.jquery.com/category/events/)
- [CSS Selectors](https://www.w3schools.com/cssref/css_selectors.asp)

onelinerhub: [How can I create a quiz using jQuery?](https://onelinerhub.com/jquery/how-can-i-create-a-quiz-using-jquery)