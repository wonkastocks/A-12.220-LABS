

## Task List


| Task                           |
|--------------------------------|
| Troubleshoot Inability to Access Network |
| Investigate Desktop Alerts     |
| Analyze False Antivirus Alerts |
| Identify Altered System Files  |
| Recover Missing or Renamed Files |
| Troubleshoot Unwanted Notifications |
| Diagnose OS Update Failures    |
| Resolve Browser Redirection Issues |
| Diagnose Degraded Browser Performance |
| Remove Random/Frequent Pop-ups |






## Task/Objective


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Troubleshoot Inability to Access Network | 3.0 Software Troubleshooting                            |
| Investigate Desktop Alerts     | 4.0 Operational Procedures                                        |
| Analyze False Antivirus Alerts | 4.0 Operational Procedures                                        |
| Identify Altered System Files  | 1.0 Operating Systems                                             |
| Recover Missing or Renamed Files | 4.0 Operational Procedures                                      |
| Troubleshoot Unwanted Notifications | 3.0 Software Troubleshooting                                 |
| Diagnose OS Update Failures    | 4.0 Operational Procedures                                        |
| Resolve Browser Redirection Issues | 1.101.0   Operating Systems |
| Diagnose Degraded Browser Performance | 4.0 Operational Procedures                                 |
| Remove Random/Frequent Pop-ups | 4.0 Operational Procedures                                        |

---


# Lab 16: PC Security Troubleshooting

## Introduction

This hands-on lab provides comprehensive practice in diagnosing and resolving PC security issues—critical skills for IT professionals and CompTIA A+ certification candidates. Covering objectives from the 220-1202 exam, you'll develop proficiency in identifying security threats, analyzing suspicious system behavior, and implementing effective remediation strategies that restore system security and functionality.

Through guided exercises, you'll master essential security troubleshooting practices including network connectivity analysis, desktop alert investigation, antivirus validation, system file integrity checking, data recovery procedures, notification management, update failure resolution, browser security repair, performance optimization, and malicious pop-up removal. These skills are fundamental for maintaining secure computing environments and responding effectively to security incidents in professional settings.

## Learning Objectives

By completing this lab, you will be able to:

### Security Incident Investigation
• Troubleshoot network connectivity issues potentially caused by malware
• Investigate suspicious desktop alerts and security warnings
• Analyze false antivirus alerts and social engineering attempts
• Identify and assess altered or corrupted system files

### System Recovery and Remediation
• Recover missing or renamed files from security incidents
• Resolve unwanted notifications and system alerts
• Diagnose and fix operating system update failures
• Restore browser functionality after security compromises

### Performance and Stability Restoration
• Resolve browser redirection and hijacking issues
• Diagnose and improve degraded browser performance
• Remove random and frequent pop-up advertisements
• Restore normal system operation after malware removal

### Key Terms Covered in This Lab

| # | Key Term | Description |
|---|----------|-------------|
| 1 | Malware Infection | System compromise by malicious software affecting normal operation |
| 2 | Browser Hijacking | Unauthorized modification of browser settings and behavior |
| 3 | False Positive | Legitimate software incorrectly identified as malicious |
| 4 | System File Corruption | Damage to critical operating system files affecting functionality |
| 5 | Adware | Software that displays unwanted advertisements and pop-ups |
| 6 | Browser Redirection | Automatic forwarding to unintended websites |
| 7 | Rogue Antivirus | Fake security software designed to deceive users |
| 8 | Network Isolation | Disconnection from network resources due to security issues |
| 9 | Registry Corruption | Damage to Windows registry database affecting system behavior |
| 10 | Performance Degradation | Reduced system speed and responsiveness due to security issues |
| 11 | Pop-up Blocker | Browser feature preventing unwanted advertising windows |
| 12 | Security Alert Fatigue | User desensitization to legitimate security warnings |

### Lab Task Overview

