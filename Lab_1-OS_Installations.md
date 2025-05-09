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


**Install Windows 11 from Install Media**

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


**Break the Windows 11 Installation**

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


**Restoring Windows 11**

When Automatic Repair fails you will be presented with a blue screen.

Click Advanced options.

Click Troubleshoot.

Click Reset this PC.

Click Keep my files.

Click Local reinstall.

Click Reset.

While the reset is processing move on to the next section.


**Create an Extra Drive for Windows 11**

When the Reset operation completes you will be presented with the login screen.

Double click anywhere on that screen to make the login prompt appear.

Click the power button in the bottom right corner and select Shut Down.

Click Shut down anyway when asked.

When the VM has finished shutting down, click the File menu in the connection window and select Settings.

In the left pane select SCSI Controller.

Ensure Hard Drive is selected and click Add.

Drop down the Location box and select 3.

Ensure that Virtual hard disk is selected and click the New button.

Click the Next button three times.

In the Size box enter 20 and click Next.

Click Finish.

Click OK to close the Settings window.

Click the Start button to power on the VM again.

Click the Maximize button to make the connection window full screen.

Double click the login screen to make the prompt appear.

Enter Password in the password field and press Enter to login.

Leave the VM in this state and continue to the next section.


**Manage New Hard Drive**

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


**Run a PC Health Check**

In the search box, type health.

Select Device performance & health.

Examine the Health Report.

Leave the device in its current state and proceed to the next section.


**Configure Internet Access**

Right click Start and select Terminal (Admin).

Click Yes in the UAC window.

At the PowerShell prompt type: New-NetIPAddress -InterfaceAlias Ethernet -IPAddress 192.168.0.20 -PrefixLength 24 -DefaultGateway 192.168.0.250

Press Enter.

At the next prompt type: Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 1.1.1.1

Press Enter.

Close the Windows Terminal.


**Driver Update**

Right click Start and select Device Manager.

Expand Display Adapters.

Right click Microsoft Hyper-V Video and select Update Driver.

Click Search automatically for drivers.

Click Search for updated drivers on Windows Update.

Click Advanced options.

Click Optional updates.

Note that there are no updates available at this time.

Close the Settings app.

Close Device Manager.

Proceed to the next section.


**Create a New User Profile**

In the search bar type users and select Other Users.

Click Add Account.

Click I don't have this person's sign-in information.

Click Add a user without a Microsoft account.

In the User name box type in Student2.

In the 2 password boxes type Password.

For each of the security questions, drop down the list and select the first option that is not greyed out.

For each of the answers enter: ACI

Click Next.

Note that the new user Student2 is now created.

Close the Settings app and proceed to the next section.


**Log In to the New Account**

Right click Start and select Shut down or sign out > Sign out

Double click the login screen so that the login prompt appears.

Select Student2 in the left corner of the screen.

Type Password in the box provided and press Enter.

It will take a moment for the account profile to be created. Please wait.

In the Choose privacy settings for your device window, scroll to the bottom and click Accept.

Right click Start and select Shut down or sign out > Sign out

Double click the login screen so that the login prompt appears.

Select Student in the left corner of the screen.

Type Password in the box provided and press Enter.

Leave the VM in its current state and move on to the next section.


**Backup a User Profile**

Minimize the connection window.

Click File Explorer in the taskbar of the Host.

In the left pane, click Hyper-V (E:).

In the right pane, right click the empty space and select New > Folder.

Give the new folder the name of Profiles and press Enter.

Right click Profiles and select Properties.

Click the Sharing tab.

Click the Advanced Sharing button.

Check the Share this folder check box.

Click the Permissions button.

Check the check box for the Change permission in the Allow column.

Click OK.

Click OK.

Click Close.

Restore the Connection window.

Click the File Explorer icon in the taskbar.

Click Network in the left pane.

You will see a yellow notice appear. Click the notice to activate a menu.

