# 1- OS installations

## Task List


| Task                           |
|--------------------------------|
| Install Windows 11 From Install Media |
| Break Windows 11 Install       |
| Restore Windows 11             |
| Create an Extra Drive for Windows 11 |
| Manage New Drive               |
| Run a PC Health Check          |
| Configure Internet Access      |
| Driver Update                  |
| Create a New User Profile      |
| Login to New Account           |
| Backup a User Profile          |
| Delete a User Profile          |
| Restore a Profile from Backup  |
| Installing Ubuntu Linux        |






## Tasks to be Covered and Correlated Objectives


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

## Lab Steps

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



Manage New Hard Drive

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



Backup a User Profile

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


