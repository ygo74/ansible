# Ansible prerequisites

## Ansible Development environment
Install Python On Windows
Visual Studio code extension :
* ms-python.python

## Python dependencies


## Prerequisites for Azure Build

## Declare Variables
* a Resource Group : AKS
* a Container Registry : mesfContainerRegistry
* a AKS cluster : aksCluster

## Create A Service Principal

### Create Service Principal for Ansible Automation
***Create an application***
```powershell
New-AzureRmADApplication -DisplayName Ansible-Automation -IdentifierUris http://azure/ansible
$application = Get-AzureRmADApplication -DisplayName Ansible-Automation
```

***Create a Service Principal***
```powershell
Add-Type -Assembly System.Web
$password = [System.Web.Security.Membership]::GeneratePassword(16,3)
$securePassword = ConvertTo-SecureString -Force -AsPlainText -String $password
New-AzureRmADServicePrincipal -ApplicationId $application.ApplicationId -Password $securePassword

$svcPrincipal = Get-AzureRmADServicePrincipal -DisplayName Ansible-Automation
$svcPrincipal |fl *
```

***Assign Contributor permission to All the subscription***
```
$subscriptionId=Get-AzureRmSubscription | select-object -ExpandProperty Id
New-AzureRmRoleAssignment  -ObjectId $svcPrincipal.Id  -RoleDefinitionName Contributor -Scope "/subscriptions/$subscriptionId"
```

