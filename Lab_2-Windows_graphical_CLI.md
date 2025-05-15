# 2-Windows graphical, CLI

## Task List


| Task                                         |
|-----------------------------------------------|
| Using Task Manager for System Monitoring      |
| Managing System Resources with MMC Snap-ins   |
| Analyzing System Information and Resources    |
| Managing and Optimizing Disk Performance      |
| Using Command-Line for File and Folder Navigation |
| Using Command-Line for Network Management     |
| Configuring System Settings with System Configuration Utility |
| Managing the Windows Registry                 |
| Configuring Group Policies                    |
| Managing Windows System Tools                 |






## Tasks to be Covered and Correlated Objectives


| Task                                         | Objective/Domain/Description        |
|-----------------------------------------------|-------------------------------------|
| Using Task Manager for System Monitoring      | 1.0 Operating Systems               |
| Managing System Resources with MMC Snap-ins   | 1.0 Operating Systems               |
| Analyzing System Information and Resources    | 1.0 Operating Systems               |
| Managing and Optimizing Disk Performance      | 4.0 Operational Procedures          |
| Using Command-Line for File and Folder Navigation | 4.0 Operational Procedures     |
| Using Command-Line for Network Management     | 4.0 Operational Procedures          |
| Configuring System Settings with System Configuration Utility | 1.0 Operating Systems |
| Managing the Windows Registry                 | 4.0 Operational Procedures          |
| Configuring Group Policies                    | 4.0 Operational Procedures          |
| Managing Windows System Tools                 | 1.0 Operating Systems               |

---


Here are detailed, step-by-step instructions for each of the tasks you listed, formatted for your A+ exam lab. These instructions are designed to be clear, concise, and easy for students to follow.

**Task 1: Using Task Manager for System Monitoring (Objective 1.0)**

**Objective:** Monitor system performance and resource usage.

**Steps:**

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



**Task 2: Managing System Resources with MMC Snap-ins (Objective 1.0)**

**Objective:** Use Microsoft Management Console (MMC) to manage system resources.

**Steps:**

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
 
**Task 3: Analyzing System Information and Resources (Objective 1.0)**

**Objective:** Use System Information and Resource Monitor to analyze system details.

**Steps:**

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


**Task 4: Managing and Optimizing Disk Performance (Objective 4.0)**

**Objective:** Use tools to manage and optimize disk performance.

**Steps:**

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

**Task 5: Using Command-Line for File and Folder Navigation (Objective 4.0)**

**Objective:** Use Command Prompt to navigate the file system.

**Steps:**

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

**Task 6: Using Command-Line for Network Management (Objective 4.0)**

**Objective:** Use Command Prompt to manage network settings and troubleshoot network issues.

**Steps:**

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


**Task 7: Configuring System Settings with System Configuration Utility (Objective 1.0)**

**Objective:** Use System Configuration Utility (msconfig) to configure system startup and services.

**Steps:**

1.  **Open System Configuration:**

    * Type "msconfig" in the search bar and press Enter.

2.  **Explore the Tabs:**

    * **General:**
        * **Normal startup:** Load all device drivers and services.
        * **Diagnostic startup:** Load only basic devices and services (used for troubleshooting).
        * **Selective startup:** Choose which services and startup items to load.
            * **Adjustment**: Have the student switch between "Normal startup" and "Diagnostic startup" and observe the differences in the startup process. (This may require restarting the computer.)
            * **Observation**: Discuss the purpose of each startup mode and when it might be used.
    * **Boot:** Configure operating system boot options.
        * You can set the default OS if you have multiple installed, enable Safe Boot, and set other advanced options. \*Note: Be cautious when changing boot options.\*
            * **Adjustment**: Have the student enable "Safe Boot" with the "Minimal" option and restart the computer. Then, have them disable Safe Boot and restart again.
            * **Observation**: Discuss what Safe Boot is and how it can be used to troubleshoot system problems. **Important**: Emphasize the need to be cautious when changing boot options.
    * **Services:**
        * View and manage system services.
        * Check "Hide all Microsoft services" to avoid accidentally disabling critical system services.
        * You can enable or disable services. \*Note: Disabling the wrong services can cause system instability.\*
            * **Adjustment**: Have the student identify a non-Microsoft service that is not essential and disable it. Then, have them restart the computer and observe any changes in system behavior. (Choose a non-critical service, and make sure the student knows how to re-enable it if necessary.)
            * **Observation**: Discuss the importance of services in the Windows operating system. Explain the potential consequences of disabling essential services. Stress the importance of only disabling services when you are sure they are not needed.
    * **Startup:**
        * Manage startup items (applications that run when Windows starts).
        * Click "Open Task Manager" to manage startup apps in Windows 10 and later.
            * **Adjustment**: Have the student disable a non-essential startup item in Task Manager (as opened from msconfig), restart, and observe the change in startup.
            * **Observation**: Reinforce how startup items affect boot time and system performance.
    * **Tools:**
        * Provides shortcuts to various administrative tools (e.g., Device Manager, Event Viewer).
            * **Adjustment**: Have the student use the "Tools" tab to open several different administrative tools.
            * **Observation**: Discuss the purpose of the "Tools" tab as a quick way to access system utilities.

