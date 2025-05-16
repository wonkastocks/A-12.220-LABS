# Lab 2: Windows Graphical & Command-Line Interface (CLI)

## Introduction and Objectives

This lab provides hands-on experience with managing a Windows environment through both graphical user interfaces (GUIs) and command-line interfaces (CLI). The exercises cover essential system tools, resource management, configuration settings, and administrative tasks using both interfaces. These tasks directly support the CompTIA A+ 220-1202 objectives, particularly Objective 1.2 (Operating System Configuration), Objective 1.3 (Troubleshooting), Objective 1.4 (System Management), and Objective 4.0 (Command-Line Tools).

**In this lab, you will learn to:**

- Monitor and analyze system performance using Task Manager and Resource Monitor
- Manage system resources and administrative tools with MMC snap-ins
- Gather and interpret system information for troubleshooting
- Optimize disk performance and use built-in maintenance utilities
- Navigate and manage the file system using command-line tools
- Configure and troubleshoot network settings with CLI utilities
- Adjust system configuration and startup options using System Configuration Utility
- Safely edit and back up the Windows Registry
- Apply and manage Group Policy for system-wide settings
- Leverage built-in Windows system tools for effective administration

Proficiency in both GUI and CLI methods is essential for effective Windows system administration. These skills enable efficient system management, issue troubleshooting, performance optimization, and task automation. The ability to work effectively in both interfaces is crucial for IT professionals, as different scenarios may require different approaches. Mastery of these objectives is important for CompTIA A+ certification and professional IT support roles.


## Key Terms Covered in This Lab

| #  | Key Term                         | Description                                                                 |
|----|-----------------------------------|-----------------------------------------------------------------------------|
| 1  | Task Manager                     | Tool for monitoring and managing running processes, performance, and startup programs in Windows. |
| 2  | MMC Snap-in                      | Modular administrative tools added to the Microsoft Management Console for system management. |
| 3  | Resource Monitor                 | Utility for real-time monitoring of CPU, memory, disk, and network usage.   |
| 4  | System Configuration Utility     | Tool (`msconfig`) for managing startup options, services, and boot settings.|
| 5  | Command-Line Interface (CLI)     | Text-based interface for executing commands and managing the system.        |
| 6  | Registry Editor                  | Tool (`regedit`) for viewing and editing the Windows Registry.              |
| 7  | Group Policy                     | Framework for managing and configuring operating system, application, and user settings in a Windows environment. |
| 8  | Disk Cleanup                     | Utility for removing unnecessary files to free up disk space.               |
| 9  | Defragmenter/Optimize Drives     | Tool for optimizing and defragmenting hard drives to improve performance.   |
| 10 | Network Troubleshooting Commands | Commands such as `ipconfig`, `ping`, `netstat`, and `nslookup` for diagnosing network issues. |

## Task List

| Task |
|------|
| Monitor System Performance with Task Manager |
| Manage System Resources with MMC Snap-ins |
| Analyze System Information and Resources |
| Manage and Optimize Disk Performance |
| Navigate and Manage File System via Command Line |
| Configure and Manage Network via Command Line |
| Configure System Settings with System Configuration Utility |
| Manage Windows Registry |
| Configure Group Policy |
| Administer Windows System Tools |

## Tasks to be Covered and Correlated Objectives

| Task | Objective/Domain/Description |
|--------------------------------|------------------------------------------------------------------|
| Monitor System Performance with Task Manager | 1.2 Operating Systems - Given a scenario, use the appropriate Microsoft command-line tool |
| Manage System Resources with MMC Snap-ins | 1.4 Operating Systems - Given a scenario, use Microsoft operating system features and tools |
| Analyze System Information and Resources | 1.2 Operating Systems - Given a scenario, use the appropriate Microsoft command-line tool |
| Manage and Optimize Disk Performance | 4.0 Operational Procedures - Given a scenario, use the appropriate Microsoft operating system tools |
| Navigate and Manage File System via Command Line | 4.0 Operational Procedures - Given a scenario, use the appropriate Microsoft command-line tool |
| Configure and Manage Network via Command Line | 4.0 Operational Procedures - Given a scenario, use the appropriate Microsoft command-line tool |
| Configure System Settings with System Configuration Utility | 1.2 Operating Systems - Given a scenario, use the appropriate Microsoft command-line tool |
| Manage Windows Registry | 1.4 Operating Systems - Given a scenario, use Microsoft operating system features and tools |
| Configure Group Policy | 4.0 Operational Procedures - Given a scenario, use the appropriate Microsoft operating system tools |
| Administer Windows System Tools | 1.4 Operating Systems - Given a scenario, use Microsoft operating system features and tools |

