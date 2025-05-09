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






**Backup a User Profile**

Double click the login screen so that the login prompt appears.

Select Student in the left corner of the screen.

Type Passw0rd in the box provided and press Enter.

Leave the VM in its current state and move on to the next section.

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

A window will appear. Click No, make the network that I am connected to a private network.

Close File Explorer

In the search bar type control panel, and select Control Panel from the search results.

Drop down the View by list and select Small icons.

Click on Backup and Restore (Windows 7)

Click Set up backup.

Click Save on a network...

Click Browse...

Expand SERVER22-HYPER-

Select Profiles and click OK.






**Delete a User Profile**

In the Username field type administrator

In the password field type P@ssw0rd

Click OK.

Click Next.

Select Let me choose and click Next.

Uncheck Student's Libraries.

Uncheck Include a system image...

Click Next.

Click Save settings and run backup.

Wait for the backup process to complete.

Once it is complete click control panel home and proceed to the next section.

In the All Control Panel Items window, click System.

Scroll down some and click the Advanced system settings link.

Under User Profiles click Settings.

Click the Student2 account and click Delete.






**Restore a User Profile from a Backup**

Click Yes to confirm deletion.

Close all windows except for Control Panel and proceed to the next section.

In the All Control Panel Items window, click Back up and Restore (Windows 7)

Click the Restore all users' files link.

Click Browse for folders.

In the left pane click Back up on \\SERVER22-HYPER-\Profiles.

In the right pane select Back up of C: and click Add folder.

Click Next.

Click Restore.

When the files have been restored click Finish.

Click Start

Click Student

Click the ellipsis (...)

Select Sign Out.

Close the VM window and proceed to the next exercise.






**Installing Ubuntu Linux**

Click Ubuntu Install on the topology map.

You will be presented with the Choose your language page. Click the Reboot button in the VM window toolbar.

Click OK to reboot the VM.

This process may take a few minutes, please be patient.

You will again be presented with the Choose your language page. Click Next.

On the Accessibility page click Next.

On the Select your keyboard layout page click Next.

On the Connect to the internet page, select Do not connect to the internet, and click Next.

On the What do you want to do with Ubuntu? page, click Next.

On the How would you like to install Ubuntu? page, click Next.

On the What apps would you like to start with? page, click Next.

On the Install proprietary software? page, click Next.

On the How do you want to install Ubuntu? page, click Next.

Enter the following information and click Next:

Your name: Student

Password: Passw0rd

Confirm Password: Passw0rd

In the timezone box type: New York then click Next.

Click Install.

Please wait while Ubuntu installs.

Once it is finished, click Restart Now.

If you get the message Please remove the install medium, and press ENTER:, just press enter to finish the reboot.

When presented with the login screen, click Student.

Enter the password of Passw0rd and press Enter.

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
