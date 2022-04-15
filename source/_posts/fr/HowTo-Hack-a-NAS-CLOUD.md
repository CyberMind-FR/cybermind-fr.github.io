---
title: HowTo Hack a NAS CLOUD
lang: fr
date: 2014-09-24 00:00:00
tags: 
- ARM
- Aramada
- NAS
- CLOUD
- SECUBOX
categories: Cyber
---
====== HowTo Hack a NAS CLOUD ======


Je viens d'acquérir un nouveau boitier NAS.
Le IcyBox IB-NAS6220-B

200 € chez LDLC : http://www.ldlc.com/fiche/PB00109232.html

Son gros avantage, qui m'a fait le choisir, est que le CPU est un Kirkwood de Marvell.
Le même processeur que les SheevaPlug et GuruPlug.

Ce choix est donc ciblé pour le "hack".
<!-- more -->

Premières impressions :
  * silencieux,
  * joli,
  * facile à monter

L'ajout des disques se fait sans vis ; une clé permet de dévérouiller les emplacements SATA 3"1/2 qui se démontent simplement par un appuie sur le rack.
Les vis de fixation des disques sont remplacées par des ergots métalliques.

Une fois les 2 x 2To en place, le branchement sur le réseau et l'allumage :
Silence, le ventilateur est très silencieux, et le boitier NAS est resté quelques heures dans le salon sans que personne ne le remarque.
Si ce n'est les diodes colorées qui font guirlande de Noël lors de la construction du RAID.

L'interface web est jolie elle aussi.
Les possibilités ont l'air sympathiques, mais c'est là que commencent les désagréments :
le navigateur de fichiers intégré me propose d'installer un " google truk " !!!

C'est décidé, je vais le "hacker".

J'hésite entre le démontage, les sheevaplugs ont tous des accès jtag pour le développement.
Il me reste cette solution facile ! ;-)

Je tombe sur un forum allemand : nas-portal.org et surtout un fil sur le sujet 6220 :
http://forum.nas-portal.org/showthread.php?12855-Ib-nas6220-b/

:wiki:notes:nashack:datasheet_ib-nas6220_e.pdf|

:wiki:notes:nashack:111a.jpg.jpeg|

:wiki:notes:nashack:111b.jpg.jpeg|

:wiki:notes:nashack:111c.jpg.jpeg|

:wiki:notes:nashack:111d.jpg.jpeg|

L'accès en web au NAS permet une escalade de privilège root assez simple !
C'est effrayant comme certain produit sont mal sécurisé...

:wiki:notes:nashack:capture00.png|

:wiki:notes:nashack:capture00-1.png|

Après l'authentification en admin / admin par le web, il suffit de modifier l'url dans la barre d'adresse.

:wiki:notes:nashack:capture00-2.png|


En remplaçant admin par root, on se retouve authentifié avec l'utilisateur root.

:wiki:notes:nashack:capture00-4.png|

:wiki:notes:nashack:capture00-3.png|

:wiki:notes:nashack:capture00-5.png|



Il suffit de changer le mot de passe et l'accès ssh en root sera alors possible.

:wiki:notes:nashack:capture00-6.png|

:wiki:notes:nashack:capture00-7.png|

:wiki:notes:nashack:capture00-8.png|

:wiki:notes:nashack:capture00-9.png|



Pour la saisie de l'ancien mot de passe, autre faille de sécurité, il n'est pas vérifié :
on saisie n'importe quoi en old password, puis son mot de passe dédié NASHACK

la porte est ouverte, et ce n'est pas une "backdoor" mais la grande porte !
nautilus en ssh

:wiki:notes:nashack:capture00-11.png|

:wiki:notes:nashack:capture00-fenetresansnom.png|


:wiki:notes:nashack:capture00-12.png|

et l'accès ssh terminal ( en root ) :


    ssh root@jshare.local


:wiki:notes:nashack:capture00-10.png|

<code>
    gek@astree:/$ ssh root@jshare.local
    The authenticity of host 'jshare.local (192.168.0.116)' can't be established.
    RSA key fingerprint is bc:66:86:a9:84:7f:ae:ad:aa:62:5b:24:b8:7d:af:1b.
    Are you sure you want to continue connecting (yes/no)? yes
    Warning: Permanently added 'jshare.local,192.168.0.116' (RSA) to the list of known hosts.
    root@jshare.local's password:
    Last login: Sun Sep 25 21:39:41 2011 from 192.168.0.111
    [root@JSHARE ~]# uname -ar
    Linux JSHARE 2.6.35.4 #1 PREEMPT Sun Sep 19 09:18:57 CST 2010 armv5tel armv5tel armv5tel GNU/Linux
    [root@JSHARE ~]# cat /etc/system-release
    Fedora release 12 (Constantine)
    [root@JSHARE ~]# whoami     
    root
    [root@JSHARE ~]# cat /proc/cpuinfo
    Processor   : Feroceon 88FR131 rev 1 (v5l)
    BogoMIPS   : 1196.03
    Features   : swp half thumb fastmult edsp
    CPU implementer   : 0x56
    CPU architecture: 5TE
    CPU variant   : 0x2
    CPU part   : 0x131
    CPU revision   : 1

    Hardware   : Marvell DB-88F6281-BP Development Board
    Revision   : 0000
    Serial      : 0000000000000000
    [root@JSHARE ~]#
</code>


Et ce n'est pas fini... :siffle:

Je commence par faire une analyse...
Où suis-je ?

$ uname -a


<code>
    Linux JSHARE 2.6.35.4 #1 PREEMPT Sun Sep 19 09:18:57 CST 2010 armv5tel armv5tel armv5tel GNU/Linux
</code>


$ cat /proc/cmdline


<code>
    console=ttyS0,115200 ubi.mtd=2,2048 root=ubi0:rootfs rootfstype=ubifs init=/linuxrc
</code>


$ cat /proc/cpuinfo


<code>
    Processor   : Feroceon 88FR131 rev 1 (v5l)
    BogoMIPS   : 1196.03
    Features   : swp half thumb fastmult edsp
    CPU implementer   : 0x56
    CPU architecture: 5TE
    CPU variant   : 0x2
    CPU part   : 0x131
    CPU revision   : 1

    Hardware   : Marvell DB-88F6281-BP Development Board
    Revision   : 0000
    Serial      : 0000000000000000
</code>


$ dmesg


