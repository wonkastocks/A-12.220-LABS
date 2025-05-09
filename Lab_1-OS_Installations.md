# 1- OS installations

## Task List


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Install Windows 11 From Install Media | Objective 1.1 |
| Break Windows 11 Install       | Objective 1.1 |
| Restore Windows 11             | Objective 1.1 |
| Create an Extra Drive for Windows 11 | Objective 1.1 |
| Manage New Drive               | Objective 1.1 |
| Run a PC Health Check          | Objective 1.1 |
| Configure Internet Access      | Objective 1.1 |
| Driver Update                  | Objective 1.1 |
| Create a New User Profile      | Objective 1.1 |
| Login to New Account           | Objective 1.1 |
| Backup a User Profile          | Objective 1.1 |
| Delete a User Profile          | Objective 1.1 |
| Restore a Profile from Backup  | Objective 1.1 |
| Installing Ubuntu Linux        | Objective 1.1 |






## Tasks to be Covered and Correlated Objectives


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| **Operating system installations and upgrades** | |
| Install Windows 11 From Install Media | Objective 1.1 |
| **Break the Windows 11 Installation** | |
| Break Windows 11 Install       | Objective 1.1 |
| **Restoring Windows 11** | |
| Restore Windows 11             | Objective 1.1 |
| **Create an Extra Drive for Windows 11** | |
| Create an Extra Drive for Windows 11 | Objective 1.1 |
| **Manage New Hard Drive** | |
| Manage New Drive               | Objective 1.1 |
| **Run a PC Health Check** | |
| Run a PC Health Check          | Objective 1.1 |
| **Configure Internet Access** | |
| Configure Internet Access      | Objective 1.1 |
| **Driver Update** | |
| Driver Update                  | Objective 1.1 |
| **Create a New User Profile** | |
| Create a New User Profile      | Objective 1.1 |
| **Log In to the New Account** | |
| Login to New Account           | Objective 1.1 |
| **Backup a User Profile** | |
| Backup a User Profile          | Objective 1.1 |
| **Delete a User Profile** | |
| Delete a User Profile          | Objective 1.1 |
| **Restore a User Profile from a Backup** | |
| Restore a Profile from Backup  | Objective 1.1 |
| **Installing Ubuntu Linux** | |
| Installing Ubuntu Linux        | Objective 1.1 |

## Lab Steps

### Install Windows 11 from Install Media

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

### Create an Extra Drive for Windows 11

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

1. In the search box, type **health**.
2. Select **Device performance & health**.
3. Examine the Health Report.
4. Right-click **Start** and select **Terminal (Admin)**.
5. Click **Yes** in the UAC window.
6. At the PowerShell prompt, type: 
New-NetIPAddress -InterfaceAlias Ethernet -IPAddress 192.168.0.20 -PrefixLength 24 -DefaultGateway 192.168.0.250

lua
Copy
7. Press Enter.
8. At the next prompt, type: 
Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 1.1.1.1

markdown
Copy
9. Press Enter.
10. Close the Windows Terminal.

---
## Create a New User Profile

1. Right-click **Start** and select **Device Manager**.
2. Expand **Display Adapters**.
3. Right-click **Microsoft Hyper-V Video** and select **Update Driver**.
4. Click **Search automatically for drivers**.
5. Click **Search for updated drivers on Windows Update**.
6. Click **Advanced options**.
7. Click **Optional updates**.
8. Close the **Settings** app.
9. Close **Device Manager**.

---

## Log In to the New Account

1. In the search bar, type **users** and select **Other Users**.
2. Click **Add Account**.
3. Click **I don't have this person's sign-in information**.
4. Click **Add a user without a Microsoft account**.
5. In the **User name** box, type **Student2**.
6. In the **password** boxes, type **Passw0rd**.
7. For each of the security questions, drop down the list and select the first option that is not greyed out.
8. For each of the answers, enter **ACI**.
9. Click **Next**.

## Backup a User Profile

1. Double-click the login screen so that the login prompt appears.
2. Select **Student** and type **Passw0rd** in the box provided and press Enter.
3. Minimize the connection window.
4. Click **File Explorer** in the taskbar of the Host.
5. In the left pane, click **Hyper-V (E:)**.
6. In the right pane, right-click the empty space and select **New > Folder**.
7. Name the folder **Profiles** and press Enter.
8. Right-click **Profiles** and select **Properties**.
9. Click the **Sharing** tab.
10. Click the **Advanced Sharing** button.
11. Check the **Share this folder** checkbox.
12. Click the **Permissions** button.
13. Check the checkbox for the **Change** permission in the **Allow** column.
14. Click **OK**.

---

## Installing Ubuntu Linux

1. Click **Ubuntu Install** on the topology map.
2. You will be presented with the **Choose your language** page. Click the **Reboot** button in the VM window toolbar.
3. Click **OK** to reboot the VM.
4. This process may take a few minutes, please be patient.
5. You will again be presented with the **Choose your language** page. Click **Next**.
6. On the **Accessibility** page, click **Next**.
7. On the **Select your keyboard layout** page, click **Next**.
8. On the **Connect to the internet** page, select **Do not connect to the internet**, and click **Next**.
9. On the **What do you want to do with Ubuntu?** page, click **Next**.
10. On the **How would you like to install Ubuntu?** page, click **Next**.
11. On the **What apps would you like to start with?** page, click **Next**.
12. On the **Install proprietary software?** page, click **Next**.
13. On the **How do you want to install Ubuntu?** page, click **Next**.
14. Enter the following information and click **Next**:
 - **Your name**: Student
 - **Password**: Passw0rd
 - **Confirm Password**: Passw0rd
 - **Timezone**: New York
15. Click **Install**.
16. Please wait while Ubuntu installs.
17. Once it is finished, click **Restart Now**.
18. If you get the message **Please remove the install medium, and press ENTER**, just press Enter to finish the reboot.
19. When presented with the login screen, click **Student**.
20. Enter the password **Passw0rd** and press **Enter**.
21. Click **Next** three times, then click **Finish**.
22. Click the **Power** icon in the upper right corner.
23. Click the gear icon to enter the **Settings** app.
24. In the **Network** panel, under **Wired**, click the gear icon to enter wired network configuration.
25. Click the **IPv4** tab.
26. Select **Manual**.
27. Enter the following details:
 - **Address**: 192.168.0.30
 - **Netmask**: 24
 - **Gateway**: 192.168.0.250
 - **DNS**: 1.1.1.1
28. Click **Apply**.
29. Click the **Show Apps** button at the bottom left of the screen.
30. Type **terminal** in the search box.
31. Click on **Terminal** to open a terminal window.
32. At the prompt, type:
 ```
 ping -c 4 cisco.com
 ```
33. Press Enter. You should get success messages for all 4 pings.
34. Close the VM window and click the **Stop** button to complete the lab.
