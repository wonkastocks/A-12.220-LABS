

## Task List


| Task                           |
|--------------------------------|
| Configure IP Addressing        |
| Configure DNS Settings         |
| Configure Windows Firewall Rules|
| Configure File and Printer Sharing|
| Map Network Drives             |
| Establish a VPN Connection     |
| Test Network Connectivity      |
| Configure Network Discovery    |
| Configure Proxy Settings       |
| Configure Network Locations    |






## Task/Objective


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Configure IP Addressing        | 4.0 Operational Procedures                                        |
| Configure DNS Settings         | 4.0 Operational Procedures                                        |
| Configure Windows Firewall Rules| 4.0 Operational Procedures                                       |
| Configure File and Printer Sharing| 4.0 Operational Procedures                                     |
| Map Network Drives             | 4.0 Operational Procedures                                        |
| Establish a VPN Connection     | 1.0 Operating Systems                                             |
| Test Network Connectivity      | 4.0 Operational Procedures                                        |
| Configure Network Discovery    | 4.0 Operational Procedures                                        |
| Configure Proxy Settings       | 4.0 Operational Procedures                                        |
| Configure Network Locations    | 4.0 Operational Procedures                                        |

---


# Lab 4: Windows Networking Configuration

## How to Use This Lab

1. Follow each task in sequence to complete the lab
2. Complete all verification steps for each task
3. Answer the challenge questions to test your understanding
4. Use the troubleshooting section if you encounter any issues

## Introduction

Welcome to this hands-on lab focused on Windows Networking Configuration. This lab provides practical experience in configuring and managing network settings in Windows, a critical skill for IT professionals and CompTIA A+ certification candidates. You'll develop proficiency in IP configuration, DNS settings, firewall rules, and network troubleshooting.

### Why This Lab Matters

Networking forms the foundation of modern IT infrastructure, and the ability to configure and troubleshoot network settings is fundamental to roles including:

- IT Support Specialist
- Network Administrator
- System Administrator
- Help Desk Technician
- Technical Support Engineer

### What You'll Learn

Through carefully designed exercises, you will:

- Configure and verify IP addressing
- Set up and test DNS configurations
- Create and manage Windows Firewall rules
- Configure file and printer sharing
- Map network drives and establish VPN connections
- Troubleshoot network connectivity issues

### Real-World Application

These skills apply to scenarios such as:

- Setting up office networks
- Troubleshooting connectivity issues
- Securing network communications
- Configuring remote access solutions
- Managing network resources

### Certification Alignment

This lab supports CompTIA A+ (220-1102) preparation, addressing key objectives in Domain 4.0 (Operational Procedures). The hands-on experience will help you pass certification exams while building practical skills.

### Lab Scenario

You are an IT support specialist at a medium-sized company. The network administrator has asked you to configure the network settings on several Windows workstations. Your tasks include setting up IP addressing, configuring DNS, setting up file sharing, and ensuring secure network communications.

## Learning Objectives

This lab is designed to help you develop practical Windows networking skills that align with CompTIA A+ objectives. By completing these exercises, you will build competence in network configuration and troubleshooting that is directly applicable to real-world IT support scenarios.

### Task-Specific Objectives

1. **Configure IP Addressing**
   - Understand IPv4 addressing
   - Configure static IP addresses
   - Verify IP configuration

2. **Configure DNS Settings**
   - Configure DNS server addresses
   - Test DNS resolution
   - Flush and manage DNS cache

3. **Configure Windows Firewall Rules**
   - Create inbound and outbound rules
   - Configure rule properties
   - Test firewall configurations

4. **Configure File and Printer Sharing**
   - Set up file sharing
   - Configure sharing permissions
   - Access shared resources

5. **Map Network Drives**
   - Map drives using different methods
   - Configure persistent connections
   - Troubleshoot mapping issues

6. **Establish a VPN Connection**
   - Configure VPN settings
   - Connect to a VPN server
   - Troubleshoot VPN connectivity

7. **Test Network Connectivity**
   - Use network diagnostic tools
   - Interpret test results
   - Troubleshoot connectivity issues

8. **Configure Network Discovery**
   - Enable/disable network discovery
   - Configure network profiles
   - Troubleshoot discovery issues

9. **Configure Proxy Settings**
   - Configure manual and automatic proxy settings
   - Test proxy configurations
   - Troubleshoot proxy issues

