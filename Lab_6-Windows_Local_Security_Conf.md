

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


# Lab 6: Windows Local Security Configuration

## Introduction

This hands-on lab provides comprehensive practice in configuring and managing Windows local security settings—essential skills for IT professionals and CompTIA A+ certification candidates. Covering objectives from both the 220-1101 and 220-1102 exams, you'll develop proficiency in:

- Windows security configuration and hardening
- User account and permission management
- System protection and encryption implementation
- Security policy configuration and enforcement

Through guided exercises, you'll master both GUI and command-line techniques while learning industry best practices for securing Windows systems in professional environments.

## Learning Objectives

By completing this lab, you will be able to:

### Security Configuration

- Configure and manage Windows Defender Antivirus settings
- Implement Windows Firewall with Advanced Security rules
- Create and modify local security policies
- Configure encryption using EFS and BitLocker

### Account Management

- Create and manage local user accounts with appropriate permissions
- Configure User Account Control (UAC) settings
- Implement password policies and account restrictions
- Apply principle of least privilege to user accounts

### System Protection

- Configure Windows Update settings for security patches
- Implement file and folder permissions using NTFS
- Set up audit policies for security monitoring
- Configure system restore and backup options

### Policy Implementation

- Create and enforce password complexity requirements
- Configure account lockout policies
- Implement local Group Policy settings
- Monitor security events and logs

### Compliance & Best Practices

- Apply security baselines for different environments
- Document security configurations
- Troubleshoot common security issues
- Maintain compliance with security standards

### **Key Terms Covered in This Lab**

| #  | Key Term                     | Description                                                                 |
|----|------------------------------|-----------------------------------------------------------------------------|
| 1  | Windows Defender             | Built-in antivirus and anti-malware solution in Windows                    |
| 2  | Windows Firewall             | Network security system that monitors and controls network traffic          |
| 3  | User Account Control (UAC)   | Security feature that prevents unauthorized system changes                  |
| 4  | Local Security Policy        | Settings that control security behavior on a local computer                |
| 5  | NTFS Permissions            | File system permissions controlling access to files and folders             |
| 6  | Encrypting File System (EFS) | File encryption feature built into NTFS                                    |
| 7  | Password Policy             | Rules governing password complexity and usage                               |
| 8  | Account Lockout Policy      | Settings that lock accounts after failed login attempts                     |
| 9  | Windows Update              | Service for downloading and installing security patches                     |
| 10 | Security Baseline           | Standard security configuration for systems                                |
| 11 | Audit Policy                | Settings that determine which security events are logged                    |
| 12 | Principle of Least Privilege| Security concept of minimal necessary permissions                          |

### **Lab Task Overview**

| Task                                            | Description                                        |
|-------------------------------------------------|---------------------------------------------------|
| Configure Windows Defender Antivirus Settings   | Set up real-time protection and scan schedules   |
| Configure Windows Firewall with Advanced Security| Create inbound and outbound firewall rules       |
| Manage Local User Accounts                      | Create users and assign appropriate permissions   |
| Configure User Account Control (UAC) Levels     | Adjust UAC notification and protection levels     |
| Configure Encrypting File System (EFS)          | Encrypt files and manage certificates            |
| Manage NTFS Permissions                         | Set file and folder access permissions           |
| Configure Local Security Policy                 | Implement security policies via Local Policy      |
| Configure Windows Update Settings               | Manage update installation and scheduling        |
| Configure Password Policies                     | Set password complexity and expiration rules     |

### **CompTIA A+ Objective Mapping**

| Task Area                        | Exam Objective Reference                  |
|----------------------------------|-------------------------------------------|
| Windows Defender Configuration   | 2.2 Security Settings                     |
| Firewall Management             | 2.2 Security Settings                     |
| User Account Management         | 2.2 Security Settings                     |
| UAC Configuration               | 2.2 Security Settings                     |
| EFS Implementation              | 2.2 Security Settings                     |
| NTFS Permissions                | 2.2 Security Settings                     |
| Local Security Policy           | 2.2 Security Settings                     |
| Windows Update Configuration    | 1.6 Windows Settings                      |
| Password Policy Management      | 2.7 Workstation Security                  |

## Getting Started