## Key Learning Areas

- **Network Management**: Leveraging CLI tools for network configuration and management
- **System Configuration**: Using the System Configuration Utility and Group Policies to configure system settings and security policies
- **Registry Management**: Navigating and making changes to the Windows Registry for system configuration
- **Windows System Tools**: Familiarizing yourself with various tools and settings that play a key role in system administration

This lab aligns with the CompTIA A+ 220-1202 objectives, primarily focusing on Operating Systems (1.0) and Operational Procedures (4.0). By the end of this lab, you will gain practical experience in managing and troubleshooting a Windows system using both graphical interfaces and command-line commands, skills that are essential for any IT support professional.

The following sections provide detailed procedures for completing each task in the lab environment.

## Task 1: Monitor System Performance with Task Manager

**Objective:** Monitor system performance and resource usage using Windows Task Manager.

### Step-by-Step Instructions

1. Click the Start button to provision the lab.
2. When the lab loads, click the computer image in the right pane to open a VM window.
3. When Windows 11 finishes booting, double click the screen to reveal the login prompt.
4. Click Student in the bottom left corner to select the Student account.
5. Login with the password of Passw0rd.
6. Right-click on the taskbar and select Task Manager.
7. Examine each of the options on the left hand side of Task Manager.
8. Click the Performance option on the left hand side.
9. Start various programs to see the changes in the CPU, Memory and Disk usage.
10. Click the Processes option.
11. Click the Run new task button.
12. In the new window type in notepad and press Enter.
13. Notice that Notepad appears in the process list.
14. Select Notepad and click End task.
15. Next select the Startup apps option on the left hand side.
16. Select Microsoft OneDrive and click the Disable button to keep it from starting when the Student account logs in.
17. Close any open windows in the Windows 11 VM and proceed to the next exercise.


---

**Challenge Question:**

*What section in Task Manager allows you to view real-time CPU, Memory, and Disk usage?*

**Answer:**

*Performance*

**Task 1 Summary:**
In this task, you learned to use Task Manager to monitor system performance and manage running processes. This skill is essential for diagnosing performance issues and ensuring system stability, which is a core responsibility for IT professionals and directly supports CompTIA A+ troubleshooting objectives.

## Task 2: Manage System Resources Using MMC Snap-ins

**Objective:** Configure and utilize Microsoft Management Console (MMC) snap-ins for system administration.

### Step-by-Step Instructions

1. Type mmc in the Search bar and press Enter to open Microsoft Management Console.
2. Click Yes in the UAC window.
3. Click File > Add/Remove Snap-in...
4. Select Event Viewer and click Add >
5. Leave Local computer selected and click OK.
6. Select Disk Management and click Add >
7. Leave This computer selected and click Finish.
8. Select Task Scheduler and click Add >
9. Leave Local computer selected and click OK.
10. Select Device Manager and click Add >
11. Select Performance Monitor and click Add >
12. Click OK.
13. Expand Event Viewer (Local) in the left pane.
14. Explore Windows Logs (Application, Security, System) to view events.
15. Navigate to the System log and look for any Error events.
16. Click on an event to see its details.
17. In the left pane, click on Disk Management.
18. View the list of disks and their partitions. Do not make changes unless specifically instructed.
19. Right-click on a partition to see available options.
20. Press ESC to close the menu.
21. In the left pane, click on Task Scheduler (Local)
22. Explore the Task Scheduler Library
23. Click Create Basic Task... in the right pane to create a new task.
24. In the Name box type: Run Notepad.
25. Click Next.
26. On the Task Trigger page click Next.
27. On the Daily page click Next.
28. On the Action page leave the default action and click Next.
29. On the Start a Program page click the Browse buton.
30. In the Open dialog, in the search bar type note.
31. Select notepad from the list and click Open.
32. Click Next.
33. Click Finish.
34. Expand Task Scheduler (Local) and select Task Scheduler Library.
35. In the center pane scroll down the list until you see Run Notepad.
36. Right click Run Notepad and select Run.
37. Notice that a Notepad window opens.
38. Close Notepad.
39. In the left pane, click on Device Manager.
40. Expand the different device categories (e.g., "Disk drives," "Network adapters").
41. Right-click on a device to view its properties, update drivers, or disable it.
42. In the left pane, expand Performance (Local) .
43. Expand Monitoring Tools.
44. Select Performance Monitor.
45. Click the green "+" button to add counters.
46. Select performance counters (e.g., "CPU Usage," "Memory\Available MBytes") and click Add.
47. Click OK to view the performance graph.
48. Close Microsoft Management Console.
49. Click No to skip saving the layout to a file.
50. Proceed to the next section.


