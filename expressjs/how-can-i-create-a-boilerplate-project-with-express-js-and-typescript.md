# How can I create a boilerplate project with Express.js and TypeScript?
// plain

Creating a boilerplate project with Express.js and TypeScript is easy.

1. First, create a new project directory and navigate into it:

```
mkdir my-project
cd my-project
```

2. Install the npm packages for Express.js and TypeScript:

```
npm install express typescript
```

3. Create a `tsconfig.json` file to configure the TypeScript compiler:

```
{
  "compilerOptions": {
    "target": "es6",
    "module": "commonjs",
    "outDir": "dist",
    "strict": true
  }
}
```

4. Create a `src` directory and an `index.ts` file to contain the Express application code:

```
mkdir src
touch src/index.ts
```

5. In the `index.ts` file, add the code for the Express application:

```ts
import express from "express";

const app = express();

app.get("/", (req, res) => {
  res.send("Hello, world!");
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
```

6. Compile the TypeScript code to JavaScript:

```
tsc
```

7. Finally, start the Express server:

```
node dist/index.js
```

## Output example


```
Server listening on port 3000
```

## Helpful links

- [Express.js](https://expressjs.com/)
- [TypeScript](https://www.typescriptlang.org/)

onelinerhub: [How can I create a boilerplate project with Express.js and TypeScript?](https://onelinerhub.com/expressjs/how-can-i-create-a-boilerplate-project-with-express-js-and-typescript)