Before beginning the hands-on tasks, follow these steps to access your virtual lab environment:

1. **Click** the **Start** button in your lab portal to provision the lab environment.
2. **Click** the computer image or "Launch VM" button in the right pane when the lab loads to open the Windows virtual machine window.
3. **Wait** for Windows 11 to finish booting. When you see the lock screen, **double-click** anywhere to reveal the login prompt.
4. **Select** the **Student** account (if prompted).
5. **Login** with the password `P@ssw0rd` (case sensitive).
6. **Ensure** you are logged in as an Administrator for this lab.
7. Once logged in, you are ready to begin the lab activities below.

If you encounter any issues starting the lab or logging in, notify your instructor for assistance.

---

Before you begin the hands-on tasks in this lab, you will gain practical experience implementing comprehensive Windows security configurations. You will learn to protect systems from malware, control network access, manage user permissions, and enforce security policies. These skills are essential for maintaining secure computing environments, protecting sensitive data, and ensuring compliance with organizational security requirements. Mastery of these tasks directly aligns with CompTIA A+ exam objectives, preparing you to demonstrate proficiency in Windows security configuration and management—critical competencies for IT security professionals.

## Task 1: Configure Windows Defender Antivirus Settings

### Objective: Antivirus Configuration and Management

1. **Open Windows Security**
   - Press `Win+I` to open Settings
   - Navigate to **Privacy & security** > **Windows Security**
   - Click **Open Windows Security**

2. **Check Protection Status**
   - Review the Security at a glance dashboard
   - Note any security recommendations or warnings
   - Click **Virus & threat protection**

3. **Configure Real-time Protection**
   - Under **Virus & threat protection settings**, click **Manage settings**
   - Ensure **Real-time protection** is **On**
   - Enable **Cloud-delivered protection**
   - Enable **Automatic sample submission**
   - Turn on **Tamper Protection**

4. **Configure Scan Options**
   - Return to main Virus & threat protection page
   - Click **Scan options**
   - Review available scan types:
     - Quick scan
     - Full scan
     - Custom scan
     - Microsoft Defender Offline scan

5. **Schedule a Scan**
   - Open **Task Scheduler** (`taskschd.msc`)
   - Navigate to **Task Scheduler Library** > **Microsoft** > **Windows** > **Windows Defender**
   - Right-click **Windows Defender Scheduled Scan**
   - Select **Properties** and configure schedule

6. **Add Exclusions**
   - Return to Virus & threat protection settings
   - Scroll to **Exclusions** and click **Add or remove exclusions**
   - Click **Add an exclusion** > **Folder**
   - Create and exclude a test folder: `C:\TestExclude`

7. **Update Definitions**
   - Click **Virus & threat protection updates**
   - Click **Check for updates**
   - Verify definitions are current

8. **Configure Ransomware Protection**
   - Click **Ransomware protection**
   - Turn on **Controlled folder access**
   - Click **Protected folders** to review default protected locations
   - Add a custom folder if needed

9. **Run a Quick Scan**
   - Return to main Virus & threat protection
   - Click **Quick scan**
   - Monitor scan progress and results

10. **Review Protection History**
    - Click **Protection history**
    - Review any recent detections or actions
    - Note quarantined items if any

**Challenge Question:**
What feature prevents unauthorized apps from encrypting your files?

**Answer:** Ransomware

**Task Summary:**
In this task, you configured Windows Defender Antivirus to provide comprehensive malware protection. You enabled real-time protection, cloud-based detection, and ransomware protection to defend against modern threats. This configuration ensures continuous monitoring for malicious software, automatic updates for the latest threat definitions, and protection of important folders from ransomware attacks. These settings form the first line of defense in a layered security approach.

## Task 2: Configure Windows Firewall with Advanced Security

### Objective: Network Security Configuration

1. **Open Windows Defender Firewall**
   - Press `Win+R`, type `wf.msc`, press Enter
   - Observe the Windows Defender Firewall with Advanced Security console

2. **Review Firewall Profiles**
   - In the center pane, review the three profiles:
     - Domain Profile
     - Private Profile
     - Public Profile
   - Note which profile is currently active

