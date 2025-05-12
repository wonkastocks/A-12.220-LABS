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

1.  **Open Task Manager:**

    * **Method 1:** Press `Ctrl + Shift + Esc`.
    * **Method 2:** Right-click on the taskbar and select "Task Manager."
    * **Method 3:** Type "Task Manager" in the search bar and press Enter.

2.  **Explore the Tabs:**

    * **Processes:** View running applications and background processes, and their resource usage (CPU, Memory, Disk, Network).
    * **Performance:** Monitor overall system performance, including CPU, memory, disk, Wi-Fi, and Ethernet. Click on each item to see detailed graphs.
    * **Users:** See logged-on users.
    * **Details:** Provides more detailed information about processes than the "Processes" tab.
    * **Services:** Manage system services (start, stop, restart).

3.  **Monitor Resource Usage:**

    * Observe the CPU, Memory, Disk, and Network graphs on the "Performance" tab. Note any high usage.
        * \* **Adjustment:** Have the student open several applications (e.g., a web browser, a word processor, a video player) simultaneously.
        * \* **Observation:** Ask the student to observe how the CPU and Memory usage changes as they open more applications. Have them identify which applications are consuming the most resources.
    * On the "Processes" tab, click on the CPU, Memory, Disk, and Network columns to sort processes by resource usage. Identify resource-intensive processes.
        * **Adjustment:** Have the student sort the processes by CPU usage and identify the top 3 consumers. Then, have them sort by Memory usage and note the top 3.
        * **Observation:** Discuss with the student why certain applications or processes might use more resources than others (e.g., a video game vs. a text editor).

4.  **End a Process (if necessary):**

    * On the "Processes" tab, select a non-critical process (do *not* end system processes unless absolutely necessary for troubleshooting and you know what you are doing).
        * **Adjustment:** Have the student open Notepad and type some text. Then, have them locate the Notepad process in Task Manager.
    * Click "End task."
        * **Observation:** Ask the student what happens to the Notepad application. Discuss the importance of saving work before ending a process.

5.  **View Startup Apps:**

    * Go to the "Startup apps" tab.
    * Note the applications that start automatically when Windows starts.
    * To disable a startup app, select it and click "Disable". \*Note:\* Be careful not to disable essential startup items.
        * **Adjustment:** Have the student identify a non-essential startup app and disable it. Then, have them restart the computer.
        * **Observation:** Ask the student if they notice any difference in the startup time after disabling the application. Discuss the impact of startup apps on system performance.

**Task 2: Managing System Resources with MMC Snap-ins (Objective 1.0)**

**Objective:** Use Microsoft Management Console (MMC) to manage system resources.

**Steps:**

1.  **Open MMC:**

    * Type "mmc" in the search bar and press Enter.

2.  **Add Snap-ins:**

    * Click "File" > "Add/Remove Snap-in..."
    * In the "Available snap-ins" list, select the following, clicking "Add >" after each, and then click "OK":
        * **Event Viewer:** View system, application, and security logs.
        * **Disk Management:** Manage hard drives, partitions, and volumes.
        * **Task Scheduler:** Schedule automated tasks.
        * **Device Manager:** Manage hardware devices and drivers.
        * **Performance Monitor:** Analyze system performance.
    * Click "OK".

3.  **Use the Snap-ins:**

    * **Event Viewer:**
        * Expand "Event Viewer (Local)" in the left pane.
        * Explore "Windows Logs" (Application, Security, System) to view events.
            * **Adjustment:** Have the student navigate to the "System" log and look for any "Error" events.
        * Click on an event to see its details.
            * **Observation:** Ask the student to describe the information provided in the event details (e.g., event ID, source, description). Discuss the importance of Event Viewer for troubleshooting.
    * **Disk Management:**
        * In the left pane, click on "Disk Management".
        * View the list of disks and their partitions. (Do *not* make changes unless specifically instructed).
            * **Adjustment:** Have the student identify the file system type (e.g., NTFS, FAT32) of their system partition. Ask them to also identify the capacity and free space of a particular drive.
        * Right-click on a partition to see available options (e.g., Format, Delete Volume).
            * **Observation:** Discuss the options available. Emphasize the importance of understanding the consequences of formatting or deleting a volume.
    * **Task Scheduler:**
        * In the left pane, click on "Task Scheduler (Local)".
        * Explore the Task Scheduler Library
            * **Adjustment:** Have the student locate a scheduled task (e.g., a disk defragmentation task).
        * Click "Create Basic Task..." in the right pane to create a new task (walk through the wizard, but do not save unless instructed).
            * **Observation:** Discuss the different triggers and actions that can be configured for a task.
    * **Device Manager:**
        * In the left pane, click on "Device Manager".
        * Expand the different device categories (e.g., "Disk drives," "Network adapters").
        * Right-click on a device to view its properties, update drivers, or disable it.
            * **Adjustment:** Have the student check the driver version of their network adapter. Then, have them open the properties of their display adapter and look at the driver tab.
            * **Observation:** Show the student how to check for driver updates. Discuss the importance of keeping drivers up to date.
    * **Performance Monitor:**
        * In the left pane, click on "Performance Monitor".
        * Click the green "+" button to add counters.
        * Select performance counters (e.g., "CPU Usage," "Memory\\Available MBytes") and click "Add".
        * Click "OK" to view the performance graph.
            * **Adjustment**: Have the student add the "Processor Time" counter for all processor instances and observe the graph while opening and closing different applications.
            * **Observation:** Ask the student to describe how the graph changes as they open and close applications. Discuss how Performance Monitor can be used to identify performance bottlenecks.
    * Save the Console (Optional):
        * Click "File" > "Save As..."
        * Enter a name for the console (e.g., "AdminTools.msc") and save it to the desktop. This allows you to quickly access the same snap-ins later.

