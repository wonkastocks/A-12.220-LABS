

## Task List


| Task                           |
|--------------------------------|
| Configure Strong Passwords     |
| Enable Account Lockout Policies|
| Configure Firewall Settings    |
| Update Operating System        |
| Update Applications           |
| Disable Unnecessary Services   |
| Manage User Account Permissions|
| Configure Screen Lock Settings |
| Implement Data Encryption      |
| Configure Automatic Updates    |






## Task/Objective


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Configure Strong Passwords     | 4.0 Operational Procedures                                        |
| Enable Account Lockout Policies| 4.0 Operational Procedures                                        |
| Configure Firewall Settings    | 4.0 Operational Procedures                                        |
| Update Operating System        | 1.0 Operating Systems                                             |
| Update Applications           | 4.0 Operational Procedures                                        |
| Disable Unnecessary Services   | 4.0 Operational Procedures                                        |
| Manage User Account Permissions| 4.0 Operational Procedures                                        |
| Configure Screen Lock Settings | 4.0 Operational Procedures                                        |
| Implement Data Encryption      | 1.101.0  |  Operating Systems: Given a scenario, install and configure cloud-based productivity tools.     |
| Configure Automatic Updates    | 4.0 Operational Procedures                                        |

---


# Lab 10: System Hardening

## Introduction

This hands-on lab provides comprehensive practice in implementing system hardening techniques—critical skills for IT professionals and CompTIA A+ certification candidates. Covering objectives from the 220-1202 exam, you'll develop proficiency in securing Windows systems through systematic configuration of security controls, user account management, service hardening, and data protection measures.

Through guided exercises, you'll master essential hardening practices including password policy enforcement, account lockout configuration, firewall management, service minimization, permission control, screen lock implementation, data encryption, and automated update configuration. These skills are fundamental for creating secure computing environments that resist both external attacks and internal security breaches while maintaining system functionality and user productivity.

## Learning Objectives

By completing this lab, you will be able to:

### Security Policy Implementation
• Configure comprehensive password policies and enforcement mechanisms
• Implement account lockout policies for failed authentication attempts
• Manage user account permissions and privilege restrictions
• Configure screen lock settings for unauthorized access prevention

### System Configuration Hardening
• Configure and manage Windows Firewall settings
• Disable unnecessary services and minimize attack surface
• Update operating systems and applications systematically
• Implement data encryption for information protection

### Access Control Management
• Establish principle of least privilege for user accounts
• Configure automatic update mechanisms for security patches
• Implement screen saver policies with password protection
• Manage service accounts and system-level permissions

### Key Terms Covered in This Lab

| # | Key Term | Description |
|---|----------|-------------|
| 1 | System Hardening | Process of securing computer systems by reducing vulnerabilities |
| 2 | Attack Surface | Total number of possible entry points for unauthorized access |
| 3 | Principle of Least Privilege | Security concept limiting user access to minimum required resources |
| 4 | Service Minimization | Disabling unnecessary services to reduce security exposure |
| 5 | Data Encryption | Process of converting data into coded format to prevent unauthorized access |
| 6 | Account Lockout | Security mechanism that disables accounts after failed login attempts |
| 7 | Screen Lock | Security feature requiring authentication to access active sessions |
| 8 | Group Policy | Windows administrative template system for managing security settings |
| 9 | BitLocker | Microsoft's full disk encryption technology |
| 10 | Windows Update | Microsoft's system for delivering security patches and updates |
| 11 | User Account Control | Windows security feature preventing unauthorized system changes |
| 12 | Firewall Rules | Network traffic filtering configurations for security protection |

### Lab Task Overview

| Task | Description |
|------|-------------|
| Configure Strong Passwords | Establish robust password requirements and policies |
| Enable Account Lockout Policies | Implement failed authentication attempt protection |
| Configure Firewall Settings | Strengthen network protection and traffic filtering |
| Update Operating System | Apply security patches and system updates |
| Update Applications | Maintain current software versions for security |
| Disable Unnecessary Services | Minimize system attack surface and exposure |
| Manage User Account Permissions | Implement principle of least privilege access |
| Configure Screen Lock Settings | Establish session security and timeout policies |
| Implement Data Encryption | Protect sensitive information through encryption |
| Configure Automatic Updates | Establish ongoing security maintenance procedures |

