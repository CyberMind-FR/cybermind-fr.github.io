---
title: MochaBin-5G@GlobalScaleTechnologies - First Flash
lang: en
date: 2022-03-21 17:07:07
tags: MOCHAbin armada
---

I prefer my own method to flash from u-boot, than the one from the commit!

<details>
  <summary>Click to expand first Flash to master OpenWrt from factory U-Boot...</summary>
```
Marvell>> usb reset
resetting USB...
USB0:   Register 2000120 NbrPorts 2
Starting the controller
USB XHCI 1.00
USB1:   Register 2000120 NbrPorts 2
Starting the controller
USB XHCI 1.00
scanning bus 0 for devices... cannot reset port 2!?
3 USB Device(s) found
scanning bus 1 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 0 Storage Device(s) found

Marvell>> mmc list
sdhci@6e0000: 0
Marvell>> mmc dev 0 0
switch to partitions #0, OK
mmc0(part 0) is current device
Marvell>> mmc info
Device: sdhci@6e0000
Manufacturer ID: 45
OEM: 100
Name: DF401
Bus Speed: 52000000
Mode : MMC High Speed (52MHz)
Rd Block Len: 512
MMC version 5.1
High Capacity: Yes
Capacity: 14.7 GiB
Bus Width: 4-bit
Erase Group Size: 512 KiB
HC WP Group Size: 8 MiB
User Capacity: 14.7 GiB WRREL
Boot Capacity: 4 MiB ENH
RPMB Capacity: 4 MiB ENH

Marvell>> usb reset
resetting USB...
USB0:   Register 2000120 NbrPorts 2
Starting the controller
USB XHCI 1.00
USB1:   Register 2000120 NbrPorts 2
Starting the controller
USB XHCI 1.00
scanning bus 0 for devices... 4 USB Device(s) found
scanning bus 1 for devices... 1 USB Device(s) found
       scanning usb for storage devices... 1 Storage Device(s) found
Marvell>> fatls usb 0
            20220316/

0 file(s), 1 dir(s)

Marvell>> fatls usb 0 20220316/
            ./
            ../
 21166088   openwrt-mvebu-cortexa72-globalscale_mochabin-initramfs-kernel.bin
  9199041   openwrt-mvebu-cortexa72-globalscale_mochabin-ext4-sdcard.img.gz
  8273433   openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz

3 file(s), 2 dir(s)

Marvell>>

Marvell>> load usb 0:1 $kernel_addr_r 20220316/openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz
8273433 bytes read in 113 ms (69.8 MiB/s)
Marvell>> gzwrite mmc 0 $kernel_addr_r $filesize

22020096/570425344
        uncompressed 22043806 of 570425344
        crcs == 0x00000000/0x870497c0
Marvell>> mmc part

Partition Map for MMC device 0  --   Partition Type: DOS

Part    Start Sector    Num Sectors     UUID            Type
  1     2048            33280           56839e07-01     83 Boot
  2     36864           213504          56839e07-02     83
Marvell>>

Marvell>> env default -a
## Resetting to default environment
SF: Detected w25q32bv with page size 256 Bytes, erase size 4 KiB, total 4 MiB

Marvell>> setenv bootcmd 'load mmc 0 ${loadaddr} boot.scr && source ${loadaddr}'
Marvell>> setenv console 'console=ttyS0,115200'
Marvell>> saveenv
Saving Environment to SPI Flash... Erasing SPI flash...Writing to SPI flash...done
OK
```
</details>

<details>
  <summary>Click to expand first login to factory Ubuntu with some few commands...</summary>
