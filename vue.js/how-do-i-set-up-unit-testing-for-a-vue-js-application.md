# How do I set up unit testing for a Vue.js application?
// plain

Unit testing for a Vue.js application can be set up in several steps.

1. Install the necessary packages with the following command:
```
npm install --save-dev @vue/cli-plugin-unit-jest
```
2. Create the jest configuration file with the following command:
```
vue-cli-service test:e2e
```
3. Create a test file in the `tests` directory. For example:
```
// tests/example.spec.js
import { shallowMount } from '@vue/test-utils'
import HelloWorld from '@/components/HelloWorld.vue'

describe('HelloWorld.vue', () => {
  it('renders props.msg when passed', () => {
    const msg = 'new message'
    const wrapper = shallowMount(HelloWorld, {
      propsData: { msg }
    })
    expect(wrapper.text()).toMatch(msg)
  })
})
```
4. Run the tests with the following command:
```
npm run test:unit
```
5. To view the test results, open the generated `jest_html_reporters.html` file in the `coverage` directory.

For more information on unit testing Vue.js applications, see the following links:
- [Vue Test Utils](https://vue-test-utils.vuejs.org/)
- [Jest](https://jestjs.io/)
- [Vue CLI Unit Testing Guide](https://cli.vuejs.org/guide/unit-testing.html)

onelinerhub: [How do I set up unit testing for a Vue.js application?](https://onelinerhub.com/vue.js/how-do-i-set-up-unit-testing-for-a-vue-js-application)