### CompTIA A+ Objective Mapping

| Task Area | Exam Objective Reference |
|-----------|-------------------------|
| System Hardening | 2.7 Given a scenario, apply workstation security options and hardening techniques |
| Password Security | 2.2 Given a scenario, configure and apply basic Microsoft Windows OS security settings |
| User Account Management | 2.2 Given a scenario, configure and apply basic Microsoft Windows OS security settings |
| Firewall Configuration | 2.10 Given a scenario, apply security settings on SOHO wireless and wired networks |
| Data Encryption | 1.11 Given a scenario, install and configure cloud-based productivity tools |
| Update Management | 4.0 Operational Procedures |
| Service Management | 4.0 Operational Procedures |
| Access Control | 4.0 Operational Procedures |

## Getting Started

Before beginning the hands-on tasks, follow these steps to access your virtual lab environment:

1. **Click** the **Start** button in your lab portal to provision the lab environment.

2. **Click** the computer image or "Launch VM" button in the right pane when the lab loads to open the Windows virtual machine window.

3. **Wait** for Windows 11 to finish booting. When you see the lock screen, **double-click** anywhere to reveal the login prompt.

4. **Select** the **Student** account (if prompted).

5. **Login** with the password `P@ssw0rd` (case sensitive).

6. Once logged in, you are ready to begin the lab activities below.

If you encounter any issues starting the lab or logging in, notify your instructor for assistance.

---

Before you begin the hands-on tasks in this lab, you will gain practical experience implementing system hardening techniques that are critical for maintaining secure computing environments. You will learn to systematically reduce system vulnerabilities, configure protective policies, and establish ongoing security maintenance procedures using real-world tools and workflows. These skills are essential for creating defense-in-depth strategies that protect against both external threats and internal security risks. Mastery of these tasks directly aligns with CompTIA A+ exam objectives and prepares you for professional system security responsibilities.

## Task 1: Configure Strong Passwords

### Objective: Establish robust password requirements

1. **Press** `Win + R` and type `gpedit.msc`

2. **Press** **Enter** to open Group Policy Editor

3. **Navigate** to **Computer Configuration > Windows Settings > Security Settings > Account Policies > Password Policy**

4. **Double-click** **Minimum password length**

5. **Set** the value to **12** characters and click **OK**

6. **Double-click** **Password must meet complexity requirements**

7. **Select** **Enabled** and click **OK**

8. **Double-click** **Maximum password age**

9. **Set** the value to **90** days and click **OK**

10. **Double-click** **Enforce password history** and set to **24** passwords

**Challenge Question:**
What is the minimum recommended length for secure passwords?

**Answer:** Twelve

**Task Summary:**
You configured comprehensive password policies that establish strong authentication requirements for system access. These policies prevent weak passwords that are easily compromised through dictionary attacks or brute force attempts, creating a fundamental security barrier that protects against unauthorized access and credential-based threats.

## Task 2: Enable Account Lockout Policies

### Objective: Implement failed authentication attempt protection

1. **In Group Policy Editor**, navigate to **Account Policies > Account Lockout Policy**

2. **Double-click** **Account lockout threshold**

3. **Set** the value to **5** invalid logon attempts

4. **Click** **OK**

5. **Double-click** **Account lockout duration**

6. **Set** the value to **30** minutes

7. **Click** **OK**

8. **Double-click** **Reset account lockout counter after**

9. **Set** the value to **30** minutes and click **OK**

10. **Close** Group Policy Editor and run `gpupdate /force` in Command Prompt

**Challenge Question:**
What policy prevents automated password guessing attacks?

**Answer:** Lockout

**Task Summary:**
You implemented account lockout policies that automatically disable user accounts after multiple failed login attempts. This protection prevents brute force password attacks and limits the effectiveness of automated credential guessing tools while providing time for administrators to investigate potential security incidents.