10. **Configure Network Locations**
    - Understand network location types
    - Configure location settings
    - Troubleshoot location-based issues

### Expected Outcomes

Upon successful completion of this lab, you will be able to:

1. Configure and verify IP addressing on Windows systems
2. Set up and test DNS configurations
3. Create and manage Windows Firewall rules
4. Configure and troubleshoot file and printer sharing
5. Map network drives and establish VPN connections
6. Use network diagnostic tools to test and troubleshoot connectivity
7. Configure network discovery and proxy settings
8. Manage network locations and profiles

### Key Terms and Concepts

| Term | Definition |
|------|------------|
| **IP Address** | A unique identifier assigned to each device on a network (e.g., 192.168.1.1) |
| **Subnet Mask** | Defines which part of an IP address is the network portion (e.g., 255.255.255.0) |
| **Default Gateway** | The device that routes traffic between different networks (typically a router) |
| **DNS** | Domain Name System, translates domain names to IP addresses |
| **Firewall** | Security system that monitors and controls network traffic based on predetermined rules |
| **VPN** | Virtual Private Network, creates a secure encrypted connection over the internet |
| **Network Share** | A shared resource on a network, such as files or printers |
| **Network Drive** | A drive letter mapped to a network share for easy access |
| **Proxy Server** | An intermediary server that forwards requests between clients and other servers |
| **Network Profile** | A collection of network and sharing settings (Public, Private, or Domain) |
| **DHCP** | Dynamic Host Configuration Protocol, automatically assigns IP addresses to devices |
| **NAT** | Network Address Translation, allows multiple devices to share a single public IP |
| **Port** | A virtual point for network communications (e.g., 80 for HTTP, 443 for HTTPS) |
| **Latency** | The time it takes for data to travel from source to destination |
| **Bandwidth** | The maximum rate of data transfer across a network path |

### Lab Task Overview

| Task | Description |
|------|-------------|
| Configure IP Addressing | Set up and verify IP configuration |
| Configure DNS Settings | Configure and test DNS resolution |
| Configure Windows Firewall Rules | Create and manage firewall rules |
| Configure File and Printer Sharing | Set up and test file sharing |
| Map Network Drives | Map and verify network drives |
| Establish a VPN Connection | Configure and test VPN connectivity |
| Test Network Connectivity | Use tools to test and verify network connections |
| Configure Network Discovery | Manage network discovery settings |
| Configure Proxy Settings | Set up and test proxy configurations |
| Configure Network Locations | Manage network location settings |

### CompTIA A+ Objective Mapping

| Task Area | Exam Objective Reference | Domain |
|-----------|--------------------------|--------|
| IP Addressing | 4.1 | Operational Procedures |
| DNS Settings | 4.1 | Operational Procedures |
| Windows Firewall | 4.1 | Operational Procedures |
| File and Printer Sharing | 4.1 | Operational Procedures |
| Network Drives | 4.1 | Operational Procedures |
| VPN Connection | 1.9 | Operating Systems |
| Network Testing | 4.1 | Operational Procedures |
| Network Discovery | 4.1 | Operational Procedures |
| Proxy Settings | 4.1 | Operational Procedures |
| Network Locations | 4.1 | Operational Procedures |

## Systems/Software Required

- Windows 10 or 11 System with Administrator Privileges
- Router Access
- Network Connection
- VPN Server
- Test system to connect to

## Required Tools/Resources

- Command Prompt (for network commands)
- Windows Settings app
- Windows Defender Firewall
- Network and Sharing Center
- VPN configuration details (if applicable)
- Network share details (for file sharing tasks)

---

## Getting Started

Before beginning the hands-on tasks, follow these steps to access your virtual lab environment:

1. **Click** the **Start** button in your lab portal to provision the lab environment.
2. **Click** the computer image or "Launch VM" button in the right pane when the lab loads to open the Windows virtual machine window.
3. **Wait** for Windows 11 to finish booting. When you see the lock screen, **double-click** anywhere to reveal the login prompt.
4. **Select** the **Student** account (if prompted).
5. **Login** with the password `P@ssw0rd` (case sensitive).
6. Once logged in, you are ready to begin the lab activities below.

If you encounter any issues starting the lab or logging in, notify your instructor for assistance.

---

## Task 1: Configure IP Addressing

