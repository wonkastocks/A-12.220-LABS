**Note:** In a virtual environment, these labs are not possible. Where available, videos and reading assignments will be added.

Lab  Title	Practical/Theory	Domain	Objective	Lab VMs required	Videos
Operating system types, filesystems, lifecycle compatibility	Theory	Operating Systems	Explain common operating system types and their purposes 1.0	N/A	
Windows edition features and comparison	Theory	Operating Systems	Compare and contrast basic features of Microsoft Windows editions 1.2	N/A	
macOS and Linux desktop features and utilities	Theory	Operating Systems	Explain common features and tools of the macOS desktop operating system 1.7, 
Identify common features and tools of the Linux client/desktop operating system 1.8	N/A	
Application and cloud-service deployment	Theory	Operating Systems	Install applications according to requirements 1.9, 
Install and configure cloud-based productivity tools 1.10	N/A	


## Steps Taken

Operating System Installations and Upgrades
Introduction
Install Windows 11 from Install Media
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
Wireless security protocols and authentication	Theory	Security	Compare and contrast wireless security protocols and authentication methods 2.3	N/A	
Mobile-device security configuration	Theory	Security	Apply common methods for securing mobile devices 2.8	N/A	
Mobile OS and application troubleshooting	Theory	Software Troubleshooting	Troubleshoot common mobile OS and application issues 3.2	N/A	
Mobile security issue troubleshooting	Theory	Software Troubleshooting	Troubleshoot common mobile OS and application security issues 3.3	N/A	
Documentation and asset-management best practices	Theory	Operational Procedures	Implement best practices associated with documentation and support systems information management 4.1	N/A	
Change-management process implementation	Theory	Operational Procedures	Apply change-management procedures 4.2	N?A	
Safety procedures and environmental controls	Theory	Operational Procedures	Use common safety procedures 4.4, 
Summarize environmental impacts and local environment controls 4.5	N/A	
Policy, licensing, and privacy compliance	Theory	Operational Procedures	Explain the importance of prohibited content/activity and privacy, licensing, and policy concepts 4.6	N/A	
Communication skills and professionalism	Theory	Operational Procedures	Use proper communication techniques and professionalism 4.7	N/A	