```
BootROM - 2.03
Starting CP-0 IOROM 1.07
Booting from SPI NOR flash 1 (0x32)
Found valid image at boot postion 0x000
lmv_ddr: mv_ddr-devel-18.12.0-g2e20f5d (Dec 30 2021 - 16:08:48)
mv_ddr: scrubbing memory...
mv_ddr: completed successfully
BL2: Initiating SCP_BL2 transfer to SCP


U-Boot 2018.03-devel-18.12.3-ga49bd540df (Dec 30 2021 - 16:06:18 +0800)

Model: Marvell Armada 7040 Mochabin development board
SoC: Armada7040-B0; AP806-B0; CP115-A0
Clock:  CPU     1400 [MHz]
        DDR     800  [MHz]
        FABRIC  800  [MHz]
        MSS     200  [MHz]
LLC Enabled (Exclusive Mode)
DRAM:  8 GiB
Bus spi@700680 CS0 configured for direct access 00000000f9000000:0x1000000
SF: Detected w25q32bv with page size 256 Bytes, erase size 4 KiB, total 4 MiB
EEPROM configuration pattern not detected.
Comphy chip #0:
Comphy-0: SGMII1        3.125 Gbps
Comphy-1: USB3_HOST0
Comphy-2: SATA0
Comphy-3: SATA1
Comphy-4: SFI0          10.3125 Gbps
Comphy-5: PEX2
UTMI PHY 0 initialized to USB Host0
UTMI PHY 1 initialized to USB Host1
SATA link 0 timeout.
Target spinup took 0 ms.
AHCI 0001.0000 32 slots 2 ports 6 Gbps 0x3 impl SATA mode
flags: 64bit ncq led only pmp fbss pio slum part sxs
PCIE-0: Link down
MMC:   sdhci@6e0000: 0
Loading Environment from SPI Flash... OK
Model: Marvell Armada 7040 Mochabin development board
Net:   eth0: mvpp2-0 [PRIME], eth1: mvpp2-1, eth2: mvpp2-2
Hit any key to stop autoboot:  0
576 bytes read in 9 ms (62.5 KiB/s)
## Executing script at 06000000
switch to partitions #0, OK
mmc0(part 0) is current device
24275 bytes read in 12 ms (1.9 MiB/s)
11859976 bytes read in 871 ms (13 MiB/s)
## Flattened Device Tree blob at 06f00000
   Booting using the fdt blob at 0x6f00000
   Using Device Tree in place at 0000000006f00000, end 0000000006f08ed2

Starting kernel ...

[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd081]
[    0.000000] Linux version 5.10.104 (builder@buildhost) (aarch64-openwrt-linux-musl-gcc (OpenWrt GCC 11.2.0 r19124-832b90216f) 11.2.0, GNU ld (GNU Binutils) 2.37) #0 SMP Tue Mar 15 23:48:24 2022
[    0.000000] Machine model: Globalscale MOCHAbin
[    0.000000] Zone ranges:
[    0.000000]   DMA      [mem 0x0000000000000000-0x00000000ffffffff]
[    0.000000]   DMA32    empty
[    0.000000]   Normal   [mem 0x0000000100000000-0x000000023fffffff]
[    0.000000] Movable zone start for each node
[    0.000000] Early memory node ranges
[    0.000000]   node   0: [mem 0x0000000000000000-0x0000000003ffffff]
[    0.000000]   node   0: [mem 0x0000000004000000-0x00000000041fffff]
[    0.000000]   node   0: [mem 0x0000000004200000-0x00000000bfffffff]
[    0.000000]   node   0: [mem 0x0000000100000000-0x000000023fffffff]
[    0.000000] Initmem setup node 0 [mem 0x0000000000000000-0x000000023fffffff]
[    0.000000] psci: probing for conduit method from DT.
[    0.000000] psci: PSCIv1.1 detected in firmware.
[    0.000000] psci: Using standard PSCI v0.2 function IDs
[    0.000000] psci: MIGRATE_INFO_TYPE not supported.
[    0.000000] psci: SMC Calling Convention v1.1
[    0.000000] percpu: Embedded 16 pages/cpu s27672 r8192 d29672 u65536
[    0.000000] Detected PIPT I-cache on CPU0
[    0.000000] CPU features: detected: Spectre-v2
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2064384
[    0.000000] Kernel command line: root=PARTUUID=56839e07-02 rw rootwait console=ttyS0,115200
[    0.000000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[    0.000000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0x00000000bc000000-0x00000000c0000000] (64MB)
[    0.000000] Memory: 8164940K/8388608K available (8062K kernel code, 894K rwdata, 2092K rodata, 448K init, 284K bss, 223668K reserved, 0K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] rcu: Hierarchical RCU implementation.
[    0.000000]  Tracing variant of Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 10 jiffies.
[    0.000000] NR_IRQS: 64, nr_irqs: 64, preallocated irqs: 0
[    0.000000] GIC: Adjusting CPU interface base to 0x00000000f022f000
[    0.000000] GIC: Using split EOI/Deactivate mode
[    0.000000] GICv2m: DT overriding V2M MSI_TYPER (base:160, num:32)
[    0.000000] GICv2m: range[mem 0xf0280000-0xf0280fff], SPI[160:191]
[    0.000000] GICv2m: DT overriding V2M MSI_TYPER (base:192, num:32)
[    0.000000] GICv2m: range[mem 0xf0290000-0xf0290fff], SPI[192:223]
[    0.000000] GICv2m: DT overriding V2M MSI_TYPER (base:224, num:32)
[    0.000000] GICv2m: range[mem 0xf02a0000-0xf02a0fff], SPI[224:255]
[    0.000000] GICv2m: DT overriding V2M MSI_TYPER (base:256, num:32)
[    0.000000] GICv2m: range[mem 0xf02b0000-0xf02b0fff], SPI[256:287]
[    0.000000] random: get_random_bytes called from start_kernel+0x3a0/0x4e4 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 25.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c40939b5, max_idle_ns: 440795202646 ns
[    0.000002] sched_clock: 56 bits at 25MHz, resolution 40ns, wraps every 4398046511100ns
[    0.000083] Calibrating delay loop (skipped), value calculated using timer frequency.. 50.00 BogoMIPS (lpj=250000)
[    0.000091] pid_max: default: 32768 minimum: 301
[    0.000208] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.000265] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.000954] rcu: Hierarchical SRCU implementation.
[    0.001018] dyndbg: Ignore empty _ddebug table in a CONFIG_DYNAMIC_DEBUG_CORE build
[    0.001196] smp: Bringing up secondary CPUs ...
[    0.001522] Detected PIPT I-cache on CPU1
[    0.001559] CPU1: Booted secondary processor 0x0000000001 [0x410fd081]
[    0.001912] Detected PIPT I-cache on CPU2
[    0.001942] CPU2: Booted secondary processor 0x0000000100 [0x410fd081]
[    0.002296] Detected PIPT I-cache on CPU3
[    0.002317] CPU3: Booted secondary processor 0x0000000101 [0x410fd081]
[    0.002357] smp: Brought up 1 node, 4 CPUs
[    0.002369] SMP: Total of 4 processors activated.
[    0.002374] CPU features: detected: 32-bit EL0 Support
[    0.002378] CPU features: detected: CRC32 instructions
[    0.002414] CPU features: emulated: Privileged Access Never (PAN) using TTBR0_EL1 switching
[    0.002419] CPU: All CPU(s) started at EL2
[    0.002434] alternatives: patching kernel code
[    0.004821] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 19112604462750000 ns
[    0.004832] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.004901] pinctrl core: initialized pinctrl subsystem
[    0.005531] NET: Registered protocol family 16
[    0.005948] DMA: preallocated 1024 KiB GFP_KERNEL pool for atomic allocations
[    0.006154] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA pool for atomic allocations
[    0.006357] DMA: preallocated 1024 KiB GFP_KERNEL|GFP_DMA32 pool for atomic allocations
[    0.006566] thermal_sys: Registered thermal governor 'step_wise'
[    0.006999] cpuidle: using governor ladder
[    0.007047] ASID allocator initialised with 65536 entries
[    0.019486] cryptd: max_cpu_qlen set to 1000
[    0.020585] SCSI subsystem initialized
[    0.020790] usbcore: registered new interface driver usbfs
[    0.020812] usbcore: registered new interface driver hub
[    0.020832] usbcore: registered new device driver usb
[    0.021389] clocksource: Switched to clocksource arch_sys_counter
[    0.021702] NET: Registered protocol family 2
[    0.022168] IP idents hash table entries: 131072 (order: 8, 1048576 bytes, linear)
[    0.024467] tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
[    0.024532] TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.024828] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    0.025441] TCP: Hash tables configured (established 65536 bind 65536)
[    0.025537] UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    0.025651] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    0.025852] NET: Registered protocol family 1
[    0.025870] PCI: CLS 0 bytes, default 64
[    0.026495] workingset: timestamp_bits=46 max_order=21 bucket_order=0
[    0.028232] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.028238] jffs2: version 2.2 (NAND) (SUMMARY) (LZMA) (RTIME) (CMODE_PRIORITY) (c) 2001-2006 Red Hat, Inc.
[    0.028695] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 250)
[    0.030160] armada-ap806-pinctrl f06f4000.system-controller:pinctrl: registered pinctrl driver
[    0.030555] armada-cp110-pinctrl f2440000.system-controller:pinctrl: registered pinctrl driver
[    0.032976] mv_xor_v2 f0400000.xor: Marvell Version 2 XOR driver
[    0.033433] mv_xor_v2 f0420000.xor: Marvell Version 2 XOR driver
[    0.033889] mv_xor_v2 f0440000.xor: Marvell Version 2 XOR driver
[    0.034370] mv_xor_v2 f0460000.xor: Marvell Version 2 XOR driver
[    0.034876] mv_xor_v2 f26a0000.xor: Marvell Version 2 XOR driver
[    0.035350] mv_xor_v2 f26c0000.xor: Marvell Version 2 XOR driver
[    0.035486] Serial: 8250/16550 driver, 16 ports, IRQ sharing enabled
[    0.036602] printk: console [ttyS0] disabled
[    0.036651] f0512000.serial: ttyS0 at MMIO 0xf0512000 (irq = 16, base_baud = 12500000) is a 16550A
[    0.722327] printk: console [ttyS0] enabled
[    0.727056] f2702000.serial: ttyS1 at MMIO 0xf2702000 (irq = 33, base_baud = 15625000) is a 16550A
[    0.736461] omap_rng f2760000.trng: Random Number Generator ver. 203b34c
[    0.736774] random: fast init done
[    0.746639] random: crng init done
[    0.751638] loop: module loaded
[    0.754812] Loading iSCSI transport class v2.0-870.
[    0.760547] ahci f2540000.sata: supply ahci not found, using dummy regulator
[    0.767713] ahci f2540000.sata: supply phy not found, using dummy regulator
[    0.774927] platform f2540000.sata:sata-port@0: supply target not found, using dummy regulator
[    0.784873] spi-nor spi2.0: w25q32 (4096 Kbytes)
[    0.789608] 3 fixed-partitions partitions found on MTD device spi2.0
[    0.795999] Creating 3 MTD partitions on "spi2.0":
[    0.800810] 0x000000000000-0x0000003e0000 : "u-boot"
[    0.806007] 0x0000003e0000-0x0000003f0000 : "hw-info"
[    0.811219] 0x0000003f0000-0x000000400000 : "u-boot-env"
[    0.818669] hwmon hwmon0: temp1_input not attached to any thermal zone
[    0.827799] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    0.890127] hwmon hwmon1: temp1_input not attached to any thermal zone
[    0.902128] hwmon hwmon2: temp1_input not attached to any thermal zone
[    0.913921] hwmon hwmon3: temp1_input not attached to any thermal zone
[    0.925714] hwmon hwmon4: temp1_input not attached to any thermal zone
[    0.941291] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    0.955489] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.962053] ehci-pci: EHCI PCI platform driver
[    0.966542] ehci-platform: EHCI generic platform driver
[    0.971892] ehci-orion: EHCI orion driver
[    0.976236] xhci-hcd f2510000.usb3: xHCI Host Controller
[    0.981589] xhci-hcd f2510000.usb3: new USB bus registered, assigned bus number 1
[    0.989163] xhci-hcd f2510000.usb3: hcc params 0x0a000990 hci version 0x100 quirks 0x0000000000010010
[    0.998451] xhci-hcd f2510000.usb3: irq 37, io mem 0xf2510000
[    1.004511] hub 1-0:1.0: USB hub found
[    1.008288] hub 1-0:1.0: 1 port detected
[    1.012331] xhci-hcd f2510000.usb3: xHCI Host Controller
[    1.017669] xhci-hcd f2510000.usb3: new USB bus registered, assigned bus number 2
[    1.025195] xhci-hcd f2510000.usb3: Host supports USB 3.0 SuperSpeed
[    1.031606] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    1.039869] hub 2-0:1.0: USB hub found
[    1.043671] hub 2-0:1.0: 1 port detected
[    1.047841] usbcore: registered new interface driver usb-storage
[    1.054100] armada38x-rtc f2284000.rtc: registered as rtc0
[    1.059624] armada38x-rtc f2284000.rtc: setting system clock to 2022-03-17T12:49:12 UTC (1647521352)
[    1.068850] i2c /dev entries driver
[    1.072854] pca953x 0-0039: supply vcc not found, using dummy regulator
[    1.079548] pca953x 0-0039: using no AI
[    1.099327] sdhci: Secure Digital Host Controller Interface driver
[    1.105573] sdhci: Copyright(c) Pierre Ossman
[    1.110159] sdhci-pltfm: SDHCI platform and OF driver helper
[    1.123162] NET: Registered protocol family 10
[    1.128038] Segment Routing with IPv6
[    1.131762] NET: Registered protocol family 17
[    1.136246] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    1.141532] mmc0: SDHCI controller on f06e0000.sdhci [f06e0000.sdhci] using ADMA 64-bit
[    1.157611] 8021q: 802.1Q VLAN Support v1.8
[    1.164512] armada8k-pcie f2640000.pcie: host bridge /cp0/pcie@f2640000 ranges:
[    1.171915] armada8k-pcie f2640000.pcie:      MEM 0x00f8000000..0x00f8efffff -> 0x00f8000000
[    1.227429] mmc0: new high speed MMC card at address 0001
[    1.233711] mmcblk0: mmc0:0001 DF4016 14.7 GiB
[    1.238698] mmcblk0boot0: mmc0:0001 DF4016 partition 1 4.00 MiB
[    1.244917] mmcblk0boot1: mmc0:0001 DF4016 partition 2 4.00 MiB
[    1.250924] mmcblk0rpmb: mmc0:0001 DF4016 partition 3 4.00 MiB, chardev (248:0)
[    1.259425]  mmcblk0: p1 p2
[    2.171413] armada8k-pcie f2640000.pcie: Phy link never came up
[    2.177381] armada8k-pcie f2640000.pcie: Link not up after reconfiguration
[    2.184486] armada8k-pcie f2640000.pcie: PCI host bridge to bus 0000:00
[    2.191147] pci_bus 0000:00: root bus resource [bus 00-ff]
[    2.196689] pci_bus 0000:00: root bus resource [mem 0xf8000000-0xf8efffff]
[    2.203665] pci 0000:00:00.0: [11ab:0110] type 01 class 0x060400
[    2.209730] pci 0000:00:00.0: reg 0x10: [mem 0x00000000-0x000fffff]
[    2.216146] pci 0000:00:00.0: supports D1 D2
[    2.220449] pci 0000:00:00.0: PME# supported from D0 D1 D3hot
[    2.231837] pci 0000:00:00.0: BAR 0: assigned [mem 0xf8000000-0xf80fffff]
[    2.238676] pci 0000:00:00.0: PCI bridge to [bus 01-ff]
[    2.807920] pcieport 0000:00:00.0: AER: enabled with IRQ 43
[    2.814119] ahci f2540000.sata: supply ahci not found, using dummy regulator
[    2.821331] ahci f2540000.sata: supply phy not found, using dummy regulator
[    2.828469] platform f2540000.sata:sata-port@0: supply target not found, using dummy regulator
[    2.837716] platform f2540000.sata:sata-port@1: supply target not found, using dummy regulator
[    2.848802] ahci f2540000.sata: masking port_map 0x3 -> 0x3
[    2.854497] ahci f2540000.sata: AHCI 0001.0000 32 slots 2 ports 6 Gbps 0x3 impl platform mode
[    2.863082] ahci f2540000.sata: flags: 64bit ncq sntf led only pmp fbs pio slum part sxs
[    2.872124] scsi host0: ahci
[    2.875304] scsi host1: ahci
[    2.878305] ata1: SATA max UDMA/133 mmio [mem 0xf2540000-0xf256ffff] port 0x100 irq 44
[    2.886272] ata2: SATA max UDMA/133 mmio [mem 0xf2540000-0xf256ffff] port 0x180 irq 44
[    2.895496] sfp sfp-eth0: Host maximum power 1.0W
[    2.903358] sfp sfp-eth2: Host maximum power 1.0W
[    2.911642] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    2.971470] hwmon hwmon1: temp1_input not attached to any thermal zone
[    2.982872] hwmon hwmon2: temp1_input not attached to any thermal zone
[    2.993976] hwmon hwmon3: temp1_input not attached to any thermal zone
[    3.005581] hwmon hwmon4: temp1_input not attached to any thermal zone
[    3.022294] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    3.057359] mvpp2 f2000000.ethernet eth0: Using firmware node mac address 00:51:82:11:22:00
[    3.069316] mvpp2 f2000000.ethernet eth1: Using firmware node mac address 00:51:82:11:22:01
[    3.079945] mvpp2 f2000000.ethernet eth2: Using firmware node mac address 00:51:82:11:22:02
[    3.109402] xhci-hcd f2500000.usb3: xHCI Host Controller
[    3.114766] xhci-hcd f2500000.usb3: new USB bus registered, assigned bus number 3
[    3.122374] xhci-hcd f2500000.usb3: hcc params 0x0a000990 hci version 0x100 quirks 0x0000000000010010
[    3.131688] xhci-hcd f2500000.usb3: irq 36, io mem 0xf2500000
[    3.138060] hub 3-0:1.0: USB hub found
[    3.141891] hub 3-0:1.0: 1 port detected
[    3.146039] xhci-hcd f2500000.usb3: xHCI Host Controller
[    3.151402] xhci-hcd f2500000.usb3: new USB bus registered, assigned bus number 4
[    3.158922] xhci-hcd f2500000.usb3: Host supports USB 3.0 SuperSpeed
[    3.165335] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    3.173646] hub 4-0:1.0: USB hub found
[    3.177422] hub 4-0:1.0: 1 port detected
[    3.184215] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    3.241427] hwmon hwmon1: temp1_input not attached to any thermal zone
[    3.242574] ata1: SATA link down (SStatus 0 SControl 300)
[    3.254223] hwmon hwmon2: temp1_input not attached to any thermal zone
[    3.265043] hwmon hwmon3: temp1_input not attached to any thermal zone
[    3.275775] hwmon hwmon4: temp1_input not attached to any thermal zone
[    3.431426] usb 3-1: new high-speed USB device number 2 using xhci-hcd
[    3.431447] ata2: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    3.432124] ata2.00: ATA-11: WDC  WDS100T1R0B-68A4Z0, 411000WR, max UDMA/133
[    3.451359] ata2.00: 1953525168 sectors, multi 1: LBA48 NCQ (depth 32)
[    3.459999] ata2.00: configured for UDMA/133
[    3.464549] scsi 1:0:0:0: Direct-Access     ATA      WDC  WDS100T1R0B 00WR PQ: 0 ANSI: 5
[    3.473271] sd 1:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    3.480997] sd 1:0:0:0: [sda] Write Protect is off
[    3.485886] sd 1:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    3.495609] sd 1:0:0:0: [sda] Attached SCSI removable disk
[    3.632815] hub 3-1:1.0: USB hub found
[    3.636665] hub 3-1:1.0: 4 ports detected
[    3.791465] usb 4-1: new SuperSpeed Gen 1 USB device number 2 using xhci-hcd
[    3.822536] hub 4-1:1.0: USB hub found
[    3.826398] hub 4-1:1.0: 4 ports detected
[    4.003462] mvpp2 f2000000.ethernet: all ports have a low MTU, switching to per-cpu buffers
[    4.045883] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    4.060988] mv88e6085 f212a200.mdio-mii:03 lan0 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch@3!mdio:11] driver [Marvell 88E6341 Family] (irq=77)
[    4.083652] mv88e6085 f212a200.mdio-mii:03 lan1 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch@3!mdio:12] driver [Marvell 88E6341 Family] (irq=78)
[    4.106233] mv88e6085 f212a200.mdio-mii:03 lan2 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch@3!mdio:13] driver [Marvell 88E6341 Family] (irq=79)
[    4.128216] mv88e6085 f212a200.mdio-mii:03 lan3 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch@3!mdio:14] driver [Marvell 88E6341 Family] (irq=80)
[    4.156378] mv88e6085 f212a200.mdio-mii:03: configuring for inband/2500base-x link mode
[    4.164840] usb 4-1.2: new SuperSpeed Gen 1 USB device number 3 using xhci-hcd
[    4.198154] DSA: tree 0 setup
[    4.210244] VFS: Mounted root (squashfs filesystem) readonly on device 179:2.
[    4.217572] Freeing unused kernel memory: 448K
[    4.223605] usb-storage 4-1.2:1.0: USB Mass Storage device detected
[    4.230115] scsi host2: usb-storage 4-1.2:1.0
[    4.281502] Run /sbin/init as init process
[    4.462296] init: Console is alive
[    4.575773] kmodloader: loading kernel modules from /etc/modules-boot.d/*
[    4.614539] kmodloader: done loading kernel modules from /etc/modules-boot.d/*
[    4.627071] init: - preinit -
[    5.107929] mvpp2 f2000000.ethernet eth1: configuring for fixed/2500base-x link mode
[    5.116907] mvpp2 f2000000.ethernet eth1: Link is Up - 2.5Gbps/Full - flow control off
[    5.121943] mv88e6085 f212a200.mdio-mii:03 lan0: configuring for phy/ link mode
[    5.133988] 8021q: adding VLAN 0 to HW filter on device lan0
[    5.139699] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[    5.282191] scsi 2:0:0:0: Direct-Access     Kingston DataTraveler 3.0      PQ: 0 ANSI: 6
[    5.291592] sd 2:0:0:0: [sdb] 60437492 512-byte logical blocks: (30.9 GB/28.8 GiB)
[    5.299429] sd 2:0:0:0: [sdb] Write Protect is off
[    5.304458] sd 2:0:0:0: [sdb] Write cache: disabled, read cache: enabled, doesn't support DPO or FUA
[    5.315481]  sdb: sdb1
[    5.318889] sd 2:0:0:0: [sdb] Attached SCSI removable disk
[    8.624024] F2FS-fs (loop0): Mounted with checkpoint version = 3d07f56a
[    8.631266] mount_root: switching to f2fs overlay
[    8.636546] overlayfs: "xino" feature enabled using 32 upper inode bits.
[    8.763522] EXT4-fs (mmcblk0p1): mounted filesystem without journal. Opts: (null)
[    8.777403] urandom-seed: Seeding with /etc/urandom.seed
[    8.881604] procd: - early -
[    9.534268] procd: - ubus -
[    9.588630] procd: - init -
Please press Enter to activate this console.
[    9.849260] kmodloader: loading kernel modules from /etc/modules.d/*
[    9.871685] urngd: v1.0.2 started.
[    9.904154] PPP generic driver version 2.4.2
[    9.908866] NET: Registered protocol family 24
[    9.915460] kmodloader: done loading kernel modules from /etc/modules.d/*
[   12.772877] mvpp2 f2000000.ethernet eth1: Link is Down
[   12.791027] mvpp2 f2000000.ethernet eth1: configuring for fixed/2500base-x link mode
[   12.799236] mvpp2 f2000000.ethernet eth1: Link is Up - 2.5Gbps/Full - flow control off
[   12.810596] mv88e6085 f212a200.mdio-mii:03 lan0: configuring for phy/ link mode
[   12.820825] 8021q: adding VLAN 0 to HW filter on device lan0
[   12.826565] IPv6: ADDRCONF(NETDEV_CHANGE): eth1: link becomes ready
[   12.943561] br-lan: port 1(lan0) entered blocking state
[   12.948836] br-lan: port 1(lan0) entered disabled state
[   12.955956] device lan0 entered promiscuous mode
[   12.960609] device eth1 entered promiscuous mode
[   13.070259] mv88e6085 f212a200.mdio-mii:03 lan1: configuring for phy/ link mode
[   13.078833] 8021q: adding VLAN 0 to HW filter on device lan1
[   13.194505] br-lan: port 2(lan1) entered blocking state
[   13.199759] br-lan: port 2(lan1) entered disabled state
[   13.206736] device lan1 entered promiscuous mode
[   13.233762] mv88e6085 f212a200.mdio-mii:03 lan2: configuring for phy/ link mode
[   13.242384] 8021q: adding VLAN 0 to HW filter on device lan2
[   13.355709] br-lan: port 3(lan2) entered blocking state
[   13.360979] br-lan: port 3(lan2) entered disabled state
[   13.368756] device lan2 entered promiscuous mode
[   13.396173] mv88e6085 f212a200.mdio-mii:03 lan3: configuring for phy/ link mode
[   13.404780] 8021q: adding VLAN 0 to HW filter on device lan3
[   13.525721] br-lan: port 4(lan3) entered blocking state
[   13.530990] br-lan: port 4(lan3) entered disabled state
[   13.539530] device lan3 entered promiscuous mode
[   13.580818] mvpp2 f2000000.ethernet eth0: configuring for inband/10gbase-r link mode
[   13.589847] br-wan: port 1(eth0) entered blocking state
[   13.595139] br-wan: port 1(eth0) entered disabled state
[   13.600873] device eth0 entered promiscuous mode
[   13.607793] br-wan: port 1(eth0) entered blocking state
[   13.613068] br-wan: port 1(eth0) entered forwarding state
[   13.624145] mvpp2 f2000000.ethernet eth2: PHY [f212a200.mdio-mii:01] driver [Marvell 88E1510] (irq=POLL)
[   13.633761] mvpp2 f2000000.ethernet eth2: configuring for phy/rgmii-id link mode
[   13.642325] br-wan: port 2(eth2) entered blocking state
[   13.647576] br-wan: port 2(eth2) entered disabled state
[   13.653310] device eth2 entered promiscuous mode
[   13.658063] br-wan: port 2(eth2) entered blocking state
[   13.663322] br-wan: port 2(eth2) entered forwarding state
[   13.784836] br-wan: port 1(eth0) entered disabled state
[   13.790846] br-wan: port 2(eth2) entered disabled state
[   17.831989] mvpp2 f2000000.ethernet eth2: Link is Up - 1Gbps/Full - flow control off
[   17.839798] br-wan: port 2(eth2) entered blocking state
[   17.845068] br-wan: port 2(eth2) entered forwarding state



BusyBox v1.35.0 (2022-03-15 23:48:24 UTC) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r19124-832b90216f
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------
root@OpenWrt:/#

root@OpenWrt:/# uname -ar
Linux OpenWrt 5.10.104 #0 SMP Tue Mar 15 23:48:24 2022 aarch64 GNU/Linux

root@OpenWrt:/# cat /etc/openwrt_release
DISTRIB_ID='OpenWrt'
DISTRIB_RELEASE='SNAPSHOT'
DISTRIB_REVISION='r19124-832b90216f'
DISTRIB_TARGET='mvebu/cortexa72'
DISTRIB_ARCH='aarch64_cortex-a72'
DISTRIB_DESCRIPTION='OpenWrt SNAPSHOT r19124-832b90216f'
DISTRIB_TAINTS=''

root@OpenWrt:/# opkg update && opkg install luci-mod-admin-full luci-ssl
Downloading https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/packages/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_core
Downloading https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/packages/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_base
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/kmods/5.10.104-1-08c8d2b2068318c202f4b6a78c92f5dc/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_kmods
Downloading https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/kmods/5.10.104-1-08c8d2b2068318c202f4b6a78c92f5dc/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_luci
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/packages/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_packages
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/packages/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/routing/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_routing
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/routing/Packages.sig
Signature check passed.
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/telephony/Packages.gz
Updated list of available packages in /var/opkg-lists/openwrt_telephony
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/telephony/Packages.sig
Signature check passed.
Installing luci-mod-admin-full (git-19.253.48496-3f93650) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-mod-admin-full_git-19.253.48496-3f93650_all.ipk
Installing liblua5.1.5 (5.1.5-10) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/liblua5.1.5_5.1.5-10_aarch64_cortex-a72.ipk
Installing lua (5.1.5-10) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/lua_5.1.5-10_aarch64_cortex-a72.ipk
Installing luci-lib-nixio (git-20.234.06894-c4a4e43) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-lib-nixio_git-20.234.06894-c4a4e43_aarch64_cortex-a72.ipk
Installing luci-lib-ip (git-20.250.76529-62505bd) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-lib-ip_git-20.250.76529-62505bd_aarch64_cortex-a72.ipk
Installing rpcd (2022-02-07-909f2a04-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/rpcd_2022-02-07-909f2a04-1_aarch64_cortex-a72.ipk
Installing libubus-lua (2022-02-28-584f56a2-2) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/libubus-lua_2022-02-28-584f56a2-2_aarch64_cortex-a72.ipk
Installing luci-lib-jsonc (git-19.317.29469-8da8f38) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-lib-jsonc_git-19.317.29469-8da8f38_aarch64_cortex-a72.ipk
Installing liblucihttp0 (2022-02-13-cc851838-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/liblucihttp0_2022-02-13-cc851838-1_aarch64_cortex-a72.ipk
Installing liblucihttp-lua (2022-02-13-cc851838-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/liblucihttp-lua_2022-02-13-cc851838-1_aarch64_cortex-a72.ipk
Installing luci-lib-base (git-20.232.39649-1f6dc29) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-lib-base_git-20.232.39649-1f6dc29_all.ipk
Installing rpcd-mod-file (2022-02-07-909f2a04-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/rpcd-mod-file_2022-02-07-909f2a04-1_aarch64_cortex-a72.ipk
Installing rpcd-mod-luci (20210614) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/rpcd-mod-luci_20210614_aarch64_cortex-a72.ipk
Installing cgi-io (2021-09-08-98cef9dd-20) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/packages/cgi-io_2021-09-08-98cef9dd-20_aarch64_cortex-a72.ipk
Installing luci-base (git-22.058.70382-d29400e) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-base_git-22.058.70382-d29400e_aarch64_cortex-a72.ipk
Installing libiwinfo-data (2021-07-11-a0a0e02d-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/libiwinfo-data_2021-07-11-a0a0e02d-1_aarch64_cortex-a72.ipk
Installing libiwinfo20210430 (2021-07-11-a0a0e02d-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/libiwinfo20210430_2021-07-11-a0a0e02d-1_aarch64_cortex-a72.ipk
Installing libiwinfo-lua (2021-07-11-a0a0e02d-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/libiwinfo-lua_2021-07-11-a0a0e02d-1_aarch64_cortex-a72.ipk
Installing luci-mod-status (git-22.041.71554-e6f21f8) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-mod-status_git-22.041.71554-e6f21f8_aarch64_cortex-a72.ipk
Installing luci-mod-system (git-22.019.40203-e0ff3ff) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-mod-system_git-22.019.40203-e0ff3ff_all.ipk
Installing rpcd-mod-iwinfo (2022-02-07-909f2a04-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/rpcd-mod-iwinfo_2022-02-07-909f2a04-1_aarch64_cortex-a72.ipk
Installing luci-mod-network (git-22.049.73249-8890111) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-mod-network_git-22.049.73249-8890111_all.ipk
Installing luci-ssl (git-20.244.36115-e10f954) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-ssl_git-20.244.36115-e10f954_all.ipk
Installing uhttpd (2022-02-07-2f8b1360-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/uhttpd_2022-02-07-2f8b1360-1_aarch64_cortex-a72.ipk
Installing uhttpd-mod-ubus (2022-02-07-2f8b1360-1) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/uhttpd-mod-ubus_2022-02-07-2f8b1360-1_aarch64_cortex-a72.ipk
Installing luci-theme-bootstrap (git-22.055.81918-06b3517) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-theme-bootstrap_git-22.055.81918-06b3517_all.ipk
Installing luci-app-firewall (git-22.046.84457-2178444) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-app-firewall_git-22.046.84457-2178444_all.ipk
Installing luci-app-opkg (git-22.043.53495-1e6f630) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-app-opkg_git-22.043.53495-1e6f630_all.ipk
Installing luci-proto-ppp (git-21.158.38888-88b9d84) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-proto-ppp_git-21.158.38888-88b9d84_all.ipk
Installing luci-proto-ipv6 (git-21.148.48881-79947af) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci-proto-ipv6_git-21.148.48881-79947af_all.ipk
Installing rpcd-mod-rrdns (20170710) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/rpcd-mod-rrdns_20170710_aarch64_cortex-a72.ipk
Installing luci (git-20.074.84698-ead5e81) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/luci/luci_git-20.074.84698-ead5e81_all.ipk
Installing libwolfssl5.1.1.5fb91bea (5.1.1-stable-2) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/libwolfssl5.1.1.5fb91bea_5.1.1-stable-2_aarch64_cortex-a72.ipk
Installing px5g-wolfssl (4) to root...
Downloading https://downloads.openwrt.org/snapshots/packages/aarch64_cortex-a72/base/px5g-wolfssl_4_aarch64_cortex-a72.ipk
Configuring liblucihttp0.
Configuring cgi-io.
Configuring liblua5.1.5.
Configuring lua.
Configuring luci-lib-nixio.
Configuring luci-lib-ip.
Configuring luci-lib-jsonc.
Configuring liblucihttp-lua.
Configuring luci-lib-base.
Configuring rpcd.
Configuring libubus-lua.
Configuring libiwinfo-data.
Configuring libiwinfo20210430.
Configuring libiwinfo-lua.
Configuring rpcd-mod-file.
Configuring rpcd-mod-luci.
Configuring luci-base.
Configuring luci-mod-system.
Configuring luci-mod-status.
Configuring rpcd-mod-iwinfo.
Configuring luci-mod-network.
Configuring luci-mod-admin-full.
Configuring luci-app-opkg.
Configuring luci-theme-bootstrap.
/luci-static/bootstrap
Configuring libwolfssl5.1.1.5fb91bea.
Configuring px5g-wolfssl.
Configuring luci-app-firewall.
Configuring uhttpd.
4+0 records in
4+0 records out
Generating EC private key
Generating selfsigned certificate with subject '/C=ZZ/ST=Somewhere/L=Unknown/O=OpenWrt133b25eb/CN=OpenWrt' and validity 20220317125219-20240316125219
Configuring uhttpd-mod-ubus.
Configuring luci-proto-ppp.
Configuring luci-proto-ipv6.
Configuring rpcd-mod-rrdns.
Configuring luci.
Configuring luci-ssl.

root@OpenWrt:/# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq master br-wan state DOWN qlen 2048
    link/ether 00:51:82:11:22:00 brd ff:ff:ff:ff:ff:ff
3: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1508 qdisc mq state UP qlen 2048
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::251:82ff:fe11:2201/64 scope link
       valid_lft forever preferred_lft forever
4: eth2: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq master br-wan state UP qlen 2048
    link/ether 00:51:82:11:22:02 brd ff:ff:ff:ff:ff:ff
5: lan0@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br-lan state LOWERLAYERDOWN qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
6: lan1@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br-lan state LOWERLAYERDOWN qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
7: lan2@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br-lan state LOWERLAYERDOWN qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
8: lan3@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br-lan state LOWERLAYERDOWN qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
9: br-lan: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.1/24 brd 192.168.1.255 scope global br-lan
       valid_lft forever preferred_lft forever
    inet6 fd24:e7dc:ef0c::1/60 scope global tentative noprefixroute
       valid_lft forever preferred_lft forever
10: br-wan: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP qlen 1000
    link/ether 00:51:82:11:22:00 brd ff:ff:ff:ff:ff:ff
    inet 10.4.2.110/24 brd 10.4.2.255 scope global br-wan
       valid_lft forever preferred_lft forever
    inet6 2a01:e0a:8ab:34b0:251:82ff:fe11:2200/64 scope global dynamic noprefixroute
       valid_lft 86280sec preferred_lft 86280sec
    inet6 fe80::251:82ff:fe11:2200/64 scope link
       valid_lft forever preferred_lft forever
root@OpenWrt:/#
```
</details>