### Objective
Configure and verify static IP addressing on a Windows computer.

### Prerequisites
- [ ] Administrative privileges on the computer
- [ ] Knowledge of your network's IP addressing scheme
- [ ] Available IP address to use

### Instructions

#### Part 1: Access Network Adapter Settings
1. **Open Network Connections**
   - Press `Win + R`, type `ncpa.cpl`, and press **Enter**
   - **Expected Result**: Network Connections window opens showing available adapters

2. **Configure IPv4 Settings**
   - Right-click your active network adapter and select **Properties**
   - Double-click **Internet Protocol Version 4 (TCP/IPv4)**
   - Select **Use the following IP address**
   - Enter the following:
     - IP address: 192.168.1.100
     - Subnet mask: 255.255.255.0
     - Default gateway: 192.168.1.1
   - Click **OK** to save settings
   - **Troubleshooting**: If you can't save settings, ensure you have administrator privileges

#### Part 2: Verify IP Configuration
1. **Open Command Prompt**
   - Press `Win + X` and select **Windows Terminal (Admin)** or **Command Prompt (Admin)**
   - Type `ipconfig /all` and press Enter
   - **Verify**: Check that your IP configuration matches what you set

2. **Test Network Connectivity**
   - In Command Prompt, type `ping 8.8.8.8`
   - **Expected Result**: You should see replies from the Google DNS server
   - **Troubleshooting**: If pings fail, check your physical connection and IP settings

### Verification
- [ ] IP address is set to 192.168.1.100
- [ ] Subnet mask is 255.255.255.0
- [ ] Default gateway is 192.168.1.1
- [ ] Can ping 8.8.8.8 successfully

**Challenge Question:** 
What protocol automatically assigns IP addresses to devices?  
Answer: DHCP

**Task Summary:**
In this task, you learned how to configure and verify static IP addressing on a Windows computer. This is essential for network troubleshooting and ensuring consistent network configuration across devices. Static IP addressing is commonly used for servers, network devices, and other systems that require a consistent network identity.

---

## Task 2: Configure DNS Settings

### Objective
Configure and test DNS server settings on a Windows computer.

### Instructions

1. **Open Network Connections**
   - Press `Win + R`, type `ncpa.cpl`, and press **Enter**
   - **Expected Result**: Network Connections window opens

2. **Configure DNS Servers**
   - Right-click your active network adapter and select **Properties**
   - Double-click **Internet Protocol Version 4 (TCP/IPv4)**
   - Select **Use the following DNS server addresses**
   - Enter the following:
     - Preferred DNS server: 8.8.8.8
     - Alternate DNS server: 8.8.4.4
   - Click **OK** to save settings

3. **Flush DNS Cache**
   - Open Command Prompt as Administrator
   - Type the following commands, pressing Enter after each:
     ```
     ipconfig /flushdns
     ipconfig /registerdns
     ```
   - **Expected Result**: Success messages for each command

4. **Test DNS Resolution**
   - In Command Prompt, type `nslookup google.com`
   - **Verify**: You should see Google's IP addresses listed
   - **Troubleshooting**: If resolution fails, check your DNS server addresses and network connectivity

### Verification
- [ ] DNS server addresses are configured correctly
- [ ] DNS cache was successfully flushed
- [ ] Can resolve domain names (e.g., google.com)
- [ ] nslookup returns expected IP addresses

**Challenge Question:**  
What does DNS stand for?  
Answer: Domain Name System

**Task Summary:**
In this task, you configured and tested DNS settings, which are crucial for translating human-readable domain names into IP addresses. Proper DNS configuration ensures reliable internet connectivity and access to network resources. This skill is fundamental for troubleshooting network connectivity issues and maintaining efficient name resolution.

---

## Task 3: Configure Windows Firewall Rules

### Objective
Create and manage Windows Firewall rules to control network traffic.

### Instructions

1. **Open Windows Defender Firewall**
   - Press `Win + R`, type `wf.msc`, and press **Enter**
   - **Expected Result**: Windows Defender Firewall with Advanced Security opens

2. **Create a New Inbound Rule**
   - In the left pane, right-click **Inbound Rules** and select **New Rule**
   - Select **Port** and click **Next**
   - Choose **TCP** and enter port `8080`
   - Select **Allow the connection** and click **Next**
   - Select all profiles (Domain, Private, Public)
   - Name the rule `Test HTTP Port 8080`
   - Click **Finish**

