<p align="center"><img src="docs/images/hero.png" alt="Simon Vedder, cloud and cloud-security engineer in Zurich. Azure automation, identity audits, infrastructure as code: unattended OS upgrades, credential rotation, scheduled VM power, privileged-role audits, app-registration audits, least-privilege RBAC." width="100%"></p>

<p align="center">
  <a href="https://simonvedder.com"><img src="https://img.shields.io/badge/blog-simonvedder.com-FF6B35" alt="Blog"></a>
  <a href="https://simonvedder.com/tools/"><img src="https://img.shields.io/badge/tools-simonvedder.com%2Ftools-0078D4" alt="Tools"></a>
  <a href="https://www.linkedin.com/in/simon-vedder/"><img src="https://img.shields.io/badge/LinkedIn-simon--vedder-0A66C2?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
</p>

**Cloud & cloud-security engineer near Zurich.** I work across Azure platform engineering and cloud
security, with a focus on Microsoft Entra ID, RBAC and infrastructure-as-code. Some of the tools below
run tedious Azure work unattended, the others audit what a tenant actually allows. All of them are
tested against live tenants before they're written up at **[simonvedder.com](https://simonvedder.com)**,
and each one with a page there comes with deploy steps and a command reference.

## Tools

<!-- TOOLS:START -->
| Tool | Kind | What it does | Ships as |
|---|---|---|---|
| **[Least Privilege Studio](https://github.com/simon-vedder/least-privilege-studio)** | Web app | Pick the actions you need for Azure RBAC or Entra ID and get the narrowest roles that cover them — or just paste in your Terraform. | Browser |
| **[RiskyRolesAnalyzer](https://github.com/simon-vedder/risky-roles-analyzer)** | Audit | One script, one HTML report: every privileged Azure RBAC and Entra role assignment, including the ones behind groups, custom roles and dormant apps | PowerShell · [page](https://simonvedder.com/tools/risky-roles-analyzer/) |
| **[AppLifecycleAnalyzer](https://github.com/simon-vedder/app-lifecycle-analyzer)** | Audit | One script, one HTML report: every Entra ID app registration with its credentials, their expiry dates and when the app was last used | PowerShell · [page](https://simonvedder.com/tools/app-lifecycle-analyzer/) |
| **[AzureInPlaceUpgrade](https://github.com/simon-vedder/azure-vm-inplace-upgrade)** | Automation | Name a VM and a target, and it goes from Windows Server 2016, 2019 or 2022 to 2025 in place — nobody logs on | Module + Bicep (preview) · [page](https://simonvedder.com/tools/azure-inplace-upgrade/) · [Gallery](https://www.powershellgallery.com/packages/AzureInPlaceUpgrade) |
| **[AzureVMCredentialRotation](https://github.com/simon-vedder/azure-vm-credential-rotation)** | Automation | Rotates local admin passwords and SSH keys on the Azure VMs that Windows LAPS and Entra login cannot reach | PowerShell · [page](https://simonvedder.com/tools/azure-vm-credential-rotation/) · [Gallery](https://www.powershellgallery.com/packages/AzureVMCredentialRotation) |
| **[VM Power Management](https://github.com/simon-vedder/azure-vm-power-management)** | Automation | Start and stop VMs on a schedule without keeping a list of machines — the tag names the schedule | Runbook (preview) · [page](https://simonvedder.com/tools/vm-power-management/) · [Gallery](https://www.powershellgallery.com/packages/AzureVMPowerManagement) |
| **[Deallocate on Activity Log](https://github.com/simon-vedder/bicep/tree/main/automations/deallocate-based-on-activitylog)** | Automation | A guest shutdown stops the OS and keeps billing the VM — an activity-log alert and a Logic App deallocate it within minutes | Logic App · [page](https://simonvedder.com/tools/deallocate-on-activity-log/) |
| **[NSG Gap Finder](https://github.com/simon-vedder/powershell/blob/main/scripts/audits/AzVM-NSGSecurityAudit.ps1)** | Audit | Azure VMs whose NIC or subnet has no network security group attached | PowerShell |
| **[VM OS Audit](https://github.com/simon-vedder/powershell/blob/main/scripts/audits/AzVM-OSInventory.ps1)** | Audit | The operating systems actually running, including the forgotten ones | PowerShell |
| **[Golden Image Builder](https://github.com/simon-vedder/bicep/tree/main/automations/build-golden-image)** | Blueprint | Gallery, image definitions, build templates and the monthly schedule | Bicep |
| **[Self-Service VM Ordering](https://github.com/simon-vedder/azure-vm-selfservice-order)** | Blueprint | A web form, a Logic App and a queue instead of portal access — VMs and AVD session hosts | ARM |

Claude Code skills in **[skills](https://github.com/simon-vedder/skills)**: `azure-cost` · `azure-rbac-advisor` · `azure-updates`
<!-- TOOLS:END -->

Collections: **[powershell](https://github.com/simon-vedder/powershell)** ·
**[terraform-azure](https://github.com/simon-vedder/terraform-azure)** · **[bicep](https://github.com/simon-vedder/bicep)** ·
**[arm](https://github.com/simon-vedder/arm)** · **[kql](https://github.com/simon-vedder/kql)**

## Recently shipped

<!-- RELEASES:START -->
- [AzureVMPowerManagement 0.1.5-preview](https://github.com/simon-vedder/azure-vm-power-management/releases/tag/v0.1.5) · [azure-vm-power-management](https://github.com/simon-vedder/azure-vm-power-management) · 2026-09-13
- [AzureVMCredentialRotation 0.4.1](https://github.com/simon-vedder/azure-vm-credential-rotation/releases/tag/v0.4.1) · [azure-vm-credential-rotation](https://github.com/simon-vedder/azure-vm-credential-rotation) · 2026-09-08
- [AzureInPlaceUpgrade 0.3.1-preview](https://github.com/simon-vedder/azure-vm-inplace-upgrade/releases/tag/v0.3.1) · [azure-vm-inplace-upgrade](https://github.com/simon-vedder/azure-vm-inplace-upgrade) · 2026-09-07
- [RiskyRolesAnalyzer 0.1.0-preview](https://github.com/simon-vedder/risky-roles-analyzer/releases/tag/v0.1.0) · [risky-roles-analyzer](https://github.com/simon-vedder/risky-roles-analyzer) · 2026-09-07
- [least-privilege-studio v2.0.0](https://github.com/simon-vedder/least-privilege-studio/releases/tag/v2.0.0) · [least-privilege-studio](https://github.com/simon-vedder/least-privilege-studio) · 2026-05-20
<!-- RELEASES:END -->

## Upstream

<!-- UPSTREAM:START -->
- [maester365/maester #2130](https://github.com/maester365/maester/pull/2130): feat(entra): add MT.1198 app registration certificate lifetime test · open
- [Azure/Community-Policy #541](https://github.com/Azure/Community-Policy/pull/541): Add policies: Deploy the Microsoft Entra login extensions to Azure VMs · open
<!-- UPSTREAM:END -->

## Latest posts

<!-- BLOG:START -->
- [Azure in-place upgrades don’t have to stay manual](https://simonvedder.com/azure-in-place-upgrades-dont-have-to-stay-manual/) · 2026-09-10
- [169.254.169.254: The Cloud Metadata Endpoint](https://simonvedder.com/169-254-169-254-the-cloud-metadata-endpoint/) · 2026-08-27
- [There’s no built-in policy for Entra VM login](https://simonvedder.com/theres-no-built-in-policy-for-entra-vm-login/) · 2026-07-26
<!-- BLOG:END -->

More at [simonvedder.com](https://simonvedder.com) · [LinkedIn](https://www.linkedin.com/in/simon-vedder/)

<sub>The tools table, releases, upstream list and posts are regenerated every Monday by
[a workflow](.github/workflows/refresh-readme.yml) from the tools catalogue, GitHub and the blog.</sub>
