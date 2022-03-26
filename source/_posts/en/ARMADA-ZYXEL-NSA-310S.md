---
title: 'ARMADA : ZYXEL NSA 310S'
lang: en
date: 2015-02-05 00:00:00
tags: ARM,ARMADA,NAS
---
====== ARMADA : ZYXEL NSA 310S ======

<code>The NS310S is a 88F6282 (ARMADA 300).
</code>

nsa310_front_400.jpg?direct&200
nsa310_rear_400.jpg?direct&200

===== Serial debug console =====

Make sure your cable is only outputting 3.3V.

''|*|-|*|*|*|'' –> pinout on the board: ''|GND|NC|RX|TX|VCC|''
=====   =====

<code>
G : N
TX : V
RX : B
</code>

<code>
$ minicom -D /dev/ttyUSB0

Bienvenue avec minicom 2.7

OPTIONS: I18n
Compilé le Jan  1 2014, 09:30:18.
Port /dev/ttyUSB0, 06:02:05

Tapez CTRL-A Z pour voir l'aide concernant les touches spéciales
</code>

===== Compile u-boot-3.6.0_STG315 from NSA310S_470AALH0C0 =====

Ask zyxel from NSA310S latest GPL source code

untar NSA310S_470AALH0C0.tar.gz

<code>
tar -zxf NSA310S_470AALH0C0.tar.gz
cd NSA310S_470AALH0C0
</code>

untar arm cross tool chain

<code>
tar -xvf sdk3.3-genericfs-arm-mv5sft.tar.gz
</code>

untar GPL sources code from build_NSA310S.tar.gz

<code>
tar -xvf build_NSA310S.tar.gz
</code>

copy u-boot from source code trunk

<code>
cp -R trunk/sysapps/u-boot-3.6.0_STG315 .
</code>

fix source code files (get them from u-boot-3.6.0_stg315-fix.tar.gz) and copy files into u-boot-3.6.0_STG315 
u-boot-3.6.0_stg315-fix.tar.gz

<code>
cd u-boot-3.6.0_STG315
</code>

fix arm cross tool chain path in building script by editing zyxel-install.sh

<file>
#!/bin/sh
export PATH=/usr/MATOS/ZYXEL/NSA310/zyxelco-GPL/FW4.70/NSA310S_470AALH0C0/sdk3.3-genericfs-arm-mv5sft/cross/bin:/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin:/usr/X11R6/bin:${HOME}/bin
export CROSS=arm-mv5sft-linux-gnueabi-
make mrproper
#make db88f6282bp_config SPIBOOT=1 DDR3=1 FREQ=533
make db88f6282bp_config NBOOT=1 DDR3=1 FREQ=533
make CROSS_COMPILE=/usr/MATOS/ZYXEL/NSA310/zyxelco-GPL/FW4.70/NSA310S_470AALH0C0/sdk3.3-genericfs-arm-mv5sft/cross/bin/arm-mv5sft-linux-gnueabi-
</file>

build u-boot binaries

<code>
./zyxel-install.sh
</code>

===== Boot Factory u-boot =====