3. **Verify the Rule**
   - In the Inbound Rules list, locate your new rule
   - Right-click the rule and select **Properties** to review settings
   - **Troubleshooting**: If rule isn't listed, ensure you have administrator privileges

### Verification
- [ ] New inbound rule for TCP port 8080 is created
- [ ] Rule is enabled and properly configured
- [ ] Rule appears in the Inbound Rules list

**Challenge Question:**  
What is the default port number for HTTP traffic?  
Answer: 80

**Task Summary:**
In this task, you learned how to create and manage Windows Firewall rules, which are essential for controlling network traffic and securing your system. Firewall rules help protect your computer from unauthorized access while allowing legitimate network communication. This skill is critical for implementing network security policies and troubleshooting connectivity issues.

---

## Task 4: Configure File and Printer Sharing

### Objective
Set up and test file sharing on a Windows computer.

### Instructions

1. **Enable File and Printer Sharing**
   - Open **Settings** > **Network & Internet** > **Ethernet**
   - Click **Network and Sharing Center**
   - Click **Change advanced sharing settings**
   - Under **Private** network profile, enable:
     - Turn on network discovery
     - Turn on file and printer sharing
   - Click **Save changes**

2. **Share a Test Folder**
   - Create a new folder named `TestShare` on your desktop
   - Right-click the folder and select **Properties**
   - Go to the **Sharing** tab and click **Share...**
   - Type `Everyone` and click **Add**
   - Set Permission Level to **Read/Write**
   - Click **Share** and then **Done**

3. **Verify the Share**
   - Open File Explorer and type `\\localhost` in the address bar
   - **Verify**: You should see your TestShare folder listed

### Verification
- [ ] File and printer sharing is enabled
- [ ] TestShare folder is created and shared
- [ ] Share is accessible via network path

**Challenge Question:**  
What protocol is commonly used for file sharing on Windows networks?  
Answer: SMB

**Task Summary:**
In this task, you configured file and printer sharing, enabling resource sharing across a network. This is a fundamental skill for network administrators and support technicians who need to set up shared resources in a business environment. Proper configuration ensures that users can access the files and printers they need while maintaining appropriate security controls.

---

## Task 5: Map Network Drives

### Objective
Map a network drive to a shared folder.

### Instructions

1. **Map the Drive**
   - Open **File Explorer**
   - Right-click **This PC** and select **Map network drive**
   - Choose an available drive letter (e.g., Z:)
   - Enter the path: `\\localhost\TestShare`
   - Check **Reconnect at sign-in**
   - Click **Finish**

2. **Test the Mapped Drive**
   - In File Explorer, navigate to **This PC**
   - **Verify**: The mapped drive (Z:) should appear under Network locations
   - Create a test file in the mapped drive to verify write access

### Verification
- [ ] Network drive is mapped successfully
- [ ] Drive appears in File Explorer
- [ ] Can create and modify files in the mapped drive

**Challenge Question:**  
What command can map a network drive from the command line?  
Answer: net use

**Task Summary:**
In this task, you learned how to map network drives, which provides users with easy access to shared network resources. Mapped drives appear as local drives in File Explorer, simplifying file access and improving productivity. This skill is essential for IT professionals who need to configure workstations with access to shared network resources.

---

## Task 6: Establish a VPN Connection

### Objective
Configure and test a VPN connection in Windows.

### Instructions

1. **Set Up VPN**
   - Open **Settings** > **Network & Internet** > **VPN**
   - Click **Add a VPN connection**
   - Configure with these settings:
     - VPN provider: Windows (built-in)
     - Connection name: `Test VPN`
     - Server name: `vpn.example.com` (or provided test server)
     - VPN type: Automatic
     - Type of sign-in info: Username and password
   - Click **Save**

2. **Connect to VPN**
   - In the VPN settings, click on the **Test VPN** connection
   - Click **Connect**
   - When prompted, enter test credentials (if applicable)
   - **Troubleshooting**: Verify server address and credentials if connection fails

### Verification
- [ ] VPN connection is created
- [ ] Can successfully connect to the VPN
- [ ] Network connectivity is maintained after connection

**Challenge Question:**  
What does VPN stand for?  
Answer: Virtual Private Network