| Task | Description |
|------|-------------|
| Troubleshoot Inability to Access Network | Diagnose network connectivity issues caused by security problems |
| Investigate Desktop Alerts | Analyze suspicious system alerts and security warnings |
| Analyze False Antivirus Alerts | Identify and respond to fake security software warnings |
| Identify Altered System Files | Detect and assess system file corruption or modification |
| Recover Missing or Renamed Files | Restore files affected by malware or security incidents |
| Troubleshoot Unwanted Notifications | Remove persistent and malicious system notifications |
| Diagnose OS Update Failures | Resolve Windows update problems and security patch issues |
| Resolve Browser Redirection Issues | Fix unauthorized browser behavior and hijacking |
| Diagnose Degraded Browser Performance | Improve browser speed and responsiveness after compromise |
| Remove Random/Frequent Pop-ups | Eliminate unwanted advertising and malicious pop-ups |

### CompTIA A+ Objective Mapping

| Task Area | Exam Objective Reference |
|-----------|-------------------------|
| Network Connectivity | 3.0 Software Troubleshooting |
| Desktop Alerts | 4.0 Operational Procedures |
| False Antivirus | 4.0 Operational Procedures |
| System Files | 1.0 Operating Systems |
| File Recovery | 4.0 Operational Procedures |
| Unwanted Notifications | 3.0 Software Troubleshooting |
| Update Failures | 4.0 Operational Procedures |
| Browser Redirection | 1.101.0 Operating Systems |
| Browser Performance | 4.0 Operational Procedures |
| Pop-up Removal | 4.0 Operational Procedures |

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

Before you begin the hands-on tasks in this lab, you will gain practical experience troubleshooting PC security issues that are critical for maintaining system security and user productivity in professional environments. You will learn to systematically diagnose security problems, identify root causes, and implement effective remediation strategies using real-world troubleshooting tools and methodologies. These skills are essential for responding to security incidents, restoring system functionality, and preventing future security compromises. Mastery of these tasks directly aligns with CompTIA A+ exam objectives and prepares you for professional security incident response responsibilities.

## Task 1: Troubleshoot Inability to Access Network

### Objective: Diagnose network connectivity issues caused by security problems

1. **Test** network connectivity by opening **Command Prompt**

2. **Run** `ping 8.8.8.8` to test internet connectivity

3. **Run** `ipconfig /all` to check network configuration

4. **Check** **Network and Sharing Center** for connection status

5. **Open** **Windows Security** and check firewall settings

6. **Review** **Firewall & network protection** for blocked applications

7. **Check** **Event Viewer** > **Windows Logs** > **System** for network errors

8. **Run** `netsh winsock reset` to reset network stack

9. **Run** `netsh int ip reset` to reset TCP/IP configuration

10. **Restart** the computer and test network connectivity

**Challenge Question:**
What command resets the Windows network socket configuration?

**Answer:** netsh

**Task Summary:**
You diagnosed network connectivity issues that may result from malware interference with network settings or firewall configurations. Network troubleshooting in security contexts requires checking for malicious modifications to network configurations and security software blocking legitimate connections.

## Task 2: Investigate Desktop Alerts

### Objective: Analyze suspicious system alerts and security warnings

1. **Take** screenshots of any suspicious desktop alerts or pop-ups

2. **Document** the exact text and appearance of security warnings

3. **Check** **Action Center** for legitimate system notifications

4. **Open** **Event Viewer** to correlate alerts with system events

5. **Review** **Windows Logs** > **Application** for alert sources

6. **Check** **Task Manager** > **Startup** for suspicious programs

7. **Examine** running processes for unknown or suspicious applications

8. **Verify** alerts against known legitimate Windows notifications

9. **Research** alert messages using Microsoft documentation

10. **Document** findings and determine alert legitimacy

**Challenge Question:**
What Windows feature provides legitimate system notifications and alerts?

**Answer:** Action

**Task Summary:**
You investigated desktop alerts to distinguish between legitimate system warnings and potential security threats. Alert analysis helps identify social engineering attempts, rogue software, and system issues that require immediate attention or remediation.

## Task 3: Analyze False Antivirus Alerts

### Objective: Identify and respond to fake security software warnings

1. **Document** any antivirus alerts with screenshots and details

2. **Verify** alerts are from legitimate Windows Security or installed antivirus

3. **Check** **Programs and Features** for unknown security software