## Task 3: Configure Firewall Settings

### Objective: Strengthen network protection and traffic filtering

1. **Open** **Windows Defender Firewall with Advanced Security**

2. **Click** **Windows Defender Firewall Properties**

3. **Set** **Domain Profile** firewall state to **On**

4. **Set** **Inbound connections** to **Block (default)**

5. **Set** **Outbound connections** to **Allow (default)**

6. **Configure** **Private Profile** with same settings

7. **Configure** **Public Profile** with same settings

8. **Click** **Inbound Rules** and review existing rules

9. **Create** a new rule to block a specific port (e.g., port 23 for Telnet)

10. **Test** firewall effectiveness with network connectivity tools

**Challenge Question:**
What security feature controls network traffic between computers?

**Answer:** Firewall

**Task Summary:**
You configured Windows Firewall to provide comprehensive network protection by blocking unauthorized inbound connections while allowing legitimate outbound communications. Proper firewall configuration creates a network perimeter that prevents external attacks and limits the spread of malware across network connections.

## Task 4: Update Operating System

### Objective: Apply security patches and system updates

1. **Open** **Settings** and navigate to **Update & Security**

2. **Click** **Check for updates**

3. **Install** all available Critical and Important updates

4. **Click** **View optional updates** and review driver updates

5. **Select** important driver updates and install them

6. **Configure** **Active hours** to prevent automatic restarts during work

7. **Set** **Restart options** to schedule outside business hours

8. **Enable** **Download updates over metered connections** if required

9. **Review** **Update history** to verify successful installations

10. **Schedule** regular update checks and installations

**Challenge Question:**
What Windows service delivers security patches and bug fixes?

**Answer:** Update

**Task Summary:**
You applied comprehensive operating system updates that eliminate known security vulnerabilities and improve system stability. Regular system updates are essential for maintaining security against current threats and ensuring compatibility with security tools and applications.

## Task 5: Update Applications

### Objective: Maintain current software versions for security

1. **Open** **Microsoft Store** from the Start menu

2. **Click** **Library** in the bottom navigation

3. **Click** **Get updates** to refresh all Store applications

4. **Wait** for updates to download and install

5. **Open** **Control Panel > Programs and Features**

6. **Review** installed programs for available updates

7. **Check** critical applications like browsers, PDF readers, and office software

8. **Update** Adobe Acrobat Reader, Java, and other common applications

9. **Configure** automatic update settings where available

10. **Document** application versions and update schedules

**Challenge Question:**
What should be regularly updated to prevent security vulnerabilities?

**Answer:** Applications

**Task Summary:**
You updated critical applications to their latest versions, eliminating known security vulnerabilities that attackers commonly exploit. Application updates are essential for maintaining security as software vendors regularly patch discovered vulnerabilities and improve security features.

## Task 6: Disable Unnecessary Services

### Objective: Minimize system attack surface and exposure

1. **Press** `Win + R` and type `services.msc`

2. **Press** **Enter** to open Services console

3. **Review** the list of running services

4. **Right-click** **Fax** service and select **Properties**

5. **Set** **Startup type** to **Disabled** and click **Stop**

6. **Right-click** **Remote Registry** service and disable it

7. **Disable** **Telephony** service if not needed

8. **Review** **Print Spooler** service (disable only if no printing required)

9. **Disable** **Windows Search** if indexing is not needed

10. **Document** disabled services and their impact on functionality

**Challenge Question:**
What process reduces system vulnerability by removing unused features?

**Answer:** Disable

**Task Summary:**
You disabled unnecessary Windows services to reduce the system's attack surface and minimize potential security vulnerabilities. Service minimization is a critical hardening technique that eliminates unused functionality that could be exploited by attackers while improving system performance.

## Task 7: Manage User Account Permissions

### Objective: Implement principle of least privilege access

1. **Open** **Computer Management** from Administrative Tools

2. **Navigate** to **Local Users and Groups > Users**

3. **Create** a new user account called "TestUser"

