

## Task List


| Task                           |
|--------------------------------|
| Configure Windows Defender Antivirus Settings |
| Configure Windows Firewall with Advanced Security |
| Manage Local User Accounts     |
| Configure User Account Control (UAC) Levels |
| Configure Encrypting File System (EFS) |
| Manage NTFS Permissions        |
| Configure Local Security Policy|
| Configure Windows Update Settings|
| Configure Password Policies    |






## Task/Objective


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Configure Windows Defender Antivirus Settings | 4.0 Operational Procedures                        |
| Configure Windows Firewall with Advanced Security | 2.0 Security                                   |
| Manage Local User Accounts     | 4.0 Operational Procedures                                        |
| Configure User Account Control (UAC) Levels | 4.0 Operational Procedures                          |
| Configure Encrypting File System (EFS) | 1.0 Operating Systems                                     |
| Manage NTFS Permissions        | 4.0 Operational Procedures                                        |
| Configure Local Security Policy| 2.0 Security                                                     |
| Configure Windows Update Settings| 4.0 Operational Procedures                                      |
| Configure Password Policies    | 4.0 Operational Procedures                                        |

---


# Lab 5: Windows Security Controls

## Getting Started

Before beginning the hands-on tasks, follow these steps to access your virtual lab environment:

1. **Click** the **Start** button in your lab portal to provision the lab environment.
2. **Click** the computer image or "Launch VM" button in the right pane when the lab loads to open the Windows virtual machine window.
3. **Wait** for Windows 11 to finish booting. When you see the lock screen, **double-click** anywhere to reveal the login prompt.
4. **Select** the **Student** account (if prompted).
5. **Login** with the password `P@ssw0rd` (case sensitive).
6. Once logged in, you are ready to begin the lab activities below.

If you encounter any issues starting the lab or logging in, notify your instructor for assistance.

## How to Use This Lab

1. Follow each task in sequence to complete the lab
2. Complete all verification steps for each task
3. Answer the challenge questions to test your understanding
4. Use the troubleshooting section if you encounter any issues

## Introduction

Welcome to this comprehensive hands-on lab focused on Windows Security Controls. In today's digital landscape, where cyber threats are increasingly sophisticated, understanding and implementing robust security measures is not just important—it's absolutely critical. This lab is designed to transform you from a passive user of Windows security features into a confident administrator capable of implementing enterprise-level security configurations.

### Why This Lab Matters

In an era where data breaches and cyber attacks make daily headlines, organizations are investing heavily in security professionals who can protect their systems and data. This lab provides you with the practical, hands-on experience that employers value most. By completing these exercises, you'll develop the skills needed to:

- Protect systems from malware and unauthorized access
- Implement security best practices in real-world scenarios
- Troubleshoot common security issues
- Configure enterprise-level security policies
- Secure sensitive data through encryption and access controls

### Who Benefits From This Lab

This training is specifically designed for:

- **Aspiring IT Security Specialists** looking to build foundational security skills
- **System Administrators** who need to secure Windows environments
- **Help Desk Professionals** who are the first line of defense against security threats
- **Network Administrators** responsible for maintaining secure network access
- **IT Professionals** preparing for CompTIA A+ and Security+ certifications
- **Anyone** who wants to understand how to protect Windows systems in an increasingly dangerous digital world

### What You'll Learn

This lab is structured to take you from fundamental security concepts to advanced configurations. Through hands-on exercises, you'll gain practical experience in:

- **Threat Protection**
  - Configure and optimize Windows Defender Antivirus for maximum protection
  - Implement real-time scanning and cloud-delivered protection
  - Schedule and analyze system scans

- **Network Security**
  - Create and manage Windows Firewall rules for inbound and outbound traffic
  - Configure advanced firewall profiles (Domain, Private, Public)
  - Monitor and troubleshoot firewall activity

- **Access Control**
  - Create and manage local user accounts with appropriate permissions
  - Implement and test User Account Control (UAC) settings
  - Configure password policies and account lockout policies

- **Data Protection**
  - Implement file and folder encryption using EFS
  - Recover encrypted files using recovery certificates
  - Configure BitLocker for full-disk encryption (where applicable)

- **System Hardening**
  - Configure and apply security templates
  - Implement security policies through Local Security Policy
  - Harden system configurations against common attack vectors

- **Maintenance & Monitoring**
  - Configure and manage Windows Update settings
  - Review security logs and event viewer
  - Implement security baselines and compliance checks

By the end of this lab, you'll have the practical skills needed to secure Windows systems in both small business and enterprise environments, making you a valuable asset in any IT security role.

### Real-World Application

The skills you'll acquire in this lab are directly transferable to critical IT security scenarios that professionals face daily:

#### Enterprise Security Implementation
- Deploy and manage security policies across an organization's Windows infrastructure
- Respond to security incidents by analyzing and mitigating threats
- Implement defense-in-depth strategies to protect against evolving cyber threats

#### Compliance and Auditing
- Configure systems to meet industry standards (NIST, CIS, ISO 27001)
- Prepare for security audits by implementing proper controls and documentation
- Ensure compliance with regulations like GDPR, HIPAA, and PCI-DSS

#### Incident Response
- Detect and respond to security breaches using built-in Windows tools
- Analyze security logs to identify suspicious activities
- Implement remediation strategies for compromised systems

#### Security Consulting
- Assess and harden Windows systems for clients
- Provide recommendations for security improvements
- Implement security baselines and best practices

#### IT Administration
- Manage user access and permissions effectively
- Secure sensitive data through encryption and access controls
- Maintain system security through regular updates and monitoring

These practical applications demonstrate how the skills you'll learn are not just theoretical concepts but essential tools for protecting organizations from the growing threat of cyber attacks.

### Certification Alignment

This lab is specifically designed to support CompTIA A+ (220-1102) certification preparation, with direct alignment to the following exam objectives:


## Getting Started

### System Requirements

This lab is provided in a pre-configured virtual lab environment. All necessary software and configurations are already set up for you.

If you'd like to set up a similar environment in your home lab, you would need:

- **Operating System**: Windows 10/11 Professional, Enterprise, or Education edition
- **Processor**: 2-core minimum (4-core recommended)
- **RAM**: 4GB minimum (8GB recommended)
- **Storage**: 100GB free disk space
- **Permissions**: Administrator access
- **Network**: Internet connection for updates and tools

### Lab Environment Setup

### Lab Environment Setup

Your lab environment is pre-configured with all necessary tools and settings. The virtual lab includes:

- A fully updated Windows 11 environment
- Pre-installed security tools and utilities
- Proper user accounts and permissions
- All required network configurations

#### For Reference: Home Lab Setup (Optional)

If you'd like to set up a similar environment in your home lab, you would need to:

1. **Set Up a Test Environment**
   - Create a virtual machine using:
     - VMware Workstation Player/Pro
     - Oracle VirtualBox
     - Hyper-V (included with Windows Pro/Enterprise)
   - Allocate sufficient resources (2+ cores, 4+ GB RAM, 64+ GB storage)

2. **Prepare the System**
   - Install all Windows updates
   - Create a system restore point
   - Set up appropriate user accounts
   - Configure network settings

