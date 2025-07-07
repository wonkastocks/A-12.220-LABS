

## Task List


| Task                           |
|--------------------------------|
| Perform a Full System Backup   |
| Perform an Incremental Backup  |
| Perform a Differential Backup  |
| Schedule Automated Backups     |
| Restore Files from a Backup    |
| Restore a System to a Previous State |
| Test Backup Integrity          |
| Implement a Backup Rotation Scheme |
| Document a Backup Plan         |
| Simulate an Offsite Backup     |






## Task/Objective


| Task                           | Objective/Domain/Description                                      |
|--------------------------------|------------------------------------------------------------------|
| Perform a Full System Backup   | 1.0 Operating Systems                                             |
| Perform an Incremental Backup  | 4.0 Operational Procedures                                        |
| Perform a Differential Backup  | 1.0 Operating Systems                                             |
| Schedule Automated Backups     | 4.0 Operational Procedures                                        |
| Restore Files from a Backup    | 1.0 Operating Systems                                             |
| Restore a System to a Previous State | 1.0 Operating Systems                                      |
| Test Backup Integrity          | 4.0 Operational Procedures                                        |
| Implement a Backup Rotation Scheme | 1.0 Operating Systems                                        |
| Document a Backup Plan         | 1.0 Operating Systems                                             |
| Simulate an Offsite Backup     | 4.0 Operational Procedures                                        |

---


# Lab 17: Backup and Recovery

## Introduction

This hands-on lab provides comprehensive practice in implementing backup and recovery solutions—critical skills for IT professionals and CompTIA A+ certification candidates. Covering objectives from the 220-1202 exam, you'll develop proficiency in various backup methodologies, recovery procedures, and data protection strategies essential for maintaining business continuity and protecting against data loss in professional environments.

Through guided exercises, you'll master essential backup and recovery practices including full system backups, incremental and differential backup strategies, automated scheduling, file restoration procedures, system state recovery, backup integrity testing, rotation schemes, documentation procedures, and offsite backup simulation. These skills are fundamental for ensuring data availability, minimizing downtime, and implementing comprehensive disaster recovery strategies.

## Learning Objectives

By completing this lab, you will be able to:

### Backup Strategy Implementation
• Perform full system backups for comprehensive data protection
• Execute incremental and differential backup procedures
• Schedule automated backup operations for consistency
• Implement backup rotation schemes for long-term data retention

### Recovery and Restoration Procedures
• Restore individual files and folders from backup archives
• Recover entire systems to previous operational states
• Test backup integrity and verify restoration capabilities
• Document backup and recovery procedures for operational continuity

### Data Protection and Management
• Simulate offsite backup procedures for disaster recovery
• Implement backup testing and validation protocols
• Establish backup retention policies and compliance requirements
• Create comprehensive backup documentation and procedures

### Key Terms Covered in This Lab

| # | Key Term | Description |
|---|----------|-------------|
| 1 | Full Backup | Complete backup of all selected data regardless of previous backups |
| 2 | Incremental Backup | Backup of only data changed since the last backup of any type |
| 3 | Differential Backup | Backup of data changed since the last full backup |
| 4 | Synthetic Full Backup | Reconstructed full backup created from existing backup components |
| 5 | Backup Rotation | Systematic cycling of backup media to ensure data retention |
| 6 | Recovery Point Objective | Maximum acceptable data loss measured in time |
| 7 | Recovery Time Objective | Maximum acceptable downtime for system restoration |
| 8 | Grandfather-Father-Son | Traditional backup rotation scheme using three generations |
| 9 | 3-2-1 Backup Rule | Best practice requiring 3 copies, 2 different media, 1 offsite |
| 10 | Backup Integrity | Verification that backup data is complete and restorable |
| 11 | System State Backup | Backup of operating system configuration and system files |
| 12 | Bare Metal Recovery | Complete system restoration to new or reformatted hardware |

### Lab Task Overview

