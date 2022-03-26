---
title: How to void your RaidSonic IcyBox NAS6220-B Warrantly...
lang: en
date: 2014-09-24 00:00:00
tags: ARM,ARMADA,NAS
---
====== How to void your RaidSonic IcyBox NAS6220-B Warrantly... ======

**All informations in this page are given "as-is", without warrantly, and can be harmfull !**

The *why* of all of this is here : "lecloud"

==== Requirements ====

Some linux knowledges, debian administration skills, and cross-toolchain compilations.
Will be also needed (minimal requirement) :
  * a screw-driver
  * two usb keys
  * some electric straps
  * a computer (tested with debian but it should work with less privileges system)
  * a internet connection (uncensored)

==== Why ====

I already own some SheevaPlugs, GuruPlugs from GlobalScale.
You are already using one also... 8-o

The ICYBOX NAS 6220 B is made with a Marvel Kirkwood 88F6281 (same µC as the Seagate DockStar) (1.2 GHz)

I just bought one and want to put Debian on it.

I started with this [thread @ NAS-Portal.org](http://forum.nas-portal.org/showthread.php?12855-Ib-nas6220-b|Ib-nas6220-b) and a small Genesi SmartBook to hack this cool NAS.
=== NO CLOUD at HOME ===

After had bought this small NAS, I discovered that a **VPN Tunnel is made with China at bootup** !

I do not agree anywhere with this and had decided to hack this box to install Debian on it. ( more secure, more open, more stable ... )

==== What ====

WIP (Work in Progress)

Short info Marvel Kirkwood SOC 1,2 GHz

   1. 256 MiB RAM
   2. 256 MiB Flash (uboot, Kernel, UBIFS)
   3. 2 * SATA
   4. 3 * USB (trough a 4 Port USB-HUB) on one USB ROOT-HUB on SOC
   5. 40 cm FAN
   6. (currently) Supports only for 2TB HDD's, check for 4K HDD's will follow 

Software Issue

   1. SSH Server running in background, need SSH-Keys to login. Maybe this thing is calling home
   2. FTP, SAMBA, DLNA Server (mt-daapd ?) 

OS-Type

   1. Fedora 
   
===== How =====

**WIP**

//Some works no more needed (see bootom of the page)//

==== References ====

  * [wiki @ NAS-Portal.org](http://wiki.nas-portal.org/index.php/IB-NAS6220-B)
  * [Datasheet of NAS6220](http://www.raidsonic.de/data/products/icybox/IB-NAS6220/datasheet_ib-nas6220_e.pdf)
  * [Datasheet of NAS6210](http://www.raidsonic.de/data/datasheet/icybox/EN/datasheet_ib-nas6210_e.pdf)
  * [RaidSonic ICY BOX IB-NAS6210, my “new” SheevaPlug](http://simon.baatz.info/raidsonic-icy-box-ib-nas6210-my-new-sheevaplug/)

==== Publication ====

[Comment perdre la garantie de son NAS (GNU/Linux Magazine) n°156 - janvier 2013 - Par Kerma Gérald)](https://connect.ed-diamond.com/GNU-Linux-Magazine/glmf-156/comment-perdre-la-garantie-de-son-nas)

Les serveurs de stockage externe, ou NAS (« Network Attached Storage ») sont devenus une partie importante des réseaux personnels et des petites entreprises.

===== Hardware modifications =====

Customized IB6220 :


:wiki:notes:ib6220-inside.jpg?w=200|

==== Add JTAG ====

::ib6220-jtag.jpg?200|

==== Add Serial ====

::ib6220-serial-uart.jpg?200|

Pinout of the J2 serial port\\
Pin 1	3.3V (pin 1 has a white stripe next to it)\\
Pin 2	RXD (from serial terminal program to NSLU2)\\
Pin 3	TXD (from NSLU2 to serial terminal program)\\
Pin 4	GND\\

RXD and TXD are (LV)TTL signals (0V/3.3V), not RS-232 signals (+/-12V). This means that they cannot be connected directly to a PC serial port. Converters are discussed below. 

[[http://www.nslu2-linux.org/wiki/HowTo/AddASerialPort]]

==== Add USB to Serial Converter ====

Passerelle USB/série BOB-FT232R (110553-91) 

:wiki:notes:110553-91.jpg?nolink&200|

[[http://www.elektor.fr/products/kits-modules/modules/110553-91-ft232r-usb-serial-bob.1913324.lynkx]]

Connector : H4PL / H4PL (AKA MPC 2 / MPC 2)

:wiki:notes:mpc2_4wire.jpeg?nolink&200|
===== U-Boot =====

==== Default U-Boot ====

Here is the default Marvell u-boot :
<code>
         __  __                      _ _
        |  \/  | __ _ _ ____   _____| | |
        | |\/| |/ _` | '__\ \ / / _ \ | |
        | |  | | (_| | |   \ V /  __/ | |
        |_|  |_|\__,_|_|    \_/ \___|_|_|
 _   _     ____              _
| | | |   | __ )  ___   ___ | |_
| | | |___|  _ \ / _ \ / _ \| __|
| |_| |___| |_) | (_) | (_) | |_
 \___/    |____/ \___/ \___/ \__|
 ** MARVELL BOARD: DB-88F6281A-BP LE

U-Boot 1.1.4 (Oct 12 2009 - 13:41:53) Marvell version: 3.4.16

U-Boot code: 00600000 -> 0067FFF0  BSS: -> 006CEE60

Soc: MV88F6281 Rev 3 (DDR2)
CPU running @ 1200Mhz L2 running @ 400Mhz
SysClock = 400Mhz , TClock = 200Mhz

DRAM CAS Latency = 5 tRP = 5 tRAS = 18 tRCD=6
DRAM CS[0] base 0x00000000   size 256MB
DRAM Total size 256MB  16bit width
Flash:  0 kB
Addresses 8M - 0M are saved for the U-Boot usage.
Mem malloc Initialization (8M - 7M): Done
NAND:256 MB

CPU : Marvell Feroceon (Rev 1)

Streaming disabled
Write allocate disabled


USB 0: host mode
PEX 0: interface detected no Link.
Net:   egiga0 [PRIME]
Hit any key to stop autoboot:  0
</code>

==== Default U-Boot commands ====
<code>
Marvell>> help
?       - alias for 'help'
SatR - sample at reset sub-system, relevent for DB only
base    - print or set address offset
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootext2    dev:boot_part1,boot_part2 addr boot_image linux_dev_name 
bootm   - boot application image from memory
bootp	- boot image via network using BootP/TFTP protocol
bubt	- Burn an image on the Boot Nand Flash.
chpart	- change active partition
cmp     - memory compare
cmpm	- Compare Memory
cp      - memory copy
cpumap - Display CPU memory mapping settings.
crc32   - checksum calculation
date    - get/set/reset date & time
dclk	- Display the MV device CLKs.
dhcp	- invoke DHCP client to obtain IP/boot params
diskboot- boot from IDE device
echo    - echo args to console
eeprom  - EEPROM sub-system
erase   - erase FLASH memory
ext2load- load binary file from a Ext2 filesystem
ext2ls  - list files in a directory (default /)
fatinfo - print information about filesystem
fatload - load binary file from a dos filesystem
fatls   - list files in a directory (default /)
fi	- Find value in the memory.
flinfo  - print FLASH memory information
fsinfo	- print information about filesystems
fsload	- load binary file from a filesystem image
g	- start application at cached address 'addr'(default addr 0x40000)
go      - start application at address 'addr'
help    - print online help
icrc32  - checksum calculation
ide     - IDE sub-system
iloop   - infinite loop on address range
imd     - i2c memory display
imm[.b, .s, .w, .l]     - i2c memory modify (auto-incrementing)
imw     - memory write (fill)
inm     - memory modify (constant address)
iprobe  - probe to discover valid I2C chip addresses
ir	- reading and changing MV internal register values.
loop    - infinite loop on address range
ls	- list files in a directory (default /)
map	- Diasplay address decode windows
md      - memory display
me	- PCI master enable
mm      - memory modify (auto-incrementing)
mp	- map PCI BAR
mtdparts- define flash/nand partitions
mtest   - simple RAM test
mw      - memory write (fill)
nand                   - NAND sub-system
nboot   - boot from NAND device
nbubt	- Burn a boot loader image on the Boot Nand Flash.
nm      - memory modify (constant address)
pci     - list and access PCI Configuration Space
phyRead	- Read PCI-E Phy register
pciePhyWrite	- Write PCI-E Phy register
phyRead	- Read Phy register
phyWrite	- Write Phy register
ping	- send ICMP ECHO_REQUEST to network host
printenv- print environment variables
protect - enable or disable FLASH write protection
rarpboot- boot image via network using RARP/TFTP protocol
rcvr	- Satrt recovery process (Distress Beacon with TFTP server)
reset   - Perform RESET of the CPU
resetenv	- Return all environment variable to default.
run     - run commands in an environment variable
saveenv - save environment variables to persistent storage
se	- PCI Slave enable
setenv  - set environment variables
sflash	- read, write or erase the external SPI Flash.
sg	- scanning the PHYs status
sp	- Scan PCI bus.
tftpboot- boot image via network using TFTP protocol
usb     - USB sub-system
usbboot - boot from USB device
version - print monitor version
</code>

===== Proof Of Concept =====
==== u-boot ====

<code>
U-Boot 2011.09-00282-gd8fffa0-dirty (Oct 14 2011 - 16:09:23)                    
Raidsonic Icybox NAS6220-B                                                      
                                                                                
SoC:   Kirkwood 88F6281_A1                                                      
DRAM:  256 MiB                                                                  
WARNING: Caches not enabled                                                     
NAND:  256 MiB                                                                  
*** Warning - bad CRC, using default environment                                
                                                                                
In:    serial                                                                   
Out:   serial                                                                   
Err:   serial                                                                   
Net:   egiga0                                                                   
PHY reset timed out                                                             
88E1116 Initialized on egiga0                                                   
Hit any key to stop autoboot:  0                                                
Using egiga0 device                                                             
ping failed; host 192.168.2.1 is not alive                                      
</code>
==== bootstrap ====
<code>
(Re)start USB...                                                                
USB:   Register 10011 NbrPorts 1                                                
USB EHCI 1.00                                                                   
scanning bus for devices... 2 USB Device(s) found                               
       scanning bus for storage devices... 0 Storage Device(s) found            
                                                                                
Reset IDE: Bus 0: OK Bus 1: OK                                                  
  Device 0: Model: SAMSUNG HD204UI  Firm: 1AQ10001 Ser#: S2H7J9BB305519         
            Type: Hard Disk                                                     
            Supports 48-bit addressing                                          
            Capacity: 1907729.0 MB = 1863.0 GB (-387938128 x 512)               
  Device 1: Model: SAMSUNG HD204UI  Firm: 1AQ10001 Ser#: S2H7J9BB305519         
            Type: Hard Disk                                                     
            Supports 48-bit addressing                                          
            Capacity: 1907729.0 MB = 1863.0 GB (-387938128 x 512)               
> boot - usb fat 0:1 -                                                          
                                                                                
** Invalid boot device **                                                       
                                                                                
## Checking Image at 00600000 ...                                               
Unknown image format!                                                           
> boot - usb ext2 0:1 -                                                         
** Block device usb 0 not supported                                             
                                                                                
## Checking Image at 00600000 ...                                               
Unknown image format!                                                           
> boot - ide fat 0:1 -                                                          
reading boot.scr                                                                
                                                                                
** Unable to read "boot.scr" from ide 0:1 **                                    
                                                                                
## Checking Image at 00600000 ...                                               
Unknown image format!                                                           
> boot - ide ext2 0:1 -                                                         
Loading file "boot.scr" from ide device 0:1 (hda1)                              
Failed to mount ext2 filesystem...                                              
** Bad ext2 partition or disk - ide 0:1 **                                      
                                                                                
## Checking Image at 00600000 ...                                               
Unknown image format!                                                           
                                                                                
NAND read: device 0 offset 0x200000, size 0x500000                              
 5242880 bytes read: OK                                                         
                                                                                
NAND read: device 0 offset 0x700000, size 0x800000                              
Skipping bad block 0x00940000                                                   
 8388608 bytes read: OK                                                         
Unknown command '!' - try 'help'                                                
         
</code>
==== linux loading ====

<code>                                                                                
## Checking Image at 00700000 ...                                               
   Legacy image found                                                           
   Image Name:   Debian kernel                                                  
   Image Type:   ARM Linux Kernel Image (uncompressed)                          
   Data Size:    1435664 Bytes = 1.4 MiB                                        
   Load Address: 00008000                                                       
   Entry Point:  00008000                                                       
   Verifying Checksum ... OK                                                    
## Booting kernel from Legacy Image at 00700000 ...                             
   Image Name:   Debian kernel                                                  
   Image Type:   ARM Linux Kernel Image (uncompressed)                          
   Data Size:    1435664 Bytes = 1.4 MiB                                        
   Load Address: 00008000                                                       
   Entry Point:  00008000                                                       
   Verifying Checksum ... OK                                                    
## Loading init Ramdisk from Legacy Image at 00900000 ...                       
   Image Name:   Debian ramdisk                                                 
   Image Type:   ARM Linux RAMDisk Image (gzip compressed)                      
   Data Size:    4910351 Bytes = 4.7 MiB                                        
   Load Address: 00000000                                                       
   Entry Point:  00000000                                                       
   Verifying Checksum ... OK                                                    
   Loading Kernel Image ... OK                                                  
OK                                                                              
</code>
==== starting kernel ====
<code>
Using machid 0x690 from environment                                             
                                                                                
Starting kernel ...                                                             
                                                                                
Uncompressing Linux... done, booting the kernel.                                
[    0.000000] Initializing cgroup subsys cpuset                                
[    0.000000] Initializing cgroup subsys cpu                                   
[    0.000000] Linux version 2.6.32-5-kirkwood (Debian 2.6.32-38) (ben@decadent1
[    0.000000] CPU: Feroceon 88FR131 [56251311] revision 1 (ARMv5TE), cr=0005397
[    0.000000] CPU: VIVT data cache, VIVT instruction cache                     
[    0.000000] Machine: Marvell DB-88F6281-BP Development Board                 
[    0.000000] Memory policy: ECC disabled, Data cache writeback                
[    0.000000] Built 1 zonelists in Zone order, mobility grouping on.  Total pa4
[    0.000000] Kernel command line: console=ttyS0,115200 mtdparts=orion_nand:1mt
[    0.000000] PID hash table entries: 1024 (order: 0, 4096 bytes)              
[    0.000000] Dentry cache hash table entries: 32768 (order: 5, 131072 bytes)  
[    0.000000] Inode-cache hash table entries: 16384 (order: 4, 65536 bytes)    
[    0.000000] Memory: 256MB = 256MB total                                      
[    0.000000] Memory: 250496KB available (3516K code, 583K data, 124K init, 0K)
[    0.000000] SLUB: Genslabs=11, HWalign=32, Order=0-3, MinObjects=0, CPUs=1, 1
[    0.000000] Hierarchical RCU implementation.                                 
[    0.000000] NR_IRQS:114                                                      
[    0.000000] Console: colour dummy device 80x30                               
[    0.000124] Calibrating delay loop... 1192.75 BogoMIPS (lpj=5963776)         
[    0.240079] Security Framework initialized                                   
[    0.240099] SELinux:  Disabled at boot.                                      
[    0.240119] Mount-cache hash table entries: 512                              
[    0.240373] Initializing cgroup subsys ns                                    
[    0.240386] Initializing cgroup subsys cpuacct                               
[    0.240394] Initializing cgroup subsys devices                               
[    0.240403] Initializing cgroup subsys freezer                               
[    0.240411] Initializing cgroup subsys net_cls                               
[    0.240450] CPU: Testing write buffer coherency: ok                          
[    0.241026] devtmpfs: initialized                                            
[    0.242434] regulator: core version 0.5                                      
[    0.242609] NET: Registered protocol family 16                               
[    0.242990] Kirkwood: MV88F6281-A1, TCLK=200000000.                          
[    0.243003] Feroceon L2: Cache support initialised.                          
[    0.243782] Kirkwood PCIe port 0:                                            
[    0.243789] link down, ignoring                                              
[    0.244847] bio: create slab <bio-0> at 0                                    
[    0.245126] vgaarb: loaded                                                   
[    0.245601] Switching to clocksource orion_clocksource                       
[    0.249637] NET: Registered protocol family 2                                
[    0.249881] IP route cache hash table entries: 2048 (order: 1, 8192 bytes)   
[    0.250714] TCP established hash table entries: 8192 (order: 4, 65536 bytes) 
[    0.250898] TCP bind hash table entries: 8192 (order: 3, 32768 bytes)        
[    0.250993] TCP: Hash tables configured (established 8192 bind 8192)         
[    0.251003] TCP reno registered                                              
[    0.251155] NET: Registered protocol family 1                                
[    0.251336] Unpacking initramfs...                                           
[    0.584163] Freeing initrd memory: 4792K                                     
[    0.584275] NetWinder Floating Point Emulator V0.97 (double precision)       
[    0.584527] audit: initializing netlink socket (disabled)                    
[    0.584562] type=2000 audit(0.570:1): initialized                            
[    0.591063] VFS: Disk quotas dquot_6.5.2                                     
[    0.591334] Dquot-cache hash table entries: 1024 (order 0, 4096 bytes)       
[    0.591429] JFFS2 version 2.2. (NAND) (SUMMARY)  �© 2001-2006 Red Hat, Inc.  
[    0.592077] msgmni has been set to 499                                       
[    0.593833] alg: No test for stdrng (krng)                                   
[    0.593955] Block layer SCSI generic (bsg) driver version 0.4 loaded (major )
[    0.593968] io scheduler noop registered                                     
[    0.593975] io scheduler anticipatory registered                             
[    0.593983] io scheduler deadline registered                                 
[    0.594163] io scheduler cfq registered (default)                            
[    0.600268] Serial: 8250/16550 driver, 2 ports, IRQ sharing disabled         
[    0.600747] serial8250.0: ttyS0 at MMIO 0xf1012000 (irq = 33) is a 16550A    
[    0.931833] console [ttyS0] enabled                                          
[    0.935937] NAND device: Manufacturer ID: 0xec, Chip ID: 0xda (Samsung NAND )
[    0.944597] Scanning device for bad blocks                                   
[    0.951511] Bad eraseblock 74 at 0x000000940000                              
[    0.968777] Bad eraseblock 417 at 0x000003420000                             
[    0.982085] Bad eraseblock 651 at 0x000005160000                             
[    0.992771] Bad eraseblock 814 at 0x0000065c0000                             
[    1.013201] Bad eraseblock 1240 at 0x000009b00000                            
[    1.035346] Bad eraseblock 1710 at 0x00000d5c0000                            
[    1.044334] Bad eraseblock 1825 at 0x00000e420000                            
[    1.057319] 5 cmdlinepart partitions found on MTD device orion_nand          
[    1.063611] Creating 5 MTD partitions on "orion_nand":                       
[    1.068794] 0x000000000000-0x000000100000 : "uboot"                          
[    1.074255] 0x000000100000-0x000000200000 : "strap"                          
[    1.079634] 0x000000200000-0x000000700000 : "kernel"                         
[    1.085089] 0x000000700000-0x000000f00000 : "ramdisk"                        
[    1.090675] 0x000000b00000-0x00000fb00000 : "rootfs"                         
[    1.096800] mice: PS/2 mouse device common for all mice                      
[    1.102266] rtc-mv rtc-mv: rtc core: registered rtc-mv as rtc0               
[    1.108213] i2c /dev entries driver                                          
[    1.111902] cpuidle: using governor ladder                                   
[    1.116151] cpuidle: using governor menu                                     
[    1.120160] mv_xor_shared mv_xor_shared.0: Marvell shared XOR driver         
[    1.126574] mv_xor_shared mv_xor_shared.1: Marvell shared XOR driver         
[    1.165672] mv_xor mv_xor.0: Marvell XOR: ( xor cpy )                        
[    1.205668] mv_xor mv_xor.1: Marvell XOR: ( xor fill cpy )                   
[    1.245669] mv_xor mv_xor.2: Marvell XOR: ( xor cpy )                        
[    1.285666] mv_xor mv_xor.3: Marvell XOR: ( xor fill cpy )                   
[    1.292337] TCP cubic registered                                             
[    1.295582] NET: Registered protocol family 17                               
[    1.300413] registered taskstats version 1                                   
[    1.305216] rtc-mv rtc-mv: setting system clock to 2011-10-14 16:43:00 UTC ()
[    1.313327] Initalizing network drop monitor service                         
[    1.318389] Freeing init memory: 124K                                        
Loading, please wait...                                                         
[    1.366081] udev[44]: starting version 164                                   
[    1.703926] SCSI subsystem initialized                                       
[    1.728849] MV-643xx 10/100/1000 ethernet driver version 1.4                 
[    1.734841] mv643xx_eth smi: probed                                          
[    1.787261] usbcore: registered new interface driver usbfs                   
[    1.878059] usbcore: registered new interface driver hub                     
[    1.886856] usbcore: registered new device driver usb                        
[    1.893860] net eth0: port 0 with MAC address 00:50:43:01:02:03              
[    1.900371] mmc0: mvsdio driver initialized, using GPIO 38 for card detection
[    1.940326] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver       
[    1.946982] orion-ehci orion-ehci.0: Marvell Orion EHCI                      
[    1.952289] orion-ehci orion-ehci.0: new USB bus registered, assigned bus nu1
[    1.995690] orion-ehci orion-ehci.0: irq 19, io mem 0xf1050000               
[    2.015637] orion-ehci orion-ehci.0: USB 2.0 started, EHCI 1.00              
[    2.021637] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002    
[    2.028472] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber1
[    2.035737] usb usb1: Product: Marvell Orion EHCI                            
[    2.040460] usb usb1: Manufacturer: Linux 2.6.32-5-kirkwood ehci_hcd         
[    2.046860] usb usb1: SerialNumber: orion-ehci.0                             
[    2.052423] usb usb1: configuration #1 chosen from 1 choice                  
[    2.058353] hub 1-0:1.0: USB hub found                                       
[    2.062153] hub 1-0:1.0: 1 port detected                                     
[    2.066332] sata_mv sata_mv.0: version 1.28                                  
[    2.070655] sata_mv sata_mv.0: slots 32 ports 2                              
[    2.089228] scsi0 : sata_mv                                                  
[    2.092708] scsi1 : sata_mv                                                  
[    2.096044] ata1: SATA max UDMA/133 irq 21                                   
[    2.100158] ata2: SATA max UDMA/133 irq 21                                   
[    2.385644] usb 1-1: new high speed USB device using orion-ehci and address 2
[    2.536209] usb 1-1: New USB device found, idVendor=1a40, idProduct=0101     
[    2.542942] usb 1-1: New USB device strings: Mfr=0, Product=1, SerialNumber=0
[    2.550123] usb 1-1: Product: USB 2.0 Hub                                    
[    2.555460] usb 1-1: configuration #1 chosen from 1 choice                   
[    2.564860] hub 1-1:1.0: USB hub found                                       
[    2.568835] hub 1-1:1.0: 4 ports detected                                    
[    2.615670] ata1: SATA link up 3.0 Gbps (SStatus 123 SControl F300)          
[    2.635866] ata1.00: ATA-8: SAMSUNG HD204UI, 1AQ10001, max UDMA/133          
[    2.642169] ata1.00: 3907029168 sectors, multi 0: LBA48 NCQ (depth 31/32)    
[    2.665968] ata1.00: configured for UDMA/133                                 
[    2.670624] scsi 0:0:0:0: Direct-Access     ATA      SAMSUNG HD204UI  1AQ1 P5
[    3.185652] ata2: SATA link up 3.0 Gbps (SStatus 123 SControl F300)          
[    3.205867] ata2.00: ATA-8: SAMSUNG HD204UI, 1AQ10001, max UDMA/133          
[    3.212169] ata2.00: 3907029168 sectors, multi 0: LBA48 NCQ (depth 31/32)    
[    3.235994] ata2.00: configured for UDMA/133                                 
[    3.240558] scsi 1:0:0:0: Direct-Access     ATA      SAMSUNG HD204UI  1AQ1 P5
[    3.284583] sd 0:0:0:0: [sda] 3907029168 512-byte logical blocks: (2.00 TB/1)
[    3.292832] sd 1:0:0:0: [sdb] 3907029168 512-byte logical blocks: (2.00 TB/1)
[    3.301753] sd 0:0:0:0: [sda] Write Protect is off                           
[    3.306704] sd 1:0:0:0: [sdb] Write Protect is off                           
[    3.311654] sd 0:0:0:0: [sda] Write cache: enabled, read cache: enabled, doeA
[    3.320815] sd 1:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doeA
[    3.330998]  sdb:                                                            
[    3.333247]  sda: sda1 sda2 sda3                                             
[    3.377745]  sdb1 sdb2 sdb3                                                  
[    3.384756] sd 0:0:0:0: [sda] Attached SCSI disk                             
[    3.394194] sd 1:0:0:0: [sdb] Attached SCSI disk                             
Begin: Loading essential drivers ... [    3.755672] md: raid1 personality regis1
done.                                                                           
Begin: Running /scripts/init-premount ... done.                                 
Begin: Mounting root file system ... Begin: Running /scripts/local-top ... Begi.
done.                                                                           
Begin: Assembling all MD arrays ... [    3.810310] md: md0 stopped.             
[    3.828549] md: bind<sdb2>                                                   
[    3.836041] md: bind<sda2>                                                   
[    3.847095] raid1: md0 is not clean -- starting background reconstruction    
[    3.853924] raid1: raid set md0 active with 2 out of 2 mirrors               
[    3.859966] md0: detected capacity change from 0 to 1999375812608            
mdadm: /dev/md/0 has been started with 2 drives.[    3.870374]  md0:            
 unknown partition table                                                        
Success: assembled all arrays.                                                  
done.                                                                           
done.                                                                           
Begin: Running /scripts/local-premount ... done.                                
[    5.042855] EXT4-fs (md0): mounted filesystem with ordered data mode         
Begin: Running /scripts/local-bottom ... done.                                  
done.                                                                           
Begin: Running /scripts/init-bottom ... done.                                   
INIT: version 2.88 booting                                                      
Using makefile-style concurrent boot in runlevel S.                             
Starting the hotplug events dispatcher: udevd[    6.269479] udev[186]: starting4
.                                                                               
Synthesizing the initial hotplug events...[    6.506583] udev[197]: renamed net1
done.                                                                           
Waiting for /dev to be fully populated...done.                                  
Generating udev events for MD arrays...done.                                    
Activating swap...[    7.532106] Adding 747932k swap on /dev/sdb3.  Priority:-1 
[    7.545930] Adding 747932k swap on /dev/sda3.  Priority:-2 extents:1 across: 
done.                                                                           
Checking root file system...fsck from util-linux-ng 2.17.2                      
e2fsck 1.41.12 (17-May-2010)                                                    
/dev/md0: clean, 24726/122036224 files, 7861995/488128860 blocks                
done.                                                                           
[    8.965897] md: resync of RAID array md0                                     
[    8.969895] md: minimum _guaranteed_  speed: 1000 KB/sec/disk.               
[    8.975779] md: using maximum available idle IO bandwidth (but not more than.
[    8.985220] md: using 128k window, over a total of 1952515442 blocks.        
[    8.991699] md: resuming resync of md0 from checkpoint.                      
[    9.336915] loop: module loaded                                              
Loading kernel modules...done.                                                  
Cleaning up ifupdown....                                                        
Setting up networking....                                                       
Activating lvm and md swap...done.                                              
Checking file systems...fsck from util-linux-ng 2.17.2                          
e2fsck 1.41.12 (17-May-2010)                                                    
/dev/sdb1: clean, 23/124992 files, 38270/250000 blocks                          
done.                                                                           
Mounting local filesystems...done.                                              
Activating swapfile swap...done.                                                
Cleaning up temporary files....                                                 
Setting kernel variables ...done.                                               
Configuring network interfaces...done.                                          
Starting portmap daemon....                                                     
Starting NFS common utilities: statd.                                           
Cleaning up temporary files....                                                 
INIT: Entering runlevel: 2                                                      
Using makefile-style concurrent boot in runlevel 2.                             
Starting portmap daemon...Already running..                                     
Starting NFS common utilities: statd.                                           
[   11.516293] RPC: Registered udp transport module.                            
[   11.521086] RPC: Registered tcp transport module.                            
[   11.525915] RPC: Registered tcp NFSv4.1 backchannel transport module.        
Starting enhanced syslogd: rsyslogd.                                            
Starting deferred execution scheduler: atd.                                     
[   12.109263] Installing knfsd (copyright (C) 1996 okir@monad.swb.de).         
[   12.643918] NET: Registered protocol family 10                               
[   12.653077] ADDRCONF(NETDEV_UP): eth1: link is not ready                     
[   12.660088] svc: failed to register lockdv1 RPC service (errno 97).          
[   12.675583] NFSD: Using /var/lib/nfs/v4recovery as the NFSv4 state recovery y
[   12.730501] NFSD: starting 90-second grace period                            
Starting periodic command scheduler: cron.                                      
Exporting directories for NFS kernel daemon....                                 
Starting NFS kernel daemon: nfsd mountd.                                        
Starting system message bus: dbus.                                              
Starting Samba daemons: nmbd smbd.                                              
Starting MTA:Starting internet superserver: inetd.                              
Starting MD monitoring service: mdadm --monitormdadm: No mail address or alert .
 failed!                                                                        
 exim4.                                                                         
Starting the Winbind daemon: winbind.                                           
Starting OpenBSD Secure Shell server: sshd.                                     
                                                                                
Debian GNU/Linux 6.0 JSHARE ttyS0                                               
                                                                                
JSHARE login: [   27.672260] eth1: link up, 100 Mb/s, full duplex, flow controld
[   27.679188] ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready                

</code>
                                                                                
==== Debian ====

You need to change the firmware content and will loose all the features and break your warrantly :
the u-boot need to be replaced
the nand partitions will be lost

# uname -ar
<code>
    Linux unassigned-hostname 2.6.32-5-kirkwood #1 Mon Oct 3 16:55:04 UTC 2011 armv5tel GNU/Linux
</code>

# cat /proc/cpuinfo
<code>
    Processor   : Feroceon 88FR131 rev 1 (v5l)
    BogoMIPS   : 1192.75
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
    
==== Recovery ====

You can recovery you nas by UART ( serial u-booting ) or by JTAG.
I have use the GuruPlug JTAG adapter that you can by directly at Globalscale Technology.
I have already tested with the Open JTAG sell by kernelconcept.

===== HOW-TO =====

==== BootStrap ====
The boot process is made in three steps :
  - u-boot start and configure the hardware components (bootcmd is started as a huge bootstrapping script collector)
  - u-boot checks the devices for boot.scr scripts and execute them if found (boot.scr load the Linux Kernel and ramdisk)
  - Linux boot and mount the root device (Debian is started by the master init process)

==== denx u-boot mod ====

apply the patch of this page by the command
<code>
$ patch -p1 -i nas6220.diff
</code>

(cross)compile the u-boot.kwb
<code>
$ export ARCH=arm
$ export CROSS_COMPILE=arm-linux-gnueabi- 
$ make mrproper
$ make ib6220_config
$ make u-boot.kwb
</code>

==== Stuff ====
:wiki:notes:nas6220.tar.gz|All the needed stuff...

:wiki:notes:debian-installer.tar.gz|

===== Notes =====

How To flash a firmware to Nand [1]

[1] www.openstora.com/wiki/index.php?title=How_to_install_your_custom_firmware

===== Refs =====

==== JTAG used ====

Genesi Debug Board (available at  [[https://newit.co.uk/shop/proddetail.php?prod=debug|NewIT]])

:wiki:notes:store_smarttop_debug.png|

OpenOCD JTAG (available at  [[http://shop.kernelconcepts.de/product_info.php?products_id=132|KernelConcept]])

:wiki:notes:openocd-jtag.jpeg|

GuruPlug JTAG Board (available at [[https://www.globalscaletechnologies.com/p-28-guruplug-jtag.aspx|GlobalScale]])

:wiki:notes:28.jpg|

===== TODO =====

==== Official OpenWrt Support ====


In Progress (Thanks to Luka Perkov) : [[http://patchwork.openwrt.org/patch/1970/|Patchwork [OpenWrt-Devel,4/5] add RaidSonic ICY BOX IB-NAS62x0 board]]

==== Official Denx U-Boot support ====

Done (Thanks to Luka Perkov) : [[http://lists.denx.de/pipermail/u-boot/2012-April/122597.html|[U-Boot] [PATCH v8] kirkwood: add NAS62x0 board support]]

[[http://git.denx.de/?p=u-boot/u-boot-marvell.git;a=commit;h=bbdbe3108da28dcd14dbff77473e6d5730ef5fc0|kirkwood: add NAS62x0 board support]]

:wiki:notes:capture.png|

UpStream :
http://lists.denx.de/pipermail/u-boot/2012-May/124403.html \\

==== Flash-kernel ====

<code>
test mtd-utils
cat /proc/mtd
</code>

<code>
test uImage and uInitrd
clear mtd 
</code>

//then update by reflash//

Adapting the flash-kernel script of Debian Squeeze

Debian’s flash-kernel script does not know the machine used here (“Marvell DB-88F6281-BP Development Board”) and refuses to install a new kernel. A simple patch helps. 
[[http://simon.baatz.info/downloads/flash-kernel.patch]]
==== Linux-kernel ====

<del>change mtd-parts (upstream)</del>

in progress (thanks to Simon Baatz)\\
soon upstream (3.5 ?)\\

[[https://git.kernel.org/?p=linux/kernel/git/next/linux-next.git;a=commit;h=f5520363532690f56e12126029864d9383d5203f||ARM: kirkwood: Add support for RaidSonic IB-NAS6210/6220 using devicetree]]

Stable now just need a small patch (runit.diff) from http://lists.infradead.org/pipermail/linux-arm-kernel/2012-June/103272.html

Here is a built package of the 3.5.1 (stable) kirkwood kernel.
::ib62x0:linux-kernel-custom.tar.gz|