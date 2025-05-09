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

**Operating system installations and upgrades**

Ensure Hard Drive is selected and click Add.

Drop down the Location box and select 3.

Ensure that Virtual hard disk is selected and click the New button.

Click the Next button three times.

In the Size box enter 20 and click Next

Click Finish.

Click OK to close the Settings window.

Click the Start button to power on the VM again.

Click the Maximize button to make the connection window full screen.

Double click the login screen to make the prompt appear.






**Manage New Hard Drive**

Run a PC Health Check

Enter Passw0rd in the password ﬁeld and press Enter to login.

Leave the VM in this state and continue to the next section.

Right click Start and select Disk Management.

In the Initialize Disk window select MBR (Master Boot Record) and click OK.

Click on Disk 1.

Right click Disk 1 and select Convert to GPT Disk.

Click the unallocated space for Disk 1.

Right click the unallocated space and choose New Simple Volume.

Click Next 3 times.

In the Volume label box replace the text with Test Disk.

Click Next.

Click Finish.

Close the Disk Manager window.

Leave the device in its current state and proceed to the next section.

## Lab Steps

### Install Windows 11 from Install Media
Click the Start button to provision the lab.
When the lab finishes starting up, click Hyper-V Server in the topology map.
Click Send Ctrl+Alt+Delete.
Sign in to the Administrator account with the password of P@ssword.
Click the Hyper-V Manager icon in the taskbar.
In the middle pane, double click Win11A. A connection window will appear.
Click the Start button to power on the VM.
To start the installer you must click inside the Connection window and press any key.
NOTE: If this process fails, simply click the Action menu and select Reset, and try again.
Once you have successfully started setup, click the Maximize button on the connection window.
At the Select language settings window, click Next.
At the Select keyboard settings window, click Next.
At the Select setup option window, select the checkbox for I agree everything will be deleted including files, apps, and settings.
Click Next.
At the Product key window, select the link for I don't have a product key.
At the Select image window, choose Windows 11 Pro, and click Next.
At the Applicable notices and license terms window, click Accept.
At the Select location to install Windows 11 window, click Next.
At the Ready to install window, click Install.
Please wait while Windows 11 installs. The VM may restart several times.
At the Is this the right country or region page, press Shift+F10 (If that doesn't work try Shift+FN+F10).
Click inside the Command Prompt window and type: OOBE\BypassNRO and press Enter.
NOTE: This command allows a user to bypass the network requirement for Windows 11 and may be removed in a future version.
At the Is this the right keyboard layout or input method page, click Yes.
At the Want to add a second keyboard layout page, click Skip.
When you get to the Let's connect you to a network page, click I don't have internet.
At the Who's going to use this device page, type the username Student and click Next.
At the Create a super memorable password page, type the password Password and click Next.
At the Confirm your password page, type Password again and click Next.
At the Now add security questions page, drop down the menu and click the first item.
In the answer box, type ACI and click Next.
Repeat this for questions 2 and 3.
At the Choose privacy settings for your device page, click Next twice, then Accept.
Please wait while the Student profile is created.
When the desktop appears, leave the VM in its current state and proceed to the next exercise.

### Break the Windows 11 Installation
Click File Explorer to open it.
In the Search field type in ntoskrnl.
Right click ntoskrnl and select Properties.
Click the Advanced button.
Next to TrustedInstaller, click the Change link.
In the text box type in Student, then click the Check Names button.
Click OK.
In the Advanced Security Settings for ntoskrnl window click OK.
In the ntoskrnl Properties window, click Edit.
Click Add.
In the text box type in Student and click Check Names.
Click OK.
In the Allow column, click the check box for Full Control.
Click OK.
In the Windows Security window click Yes.
Click OK.
Right click ntoskrnl file and click Delete.
Right click Recycle bin and select Empty Recycle Bin.
Click Yes to permanently delete the file.
Right click Start and select Shut down or sign out > Restart.
As the VM attempts to make automatic repairs move to the next section.

### Restoring Windows 11






**Backup a User Profile**

Double click the login screen so that the login prompt appears.

Select Student in the left corner of the screen.

Type Passw0rd in the box provided and press Enter.

Leave the VM in its current state and move on to the next section.

Minimize the connection window.

Click File Explorer in the taskbar of the Host.

In the left pane, click Hyper-V (E:).

In 