| Task | Description |
|------|-------------|
| Perform a Full System Backup | Create comprehensive backup of entire system |
| Perform an Incremental Backup | Execute backup of changed data since last backup |
| Perform a Differential Backup | Create backup of changes since last full backup |
| Schedule Automated Backups | Configure automatic backup operations |
| Restore Files from a Backup | Recover individual files and folders |
| Restore a System to a Previous State | Perform complete system recovery |
| Test Backup Integrity | Verify backup completeness and restoration capability |
| Implement a Backup Rotation Scheme | Establish systematic backup media cycling |
| Document a Backup Plan | Create comprehensive backup procedures |
| Simulate an Offsite Backup | Implement remote backup procedures |

### CompTIA A+ Objective Mapping

| Task Area | Exam Objective Reference |
|-----------|-------------------------|
| Full System Backup | 1.0 Operating Systems |
| Incremental Backup | 4.0 Operational Procedures |
| Differential Backup | 1.0 Operating Systems |
| Automated Scheduling | 4.0 Operational Procedures |
| File Restoration | 1.0 Operating Systems |
| System Recovery | 1.0 Operating Systems |
| Backup Testing | 4.0 Operational Procedures |
| Rotation Schemes | 1.0 Operating Systems |
| Documentation | 1.0 Operating Systems |
| Offsite Backup | 4.0 Operational Procedures |

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

Before you begin the hands-on tasks in this lab, you will gain practical experience implementing backup and recovery solutions that are critical for maintaining business continuity and data protection in professional environments. You will learn to create comprehensive backup strategies, test recovery procedures, and establish automated protection systems using real-world backup tools and methodologies. These skills are essential for preventing data loss, ensuring system availability, and meeting organizational compliance requirements. Mastery of these tasks directly aligns with CompTIA A+ exam objectives and prepares you for professional data protection responsibilities.

## Task 1: Perform a Full System Backup

### Objective: Create comprehensive backup of entire system

1. **Open** **Settings** and navigate to **Update & Security** > **Backup**

2. **Click** **Go to Backup and Restore (Windows 7)**

3. **Click** **Set up backup** to begin backup configuration

4. **Choose** backup destination (external drive or network location)

5. **Select** **Let me choose** for custom backup selection

6. **Check** all drives and system files for complete backup

7. **Ensure** **Include a system image** is selected

8. **Review** backup settings and click **Save settings and run backup**

9. **Monitor** backup progress and completion status

10. **Verify** backup completion and document backup size and duration

**Challenge Question:**
What type of backup includes all selected data regardless of previous backups?

**Answer:** Full

**Task Summary:**
You performed a comprehensive full system backup that creates a complete copy of all selected data and system configurations. Full backups provide the most comprehensive protection and serve as the foundation for backup strategies, enabling complete system recovery when necessary.

## Task 2: Perform an Incremental Backup

### Objective: Execute backup of changed data since last backup

1. **Create** some test files and modify existing documents

2. **Open** **Command Prompt** as Administrator

3. **Use** **Robocopy** for incremental backup: `robocopy C:\Users\Student D:\IncrementalBackup /MIR /XA:SH`

4. **Add** `/LOG:D:\BackupLog.txt` parameter for logging

5. **Run** the command and monitor file copying progress

6. **Make** additional file changes to test incremental functionality

7. **Run** the same command again to backup only changes

8. **Review** the log file to verify only changed files were copied

9. **Compare** backup duration with full backup time

10. **Document** incremental backup efficiency and space savings

**Challenge Question:**
What backup type only copies data changed since the last backup of any type?

**Answer:** Incremental

**Task Summary:**
You executed incremental backups that copy only data modified since the previous backup operation. Incremental backups provide efficient storage utilization and faster backup times while maintaining comprehensive data protection through cumulative backup sets.

## Task 3: Perform a Differential Backup

### Objective: Create backup of changes since last full backup

1. **Ensure** you have a baseline full backup from Task 1

2. **Create** and modify additional test files

3. **Use** **Robocopy** with archive bit checking for differential backup