3. **Create an Inbound Rule**
   - Click **Inbound Rules** in left pane
   - Click **New Rule...** in Actions pane
   - Select **Port** and click **Next**
   - Choose **TCP** and enter port **8080**
   - Select **Allow the connection**
   - Apply to all profiles
   - Name it "Test Web Server Port 8080"
   - Click **Finish**

4. **Create an Outbound Rule**
   - Click **Outbound Rules**
   - Click **New Rule...**
   - Select **Program**
   - Browse to a test application (e.g., `C:\Windows\System32\ping.exe`)
   - Select **Block the connection**
   - Apply to all profiles
   - Name it "Block Ping Outbound"
   - Test by trying to ping a website

5. **Configure Connection Security Rules**
   - Click **Connection Security Rules**
   - Click **New Rule...**
   - Select **Isolation** and click **Next**
   - Choose **Require authentication for inbound and outbound connections**
   - Select authentication method
   - Apply to all profiles
   - Name it "Require Authentication Test"

6. **Monitor Active Connections**
   - Click **Monitoring** > **Firewall**
   - Review active firewall rules
   - Click **Connection Security Rules** to view active IPsec connections

7. **Configure Firewall Properties**
   - Right-click **Windows Defender Firewall with Advanced Security**
   - Select **Properties**
   - For each profile tab:
     - Set **Firewall state** to **On**
     - Configure **Inbound connections** to **Block (default)**
     - Set **Outbound connections** to **Allow (default)**

8. **Export Firewall Policy**
   - Right-click root node
   - Select **Export Policy...**
   - Save as `FirewallBackup.wfw`

9. **Test Firewall Rules**
   - Open Command Prompt
   - Test the blocked ping: `ping google.com`
   - Verify it fails due to firewall rule

10. **Disable Test Rules**
    - Return to Firewall console
    - Right-click your test rules
    - Select **Disable Rule**

**Challenge Question:**
Which firewall profile applies to untrusted networks?

**Answer:** Public

**Task Summary:**
In this task, you configured Windows Firewall with Advanced Security to control network traffic. You created rules to allow specific ports and block certain applications, demonstrating how firewalls protect systems from network-based attacks. The different profiles (Domain, Private, Public) provide flexibility to apply appropriate security levels based on network location. This granular control over network communications is essential for preventing unauthorized access and protecting against network-based threats.

## Task 3: Manage Local User Accounts

### Objective: User Account Administration

1. **Open Computer Management**
   - Right-click Start button, select **Computer Management**
   - Expand **Local Users and Groups**
   - Click **Users**

2. **Create a New User Account**
   - Right-click in the users pane
   - Select **New User...**
   - Enter the following:
     - User name: `TestUser01`
     - Full name: `Test User One`
     - Description: `Lab test account`
     - Password: `P@ssw0rd123`
     - Uncheck **User must change password at next logon**
     - Check **Password never expires** (for lab only)
   - Click **Create**, then **Close**

3. **Create a Limited User Account**
   - Create another user:
     - User name: `LimitedUser`
     - Password: `P@ssw0rd123`
     - Description: `Limited access account`

4. **Modify User Properties**
   - Double-click `TestUser01`
   - Click **Member Of** tab
   - Click **Add...**
   - Type `Remote Desktop Users` and click **OK**
   - Apply changes

5. **Create a New Group**
   - Click **Groups** in left pane
   - Right-click and select **New Group...**
   - Name: `LabUsers`
   - Description: `Lab testing group`
   - Click **Add..** to add members
   - Add `TestUser01` and `LimitedUser`
   - Click **Create**

6. **Set Account Restrictions**
   - Double-click `LimitedUser`
   - Check **Account is disabled**
   - Click **OK**
   - Re-enable the account

7. **Configure Account Expiration**
   - Double-click `TestUser01`
   - On **General** tab, check **Account expires**
   - Set expiration date to 30 days from today
   - Click **OK**

8. **Use Command Line Tools**
   - Open Command Prompt as Administrator
   - List users: `net user`
   - View user details: `net user TestUser01`
   - Create user via command: `net user TestUser02 P@ssw0rd123 /add`

9. **Configure User Rights**
   - Open Local Security Policy (`secpol.msc`)
   - Navigate to **Local Policies** > **User Rights Assignment**
   - Double-click **Allow log on locally**
   - Add `LabUsers` group
   - Click **OK**