**Task 3: Analyzing System Information and Resources (Objective 1.0)**

**Objective:** Use System Information and Resource Monitor to analyze system details.

**Steps:**

1.  **Open System Information:**

    * Type "msinfo32" in the search bar and press Enter.

2.  **Explore System Information:**

    * In the left pane, explore the different categories:
        * **System Summary:** View basic system information (OS version, system manufacturer, processor, memory).
            * **Adjustment**: Have the student locate the BIOS version and the total physical memory.
            * **Observation**: Discuss what IRQs, DMAs, and I/O ports are and their significance.
        * **Components:** View information about installed software and drivers.
            * **Adjustment**: Have the student check the version of a specific driver (e.g., the display driver or network adapter driver).
        * **Software Environment:** View running processes, startup programs, and environment variables.
            * **Observation**: Have the student list the startup programs and compare them to what they saw in Task Manager.

3.  **Open Resource Monitor:**

    * Type "resmon" in the search bar and press Enter.
    * \* **Alternative:** Open Task Manager, go to the "Performance" tab, and click "Open Resource Monitor" at the bottom.

4.  **Analyze Resources:**

    * **CPU:** Monitor CPU usage by process, service, and thread.
        * **Adjustment**: Have the student run a CPU-intensive task (e.g., video encoding or a benchmark test) and observe the CPU usage in Resource Monitor.
        * **Observation**: Ask the student to identify the processes that are consuming the most CPU. Discuss the difference between CPU usage by process, service, and thread.
    * **Memory:** View memory usage, including physical memory, commit charge, and hard faults.
        * **Adjustment**: Have the student open several applications and observe the memory usage. Then, have them close the applications and observe the change.
        * **Observation**: Discuss the concepts of physical memory, commit charge, and hard faults. Explain how these values can indicate memory problems.
    * **Disk:** Monitor disk activity, including read/write speeds and disk queue length.
        * **Adjustment**: Have the student copy a large file from one drive to another and monitor the disk activity.
        * **Observation**: Ask the student to describe the disk activity during the file transfer. Discuss how disk queue length can indicate a disk bottleneck.
    * **Network:** View network activity, including bandwidth usage and network connections.
        * **Adjustment**: Have the student start a large download and monitor the network usage.
        * **Observation**: Ask the student to identify the process that is using the most network bandwidth. Discuss how Resource Monitor can be used to identify network-related issues.

**Task 4: Managing and Optimizing Disk Performance (Objective 4.0)**

**Objective:** Use tools to manage and optimize disk performance.

**Steps:**

1.  **Open Disk Defragmenter:**

    * Type "dfrgui" in the search bar and press Enter.
    * \*Note: On modern systems with SSDs, this tool may be called "Optimize Drives" and perform different functions appropriate to the drive type.\*

2.  **Analyze a Drive:**

    * Select a drive (e.g., C:).
    * Click "Analyze". The tool will analyze the drive for fragmentation.
        * **Observation**: Have the student note the fragmentation percentage before and after optimization. Discuss what file fragmentation is and why it impacts performance.

3.  **Optimize the Drive (if needed):**

    * If the analysis shows significant fragmentation (typically, more than 10%), click "Optimize".
    * \*For SSDs, the "Optimize" function will perform operations like TRIM, which helps maintain performance, rather than defragmentation.\*
        * **Adjustment**: If an SSD is present, have the student analyze and "optimize" it. Discuss the difference in operations performed on SSDs vs. HDDs.
        * **Observation**: Discuss the purpose of TRIM and how it helps maintain SSD performance.