4. **Run** `robocopy C:\Users\Student D:\DifferentialBackup /A /S`

5. **Note** that `/A` parameter copies files with archive bit set

6. **Make** more file changes after first differential backup

7. **Run** differential backup again without clearing archive bits

8. **Compare** file selection with incremental backup approach

9. **Verify** all changes since full backup are included

10. **Document** differential backup characteristics and restore requirements

**Challenge Question:**
What backup type includes all changes since the last full backup?

**Answer:** Differential

**Task Summary:**
You performed differential backups that capture all data changes since the last full backup. Differential backups balance storage efficiency with restoration simplicity, requiring only the full backup and latest differential backup for complete recovery.

## Task 4: Schedule Automated Backups

### Objective: Configure automatic backup operations

1. **Open** **Task Scheduler** from Administrative Tools

2. **Click** **Create Basic Task** in the Actions panel

3. **Name** the task "Daily System Backup"

4. **Set** trigger to **Daily** at a convenient time

5. **Select** **Start a program** as the action

6. **Browse** to backup program or create batch script

7. **Create** backup script: `backup_script.bat` with robocopy commands

8. **Configure** task to run with highest privileges

9. **Set** task to run whether user is logged in or not

10. **Test** scheduled task execution and verify backup operation

**Challenge Question:**
What Windows tool can automate recurring backup operations?

**Answer:** Scheduler

**Task Summary:**
You configured automated backup scheduling that ensures consistent data protection without manual intervention. Scheduled backups maintain regular protection cycles and reduce the risk of data loss due to forgotten manual backup procedures.

## Task 5: Restore Files from a Backup

### Objective: Recover individual files and folders

1. **Delete** or modify some test files to simulate data loss

2. **Open** **Backup and Restore (Windows 7)** from Control Panel

3. **Click** **Restore my files** to begin restoration process

4. **Browse** backup contents to locate deleted files

5. **Select** specific files or folders for restoration

6. **Choose** restoration location (original or alternative location)

7. **Click** **Restore** to begin file recovery process

8. **Verify** restored files match original content and attributes

9. **Test** restored file functionality and accessibility

10. **Document** restoration success and any issues encountered

**Challenge Question:**
What process recovers specific files from backup archives?

**Answer:** Restore

**Task Summary:**
You restored individual files and folders from backup archives to recover data after simulated loss. File restoration capabilities enable granular recovery of specific data without requiring full system restoration, minimizing downtime and maintaining productivity.

## Task 6: Restore a System to a Previous State

### Objective: Perform complete system recovery

1. **Create** a system restore point before making changes

2. **Open** **System Properties** > **System Protection**

3. **Click** **Create** to make a restore point named "Pre-Recovery Test"

4. **Make** system changes (install software, modify settings)

5. **Access** **System Restore** from **System Protection** tab

6. **Choose** the restore point created earlier

7. **Review** affected programs and click **Next**

8. **Confirm** restore operation and allow system restart

9. **Verify** system returns to previous configuration state

10. **Test** system functionality after restoration completion

**Challenge Question:**
What Windows feature can revert system configuration to previous state?

**Answer:** Restore

**Task Summary:**
You performed system state recovery that restored the entire system configuration to a previous point in time. System restoration provides comprehensive recovery from configuration errors, software conflicts, and system corruption while preserving user data.

## Task 7: Test Backup Integrity

### Objective: Verify backup completeness and restoration capability

1. **Navigate** to backup destination and examine backup files

2. **Check** backup file sizes and compare with original data

3. **Verify** backup completion logs for errors or warnings

4. **Perform** test restoration to temporary location

5. **Compare** restored files with original using checksum verification

6. **Use** `FC` command to compare file contents: `fc /B original.txt restored.txt`

7. **Test** backup accessibility and file structure integrity

8. **Verify** backup metadata and file attributes preservation

9. **Document** any integrity issues or restoration problems

10. **Create** backup validation checklist for regular testing

**Challenge Question:**
What process ensures backup data can be successfully restored?

**Answer:** Testing

