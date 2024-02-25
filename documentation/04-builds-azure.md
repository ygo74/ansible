# Azure DevOps Build

## Create A Service Principal for Ansible Automation

### Create Service Principal with Az Commands 

```powershell
# ----------------------------------------------------
# Create Application Ansible-Automation
# ----------------------------------------------------
New-AzADApplication -DisplayName Ansible-Automation -IdentifierUris http://azure/ansible
$application = Get-AzureRmADApplication -DisplayName Ansible-Automation

# ----------------------------------------------------
# Create Service principal Ansible-Automation
# ----------------------------------------------------
Add-Type -Assembly System.Web
$password = [System.Web.Security.Membership]::GeneratePassword(16,3)
$securePassword = ConvertTo-SecureString -Force -AsPlainText -String $password
New-AzADServicePrincipal -ApplicationId $application.ApplicationId -Password $securePassword

$svcPrincipal = Get-AzADServicePrincipal -DisplayName Ansible-Automation
$svcPrincipal |fl *

# ----------------------------------------------------
# Assign permission for Ansible-Automation
# ----------------------------------------------------
$subscriptionId=Get-AzSubscription | select-object -ExpandProperty Id
New-AzRoleAssignment  -ObjectId $svcPrincipal.Id  -RoleDefinitionName Contributor -Scope "/subscriptions/$subscriptionId"

```

### Create Service Principal with MESF Module 
```powershell
# ----------------------------------------------------
# Create Application and its service principal Ansible-Automation
# ----------------------------------------------------
Import-Module MESF_Azure -Force
Enable-MESF_AzureDebug
Register-MESFAzureServicePrincipal -Application Ansible-Automation -ResetPassword

# ----------------------------------------------------
# Synchronize Azure vault with local information
# ----------------------------------------------------
Sync-MESFAzureVault -VaultName mesfVault -Name Ansible-Automation -ObjectType ServicePrincipal

# ----------------------------------------------------
# Assign permission for Ansible-Automation
# ----------------------------------------------------
$subscriptionId=Get-AzSubscription | select-object -ExpandProperty Id
$svcPrincipal = Get-AzADServicePrincipal -DisplayName Ansible-Automation
New-AzRoleAssignment  -ObjectId $svcPrincipal.Id  -RoleDefinitionName Contributor -Scope "/subscriptions/$subscriptionId"

```

