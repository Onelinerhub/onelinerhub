# How can I use cli sed to select an Azure subscription?
// plain

Using the Azure CLI, you can select an Azure subscription with the `az account set` command. This command requires the subscription ID as an argument. For example:

```
az account set --subscription <subscription-id>
```

This command will set the active subscription to the one provided.

## Code explanation


* `az account set`: This is the command to set the active subscription.
* `--subscription`: This is an argument to the `az account set` command, which specifies the subscription ID to set as active.
* `<subscription-id>`: This is the ID of the subscription to set as active.

For more information, see the [Azure CLI documentation](https://docs.microsoft.com/en-us/cli/azure/reference-index?view=azure-cli-latest).

onelinerhub: [How can I use cli sed to select an Azure subscription?](https://onelinerhub.com/cli-sed/how-can-i-use-cli-sed-to-select-an-azure-subscription)