<code>
    Linux version 2.6.35.4 (thom@11z) (gcc version 4.5.1 (GCC) ) #1 PREEMPT Sun Sep 19 09:18:57 CST 2010
    CPU: Feroceon 88FR131 [56251311] revision 1 (ARMv5TE), cr=00053177
    CPU: VIVT data cache, VIVT instruction cache
    Machine: Marvell DB-88F6281-BP Development Board
    Ignoring unrecognised tag 0x41000403
    Memory policy: ECC disabled, Data cache writeback
    On node 0 totalpages: 65536
    free_area_init_node: node 0, pgdat c04cc008, node_mem_map c056a000
      Normal zone: 512 pages used for memmap
      Normal zone: 0 pages reserved
      Normal zone: 65024 pages, LIFO batch:15
    Built 1 zonelists in Zone order, mobility grouping on.  Total pages: 65024
    Kernel command line: console=ttyS0,115200 ubi.mtd=2,2048 root=ubi0:rootfs rootfstype=ubifs init=/linuxrc
    PID hash table entries: 1024 (order: 0, 4096 bytes)
    Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)
    Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)
    Memory: 256MB = 256MB total
    Memory: 254360k/254360k available, 7784k reserved, 0K highmem
    Virtual kernel memory layout:
        vector  : 0xffff0000 - 0xffff1000   (   4 kB)
        fixmap  : 0xfff00000 - 0xfffe0000   ( 896 kB)
        DMA     : 0xffc00000 - 0xffe00000   (   2 MB)
        vmalloc : 0xd0800000 - 0xfe800000   ( 736 MB)
        lowmem  : 0xc0000000 - 0xd0000000   ( 256 MB)
        modules : 0xbf000000 - 0xc0000000   (  16 MB)
          .init : 0xc0008000 - 0xc002b000   ( 140 kB)
          .text : 0xc002b000 - 0xc0480000   (4436 kB)
          .data : 0xc049e000 - 0xc04cd3e0   ( 189 kB)
    SLUB: Genslabs=11, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, Nodes=1
    Hierarchical RCU implementation.
       RCU-based detection of stalled CPUs is disabled.
       Verbose stalled-CPUs detection is disabled.
    NR_IRQS:114
    Console: colour dummy device 80x30
    Calibrating delay loop... 1196.03 BogoMIPS (lpj=5980160)
    pid_max: default: 32768 minimum: 301
    Mount-cache hash table entries: 512
    CPU: Testing write buffer coherency: ok
    NET: Registered protocol family 16
    Kirkwood: MV88F6281-A1, TCLK=200000000.
    Feroceon L2: Enabling L2
    Feroceon L2: Cache support initialised.
    initial MPP regs: 21111111 00003311 00551111 00000000 00000000 00000000 00000000
      final MPP regs: 21111111 00003311 00551111 00000000 00000000 00000000 00000000
    pci 0000:00:00.0: reg 10: [mem 0xf1000000-0xf10fffff 64bit pref]
    pci 0000:00:00.0: reg 18: [mem 0x00000000-0x0fffffff]
    pci 0000:00:00.0: supports D1 D2
    PCI: bus0: Fast back to back transfers disabled
    bio: create slab <bio-0> at 0
    vgaarb: loaded
    SCSI subsystem initialized
    libata version 3.00 loaded.
    usbcore: registered new interface driver usbfs
    usbcore: registered new interface driver hub
    usbcore: registered new device driver usb
    cfg80211: Calling CRDA to update world regulatory domain
    Switching to clocksource orion_clocksource
    NET: Registered protocol family 2
    IP route cache hash table entries: 2048 (order: 1, 8192 bytes)
    TCP established hash table entries: 8192 (order: 4, 65536 bytes)
    TCP bind hash table entries: 8192 (order: 3, 32768 bytes)
    TCP: Hash tables configured (established 8192 bind 8192)
    TCP reno registered
    UDP hash table entries: 256 (order: 0, 4096 bytes)
    UDP-Lite hash table entries: 256 (order: 0, 4096 bytes)
    NET: Registered protocol family 1
    RPC: Registered udp transport module.
    RPC: Registered tcp transport module.
    RPC: Registered tcp NFSv4.1 backchannel transport module.
    PCI: CLS 32 bytes, default 32
    JFFS2 version 2.2. (NAND) © 2001-2006 Red Hat, Inc.
    msgmni has been set to 496
    alg: No test for stdrng (krng)
    io scheduler noop registered
    io scheduler deadline registered
    io scheduler cfq registered (default)
    Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled
    serial8250.0: ttyS0 at MMIO 0xf1012000 (irq = 33) is a 16550A
    console [ttyS0] enabled
    loop: module loaded
    sata_mv sata_mv.0: version 1.28
    sata_mv sata_mv.0: slots 32 ports 2
    scsi0 : sata_mv
    scsi1 : sata_mv
    ata1: SATA max UDMA/133 irq 21
    ata2: SATA max UDMA/133 irq 21
    NAND device: Manufacturer ID: 0xec, Chip ID: 0xda (Samsung NAND 256MiB 3,3V 8-bit)
    Scanning device for bad blocks
    Bad eraseblock 74 at 0x000000940000
    Bad eraseblock 417 at 0x000003420000
    Bad eraseblock 651 at 0x000005160000
    Bad eraseblock 814 at 0x0000065c0000
    Bad eraseblock 1240 at 0x000009b00000
    Bad eraseblock 1710 at 0x00000d5c0000
    Bad eraseblock 1825 at 0x00000e420000
    Creating 3 MTD partitions on "orion_nand":
    0x000000000000-0x000000100000 : "u-boot"
    0x000000100000-0x000000700000 : "uImage"
    0x000000700000-0x000010000000 : "root"
    UBI: attaching mtd2 to ubi0
    UBI: physical eraseblock size:   131072 bytes (128 KiB)
    UBI: logical eraseblock size:    126976 bytes
    UBI: smallest flash I/O unit:    2048
    UBI: sub-page size:              512
    UBI: VID header offset:          2048 (aligned 2048)
    UBI: data offset:                4096
    UBI warning: ubi_eba_init_scan: cannot reserve enough PEBs for bad PEB handling, reserved 7, need 19
    UBI: attached mtd2 to ubi0
    UBI: MTD device name:            "root"
    UBI: MTD device size:            249 MiB
    UBI: number of good PEBs:        1985
    UBI: number of bad PEBs:         7
    UBI: max. allowed volumes:       128
    UBI: wear-leveling threshold:    4096
    UBI: number of internal volumes: 1
    UBI: number of user volumes:     1
    UBI: available PEBs:             0
    UBI: total number of reserved PEBs: 1985
    UBI: number of PEBs reserved for bad PEB handling: 7
    UBI: max/mean erase counter: 1/0
    UBI: image sequence number: 504793264
    ata1: SATA link up 3.0 Gbps (SStatus 123 SControl F300)
    UBI: background thread "ubi_bgt0d" started, PID 438
    MV-643xx 10/100/1000 ethernet driver version 1.4
    mv643xx_eth smi: probed
    ata1.00: ATA-8: SAMSUNG HD204UI, 1AQ10001, max UDMA/133
    ata1.00: 3907029168 sectors, multi 0: LBA48 NCQ (depth 31/32)
    net eth0: port 0 with MAC address 00:01:d2:0e:26:44
    libertas_sdio: Libertas SDIO driver
    libertas_sdio: Copyright Pierre Ossman
    ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
    orion-ehci orion-ehci.0: Marvell Orion EHCI
    orion-ehci orion-ehci.0: new USB bus registered, assigned bus number 1
    ata1.00: configured for UDMA/133
    scsi 0:0:0:0: Direct-Access     ATA      SAMSUNG HD204UI  1AQ1 PQ: 0 ANSI: 5
    sd 0:0:0:0: [sda] 3907029168 512-byte logical blocks: (2.00 TB/1.81 TiB)
    orion-ehci orion-ehci.0: irq 19, io mem 0xf1050000
    sd 0:0:0:0: [sda] Write Protect is off
    sd 0:0:0:0: [sda] Mode Sense: 00 3a 00 00
    sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
    orion-ehci orion-ehci.0: USB 2.0 started, EHCI 1.00
    sda:
    hub 1-0:1.0: USB hub found
    hub 1-0:1.0: 1 port detected
    sda1 sda2
    Initializing USB Mass Storage driver...
    usbcore: registered new interface driver usb-storage
    USB Mass Storage support registered.
    sd 0:0:0:0: [sda] Attached SCSI disk
    usbcore: registered new interface driver ums-datafab
    usbcore: registered new interface driver ums-freecom
    usbcore: registered new interface driver ums-jumpshot
    usbcore: registered new interface driver ums-sddr09
    usbcore: registered new interface driver ums-sddr55
    mice: PS/2 mouse device common for all mice
    input: gpio-keys as /devices/platform/gpio-keys/input/input0
    rtc-mv rtc-mv: rtc core: registered rtc-mv as rtc0
    i2c /dev entries driver
    md: linear personality registered for level -1
    md: raid0 personality registered for level 0
    md: raid1 personality registered for level 1
    cpuidle: using governor ladder
    cpuidle: using governor menu
    mmc0: mvsdio driver initialized, using GPIO 38 for card detection
    Registered led device: error
    Registered led device: system
    Registered led device: usbcopy
    MV-CESA:Fallback driver 'sha1' could not be loaded!
    alg: hash: Failed to load transform for mv-sha1: -2
    MV-CESA:Fallback driver 'hmac(sha1)' could not be loaded!
    alg: hash: Failed to load transform for mv-hmac-sha1: -2
    mv_xor_shared mv_xor_shared.0: Marvell shared XOR driver
    mv_xor_shared mv_xor_shared.1: Marvell shared XOR driver
    mv_xor mv_xor.0: Marvell XOR: ( xor cpy )
    mv_xor mv_xor.1: Marvell XOR: ( xor fill cpy )
    mv_xor mv_xor.2: Marvell XOR: ( xor cpy )
    mv_xor mv_xor.3: Marvell XOR: ( xor fill cpy )
    usbcore: registered new interface driver usbhid
    usbhid: USB HID core driver
    oprofile: hardware counters not available
    oprofile: using timer interrupt.
    TCP cubic registered
    NET: Registered protocol family 17
    lib80211: common routines for IEEE802.11 drivers
    lib80211_crypt: registered algorithm 'NULL'
    Gating clock of unused units
    before: 0x00c7c1dd
    after: 0x00c7c1dd
    rtc-mv rtc-mv: setting system clock to 2011-09-25 20:09:31 UTC (1316981371)
    usb 1-1: new high speed USB device using orion-ehci and address 2
    ata2: SATA link up 3.0 Gbps (SStatus 123 SControl F300)
    hub 1-1:1.0: USB hub found
    hub 1-1:1.0: 4 ports detected
    ata2.00: ATA-8: SAMSUNG HD204UI, 1AQ10001, max UDMA/133
    ata2.00: 3907029168 sectors, multi 0: LBA48 NCQ (depth 31/32)
    ata2.00: configured for UDMA/133
    scsi 1:0:0:0: Direct-Access     ATA      SAMSUNG HD204UI  1AQ1 PQ: 0 ANSI: 5
    sd 1:0:0:0: [sdb] 3907029168 512-byte logical blocks: (2.00 TB/1.81 TiB)
    sd 1:0:0:0: [sdb] Write Protect is off
    sd 1:0:0:0: [sdb] Mode Sense: 00 3a 00 00
    sd 1:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
    sdb: sdb1 sdb2
    sd 1:0:0:0: [sdb] Attached SCSI disk
    md: Waiting for all devices to be available before autodetect
    md: If you don't use raid, use raid=noautodetect
    md: Autodetecting RAID arrays.
    md: Scanned 2 and added 2 devices.
    md: autorun ...
    md: considering sdb1 ...
    md:  adding sdb1 ...
    md:  adding sda1 ...
    md: created md1
    md: bind<sda1>
    md: bind<sdb1>
    md: running: <sdb1><sda1>
    md/raid1:md1: active with 2 out of 2 mirrors
    md1: detected capacity change from 0 to 1999861579776
    md: ... autorun DONE.
    UBIFS: mounted UBI device 0, volume 0, name "rootfs"
    UBIFS: file system size:   248999936 bytes (243164 KiB, 237 MiB, 1961 LEBs)
    UBIFS: journal size:       9023488 bytes (8812 KiB, 8 MiB, 72 LEBs)
    UBIFS: media format:       w4/r0 (latest is w4/r0)
    UBIFS: default compressor: lzo
    UBIFS: reserved for root:  0 bytes (0 KiB)
    VFS: Mounted root (ubifs filesystem) on device 0:13.
    Freeing init memory: 140K
    Failed to execute /linuxrc.  Attempting defaults...
    md1: detected capacity change from 0 to 1999861579776
    md1: unknown partition table
    sd 0:0:0:0: Attached scsi generic sg0 type 0
    sd 1:0:0:0: Attached scsi generic sg1 type 0
    md1: detected capacity change from 0 to 1999861579776
    md1: unknown partition table
    uncorrectable error :
    uncorrectable error :
    end_request: I/O error, dev mtdblock0, sector 0
    EXT4-fs (md1): mounted filesystem with ordered data mode. Opts: (null)
    Adding 522108k swap on /dev/sda2.  Priority:-1 extents:1 across:522108k
    Adding 522108k swap on /dev/sdb2.  Priority:-2 extents:1 across:522108k
    NET: Registered protocol family 10
    ADDRCONF(NETDEV_UP): eth0: link is not ready
    eth0: link up, 1000 Mb/s, full duplex, flow control disabled
    ADDRCONF(NETDEV_CHANGE): eth0: link becomes ready
    tun: Universal TUN/TAP device driver, 1.6
    tun: (C) 1999-2004 Max Krasnyansky <maxk@qualcomm.com>
    eth0: no IPv6 routers present