4. **Right-click** **TestUser** and select **Properties**

5. **Click** **Member Of** tab and remove from **Users** group if needed

6. **Add** user to **Power Users** group only

7. **Configure** **Account** tab to set logon hours restrictions

8. **Set** account to expire after 30 days

9. **Test** login with restricted account to verify limitations

10. **Document** permission levels and access restrictions

**Challenge Question:**
What security principle limits user access to minimum required resources?

**Answer:** Privilege

**Task Summary:**
You implemented the principle of least privilege by configuring user accounts with minimal necessary permissions. This approach reduces security risks by limiting the potential impact of compromised accounts and prevents users from making unauthorized system changes.

## Task 8: Configure Screen Lock Settings

### Objective: Establish session security and timeout policies

1. **Open** **Group Policy Editor** (`gpedit.msc`)

2. **Navigate** to **Computer Configuration > Administrative Templates > Control Panel > Personalization**

3. **Double-click** **Enable screen saver**

4. **Select** **Enabled** and click **OK**

5. **Double-click** **Screen saver timeout**

6. **Set** to **Enabled** and specify **900** seconds (15 minutes)

7. **Double-click** **Password protect the screen saver**

8. **Select** **Enabled** and click **OK**

9. **Navigate** to **User Configuration > Administrative Templates > System > Power Management > Video and Display Settings**

10. **Configure** **Turn off the display** timeout settings

**Challenge Question:**
What security feature automatically locks unattended computer sessions?

**Answer:** Screen

**Task Summary:**
You configured automated screen lock policies that protect unattended computer sessions from unauthorized access. Screen lock settings ensure that systems automatically require authentication after periods of inactivity, preventing unauthorized users from accessing active sessions.

## Task 9: Implement Data Encryption

### Objective: Protect sensitive information through encryption

1. **Open** **Control Panel > System and Security > BitLocker Drive Encryption**

2. **Click** **Turn on BitLocker** for the system drive (if available)

3. **Choose** how to unlock the drive (password or smart card)

4. **Create** a strong encryption password

5. **Save** the recovery key to a secure location

6. **Select** encryption options (encrypt used disk space only)

7. **Run** BitLocker system check

8. **Start** the encryption process

9. **Create** an encrypted folder using **Encrypting File System (EFS)**

10. **Test** file encryption by creating and encrypting a test file

**Challenge Question:**
What technology protects data by converting it to unreadable format?

**Answer:** Encryption

**Task Summary:**
You implemented BitLocker disk encryption and EFS file encryption to protect sensitive data from unauthorized access. Data encryption ensures that even if systems are physically compromised, the stored information remains protected and unreadable to unauthorized users.

## Task 10: Configure Automatic Updates

### Objective: Establish ongoing security maintenance procedures

1. **Open** **Group Policy Editor** and navigate to **Computer Configuration > Administrative Templates > Windows Components > Windows Update**

2. **Double-click** **Configure Automatic Updates**

3. **Select** **Enabled** and choose **Auto download and schedule the install**

4. **Set** installation day to **0 - Every day**

5. **Set** installation time to **03:00** (3:00 AM)

6. **Double-click** **Allow signed updates from an intranet Microsoft update service location**

7. **Configure** update source settings as needed

8. **Enable** **Turn on recommended updates via Automatic Updates**

9. **Apply** settings and run `gpupdate /force`

10. **Verify** automatic update configuration in Windows Update settings

**Challenge Question:**
What Windows feature automatically installs security patches?

**Answer:** Automatic

**Task Summary:**
You configured automatic update policies that ensure systems receive critical security patches without manual intervention. Automated updates are essential for maintaining ongoing protection against newly discovered vulnerabilities and ensuring consistent security across all systems.

## Discussion Questions

**Discussion Questions and Answers**

1. **How does system hardening differ from installing security software, and why are both approaches necessary?**
**Answer:** System hardening involves configuring the operating system and applications to minimize vulnerabilities and reduce attack surface, while security software provides active protection against threats. Hardening addresses inherent system weaknesses through configuration changes, service minimization, and policy enforcement. Security software adds detection and response capabilities. Both approaches are necessary because hardening prevents many attacks from succeeding, while security software provides defense against threats that bypass hardened configurations.