3.  **Configure Startup (if needed):**

    * Go to the "Startup" tab and click "Open Task Manager".
    * In Task Manager, go to the "Startup apps" tab.
    * Disable any unnecessary startup items to improve boot time. \*Be careful not to disable essential startup items.\*

4.  **Configure Services (if needed):**

    * Go to the "Services" tab in System Configuration.
    * Check "Hide all Microsoft services".
    * Disable any non-essential services. \*Note: Only disable services if you are sure they are not needed. Incorrectly disabling services can cause problems.\*

**Task 8: Managing the Windows Registry (Objective 4.0)**

**Objective:** Use Registry Editor to view and modify the Windows Registry.

**Steps:**

1.  **Open Registry Editor:**

    * Type "regedit" in the search bar and press Enter.
    * Click "Yes" in the User Account Control (UAC) dialog box. \*Important: The Registry Editor is a powerful tool. Incorrect changes can cause serious system problems. Follow these instructions carefully, and only make changes when absolutely necessary and you understand the implications.\*

2.  **Navigate the Registry:**

    * The Registry is organized in a hierarchical structure, similar to folders in File Explorer. The main branches are:
        * **HKEY_CLASSES_ROOT (HKCR):** Information about file types and COM objects.
        * **HKEY_CURRENT_USER (HKCU):** Settings for the currently logged-on user.
        * **HKEY_LOCAL_MACHINE (HKLM):** Settings for the local computer.
        * **HKEY_USERS (HKU):** Settings for all loaded user profiles.
        * **HKEY_CURRENT_CONFIG (HKCC):** Current hardware configuration.
    * Expand the branches in the left pane to navigate to specific keys (folders) and subkeys.
    * In the right pane, view the values associated with the selected key. Values have a name, type, and data.

3.  **View Registry Values:** \* In the left pane, navigate to `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion`. \* In the right pane, find the value named `ProductName`. \* Double-click on `ProductName` to open the "Edit String" dialog box. \* View the value data (e.g., "Windows 10 Pro"). \*Do not change the value.\*
    * **Adjustment**: Have the student navigate to the registry key specified and view the `ProductName`, `CurrentVersion`, and `SystemRoot` values.
    * **Observation**: Ask the student to identify the operating system version and the location of the Windows installation directory.

4.  **Export a Registry Key (Important Backup Step):**

    * Before making any changes, it is crucial to back up the registry key you are going to modify.
    * In the left pane, right-click on the key you want to export (e.g., `HKEY_CURRENT_USER\Control Panel\Desktop`).
    * Select "Export".
    * Choose a location to save the .reg file (e.g., your desktop) and enter a filename (e.g., "DesktopBackup.reg").
    * Click "Save".
        * **Adjustment**: Have the student export the `HKEY_CURRENT_USER\Control Panel\Desktop` key to their desktop. Then, have them delete the key (after confirming they have the backup) and then import the key.
        * **Observation**: Stress the importance of backing up registry keys before making any changes. Show that the export creates a .reg file.

5.  **Import a Registry Key (to Restore):** \* If you need to restore the registry key, double-click the .reg file that you saved. \* Click "Yes" to the UAC prompt, and then click "Yes" to import the data into the registry.

6.  **Add a New Registry Value (if needed):** \* In the left pane, navigate to the key where you want to add the value. \* Right-click in the right pane, select "New," and choose the data type of the value: \* **String Value:** For text data. \* **Binary Value:** For binary data. \* **DWORD (32-bit) Value:** For a 32-bit number. \* **QWORD (64-bit) Value:** For a 64-bit number. \* **Expandable String Value:** A string that can contain environment variables. \* Enter a name for the value. \* Double-click on the new value to edit its data. \* Enter the data and click "OK". \* \*Example: To change the desktop background, you might navigate to `HKEY_CURRENT_USER\Control Panel\Desktop`, create a new String Value named `Wallpaper`, and set its data to the path of the image file.\*
    * **Adjustment**: Have the students add a new string value
    * Observation: Verify that the students are able to add a new string value.

7.  **Modify an Existing Registry Value (if needed):** \* In the right pane, double-click the value you want to change. \* Enter the new data and click "OK".
    * Adjustment: Have the student modify a string value.
    * Observation: Verify that the students are able to modify a string value.

8.  **Delete a Registry Value or Key (if needed):** \* In the left or right pane, right-click on the value or key you want to delete. \* Select "Delete". \* Click "Yes" to confirm. \*Deleting the wrong key or value can cause problems.\*
    * Adjustment: Have the students delete a newly created string value.
    * Observation: Verify that the students are able to delete a string value.

**Task 9: Configuring Group Policies (Objective 4.0)**

**Objective:** Use Group Policy Editor to configure system and user settings.

**Steps:**

1.  **Open Group Policy Editor:**

    * Type "gpedit.msc" in the search bar and press Enter.