</code>


$ cat /etc/system-release


<code>
    Fedora release 12 (Constantine)
</code>


$ free -m


<code>
                 total       used       free     shared    buffers     cached
    Mem:           248        245          2          0          0        197
    -/+ buffers/cache:         47        201
    Swap:         1019          0       1019
</code>


$ cat /etc/fstab

<code>
    ubi0    /               ubifs   defaults        1 1
    devpts  /dev/pts        devpts  gid=5,mode=620  0 0
    shm     /dev/shm        tmpfs   rw,nosuid,nodev 0 0
    proc    /proc           proc    defaults        0 0
    sysfs   /sys            sysfs   defaults        0 0
    none   /var/tmp   tmpfs   defaults   0 0
    sunrpc  /var/lib/nfs/rpc_pipefs rpc_pipefs      defaults 0 0
    # mount data partition to /home
    /dev/sda2 none swap defaults 0 0
    /dev/sdb2 none swap defaults 0 0
    /dev/md1 /home ext4 relatime 0 0
</code>


$ history

<code>
        1  tr -d /etc/nas/
        2  tr
        3  tr --help
        4  file tr
        5  help tr
        6  type tr
        7  exit
        8  tr
        9  exit
       10  nas-tr -d conf
       11  nas-tr -d /etc/nas/
       12  ls
       13  #nas-tr -d /etc/nas/
       14  ls
       15  nas-tr -d /etc/nas/
       16  ls
       17  ls -l
       18  exit
       19  sleep 3
       20  grep $(ip addr show eth0 | grep -i ether | cut -d ' ' -f 6 | tr -d ':') /etc/nas/device && echo No need to register || rm /etc/nas/device; /usr/bin/nas-register
       21  sleep 2
       22  ifconfig
       23  hwclock --systohc
       24  fdisk -l
       25  hwclock
       26  exit