---

**Challenge Question:**

*In Task Scheduler, what is the name of the basic task you created to open Notepad?*

**Answer:**

*Run Notepad*

**Task 2 Summary:**
You practiced using MMC snap-ins to access and manage system resources and administrative tools. Mastering MMC enhances your ability to troubleshoot, configure, and maintain Windows environments efficiently, a key skill for IT support and the CompTIA A+ exam.

## Task 3: Analyzing System Information and Resources

**Objective:** Utilize System Information and Resource Monitor to gather and analyze system details.

### Step-by-Step Instructions

1. Type msinfo32 in the search bar and press Enter.
2. In the left pane, explore the different categories:
3. System Summary: View basic system information (OS version, system manufacturer, processor, memory).
4. Locate the BIOS version and the total physical memory.
5. Components: View information about installed software and drivers.
6. Expand Components. 
7. Select Display.
8. Locate the Adapter Description.
9. Close System Information.
10. Type resmon in the search bar and press Enter.
11. Explore the different sections.
12. CPU: Monitor CPU usage by process, service, and thread.
13. Identify the processes that are consuming the most CPU. 
14. Memory: View memory usage, including physical memory, commit charge, and hard faults.
15. Disk: Monitor disk activity, including read/write speeds and disk queue length.
16. Network: View network activity, including bandwidth usage and network connections.
17. Close Resource Monitor.
18. Proceed to the next section.
---

**Challenge Question:**

*What is the name of the graphics adapter listed in System Information under Components > Display?*

**Answer:**

*VMware SVGA 3D*

**Task 3 Summary:**
In this task, you used System Information and Resource Monitor to gather and analyze system details. These skills are vital for diagnosing hardware and software issues, supporting troubleshooting, and ensuring system reliability as required by IT support roles and CompTIA A+ objectives.

## Task 4: Manage and Optimize Disk Performance

**Objective:** Utilize Windows tools for disk maintenance and performance optimization.

### Step-by-Step Instructions

1. Type dfrgui in the search bar and press Enter.
 Note: On modern systems with SSDs, this tool may be called "Optimize Drives" and perform different functions appropriate to the drive type.
2. Select C:
3. Click Analyze. The tool will analyze the drive for fragmentation.
4. Due to the fact that we are inside a VM. Defragmentation/Optimization will be unnecessary. On actual hardware it helps to periodically run this utility to maintain peak drive performance.
5. Close Optimize Drives.
6. Type cleanmgr in the search bar and press Enter.
7. Disk Cleanup will calculate space that can be freed.
8. In the list of "Files to delete", check the boxes for the types of files you want to delete (e.g., "Temporary Internet Files," "Recycle Bin").
9. Click OK to delete the files.
10. Click Clean up system files.
11. Examine the new options.
12. When you are finished, click Cancel to close Disk Cleanup.
13. Proceed to the next section.

---

**Challenge Question:**

*What is the name of the first category of files in the Files to delete list?*

**Answer:**

*Downloaded Program Files*

**Task 4 Summary:**
You practiced optimizing disk performance and cleaning up unnecessary files using Windows utilities. Maintaining disk health and free space is essential for system performance and longevity, which is a key part of IT maintenance and the A+ certification.

## Task 5: Navigate and Manage File System via Command Line

