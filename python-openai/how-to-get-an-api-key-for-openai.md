# How to get an API key for OpenAI?
// plain

OpenAI provides an API key to access its services. To get an API key, you need to create an OpenAI account and register your application.

To create an OpenAI account, go to https://openai.com/ and click on the "Sign Up" button.

Once you have created an account, you can register your application by going to the "My Applications" page.

Once your application is registered, you will be provided with an API key.

You can use the API key to access OpenAI services. For example, you can use the API key to access the OpenAI Gym environment.

```
import gym

env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

env.close()
```

## Output example

```
...
[Cart 0.00e+00 -0.00e+00  0.00e+00  0.00e+00]
[Cart 0.00e+00 -1.00e-02  0.00e+00  1.00e-02]
[Cart 0.00e+00 -2.00e-02  0.00e+00  2.00e-02]
...
```

## Helpful links
- [OpenAI](https://openai.com/)
- [OpenAI Gym](https://gym.openai.com/)

onelinerhub: [How to get an API key for OpenAI?](https://onelinerhub.com/python-openai/how-to-get-an-api-key-for-openai)