</code>


$ cat /etc/issue

<code>
    Fedora release 12 (Constantine)
    Kernel \r on an \m (\l)
</code>


$ mount

<code>
    ubi0 on / type ubifs (rw)
    proc on /proc type proc (rw)
    sysfs on /sys type sysfs (rw)
    devpts on /dev/pts type devpts (rw,gid=5,mode=620)
    shm on /dev/shm type tmpfs (rw,nosuid,nodev)
    none on /var/tmp type tmpfs (rw)
    sunrpc on /var/lib/nfs/rpc_pipefs type rpc_pipefs (rw)
    /dev/md1 on /home type ext4 (rw,relatime)
</code>


$ ps aux

<code>
    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.3   1956   820 ?        Ss   20:09   0:01 /sbin/init
    root         2  0.0  0.0      0     0 ?        S    20:09   0:00 [kthreadd]
    root         3  0.0  0.0      0     0 ?        S    20:09   0:00 [ksoftirqd/0]
    root         4  0.0  0.0      0     0 ?        S    20:09   0:00 [watchdog/0]
    root         5  0.0  0.0      0     0 ?        S    20:09   0:00 [events/0]
    root         6  0.0  0.0      0     0 ?        S    20:09   0:00 [khelper]
    root         9  0.0  0.0      0     0 ?        S    20:09   0:00 [async/mgr]
    root       149  0.0  0.0      0     0 ?        S    20:09   0:00 [sync_supers]
    root       151  0.0  0.0      0     0 ?        S    20:09   0:00 [bdi-default]
    root       153  0.0  0.0      0     0 ?        S    20:09   0:00 [kblockd/0]
    root       159  0.0  0.0      0     0 ?        S    20:09   0:00 [ata_aux]
    root       160  0.0  0.0      0     0 ?        S    20:09   0:00 [ata_sff/0]
    root       168  0.0  0.0      0     0 ?        S    20:09   0:00 [khubd]
    root       171  0.0  0.0      0     0 ?        S    20:09   0:00 [kseriod]
    root       174  0.0  0.0      0     0 ?        S    20:09   0:00 [kmmcd]
    root       184  0.0  0.0      0     0 ?        S    20:09   0:00 [cfg80211]
    root       266  0.0  0.0      0     0 ?        S    20:09   0:00 [rpciod/0]
    root       274  0.0  0.0      0     0 ?        S    20:09   0:00 [khungtaskd]
    root       275  0.0  0.0      0     0 ?        S    20:09   0:00 [kswapd0]
    root       322  0.0  0.0      0     0 ?        S    20:09   0:00 [aio/0]
    root       329  0.0  0.0      0     0 ?        S    20:09   0:00 [nfsiod]
    root       335  0.0  0.0      0     0 ?        S    20:09   0:00 [crypto/0]
    root       402  0.0  0.0      0     0 ?        S    20:09   0:00 [scsi_eh_0]
    root       406  0.0  0.0      0     0 ?        S    20:09   0:00 [scsi_eh_1]
    root       420  0.0  0.0      0     0 ?        S    20:09   0:00 [mtdblock0]
    root       425  0.0  0.0      0     0 ?        S    20:09   0:00 [mtdblock1]
    root       430  0.0  0.0      0     0 ?        S    20:09   0:00 [mtdblock2]
    root       438  0.0  0.0      0     0 ?        S    20:09   0:00 [ubi_bgt0d]
    root       439  0.0  0.0      0     0 ?        S    20:09   0:00 [orion_spi]
    root       503  0.0  0.0      0     0 ?        S    20:09   0:00 [mv_crypto]
    root       549  0.0  0.0      0     0 ?        S    20:09   0:00 [usbhid_resumer]
    root       575  0.0  0.0      0     0 ?        S    20:09   0:00 [md1_raid1]
    root       578  0.0  0.0      0     0 ?        S    20:09   0:00 [ubifs_bgt0_0]
    root       658  0.0  0.2   2316   752 ?        S<s  20:09   0:00 /sbin/udevd -d
    root       843  0.0  0.3   2312   792 ?        S<   20:09   0:00 /sbin/udevd -d
    root       877  0.0  0.0      0     0 ?        S    20:09   0:00 [jbd2/md1-8]
    root       878  0.0  0.0      0     0 ?        S    20:09   0:00 [ext4-dio-unwrit]
    root      1163  0.0  0.2   2584   576 ?        Ss   20:09   0:00 /sbin/dhclient -1 -q -lf /var/lib/dhclient/dhclient-eth0.leases -pf /var/run/dhclient-eth0.pid eth0
    root      1219  0.0  0.4  29580  1240 ?        Sl   20:09   0:00 /sbin/rsyslogd -c 4
    rpc       1229  0.0  0.3   2512   780 ?        Ss   20:09   0:00 rpcbind
    root      1248  0.0  0.3   2512  1008 ?        Ss   20:09   0:00 rpc.statd
    root      1277  0.0  0.2   3644   520 ?        Ss   20:09   0:00 rpc.idmapd
    dbus      1288  0.0  0.3   2912   780 ?        Ss   20:09   0:00 dbus-daemon --system
    avahi     1298  0.0  0.5   3188  1492 ?        S    20:09   0:00 avahi-daemon: running [JSHARE.local]
    avahi     1299  0.0  0.1   3188   496 ?        Ss   20:09   0:00 avahi-daemon: chroot helper
    root      1318  0.0  1.4   7580  3700 ?        Ss   20:09   0:00 /usr/sbin/openvpn --daemon --writepid /var/run/openvpn/client.pid --config client.conf --cd /etc/openvpn --script-security 2
    root      1327  0.0  1.0  11512  2664 ?        Ss   20:09   0:00 cupsd -C /etc/cups/cupsd.conf
    root      1387  0.0  4.6  72376 11784 ?        Sl   20:09   0:02 python /usr/bin/nas-fastcgi
    root      1405  0.0  2.4  21208  6300 ?        S    20:09   0:00 python /usr/bin/nas-inotify
    root      1410  0.0  1.7  15488  4360 ?        S    20:09   0:00 python /usr/bin/nas-buttons
    root      1423  0.1  1.9  25200  4960 ?        Sl   20:09   0:11 python /usr/bin/nas-diskmon
    root      1448  0.1  1.5  22504  3828 ?        Sl   20:09   0:12 python /usr/bin/nas-logrota
    root      1466  0.0  0.4   7964  1052 ?        Ss   20:09   0:00 /usr/sbin/sshd
    root      1503  0.0  0.2   5728   552 ?        Ss   20:09   0:00 /usr/sbin/vsftpd /etc/vsftpd/vsftpd.conf
    lighttpd  1514  0.0  0.6   7520  1632 ?        S    20:09   0:00 /usr/sbin/lighttpd -f /etc/nas/lighttpd.conf
    root      1527  0.0  1.1  19552  2948 ?        Ss   20:10   0:00 smbd -D
    root      1540  0.0  0.1   2328   428 ?        Ss   20:10   0:00 /usr/sbin/atd
    root      1543  0.0  0.5  19552  1280 ?        S    20:10   0:00 smbd -D
    root      1546  0.0  0.5   2896  1464 ?        S    20:10   0:00 /usr/bin/nas-tr -d /etc/nas
    root      1584  0.0  0.3   2312   792 ?        S<   20:10   0:00 /sbin/udevd -d
    root      1614  0.0  0.2   3900   524 ?        S    20:10   0:00 /usr/sbin/smartd -q never
    root      1622  0.0  0.2   1808   524 tty4     Ss+  20:10   0:00 /sbin/mingetty tty4
    root      1623  0.0  0.2   1808   524 tty5     Ss+  20:10   0:00 /sbin/mingetty tty5
    root      1624  0.0  0.2   1808   524 tty2     Ss+  20:10   0:00 /sbin/mingetty tty2
    root      1625  0.0  0.2   1808   524 tty3     Ss+  20:10   0:00 /sbin/mingetty tty3
    root      1626  0.0  0.2   1808   524 tty1     Ss+  20:10   0:00 /sbin/mingetty tty1
    root      1627  0.0  0.2   1808   524 tty6     Ss+  20:10   0:00 /sbin/mingetty tty6
    root      1634  0.0  0.2   1820   576 ttyS0    Ss+  20:10   0:00 /sbin/agetty /dev/ttyS0 115200 vt100-nav
    root      1657  0.0  0.0      0     0 ?        S    21:34   0:00 [flush-9:1]
    root      1662  0.0  1.1  11352  2836 ?        Ss   21:39   0:00 sshd: root@pts/0
    root      1673  0.0  0.6   4368  1560 pts/0    Ss   21:39   0:00 -bash
    root      1840  0.0  0.0      0     0 ?        S    21:57   0:00 [flush-ubifs_0_0]
    root      1860  0.0  0.3   4048   940 pts/0    R+   22:05   0:00 ps aux
