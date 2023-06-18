# How can I use Docker to deploy a React.js application?
// plain

1. To deploy a React.js application using Docker, first you need to create a Dockerfile. This is a text file that contains instructions on how to build your Docker image.

2. The Dockerfile should include commands to install node.js and the dependencies required for your React.js application. For example:

```
FROM node:10
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
```

3. Once the Dockerfile is created, you can build the Docker image with the following command:

```
docker build -t <image-name> .
```

4. After the image is built, you can run the image in a container with the following command:

```
docker run -p 3000:3000 <image-name>
```

5. This will start the container and your React.js application will be available at http://localhost:3000.

6. You can also deploy your application to a cloud service such as Amazon ECS or Google Container Engine.

7. For more information about deploying a React.js application with Docker, see the following links:

* [Dockerizing a React App](https://mherman.org/blog/dockerizing-a-react-app/)
* [Deploying a React App with Docker](https://blog.sourcerer.io/deploying-a-react-app-with-docker-a7b7f812b092)

onelinerhub: [How can I use Docker to deploy a React.js application?](https://onelinerhub.com/reactjs/how-can-i-use-docker-to-deploy-a-react-js-application)