**Objective:** Demonstrate file system navigation and management using Command Prompt commands.

### Step-by-Step Instructions

1. Type cmd in the search bar.
2. Right-click on Command Prompt in the search results and select Run as administrator.
3. Type in cd \ and press Enter to navigate to the root directory of the C: drive.
4. Type in md test and press Enter to create a new directory.
5. Type in cd test and press Enter to navigate to the test directory.
6. Type in cd .. and press Enter to navigate back one directory. In this case it brings you back to the root directory.
7. Type in dir and press Enter to list the files and subdirectories in the current directory.
8. Type in dir /p and press Enter to list the files and subdirectories in the current directory pausing the output, displaying one screen at a time.
9. Type in dir /w and press Enter to list the files and subdirectories in the current directory in wide format.
10. Type in dir /a and press Enter to list the files and subdirectories in the current directory, displaying all files, including hidden and system files.
11. Type in rd test and press Enter to remove the test directory.
NOTE: This will not work if the directory is not empty. In that case use rd /s <directory name> to remove a directory and its subdirectories and files
12. Type in md test and press Enter.
13. Type in cd test and press Enter to navigate to the test directory.
14. To create a text file type in copy con file1.txt and press Enter.
15. Type in This is a test file.
16. Press Ctrl+z and then press Enter to save the empty text file.
17. To copy the text file type in copy file1.txt file2.txt and press Enter.
18. To move the new file to C:\Users\Student type in move file2.txt c:\Users\Student\file2.txt
19. To delete a file without sending it to the Recycle Bin type in del c:\Users\Student\file2.txt
20. To display the contents of file1.txt type in type file1.txt.
21. To display the contents of the current directory type in dir and press Enter.
22. To list all files with the extension .txt in the current directory type in dir *.txt and press Enter.
NOTE: The "*" character is what is called a wildcard. In this case it allows for any character or characters to appear in the filename before .txt
23. To list all files in the current directory that have a filename starting in file and ending in any one character followed by the extension .txt type in dir file?.txt. This is another example of a wildcard.
24. Type in dir c:\Windows\System32\cmd.exe and press Enter. The path c:\Windows\System32\cmd.exe is what is known as an absolute path. An absolute path specifies the exact location of a file or directory, starting from the root directory.
25. Type in cd .. and press Enter. 
26. Type in dir test\file1.txt and press Enter. The path test\file1.txt is what is known as a relative path. A relative path specifies the location relative to the current directory.
27. Leave the Command Prompt window as is and proceed to the next section.

---

**Challenge Question:**

*What command did you use to move file2.txt to your home directory?*

**Answer:**

*move*

**Task 5 Summary:**
In this task, you navigated and managed the file system using command-line tools. Mastering CLI navigation and file management boosts your efficiency and is fundamental for advanced troubleshooting and automation in IT support.

## Task 6: Configure and Manage Network via Command Line

**Objective:** Demonstrate network configuration and troubleshooting using Command Prompt utilities.

### Step-by-Step Instructions

1. To display basic IP configuration information for all network adapters, type in ipconfig and press Enter.
2. To display detailed IP configuration information, including DNS servers, MAC address, and DHCP status type in ipconfig /all and press Enter.
3. To release the current IP address obtained from a DHCP server type in ipconfig /release and press Enter.
4. To request a new IP address from a DHCP server type in ipconfig /renew and press Enter.
5. To test network connectivity by sending ICMP echo request packets to a destination type in ping 192.168.0.250 and press Enter
6. To display all active connections and listening ports type in netstat -a and press Enter.
7. To show the executable involved in creating each connection or listening port type in netstat -b and press Enter.
8. To display addresses and port numbers in numerical form type in netstat -n and press Enter.
9. To query DNS servers to find the IP address associated with the google.com domain name type in nslookup google.com and press Enter.
10. To create a network share type in net share test=c:\test and press Enter.
11. To map the shared folder to the Z: drive type in net use Z: \\127.0.0.1\test and press Enter.
12. Type in dir z:\ to show the contents of the network drive.
13. To disconnect from drive Z: type in net use Z: /delete and press Enter.
14. To trace the route that packets take to reach google.com, showing each hop along the way type in tracert google.com
15. To show information similar to tracert, but also providing information about packet loss at each hop type in pathping google.com
16. Leave the VM in its current state and proceed to the next section.