</code>

Pièces jointes

    config.gz
        (12.43 Kio) Aucun téléchargement

le dmesg me donne une information importante :

<code>
    Creating 3 MTD partitions on "orion_nand":
    0x000000000000-0x000000100000 : "u-boot"
    0x000000100000-0x000000700000 : "uImage"
    0x000000700000-0x000010000000 : "root"
</code>


je commende par créer un répertoire de travail dans le dossier HOME de admin.

je fait une sauvegarde complète du NAS :

Uboot :

<code>
    $ dd if=/dev/mdt0 of=u-boot.bin
</code>


Kernel Linux :

<code>
    $ dd if=/dev/mdt1 of=uImage.bin
</code>


RootFS UBI Fedora :

<code>
    $ dd if=/dev/mdt2 of=rootfs_ubi.bin
</code>    
    
    Il faut maintenant savoir comment est configuré l'uboot :

Après avoir téléchargé le binaire compilé fw_printenv.

Un peu de test pour trouver la bonne configuration de fw_env.config à palcer dans /etc/

<code>
    # Configuration file for fw_(printenv/saveenv) utility.
    # Up to two entries are valid, in this case the redundant
    # environment sector is assumed present.
    # Notice, that the "Number of sectors" is ignored on NOR.

    # MTD device name       Device offset   Env. size       Flash sector size       Number of sectors

    # NAND example
    #GURUPLUG
    #/dev/mtd0               0x40000         0x20000         0x20000          1

    #SHEEVAPLUG
    #/dev/mtd0   0x0000      0x20000      0x20000      1

    #LSPRO
    #/dev/mtd0      0x3F000         0x1000          0x1000

    #/dev/mtd0   0x00      0x1000      0x20000   
    #/dev/mtd0      0xa0000         0x70000         0x20000

    #ICYBOX 6220
    /dev/mtd0   0xa0000      0x20000      0x20000
</code>


Le résultat recherché est là :

<code>
    baudrate=115200
    loads_echo=0
    ipaddr=10.4.50.165
    netmask=255.255.255.0
    CASset=min
    MALLOC_len=1
    ethprime=egiga0
    bootargs_end=:::DB88FXX81:eth0:none
    standalone=fsload 0x2000000 $(image_name);setenv bootargs $(console) root=/dev/mtdblock0 rw ip=$(ipaddr):$(serverip)$(bootargs_end) $(mvPhoneConfig); bootm 0x2000000;
    ethmtu=1500
    mvPhoneConfig=mv_phone_config=dev0:fxs,dev1:fxs
    mvNetConfig=mv_net_config=(00:11:88:0f:62:81,0:1:2:3),mtu=1500
    usb0Mode=host
    yuk_ethaddr=00:00:00:EE:51:81
    nandEcc=1bit
    netretry=no
    rcvrip=169.254.100.100
    loadaddr=0x02000000
    autoload=no
    ethact=egiga0
    bootargs_root=ubi.mtd=2,2048 root=ubi0:rootfs rootfstype=ubifs init=/linuxrc
    console=console=ttyS0,115200
    bootcmd=nand read.e 0x800000 0x100000 0x300000; setenv bootargs $(console) $(bootargs_root); bootm 0x800000
    rootpath=/tftpboot/marvell.nfs.rootfs
    image_name=uImage.6281a.ubifs.20090513
    serverip=10.128.129.205
    stdin=serial
    stdout=serial
    stderr=serial
    mainlineLinux=no
    enaMonExt=no
    enaCpuStream=no
    enaWrAllo=no
    pexMode=RC
    disL2Cache=no
    setL2CacheWT=yes
    disL2Prefetch=yes
    enaICPref=yes
    enaDCPref=yes
    sata_dma_mode=yes
    netbsd_en=no
    vxworks_en=no
    bootdelay=3
    disaMvPnp=no
    enaAutoRecovery=no
    ethaddr=00:01:d2:0e:26:44
</code>


Et tout ça sans une seule soudure, ni même démontage du boitier ! :shock:


Bon, c'est beau tout ça, mais :

Avantages (sans ordre préférentiel) :

  * Le boîtier est beau
  * c'est silencieux
  * le changement de disque est simplifié (pas de démontage)
  * l'interface ouèbe est chouette
  * le changement d'OS est facile
  * logiciels libres
  * ...


Inconvénients :

    * Liste à pucemal sécurisé en standard (comme tous les boîtiers équivalents ?)
    * ...
    
    
    L'enquête contiue, avec la maison mère ( AKITIO ) et le tunnel VPN qui passe par les flux DNS de worksys !
http://www.workssys.com/iSharing.html

/etc/client.conf

<code>
    client
    dev tun
    proto udp
    remote isharing.workssys.com 53
    resolv-retry infinite
    nobind
    persist-key
    persist-tun
    ca ca.crt
    cert client.crt
    key client.key
    comp-lzo
    verb 3
</code>        



http://wiki.myakitio.com/

http://cloudsync.myakitio.com/

Un produit équivalent chez ASUS :
http://www.asus.com/Networks/NAS/NASM25/#specifications

La petite analyse sécurité du jour :
Le mot de passe root d'origine ?

<code>
    sudo unshadow 'HACKNAS2/passwd-' 'HACKNAS2/shadow-' > 'HACKNAS2/crack.password.db'
</code>


<code>
    sudo john HACKNAS2/crack.password.db
</code>


<code>
    Created directory: /root/.john
    Loaded 2 password hashes with 2 different salts (FreeBSD MD5 [32/32])
    toor (root)