4. **Look** for recently installed programs with security-related names

5. **Run** **Windows Security** full scan to verify system status

6. **Check** **Protection history** for legitimate threat detections

7. **Research** alert messages on antivirus vendor websites

8. **Uninstall** any suspicious or unknown security software

9. **Run** **Malware removal tools** like Windows Defender Offline

10. **Verify** system is clean and alerts are from legitimate sources

**Challenge Question:**
What type of malicious software mimics legitimate antivirus programs?

**Answer:** Rogue

**Task Summary:**
You analyzed antivirus alerts to identify potential rogue security software and false positive warnings. Distinguishing between legitimate security alerts and fake warnings is crucial for preventing social engineering attacks and maintaining effective security protection.

## Task 4: Identify Altered System Files

### Objective: Detect and assess system file corruption or modification

1. **Open** **Command Prompt** as Administrator

2. **Run** `sfc /scannow` to scan for corrupted system files

3. **Review** scan results for file integrity violations

4. **Check** `%WINDIR%\Logs\CBS\CBS.log` for detailed scan results

5. **Run** `DISM /Online /Cleanup-Image /ScanHealth` to check system image

6. **If** corruption found, run `DISM /Online /Cleanup-Image /RestoreHealth`

7. **Check** **Event Viewer** > **System** for file system errors

8. **Verify** critical system files using `dir` commands

9. **Compare** file dates and sizes with known good systems

10. **Document** any alterations or corruption found

**Challenge Question:**
What Windows command scans and repairs corrupted system files?

**Answer:** sfc

**Task Summary:**
You identified altered or corrupted system files that may indicate malware activity or system compromise. System file integrity checking helps detect unauthorized modifications and enables restoration of critical operating system components.

## Task 5: Recover Missing or Renamed Files

### Objective: Restore files affected by malware or security incidents

1. **Check** **Recycle Bin** for recently deleted files

2. **Use** **File Explorer** search to locate renamed files

3. **Search** for files with unusual extensions or names

4. **Check** **File History** for available backup versions

5. **Right-click** folders and select **Restore previous versions**

6. **Use** **System Restore** to revert to pre-incident state

7. **Run** file recovery software like **Windows File Recovery**

8. **Check** **OneDrive** or cloud storage for synchronized versions

9. **Examine** **Event Viewer** for file deletion or modification events

10. **Document** recovered files and implement preventive measures

**Challenge Question:**
What Windows feature can restore previous versions of files and folders?

**Answer:** History

**Task Summary:**
You recovered files that were missing or renamed due to malware activity or security incidents. File recovery procedures help restore important data and maintain business continuity after security compromises that affect user files and documents.

## Task 6: Troubleshoot Unwanted Notifications

### Objective: Remove persistent and malicious system notifications

1. **Open** **Settings** > **System** > **Notifications & actions**

2. **Review** notification senders and disable suspicious sources

3. **Turn off** notifications from unknown or unwanted applications

4. **Check** **Focus assist** settings for notification control

5. **Open** **Task Scheduler** to look for notification-related tasks

6. **Review** scheduled tasks for suspicious or unknown entries

7. **Disable** or delete tasks that generate unwanted notifications

8. **Check** browser notification settings and permissions

9. **Block** notifications from suspicious websites

10. **Test** notification settings and verify unwanted alerts stop

**Challenge Question:**
What Windows setting controls system notifications and alerts?

**Answer:** Notifications

**Task Summary:**
You troubleshot unwanted notifications that may originate from malware, adware, or compromised applications. Notification management helps eliminate distractions and potential security threats while maintaining legitimate system alerts and communications.

## Task 7: Diagnose OS Update Failures

### Objective: Resolve Windows update problems and security patch issues

1. **Open** **Settings** > **Update & Security** > **Windows Update**

2. **Check** update history for failed or problematic updates

3. **Run** **Windows Update Troubleshooter** from Settings

4. **Clear** Windows Update cache by stopping services

5. **Stop** Windows Update service: `net stop wuauserv`

6. **Delete** contents of `C:\Windows\SoftwareDistribution` folder

