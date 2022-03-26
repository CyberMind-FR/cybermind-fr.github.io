---
title: >-
  Microsoft 
  - Windows 7 
  - Permissions Fault after privilege's escalation
lang: en
date: 2012-03-02 00:00:00
tags:
- CyberSecurity
- Vulnerability
- By-Design
---
====== Permissions Fault after privilege's escalation ======
A "By Design" Reproductible Integrity Vulnerability.
Discovered on the 2th of march 2012.

<del>secure@microsoft.com</del>

===== Type of issue (buffer overflow, SQL injection, cross-site scripting, etc.) =====

Permissions Fault after privilege's escalation

===== Product and version that contains the bug =====

Windows 7 Entreprise x86

===== Service packs, security updates, or other updates for the product you have installed =====

Full updated on the 2012/02/04
  - Full (101) updates
  - French Language Pack
  - No browser choice made (closed)
  - No IE 9 (ask later)

===== Any special configuration required to reproduce the issue =====

Standard Windows 7 install with User(s) and administrator

===== Step-by-step instructions to reproduce the issue on a fresh install =====

  - Installation
    * Fresh default install from en_windows_7_enterprise_x86_dvd_x15
    * Full update 101 Updates
    * No browser choice made
    * No IE 9 (ask later)
  - Prepare environment
    * Login adminstrator's user
    * Create Standard Account User0
    * Create Standard Account User1
    * Login User0
    * Loggoff User0
    * Login User1
    * Logoff User1
    * Reboot
  - Reproducing issue
    * Login User0
    * Try to access User1's private folder in profile folder (c:\users\user1\Documents\)
    * UAC escalation (administrator's password needed)
    * folder's permissions for User0 have been added (full control) on the accessed folder (c:\users\user1\Documents\)
  - Proof of the issue
    * Reboot
    * Login User0
    * try to acces User1's folder (c:\users\user1\Documents\)
    * -> NO more UAC needed
    * create folder "Corrupted Permissions" in (c:\users\user1\Documents\)

===== Proof-of-concept or exploit code =====

Screenshots needed ? ;-)

===== Impact of the issue, including how an attacker could exploit the issue =====

After an administrator account has made UAC's ecalation of privileges to acces on a User1 folder while User0 logged, User0 will have a full access of the User1 folder accessed without the need of UAC's escalation.
May affect integrity of Users' files by another user(s).


May be some other side effects...


----
===== MSRC Mail Exchange =====

    Le 06/02/2012 18:20, Microsoft Security Response Center a écrit

Hello xxxxxx,

Thank you for reporting this behavior to us.  I was able to reproduce this behavior and can confirm that this is by design behavior to allow user0 access to user1’s content.  As the repro requires administrative credentials,  this does not hit the security bug bar due to the fact that this behavior is by design as the user is prompted as expected for administrative credentials.  Oonce someone has those credentials they can take any action that an administrator can including adding themselves as an administrator or adding themselves to any folder they wish.  

Best Regards,
xxxx

    Tuesday, February 14, 2012 7:44 AM

To: Microsoft Security Response Center
Subject: Re: Microsoft Security :: Coordinated Vulnerability Disclosure | Report a Vulnerability | MSRC

Hello xxxx,

I need a clarification, in the following step (I put the original message at bottom) :
- folder's permissions for User0 have been added (full control) on the accessed folder (c:\users\user1\Documents\)

You agree that it was done by UAC, in a transparent and persistent way.  With no other action than UAC privilege escalation.

It's a data user integrity issue than can cause another side effects as data disclosure...

Regards,

    14/02/2012 19:38 from Microsoft Security Response Center ====

Hello xxxxxx,

Thank you for your message.  The action occurring here is providing access for user0 to user1's folder by providing administrative credentials.  This is not a vulnerability and is not a privilege escalation.  When you grant user0 access to user1’s data, administrative credentials are required.  **When the administrator grants this access, it is permanent**.  This is the reason user0 can access user1’s data.

Best Regards,
xxxx