**Task Summary:**
You tested backup integrity to ensure reliable data recovery capabilities. Regular backup testing verifies that backup procedures are working correctly and that recovery operations will succeed when needed, preventing costly surprises during actual recovery scenarios.

## Task 8: Implement a Backup Rotation Scheme

### Objective: Establish systematic backup media cycling

1. **Design** a Grandfather-Father-Son (GFS) rotation scheme

2. **Create** folder structure for Daily, Weekly, and Monthly backups

3. **Plan** retention periods: 7 daily, 4 weekly, 12 monthly backups

4. **Document** rotation schedule with specific backup dates

5. **Implement** rotation using batch scripts or backup software

6. **Create** backup script that automatically manages rotation

7. **Test** rotation by running multiple backup cycles

8. **Verify** old backups are archived according to schedule

9. **Monitor** storage usage and optimize retention periods

10. **Document** complete rotation procedures and schedules

**Challenge Question:**
What backup strategy systematically cycles backup media for long-term retention?

**Answer:** Rotation

**Task Summary:**
You implemented a backup rotation scheme that systematically manages backup retention and storage utilization. Rotation schemes ensure long-term data availability while controlling storage costs and maintaining compliance with retention requirements.

## Task 9: Document a Backup Plan

### Objective: Create comprehensive backup procedures

1. **Create** backup policy document including objectives and scope

2. **Document** Recovery Point Objective (RPO) and Recovery Time Objective (RTO)

3. **Define** backup types and scheduling for different data categories

4. **Specify** backup storage locations and retention periods

5. **Document** restoration procedures for various scenarios

6. **Include** emergency contact information and escalation procedures

7. **Create** backup verification and testing procedures

8. **Document** roles and responsibilities for backup operations

9. **Include** disaster recovery procedures and offsite storage

10. **Review** and validate documentation with testing scenarios

**Challenge Question:**
What document defines backup procedures and recovery objectives?

**Answer:** Plan

**Task Summary:**
You created comprehensive backup documentation that establishes procedures, responsibilities, and objectives for data protection operations. Backup documentation ensures consistent procedures, facilitates training, and enables effective disaster recovery when multiple personnel are involved.

## Task 10: Simulate an Offsite Backup

### Objective: Implement remote backup procedures

1. **Research** cloud storage options for offsite backup

2. **Configure** OneDrive or alternative cloud storage service

3. **Create** automated sync folder for critical backup files

4. **Test** cloud storage connectivity and upload speeds

5. **Simulate** local disaster by disconnecting from local backups

6. **Access** cloud-stored backups from alternative location

7. **Test** restoration from cloud storage to verify accessibility

8. **Calculate** recovery time objectives for cloud-based restoration

9. **Document** cloud backup procedures and limitations

10. **Verify** encryption and security for offsite storage

**Challenge Question:**
What backup location protects against local disasters?

**Answer:** Offsite

**Task Summary:**
You simulated offsite backup procedures that protect against local disasters and provide geographic data distribution. Offsite backups are essential for comprehensive disaster recovery and ensure data availability when local systems and storage are compromised.

## Discussion Questions

**Discussion Questions and Answers**

1. **How do different backup types (full, incremental, differential) balance storage efficiency with recovery complexity?**
**Answer:** Full backups provide the simplest recovery (single restore operation) but require the most storage space and time. Incremental backups are most storage-efficient and fastest to create but require the full backup plus all incremental backups for complete recovery, increasing complexity. Differential backups balance these factors by requiring only the full backup plus the latest differential backup for recovery, offering moderate storage efficiency with simplified restoration compared to incremental backups.

2. **What factors should organizations consider when establishing backup retention policies and rotation schemes?**
**Answer:** Key factors include regulatory compliance requirements, business operational needs, storage costs, recovery time objectives, data change rates, and disaster recovery requirements. Organizations must balance long-term data availability with storage costs while meeting legal retention requirements. The 3-2-1 backup rule (3 copies, 2 different media types, 1 offsite) provides a foundation, but specific retention periods should reflect business criticality, compliance obligations, and cost constraints.