7. **Start** Windows Update service: `net start wuauserv`

8. **Run** `sfc /scannow` to check for system file corruption

9. **Check** **Event Viewer** for Windows Update error codes

10. **Attempt** manual update installation and monitor for success

**Challenge Question:**
What Windows feature automatically downloads and installs security patches?

**Answer:** Update

**Task Summary:**
You diagnosed and resolved Windows update failures that can leave systems vulnerable to security threats. Update troubleshooting ensures systems receive critical security patches and maintain protection against newly discovered vulnerabilities.

## Task 8: Resolve Browser Redirection Issues

### Objective: Fix unauthorized browser behavior and hijacking

1. **Open** affected browser and check homepage settings

2. **Reset** homepage to desired location in browser settings

3. **Check** default search engine and reset if changed

4. **Review** browser extensions for suspicious or unknown add-ons

5. **Disable** or remove malicious browser extensions

6. **Clear** browsing data including cookies and cached files

7. **Check** **Programs and Features** for suspicious browser add-ons

8. **Scan** system with **Windows Defender** or antimalware tool

9. **Check** **DNS** settings for unauthorized modifications

10. **Test** browser behavior and verify redirection issues resolved

**Challenge Question:**
What browser component can cause unwanted redirections when compromised?

**Answer:** Extensions

**Task Summary:**
You resolved browser redirection issues caused by malware, browser hijackers, or malicious extensions. Browser security restoration ensures users can safely browse the internet without being redirected to malicious or unwanted websites.

## Task 9: Diagnose Degraded Browser Performance

### Objective: Improve browser speed and responsiveness after compromise

1. **Open** **Task Manager** and check browser memory usage

2. **Close** unnecessary browser tabs and processes

3. **Clear** browser cache, cookies, and temporary files

4. **Disable** resource-intensive browser extensions temporarily

5. **Check** for multiple browser processes consuming resources

6. **Reset** browser to default settings if performance issues persist

7. **Update** browser to latest version for security and performance

8. **Run** **Disk Cleanup** to free up system storage space

9. **Check** for malware that may be affecting browser performance

10. **Test** browser performance and monitor resource usage

**Challenge Question:**
What browser storage can be cleared to improve performance?

**Answer:** Cache

**Task Summary:**
You diagnosed and improved degraded browser performance that often results from malware infections, excessive extensions, or system compromise. Browser performance optimization ensures efficient web browsing and reduces security risks associated with slow or unresponsive browsers.

## Task 10: Remove Random/Frequent Pop-ups

### Objective: Eliminate unwanted advertising and malicious pop-ups

1. **Document** pop-up sources, timing, and content with screenshots

2. **Check** browser pop-up blocker settings and enable if disabled

3. **Review** installed browser extensions for ad-blocking capabilities

4. **Install** reputable ad-blocker like **uBlock Origin** if needed

5. **Check** **Programs and Features** for suspicious adware programs

6. **Uninstall** any unknown or recently installed suspicious software

7. **Run** **Windows Defender** full system scan for adware detection

8. **Use** **Malwarebytes** or similar anti-malware tool for additional scanning

9. **Check** **Task Scheduler** for tasks that might generate pop-ups

10. **Reset** browser settings to default if pop-ups persist

**Challenge Question:**
What browser feature prevents unwanted advertising windows?

**Answer:** Blocker

**Task Summary:**
You removed random and frequent pop-ups caused by adware, malware, or browser compromises. Pop-up elimination improves user experience and system security by preventing exposure to malicious advertising and potential social engineering attempts.

## Discussion Questions

**Discussion Questions and Answers**

1. **How do security-related network connectivity issues differ from standard network problems, and what additional troubleshooting steps are required?**
**Answer:** Security-related network issues often involve malware modifying network settings, firewalls blocking legitimate traffic, or DNS hijacking redirecting connections. Additional troubleshooting includes checking for malicious processes, scanning for malware, verifying DNS settings, examining firewall rules for unauthorized changes, and resetting network configurations that may have been compromised. These issues require both technical network troubleshooting and security analysis to identify root causes.

