# integration

How do I integrate web3 with Vue.js?
// plain

Integrating web3 with Vue.js is a straightforward process.

First, install the web3.js library:

```
npm install web3
```

Then, import web3 into your Vue component:

```
import Web3 from 'web3'
```

Next, create a web3 instance:

```
const web3 = new Web3(Web3.givenProvider || 'http://localhost:8545')
```

Now, you can use the web3 instance to interact with the Ethereum blockchain. For example, to get the current block number:

```
web3.eth.getBlockNumber()
  .then(console.log)
```

This will output the current block number.

To use web3 in your Vue component, you can add it to the `data` function:

```
data () {
  return {
    web3: null
  }
},
```

Then, in the `mounted` function, you can set the web3 instance:

```
mounted () {
  this.web3 = new Web3(Web3.givenProvider || 'http://localhost:8545')
}
```

Now, you can use the web3 instance anywhere in your Vue component.

## Helpful links
* [Web3.js Documentation](https://web3js.readthedocs.io/en/v1.2.1/)
* [Vue.js Documentation](https://vuejs.org/v2/guide/)

onelinerhub: [integration

How do I integrate web3 with Vue.js?](https://onelinerhub.com/vue.js/integration--how-do-i-integrate-web--with-vue-js)