4.  **Open Disk Cleanup:**

    * Type "cleanmgr" in the search bar and press Enter.
    * Select the drive you want to clean (e.g., C:) and click "OK".
    * Disk Cleanup will calculate space that can be freed.
    * In the list of "Files to delete", check the boxes for the types of files you want to delete (e.g., "Temporary Internet Files," "Recycle Bin").
    * Click "OK" to delete the files.
    * For more options, click "Clean up system files".
        * **Adjustment**: Have the student use Disk Cleanup to remove temporary files and empty the Recycle Bin. Then, have them check the amount of free space on the drive before and after the cleanup.
        * **Observation**: Discuss the different types of files that Disk Cleanup can remove and their purpose. Discuss the importance of regularly cleaning up unnecessary files.

**Task 5: Using Command-Line for File and Folder Navigation (Objective 4.0)**

**Objective:** Use Command Prompt to navigate the file system.

**Steps:**

1.  **Open Command Prompt:**

    * Type "cmd" in the search bar.
    * Right-click on "Command Prompt" in the search results and select "Run as administrator". (Some commands require administrator privileges.)

2.  **Basic Navigation:**

    * `cd <directory>`: Change directory. For example, `cd Documents` to go to the Documents folder, or `cd \` to go to the root of the drive.
        * **Adjustment**: Have the student create a new folder on the C: drive using the `md` command. Then, have them use the `cd` command to navigate into that folder.
    * `cd ..`: Go up one directory level.
        * **Observation**: Have the student navigate to a subfolder and then use `cd ..` to go back to the parent folder.
    * `dir`: List the files and subdirectories in the current directory.
        * `dir /p`: Pauses the output, displaying one screen at a time.
        * `dir /w`: Displays the listing in wide format.
        * `dir /a`: Displays all files, including hidden and system files.
            * **Adjustment**: Have the student use the `dir` command with different switches (`/p`, `/w`, `/a`) and observe the differences in the output. Have them create a few text files and then use `dir` with wildcards.
            * **Observation**: Discuss the different ways the `dir` command can be used to display file and folder information. Explain the purpose of the different switches.
    * `md <directory name>`: Create a new directory (folder). For example, `md NewFolder`.
    * `rmdir <directory name>`: Remove an empty directory. For example, `rmdir NewFolder`. (Use `rmdir /s <directory name>` to remove a directory and its subdirectories and files).
        * **Adjustment**: Have the student create a directory with subdirectories and files. Then, have them try to remove the parent directory with `rmdir` and then with `rmdir /s`.
        * **Observation**: Discuss the difference between removing an empty directory and a directory with content. Emphasize the importance of using the `/s` switch with caution.
    * `copy <source> <destination>`: Copy a file. For example, `copy file1.txt C:\Backup`.
    * `move <source> <destination>`: Move a file or directory. For example, `move file1.txt C:\Backup`
        * **Adjustment**: Have the student copy a file from one folder to another, then move it back. Then, have them try to copy a file to a directory that doesn't exist.
        * **Observation**: Discuss the different ways the `copy` and `move` commands can be used. Explain how to handle errors, and what happens if the destination directory does not exist.
    * `del <filename>`: Delete a file. For example, `del file1.txt`. (Use with caution!)
        * **Adjustment**: Have the student create a text file and then delete it using the `del` command. Then, have them try to delete a file that doesn't exist.
        * **Observation**:  **Important:** Emphasize the importance of using the `del` command with caution, as deleted files are not sent to the Recycle Bin when deleted from the command line.
    * `type <filename>`: Display the contents of a text file.
        * **Adjustment**: Have the student create a text file with several lines of text and then use the `type` command to display its contents.
        * **Observation**: Discuss how the `type` command can be used to quickly view the contents of a text file.

3.  **Wildcards:**

    * `*`: Represents any character(s). For example, `dir *.txt` lists all files with the .txt extension.
    * `?`: Represents any single character. For example, `dir file?.txt` lists files like file1.txt, file2.txt, etc.
        * **Adjustment**: Have the student create several files with different names and extensions and then use wildcards to list specific groups of files. For example, have them create files like `file1.txt`, `file2.txt`, `fileA.txt`, `fileB.dat`, and then use commands like `dir file*.txt`, `dir file?.txt`, and `dir *.*`.
        * **Observation**: Discuss how wildcards can be used to select multiple files and directories that match a pattern.

4.  **Pathname Conventions**

    * Absolute path: Specifies the exact location of a file or directory, starting from the root directory (e.g., `C:\Users\Username\Documents\MyFile.txt`).
    * Relative path: Specifies the location relative to the current directory (e.g., if you are in `C:\Users\Username`, then `Documents\MyFile.txt` refers to the same file).
        * **Adjustment**: Have the student navigate to a specific directory using both absolute and relative paths. For example, have them navigate to their "Documents" folder using both `cd C:\Users\Username\Documents` and `cd Documents` (assuming they are currently in `C:\Users\Username`).
        * **Observation**: Discuss the difference between absolute and relative paths and when each might be more useful.

**Task 6: Using Command-Line for Network Management (Objective 4.0)**

**Objective:** Use Command Prompt to manage network settings and troubleshoot network issues.

**Steps:**

1.  **Open Command Prompt (as administrator):**

    * Type "cmd" in the search bar.
    * Right-click on "Command Prompt" in the search results and select "Run as administrator".

2.  **Basic Network Commands:**

    * `ipconfig`: Display basic IP configuration information for all network adapters.
        * `ipconfig /all`: Display detailed IP configuration information, including DNS servers, MAC address, and DHCP status.
            * **Adjustment**: Have the student use `ipconfig` and `ipconfig /all` and compare the output. Have them identify their IP address, subnet mask, default gateway, and DNS servers.
        * `ipconfig /release`: Release the current IP address obtained from a DHCP server.
        * `ipconfig /renew`: Request a new IP address from a DHCP server.
            * **Adjustment**: If the student's computer is using DHCP, have them use `ipconfig /release` and then `ipconfig /renew`. Have them observe the change in their IP address. Ifconfig /all before and after
            * **Observation**: Discuss the difference between static and dynamic IP addressing. Explain the role of DHCP.
    * `ping <destination>`: Test network connectivity by sending ICMP echo request packets to a destination (e.g., `ping 8.8.8.8` to ping Google's public DNS server, or `ping www.google.com` to ping Google's website).
        * **Adjustment**: Have the student ping several different destinations (e.g., their local router, a website, another computer on the network). Have them ping using both the IP address and the domain name.
        * **Observation**: Discuss the output of the `ping` command and how it indicates network connectivity. Explain what the round-trip time (RTT) means. Discuss how to interpret packet loss.
    * `netstat`: Display active network connections and listening ports.
        * `netstat -a`: Display all active connections and listening ports.
        * `netstat -b`: Show the executable involved in creating each connection or listening port.
        * `netstat -n`: Display addresses and port numbers in numerical form.
            * **Adjustment**: Have the student use `netstat` with different switches (`-a`, `-b`, `-n`) and compare the output. Have them identify the state of different connections (e.g., ESTABLISHED, LISTEN).
            * **Observation**: Discuss the different states of network connections and what they mean. Explain the concept of ports and how they are used by network applications.
    * `nslookup <domain name>`: Query DNS servers to find the IP address associated with a domain name (e.g., `nslookup www.google.com`). Also used to troubleshoot DNS issues.
        * **Adjustment**: Have the student use `nslookup` to find the IP address of several websites. Then, have them try to use `nslookup` on a non-existent domain name.
        * **Observation**: Discuss the role of DNS in resolving domain names to IP addresses. Explain how `nslookup` can be used to troubleshoot DNS problems.
    * `net use`: Connect to, disconnect from, or display information about shared resources (e.g., network drives, printers).
        * `net use Z: \\servername\sharename`: Map the network share `\\servername\sharename` to drive letter Z:.
        * `net use Z: /delete`: Disconnect from drive Z:.
            * **Adjustment**: If there is a network share available, have the student map a network drive using the `net use` command and then disconnect from it.
            * **Observation**: Discuss how the `net use` command can be used to access shared resources on a network.
    * `tracert <destination>`: Trace the route that packets take to reach a destination, showing each hop along the way (e.g., `tracert www.google.com`).
        * **Adjustment**: Have the student use `tracert` to trace the route to several different destinations (e.g., a local website, a remote website).
        * **Observation**: Discuss the output of the `tracert` command and how it shows the path that network traffic takes. Explain how `tracert` can be used to identify network bottlenecks.
    * `pathping <destination>`: Similar to tracert, but also provides information about packet loss at each hop.
        * **Adjustment**: Have the student compare the output of `tracert` and `pathping` to the same destination.
        * **Observation**: Discuss the additional information provided by `pathping`, such as packet loss statistics.

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