2. **What strategies should IT professionals use to distinguish between legitimate security alerts and social engineering attempts?**
**Answer:** Legitimate alerts come from known, installed security software and provide specific, actionable information without urgent language or immediate payment demands. Social engineering alerts often use fear tactics, claim immediate threats, request personal information, or direct users to suspicious websites. Verification strategies include checking alert sources, cross-referencing with official vendor communications, avoiding clicking suspicious links, and consulting security team or documentation before taking action.

3. **Why is systematic documentation important when investigating security incidents, and what information should be recorded?**
**Answer:** Documentation provides evidence for incident analysis, supports legal requirements, enables pattern recognition, and facilitates knowledge sharing for future incidents. Key information includes timestamps, screenshots, affected systems, user actions, error messages, remediation steps taken, and outcomes. This documentation helps identify attack vectors, assess damage scope, improve response procedures, and support compliance requirements or forensic investigations.

4. **How do browser security issues impact overall system security, and what comprehensive remediation approaches should be used?**
**Answer:** Browser compromises can lead to system-wide infections through drive-by downloads, credential theft, and malware installation. Comprehensive remediation includes resetting browser settings, removing malicious extensions, clearing stored data, scanning for system-level infections, updating security software, and implementing protective measures like ad blockers and secure DNS. Browser security affects data protection, privacy, and serves as a gateway for broader system compromises.

5. **What preventive measures can organizations implement to reduce the frequency and impact of PC security incidents?**
**Answer:** Preventive measures include regular security training, automated patch management, endpoint protection software, web filtering, email security, backup systems, and incident response procedures. User education about social engineering, phishing, and safe browsing practices significantly reduces security incidents. Technical controls like application whitelisting, network segmentation, and monitoring systems provide additional protection layers and early detection capabilities.

## Summary

In this CompTIA A+ Lab 16, you gained comprehensive hands-on experience troubleshooting PC security issues that commonly affect business computing environments. You learned to systematically diagnose security problems, identify root causes of system compromise, and implement effective remediation strategies that restore security and functionality while preventing future incidents.

The practical exercises in this lab covered the complete security troubleshooting spectrum, from network connectivity issues and system alerts through browser security problems and malware removal. You practiced using diagnostic tools, analyzing system behavior, and implementing targeted solutions that address both immediate symptoms and underlying security vulnerabilities. These skills are essential for IT professionals who must respond quickly to security incidents while maintaining system reliability and user productivity.

Understanding PC security troubleshooting is critical for CompTIA A+ certification and professional IT support roles. The hands-on experience with incident investigation, threat analysis, and system remediation provides immediately applicable knowledge for workplace scenarios where security breaches can have significant business impact. These competencies demonstrate your ability to maintain secure computing environments, respond effectively to security incidents, and implement comprehensive solutions that protect organizational assets while ensuring operational continuity.

## References

1. CompTIA. (2024). *CompTIA A+ Certification Exam Objectives (220-1202)*. CompTIA, Inc.

2. National Institute of Standards and Technology. (2018). *Computer Security Incident Handling Guide* (NIST Special Publication 800-61, Revision 2).

3. Microsoft Corporation. (2024). *Windows Security Troubleshooting Guide*. Microsoft Security Documentation.

4. Meyers, M. (2024). *CompTIA A+ Certification All-in-One Exam Guide, Eleventh Edition* (11th ed.). McGraw-Hill Education.

5. SANS Institute. (2023). *Incident Response and Digital Forensics*. SANS Security Training.

6. Malwarebytes Corporation. (2024). *Malware Removal and System Recovery Guide*. Malwarebytes Technical Documentation.

7. National Institute of Standards and Technology. (2020). *Guide to Malware Incident Prevention and Handling* (NIST Special Publication 800-83, Revision 1).

8. Chapple, M., & Seidl, D. (2022). *CompTIA Security+ Study Guide: Exam SY0-601* (8th ed.). Sybex.

9. Casey, E., & Rose, C. (2018). *Handbook of Digital Forensics and Investigation*. Academic Press.

10. Ciampa, M. (2023). *CompTIA Security+ Guide to Network Security Fundamentals* (7th ed.). Cengage Learning.