Disable the FireWall from WAN:
```
root@OpenWrt:/# service firewall stop
```

[Access Web-UI (LuCI) from FireFox](http://openwrt.local/cgi-bin/luci/)

Openwrt / LuCI / Login:
<img src="/uploads/images/MochaBin-5G/OpenWrt-FirstFlash/MOCHAbin-FirstTry-OpenWrt - Overview - LuCI-LOGIN.png" width="1000px" heigth="1000px">

Openwrt / LuCI / Status / Overview:
<img src="/uploads/images/MochaBin-5G/OpenWrt-FirstFlash/MOCHAbin-FirstTry-OpenWrt - Overview - LuCI-STATUS.png" width="1000px" heigth="1000px">

Openwrt / LuCI / Network / Interfaces:
<img src="/uploads/images/MochaBin-5G/OpenWrt-FirstFlash/MOCHAbin-FirstTry-OpenWrt - Interfaces - LuCI-INTERFACES.png" width="1000px" heigth="1000px">

Openwrt / LuCI / Network / Devices:
<img src="/uploads/images/MochaBin-5G/OpenWrt-FirstFlash/MOCHAbin-FirstTry-OpenWrt - Interfaces - LuCI-DEVICES.png" width="1000px" heigth="1000px">

Openwrt / LuCI / System / Backup - Flash Firmware:
<img src="/uploads/images/MochaBin-5G/OpenWrt-FirstFlash/MOCHAbin-FirstTry-OpenWrt - Backup _ Flash Firmware - LuCI.png" width="1000px" heigth="1000px">

[OpenWrt commit "mvebu: add Globalscale MOCHAbin"](https://git.openwrt.org/?p=openwrt/openwrt.git;a=commit;h=78cf3e53b1f4ea6428925302d78f743a693d5fb1)
<details>
  <summary>Click to expand OpenWrt commit details "mvebu: add Globalscale MOCHAbin"...</summary>
```
 mvebu: add Globalscale MOCHAbin

Globalscale MOCHAbin is a Armada 7040 based development board.

Specifications:
* Armada 7040 Quad core ARMv8 Cortex A-72 @ 1.4GHz
* 2 / 4 / 8 GB of DDR4 DRAM
* 16 GB eMMC
* 4MB SPI-NOR (Bootloader)
* 1x M.2-2280 B-key socket (for SSD expansion, SATA3 only)
* 1x M.2-2250 B-key socket (for modems, USB2.0 and I2C only)
* 1x Mini-PCIe 3.0 (x1, USB2.0 and I2C)
* 1x SATA 7+15 socket (SATA3)
* 1x 16-pin (2×8) MikroBus Connector
* 1x SIM card slot (Connected to the mini-PCIe and both M.2 slots)
* 2x USB3.0 Type-A ports via SMSC USB5434B hub
* Cortex 2x5 JTAG
* microUSB port for UART (PL2303GL/PL2303SA onboard)
* 1x 10G SFP+
* 1x 1G SFP (Connected to 88E1512 PHY)
* 1x 1G RJ45 with PoE PD (Connected to 88E1512 PHY)
* 4x 1G RJ45 ports via Topaz 88E6141 switch
* RTC with battery holder (SoC provided, requires CR2032 battery)
* 1x 12V DC IN
* 1x Power switch
* 1x 12V fan header (3-pin, power only)
* 1x mini-PCIe LED header (2x0.1" pins)
* 1x M.2-2280 LED header (2x0.1" pins)
* 6x Bootstrap jumpers
* 1x Power LED (Green)
* 3x Tri-color RGB LEDs (Controllable)
* 1x Microchip ATECC608B secure element

Note that 1G SFP and 1G WAN cannot be used at the same time as they are in
parallel connected to the same PHY.

Installation:

Copy dtb from build_dir to bin/ and run tftpserver there:
$ cp ./build_dir/target-aarch64_cortex-a72_musl/linux-mvebu_cortexa72/image-armada-7040-mochabin.dtb bin/targets/mvebu/cortexa72/
$ in.tftpd -L -s bin/targets/mvebu/cortexa72/

Connect to the device UART via microUSB port and power on the device.

Power on the device and hit any key to stop the autoboot.

Set serverip (host IP) and ipaddr (any free IP address on the same subnet), e.g:
$ setenv serverip 192.168.1.10 # Host
$ setenv ipaddr 192.168.1.15 # Device

Set the ethernet device (Example for the 1G WAN):
$ setenv ethact mvpp2-2

Ping server to confirm network is working:
$ ping $serverip
Using mvpp2-2 device
host 192.168.1.15 is alive

Tftpboot the firmware:
$ tftpboot $kernel_addr_r openwrt-mvebu-cortexa72-globalscale_mochabin-initramfs-kernel.bin
$ tftpboot $fdt_addr_r image-armada-7040-mochabin.dtb

Boot the image:
$ booti $kernel_addr_r - $fdt_addr_r

Once the initramfs is booted, transfer openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz
to /tmp dir on the device.

Gunzip and dd the image:
$ gunzip /tmp/openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz
$ dd if=/tmp/openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img of=/dev/mmcblk0 && sync

Reboot the device.

Hit any key to stop the autoboot.

Reset U-boot env and set the bootcmd:
$ env default -a
$ setenv bootcmd 'load mmc 0 ${loadaddr} boot.scr && source ${loadaddr}'

Optionally I would advise to edit the console env variable to remove earlycon as that
causes the kernel to never use the driver for the serial console.
Earlycon should be used only for debugging before the kernel can configure the console
and will otherwise cause various issues with the console.

$ setenv console 'console=ttyS0,115200'

Save and reset
$ saveenv
$ reset

OpenWrt should boot from eMMC now.

Signed-off-by: Robert Marko <robert.marko@sartura.hr>
```
</details>

More References:
* [OpenWrt WIKI DATA for MOCHAbin (WIP)](https://openwrt.org/toh/hwdata/globalscale/globalscale_mochabin)
* [Download OpenWrt firmware for MOCHAbin SNAPSHOT (with Firmware Selector)](https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=mvebu%2Fcortexa72&id=globalscale_mochabin)
* [Download OpenWrt firmware (SquashFS-SDCard) for MOCHAbin SNAPSHOT (Direct Link)](https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz)
* [Download OpenWrt firmware (EXT4-SDCard) for MOCHAbin SNAPSHOT (Direct Link)](https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/openwrt-mvebu-cortexa72-globalscale_mochabin-ext4-sdcard.img.gz)