10. **Test Account Access**
    - Lock computer (`Win+L`)
    - Try logging in as `TestUser01`
    - Verify access and group membership
    - Log back in as Administrator

**Challenge Question:**
Which group allows remote desktop connections?

**Answer:** Remote

**Task Summary:**
In this task, you created and managed local user accounts to implement proper access control. You applied the principle of least privilege by creating limited accounts and assigning only necessary permissions through group membership. This approach minimizes security risks by ensuring users have only the access required for their roles. Proper user account management is fundamental to system security and prevents unauthorized access to sensitive resources.

## Task 4: Configure User Account Control (UAC) Levels

### Objective: UAC Security Configuration

1. **Access UAC Settings**
   - Open Control Panel
   - Navigate to **User Accounts** > **User Accounts**
   - Click **Change User Account Control settings**

2. **Review UAC Levels**
   - Observe the slider with four levels:
     - Always notify (highest)
     - Default (notify only when apps try to make changes)
     - Notify only when apps try to make changes (do not dim desktop)
     - Never notify (lowest)

3. **Test Current UAC Level**
   - Note current slider position
   - Open Command Prompt as Administrator
   - Observe UAC prompt behavior

4. **Change UAC Level**
   - Move slider to highest setting
   - Click **OK**
   - Accept UAC prompt to apply changes
   - Restart required for some changes

5. **Configure via Local Security Policy**
   - Open `secpol.msc`
   - Navigate to **Local Policies** > **Security Options**
   - Find UAC-related policies:
     - Admin Approval Mode for the Built-in Administrator account
     - Behavior of the elevation prompt for administrators
     - Behavior of the elevation prompt for standard users

6. **Modify UAC Policies**
   - Double-click **User Account Control: Behavior of the elevation prompt for administrators**
   - Change to **Prompt for consent on the secure desktop**
   - Click **OK**

7. **Configure Application Elevation**
   - Right-click an application (e.g., Notepad)
   - Select **Properties** > **Compatibility** tab
   - Check **Run this program as an administrator**
   - Apply changes

8. **Test UAC with Different Settings**
   - Try to modify system settings
   - Install a program
   - Access protected folders
   - Note UAC behavior differences