**Task Summary:**
In this task, you configured and tested a VPN connection, which is essential for secure remote access to network resources. VPNs encrypt network traffic, protecting sensitive data when using untrusted networks. This skill is increasingly important in today's distributed work environments where employees need secure access to company resources from various locations.

---

## Task 7: Test Network Connectivity

### Objective
Use network diagnostic tools to test and troubleshoot connectivity.

### Instructions

1. **Basic Connectivity Tests**
   - Open Command Prompt as Administrator
   - Run the following commands and record results:
     - `ping 8.8.8.8`
     - `tracert google.com`
     - `netstat -an | find "ESTABLISHED"`

2. **Advanced Testing**
   - Run `pathping google.com` and analyze results
   - Use `Test-NetConnection` in PowerShell to test specific ports
   - **Troubleshooting**: Note any timeouts or errors in the results

### Verification
- [ ] All test commands complete successfully
- [ ] Can interpret the results of each test
- [ ] Can identify potential network issues from test results

**Challenge Question:**  
What command shows the path packets take to reach a destination?  
Answer: tracert

**Task Summary:**
In this task, you used various network diagnostic tools to test and troubleshoot connectivity. These tools are essential for identifying and resolving network issues in both home and enterprise environments. The ability to interpret the results of these tests is a fundamental skill for network administrators and support technicians.

---

## Task 8: Configure Network Discovery

### Objective
Configure network discovery settings in Windows.

### Instructions

1. **Access Advanced Sharing Settings**
   - Open **Settings** > **Network & Internet** > **Network and Sharing Center**
   - Click **Change advanced sharing settings**

2. **Configure Network Discovery**
   - Under **Private** network profile:
     - Turn on network discovery
     - Turn on automatic setup of network connected devices
   - Under **Guest or Public** network profile:
     - Turn off network discovery
   - Click **Save changes**

3. **Verify Settings**
   - Open File Explorer and navigate to **Network**
   - **Verify**: You should see other devices on the network (if any)

### Verification
- [ ] Network discovery is configured correctly
- [ ] Can see other network devices (if available)
- [ ] Settings are saved successfully

**Challenge Question:**  
What network profile is most secure: Public or Private?  
Answer: Public

**Task Summary:**
In this task, you configured network discovery settings, which control how your computer interacts with other devices on the network. Proper configuration of these settings is important for both functionality and security. Network discovery is typically enabled on private networks to facilitate resource sharing while being disabled on public networks for security.

---

## Task 9: Configure Proxy Settings

### Objective
Configure and test proxy settings in Windows.

### Instructions

1. **Access Proxy Settings**
   - Open **Settings** > **Network & Internet** > **Proxy**
   - Under **Manual proxy setup**, toggle **Use a proxy server** to **On**
   - Enter the following test proxy settings:
     - Address: `proxy.example.com`
     - Port: `8080`
   - Click **Save**

2. **Test Proxy Connection**
   - Open a web browser and attempt to visit a website
   - **Troubleshooting**: If connection fails, verify proxy settings and network connectivity

3. **Disable Proxy**
   - Return to Proxy settings
   - Toggle **Use a proxy server** to **Off**
   - Click **Save**

### Verification
- [ ] Proxy settings are configured correctly
- [ ] Can verify proxy behavior (if test proxy is available)
- [ ] Can successfully disable proxy when done

**Challenge Question:**  
What is the purpose of a proxy server?  
Answer: Filtering

**Task Summary:**
In this task, you learned how to configure proxy settings in Windows. Proxy servers can provide various functions including content filtering, improved performance through caching, and enhanced privacy. Understanding how to configure and troubleshoot proxy settings is important for network administrators and support technicians working in environments that use proxy servers.

---

## Task 10: Configure Network Locations

### Objective
Configure and manage network location types in Windows.

### Instructions

1. **View Current Network Profile**
   - Open **Settings** > **Network & Internet** > **Status**
   - Click **Properties** under your active network
   - Note the current network profile (Private, Public, or Domain)

2. **Change Network Profile**
   - Under **Network profile**, select a different profile (e.g., change from Public to Private)
   - **Note**: You may need administrator privileges
   - **Troubleshooting**: If option is grayed out, check group policy settings

3. **Verify Firewall Rules**
   - Open Windows Defender Firewall
   - Note how different rules are enabled/disabled based on profile

### Verification
- [ ] Can view current network profile
- [ ] Can change between network profiles (with appropriate permissions)
- [ ] Can observe different firewall behaviors based on profile