3. **Why is regular backup testing crucial for effective disaster recovery, and what testing methods should be implemented?**
**Answer:** Backup testing verifies that backup procedures are working correctly and that data can be successfully restored when needed. Without testing, organizations may discover backup failures during actual emergencies when recovery is critical. Testing methods include regular restoration tests, integrity verification, recovery time measurement, and disaster recovery drills. Testing should cover various scenarios including individual file recovery, complete system restoration, and cross-platform recovery to ensure comprehensive preparation.

4. **How do Recovery Point Objective (RPO) and Recovery Time Objective (RTO) influence backup strategy design?**
**Answer:** RPO determines the maximum acceptable data loss and influences backup frequency - shorter RPOs require more frequent backups. RTO determines maximum acceptable downtime and influences backup technology choices and restoration procedures. For example, a 1-hour RPO might require continuous data replication, while a 24-hour RPO might allow nightly backups. Similarly, a 4-hour RTO might require high-speed restoration systems, while a 24-hour RTO might allow standard backup restoration procedures.

5. **What security considerations are important when implementing backup and recovery systems?**
**Answer:** Security considerations include backup encryption (in transit and at rest), access controls for backup media and systems, secure offsite storage, backup integrity verification, and audit trails for backup and restoration activities. Organizations must protect backup data from unauthorized access while ensuring authorized personnel can perform recovery operations. This includes managing encryption keys securely, implementing role-based access controls, and maintaining backup system security updates and monitoring.

## Summary

In this CompTIA A+ Lab 17, you gained comprehensive hands-on experience implementing backup and recovery solutions that are essential for maintaining business continuity and protecting organizational data assets. You learned to execute various backup strategies, test recovery procedures, establish automated protection systems, and create comprehensive documentation that ensures reliable data protection and disaster recovery capabilities.

The practical exercises in this lab covered the complete backup and recovery lifecycle, from initial backup strategy design through testing, validation, and documentation. You practiced implementing multiple backup types, rotation schemes, and recovery procedures that balance storage efficiency with restoration requirements. These skills are essential for IT professionals who must ensure data availability, minimize downtime, and protect against data loss in various disaster scenarios.

Understanding backup and recovery principles is critical for CompTIA A+ certification and professional IT operations roles. The hands-on experience with backup tools, testing procedures, and documentation provides immediately applicable knowledge for workplace scenarios where data protection directly impacts business operations and compliance requirements. These competencies demonstrate your ability to implement comprehensive data protection strategies that ensure organizational resilience and maintain operational continuity in the face of system failures, disasters, and security incidents.

## References

1. CompTIA. (2024). *CompTIA A+ Certification Exam Objectives (220-1202)*. CompTIA, Inc.

2. National Institute of Standards and Technology. (2020). *Guide for Developing Security Plans for Federal Information Systems* (NIST Special Publication 800-18, Revision 1).

3. Microsoft Corporation. (2024). *Windows Backup and Recovery Guide*. Microsoft Technical Documentation.

4. Meyers, M. (2024). *CompTIA A+ Certification All-in-One Exam Guide, Eleventh Edition* (11th ed.). McGraw-Hill Education.

5. National Institute of Standards and Technology. (2020). *Security and Privacy Controls for Information Systems and Organizations* (NIST Special Publication 800-53, Revision 5).

6. Disaster Recovery Institute International. (2023). *Professional Practices for Business Continuity Management*. DRI International Standards.

7. SANS Institute. (2023). *Backup and Recovery Essentials*. SANS Security Training.

8. Chapple, M., & Seidl, D. (2022). *CompTIA Security+ Study Guide: Exam SY0-601* (8th ed.). Sybex.

9. Stallings, W., & Brown, L. (2023). *Computer Security: Principles and Practice* (4th ed.). Pearson Education.

10. International Organization for Standardization. (2019). *ISO 22301:2019 Security and resilience — Business continuity management systems — Requirements*.