---

**Challenge Question:**

*What command did you use to display your current IPv4 address?*

**Answer:**

*ipconfig*

**Task 6 Summary:**
You configured and troubleshooted network settings using command-line utilities. These skills are crucial for diagnosing connectivity issues and ensuring secure, reliable network operations, as required for IT professionals and CompTIA A+.

## Task 7: Configure System Settings with System Configuration Utility

**Objective:** Configure system startup and services using the System Configuration Utility.

### Step-by-Step Instructions

1. Open the System Configuration Utility by typing msconfig in the search bar and pressing Enter
2. In the General tab, select Selective startup and uncheck Load startup items.
3. Go to the Boot tab and note the current timeout value. Change it to 10 seconds.
4. In the Services tab, uncheck both instances of Microsoft Edge Update Service.
5. In the Startup tab, click Open Task Manager and click OneDrive, then click the Disable button.
6. Close Task Manager.
7. Click Apply and OK. If prompted, restart your computer.
8. When the VM finishes restarting, log back into the Student account with the password of Passw0rd.

---

**Challenge Question:**

*In the System Configuration Utility, which tab allows you to disable non-essential startup items?*

**Answer:**

*General*

**Task 7 Summary:**
You learned to adjust system startup, services, and configuration using the System Configuration Utility. This enables you to optimize boot times and troubleshoot startup issues, supporting system reliability and aligning with A+ objectives.

## Task 8: Manage Windows Registry

### Step-by-Step Instructions

1. Open Registry Editor by typing regedit in the search bar and pressing Enter. Approve the UAC prompt.
2. Export the Desktop key from HKEY_CURRENT_USER\Control Panel\Desktop (right-click > Export). Save the file as DesktopBackup.reg.
3. Open File Explorer by clicking the icon on the taskbar.
4. Click Documents in the left pane.
5. Right click the exported .reg file and select Edit in Notepad and make a note of the first line (should be Windows Registry Editor Version 5.00).
6. Close Notepad.
7. Import the backup file by double-clicking it and confirming the prompts.
8. Create a new string value under HKEY_CURRENT_USER\Control Panel\Desktop called TestValue and set its data to CascadeLab.
9. Delete the TestValue entry after taking your screenshot.
10. Close the Registry Editor.
11. Leave the VM in its current condition and proceed to the next section.


---

**Challenge Question:**

*In Registry Editor, which key did you export to create a backup named DesktopBackup.reg?*

**Answer:**

*Desktop*

**Task 8 Summary:**
In this task, you navigated, modified, and backed up the Windows Registry. Understanding the registry is essential for advanced troubleshooting and configuration but requires caution due to its impact on system stability, as emphasized in A+ certification.

## Task 9: Configure Group Policy

**Objective:** Configure system and user settings using the Group Policy Editor.

**Procedure:**

1. **Group Policy Editor Initialization:**
   - Press `Win + R`, type `gpedit.msc`, and press Enter
   - Click "Yes" when prompted by User Account Control (UAC)
   - Wait for the Group Policy Editor interface to load completely

2. **Group Policy Structure:**
   - In the left pane, locate these main branches:
     - **Computer Configuration:** Policies that apply to all users on this computer
     - **User Configuration:** Policies that apply to the current user account
   - Expand each branch to view its three main folders:
     - Software Settings
     - Windows Settings
     - Administrative Templates

3. **Policy Application Methods:**
   - **Automatic Updates:**
     - Occurs every 90-120 minutes by default
     - Background processing applies new policies automatically
   - **Manual Updates:**
     - For application-specific policies: Restart the affected application
     - For user-specific policies: Sign out and back in, or use `gpupdate /target:user`
     - For computer policies: Restart the computer or use `gpupdate /target:computer`
     - System restart (for computer policies)
     - `gpupdate /force` command (immediate update)

4. **Policy Processing:**
   - Understand that policies are applied in this order:
     1. Local Group Policy
     2. Site-level Group Policy (if applicable)
     3. Domain-level Group Policy (if applicable)
     4. Organizational Unit (OU) Group Policy (if applicable)
   - Note that later policies override earlier ones by default
   - To view effective settings, open Command Prompt and type `rsop.msc` to see the Resultant Set of Policy