**Challenge Question:**  
Which network profile has the most restrictive firewall rules?  
Answer: Public

**Task Summary:**
In this task, you learned about Windows network location profiles and how they affect system behavior. Network profiles (Public, Private, Domain) determine which firewall rules and sharing settings are applied. Understanding these profiles is essential for properly securing Windows systems in different network environments and troubleshooting connectivity issues.

---

## Discussion Questions

1. **What are the main differences between static and dynamic IP addressing, and when would you use each?**
   **Answer:** Static IP addressing manually assigns a fixed IP address to a device, while dynamic IP addressing automatically assigns addresses from a pool. Use static IPs for servers, printers, and network devices that need consistent addressing. Use dynamic IP addressing (DHCP) for general workstations and devices where IP consistency isn't critical, as it simplifies network management and reduces configuration errors.

2. **How does DNS resolution work, and what could cause DNS resolution to fail?**
   **Answer:** DNS resolution translates domain names to IP addresses through a hierarchical system of DNS servers. It can fail due to incorrect DNS server settings, network connectivity issues, DNS server outages, firewall blocking DNS traffic, or problems with the local DNS cache. Troubleshooting steps include checking network connectivity, verifying DNS server settings, flushing the DNS cache, and testing with alternative DNS servers.

3. **What are the security implications of enabling file and printer sharing on a network?**
   **Answer:** Enabling file and printer sharing can expose sensitive data if not properly secured. Risks include unauthorized access to shared resources, potential malware spread, and data breaches. To mitigate these risks, always use strong authentication, implement proper share and NTFS permissions, enable encryption for sensitive data, use firewalls to restrict access, and regularly audit shared resources and access logs.

4. **How would you troubleshoot a situation where a user can access network resources by IP address but not by hostname?**
   **Answer:** This typically indicates a DNS resolution issue. I would: 1) Verify network connectivity with `ping` to both IP and hostname, 2) Check DNS server configuration with `ipconfig /all`, 3) Test DNS resolution with `nslookup` or `ping hostname`, 4) Flush the DNS cache with `ipconfig /flushdns`, 5) Verify the DNS suffix settings, 6) Check the local hosts file for incorrect entries, and 7) Test with alternative DNS servers if available.

5. **What are the advantages of using a VPN for remote access, and what security considerations should be taken into account when setting one up?**
   **Answer:** VPNs provide secure, encrypted connections over public networks, allowing secure remote access to company resources. Advantages include data encryption, secure authentication, and the ability to access resources as if on the local network. Security considerations include: using strong encryption protocols (like IKEv2 or OpenVPN), implementing multi-factor authentication, regularly updating VPN software, configuring proper access controls, monitoring for unusual activity, and ensuring endpoint security measures are in place on all devices that connect to the VPN.

## Troubleshooting

If you encounter issues during the lab, try these general troubleshooting steps:

1. **Network Connectivity Issues**
   - Verify physical connections (cables, Wi-Fi)
   - Check if other devices can connect to the network
   - Restart your router/modem
   - Disable and re-enable the network adapter

2. **IP Configuration Problems**
   - Run `ipconfig /release` followed by `ipconfig /renew`
   - Verify IP settings match your network requirements
   - Check for IP address conflicts

3. **DNS Resolution Failures**
   - Try using alternative DNS servers (e.g., 8.8.8.8, 1.1.1.1)
   - Flush DNS cache with `ipconfig /flushdns`
   - Check hosts file for incorrect entries

4. **Firewall Issues**
   - Temporarily disable Windows Firewall to test if it's blocking connections
   - Check Windows Firewall logs for blocked connections
   - Verify that required ports are open

5. **File Sharing Problems**
   - Verify Network Discovery is turned on
   - Check sharing permissions and NTFS permissions
   - Ensure the File and Printer Sharing exception is enabled in Windows Firewall

## Command Summary

