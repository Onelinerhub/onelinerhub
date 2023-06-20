# How can I create a Vue.js quiz?
// plain

Creating a Vue.js quiz is a great way to test your users' knowledge of the framework. To get started, you can use the [Vue CLI](https://cli.vuejs.org/) to generate a new Vue project. Once you have your project set up, you can start adding components and code for your quiz.

For example, you can create a `Question` component that takes a `question` prop and renders the question text. This component can also render a `form` containing the answer choices.

```html
<template>
  <div>
    <h3>{{ question }}</h3>
    <form>
      <input type="radio" value="A" />
      <label>Answer A</label>
      <br />
      <input type="radio" value="B" />
      <label>Answer B</label>
      <br />
      <input type="radio" value="C" />
      <label>Answer C</label>
    </form>
  </div>
</template>

<script>
export default {
  props: ["question"],
};
</script>
```

You can also create a `Quiz` component that takes an array of `questions` and renders each one in a loop. This component can also keep track of the user's answers and display the results when they are done.

```html
<template>
  <div>
    <h1>Quiz</h1>
    <div v-for="(question, index) in questions" :key="index">
      <Question :question="question" />
    </div>
    <button @click="submitQuiz()">Submit Quiz</button>
  </div>
</template>

<script>
import Question from "./Question";

export default {
  components: {
    Question,
  },
  props: ["questions"],
  data() {
    return {
      answers: [],
    };
  },
  methods: {
    submitQuiz() {
      // Submit answers and display results
    },
  },
};
</script>
```

Finally, you can create a `QuizApp` component that renders the `Quiz` component with your questions.

```html
<template>
  <div>
    <Quiz :questions="questions" />
  </div>
</template>

<script>
import Quiz from "./Quiz";

export default {
  components: {
    Quiz,
  },
  data() {
    return {
      questions: [
        {
          question: "What is the name of the Vue.js CLI?",
          answers: ["Vue CLI", "Vuex CLI", "Vue Router CLI"],
        },
        {
          question: "What is the syntax for creating a component?",
          answers: ["Vue.component()", "Vue.createComponent()", "Vue.makeComponent()"],
        },
      ],
    };
  },
};
</script>
```

Once you have all the components set up, you can serve the app with `npm run serve` and test it out. With a few lines of code, you can create a fully functional Vue.js quiz.

onelinerhub: [How can I create a Vue.js quiz?](https://onelinerhub.com/vue.js/how-can-i-create-a-vue-js-quiz)