9. **Use Registry to View UAC Settings**
   - Open Registry Editor
   - Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System`
   - Review UAC-related values:
     - EnableLUA
     - ConsentPromptBehaviorAdmin
     - PromptOnSecureDesktop

10. **Reset to Recommended Settings**
    - Return UAC slider to default position
    - Verify with a test requiring elevation
    - Document the security impact of each level

**Challenge Question:**
What is the recommended UAC notification level?

**Answer:** Default

**Task Summary:**
In this task, you configured User Account Control to prevent unauthorized system changes. UAC creates a security boundary between standard user operations and administrative tasks, requiring explicit consent for elevated privileges. This protection prevents malware from silently gaining administrative access and alerts users when programs attempt system modifications. The different UAC levels allow organizations to balance security needs with user productivity requirements.

## Task 5: Configure Encrypting File System (EFS)

### Objective: File Encryption Implementation

1. **Create Test Files and Folders**
   - Create folder: `C:\EFSTest`
   - Create text file: `C:\EFSTest\Confidential.txt`
   - Add content: "This is confidential data"
   - Create subfolder: `C:\EFSTest\SecureData`

2. **Encrypt a File**
   - Right-click `Confidential.txt`
   - Select **Properties**
   - Click **Advanced...**
   - Check **Encrypt contents to secure data**
   - Click **OK** twice
   - Choose to encrypt file only

3. **Encrypt a Folder**
   - Right-click `SecureData` folder
   - Properties > Advanced
   - Check **Encrypt contents to secure data**
   - Apply to folder, subfolders, and files
   - Notice green text color for encrypted items

4. **View Encryption Details**
   - Open Command Prompt
   - Navigate to `C:\EFSTest`
   - Run: `cipher /c Confidential.txt`
   - Note encryption algorithm and certificate thumbprint

5. **Back Up EFS Certificate**
   - Press `Win+R`, type `certmgr.msc`
   - Navigate to **Personal** > **Certificates**
   - Find your EFS certificate
   - Right-click > **All Tasks** > **Export...**
   - Export with private key
   - Use strong password
   - Save as `EFSBackup.pfx`

6. **Share Encrypted File**
   - Right-click encrypted file
   - Properties > Advanced > Details
   - Click **Add** to add another user
   - Select a user who has an EFS certificate
   - Apply changes

7. **Test Access with Another User**
   - Create new local user: `EFSTestUser`
   - Log in as that user
   - Try to access encrypted file
   - Verify access is denied

8. **Use Cipher Command**
   - As administrator, open Command Prompt
   - Encrypt all files in folder: `cipher /e /s:C:\EFSTest`
   - Display encryption info: `cipher /c /s:C:\EFSTest`
   - Create new recovery agent: `cipher /r:EFSRecovery`

9. **Configure EFS Recovery Policy**
   - Open `gpedit.msc` (if available)
   - Navigate to **Computer Configuration** > **Windows Settings** > **Security Settings** > **Public Key Policies**
   - Right-click **Encrypting File System**
   - Add Data Recovery Agent if needed

10. **Decrypt Files**
    - Right-click encrypted file
    - Properties > Advanced
    - Uncheck **Encrypt contents**
    - Apply to test decryption
    - Re-encrypt when complete

**Challenge Question:**
What color indicates EFS encrypted files in File Explorer?

**Answer:** Green

**Task Summary:**
In this task, you implemented file-level encryption using EFS to protect sensitive data. EFS provides transparent encryption that protects files from unauthorized access while remaining invisible to authorized users. You learned the critical importance of backing up encryption certificates, as losing them means permanent data loss. This encryption method is ideal for protecting confidential files on shared computers or in case of device theft.

## Task 6: Manage NTFS Permissions

### Objective: File System Security

1. **Create Test Structure**
   - Create folder: `C:\NTFSTest`
   - Create subfolders:
     - `C:\NTFSTest\Public`
     - `C:\NTFSTest\Private`
     - `C:\NTFSTest\ReadOnly`

2. **View Current Permissions**
   - Right-click `C:\NTFSTest`
   - Select **Properties** > **Security** tab
   - Review default permissions
   - Click **Advanced** for detailed view

3. **Modify Basic Permissions**
   - Select **Users** group
   - Click **Edit...**
   - Check **Modify** permission
   - Uncheck **Delete** under Deny
   - Apply changes

4. **Set Advanced Permissions**
   - Click **Advanced** button
   - Click **Disable inheritance**
   - Choose **Convert inherited permissions**
   - Select a permission entry
   - Click **Edit** to modify

5. **Configure Private Folder**
   - Right-click `Private` folder
   - Security > Edit
   - Remove **Users** group
   - Add specific user: `TestUser01`
   - Grant **Full Control**

6. **Set Read-Only Permissions**
   - Configure `ReadOnly` folder
   - Remove all permissions except Administrators
   - Add **Everyone** group
   - Grant only **Read & Execute** permissions

7. **Configure Auditing**
   - In Advanced Security Settings
   - Click **Auditing** tab
   - Click **Add**
   - Select **Everyone**
   - Audit successful and failed **Delete** attempts

8. **Test Effective Permissions**
   - In Advanced Security Settings
   - Click **Effective Access** tab
   - Select a user to test
   - Click **View effective access**
   - Review calculated permissions

9. **Use Command Line Tools**
   - Open Command Prompt as Administrator
   - View permissions: `icacls C:\NTFSTest`
   - Grant permission: `icacls C:\NTFSTest\Public /grant TestUser01:(OI)(CI)M`
   - Remove permission: `icacls C:\NTFSTest\Private /remove Users`

10. **Take Ownership**
    - Create file in Private folder as Administrator
    - Log in as TestUser01
    - Try to access file
    - As Administrator, change owner to TestUser01
    - Verify access changes

**Challenge Question:**
Which NTFS permission includes all other permissions?

**Answer:** Full

**Task Summary:**
In this task, you configured NTFS permissions to control file and folder access at a granular level. NTFS permissions provide detailed security control, allowing you to specify exactly what users can do with files and folders. You implemented the principle of least privilege by granting only necessary permissions and learned how permission inheritance affects security. This fine-grained access control is essential for protecting sensitive data and maintaining proper separation of user access in multi-user environments.

## Task 7: Configure Local Security Policy

### Objective: Security Policy Implementation

1. **Open Local Security Policy**
   - Press `Win+R`, type `secpol.msc`
   - Press Enter
   - Explore the policy categories

2. **Configure Account Policies**
   - Expand **Account Policies**
   - Click **Password Policy**
   - Double-click **Minimum password length**
   - Set to **12 characters**
   - Click **OK**

3. **Set Password Complexity**
   - Double-click **Password must meet complexity requirements**
   - Select **Enabled**
   - Click **OK**
   - Review complexity requirements

4. **Configure Account Lockout**
   - Click **Account Lockout Policy**
   - Set **Account lockout threshold** to **5 invalid attempts**
   - Set **Account lockout duration** to **30 minutes**
   - Set **Reset account lockout counter** to **30 minutes**

5. **Configure Security Options**
   - Navigate to **Local Policies** > **Security Options**
   - Enable **Interactive logon: Do not display last user name**
   - Enable **Interactive logon: Require Domain Controller authentication**

6. **Set Audit Policies**
   - Go to **Local Policies** > **Audit Policy**
   - Enable **Audit account logon events** - Success and Failure
   - Enable **Audit object access** - Failure
   - Enable **Audit policy change** - Success and Failure

7. **Configure User Rights**
   - Click **User Rights Assignment**
   - Double-click **Shut down the system**
   - Add or remove users as needed
   - Configure **Access this computer from the network**

8. **Export Security Settings**
   - Right-click **Security Settings**
   - Select **Export policy...**
   - Save as `SecurityPolicy.inf`

9. **Apply Security Template**
   - Open Command Prompt as Administrator
   - Apply template: `secedit /configure /db security.sdb /cfg SecurityPolicy.inf`
   - Analyze current settings: `secedit /analyze /db security.sdb`

10. **Verify Policy Application**
    - Open Event Viewer
    - Check Security log for policy changes
    - Test password change with new requirements
    - Verify audit events are being logged

**Challenge Question:**
What tool configures local security policies?

**Answer:** secpol

**Task Summary:**
In this task, you configured local security policies to enforce organizational security requirements. These policies control authentication, auditing, and user rights across the system. By implementing password policies, account lockout settings, and audit policies, you created a security framework that protects against unauthorized access while maintaining accountability through logging. Local security policies form the foundation of Windows security hardening and compliance efforts.

## Task 8: Configure Windows Update Settings

### Objective: Update Management

1. **Access Windows Update**
   - Open Settings (`Win+I`)
   - Navigate to **Windows Update**
   - Review current update status

2. **Check for Updates**
   - Click **Check for updates**
   - Wait for scan to complete
   - Review available updates
   - Note update classifications

3. **Configure Active Hours**
   - Click **Advanced options**
   - Under Active hours, click **Change**
   - Set your typical work hours
   - Windows won't restart during these hours

4. **Configure Update Options**
   - In Advanced options:
   - Toggle **Receive updates for other Microsoft products**
   - Enable **Download updates over metered connections**
   - Configure **Notify me when a restart is required**

5. **Pause Updates**
   - Click **Pause updates**
   - Select pause duration (up to 5 weeks)
   - Note when updates will resume
   - Click **Resume updates** to test

6. **Configure Delivery Optimization**
   - Click **Advanced options** > **Delivery Optimization**
   - Choose download source:
     - PCs on my local network
     - PCs on the Internet
   - Set bandwidth limits if needed

7. **View Update History**
   - Return to Windows Update
   - Click **Update history**
   - Review successful installations
   - Check for failed updates
   - Click **Uninstall updates** if needed

8. **Configure via Group Policy**
   - Open `gpedit.msc` (if available)
   - Navigate to **Computer Configuration** > **Administrative Templates** > **Windows Components** > **Windows Update**
   - Configure **Configure Automatic Updates**
   - Set to **4 - Auto download and schedule the install**

9. **Use Windows Update CLI**
   - Open PowerShell as Administrator
   - Check for updates: `Get-WindowsUpdate` (if module installed)
   - View update history: `Get-WUHistory`
   - Install updates: `Install-WindowsUpdate`

10. **Configure Update Notifications**
    - In Settings > System > Notifications
    - Ensure Windows Update notifications are enabled
    - Test by checking for updates
    - Verify notification appears

**Challenge Question:**
How many days can you pause Windows updates?

**Answer:** 35

**Task Summary:**
In this task, you configured Windows Update to maintain system security through timely patch installation. Regular updates protect against newly discovered vulnerabilities and provide security improvements. You learned to balance security needs with productivity by configuring active hours and update schedules. Proper update management is critical for maintaining a secure environment, as unpatched systems are primary targets for attackers exploiting known vulnerabilities.

## Task 9: Configure Password Policies

### Objective: Password Security Management

1. **Open Local Group Policy**
   - Press `Win+R`, type `gpedit.msc`
   - Navigate to **Computer Configuration** > **Windows Settings** > **Security Settings** > **Account Policies** > **Password Policy**

2. **Set Password History**
   - Double-click **Enforce password history**
   - Set to **24 passwords remembered**
   - This prevents password reuse
   - Click **OK**

3. **Configure Maximum Password Age**
   - Double-click **Maximum password age**
   - Set to **90 days**
   - This forces regular password changes
   - Apply setting

4. **Set Minimum Password Age**
   - Double-click **Minimum password age**
   - Set to **1 day**
   - Prevents immediate password cycling
   - Click **OK**

5. **Configure Complexity Requirements**
   - Double-click **Password must meet complexity requirements**
   - Enable this setting
   - Review requirements:
     - Not contain username
     - At least 6 characters (overridden by minimum length)
     - Contains 3 of 4 character types

6. **Set Minimum Length**
   - Double-click **Minimum password length**
   - Set to **14 characters**
   - This exceeds the 12 from earlier for enhanced security
   - Apply change

7. **Configure Fine-Grained Policies**
   - Open **Active Directory Administrative Center** (if available)
   - Navigate to **System** > **Password Settings Container**
   - Create new Password Settings Object (PSO)
   - Apply more restrictive settings to specific groups

8. **Test Password Policy**
   - Try to change a user password
   - Test with non-compliant password: `simple`
   - Test with compliant password: `C0mpl3x!P@ssw0rd`
   - Verify policy enforcement

9. **Document Policy Settings**
   - Open Command Prompt
   - Export policy: `secedit /export /cfg PasswordPolicy.inf /areas SECURITYPOLICY`
   - Review exported file
   - Document all password requirements

10. **Create Policy Exception**
    - For service accounts that need non-expiring passwords
    - Create separate OU or group
    - Apply different PSO or local policy
    - Document exceptions carefully

**Challenge Question:**
How many character types must complex passwords contain?

**Answer:** Three

**Task Summary:**
In this task, you configured comprehensive password policies to enforce strong authentication. Strong passwords are the first line of defense against unauthorized access, and these policies ensure users create passwords that resist common attack methods. By requiring length, complexity, and regular changes while preventing reuse, you significantly reduced the risk of password-based attacks. These policies must balance security with usability to ensure user compliance and minimize support issues.

## Discussion Questions

**Discussion Questions and Answers**

1. **Why is it important to configure different Windows Firewall profiles?**
   **Answer:** Different firewall profiles (Domain, Private, Public) allow appropriate security levels for different network environments. The Public profile should be most restrictive for untrusted networks like coffee shops, while Domain profiles can be more permissive within trusted corporate networks. This flexibility ensures security without hindering productivity.

2. **What are the security implications of disabling UAC entirely?**
   **Answer:** Disabling UAC removes a critical security boundary that prevents unauthorized elevation of privileges. Without UAC, malware can silently gain administrative access, users might unknowingly make harmful system changes, and there's no notification when programs attempt to modify protected areas. This significantly increases the risk of system compromise.

3. **How do NTFS permissions and share permissions interact?**
   **Answer:** When accessing files over a network, both NTFS and share permissions apply, and the most restrictive permission takes precedence. NTFS permissions apply whether accessing locally or over network, while share permissions only apply to network access. Best practice is to set share permissions to "Everyone - Full Control" and use NTFS permissions for actual security control.

4. **What's the difference between EFS and BitLocker encryption?**
   **Answer:** EFS encrypts individual files and folders at the file system level, using certificates tied to user accounts. It's transparent to the logged-in user but protects against other users. BitLocker encrypts entire drives at the disk level, protecting against offline attacks and theft. EFS is better for multi-user systems where users need private files, while BitLocker protects against physical theft of devices.

5. **Why should password policies balance security with usability?**
   **Answer:** Overly complex password policies can lead to poor security practices like writing passwords down, using predictable patterns, or increased help desk calls for resets. A balanced approach (12-14 character minimum, complexity requirements, 90-day expiration) provides strong security while remaining manageable for users. Consider implementing password managers to help users cope with complexity requirements.

## Summary

In this comprehensive Windows Local Security Configuration lab, you gained hands-on experience implementing multiple layers of security controls. You performed critical security tasks including:

- Configuring Windows Defender Antivirus with real-time protection and ransomware defense
- Implementing Windows Firewall rules to control network access
- Creating and managing local user accounts with appropriate permissions
- Adjusting UAC levels to balance security and usability
- Encrypting sensitive files using EFS
- Setting granular NTFS permissions for access control
- Implementing local security policies and audit settings
- Managing Windows Update for security patches
- Enforcing strong password policies

**What you did:**
You followed detailed procedures to configure each security component, tested the effectiveness of your configurations, and learned to use both GUI and command-line tools. Each task built upon previous ones to create a comprehensive security posture for a Windows system.

**Why you did it:**
These security configurations are essential for protecting Windows systems from various threats including malware, unauthorized access, and data breaches. By implementing defense-in-depth strategies, you learned to create multiple security layers that work together to protect systems and data. These skills directly address real-world security challenges IT professionals face daily.

**How it will help you in the future:**
Mastering Windows security configuration prepares you for roles in IT security, system administration, and support. You'll be able to secure endpoints, implement organizational security policies, respond to security incidents, and maintain compliance with security standards. These skills are highly valued in the industry and directly align with CompTIA A+ 220-1102 security objectives, preparing you for both certification success and real-world IT security challenges.

The knowledge gained from this lab forms a foundation for more advanced security concepts and prepares you to protect organizational assets in an increasingly threat-filled digital landscape.

## References

1. Microsoft. (2023). *Windows Security deployment guide*. Microsoft Learn. [https://learn.microsoft.com/en-us/windows/security/operating-system-security/windows-security-deployment-guide](https://learn.microsoft.com/en-us/windows/security/operating-system-security/windows-security-deployment-guide)

2. National Institute of Standards and Technology. (2020). *Guide to General Server Security* (NIST Special Publication 800-123). [https://doi.org/10.6028/NIST.SP.800-123](https://doi.org/10.6028/NIST.SP.800-123)

3. Center for Internet Security. (2023). *CIS Microsoft Windows 10 Enterprise Benchmark v2.0.0*. [https://www.cisecurity.org/benchmark/microsoft_windows_desktop](https://www.cisecurity.org/benchmark/microsoft_windows_desktop)

4. Microsoft. (2023). *Configure Windows Defender Firewall with Advanced Security*. Microsoft Learn. [https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/windows-firewall-with-advanced-security)

5. Russinovich, M., Solomon, D., & Ionescu, A. (2023). *Windows Internals, Part 1* (7th ed.). Microsoft Press.

6. CompTIA. (2024). *CompTIA A+ Certification Exam Objectives Core 2 (220-1102)*. [https://www.comptia.org/certifications/a](https://www.comptia.org/certifications/a)

7. National Institute of Standards and Technology. (2022). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800-53, Revision 5). [https://doi.org/10.6028/NIST.SP.800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5)

8. Plett, E., & Poggemeyer, L. (2023). *Implementing and managing Windows security features*. In *Windows Security Monitoring: Essential Skills* (pp. 145-201). Apress.

9. Stewart, J. M., Chapple, M., & Gibson, D. (2021). *CompTIA Security+ Study Guide: Exam SY0-601* (9th ed.). Sybex.

10. Sans Institute. (2023). *Windows Security Hardening: Essential Steps for Securing Windows Systems*. SANS Security Awareness. [https://www.sans.org/white-papers/](https://www.sans.org/white-papers/)
