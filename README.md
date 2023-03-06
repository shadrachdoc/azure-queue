## This project requires the following configurations and setup:

# Azure Container Registry (ACR)
ACR needs to be configured
Service connection needs to be created for ACR
Service connection name: ACR for acr service
# Azure Kubernetes Service (AKS)
AKS needs to be configured
Service connection needs to be created for AKS
Service connection name: dev
# Storage Account
Storage account and Queue need to be created
Queue name: incoming
Please embed the storage account service connection with the git source code.

Create a pipeline using the 'azure-pipeline.yaml' file and trigger the pipeline to initiate the deployment process.