<code>
         __  __                      _ _
        |  \/  | __ _ _ ____   _____|   |
        |   |\/|   |/ _` | '__

/ / _
|   |
        |   |   | (_|   |
V /  __/ |   |
        |_|   |_|\__,_|_|    \_/ \___|_|_|
 _   _     ____              _
|   |   | __ )  ___   ___ |   |_
|   |   |___|  _
/ _
/ _ \| __|
|   |_|   |___|   |_) | (_) | (_) |   |_
 \___/    |____/ \___/ \___/ \__|
 ** MARVELL BOARD: DB6702A-GMtech LE

U-Boot 1.1.4 (May 28 2013 - 16:07:08) Marvell version: 3.6.0

U-Boot code: 00600000 -> 0067FFF0  BSS: -> 006CFB00

Soc: 88F6702 A1 CPU running @ 1000Mhz L2 running @ 500Mhz
SysClock = 400Mhz , TClock = 166Mhz

DRAM (DDR2) CAS Latency = 5 tRP = 5 tRAS = 18 tRCD=6
DRAM CS[0] base 0x00000000   size 256MB
DRAM Total size 256MB  16bit width
Addresses 10M - 0M are saved for the U-Boot usage.
Mem malloc Initialization (10M - 7M): Done
NAND:128 MB
Flash:  0 kB

CPU : Marvell Feroceon (Rev 1)
Kernel address is 0xc80000.

Streaming disabled
Write allocate disabled

USB 0: host mode
PEX 0: interface detected no Link.
Net:   egiga0 [PRIME]
Hit any key to stop autoboot:  0
Marvell>>
Marvell>> version

U-Boot 1.1.4 (May 28 2013 - 16:07:08) Marvell version: 3.6.0
</code>

===== Load official compiled u-boot =====

<code>
Marvell>> usb reset
(Re)start USB...
USB:   scanning bus for devices... 3 USB Device(s) found
Waiting for storage device(s) to settle before scanning...
1 Storage Device(s) found
Marvell>> fatls usb 0:1
   475592   u-boot-db88f6282bp_533ddr3db_nand.bin
   475592   u-boot.bin

2 file(s), 2 dir(s)

Marvell>> fatload usb 0:1 0x00800000 u-boot.bin
reading u-boot.bin
..............................................

475592 bytes read
</code>

===== Chain to loaded u-boot =====

<code>
Marvell>> go 0x800200
## Starting application at 0x00800200 ...
         __  __                      _ _
        |  \/  | __ _ _ ____   _____|   |
        |   |\/|   |/ _` | '__

/ / _
|   |
        |   |   | (_|   |
V /  __/ |   |
        |_|   |_|\__,_|_|    \_/ \___|_|_|
 _   _     ____              _
|   |   | __ )  ___   ___ |   |_
|   |   |___|  _
/ _
/ _ \| __|
|   |_|   |___|   |_) | (_) | (_) |   |_
 \___/    |____/ \___/ \___/ \__|
 ** MARVELL BOARD: DB-88F6282A-BP LE

U-Boot 1.1.4 (Feb  5 2015 - 05:38:58) Marvell version: 3.6.0

U-Boot code: 00600000 -> 0067FFF0  BSS: -> 006CFB00

Soc: 88F6702 A1 CPU running @ 1000Mhz L2 running @ 500Mhz
SysClock = 400Mhz , TClock = 166Mhz

DRAM (DDR2) CAS Latency = 5 tRP = 5 tRAS = 18 tRCD=6
DRAM CS[0] base 0x00000000   size 256MB
DRAM Total size 256MB  16bit width
Addresses 10M - 0M are saved for the U-Boot usage.
Mem malloc Initialization (10M - 7M): Done
NAND:128 MB
Flash:  0 kB

CPU : Marvell Feroceon (Rev 1)
Kernel address is 0xc80000.

Streaming disabled
Write allocate disabled

USB 0: host mode
PEX 0: interface detected no Link.
Net:   egiga0 [PRIME]
Hit any key to stop autoboot:  0
Marvell>> version

U-Boot 1.1.4 (Feb  5 2015 - 05:38:58) Marvell version: 3.6.0
</code>

===== Références =====