2.  **Navigate Group Policy:**

    * The Group Policy Editor is divided into two main sections:
        * **Computer Configuration:** Settings that apply to the computer, regardless of who logs on.
        * **User Configuration:** Settings that apply to specific users.
    * Within each section, settings are organized into categories:
        * **Software Settings:** Software installation and maintenance.
        * **Windows Settings:** Security settings, scripts, and other Windows configurations.
        * **Administrative Templates:** Registry-based settings that control the user interface and behavior of Windows and applications.

3.  **Example 1: Set the Default Desktop Background (User Configuration):** \* In the left pane, expand "User Configuration" > "Administrative Templates" > "Control Panel" > "Personalization". \* In the right pane, double-click on "Force a specific default wallpaper". \* In the dialog box: \* Select "Enabled". \* In the "Wallpaper Name" box, enter the full path to the wallpaper image file (e.g., `C:\\Windows\\Web\\Wallpaper\\Windows\\img0.jpg`). \* Click "OK". \* Close the Group Policy Editor. \* Open Command Prompt and run the command `gpupdate /force` and press Enter. \* Log off and log back on to see the change.
    * **Adjustment**: Have the student change the default desktop background using Group Policy. Provide them with the path to a wallpaper image. Have them verify the change.
    * **Observation**: Ensure the student can successfully navigate the Group Policy Editor, enable the policy, and specify the wallpaper path. Verify that the desktop background changes after the policy is applied and the user logs back on.

4.  **Example 2: Disable the Control Panel (User Configuration):** \* In the left pane, expand "User Configuration" > "Administrative Templates" > "Control Panel". \* In the right pane, double-click on "Prohibit access to Control Panel and PC settings". \* In the dialog box: \* Select "Enabled". \* Click "OK". \* Close the Group Policy Editor. \* Open Command Prompt and run the command `gpupdate /force` and press Enter. \* Log off and log back on to see the change.
    * **Adjustment**: Have the student disable access to the Control Panel using Group Policy. Have them attempt to open the Control Panel and observe the result. Then, have them disable the policy and verify that they can access the Control Panel again.
    * **Observation**: Ensure the student can successfully configure the Group Policy to disable Control Panel access. Verify that the Control Panel is inaccessible when the policy is in effect and accessible when the policy is disabled.

5.  **Update Group Policy:**

    * Group Policy changes do not take effect immediately. To apply changes:
        * **Method 1:** Close and reopen the application or setting.
        * **Method 2:** Log off and log back on.
        * **Method 3:** Open Command Prompt (as administrator) and run the command `gpupdate /force` and press Enter. This forces an immediate update of Group Policy settings.
        * **Adjustment**: Have the student make a change to a Group Policy setting and then use all three methods to apply the change. Have them observe when the change takes effect in each case.
        * **Observation**: Discuss the different methods for updating Group Policy and their effectiveness. Explain the purpose of the `gpupdate /force` command.

**Task 10: Managing Windows System Tools (Objective 1.0)**

**Objective:** Use various Windows system tools for administration and troubleshooting.

**Steps:**

1.  **Accessing System Tools:**

    * Many system tools are located in the "Administrative Tools" folder:
        * **Method 1:** Type "administrative tools" in the search bar and press Enter.
        * **Method 2:** Open Control Panel, go to "System and Security" > "Administrative Tools".

2.  **Key System Tools:**

    * **Component Services:** Configure COM+ components.
    * **Computer Management:** A collection of administrative tools, including:
        * **Event Viewer**
        * **Task Scheduler**
        * **Shared Folders**
        * **Local Users and Groups**
        * **Performance Monitor**
        * **Device Manager**
        * **Disk Management**
        * **Services**
    * **Defragment and Optimize Drives:** Optimize hard drive performance.
    * **Disk Cleanup:** Free up disk space by deleting unnecessary files.* **Event Viewer:** View system, application, and security logs.
    * **Local Security Policy:** Configure security settings (only available on Windows Pro and Enterprise editions).
    * **Performance Monitor:** Analyze system performance.
    * **Resource Monitor:** View real-time resource usage (CPU, memory, disk, network).
    * **System Configuration:** Configure startup and services.
    * **System Information:** View detailed system information.
    * **Task Scheduler:** Schedule automated tasks.
    * **Windows Firewall with Advanced Security:** Configure firewall settings.

3.  **Using a System Tool (Example: Services):**

    * Open "Services" from the Administrative Tools" folder.
    * View the list of system services.
    * Right-click on a service to:
        * **Start:** Start the service.
        * **Stop:** Stop the service.
        * **Restart:** Restart the service.
        * **Properties:** Configure the service's startup type (Automatic, Manual, Disabled), recovery options, and dependencies.
            * **Adjustment**: Have the student change the startup type of a non-critical service (e.g., a third-party service) from "Manual" to "Automatic". Then, have them restart the computer and check if the service is running. (Make sure they choose a service that is not essential for system stability and note the original startup type.)
            * **Observation**: Discuss the different service startup types (Automatic, Manual, Disabled) and what they mean. Explain how to configure a service to start automatically at boot. **Important**: Emphasize the need to be very careful when changing service settings.