5. **Common Configuration Areas:**
   - **Account Policies**: Configure password requirements and account lockout settings
   - **Local Policies**: Set audit policies and user rights assignments
   - **Windows Settings**: Manage startup/shutdown scripts and security settings
   - **Administrative Templates**: Control system and application settings through policy

6. **Apply and Test Policy:**
   - After making changes, run `gpupdate /force` in Command Prompt to apply policies immediately.
   - Log off and log back in (or restart the computer) to verify that the policy changes are in effect.
   - Test the specific setting you configured (e.g., password complexity, desktop restrictions) to confirm the policy works as intended.

**Outcome:**
You have successfully modified and tested Group Policy settings. You should now be able to enforce security and operational standards, verify their effect, and troubleshoot policy-related issues—an essential skill for IT support roles and the CompTIA A+ exam.

**Challenge Question:**

*Which tool do you use to edit local Group Policy settings in Windows?*

**Task 9 Summary:**
You learned to configure system and user settings using the Group Policy Editor. Mastering Group Policy allows you to enforce security, compliance, and operational standards across multiple computers, a critical skill for IT administrators and required by CompTIA A+.

---

## Task 10: Administer Windows System Tools

**Objective:** Utilize built-in Windows tools for system administration and troubleshooting.

**Procedure:**

1. **Accessing Administrative Tools:**
   - Press `Win + X` and select "Windows PowerShell (Admin)" or "Command Prompt (Admin)"
   - Alternatively, press `Win + R`, type `control admintools`, and press Enter
   - For specific tools, use these Run commands:
     - `services.msc` for Services
     - `compmgmt.msc` for Computer Management
     - `eventvwr.msc` for Event Viewer
     - `taskschd.msc` for Task Scheduler

2. **Core System Utilities:**
   - **Computer Management (`compmgmt.msc`):**
     1. Open Run dialog (`Win + R`), type `compmgmt.msc`, and press Enter
     2. Explore these key sections:
        - **Event Viewer**: Review system and application logs for troubleshooting
        - **Task Scheduler**: Create and manage automated tasks
        - **Shared Folders**: Monitor and manage network shares
        - **Local Users and Groups**: Manage user accounts and groups
        - **Performance Monitor**: Track system performance metrics
        - **Device Manager**: Configure and troubleshoot hardware devices
        - **Disk Management**: Manage disk partitions and volumes
        - **Services**: Configure and control system services

   - **System Maintenance Tools:**
     - **Disk Defragmenter**: Type `dfrgui` in the Run dialog
     - **Disk Cleanup**: Type `cleanmgr` in the Run dialog
     - **System Configuration**: Type `msconfig` in the Run dialog
     - **System Information**: Type `msinfo32` in the Run dialog
     - **Resource Monitor**: Type `resmon` in the Run dialog
     - **Windows Firewall**: Type `firewall.cpl` in the Run dialog

3. **Service Management Example:**
   1. Open Services by pressing `Win + R`, typing `services.msc`, and pressing Enter
   2. Right-click any service to:
      - **Start/Stop**: Control the service's current state
      - **Restart**: Stop and then start the service
      - **Properties**: Configure service settings
   3. In the Properties window, configure:
      - **General Tab**: Set display name, description, and startup type
      - **Log On Tab**: Configure service account and desktop interaction
      - **Recovery Tab**: Set actions for service failure
      - **Dependencies Tab**: View service dependencies

4. **Validate and Practice:**
   - Open several of the listed tools (Services, Event Viewer, Task Scheduler, etc.) and explore their interfaces.
   - Practice starting/stopping a service, viewing an event log, and creating a basic scheduled task.
   - Use Disk Cleanup and Disk Defragmenter to maintain system health.
   - Document what you changed or explored for lab completion.

Task 10 Summary:
You learned to utilize built-in Windows tools for system administration and troubleshooting. Mastering these tools enables you to manage, maintain, and secure Windows environments effectively—an essential competency for IT professionals and a key focus of CompTIA A+.

---

## Discussion Questions

**Question 1:**