[[https://github.com/psch2/uboot-nsa320|U-Boot for ZyXEL NSA320 2-Bay Power Media Server ]]

[[https://github.com/PlanetEater/uboot-nsa320|Updated U-Boot for ZyXEL NSA320 2-Bay Power Media Server]]

===== U-Boot (factory) Help & Env =====

<code>
         __  __                      _ _
        |  \/  | __ _ _ ____   _____|   |
        |   |\/|   |/ _` | '__

/ / _
|   |
        |   |   | (_|   |
V /  __/ |   |
        |_|   |_|\__,_|_|    \_/ \___|_|_|
 _   _     ____              _
|   |   | __ )  ___   ___ |   |_
|   |   |___|  _
/ _
/ _ \| __|
|   |_|   |___|   |_) | (_) | (_) |   |_
 \___/    |____/ \___/ \___/ \__|
 ** MARVELL BOARD: DB6702A-GMtech LE

U-Boot 1.1.4 (May 28 2013 - 16:07:08) Marvell version: 3.6.0

U-Boot code: 00600000 -> 0067FFF0  BSS: -> 006CFB00

Soc: 88F6702 A1 CPU running @ 1000Mhz L2 running @ 500Mhz
SysClock = 400Mhz , TClock = 166Mhz

DRAM (DDR2) CAS Latency = 5 tRP = 5 tRAS = 18 tRCD=6
DRAM CS[0] base 0x00000000   size 256MB
DRAM Total size 256MB  16bit width
Addresses 10M - 0M are saved for the U-Boot usage.
Mem malloc Initialization (10M - 7M): Done
NAND:128 MB
Flash:  0 kB

CPU : Marvell Feroceon (Rev 1)
Kernel address is 0xc80000.

Streaming disabled
Write allocate disabled

USB 0: host mode
PEX 0: interface detected no Link.
Net:   egiga0 [PRIME]
Hit any key to stop autoboot:  0
Marvell>> help
?       - alias for 'help'
SatR - sample at reset sub-system, relevent for DB only
base    - print or set address offset
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootext2    dev:boot_part1,boot_part2 addr boot_image linux_dev_name
bootm   - boot application image from memory
bootp    - boot image via network using BootP/TFTP protocol
bubt    - Burn an image on the Boot Nand Flash.
chpart    - change active partition
cmp     - memory compare
cmpm    - Compare Memory
cp      - memory copy
cpumap - Display CPU memory mapping settings.
crc32   - checksum calculation
date    - get/set/reset date & time
dclk    - Display the MV device CLKs.
dhcp    - invoke DHCP client to obtain IP/boot params
diskboot- boot from IDE device
echo    - echo args to console
eeprom  - EEPROM sub-system
erase   - erase FLASH memory
ext2load- load binary file from a Ext2 filesystem
ext2ls  - list files in a directory (default /)
fatinfo - print information about filesystem
fatload - load binary file from a dos filesystem
fatls   - list files in a directory (default /)
fi    - Find value in the memory.
flinfo  - print FLASH memory information
fsinfo    - print information about filesystems
fsload    - load binary file from a filesystem image
g    - start application at cached address 'addr'(default addr 0x40000)
go      - start application at address 'addr'
help    - print online help
icrc32  - checksum calculation
ide     - IDE sub-system
iloop   - infinite loop on address range
imd     - i2c memory display
iminfo  - print header information for application image
imm[.b, .s, .w, .l]     - i2c memory modify (auto-incrementing)
imw     - memory write (fill)
inm     - memory modify (constant address)
iprobe  - probe to discover valid I2C chip addresses
ir    - reading and changing MV internal register values.
loop    - infinite loop on address range
ls    - list files in a directory (default /)
map    - Diasplay address decode windows
md      - memory display
me    - PCI master enable
mm      - memory modify (auto-incrementing)
mmcinit - init mmc card
mp    - map PCI BAR
mtdparts- define flash/nand partitions
mtest   - simple RAM test
mw      - memory write (fill)
nand                   - NAND sub-system
nboot   - boot from NAND device
nbubt    - Burn a boot loader image on the Boot Nand Flash.
nm      - memory modify (constant address)
pci     - list and access PCI Configuration Space
phyRead    - Read PCI-E Phy register
pciePhyWrite    - Write PCI-E Phy register
phyRead    - Read Phy register
phyWrite    - Write Phy register
ping    - send ICMP ECHO_REQUEST to network host
printenv- print environment variables
printinfo- print environment variables
protect - enable or disable FLASH write protection
rarpboot- boot image via network using RARP/TFTP protocol
rcvr    - Satrt recovery process (Distress Beacon with TFTP server)
reset   - Perform RESET of the CPU
resetenv    - Return all environment variable to default.
run     - run commands in an environment variable
saveenv - save environment variables to persistent storage
saveinfo - save environment variables to persistent storage
se    - PCI Slave enable
setenv  - set environment variables
setinfo  - set environment variables
sflash    - read, write or erase the external SPI Flash.
sg    - scanning the PHYs status
sp    - Scan PCI bus.
switchRegRead    - Read switch register
switchRegWrite    - Write switch register
Temp    - read chip Tj temp
tftpboot- boot image via network using TFTP protocol
usb     - USB sub-system
usbboot - boot from USB device
version - print monitor version
Marvell>> printenv
bootargs=console=ttyS0,115200 mtdparts=nand_mtd:0x100000(uboot),0x80000(uboot_env),0x80000(key_store),0x80000(info),0xA00000(etc),0xA00000(kernel_1),0x2FC0000(rootfs1),0xA00000(kernel_2),0x2FC0000(rootfs2) root=/dev/nfs rw init=/init
bootcmd=nand read.e 0x2000000 $(kernel_addr) 0xA00000; bootm 0x2000000
bootdelay=2
baudrate=115200
loads_echo=0
ipaddr=10.4.52.165
serverip=10.4.52.7
rootpath=/srv/ubuntu
netmask=255.255.255.0
nandEcc=1bit
MODEL_ID=AD03
PRODUCT_NAME=STG-315
FEATURE_BIT=00
CONTRY_TYPE=FF
VENDOR_NAME=MitraStar Technology Corp.
run_diag=yes
ethaddr=4C:9E:FF:BF:7A:EB
stdin=serial
stdout=serial
stderr=serial
console=console=ttyS0,115200 mtdparts=nand_mtd:0xc0000@0(uboot)ro,0x7f00000@0x100000(root)
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
ethprime=egiga0
netbsd_en=no
vxworks_en=no
bootargs_root=root=/dev/nfs rw
bootargs_end=:::DB88FXX81:eth0:none
image_name=uImage
standalone=fsload 0x2000000 $(image_name);setenv bootargs $(console) root=/dev/mtdblock0 rw ip=$(ipaddr):$(serverip)$(bootargs_end) $(mvPhoneConfig); bootm 0x2000000;
disaMvPnp=no
ethmtu=1500
mvPhoneConfig=mv_phone_config=dev[0]:fxs,dev[1]:fxo
mvNetConfig=mv_net_config=(00:11:88:0f:62:81,0:1:2:3),mtu=1500
usb0Mode=host
yuk_ethaddr=00:00:00:EE:51:81
netretry=no
rcvrip=169.254.100.100
loadaddr=0x02000000
autoload=no
image_multi=yes
enaAutoRecovery=yes
kernel_addr=0xc80000
pcieTune=no
ethact=egiga0

Environment size: 1509/131068 bytes
Marvell>>
</code>

===== Liste des ZyXel et compatibles =====

^MODEL_ID ^PRODUCT_NAME |
|D401 |NSA210 |
|D501 |NSA220 |
|DC01 |NSA221 |
|DA01 |NSA310_TDC |
|A203 |NSA310_ZyXEL |
|DD01 |NSA320 |
|AA03 |NSA325 |
|A403 |STG100 |
|A803 |STG211 |
|AB03 |STG212 |
|AE03 |NSA325v2 |
|AD03 |STG-315 |

===== DB6702A-GMtech boards =====

  * ZyXEL NSA310S
  * ZyXEL NSA320S
  * DLINK DNS-320 B2
  * LaCie CloudBox

===== MitraStar Technology Corp.- STG-315 =====

ZyXEL - NSA310S

<code>
/ # cat /etc/modelname
NSA310S
</code>

Marvell Development Board (LSP Version KW_LSP_5.1.3_patch30)– DB-88F6702A-BPE

<code>
/ # cat /proc/cpuinfo
Processor       : Feroceon 88FR131 rev 1 (v5l)
BogoMIPS        : 992.87
Features        : swp half thumb fastmult edsp
CPU implementer : 0x56
CPU architecture: 5TE
CPU variant     : 0x2
CPU part        : 0x131
CPU revision    : 1

Hardware        : Feroceon-KW
Revision        : 0000
Serial          : 0000000000000000
</code>

DB-88F6702A-BP

<code>
/ # cat /proc/board_type
DB-88F6702A-BP
</code>

NAND MTDPARTS

<code>
/ # cat /proc/mtd
dev:    size   erasesize  name
mtd0: 00100000 00020000 "uboot"
mtd1: 00080000 00020000 "uboot_env"
mtd2: 00080000 00020000 "key_store"
mtd3: 00080000 00020000 "info"
mtd4: 00a00000 00020000 "etc"
mtd5: 00a00000 00020000 "kernel_1"
mtd6: 02fc0000 00020000 "rootfs1"
mtd7: 00a00000 00020000 "kernel_2"
mtd8: 02fc0000 00020000 "rootfs2"
</code>

<code>
/ # cat /etc/fw_env.config
# Configuration file for fw_(printenv/saveenv) utility.
# Up to two entries are valid, in this case the redundand
# environment sector is assumed present.
# Notice, that the "Number of sectors" is ignored on NOR.

# MTD device name       Device offset   Env. size       Flash sector size       Number of sectors
# NAND example
/dev/mtd1               0x0000          0x20000         0x20000                 4
</code>

<code>
/ # fw_printenv
bootargs=console=ttyS0,115200 mtdparts=nand_mtd:0x100000(uboot),0x80000(uboot_env),0x80000(key_store),0x80000(info),0xA00000(etc),0xA00000(kernel_1),0x2FC0000(rootfs1),0xA00000(kernel_2),0x2FC0000(rootfs2) root=/dev/nfs rw init=/init
bootcmd=nand read.e 0x2000000 $(kernel_addr) 0xA00000; bootm 0x2000000
bootdelay=2
baudrate=115200
loads_echo=0
ipaddr=10.4.52.165
serverip=10.4.52.7
rootpath=/srv/ubuntu
netmask=255.255.255.0
nandEcc=1bit
kernel_addr=C80000
MODEL_ID=AD03
PRODUCT_NAME=STG-315
FEATURE_BIT=00
CONTRY_TYPE=FF
VENDOR_NAME=MitraStar Technology Corp.
run_diag=yes
ethaddr=4C:9E:FF:BF:7A:EB
</code>

<code>
/ # cat /etc/info_env.config
# Configuration file for fw_(printenv/saveenv) utility.
# Up to two entries are valid, in this case the redundand
# environment sector is assumed present.

# Notice, that the "Number of sectors" is ignored on NOR.
# MTD device name       Device offset   Env. size       Flash sector size       Number of sectors
# NAND example
/dev/mtd3               0x0000          0x20000         0x20000                 4
</code>

<code>
/ # strings /dev/mtd3
-skernel_addr_1=0xc80000
kernel_mtd_1=5
sysimg_mtd_1=6
kernel_addr_2=0x4640000
kernel_mtd_2=7
sysimg_mtd_2=8
fwversion_1=V4.70(AALH.0)
revision_1=41128
modelid_1=AD03
core_checksum_1=54a9748949a91673b27122b78973179d
zld_checksum_1=e6731ee8684c55c19bca33ee639b1653
romfile_checksum_1=4C30
img_checksum_1=5864cff5e093b4fa85684dc449558ace
fwversion_2=V4.70(AALH.0)
revision_2=41128
modelid_2=AD03
core_checksum_2=54a9748949a91673b27122b78973179d
zld_checksum_2=e6731ee8684c55c19bca33ee639b1653
romfile_checksum_2=4C30
img_checksum_2=5864cff5e093b4fa85684dc449558ace
next_bootfrom=1
curr_bootfrom=1
</code>

\\