</code>


:siffle:

/etc/nas/lighttpd.conf

<code>
    # lighttpd configuration file

    accesslog.filename  = "/var/log/lighttpd/access.log"
    server.errorlog = "/var/log/lighttpd/error.log"
    index-file.names = ( "index.html" )

    mimetype.assign = (
      ".rpm"          =>      "application/x-rpm",
      ".pdf"          =>      "application/pdf",
      ".sig"          =>      "application/pgp-signature",
      ".spl"          =>      "application/futuresplash",
      ".class"        =>      "application/octet-stream",
      ".ps"           =>      "application/postscript",
      ".torrent"      =>      "application/x-bittorrent",
      ".dvi"          =>      "application/x-dvi",
      ".gz"           =>      "application/x-gzip",
      ".pac"          =>      "application/x-ns-proxy-autoconfig",
      ".swf"          =>      "application/x-shockwave-flash",
      ".tar.gz"       =>      "application/x-tgz",
      ".tgz"          =>      "application/x-tgz",
      ".tar"          =>      "application/x-tar",
      ".zip"          =>      "application/zip",
      ".mp3"          =>      "audio/mpeg",
      ".m3u"          =>      "audio/x-mpegurl",
      ".wma"          =>      "audio/x-ms-wma",
      ".wax"          =>      "audio/x-ms-wax",
      ".ogg"          =>      "application/ogg",
      ".wav"          =>      "audio/x-wav",
      ".gif"          =>      "image/gif",
      ".jar"          =>      "application/x-java-archive",
      ".jpg"          =>      "image/jpeg",
      ".jpeg"         =>      "image/jpeg",
      ".png"          =>      "image/png",
      ".xbm"          =>      "image/x-xbitmap",
      ".xpm"          =>      "image/x-xpixmap",
      ".xwd"          =>      "image/x-xwindowdump",
      ".css"          =>      "text/css",
      ".html"         =>      "text/html",
      ".htm"          =>      "text/html",
      ".js"           =>      "text/javascript",
      ".asc"          =>      "text/plain",
      ".c"            =>      "text/plain",
      ".cpp"          =>      "text/plain",
      ".log"          =>      "text/plain",
      ".conf"         =>      "text/plain",
      ".text"         =>      "text/plain",
      ".txt"          =>      "text/plain",
      ".dtd"          =>      "text/xml",
      ".xml"          =>      "text/xml",
      ".mpeg"         =>      "video/mpeg",
      ".mpg"          =>      "video/mpeg",
      ".mov"          =>      "video/quicktime",
      ".qt"           =>      "video/quicktime",
      ".avi"          =>      "video/x-msvideo",
      ".asf"          =>      "video/x-ms-asf",
      ".asx"          =>      "video/x-ms-asf",
      ".wmv"          =>      "video/x-ms-wmv",
      ".bz2"          =>      "application/x-bzip",
      ".tbz"          =>      "application/x-bzip-compressed-tar",
      ".tar.bz2"      =>      "application/x-bzip-compressed-tar",
      ".flv"          =>      "video/x-flv",
      # default mime type
      ""              =>      "application/octet-stream",
    )

    server.modules = (
        "mod_cgi",
        "mod_fastcgi",
        "mod_auth",
        "mod_rewrite",
        "mod_access",
        "mod_accesslog",
        "mod_proxy",
    )

    url.access-deny = ( "~", ".inc" )

    $HTTP["url"] =~ "\.pdf$" {
      server.range-requests = "disable"
    }

    static-file.exclude-extensions = ( ".cgi" )

    server.pid-file = "/var/run/lighttpd.pid"
    server.username = "lighttpd"
    server.groupname = "lighttpd"
    server.document-root = "/var/www/nas/"

    cgi.assign = ( ".cgi"  => "/usr/bin/python" )

    auth.backend = "htdigest"
    auth.backend.htdigest.userfile = "/etc/nas/htdigest"
    auth.require = (
        "/webdav" => (
            "method" => "digest",
            "realm" => "Network Attached Storage",
            "require" => "valid-user",
        ),
    )

    $HTTP["url"] =~ "^/submit|^/files" {
        proxy.server = ( "" =>
            (
                (
                    "host" => "127.0.0.1",
                    "port" => 4080
                )
            )
        )
    }

    fastcgi.debug = 1
    $HTTP["url"] =~ "^/testonly|^/dav|^/webdav|^/nas|^/[^_]+_[^_]+.*\.rss$" {
        fastcgi.server = (
            "" => (
                (
                  "socket" => "/var/run/nas-fastcgi.sock",
                  "check-local" => "disable",
                  "allow-x-send-file" => "enable",
                )
            ),
        )
    }
</code>


/usr/bin/nas-fastcgi

