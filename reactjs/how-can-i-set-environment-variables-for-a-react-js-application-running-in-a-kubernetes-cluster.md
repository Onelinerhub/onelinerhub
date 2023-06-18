# How can I set environment variables for a React.js application running in a Kubernetes cluster?
// plain

Environment variables can be set for a React.js application running in a Kubernetes cluster by either setting them as arguments when starting the container, or by setting them as ConfigMaps.

Setting them as arguments when starting the container:

```
kubectl run my-react-app --image=<image_name> --env="MY_VARIABLE_NAME=my_variable_value"
```

Setting them as ConfigMaps:

```
apiVersion: v1
kind: ConfigMap
metadata:
  name: my-react-app-config
data:
  MY_VARIABLE_NAME: my_variable_value
```

Then, you can mount the ConfigMap to the container using the `--volume-mounts` argument when starting the container:

```
kubectl run my-react-app --image=<image_name> --volume-mounts="name=my-react-app-config,mountPath=/etc/config"
```

The environment variables will then be available to the React.js application.

## Helpful links
- https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/
- https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/

onelinerhub: [How can I set environment variables for a React.js application running in a Kubernetes cluster?](https://onelinerhub.com/reactjs/how-can-i-set-environment-variables-for-a-react-js-application-running-in-a-kubernetes-cluster)