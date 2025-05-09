# Operating System Installations and Upgrades

## Introduction

### Install Windows 11 from Install Media

**Task:** Perform a clean installation of Windows 11 from installation media.
**Objective Reference:** 1.1

1. Click the **Start** button to provision the lab.
2. When the lab finishes starting up, click **Hyper-V Server** in the topology map.
3. Click **Send Ctrl+Alt+Delete**.
4. Sign in to the **Administrator** account with the password `P@ssw0rd`.
5. Click the **Hyper-V Manager** icon in the taskbar.
6. In the middle pane, double-click **Win11A**. A connection window will appear.
7. Click the **Start** button to power on the VM.
8. To start the installer, click inside the Connection window and press any key.
   - **Note**: If this process fails, click the **Action** menu and select **Reset**, and try again.
9. Once you have successfully started setup, click the **Maximize** button on the connection window.
10. At the **Select language settings** window, click **Next**.
11. At the **Select keyboard settings** window, click **Next**.
12. At the **Select setup option** window, select the checkbox for "I agree everything will be deleted including files, apps, and settings."
13. Click **Next**.
14. At the **Product key** window, select the link for **I don't have a product key**.
15. At the **Select image** window, choose **Windows 11 Pro**, and click **Next**.
16. At the **Applicable notices and license terms** window, click **Accept**.
17. At the **Select location to install Windows 11** window, click **Next**.
18. At the **Ready to install** window, click **Install**.
19. Please wait while Windows 11 installs. The VM may restart several times.
20. At the **Is this the right country or region** page, press **Shift+F10** (If that doesn't work try **Shift+FN+F10**).
21. In the Command Prompt window, type: `OOBE\BypassNRO` and press **Enter**.
   - **Note**: This command allows a user to bypass the network requirement for Windows 11 and may be removed in a future version.
22. At the **Is this the right keyboard layout or input method** page, click **Yes**.
23. At the **Want to add a second keyboard layout** page, click **Skip**.
24. When you get to the **Let's connect you to a network** page, click **I don't have internet**.
25. At the **Who's going to use this device** page, type the username **Student** and click **Next**.
26. At the **Create a super memorable password** page, type the password **Passw0rd** and click **Next**.
27. At the **Confirm your password** page, type **Passw0rd** again and click **Next**.
28. At the **Now add security questions** page, drop down the menu and click the first item.
29. In the answer box, type **ACI** and click **Next**.
30. Repeat this for questions 2 and 3.
31. At the **Choose privacy settings for your device** page, click **Next** twice, then **Accept**.
32. Please wait while the **Student** profile is created.

---

## Break the Windows 11 Installation

**Task:** Simulate a failed Windows 11 installation by intentionally corrupting system files.
**Objective Reference:** 1.1

1. When the desktop appears, leave the VM in its current state and proceed to the next exercise.
2. Click **File Explorer** to open it.
3. In the **Search** field, type in **ntoskrnl**.
4. Right-click **ntoskrnl** and select **Properties**.
5. Click the **Advanced** button.
6. Next to **TrustedInstaller**, click the **Change** link.
7. In the text box, type in **Student**, then click the **Check Names** button.
8. Click **OK**.
9. In the **Advanced Security Settings for ntoskrnl** window, click **OK**.
10. In the **ntoskrnl Properties** window, click **Edit**.
11. Click **Add**. In the text box, type in **Student** and click **Check Names**.
12. Click **OK**.
13. In the **Allow** column, click the check box for **Full Control**.
14. Click **OK**.
15. In the **Windows Security** window, click **Yes**.

---

## Restoring Windows 11

**Task:** Restore a non-booting Windows 11 system using built-in recovery tools.
**Objective Reference:** 1.2

### Create an Extra Drive for Windows 11

**Task:** Add and configure an extra virtual hard drive in Windows 11.
**Objective Reference:** 1.2

1. Right-click **ntoskrnl** file and click **Delete**.
2. Right-click **Recycle bin** and select **Empty Recycle Bin**.
3. Click **Yes** to permanently delete the file.
4. Right-click **Start** and select **Shut down or sign out > Restart**.
5. As the VM attempts to make automatic repairs, move to the next section.
6. When **Automatic Repair** fails, you will be presented with a blue screen.
7. Click **Advanced options**.
8. Click **Troubleshoot**.
9. Click **Reset this PC**.
10. Click **Keep my files**.
11. Click **Local reinstall**.
12. Click **Reset**.
13. While the reset is processing, move on to the next section.
14. When the Reset operation completes, you will be presented with the login screen.

---

## Manage New Hard Drive

**Task:** Partition, format, and label a new hard drive in Windows 11.
**Objective Reference:** 1.2

1. Enter **Passw0rd** in the password field and press Enter to login.
2. Right-click **Start** and select **Disk Management**.
3. In the **Initialize Disk** window, select **MBR (Master Boot Record)** and click **OK**.
4. Click on **Disk 1**.
5. Right-click **Disk 1** and select **Convert to GPT Disk**.
6. Click the unallocated space for **Disk 1**.
7. Right-click the unallocated space and choose **New Simple Volume**.
8. Click **Next** three times.
9. In the **Volume label** box, replace the text with **Test Disk**.
10. Click **Next**.
11. Click **Finish**.
12. Close the **Disk Manager** window.

---

## Configure Internet Access

**Task:** Configure and verify internet access and perform a PC health check in Windows 11.
**Objective Reference:** 1.4

1. In the search box, type **health**.
2. Select **Device performance & health**.
3. Examine the Health Report.
4. Right-click **Start** and select **Terminal (Admin)**.
5. Click **Yes** in the UAC window.
6. At the PowerShell prompt, type: 




---

## Discussion Questions

**Question 1:**

What are the key considerations when performing a clean installation versus an upgrade installation of Windows 11?

**Answer:**

A clean installation completely erases the existing operating system and user data, providing a fresh start and often better performance, but requires full data backup and application reinstallation. An upgrade installation preserves user data, settings, and applications but may carry over issues from the previous OS. Key considerations include hardware compatibility, data backup, application compatibility, and licensing. (Objective 1.1)

**Question 2:**

Why is it important to verify hardware compatibility before installing a new operating system, and how can you do this for Windows 11?

**Answer:**

Verifying hardware compatibility ensures the OS will function correctly and receive updates. For Windows 11, Microsoft provides the PC Health Check tool to verify requirements such as TPM 2.0, Secure Boot, CPU, RAM, and storage. Incompatible hardware may prevent installation or cause instability. (Objective 1.1)

**Question 3:**

Describe the process and purpose of partitioning and formatting a hard drive during an OS installation.

**Answer:**

Partitioning divides a physical drive into logical sections, allowing for multiple operating systems or data separation. Formatting prepares a partition with a file system (like NTFS or FAT32) so the OS can store files. This process is essential for organizing data and ensuring the OS can access and manage storage. (Objective 1.2)

**Question 4:**

What are some common reasons an OS installation might fail, and how can you troubleshoot them?

**Answer:**

Common reasons include hardware incompatibility, corrupt installation media, insufficient disk space, or missing drivers. Troubleshooting steps include verifying hardware requirements, using official installation media, checking for error codes, and reviewing installation logs. (Objective 1.3)

**Question 5:**

Explain the importance of applying updates and drivers immediately after installing a new operating system.

**Answer:**

Applying updates and drivers ensures the OS is secure, stable, and compatible with hardware. Updates patch vulnerabilities and improve performance, while drivers enable hardware functionality. Failing to update can leave the system exposed to security risks and hardware malfunctions. (Objective 1.4)

