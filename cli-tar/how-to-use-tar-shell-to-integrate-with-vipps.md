# How to use tar shell to integrate with Vipps?
// plain

**Using tar shell to integrate with Vipps**

Tar shell can be used to integrate with Vipps in order to facilitate payments. This integration allows you to process payments securely and quickly. Here is an example of how to use tar shell to integrate with Vipps:

1. Install the Vipps library with the following command:

```
npm install vipps-node-sdk
```

2. Create a new file and import the Vipps library with the following code:

```
const Vipps = require('vipps-node-sdk');
```

3. Initialize the Vipps library with the following code:

```
const vipps = new Vipps(
  {
    clientId: 'your-client-id',
    secret: 'your-secret',
    subkey: 'your-subkey',
    environment: 'production',
  },
);
```

4. Make a call to the Vipps API with the following code:

```
vipps.payments.authorize({
  orderId: 'your-order-id',
  amount: 'your-amount',
  callbackUrl: 'your-callback-url',
});
```

5. Handle the response from the Vipps API with the following code:

```
vipps.payments.on('payment_authorized', (data) => {
  // Handle the response from the Vipps API
});
```

6. Finally, capture the payment with the following code:

```
vipps.payments.capture({
  orderId: 'your-order-id',
});
```

This is how you can use tar shell to integrate with Vipps.

## Helpful links
- [Vipps Node SDK](https://github.com/vippsas/vipps-node-sdk)
- [Vipps Payments API Documentation](https://vippsas.github.io/vipps-developers-docs/)

onelinerhub: [How to use tar shell to integrate with Vipps?](https://onelinerhub.com/cli-tar/how-to-use-tar-shell-to-integrate-with-vipps)