3. **Install Required Tools**
   - [Microsoft Security Compliance Toolkit](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
   - [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
   - [Nmap](https://nmap.org/download.html) for network scanning
   - Text editor (Notepad++ or VS Code recommended)

### Safety Guidelines

- Work in a non-production environment when possible
- Document all changes made during the lab
- Create restore points before major configuration changes
- Back up important data before starting
- Be cautious with network connectivity in virtual environments

### Lab Structure

- **Estimated Time**: 6-8 hours total
- **Tasks**: 10 main tasks, each 15-45 minutes
- **Approach**:
  - Complete tasks in order
  - Read all instructions before starting
  - Take notes on configurations
  - Verify each step before proceeding

### Getting Help

- Refer to the troubleshooting sections in each task
- Consult the glossary for security terminology
- Review the discussion questions for additional learning
- Check the references section for further reading

Now that your environment is prepared, you're ready to begin with the first task: Configuring Windows Defender Antivirus Settings.

- **1.0 Operating Systems (34% of exam)**
  - 1.7 Given a scenario, apply application installation and configuration concepts
  - 1.8 Explain common OS types and their purposes
  - 1.9 Given a scenario, perform OS installations and upgrades

- **2.0 Security (31% of exam)**
  - 2.1 Summarize the importance of physical security measures
  - 2.2 Explain logical security concepts
  - 2.3 Compare and contrast wireless security protocols and authentication methods
  - 2.4 Given a scenario, detect, remove, and prevent malware using appropriate tools and methods
  - 2.5 Explain common social-engineering attacks, threats, and vulnerabilities
  - 2.6 Given a scenario, manage and configure basic security settings in the Windows OS
  - 2.7 Given a scenario, configure a workstation to meet best practices for security
  - 2.8 Explain common methods for securing mobile and embedded devices
  - 2.9 Given a scenario, use common data destruction and disposal methods
  - 2.10 Given a scenario, configure appropriate security settings on small office/home office (SOHO) wireless and wired networks
  - 2.11 Given a scenario, install and configure browsers and relevant security settings

- **4.0 Operational Procedures (22% of exam)**
  - 4.1 Implement best practices associated with documentation and support systems
  - 4.2 Explain basic change-management best practices
  - 4.3 Implement workstation backup and recovery methods
  - 4.4 Explain common safety procedures
  - 4.5 Explain environmental impacts and local environmental controls
  - 4.6 Explain the importance of prohibited content/activity and privacy, licensing, and policy concepts
  - 4.7 Given a scenario, use proper communication techniques and professionalism
  - 4.8 Identify the basics of scripting
  - 4.9 Given a scenario, use remote access technologies

This comprehensive coverage ensures you'll be well-prepared for the security-related portions of the CompTIA A+ exam while developing practical, job-ready skills.

### Lab Scenario: Securing Acme Corporation's Workstations

**Your Role:** Junior IT Security Specialist  
**Company:** Acme Corporation (Medium-sized financial services firm)  
**Location:** Corporate Headquarters  
**Date:** May 23, 2025

#### Background
Acme Corporation has recently expanded its operations and onboarded 50 new employees. Following a recent security audit, several vulnerabilities were identified in the company's Windows workstations. The audit revealed:

- Inconsistent security configurations across workstations
- Outdated security patches and update policies
- Weak password policies and authentication controls
- Insufficient protection against malware and unauthorized access
- Lack of encryption for sensitive financial data

#### Your Mission
As the newest member of the IT security team, you've been tasked with implementing comprehensive security controls across all Windows workstations. Your manager, the Chief Information Security Officer (CISO), has provided you with the organization's security policy document and expects you to:

1. Implement and verify all security controls outlined in this lab
2. Document all configurations for compliance purposes
3. Provide a summary report of the security posture after implementation
4. Be prepared to explain your security decisions to the audit team

#### Success Criteria
Your work will be considered successful if you can:
- Demonstrate that all workstations meet or exceed the security baseline
- Provide clear documentation of all security configurations
- Successfully defend your security implementation in a mock audit
- Ensure all systems remain functional for end-users

#### Available Resources
- Administrative access to Windows workstations
- Company security policy document

Before beginning this lab, ensure you have the following requirements in place:

#### Hardware Requirements
- A physical or virtual machine running Windows 10/11 Professional, Enterprise, or Education edition
  - Minimum: 2-core processor, 4GB RAM, 64GB free disk space
  - Recommended: 4-core processor, 8GB RAM, 100GB free disk space for better performance
- Internet connectivity for downloading updates and additional tools
- A second test machine or virtual machine (recommended for testing network security settings)




### Software Requirements

- Windows 10/11 with the latest updates installed
- Administrative access to the system
- Virtualization software (if using virtual machines) such as:
  - VMware Workstation Player/Pro
  - Oracle VirtualBox
  - Hyper-V (included with Windows Pro/Enterprise)
- Text editor (Notepad++ or VS Code recommended for better editing experience)

### Required Accounts and Permissions
- Local administrator account credentials
- Microsoft account (optional, for some Windows features)




### Pre-Lab Setup
1. **Create a System Restore Point**
   - Type "Create a restore point" in the Windows search bar
   - Select your system drive and click "Configure..."
   - Enable "Turn on system protection" if not already enabled
   - Click "Create..." to create a new restore point

2. **Disable Automatic Windows Updates Temporarily**
   - Open Settings > Update & Security > Windows Update
   - Click "Advanced options"
   - Pause updates for 7 days (we'll re-enable this during the lab)

3. **Download Required Tools**
   - [Microsoft Security Compliance Toolkit](https://www.microsoft.com/en-us/download/details.aspx?id=55319)
   - [Sysinternals Suite](https://docs.microsoft.com/en-us/sysinternals/downloads/sysinternals-suite)
   - [Nmap](https://nmap.org/download.html) (for network scanning)




### Knowledge Prerequisites
- Basic understanding of Windows operating system concepts
- Familiarity with Windows Command Prompt and PowerShell
- Basic networking concepts (IP addressing, ports, protocols)
- Understanding of fundamental security principles




### Safety Precautions
⚠️ **Important:** Some exercises involve making system changes that could affect system stability or security. It's strongly recommended to:
- Perform these exercises in a non-production environment
- Use a virtual machine when possible
- Have a backup of important data
- Document all changes made during the lab


## Lab Task Overview

| Task | Description |
| ---- | ----------- |
| Windows Firewall Configuration | Configured Windows Firewall with Advanced Security, created custom rules, and managed network profiles |
| User Account Management | Created and managed local user accounts, implemented password policies, and managed group memberships |
| Data Protection | Implemented BitLocker for full-disk encryption and EFS for file-level encryption |
| File System Security | Configured NTFS and shared folder permissions, set inheritance, and managed access control lists |
| Windows Update | Managed update settings, configured maintenance windows, and verified update status |
| Security Policies | Implemented local security policies, configured audit policies, and reviewed security logs |
| Windows Security Center | Monitored system security status and configured real-time protection settings |
| Security Best Practices | Applied security baselines and implemented security recommendations |
| Troubleshooting | Addressed common security-related issues and verified security configurations |
| Command Line Security Tools | Utilized PowerShell and command-line tools for security management |

## Task List

| Task |
|--------------------------------|
| Configure Windows Defender Antivirus Settings |
| Configure Windows Firewall with Advanced Security |
| Manage Local User Accounts |
| Configure User Account Control (UAC) Levels |
| Configure Encrypting File System (EFS) |
| Manage NTFS Permissions |
| Configure Local Security Policy |
| Configure Windows Update Settings |
| Configure Password Policies |
| Utilize Command Line Security Tools |

## Task/Objective

| Task | Objective/Domain/Description |
|--------------------------------|------------------------------------------------------------------|
| Configure Windows Defender Antivirus Settings | 4.0 Operational Procedures |
| Configure Windows Firewall with Advanced Security | 2.0 Security |
| Manage Local User Accounts | 4.0 Operational Procedures |
| Configure User Account Control (UAC) Levels | 4.0 Operational Procedures |
| Configure Encrypting File System (EFS) | 1.0 Operating Systems |
| Manage NTFS Permissions | 4.0 Operational Procedures |
| Configure Local Security Policy | 2.0 Security |
| Configure Windows Update Settings | 4.0 Operational Procedures |
| Configure Password Policies | 4.0 Operational Procedures |
| Utilize Command Line Security Tools | 4.0 Operational Procedures |

---

# Task 1: Configure Windows Defender Antivirus Settings

## Objective
Configure and manage Windows Defender Antivirus settings to protect the system from malware and other threats.

## Steps

1. **Open Windows Security**
   - **Click** on the Start menu
   - **Type** "Windows Security"
   - **Press** Enter

2. **Run a quick scan**
   - **Click** on "Virus & threat protection"
   - **Click** "Quick scan"
   - **Wait** for the scan to complete

3. **Configure real-time protection**
   - **Click** on "Manage settings" under "Virus & threat protection settings"
   - **Toggle** "Real-time protection" to On
   - **Toggle** "Cloud-delivered protection" to On
   - **Toggle** "Automatic sample submission" to On

4. **Run a full scan**
   - **Click** on "Scan options"
   - **Select** "Full scan"
   - **Click** "Scan now"

5. **Check Windows Defender status using PowerShell**
   - Press `Windows + X` and select "Windows PowerShell (Admin)" or "Terminal (Admin)"
   - To check the current status, type the following command and press Enter:
     ```powershell
     Get-MpComputerStatus
     ```
   - This will display the current protection status, including real-time protection and virus definition information

6. **Update virus definitions**
   - In the same PowerShell window, type the following command and press Enter:
     ```powershell
     Update-MpSignature
     ```
   - Wait for the update to complete before proceeding

7. **Run a quick scan**
   - In the PowerShell window, type the following command and press Enter:
     ```powershell
     Start-MpScan -ScanType QuickScan
     ```
   - This will initiate a quick scan of your system for malware
   - Note: For a more thorough scan, you can use `-ScanType FullScan` instead, but this will take significantly longer

## Challenge Question
What does real-time protection in Windows Defender block? (Answer: Threats)

## Task Summary
In this task, you configured Windows Defender Antivirus settings to protect your system from malware and other threats. You learned how to:
- Run quick and full system scans to detect potential threats
- Enable and configure real-time protection for continuous monitoring
- Update virus definitions to ensure the latest threat detection
- Review scan results and protection history

This is important because maintaining up-to-date antivirus protection is a critical first line of defense against malware, helping to prevent security breaches and data loss.

---

# Task 2: Configure Windows Firewall with Advanced Security

## Objective
Set up and manage Windows Firewall with Advanced Security to control network traffic.

## Steps

1. **Open Windows Defender Firewall with Advanced Security**
   - **Press** `Windows + R`
   - **Type** `wf.msc`
   - **Press** Enter

2. **Create a new inbound rule**
   - **Right-click** on "Inbound Rules"
   - **Select** "New Rule..."
   - **Choose** "Port" and click "Next"
   - **Select** "TCP" and enter port `80`
   - **Click** "Next"
   - **Select** "Allow the connection"
   - **Check** all profiles (Domain, Private, Public)
   - **Name** the rule "Allow HTTP"
   - **Click** "Finish"

3. **Manage Firewall using PowerShell**
   - Open PowerShell as Administrator:
     - Press `Windows + X`
     - Select "Windows PowerShell (Admin)" or "Terminal (Admin)"
   - To check the current firewall status, type:
     ```powershell
     Get-NetFirewallProfile | Format-Table Name, Enabled
     ```
   - To create a new firewall rule to block RDP (Remote Desktop Protocol), type:
     ```powershell
     New-NetFirewallRule -DisplayName "Block RDP" -Direction Inbound -LocalPort 3389 -Protocol TCP -Action Block
     ```
   - To view all active inbound rules, type:
     ```powershell
     Get-NetFirewallRule -Enabled True -Direction Inbound | Format-Table -AutoSize
     ```

3. **Enable logging**
   - **Right-click** on "Windows Defender Firewall with Advanced Security"
   - **Select** "Properties"
   - **Click** on the "Domain Profile" tab
   - **Click** "Customize" under Logging
   - **Set** "Log dropped packets" to Yes
   - **Set** "Log successful connections" to Yes
   - **Click** OK

## Challenge Question
Which Windows Firewall profile should be used for a public kiosk in a shopping mall? (Answer: Public)

## Task Summary
In this task, you've learned how to configure and manage Windows Firewall with Advanced Security, a critical component of Windows security that controls network traffic to and from your computer. You've gained hands-on experience with:

- Creating custom inbound and outbound rules to control network access
- Enabling firewall logging for monitoring and troubleshooting
- Managing firewall profiles (Domain, Private, Public) for different network types
- Using PowerShell commands to manage firewall settings programmatically

These skills are essential for implementing network security best practices, such as the principle of least privilege, where you only allow necessary network traffic while blocking potentially malicious connections. In a professional setting, these capabilities help secure systems by preventing unauthorized access and providing visibility into network activity.

---

# Task 3: Manage Local User Accounts

## Objective
Create, modify, and manage local user accounts and groups.

## Steps

1. **Create a new local user**
   - **Option 1: Using GUI**
     - **Press** `Windows + R`
     - **Type** `lusrmgr.msc`
     - **Press** Enter
     - **Right-click** on "Users"
     - **Select** "New User..."
     - **Enter** username and password
     - **Uncheck** "User must change password at next logon"
     - **Check** "Password never expires"
     - **Click** "Create"
   - **Option 2: Using PowerShell**
     ```powershell
     # Create a new local user
     New-LocalUser -Name "TestUser" -Password (ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force) -FullName "Test User" -Description "Test account"
     ```

2. **Add user to a group**
   - **Option 1: Using GUI**
     - **Double-click** the new user
     - **Go** to the "Member Of" tab
     - **Click** "Add..."
     - **Type** "Remote Desktop Users" or "Power Users"
     - **Click** "Check Names"
     - **Click** OK
   - **Option 2: Using PowerShell**
     ```powershell
     # Add user to a group
     Add-LocalGroupMember -Group "Remote Desktop Users" -Member "TestUser"
     ```

3. **Disable a user account**
   - **Option 1: Using GUI**
     - **Right-click** on the user
     - **Select** "Properties"
     - **Check** "Account is disabled"
     - **Click** OK
   - **Option 2: Using PowerShell**
     ```powershell
     # Disable a user
     Disable-LocalUser -Name "TestUser"
     ```

## Challenge Question
What is the difference between a standard user account and an administrator account? (Answer: Access)

## Task Summary
In this task, you learned essential user account management skills in Windows. You practiced:
- Creating and managing local user accounts with appropriate permissions
- Adding users to security groups to control access to resources
- Disabling user accounts when they're no longer needed
- Using both GUI tools and PowerShell commands for user management

This is important because proper user account management is a fundamental security practice. By understanding how to create and manage user accounts with the principle of least privilege, you can help prevent unauthorized access to sensitive systems and data. These skills are essential for maintaining a secure computing environment in both personal and professional settings.

---

# Task 4: Configure User Account Control (UAC) Levels

## Objective
Adjust UAC settings to balance security and usability.

## Steps

1. **Open User Account Control Settings**
   - **Option 1: Using GUI**
     - **Press** `Windows + R`
     - **Type** `ms-settings:windowsdefender`
     - **Press** Enter
     - **Click** on "App & browser control"
     - **Scroll** down and click "Exploit protection settings"
     - **Click** on "Change settings" under "User Account Control settings"
   - **Option 2: Using PowerShell**
     ```powershell
     # Open UAC settings
     Start-Process ms-settings:windowsdefender
     ```

2. **Adjust UAC level**
   - **Option 1: Using GUI**
     - **Move** the slider to "Notify me only when apps try to make changes to my computer (default)"
     - **Click** OK
     - **Click** "Yes" to confirm
   - **Option 2: Using PowerShell**
     ```powershell
     # Check current UAC setting
     $uac = Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System"
     Write-Host "Current UAC setting: $($uac.EnableLUA)"
     
     # Set UAC to default level (1=Enabled, 0=Disabled)
     Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" -Name "EnableLUA" -Value 1
     ```

3. **Test UAC**
   - **Option 1: Using GUI**
     - **Try** to open an application that requires elevation (e.g., Command Prompt as admin)
     - **Verify** that the UAC prompt appears
   - **Option 2: Using PowerShell**
     ```powershell
     # Test UAC by attempting to create a scheduled task (requires elevation)
     try {
         $action = New-ScheduledTaskAction -Execute 'cmd.exe' -Argument '/c echo UAC test'
         $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1)
         Register-ScheduledTask -TaskName 'UAC_Test' -Action $action -Trigger $trigger -RunLevel Highest -Force -ErrorAction Stop
         Unregister-ScheduledTask -TaskName 'UAC_Test' -Confirm:$false
         Write-Host "UAC is working - elevation prompt should have appeared" -ForegroundColor Green
     }
     catch {
         Write-Host "UAC test failed: $_" -ForegroundColor Red
     }
     ```

## Challenge Question
What does the highest UAC level require? (Answer: Approval)

## Task Summary
In this task, you configured User Account Control (UAC) settings to balance security and usability. You learned how to:
- Adjust UAC notification levels to control when elevation prompts appear
- Test UAC behavior with different security levels
- Understand the security implications of UAC settings

This is important because UAC helps prevent unauthorized system changes by requiring administrative approval, which is a key security control in Windows operating systems.

---

# Task 5: Configure Encrypting File System (EFS)

## Objective
Encrypt sensitive files using EFS for enhanced security.

## Steps

1. **Create a test file**
   - **Option 1: Using GUI**
     - **Right-click** on the desktop
     - **Select** New > Text Document
     - **Name** it "Secret.txt"
   - **Option 2: Using PowerShell**
     ```powershell
     # Create a test file with sample content
     $testContent = "This is a test file for EFS encryption"
     $testContent | Out-File -FilePath "$env:USERPROFILE\Desktop\Secret.txt"
     ```

2. **Encrypt the file**
   - **Option 1: Using GUI**
     - **Right-click** on "Secret.txt"
     - **Select** "Properties"
     - **Click** "Advanced..."
     - **Check** "Encrypt contents to secure data"
     - **Click** OK
     - **Click** Apply
     - **Select** "Encrypt the file only"
     - **Click** OK
   - **Option 2: Using PowerShell**
     ```powershell
     # Check if EFS is enabled
     $efsStatus = fsutil behavior query encryptpagingfile
     Write-Host "EFS Status: $efsStatus"
     
     # Encrypt the file
     $filePath = "$env:USERPROFILE\Desktop\Secret.txt"
     cipher /e "$filePath"
     
     # Verify encryption
     $encrypted = (Get-Item $filePath).Attributes -match "Encrypted"
     Write-Host "File encrypted: $($encrypted -ne $null)"
     ```

3. **Back up your EFS certificate**
   - **Option 1: Using GUI**
     - **Press** `Windows + R`
     - **Type** `certmgr.msc`
     - **Press** Enter
     - **Navigate** to Personal > Certificates
     - **Right-click** your EFS certificate
     - **Select** All Tasks > Export...
     - **Follow** the wizard to export with a password
   - **Option 2: Using PowerShell**
     ```powershell
     # Create backup directory if it doesn't exist
     $backupDir = "$env:USERPROFILE\EFS_Backup"
     if (-not (Test-Path $backupDir)) {
         New-Item -ItemType Directory -Path $backupDir | Out-Null
     }
     
     # Back up EFS certificate
     $cert = Get-ChildItem -Path Cert:\CurrentUser\My | Where-Object { $_.EnhancedKeyUsageList.FriendlyName -eq 'Encrypting File System' }
     if ($cert) {
         $cert | Export-Certificate -FilePath "$backupDir\EFS_Cert.cer" -Type CERT
         Write-Host "EFS certificate backed up to $backupDir\EFS_Cert.cer"
     } else {
         Write-Warning "No EFS certificate found in the personal store"
     }
     
     # Alternative method using cipher
     cipher /x:"$backupDir\efs_certificate" "$env:USERPROFILE\Desktop\Secret.txt"
     ```

## Challenge Question
What does EFS provide for files? (Answer: Encryption)

## Task Summary
In this task, you worked with the Encrypting File System (EFS) to protect sensitive files. You learned how to:
- Encrypt individual files and folders using EFS
- Back up and manage EFS certificates for recovery purposes
- Verify encryption status of files and folders

This is important because EFS provides file-level encryption that protects sensitive data even if an attacker gains physical access to the storage media, ensuring data confidentiality.

---

# Task 6: Manage NTFS Permissions

## Objective
Configure and verify NTFS permissions for files and folders using both GUI and PowerShell methods.

## Steps

1. **Create a test folder**
   - **Option 1: Using GUI**
     - **Right-click** on the desktop
     - **Select** New > Folder
     - **Name** it "SecureData"
   - **Option 2: Using PowerShell**
     ```powershell
     # Create a secure directory
     $secureDir = "$env:USERPROFILE\Desktop\SecureData"
     if (-not (Test-Path $secureDir)) {
         New-Item -Path $secureDir -ItemType Directory | Out-Null
         Write-Host "Created directory: $secureDir"
     } else {
         Write-Host "Directory already exists: $secureDir"
     }
     ```

2. **Set NTFS permissions**
   - **Option 1: Using GUI**
     - **Right-click** on "SecureData"
     - **Select** "Properties"
     - **Go** to the "Security" tab
     - **Click** "Edit..."
     - **Click** "Add..."
     - **Type** "Authenticated Users"
     - **Click** "Check Names"
     - **Click** OK
     - **Select** "Authenticated Users"
     - **Check** "Modify" under Allow
     - **Click** Apply then OK
   - **Option 2: Using PowerShell**
     ```powershell
     # Import required module
     Import-Module NTFSSecurity -ErrorAction SilentlyContinue
     
     # Define paths and identity
     $folderPath = "$env:USERPROFILE\Desktop\SecureData"
     $identity = [System.Security.Principal.NTAccount]::new("Authenticated Users")
     
     # Get current ACL
     $acl = Get-Acl -Path $folderPath
     
     # Define access rule (Modify permissions)
     $accessRule = [System.Security.AccessControl.FileSystemAccessRule]::new(
         $identity,
         'Modify',
         'ContainerInherit,ObjectInherit',
         'None',
         'Allow'
     )
     
     # Add the access rule
     $acl.SetAccessRule($accessRule)
     
     # Apply the modified ACL
     Set-Acl -Path $folderPath -AclObject $acl
     Write-Host "NTFS permissions updated for: $folderPath"
     
     # Verify permissions
     Get-NTFSAccess -Path $folderPath | Format-Table -AutoSize
     ```

3. **Verify permissions**
   - **Option 1: Using GUI**
     - **Create** a new text file in the folder
     - **Try** to modify and delete it
   - **Option 2: Using PowerShell**
     ```powershell
     # Create a test file
     $testFile = "$env:USERPROFILE\Desktop\SecureData\test_permissions.txt"
     "Test content" | Out-File -FilePath $testFile -Force
     
     # Test file operations
     try {
         # Test write access
         "Additional content" | Out-File -FilePath $testFile -Append -ErrorAction Stop
         Write-Host "Write test: SUCCESS" -ForegroundColor Green
         
         # Test read access
         $content = Get-Content -Path $testFile -ErrorAction Stop
         Write-Host "Read test: SUCCESS" -ForegroundColor Green
         Write-Host "File content: $content"
         
         # Test delete access
         Remove-Item -Path $testFile -Force -ErrorAction Stop
         Write-Host "Delete test: SUCCESS" -ForegroundColor Green
     } catch {
         Write-Warning "Permission test failed: $_"
     }
     
     # View effective permissions (requires admin rights)
     # Get-NTFSEffectiveAccess -Path $folderPath -Account "$env:USERDOMAIN\$env:USERNAME"
     ```

## Challenge Question
What do NTFS permissions control? (Answer: Access)

## Task Summary
In this task, you learned multiple methods to manage NTFS permissions effectively:

### Key Learnings:
- **Permission Management**: Set and modified NTFS permissions using both GUI and PowerShell
- **Access Control**: Implemented the principle of least privilege for file system access
- **Verification**: Tested and verified permissions through various operations
- **Automation**: Used PowerShell to script permission management tasks

### PowerShell Commands Used:
- `Get-Acl` / `Set-Acl`: View and modify access control lists
- `New-Object System.Security.AccessControl.FileSystemAccessRule`: Create permission rules
- `Get-NTFSAccess`: View detailed NTFS permissions (requires NTFSSecurity module)
- `Test-Path`: Check if a path exists
- `New-Item`: Create files and directories

### Best Practices:
1. Always test permissions in a non-production environment first
2. Document permission changes for auditing purposes
3. Use groups instead of individual users when assigning permissions
4. Regularly review and audit permissions to maintain security
5. Consider using the `-WhatIf` parameter when running PowerShell commands to preview changes

This is important because proper permission settings ensure that users can only access the resources they need, following the principle of least privilege and helping to maintain data security and integrity.

---

# Task 7: Configure Local Security Policy

## Objective
Implement and manage security settings through Local Security Policy using both GUI and PowerShell methods.

## Steps

1. **Open Local Security Policy**
   - **Option 1: Using GUI**
     - **Press** `Windows + R`
     - **Type** `secpol.msc`
     - **Press** Enter
   - **Option 2: Using PowerShell**
     ```powershell
     # Open Local Security Policy (requires admin rights)
     Start-Process secpol.msc -Verb RunAs
     
     # Alternative: View security settings via registry
     # Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System'
     ```

2. **Configure Account Lockout Policy**
   - **Option 1: Using GUI**
     - **Navigate** to Account Policies > Account Lockout Policy
     - **Double-click** "Account lockout threshold"
     - **Set** to 3 invalid logon attempts
     - **Click** OK
     - **Click** OK on the suggested lockout duration
   - **Option 2: Using PowerShell**
     ```powershell
     # Requires administrative privileges
     if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
         Write-Warning "Please run this script as Administrator"
         exit 1
     }
     
     # Set account lockout threshold (3 attempts)
     $lockoutThreshold = 3  # Number of invalid logon attempts before lockout
     $lockoutDuration = 30  # Lockout duration in minutes (0 = until admin unlocks)
     $resetCounterAfter = 15 # Reset failed logon attempt counter after (minutes)
     
     # Apply account lockout policy
     net accounts /lockoutthreshold:$lockoutThreshold /lockoutduration:$lockoutDuration /lockoutwindow:$resetCounterAfter
     
     # Verify the settings
     $lockoutPolicy = net accounts
     Write-Host "Account Lockout Policy:"
     $lockoutPolicy | Select-String -Pattern "lockout" -Context 0,3
     
     # Alternative method using SecurityPolicy module (if available)
     # Set-PolicyFileEntry -Path 'System\Access' -Section 'System Access' -Key 'LockoutBadCount' -Value $lockoutThreshold
     ```

3. **Configure Password Policy**
   - **Option 1: Using GUI**
     - **Navigate** to Account Policies > Password Policy
     - **Set** "Enforce password history" to 24 passwords
     - **Set** "Maximum password age" to 60 days
     - **Set** "Minimum password length" to 12 characters
   - **Option 2: Using PowerShell**
     ```powershell
     # Set password policy using net accounts
     net accounts /maxpwage:60 /minpwlen:12 /uniquepw:24 /minpwage:1
     
     # Alternative: Using Group Policy Cmdlets (Windows 10 1809+ and Windows Server 2019+)
     # Set-GPRegistryValue -Name "Default Domain Policy" -Key "HKLM\SOFTWARE\Policies\Microsoft\Windows NT\DNSClient" -ValueName "MaxPasswordAge" -Value 60 -Type DWord
     
     # View current password policy
     Write-Host "Current Password Policy:"
     net accounts | Select-String -Pattern "(Maximum|Minimum|Length|History)"
     ```

4. **Enable Audit Policy**
   - **Option 1: Using GUI**
     - **Navigate** to Local Policies > Audit Policy
     - **Double-click** "Audit account logon events"
     - **Check** both Success and Failure
     - **Click** OK
   - **Option 2: Using PowerShell**
     ```powershell
     # Enable auditing for account logon events (success and failure)
     auditpol /set /subcategory:"Account Logon" /success:enable /failure:enable
     
     # Enable other important audit categories
     $auditCategories = @(
         "Logon",
         "Account Management",
         "Policy Change",
         "Privilege Use",
         "Detailed Tracking"
     )
     
     foreach ($category in $auditCategories) {
         auditpol /set /subcategory:"$category" /success:enable /failure:enable
     }
     
     # View current audit policy
     Write-Host "Current Audit Policy:"
     auditpol /get /category:* | Select-String -Pattern "(Success|Failure)\\s+(Audit|No Auditing)"
     ```

5. **Export and Import Security Templates (Optional)**
   ```powershell
   # Export current security policy
   secedit /export /cfg "$env:USERPROFILE\Desktop\Local_Security_Policy_Backup.inf"
   
   # Import security policy from file (use with caution)
   # secedit /configure /db secedit.sdb /cfg "C:\path\to\security\template.inf" /overwrite /log secedit.log
   
   # Generate a report of current security settings
   secedit /export /cfg "$env:USERPROFILE\Desktop\Security_Report.txt" /areas SECURITYPOLICY
   ```

## Challenge Question
What do audit policies track? (Answer: Events)

## Task Summary
In this task, you learned how to configure and manage Local Security Policy settings using both GUI and PowerShell methods.

### Key Learnings:
- **Policy Management**: Configured account and password policies to enhance security
- **Audit Configuration**: Enabled comprehensive auditing for security events
- **Automation**: Used PowerShell to script security policy configurations
- **Documentation**: Created security policy backups and reports

### PowerShell Commands Used:
- `net accounts`: View and configure password and account lockout policies
- `auditpol`: Configure and view audit policies
- `secedit`: Export and import security configurations
- `Set-GPRegistryValue`: Configure Group Policy settings (domain environments)

### Best Practices:
1. Always back up current security settings before making changes
2. Test policy changes in a non-production environment first
3. Document all policy changes for audit purposes
4. Regularly review security logs for suspicious activities
5. Consider using Group Policy in domain environments for centralized management

This is important because properly configured security policies are essential for maintaining system security, ensuring compliance with organizational standards, and providing an audit trail for security events.

### Key Learnings:
   - **Update Management**: Checked for and installed Windows updates using both GUI and PowerShell
   - **Active Hours**: Configured active hours to prevent disruptions during work hours
   - **Update History**: Reviewed installed updates and update history
   - **Automation**: Used PowerShell to automate update management tasks
    
### PowerShell Commands Used:
  - `Get-WindowsUpdate`: Check for available updates
  - `Install-WindowsUpdate`: Install available updates
  - `Get-HotFix`: View installed updates
  - `Set-ItemProperty`: Configure Windows Update settings
  - `Get-WmiObject`: Query Windows Management Instrumentation for update information
    
### Best Practices:
  1. Keep systems updated with the latest security patches
  2. Configure active hours to prevent disruptions during work hours
  3. Regularly review installed updates and update history
  4. Test updates in a non-production environment before deploying to production
  5. Maintain a schedule for regular update checks and installations
    
This is important because keeping systems updated with the latest security patches is one of the most effective ways to protect against known vulnerabilities and security threats.
    
     ---
# Task 9: Configure Password Policies

## Objective
Implement and enforce strong password policies using both GUI and PowerShell methods.

## Steps

### 1. Configure Password Policy

#### Option 1: Using Local Security Policy (GUI)
- **Press** `Windows + R`
- **Type** `secpol.msc` and press Enter
- **Navigate** to Account Policies > Password Policy
- Configure the following settings:
  - **Enforce password history**: 24 passwords remembered
  - **Maximum password age**: 90 days
  - **Minimum password age**: 1 day
  - **Minimum password length**: 14 characters
  - **Password must meet complexity requirements**: Enabled
  - **Store passwords using reversible encryption**: Disabled

#### Option 2: Using PowerShell
```powershell
# View current password policy settings
Get-LocalUser | Select-Object *password* | Format-List
Get-LocalUser | Where-Object {$_.PasswordRequired -eq $false} | Select-Object Name,Enabled,PasswordRequired

# Set password policy using PowerShell
# Requires running as Administrator
$passwordPolicy = @{
    "PasswordHistoryCount" = 24
    "MaxPasswordAge" = (New-TimeSpan -Days 90)
    "MinPasswordAge" = (New-TimeSpan -Days 1)
    "MinPasswordLength" = 14
    "PasswordComplexity" = $true
    "PasswordReversibleEncryptionEnabled" = $false
}

# Apply password policy settings
Set-LocalUser -Name $env:USERNAME -PasswordNeverExpires $false
Set-LocalUser -Name $env:USERNAME -UserMayNotChangePassword $false

# For domain environments, you can use:
# Set-ADDefaultDomainPasswordPolicy -Identity yourdomain.com @passwordPolicy

# Export password policy for documentation
$passwordPolicy | ConvertTo-Json | Out-File -FilePath "$env:USERPROFILE\Desktop\PasswordPolicy_$(Get-Date -Format 'yyyyMMdd').json"
```

### 2. Configure Account Lockout Policy

#### Option 1: Using Local Security Policy (GUI)
- **Navigate** to Account Policies > Account Lockout Policy
- Configure the following settings:
  - **Account lockout threshold**: 5 invalid logon attempts
  - **Account lockout duration**: 30 minutes
  - **Reset account lockout counter after**: 30 minutes

#### Option 2: Using PowerShell
```powershell
# View current account lockout policy
$lockoutPolicy = Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN
$lockoutPolicy | Select-Object *lockout*

# Set account lockout policy
$securityTemplate = @"
[System Access]
LockoutBadCount = 5
LockoutDuration = 30
LockoutWindow = 30
"@

$tempFile = [System.IO.Path]::GetTempFileName()
$securityTemplate | Out-File -FilePath $tempFile -Encoding ascii

# Apply the security template
secedit /configure /db secedit.sdb /cfg $tempFile
Remove-Item -Path $tempFile

# Verify the settings
Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN | 
    Select-Object LockoutBadCount, LockoutDuration, LockoutWindow
```

### 3. Password Audit and Compliance Check

```powershell
# Check for accounts with non-expiring passwords
Get-LocalUser | Where-Object {$_.PasswordNeverExpires -eq $true} | 
    Select-Object Name, Enabled, PasswordNeverExpires, PasswordRequired

# Check for accounts with blank passwords (security risk!)
$users = Get-LocalUser | Where-Object {$_.Enabled -eq $true}
foreach ($user in $users) {
    try {
        $passwordCheck = [ADSI]::new("WinNT://$env:COMPUTERNAME/$($user.Name),User")
        if ($passwordCheck.Password -eq "") {
            Write-Warning "Account $($user.Name) has a blank password!"
        }
    } catch {
        Write-Verbose "Could not check password for $($user.Name)" -Verbose
    }
}

# Generate password policy compliance report
$report = @()
$report += "Password Policy Compliance Report - $(Get-Date)"
$report += "=" * 40
$report += "`n[Password Policy Settings]"
$report += "-" * 40
$report += "Minimum password length: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).MinimumPasswordLength"
$report += "Password complexity required: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).PasswordComplexity)"
$report += "Password history maintained: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).PasswordHistorySize) passwords"
$report += "Maximum password age: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).MaximumPasswordAge) days"
$report += "Minimum password age: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).MinimumPasswordAge) days"
$report += "`n[Account Lockout Settings]"
$report += "-" * 40
$report += "Account lockout threshold: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).LockoutBadCount) attempts"
$report += "Account lockout duration: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).LockoutDuration) minutes"
$report += "Reset account lockout counter after: $(Get-LocalSecurityPolicy -Area SECURITY_POLICY_DOMAIN).LockoutWindow) minutes"

# Save report to desktop
$report | Out-File -FilePath "$env:USERPROFILE\Desktop\PasswordPolicyReport_$(Get-Date -Format 'yyyyMMdd').txt"
```

## Challenge Question
What is the recommended minimum password length according to NIST SP 800-63B? (Answer: 12 characters)

## Task Summary
In this task, you learned multiple methods to configure and enforce strong password policies:

### Key Learnings:
- **Password Policy Configuration**: Set minimum length, complexity, and history requirements
- **Account Lockout Policies**: Implemented protection against brute force attacks
- **Security Auditing**: Created scripts to audit and document password policies
- **Compliance Reporting**: Generated detailed reports of current security settings

### PowerShell Commands Used:
- `Get-LocalUser`: Retrieve local user account information
- `Set-LocalUser`: Configure local user account settings
- `Get-LocalSecurityPolicy`: View current security policy settings
- `secedit`: Configure system security settings
- `ConvertTo-Json`: Format data for documentation

### Best Practices:
1. Enforce a minimum password length of at least 12 characters
2. Require password complexity (uppercase, lowercase, numbers, special characters)
3. Set maximum password age to 60-90 days
4. Maintain password history (24 passwords recommended)
5. Implement account lockout after 5 failed attempts
6. Set lockout duration to 30-60 minutes
7. Regularly audit password policies and user accounts
8. Document all policy changes for compliance purposes

This is important because strong password policies are a critical defense against unauthorized access, credential stuffing, and brute force attacks, helping to protect sensitive systems and data from compromise.

---

# Task 10: Utilize Command Line Security Tools

## Objective
Master the use of command-line tools for comprehensive security administration and monitoring using both traditional commands and modern PowerShell cmdlets.

## Steps

### 1. Network Security Analysis

#### Option 1: Using Traditional Commands

```cmd
:: View listening ports and established connections
netstat -ano | findstr LISTENING
netstat -ano | findstr ESTABLISHED

:: Check for hidden connections
netstat -bano

:: View network routing table
route print

:: Check ARP cache for potential ARP spoofing
arp -a
```

#### Option 2: Using PowerShell

```powershell
# Get detailed network connections with process information
Get-NetTCPConnection -State Listen | 
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, State, 
    @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess).ProcessName}} | 
    Sort-Object -Property LocalPort | Format-Table -AutoSize

# Check for suspicious outbound connections
Get-NetTCPConnection -State Established | 
    Where-Object {$_.RemoteAddress -notlike "127.0.0.1" -and $_.RemoteAddress -notlike "::1"} |
    Select-Object LocalAddress, LocalPort, RemoteAddress, RemotePort, 
    @{Name="Process";Expression={(Get-Process -Id $_.OwningProcess -ErrorAction SilentlyContinue).ProcessName}} |
    Sort-Object -Property Process | Format-Table -AutoSize

# Check DNS cache for potential DNS poisoning
Get-DnsClientCache | Format-Table -AutoSize

# Check network interfaces and their configurations
Get-NetIPConfiguration -Detailed | Format-List
```

### 2. Process and Service Analysis

#### Option 1: Using Traditional Commands

```cmd
:: List all running processes with services
tasklist /svc /fo list

:: Check for hidden processes
tasklist /v /fi "STATUS eq running"

:: View services and their status
net start
sc query state= all
```

#### Option 2: Using PowerShell

```powershell
# Get detailed process information with hashes for verification
Get-Process | Select-Object ProcessName, Id, Path, 
    @{Name="SHA256";Expression={(Get-FileHash -Path $_.Path -Algorithm SHA256 -ErrorAction SilentlyContinue).Hash}} |
    Sort-Object -Property ProcessName | Format-Table -AutoSize

# Check for processes with network connections
Get-Process | Where-Object {$_.MainWindowTitle -ne ""} | 
    Select-Object Name, Id, Path | 
    Format-Table -AutoSize

# Check for unsigned processes
Get-Process | Where-Object { 
    $sig = Get-AuthenticodeSignature -FilePath $_.Path -ErrorAction SilentlyContinue
    $sig.Status -ne "Valid" -and $sig.Status -ne "NotSigned"
} | Select-Object ProcessName, Id, Path

# Check for suspicious services
Get-Service | Where-Object { $_.Status -eq "Running" } | 
    Select-Object DisplayName, Name, Status, StartType |
    Sort-Object -Property DisplayName | Format-Table -AutoSize
```

### 3. Firewall and Network Security

#### Option 1: Using netsh

```cmd
:: View all firewall rules
netsh advfirewall firewall show rule name=all

:: View inbound/outbound rules separately
netsh advfirewall firewall show rule name=all dir=in
netsh advfirewall firewall show rule name=all dir=out
```

#### Option 2: Using PowerShell

```powershell
# Get all enabled firewall rules with details
Get-NetFirewallRule -Enabled True -Direction Inbound | 
    Where-Object { $_.Profile -match "Domain|Private|Public" } |
    ForEach-Object {
        $rule = $_
        $filters = Get-NetFirewallPortFilter -AssociatedNetFirewallRule $_
        $addresses = Get-NetFirewallAddressFilter -AssociatedNetFirewallRule $_
        $applications = Get-NetFirewallApplicationFilter -AssociatedNetFirewallRule $_
        
        [PSCustomObject]@{
            Name = $rule.DisplayName
            Enabled = $rule.Enabled
            Direction = $rule.Direction
            Action = $rule.Action
            Profile = $rule.Profile
            Protocol = $filters.Protocol
            LocalPort = $filters.LocalPort
            RemotePort = $filters.RemotePort
            RemoteAddress = $addresses.RemoteAddress
            Program = $applications.Program
        }
    } | Format-Table -AutoSize

# Check for overly permissive rules
Get-NetFirewallRule -Enabled True | 
    Where-Object { $_.Action -eq "Allow" -and $_.Direction -eq "Inbound"

---

# Task 11: Configure Windows Defender Antivirus

## Objective
Configure and manage Windows Defender Antivirus settings to protect the system from malware and other threats using both GUI and PowerShell methods.

## Background
Windows Defender Antivirus is a critical component of Windows security that provides real-time protection against various threats. It includes features like real-time scanning, cloud-delivered protection, and ransomware protection.

## Prerequisites
- Administrative privileges on the system
- Internet connectivity for downloading updates and additional tools
- 15-20 minutes of dedicated time

## Steps

### 1. Check Windows Defender Status

#### Option 1: Using GUI
1. Open Windows Security
   - Click Start and type "Windows Security"
   - Select the Windows Security app

2. Navigate to Virus & threat protection
   - Click on "Virus & threat protection"
   - Review the protection status

#### Option 2: Using PowerShell
```powershell
# Get Windows Defender status
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AntispywareEnabled

# Get detailed protection status
Get-MpThreatDetection | Format-Table -AutoSize
```

### 2. Run Security Scans

#### Option 1: Using GUI
1. In Windows Security, go to "Virus & threat protection"
2. Click "Quick scan" for a fast scan
3. For a full scan, click "Scan options" and select "Full scan"

#### Option 2: Using PowerShell
```powershell
# Run a quick scan
Start-MpScan -ScanType QuickScan

# Run a full scan (takes longer)
Start-MpScan -ScanType FullScan

# Scan a specific path
Start-MpScan -ScanType CustomScan -ScanPath "C:\Path\To\Scan"
```

### 3. Update Security Intelligence

#### Option 1: Using GUI
1. In Windows Security, go to "Virus & threat protection"
2. Click "Check for updates" under "Virus & threat protection updates"

#### Option 2: Using PowerShell
```powershell
# Update security intelligence
Update-MpSignature

# Check update status
Get-MpThreatCatalog | Select-Object Name, Severity, IsActive
```

### 4. Configure Real-time Protection

#### Option 1: Using GUI
1. Go to Windows Security > Virus & threat protection > Manage settings
2. Toggle "Real-time protection" as needed

#### Option 2: Using PowerShell
```powershell
# Enable real-time protection
Set-MpPreference -DisableRealtimeMonitoring $false

# Disable real-time protection (not recommended)
# Set-MpPreference -DisableRealtimeMonitoring $true
```

### 5. Configure Cloud-Delivered Protection

#### Option 1: Using GUI
1. Go to Windows Security > Virus & threat protection > Manage settings
2. Toggle "Cloud-delivered protection"

#### Option 2: Using PowerShell
```powershell
# Enable cloud-delivered protection
Set-MpPreference -MAPSReporting Advanced

# Check cloud protection status
Get-MpPreference | Select-Object MAPSReporting
```

### 6. Configure Ransomware Protection

#### Option 1: Using GUI
1. Go to Windows Security > Virus & threat protection > Ransomware protection
2. Toggle "Controlled folder access"
3. Add protected folders as needed

#### Option 2: Using PowerShell
```powershell
# Enable controlled folder access
Set-MpPreference -EnableControlledFolderAccess Enabled

# Add protected folder
Add-MpPreference -ControlledFolderAccessProtectedFolders "C:\Sensitive"

# Add allowed application
Add-MpPreference -ControlledFolderAccessAllowedApplications "C:\Path\To\App.exe"
```

## Verification

### 1. Check Protection Status
```powershell
# Get overall protection status
Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, AMServiceEnabled

# Check if any threats were detected
Get-MpThreatDetection | Where-Object { $_.ThreatID -ne 0 } | Format-Table -AutoSize
```

### 2. Review Windows Defender Logs
```powershell
# View recent Windows Defender events
Get-WinEvent -LogName "Microsoft-Windows-Windows Defender/Operational" -MaxEvents 10 | 
    Select-Object TimeCreated, Message | Format-Table -Wrap -AutoSize
```

## Security Best Practices

### 1. Update Management
```powershell
# Schedule daily signature updates
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-Command Update-MpSignature"
$trigger = New-ScheduledTaskTrigger -Daily -At 2am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "Windows Defender Update" -Description "Daily Windows Defender signature updates"
```

### 2. Scheduled Scanning
```powershell
# Schedule weekly full scan
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-Command Start-MpScan -ScanType FullScan"
$trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 2am
Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "Windows Defender Weekly Scan" -Description "Weekly full system scan"
```

### 3. Exclusion Management
```powershell
# Add process exclusion
Add-MpPreference -ExclusionProcess "C:\Path\To\Process.exe"

# Add path exclusion
Add-MpPreference -ExclusionPath "C:\Path\To\Exclude"

# View current exclusions
Get-MpPreference | Select-Object Exclusion* | Format-List
```

## Troubleshooting

### 1. Windows Security Won't Open
```powershell
# Reset Windows Security app
Get-AppxPackage Microsoft.SecHealthUI -AllUsers | Reset-AppxPackage

# Check for system file corruption
sfc /scannow

# Check Windows Update for security intelligence updates
Get-WindowsUpdate -Install -AcceptAll -UpdateType Software
```

### 2. Real-time Protection Issues
```powershell
# Check for conflicting software
Get-Service | Where-Object { $_.DisplayName -match "antivirus|security" }

# Restart Windows Defender service
Restart-Service -Name WinDefend -Force

# Check Group Policy settings
Get-ItemProperty -Path "HKLM:\SOFTWARE\Policies\Microsoft\Windows Defender"
```

### 3. Performance Issues
```powershell
# Check system impact
Get-MpPerformanceReport

# View scan history
Get-MpThreatDetection | Sort-Object -Property InitialDetectionTime -Descending | Format-Table -AutoSize
```

## Documentation

### 1. Export Configuration
```powershell
# Export current configuration
Get-MpPreference | Export-Clixml -Path "$env:USERPROFILE\Desktop\DefenderConfig.xml"

# Export scan history
Get-MpThreatDetection | Export-Csv -Path "$env:USERPROFILE\Desktop\DefenderScanHistory.csv" -NoTypeInformation
```

### 2. Create Restore Point
```powershell
# Create system restore point before making changes
Checkpoint-Computer -Description "Before Windows Defender Configuration" -RestorePointType MODIFY_SETTINGS
```

##   

### Troubleshooting

#### Issue 1: "Encrypt contents to secure data" Option is Grayed Out
- **Cause**: The drive is not NTFS, or the edition of Windows doesn't support EFS
- **Solution**:
  - Convert the drive to NTFS using `convert X: /fs:ntfs` (where X is the drive letter)
  - Upgrade to a supported Windows edition (Pro, Enterprise, or Education)

#### Issue 2: "Access is Denied" When Opening Encrypted Files
- **Cause**: The current user doesn't have the proper encryption certificate
- **Solution**:
  - Log in as the user who encrypted the file
  - Restore the user's EFS certificate from backup
  - Contact the system administrator for recovery options

#### Issue 3: Lost EFS Certificate
- **Cause**: Certificate was deleted or corrupted
- **Solution**:
  - Restore from a backup of the certificate
  - Use a Data Recovery Agent (DRA) if configured
  - As a last resort, use third-party recovery tools (not recommended for production environments)

2. **File Management"**
   - Encrypt folders rather than individual files when possible
   - Be cautious when moving encrypted files to non-NTFS locations
   - Decrypt files before transferring them to external media or cloud storage

3. **System Configuration**
   - Enable BitLocker for full-disk encryption in addition to EFS
   - Configure EFS to use smart cards for stronger authentication
   - Regularly back up encrypted files and certificates

### Documentation Requirements
1. **Record Certificate Information**
   - Document the thumbprint of EFS certificates
   - Note the certificate expiration dates
   - Record the location of certificate backups

2. **Recovery Procedures**
   - Document steps for EFS certificate recovery
   - Include contact information for certificate authorities
   - Note any organizational policies regarding EFS usage

3. **User Guidelines**
   - Create a user guide for working with encrypted files
   - Document how to identify encrypted files
   - Include instructions for requesting access to encrypted files

### Real-World Application
Understanding EFS is crucial for:
- Protecting sensitive business documents
- Securing personal information on shared computers
- Meeting compliance requirements (e.g., HIPAA, GDPR)
- Preventing data breaches from lost or stolen devices

### Challenge Question
What file system is required for EFS encryption? (Answer: NTFS)

## Task Summary
In this task, you configured and managed Windows Defender Antivirus settings to protect your system from malware and other security threats. You learned how to:
- Navigate and use the Windows Security interface
- Perform quick and full system scans
- Configure real-time and cloud-delivered protection
- Set up ransomware protection features
- Review and interpret protection history
- Apply security best practices for antivirus management

This is important because Windows Defender Antivirus serves as a critical first line of defense against malware and other security threats. Proper configuration ensures that your system is protected against the latest threats while maintaining system performance. Understanding these settings allows you to balance security with usability and troubleshoot common issues that may arise.

## Windows Security Command Reference

This section provides a comprehensive reference of essential Windows commands for security management and system administration. These commands are invaluable for security professionals to manage, monitor, and troubleshoot Windows security settings.

| Command | Description | Example |
|---------|-------------|---------|
| `Get-Acl` | Retrieves the security descriptor for a resource | `Get-Acl -Path "C:\Path" \| Format-List` |
| `Set-Acl` | Applies a security descriptor to a resource | `Get-Acl -Path "Source" \| Set-Acl -Path "Destination"` |
| `auditpol` | Configures and displays audit policies | `auditpol /get /category:*` |
| `Get-WindowsUpdate` | Manages Windows updates | `Get-WindowsUpdate -Install -AcceptAll -AutoReboot` |
| `Set-ItemProperty` | Modifies registry values | `Set-ItemProperty -Path "HKLM:\..." -Name "NoAutoUpdate" -Value 0` |
| `Get-Service` | Manages Windows services | `Get-Service -Name wuauserv \| Start-Service` |
| `Set-Service` | Configures service properties | `Set-Service -Name wuauserv -StartupType Automatic` |
| `Get-Process` | Lists running processes | `Get-Process \| Where-Object { $_.CPU -gt 50 }` |
| `Stop-Process` | Terminates running processes | `Stop-Process -Name "ProcessName" -Force` |
| `Get-EventLog` | Queries Windows event logs | `Get-EventLog -LogName Security -Newest 20` |
| `gpupdate` | Applies Group Policy updates | `gpupdate /force` |
| `secedit` | Configures system security | `secedit /configure /cfg %windir%\inf\defltbase.inf /db defltbase.sdb /verbose` |
| `net user` | Manages user accounts | `net user username /add /passwordreq:yes` |
| `net localgroup` | Manages local groups | `net localgroup Administrators username /add` |
| `whoami /priv` | Displays user privileges | `whoami /priv` |
| `systeminfo` | Shows system configuration | `systeminfo \| findstr /B /C:"OS Name" /C:"OS Version"` |
| `sfc /scannow` | Scans and repairs system files | `sfc /scannow` |
| `DISM` | Services Windows images | `DISM /Online /Cleanup-Image /RestoreHealth` |

## Discussion Questions

1. **How does the principle of least privilege enhance system security, and what are the potential challenges in implementing it effectively in a large organization?**
   The principle of least privilege (PoLP) enhances security by ensuring users and processes have only the minimum levels of access necessary to perform their functions. In practice, this means carefully managing user permissions, service accounts, and application privileges. However, implementing PoLP in large organizations faces challenges such as balancing security with productivity, managing complex permission structures, and maintaining accurate access control lists. Organizations must establish clear policies, implement robust identity and access management systems, and conduct regular access reviews to ensure the principle is effectively maintained as roles and responsibilities evolve.

2. **Compare and contrast the security implications of using EFS versus BitLocker for data protection in an enterprise environment.**
   EFS (Encrypting File System) and BitLocker serve different but complementary security purposes. EFS provides file-level encryption, ideal for protecting individual files and folders with user-specific keys, making it perfect for multi-user systems where different users need access to different encrypted files. BitLocker, on the other hand, offers full-disk encryption, protecting all data on a volume, including system files, but lacks the granularity of EFS. In an enterprise, BitLocker is typically used for device protection (especially for laptops), while EFS is better suited for securing specific sensitive files. The main security consideration is that EFS relies on user credentials, so strong password policies are essential, while BitLocker can leverage TPM chips for additional security.

3. **What are the key considerations when designing a Windows Update deployment strategy for a 24/7 healthcare environment?**
   In a 24/7 healthcare environment, update deployment requires careful planning to ensure system availability while maintaining security. Key considerations include:
   - Scheduling updates during periods of lowest clinical activity
   - Implementing a phased rollout to test updates on non-critical systems first
   - Ensuring all medical devices and applications are compatible with updates
   - Maintaining detailed documentation of update history and rollback procedures
   - Training IT staff to handle update-related issues during off-hours
   - Implementing a robust monitoring system to detect update failures
   - Having a rollback plan for critical systems if updates cause issues
   - Coordinating with medical device manufacturers for specialized equipment updates

4. **How can Windows Event Logs be leveraged for proactive security monitoring, and what are the limitations of this approach?**
   Windows Event Logs are a valuable resource for security monitoring when properly configured and analyzed. They can be used to detect suspicious activities such as multiple failed login attempts, privilege escalation, and changes to security settings. Effective use involves:
   - Enabling detailed auditing for security-relevant events
   - Centralizing logs using SIEM (Security Information and Event Management) solutions
   - Creating custom alerts for critical security events
   - Establishing baseline behavior to identify anomalies
   
   However, there are limitations:
   - Logs can generate significant data volume, making it challenging to identify real threats
   - Attackers with administrative access can clear or modify logs
   - Some sophisticated attacks may not generate log entries
   - Proper log analysis requires skilled security personnel
   - Logs only show what happened, not the full context of an attack

5. **Discuss the trade-offs between security and usability when implementing User Account Control (UAC) in different organizational contexts.**
   UAC presents a classic security-usability trade-off. Higher UAC settings provide better security by requiring explicit approval for administrative actions but can lead to "alert fatigue" where users automatically approve prompts without reading them. In different contexts:
   - **Enterprise environments** may lower UAC slightly to reduce help desk calls while maintaining security through Group Policy
   - **Financial institutions** typically keep UAC at the highest setting due to the sensitive nature of their data
   - **Educational environments** might implement different UAC levels for staff (higher) versus students (lower but with restricted privileges)
   - **Healthcare** must balance security with the need for immediate access to patient information
   
   The key is to find the right balance where security is maintained without significantly impeding productivity, often through careful policy design and user education.

6. **What are the critical components of an effective endpoint security strategy beyond traditional antivirus software?**
   A comprehensive endpoint security strategy should include:
   - **Application whitelisting/blacklisting** to control which programs can run
   - **Endpoint Detection and Response (EDR)** solutions for advanced threat detection and response
   - **Data Loss Prevention (DLP)** to prevent sensitive data exfiltration
   - **Patch management** to ensure all systems are up-to-date
   - **Device control** to manage USB and peripheral access
   - **Network access control** to verify device compliance before granting network access
   - **Behavioral analysis** to detect anomalous activities
   - **Email and web security** to block phishing and malicious websites
   - **Mobile device management** for BYOD and mobile security
   - **Regular security awareness training** for all users

7. **How can organizations effectively balance the need for strong password policies with user convenience and the risk of password fatigue?**
   Organizations can balance security and usability through:
   - Implementing **password managers** to handle complex passwords
   - Adopting **passphrase policies** instead of complex character requirements
   - Implementing **multi-factor authentication (MFA)** to reduce reliance on password strength alone
   - Using **risk-based authentication** that adjusts requirements based on context
   - Implementing **single sign-on (SSO)** solutions to reduce the number of passwords users must remember
   - Providing **passwordless authentication** options where possible (e.g., Windows Hello, FIDO2 security keys)
   - Educating users on creating **memorable but strong** passphrases
   - Implementing **account lockout policies** that prevent brute force attacks without being overly restrictive

8. **What are the security implications of using Remote Desktop Protocol (RDP) in an enterprise environment, and how can these risks be mitigated?**
   RDP, while convenient, presents several security risks:
   - **Brute force attacks** on exposed RDP ports
   - **Credential theft** through keyloggers or phishing
   - **Vulnerability exploits** in the RDP protocol
   - **Lateral movement** if an attacker gains access
   
   Mitigation strategies include:
   - Using **Network Level Authentication (NLA)**
   - Implementing **account lockout policies**
   - Restricting RDP access through **firewall rules** and **VPN requirements**
   - Using **RDP Gateways** for secure remote access
   - Implementing **MFA** for RDP connections
   - Regularly **patching** all systems with RDP enabled
   - Monitoring for **suspicious RDP activity**
   - Using **restricted admin mode** or **Remote Credential Guard**

9. **How can organizations effectively manage and secure administrative privileges in a Windows environment to prevent privilege escalation attacks?**
   Effective privilege management involves:
   - Implementing the **principle of least privilege** for all accounts
   - Using **Privileged Access Workstations (PAWs)** for administrative tasks
   - Implementing **Just-In-Time (JIT) administrative access**
   - Using **Privileged Access Management (PAM)** solutions
   - Implementing **LAPS (Local Administrator Password Solution)**
   - Maintaining **separate admin and user accounts** for IT staff
   - Enforcing **strong authentication** for privileged accounts
   - Regularly **auditing privileged access** and permissions
   - Implementing **credential guarding** and **device guard** features

10. **What role does Windows Defender Application Control (WDAC) play in a defense-in-depth security strategy, and how does it compare to traditional application whitelisting?**
    Windows Defender Application Control (WDAC) is a powerful security feature that uses a deny-by-default approach to application execution. Unlike traditional application whitelisting, WDAC:
    - Uses **code integrity policies** to validate application binaries
    - Can enforce policies at the **kernel level**
    - Supports **dynamic code trust** for modern applications
    - Integrates with **Windows Defender ATP** for cloud-based intelligence
    - Can be **managed through Intune** for enterprise deployment
    
    In a defense-in-depth strategy, WDAC provides a critical layer of protection by preventing unauthorized code execution, even if other security controls are bypassed. It's particularly effective against fileless malware and zero-day exploits that might evade traditional signature-based detection.

## Summary

In this comprehensive lab, you've gained hands-on experience with essential Windows security controls that form the foundation of system security in both personal and enterprise environments. These practical exercises were designed to build your competency in securing Windows systems against common threats and vulnerabilities.

### What You've Done and Why It Matters

1. **Windows Firewall Configuration**
   - Implemented and configured Windows Firewall with Advanced Security
   - Created custom inbound and outbound rules to control network traffic
   - *Importance*: Firewalls serve as the first line of defense against network-based attacks, preventing unauthorized access while allowing legitimate traffic to pass through.

2. **User Account Management**
   - Created and managed local user accounts and groups
   - Implemented password policies and account lockout settings
   - *Importance*: Proper user account management ensures the principle of least privilege is followed, reducing the attack surface and limiting potential damage from compromised accounts.

3. **Data Protection with Encryption**
   - Explored BitLocker for full-disk encryption
   - Utilized EFS for file and folder-level encryption
   - *Importance*: Encryption protects sensitive data from unauthorized access, especially important for portable devices that might be lost or stolen.

4. **File System Security**
   - Configured NTFS permissions and shared folder permissions
   - Implemented inheritance and explicit permissions
   - *Importance*: Proper file system security ensures that only authorized users can access specific resources, protecting sensitive data from unauthorized viewing or modification.

5. **Windows Update Management**
   - Configured update settings and deployment options
   - Managed update schedules and maintenance windows
   - *Importance*: Regular updates patch security vulnerabilities, making this one of the most effective ways to protect systems from known exploits.

6. **Security Policies and Auditing**
   - Implemented local security policies
   - Configured audit policies and reviewed security logs
   - *Importance*: Security policies enforce consistent security settings across systems, while auditing provides accountability and helps detect potential security incidents.

7. **Windows Security Center**
   - Explored the unified security dashboard
   - Configured real-time protection and threat management
   - *Importance*: Centralized security management provides visibility into the security state of the system and helps detect and respond to threats.

### Real-World Applications

These skills are directly applicable to:
- Enterprise IT environments managing Windows workstations and servers
- Security operations centers monitoring for potential threats
- Compliance audits requiring specific security configurations
- Help desk and support roles troubleshooting security-related issues

### Continuing Your Security Journey

To further develop your Windows security expertise:
1. **Practice in a Lab Environment**: Set up a virtual lab to test different security configurations
2. **Stay Current**: Follow security bulletins from Microsoft and security research organizations
3. **Pursue Certifications**: Consider certifications like:
   - CompTIA Security+
   - Microsoft Certified: Security, Compliance, and Identity Fundamentals
   - Microsoft 365 Certified: Security Administrator Associate
4. **Join Security Communities**: Engage with professional networks to share knowledge and stay informed about emerging threats

Remember that security is an ongoing process, not a one-time configuration. Regular review and updating of security settings in response to new threats is essential for maintaining a secure computing environment.



## Next Steps

1. Practice these security configurations in different scenarios
2. Explore additional security features in Windows
3. Research and implement Group Policy for managing security settings in domain environments
4. Stay updated with the latest Windows security features and best practices

## References

Meyers, M. (2022). *CompTIA A+ Certification All-in-One Exam Guide, Eleventh Edition (Exams 220-1101 & 220-1102)*. McGraw-Hill Education.

National Institute of Standards and Technology. (2021). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800-53, Revision 5). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-53r5

Meyers, M. (2022). *Mike Meyers' CompTIA A+ Guide to Managing and Troubleshooting PCs, Seventh Edition (Exams 220-1101 & 220-1102)*. McGraw-Hill Education.

National Institute of Standards and Technology. (2018). *Guide to General Server Security* (NIST Special Publication 800-123). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-123

Prowse, D. (2022). *CompTIA A+ 220-1101 and 220-1102 Exam Cram*. Pearson IT Certification.

National Institute of Standards and Technology. (2020). *Guide to Enterprise Password Management* (NIST Special Publication 800-63B). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-63b

Clarke, G. (2022). *CompTIA A+ Certification Study Guide, Eleventh Edition (Exams 220-1101 & 220-1102)*. McGraw-Hill Education.

National Institute of Standards and Technology. (2018). *Guide to Securing Microsoft Windows 10* (NIST Special Publication 800-179). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-179

Simpson, J. (2022). *CompTIA A+ Complete Study Guide: Exam Core 1 220-1101 and Exam Core 2 220-1102*. Sybex.

National Institute of Standards and Technology. (2021). *Guide to Enterprise Patch Management Technologies* (NIST Special Publication 800-40, Revision 4). U.S. Department of Commerce. https://doi.org/10.6028/NIST.SP.800-40r4