<code>
    #!/usr/bin/env python
    #fileencoding: utf-8
    #Author: Liu DongMiao <liudongmiao@gmail.com>
    #Created  : Fri 02 Jul 2010 03:23:25 PM CST
    #Modified : Thu 30 Sep 2010 12:42:23 PM CST

    import sys
    if len(sys.argv) > 1:
        debug = True
    else:
        debug = False

    import os
    import re
    import stat
    import errno
    import magic
    import mimetypes
    import urllib
    import urlparse
    from flup.server.fcgi import WSGIServer
    from nas.system import *
    from nas.convert import convert
    from cgitb import Hook
    from cStringIO import StringIO
    from nas.webdav import responses
    from nas.webdav import StatusError, StatusComplete, WEBDAV

    import pwd
    from nas.urls import URLS, UPLOAD
    from nas.login import updatetime

    try:
        mime = magic.open(magic.MAGIC_MIME)
        mime.load()
    except:
        mime = None
    mimetypes.init()

    def getquery(environ):
        uri, sep, query = environ['REQUEST_URI'].partition('?')
        tail = uri[-1:]
        uri = os.path.normpath(urllib.unquote_plus(uri))
        if tail == '/':
            uri += '/'

        if query:
            qs = {'url': '%s?%s' % (uri, query)}
        else:
            qs = {'url': '%s' % uri}

        def setrequest(qs, environ):
            length = int(environ['CONTENT_LENGTH'])
            qs['hash'] = environ.get('HTTP_SESSION', None)
            qs['post'] = environ['wsgi.input']
            qs['length'] = length
            header = environ.get('HTTP_CONTENT_RANGE', '')
            #if not header:
            #    header = environ.get('X_HTTP_CONTENT_RANGE', '')
            ranged = re.findall('^bytes (\d+)-(\d+)/(\d+)$', header)
            if len(ranged) == 1:
                start, end, overall = map(int, ranged[0])
                if start <= end and end <= overall:
                    qs['offset'] = start
                    if overall - end == 1:
                        qs['lastpackage'] = True
                    else:
                        qs['lastpackage'] = False

        method = environ['REQUEST_METHOD']
        if 'CONTENT_LENGTH' not in environ and 'HTTP_CONTENT_LENGTH' in environ:
            environ['CONTENT_LENGTH'] = environ['HTTP_CONTENT_LENGTH']

        if 'CONTENT_LENGTH' in environ:
            length = int(environ['CONTENT_LENGTH'])
            for (regex, view) in UPLOAD:
                if re.match(regex, uri):
                    setrequest(qs, environ)
                    break
            else:
                if uri.startswith('/dav') or uri.startswith('/webdav'):
                    setrequest(qs, environ)
                else:
                    query += '&%s' % environ['wsgi.input'].read(length)

        result = urlparse.parse_qsl(query, True)
        for name, value in result:
            #try:
            #    value = urllib.unquote_plus(value)
            #except UnicodeError:
            #    continue
            if name in qs:
                old = qs[name]
                if isinstance(old, str):
                    qs[name] = [old, value]
                else:
                    qs[name].append(value)
            else:
                qs[name] = value

        if qs.get('hash') is None:
            qs['hash'] = environ.get('HTTP_SESSION')

        qs['login'] = None
        if qs.get('hash') is not None:
            try:
                qs['login'] = updatetime(qs.get('hash'))
            except NASError:
                pass

        if 'REMOTE_USER' in environ:
            qs['login'] = environ.get('REMOTE_USER')

        #if 'login' not in qs:
        #    qs['login'] = None

        if False and 'login' not in qs:
            cookie = environ.get('HTTP_COOKIE', '')
            for item in re.split(';\s*', cookie):
                result = re.findall('^session=([a-f0-9]{40})$', item)
                if not len(result):
                    continue
                try:
                    login = updatetime(result[0])
                except NASError:
                    continue
                qs['login'] = login
                break

        return (uri, qs)

    def application(environ, start_response):
        try:
            code, headers, body = _application(environ, start_response)
        except Exception:
            code = 500
            headers = []
            mimetype = 'text/html'
            fp = StringIO()
            hook = Hook(file=fp)
            hook.handle()
            body = [fp.getvalue()]
            import time
            file = open('/tmp/nas.fastcgi.webdav.%s.html' % time.time(), 'w')
            file.write(fp.getvalue())
            file.close()
            fp.close()

        status = '%s %s' % (code, responses[code])

        start_response(status, headers)
        return body


    def _application(environ, start_response):
        headers = []
        body = []
       
        uri, qs = getquery(environ)

        if uri.startswith('/testonly'):
            nil, nil, query = environ['REQUEST_URI'].partition('?')
            from nas.testonly import testonly
            code = 200
            result = testonly(query)
            body = [result.getvalue()]
            result.close()
        elif uri.startswith('/dav') or uri.startswith('/webdav'):
            code = 405
            webdav = WEBDAV()
            method = environ.get('REQUEST_METHOD')
            qs['environ'] = environ
            print >>sys.stderr, uri, method, environ
            if hasattr(webdav, method):
                function = getattr(webdav, method)
                try:
                    function(**qs)
                except NASError as error:
                    values = {'error': {'reason': error.reason,
                                        'detail': error.detail
                    body = writexml(values)
                    if uri.startswith('/dav'):
                        code = 200
                    else:
                        code = 503
                except (StatusError, StatusComplete) as error:
                    code = error.status
                    headers = error.headers
                    body = error.body
        else:
            code = 404
            function = None
            mimetype = 'text/xml; charset="utf-8"'
            values = None
            view = None

            for (regex, view) in URLS + UPLOAD:
                if re.match(regex, uri):
                    break
            else:
                view = None

            if view is not None:
                (modname, sep, funcname) = view.rpartition('.')
                if sep == '.':
                    try:
                        __import__(modname)
                        module = sys.modules[modname]
                    except ImportError: pass
                    else:
                        if hasattr(module, funcname):
                            function = getattr(module, funcname)
                            code = 200

                if modname.endswith('noauth'):
                    print >>sys.stderr, uri
                    qs['uri'] = uri
                elif qs['login'] is None:
                    values = {'error': {'reason': 'Not Login'

            if values is None and callable(function):
                try:
                    values = function(**qs)
                except NASError as error:
                    values = {'error': {'reason': error.reason,
                                        'detail': error.detail
                except (StatusError, StatusComplete) as error:
                    code = error.status
                    headers = error.headers
                    body = error.body
                except OSError as error:
                    values = {'error': {'reason': error.strerror,
                                        'detail': error.filename

            if debug:
                print >>sys.stderr, qs

            if values:
                if isinstance(values, (basestring, list, dict)) and qs.get('output') == 'json':
                    mimetype = 'text/javascript; charset="utf-8"'
                    body = writexml(values, **qs)
                else:
                    body = writexml(values)

            if debug:
                print >>sys.stderr, body

            for header in headers:
                if header[0].lower() == 'content-type':
                    break
            else:
                headers.append(('Content-Type', mimetype))

        return code, headers, body

    if __name__ == '__main__':
        pidfile = '/var/run/nas-fastcgi.pid'
        pid = getpid(pidfile)
        if pid:
            print >>sys.stderr, 'nas-fastcgi is running at', pid
            sys.exit(0)
        if not debug:
            daemon()
        # write pid
        file = open(pidfile, 'w')
        try:
            file.write(str(os.getpid()))
        finally:
            file.close()

        import signal
        from nas.system import sigchld
        signal.signal(signal.SIGCHLD, sigchld)

        options = { 'bindAddress': '/var/run/nas-fastcgi.sock', 'umask': 0000 }
        WSGIServer(application, **options).run()

    # vim: set sta sw=4 et:
</code>    
    
    KÉSSÉÇA !?

Le "cloud"... le "nuage" c'est aussi ça ?! :shock:

C'est chouette, j'ai une url dynamique perso chez myicybox.com ?


:wiki:notes:nashack:capture000.png|

Cette url :

:wiki:notes:nashack:capture000-1.png|



Me donne accès sur le NAS :


:wiki:notes:nashack:capture000-2.png|

avec activation du JavaScript je suis sur mon IP privée !

Un tunnel VPN... chez : worksys.com.cn est actif à partir de mon NAS...

:wiki:notes:nashack:capture000-3.png|



Ce tunnel VPN est activé au démarrage... à chaque démarrage ...
Chiffré et sécurisé.

:wiki:notes:nashack:capture000-5.png|


Cette IP n'est pas chez moi :



Les réglages du NAS ne mentionne rien.

:wiki:notes:nashack:capture000-7.png|



Les redémarrages successifs se font attribuer des IP internes différentes. L'adresse MAC matérielle change.

:wiki:notes:nashack:capture000-8.png|



Pourtant le VPN est là :

:wiki:notes:nashack:capture000-9.png|



Et ce tunel VPN passe sur le port 53 (BIND, LE DNS) le plus facilement camouflable, le plus facilement utilisable par les hackers car non filtrable.

:wiki:notes:nashack:capture000-10.png|



Ce tunnel est chiffré et il est impossible de le sniffer.
Il n'est pas routé, mais pourrait l'être.

worksys.com (.cn) redirige mon IP qu'il a donc obtenu dynamiquement et en temps réel.
MAIS, n'a-t-il que ces données.

Su un NAS ou je suis censé stocker mes informations personnelles, sécurisées, localement !!!

GRANDIOSE... :grr:

Le programme est de cloner le système uboot+linux+rootfs ( fedora modifié ) sur un sheevalug (même processeur) pour valider la méthode d'upgrade de l'IB-6220 ( le NAS ).
Le sheevaplug possède un port série + jtag directement accessible par un simple cable USB.

Une fois la méthode validée, et les problèmes résolus, je pourrais mettre à jour le nas sans risque.
Celui ne possède pas de port jtag ni de port série facilement accessible.

Le démontage détermine un possible port série :

<code>
    3,3V   RX   TX  GND
</code>


Mais, pour le sport, et surtout pour la simplicité de la procédure pour d'autres, je vais le faire "à ma méthode", sans démontage...

<code>
    Hey guys some news ....
    Current pinout of serial console
    2mm lead pitch header, near 2*5 header, PCB is with USB/Ethernet-Plug is facing to you.
    The 2 other (4 pin header are on right side)
</code>

<code>
    UNKNOWN UNKNOWN TX GND
    (RX) (3,3V)

    In pins in parentheses, are not tested yet !!!
</code>

    
<code>
        3,3V   RX   TX  GND
        
    You need a cable with 3,3Volts signals !!
</code>


    
<code>
        $ busybox microcom -s 115200 /dev/ttyUSB0
</code>
        
        La méthode du clonage est validée.
Il a fallut mette à jour linux ( le noyau ou kernel ) et les modules pour des problèmes de stabilité et bug dans la version intégrée au nas.
Essentiellement des problèmes réseau sur le sheevaplug.

:wiki:notes:nashack:capture00000.png|

:wiki:notes:nashack:capture0000.png|

:wiki:notes:nashack:capture0000-3.png|


Il faut, en plus du boitier NAS à cloner, un clé USB debian "maison" et un sheevaplug...

:wiki:notes:nashack:capture0000-1.png|



Le Linux 2.6.35.4 sera aussi utile pour résoudre les BUG de la version 2.6.35.4 intégrée au IB6220.

Il faut pour cloner à partir de l'IB6220, les u-boot-tools ( uboot env ) et les mtd-utils ( nand ) :

À préparer sur une debian puis à rappatrier dans les dossier /home/hackme de travaille sur le IB ( ou le clone ).

http://packages.debian.org/squeeze/armel/uboot-envtools

wget http://ftp.fr.debian.org/debian/pool/main/u/uboot-envtools/uboot-envtools_20081215-2_armel.deb
dpkg -x uboot-envtools_20081215-2_armel.deb hackme/uboot

http://packages.debian.org/squeeze/armel/mtd-utils

wget http://ftp.fr.debian.org/debian/pool/main/m/mtd-utils/mtd-utils_20090606-1_armel.deb
dpkg -x mtd-utils_20090606-1_armel.deb hackme/mtd

Les varaiables d'environnement uboot utilisée pour les tests du clone sont :

<code>
    [root@JCLONE ~]# /home/hackme/u-boot-tools/fw_printenv
    bootdelay=3
    baudrate=115200
    x_bootargs=console=ttyS0,115200 mtdparts=orion_nand:512k(uboot),4m@1m(kernel),507m@5m(rootfs) rw
    x_bootcmd_kernel=nand read 0x6400000 0x100000 0x400000
    x_bootcmd_sata=ide reset;
    x_bootargs_root=ubi.mtd=2 root=ubi0:rootfs rootfstype=ubifs
    ethact=egiga0
    bootcmd_usb=usb start; run x_bootcmd_usb; bootm 0x00800000 0x01100000
    x_bootcmd_usb=setenv bootargs ${x_bootargs_root_usb}; ext2load usb 0:1 0x00800000 /uImage; ext2load usb 0:1 0x01100000 /uInitrd;
    x_bootargs_root_usb=console=ttyS0,115200 root=/dev/sda3 mtdparts=orion_nand:1m(uboot),6m@1m(kernel),249m@7m(rootfs) rw
    x_bootargs_console=console=ttyS0,115200
    bootcmd=run bootcmd_ethernet;run x_bootcmd_nand
    bootcmd_ethernet=setenv ethact egiga0; ${x_bootcmd_ethernet}; setenv ethact egiga1; ${x_bootcmd_ethernet};
    gatewayip=192.168.0.1
    serverip=192.168.0.254
    ipaddr=192.168.0.177
    ethaddr=00:50:43:01:62:7e
    x_bootcmd_ethernet=ping 192.168.0.1
    mainlineLinux=yes
    arcNumber=2097
    x_bootargs_root_nand=ubi.mtd=2,2048 root=ubi0:rootfs rootfstype=ubifs init=/linuxrc mtdparts=orion_nand:1m(uboot),6m@1m(kernel),249m@7m(rootfs) rw
    stdin=serial
    stdout=serial
    stderr=serial
    x_bootcmd_nand=setenv bootargs $(x_bootargs_console) $(x_bootargs_root_nand); nand read.e 0x00800000 0x00100000 0x00300000; bootm 0x00800000;
</code>


Ces variables sont modifiables et affichables, après modification ( upgrade ) de l'uboot par le denx ( modifié ) perso :


<code>
    [root@JCLONE ~]# cat /etc/fw_env.config
    # SHEEVAPLUG DENX UBOOT                                                         
    /dev/mtd0               0x60000         0x20000         0x20000                 
</code>


L'uboot utilisé pour le clone est le 20110531-MMC-SATA
Il intègre les patchs qui sont maintenant intégré dans l'uboot Debian !

Pièces jointes

:wiki:notes:nashack:uboot-sata-mmc.zip|

:wiki:notes:nashack:nashack.tar.gz|

:wiki:notes:nashack:2.6.35.4.tar.gz|

Le principe d'un VPN :

:wiki:notes:nashack:capture-02.png|



L'explication commerciale !

:wiki:notes:nashack:capture-04.png|

:wiki:notes:nashack:capture-05.png|

:wiki:notes:nashack:capture-06.png|

:wiki:notes:nashack:capture-07.png|

:wiki:notes:nashack:capture-08.png|

:wiki:notes:nashack:capture-09.png|

:wiki:notes:nashack:capture-10.png|



:wiki:notes:nashack:capture-11.png|



Le copyright :

:wiki:notes:nashack:capture-12.png|


Et pourtant il est actif, sasn possibilité utilisateur de l'arrêter, ni même le voir...

:wiki:notes:nashack:capture-15.png|



alors qu'un simple


<code>
    $ chkconfig openvpn off
</code>

dans un terminal.
Suivi d'un reboot, et il n'est plus lancé !

PLus besoin au grand internet de sauvegarder vos données personnelles, vous le faites pour eux !
:diablo:

Mais c'est gratuit, au moins au début ! :diablo:

:wiki:notes:nashack:capture-5.png|



Et puis c'est joli...

:wiki:notes:nashack:capture-6.png|



Il existe plusieurs portail / société :
myisharing.com

:wiki:notes:nashack:capture-7.png|


myakitio.com

:wiki:notes:nashack:capture-8.png|



Ces produits ont des documentations officielles sous la forme de wiki :
cloudsync.myakitio.com/
wiki.myakitio.com/

:wiki:notes:nashack:changelog.pdf|ChangeLog.pdf

Bien sûr, tout ceci n'est pas un problème, mais une fonctionnalité, et ce n'est pas envisageable de la désactiver :

:wiki:notes:nashack:capture-9.png|

On se retrouve à partir d'un produit allemand, fabriqué en chine, sur des sites américains et canadien, mais mon analyse montre que les certificats de la connexion VPN et la connexion elle même, est réalisée avec la chine !

Pourquoi faire des spywares et autre logiciels espions quand le produit peut-être lui même un "pont" avec votre réseau !
:up:

Réf : 
:wiki:notes:nashack:uboot-envtool.tar|