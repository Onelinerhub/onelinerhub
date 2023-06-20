# How can I use Docker to deploy a Vue.js application?
// plain

1. Create a `Dockerfile` to define the environment for your Vue.js application.
    ```
    # Use node image as base
    FROM node:latest

    # Create app directory
    WORKDIR /usr/src/app

    # Install app dependencies
    COPY package*.json ./
    RUN npm install

    # Bundle app source
    COPY . .

    # Expose port
    EXPOSE 8080

    # Run app
    CMD ["npm", "run", "serve"]
    ```
2. Build the Docker image using the `Dockerfile`:
    ```
    docker build -t my-vue-app .
    ```
3. Run the Docker container:
    ```
    docker run -p 8080:8080 my-vue-app
    ```

The above steps will allow you to deploy your Vue.js application using Docker. `Dockerfile` defines the environment for the application. It uses `node:latest` as the base image, creates the application directory, installs the dependencies, bundles the source code, exposes port 8080 and runs the application using `npm run serve` command. Then, `docker build` command is used to build the Docker image and `docker run` command is used to run the container.

## Helpful links

- [Docker Documentation](https://docs.docker.com/)
- [Vue.js Docker Guide](https://vuejs.org/v2/cookbook/dockerize-vuejs-app.html)

onelinerhub: [How can I use Docker to deploy a Vue.js application?](https://onelinerhub.com/vue.js/how-can-i-use-docker-to-deploy-a-vue-js-application)