What are the advantages of using Task Manager and Resource Monitor for troubleshooting system performance issues in Windows?

**Answer:**

Task Manager provides a quick overview of running processes, CPU, memory, disk, and network usage, helping identify resource hogs and unresponsive applications. Resource Monitor offers deeper real-time analysis of system resources, allowing you to pinpoint which processes are using specific files, network ports, or causing disk bottlenecks. Together, they enable effective diagnosis and resolution of performance problems. (Objective 1.2)

**Question 2:**

How can command-line tools like ipconfig, netstat, and nslookup assist in network troubleshooting?

**Answer:**

`ipconfig` displays IP configuration and can release/renew DHCP leases. `netstat` shows active connections and listening ports, helping identify open or suspicious network activity. `nslookup` tests DNS resolution. These tools help diagnose connectivity issues, identify misconfigurations, and verify network status from the command line. (Objective 4.0)

**Question 3:**

What precautions should you take before editing the Windows Registry, and why is documentation important?

**Answer:**

Always back up the registry or create a system restore point before making changes, as incorrect edits can destabilize or disable Windows. Documenting changes allows for easier troubleshooting and recovery if issues arise, and ensures repeatability for future configurations. (Objective 1.4)

**Question 4:**

Describe how Group Policy can be used to enforce security and configuration settings across multiple computers in a Windows environment.

**Answer:**

Group Policy allows administrators to centrally manage settings such as password policies, software restrictions, and user permissions. Policies can be applied at the local, site, domain, or organizational unit (OU) level, ensuring consistent security and operational standards across all managed systems. (Objective 4.0)

**Question 5:**

Why is it important to use built-in Windows system tools like Disk Cleanup, Defragmenter, and System Configuration, and what risks are associated with improper use?

**Answer:**

These tools help maintain system health by freeing up disk space, optimizing performance, and managing startup processes. However, improper use—such as deleting critical files or disabling essential services—can lead to data loss or system instability. Always review actions and understand tool functions before applying changes. (Objective 1.2, 1.4)

---

## Summary

In this lab, you learned to:

- Monitor and analyze system performance using Task Manager and Resource Monitor
- Manage system resources and administrative tools with MMC snap-ins
- Gather and interpret system information for troubleshooting
- Optimize disk performance and use built-in maintenance utilities
- Navigate and manage the file system using command-line tools
- Configure and troubleshoot network settings with CLI utilities
- Adjust system configuration and startup options using System Configuration Utility
- Safely edit and back up the Windows Registry
- Apply and manage Group Policy for system-wide settings
- Leverage built-in Windows system tools for effective administration

These activities directly support the CompTIA A+ 220-1202 objectives, especially those related to system configuration, resource management, security, and operational procedures. Mastering these skills ensures you are prepared to efficiently support, secure, and optimize Windows environments in real-world IT roles.

---

## References

National Institute of Standards and Technology. (2011). *Guide to General Server Security (SP 800-123)*. https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-123.pdf

National Institute of Standards and Technology. (2020). *Security and Privacy Controls for Information Systems and Organizations (SP 800-53 Rev. 5)*. https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final

National Institute of Standards and Technology. (2016). *Data Integrity: Detecting and Responding to Ransomware and Other Destructive Events (SP 1800-11)*. https://www.nist.gov/publications/data-integrity-detecting-and-responding-ransomware-and-other-destructive-events

Microsoft. (2023). *Windows 11 System Requirements*. https://www.microsoft.com/en-us/windows/windows-11-specifications

Microsoft. (2023). *Windows 11 Documentation*. https://learn.microsoft.com/en-us/windows/

Microsoft. (2023). *Command-line reference A-Z*. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/windows-commands

CompTIA. (2022). *CompTIA A+ Certification Exam Objectives (220-1202)*. https://www.comptia.org/certifications/a

Microsoft. (2023). *Group Policy Overview*. https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/group-policy-overview

Microsoft. (2023). *Registry Editor Guidance*. https://learn.microsoft.com/en-us/windows/win32/sysinfo/registry

U.S. Department of Homeland Security. (2019). *Cybersecurity Workforce Training Guide*. https://www.cisa.gov/sites/default/files/publications/cybersecurity-workforce-training-guide.pdf

---