2. **What is the principle of least privilege, and how does it enhance system security?**
**Answer:** The principle of least privilege grants users and processes only the minimum access rights necessary to perform their functions. This approach enhances security by limiting the potential damage from compromised accounts, reducing the attack surface available to malicious actors, and preventing accidental system changes. When accounts are compromised, limited privileges restrict what attackers can access or modify, containing potential security incidents.

3. **Why is service minimization considered a critical component of system hardening?**
**Answer:** Service minimization reduces the attack surface by eliminating unnecessary system components that could be exploited by attackers. Each running service represents a potential entry point for security threats. Disabling unused services reduces memory consumption, improves performance, and eliminates potential vulnerabilities in software that isn't needed. This approach follows the security principle of reducing complexity and minimizing exposure to threats.

4. **How do account lockout policies balance security with usability?**
**Answer:** Account lockout policies prevent brute force attacks by disabling accounts after failed login attempts, but must be configured to avoid impacting legitimate users. The lockout threshold should be high enough to accommodate honest mistakes but low enough to stop automated attacks. Lockout duration should provide security without causing excessive user frustration. Reset timers should allow legitimate users to retry after brief periods while maintaining protection against persistent attacks.

5. **What role does data encryption play in comprehensive system hardening strategies?**
**Answer:** Data encryption protects information confidentiality even when other security controls fail. It ensures that stolen devices, compromised storage, or intercepted communications cannot reveal sensitive information to unauthorized parties. Encryption serves as a final defense layer that maintains data protection regardless of system breaches. Full disk encryption protects against physical theft, while file-level encryption provides granular protection for specific sensitive data.

## Summary

In this CompTIA A+ Lab 10, you gained comprehensive hands-on experience implementing system hardening techniques that create robust security foundations for Windows environments. You learned to configure security policies, manage user permissions, minimize attack surfaces, implement encryption, and establish ongoing maintenance procedures using systematic approaches that balance security with operational requirements.

The practical exercises in this lab addressed multiple layers of system security, from password policies and account management to service configuration and data protection. You practiced implementing defense-in-depth strategies that provide overlapping security controls, ensuring that multiple barriers protect against various threat vectors. These skills are essential for IT professionals who must create and maintain secure computing environments in diverse organizational settings.

Understanding system hardening principles is critical for CompTIA A+ certification and professional IT security roles. The hands-on experience with Group Policy configuration, service management, encryption implementation, and automated update procedures provides immediately applicable knowledge for workplace scenarios. These competencies demonstrate your ability to implement comprehensive security strategies that protect organizational assets while maintaining system functionality and user productivity in professional computing environments.

## References

1. CompTIA. (2024). *CompTIA A+ Certification Exam Objectives (220-1202)*. CompTIA, Inc.

2. National Institute of Standards and Technology. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800-53, Revision 5).

3. Microsoft Corporation. (2024). *Windows Security Baselines*. Microsoft Security Compliance Toolkit Documentation.

4. National Institute of Standards and Technology. (2017). *Guide to General Server Security* (NIST Special Publication 800-123).

5. Meyers, M. (2024). *CompTIA A+ Certification All-in-One Exam Guide, Eleventh Edition* (11th ed.). McGraw-Hill Education.

6. SANS Institute. (2023). *Windows Security and Hardening*. SANS Security Training.

7. Chapple, M., & Seidl, D. (2022). *CompTIA Security+ Study Guide: Exam SY0-601* (8th ed.). Sybex.

8. National Institute of Standards and Technology. (2019). *Cybersecurity Framework Version 1.1*. NIST Framework for Improving Critical Infrastructure Cybersecurity.

9. Ciampa, M. (2023). *CompTIA Security+ Guide to Network Security Fundamentals* (7th ed.). Cengage Learning.

10. Stallings, W., & Brown, L. (2023). *Computer Security: Principles and Practice* (4th ed.). Pearson Education.