Click Turn on network discovery and file sharing.

A window will appear.

Click No, make the network that I am connected to a private network.

Close File Explorer.

In the search bar type control panel, and select Control Panel from the search results.

Drop down the View by list and select Small icons.

Click on Backup and Restore (Windows 7).

Click Set up backup.

Click Save on a network...

Click Browse...

Expand SERVER22-HYPER-

Select Profiles and click OK.

In the Username field type administrator

In the password field type P@ssword

Click OK.

Click Next.

Select Let me choose and click Next.

Uncheck Student's Libraries.

Uncheck Include a system image...

Click Next.

Click Save settings and run backup.

Wait for the backup process to complete.

Once it is complete click control panel home and proceed to the next section.


**Delete a User Profile**

In the All Control Panel Items window, click System.

Scroll down some and click the Advanced system settings link.

Under User Profiles click Settings.

Click the Student2 account and click Delete.

Click Yes to confirm deletion.

Close all windows except for Control Panel and proceed to the next section.


**Restore a User Profile from a Backup**

In the All Control Panel Items window, click Backup and Restore (Windows 7).

Click the Restore all users' files link.

Click Browse for folders.
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
Break the Windows 11 Installation
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
Restoring Windows 11
When Automatic Repair fails you will be presented with a blue screen.    
Click Advanced options.    
Click Troubleshoot.    
Click Reset this PC.    
Click Keep my files.    
Click Local reinstall.    
Click Reset.    
While the reset is processing move on to the next section.    
Create an Extra Drive for Windows 11
When the Reset operation completes you will be presented with the login screen.    
Double click anywhere on that screen to make the login prompt appear.    
Click the power button in the bottom right corner and select Shut Down.    
Click Shut down anyway when asked.    
When the VM has finished shutting down, click the File menu in the connection window and select Settings.    
In the left pane select SCSI Controller.    
Ensure Hard Drive is selected and click Add.    
Drop down the Location box and select 3.    
Ensure that Virtual hard disk is selected and click the New button.    
Click the Next button three times.    
In the Size box enter 20 and click Next.    
Click Finish.    
Click OK to close the Settings window.    
Click the Start button to power on the VM again.    
Click the Maximize button to make the connection window full screen.    
Double click the login screen to make the prompt appear.    
Enter Password in the password field and press Enter to login.    
Leave the VM in this state and continue to the next section.    
Manage New Hard Drive
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
Run a PC Health Check
In the search box, type health.    
Select Device performance & health.    
Examine the Health Report.    
Leave the device in its current state and proceed to the next section.    
Configure Internet Access
Right click Start and select Terminal (Admin).    
Click Yes in the UAC window.    
At the PowerShell prompt type: New-NetIPAddress -InterfaceAlias Ethernet -IPAddress 192.168.0.20 -PrefixLength 24 -DefaultGateway 192.168.0.250    
Press Enter.    
At the next prompt type: Set-DnsClientServerAddress -InterfaceAlias Ethernet -ServerAddresses 1.1.1.1    
Press Enter.    
Close the Windows Terminal.    
Driver Update
Right click Start and select Device Manager.    
Expand Display Adapters.    
Right click Microsoft Hyper-V Video and select Update Driver.    
Click Search automatically for drivers.    
Click Search for updated drivers on Windows Update.    
Click Advanced options.    
Click Optional updates.    
Note that there are no updates available at this time.    
Close the Settings app.    
Close Device Manager.    
Proceed to the next section.    
Create a New User Profile
In the search bar type users and select Other Users.    
Click Add Account.    
Click I don't have this person's sign-in information.    
Click Add a user without a Microsoft account.    
In the User name box type in Student2.    
In the 2 password boxes type Password.    
For each of the security questions, drop down the list and select the first option that is not greyed out.    
For each of the answers enter: ACI    
Click Next.    
Note that the new user Student2 is now created.    
Close the Settings app and proceed to the next section.    
Log In to the New Account
Right click Start and select Shut down or sign out > Sign out    
Double click the login screen so that the login prompt appears.    
Select Student2 in the left corner of the screen.    
Type Password in the box provided and press Enter.    
It will take a moment for the account profile to be created. Please wait.    
In the Choose privacy settings for your device window, scroll to the bottom and click Accept.    
Right click Start and select Shut down or sign out > Sign out    
Double click the login screen so that the login prompt appears.    
Select Student in the left corner of the screen.    
Type Password in the box provided and press Enter.    
Leave the VM in its current state and move on to the next section.    
Backup a User Profile
Minimize the connection window.    
Click File Explorer in the taskbar of the Host.    
In the left pane, click Hyper-V (E:).    
In the right pane, right click the empty space and select New > Folder.    
Give the new folder the name of Profiles and press Enter.    
Right click Profiles and select Properties.    
Click the Sharing tab.    
Click the Advanced Sharing button.    
Check the Share this folder check box.    
Click the Permissions button.    
Check the check box for the Change permission in the Allow column.    
Click OK.    
Click OK.    
Click Close.    
Restore the Connection window.    
Click the File Explorer icon in the taskbar.    
Click Network in the left pane.    
You will see a yellow notice appear. Click the notice to activate a menu.    
Click Turn on network discovery and file sharing.    
A window will appear.    
Click No, make the network that I am connected to a private network.    
Close File Explorer.    
In the search bar type control panel, and select Control Panel from the search results.    
Drop down the View by list and select Small icons.    
Click on Backup and Restore (Windows 7).    
Click Set up backup.    
Click Save on a network...    
Click Browse...    
Expand SERVER22-HYPER-    
Select Profiles and click OK.    
In the Username field type administrator    
In the password field type P@ssword    
Click OK.    
Click Next.    
Select Let me choose and click Next.    
Uncheck Student's Libraries.    
Uncheck Include a system image...    
Click Next.    
Click Save settings and run backup.    
Wait for the backup process to complete.    
Once it is complete click control panel home and proceed to the next section.    
Delete a User Profile
Installing Ubuntu Linux
Click Ubuntu Install on the topology map.  
You will be presented with the Choose your language page. Click the Reboot button in the VM window toolbar.  
Click OK to reboot the VM.  
This process may take a few minutes, please be patient.  
{{ ... }}
On the Accessability page click Next.    
On the Select your keyboard layout page click Next.    
On the Connect to the internet page, select Do not connect to the internet, and click Next.    
On the What do you want to do with Ubuntu? page, click Next.    
On the How would you like to install Ubuntu? page, click Next.    
On the What apps would you like to start with? page, click Next.    
On the Install proprietary software? page, click Next.    
On the How do you want to install Ubuntu? page, click Next.    
Enter the following information and click Next:    
Your name: Student    
Password: Password    
Confirm Password: Password    
In the timezone box type: New York then click Next.    
Click Install.    
Please wait while Ubuntu installs.    
Once it is finished, click Restart Now.    
If you get the message Please remove the install medium, and press ENTER:, just press enter to finish the reboot.    
When presented with the login screen, click Student.    
Enter the password of Password and press Enter.    
Click Next three times then click Finish.    
Click the Power icon in the upper right corner.    
Click the gear icon to enter the Settings app.    
In the Network panel, under Wired click the gear icon to enter wired network configuration.    
Click the IPv4 tab.    
Select Manual.    
Enter 192.168.0.30 for the Address, 24 for the Netmask, and 192.168.0.250 for the Gateway.    
For DNS enter 1.1.1.1, and click Apply.    
Click the Show Apps button at the bottom left of the screen.    
Type terminal in the search box.    
Click on Terminal to open a terminal window.    
At the prompt type ping -c 4 cisco.com and press Enter.    
You should get success messages for all 4 pings.    
Close the VM window and click the Stop button to complete the lab.    