| Command | Description | Example |
|---------|-------------|---------|
| `ipconfig` | Display IP configuration | `ipconfig /all` |
| `ping` | Test network connectivity | `ping 8.8.8.8` |
| `tracert` | Trace route to a destination | `tracert google.com` |
| `nslookup` | Query DNS for name resolution | `nslookup example.com` |
| `netstat` | Display network statistics | `netstat -an` |
| `netsh` | Configure network interfaces | `netsh interface show interface` |
| `pathping` | Combine ping and traceroute functionality | `pathping google.com` |
| `Test-NetConnection` | PowerShell cmdlet for network diagnostics | `Test-NetConnection -ComputerName google.com -Port 80` |
| `Get-NetIPConfiguration` | Get IP configuration details | `Get-NetIPConfiguration` |
| `ipconfig /flushdns` | Clear the DNS resolver cache | `ipconfig /flushdns` |
| `ipconfig /release` | Release the current IP configuration | `ipconfig /release` |
| `ipconfig /renew` | Renew the IP configuration | `ipconfig /renew` |
| `net use` | Map network drives | `net use Z: \\server\share` |
| `net view` | View network resources | `net view \\computername` |
| `Get-NetConnectionProfile` | View network profiles | `Get-NetConnectionProfile` |
| `Set-NetConnectionProfile` | Change network profile | `Set-NetConnectionProfile -InterfaceIndex 12 -NetworkCategory Private` |

**Usage Notes:**
- Replace placeholders in the Example column with actual values
- Run commands in an elevated Command Prompt or PowerShell when administrative privileges are required
- Use `/?` or `-?` after any command for help and syntax information

## Lab Summary

This comprehensive lab provided hands-on experience with essential Windows networking concepts and configurations. Throughout these exercises, you gained practical skills in configuring and managing network settings in a Windows environment, which are fundamental for IT professionals working with modern networked systems.

You began by configuring IP addressing, learning how to set up both static and dynamic IP configurations, and verifying network connectivity. This foundational knowledge is crucial for troubleshooting network issues and ensuring proper communication between devices on a network. The DNS configuration exercises enhanced your understanding of name resolution, including how to configure DNS server settings and troubleshoot resolution problems using tools like nslookup and ipconfig.

The Windows Firewall exercises developed your ability to create and manage inbound and outbound rules, an essential skill for securing systems while maintaining necessary network functionality. You also gained experience with file and printer sharing, learning how to configure permissions and access shared resources across a network. The network drive mapping exercises provided practical experience in creating persistent connections to network resources, improving efficiency in daily operations.

Your work with VPN connections gave you insight into secure remote access solutions, including configuration and troubleshooting techniques. The network discovery exercises helped you understand how to control device visibility and resource sharing in different network environments. Additionally, you explored proxy server configurations, learning how to set up and test both manual and automatic proxy settings for different network scenarios.

Throughout the lab, you utilized various network diagnostic tools including ping, tracert, netstat, and pathping, developing your ability to identify and resolve network connectivity issues. These troubleshooting skills are invaluable in real-world IT support scenarios where quick and accurate problem-solving is essential.

By completing these exercises, you've built a strong foundation in Windows networking that will serve you well in various IT roles, from help desk support to network administration. The hands-on experience with these tools and concepts will help you approach networking challenges with confidence and competence.

## References

American National Standards Institute. (2021). *Information technology - Telecommunications and information exchange between systems - Local and metropolitan area networks - Specific requirements - Part 3: Standard for Ethernet*. ANSI/IEEE Std 802.3-2021.

Comer, D. E. (2018). *Computer networks and internets* (6th ed.). Pearson.

Comptia. (2022). *CompTIA A+ Certification All-in-One Exam Guide, Eleventh Edition (Exams 220-1101 & 220-1102)*. McGraw Hill.

Microsoft. (2023). *Networking fundamentals for Windows*. Microsoft Learn. https://learn.microsoft.com/en-us/windows-server/networking/

Microsoft. (2023). *Windows 10 and Windows 11 networking documentation*. Microsoft Docs. https://docs.microsoft.com/en-us/windows/network/

National Institute of Standards and Technology. (2020). *Guidelines on firewalls and firewall policy* (NIST Special Publication 800-41, Rev. 2). U.S. Department of Commerce. https://csrc.nist.gov/publications/detail/sp/800-41/rev-2/final

Odom, W. (2020). *CCNA 200-301 Official Cert Guide, Volume 1* (1st ed.). Cisco Press.

Stallings, W. (2021). *Data and computer communications* (11th ed.). Pearson.

Tanenbaum, A. S., & Wetherall, D. J. (2021). *Computer networks* (6th ed.). Pearson.

Zeltser, L. (2021). *Network protocols handbook* (2nd ed.). SecurityCraft.
