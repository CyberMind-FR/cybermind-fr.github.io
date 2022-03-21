---
title: MochaBin-5G@GlobalScaleTechnologies - First Boot
lang: en
date: 2022-03-21 16:44:23
tags:
---

MOCHAbin-V1-2-0 #22 Early Bird - first tests:
<img src="/uploads/images/MochaBin-5G/GST@MochaBin-5G_FirstBoot.jpeg" width="768px" heigth="1024px">

MOCHAbin-V1-2-0 #22 Early Bird - M2 ADD ON SSD 1Tb:
<img src="/uploads/images/MochaBin-5G/GST@MochaBin-5G_M2-1Tb-SSD-ADDON.jpeg" width="1024px" heigth="168px">

<details>
  <summary>Click to expand first full boot to factory Ubuntu...</summary>
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
Unknown command 'ev' - try 'help'
16519680 bytes read in 1217 ms (12.9 MiB/s)
23512 bytes read in 8 ms (2.8 MiB/s)
## Flattened Device Tree blob at 06f00000
   Booting using the fdt blob at 0x6f00000
   Using Device Tree in place at 0000000006f00000, end 0000000006f08bd7
Starting kernel ...
[    0.000000] Booting Linux on physical CPU 0x0000000000 [0x410fd081]
[    0.000000] Linux version 5.4.108-00028-gaa0ecb9744ee (gti@ubuntu) (gcc version 7.3.1 20180425 [linaro-7.3-2018.05 revision d29120a424ecfbc167ef90065c0eeb7f91977701] (Linaro GCC 7.3-2018.05)) #1 SMP P1
[    0.000000] Machine model: Globalscale MOCHAbin Development Board
[    0.000000] earlycon: uart8250 at MMIO32 0x00000000f0512000 (options '')
[    0.000000] printk: bootconsole [uart8250] enabled
[    0.000000] efi: Getting EFI parameters from FDT:
[    0.000000] efi: UEFI not found.
[    0.000000] cma: Reserved 32 MiB at 0x00000000be000000
[    0.000000] NUMA: No NUMA configuration found
[    0.000000] NUMA: Faking a node at [mem 0x0000000000000000-0x000000023fffffff]
[    0.000000] NUMA: NODE_DATA [mem 0x23efd7800-0x23efd8fff]
[    0.000000] Zone ranges:
[    0.000000]   DMA32    [mem 0x0000000000000000-0x00000000ffffffff]
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
[    0.000000] percpu: Embedded 22 pages/cpu s52632 r8192 d29288 u90112
[    0.000000] Detected PIPT I-cache on CPU0
[    0.000000] CPU features: detected: EL2 vector hardening
[    0.000000] CPU features: detected: Branch predictor hardening
[    0.000000] Speculative Store Bypass Disable mitigation not required
[    0.000000] Built 1 zonelists, mobility grouping on.  Total pages: 2064384
[    0.000000] Policy zone: Normal
[    0.000000] Kernel command line: console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000 root=PARTUUID=89708921-01 rw rootwait net.ifnames=0 biosdevname=0
[    0.000000] Dentry cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
[    0.000000] Inode-cache hash table entries: 524288 (order: 10, 4194304 bytes, linear)
[    0.000000] mem auto-init: stack:off, heap alloc:off, heap free:off
[    0.000000] software IO TLB: mapped [mem 0xba000000-0xbe000000] (64MB)
[    0.000000] Memory: 8111016K/8388608K available (10172K kernel code, 644K rwdata, 3464K rodata, 1792K init, 408K bss, 244824K reserved, 32768K cma-reserved)
[    0.000000] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=4, Nodes=1
[    0.000000] rcu: Preemptible hierarchical RCU implementation.
[    0.000000] rcu:     RCU restricting CPUs from NR_CPUS=256 to nr_cpu_ids=4.
[    0.000000]  Tasks RCU enabled.
[    0.000000] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
[    0.000000] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=4
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
[    0.000000] random: get_random_bytes called from start_kernel+0x2b8/0x448 with crng_init=0
[    0.000000] arch_timer: cp15 timer(s) running at 25.00MHz (phys).
[    0.000000] clocksource: arch_sys_counter: mask: 0xffffffffffffff max_cycles: 0x5c40939b5, max_idle_ns: 440795202646 ns
[    0.000002] sched_clock: 56 bits at 25MHz, resolution 40ns, wraps every 4398046511100ns
[    0.008616] Console: colour dummy device 80x25
[    0.013348] Calibrating delay loop (skipped), value calculated using timer frequency.. 50.00 BogoMIPS (lpj=100000)
[    0.024338] pid_max: default: 32768 minimum: 301
[    0.029240] LSM: Security Framework initializing
[    0.034221] Mount-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.042247] Mountpoint-cache hash table entries: 16384 (order: 5, 131072 bytes, linear)
[    0.051559] ASID allocator initialised with 32768 entries
[    0.057354] rcu: Hierarchical SRCU implementation.
[    0.062609] EFI services will not be available.
[    0.067550] smp: Bringing up secondary CPUs ...
[    0.072770] Detected PIPT I-cache on CPU1
[    0.072807] CPU1: Booted secondary processor 0x0000000001 [0x410fd081]
[    0.073211] Detected PIPT I-cache on CPU2
[    0.073238] CPU2: Booted secondary processor 0x0000000100 [0x410fd081]
[    0.073649] Detected PIPT I-cache on CPU3
[    0.073668] CPU3: Booted secondary processor 0x0000000101 [0x410fd081]
[    0.073712] smp: Brought up 1 node, 4 CPUs
[    0.111476] SMP: Total of 4 processors activated.
[    0.116465] CPU features: detected: 32-bit EL0 Support
[    0.121896] CPU features: detected: CRC32 instructions
[    0.136341] CPU: All CPU(s) started at EL2
[    0.140685] alternatives: patching kernel code
[    0.146630] devtmpfs: initialized
[    0.152321] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
[    0.162677] futex hash table entries: 1024 (order: 4, 65536 bytes, linear)
[    0.170440] pinctrl core: initialized pinctrl subsystem
[    0.176216] DMI not present or invalid.
[    0.180428] NET: Registered protocol family 16
[    0.185798] DMA: preallocated 256 KiB pool for atomic allocations
[    0.192286] audit: initializing netlink subsys (disabled)
[    0.198086] audit: type=2000 audit(0.132:1): state=initialized audit_enabled=0 res=1
[    0.206319] cpuidle: using governor menu
[    0.210577] hw-breakpoint: found 6 breakpoint and 4 watchpoint registers.
[    0.224745] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
[    0.231833] HugeTLB registered 32.0 MiB page size, pre-allocated 0 pages
[    0.238948] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
[    0.246054] HugeTLB registered 64.0 KiB page size, pre-allocated 0 pages
[    0.253784] cryptd: max_cpu_qlen set to 1000
[    0.259376] ACPI: Interpreter disabled.
[    0.263706] iommu: Default domain type: Translated
[    0.268979] vgaarb: loaded
[    0.271963] SCSI subsystem initialized
[    0.276117] usbcore: registered new interface driver usbfs
[    0.281974] usbcore: registered new interface driver hub
[    0.287613] usbcore: registered new device driver usb
[    0.293198] pps_core: LinuxPPS API ver. 1 registered
[    0.298431] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
[    0.308135] PTP clock support registered
[    0.312270] EDAC MC: Ver: 3.0.0
[    0.316187] clocksource: Switched to clocksource arch_sys_counter
[    0.322724] VFS: Disk quotas dquot_6.6.0
[    0.326909] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
[    0.334278] pnp: PnP ACPI: disabled
[    0.341155] thermal_sys: Registered thermal governor 'step_wise'
[    0.341157] thermal_sys: Registered thermal governor 'power_allocator'
[    0.347956] NET: Registered protocol family 2
[    0.359713] tcp_listen_portaddr_hash hash table entries: 4096 (order: 4, 65536 bytes, linear)
[    0.368813] TCP established hash table entries: 65536 (order: 7, 524288 bytes, linear)
[    0.377503] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
[    0.385975] TCP: Hash tables configured (established 65536 bind 65536)
[    0.393006] UDP hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    0.400325] UDP-Lite hash table entries: 4096 (order: 5, 131072 bytes, linear)
[    0.408213] NET: Registered protocol family 1
[    0.413129] RPC: Registered named UNIX socket transport module.
[    0.419395] RPC: Registered udp transport module.
[    0.424392] RPC: Registered tcp transport module.
[    0.429344] RPC: Registered tcp NFSv4.1 backchannel transport module.
[    0.436196] PCI: CLS 0 bytes, default 64
[    0.440689] hw perfevents: unable to count PMU IRQs
[    0.445858] hw perfevents: /ap806/config-space@f0000000/pmu: failed to register PMU devices!
[    0.454975] kvm [1]: IPA Size Limit: 44 bits
[    0.459827] kvm [1]: vgic interrupt IRQ1
[    0.464079] kvm [1]: Hyp mode initialized successfully
[    0.471658] Initialise system trusted keyrings
[    0.476444] workingset: timestamp_bits=44 max_order=21 bucket_order=0
[    0.486506] squashfs: version 4.0 (2009/01/31) Phillip Lougher
[    0.493061] NFS: Registering the id_resolver key type
[    0.498454] Key type id_resolver registered
[    0.502885] Key type id_legacy registered
[    0.507144] nfs4filelayout_init: NFSv4 File Layout Driver Registering...
[    0.514329] 9p: Installing v9fs 9p2000 file system support
[    0.530388] Key type asymmetric registered
[    0.534725] Asymmetric key parser 'x509' registered
[    0.539908] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 245)
[    0.547757] io scheduler mq-deadline registered
[    0.552552] io scheduler kyber registered
[    0.558284] armada-ap806-pinctrl f06f4000.system-controller:pinctrl: registered pinctrl driver
[    0.567851] armada-cp110-pinctrl f2440000.system-controller:pinctrl: registered pinctrl driver
[    0.578217] EINJ: ACPI disabled.
[    0.583086] mv_xor_v2 f0400000.xor: Marvell Version 2 XOR driver
[    0.589765] mv_xor_v2 f0420000.xor: Marvell Version 2 XOR driver
[    0.596455] mv_xor_v2 f0440000.xor: Marvell Version 2 XOR driver
[    0.603139] mv_xor_v2 f0460000.xor: Marvell Version 2 XOR driver
[    0.609869] mv_xor_v2 f26a0000.xor: Marvell Version 2 XOR driver
[    0.616576] mv_xor_v2 f26c0000.xor: Marvell Version 2 XOR driver
[    0.624356] Serial: 8250/16550 driver, 4 ports, IRQ sharing enabled
[    0.631770] printk: console [ttyS0] disabled
[    0.656447] f0512000.serial: ttyS0 at MMIO 0xf0512000 (irq = 8, base_baud = 12500000) is a 16550A
[    0.665898] printk: console [ttyS0] enabled
[    0.665898] printk: console [ttyS0] enabled
[    0.674520] printk: bootconsole [uart8250] disabled
[    0.674520] printk: bootconsole [uart8250] disabled
[    0.705125] f2702000.serial: ttyS1 at MMIO 0xf2702000 (irq = 17, base_baud = 15625000) is a 16550A
[    0.714660] cacheinfo: Unable to detect cache hierarchy for CPU 0
[    0.721173] brd: module loaded
[    0.728260] loop: module loaded
[    0.731694] ahci f2540000.sata: f2540000.sata supply ahci not found, using dummy regulator
[    0.740044] ahci f2540000.sata: f2540000.sata supply phy not found, using dummy regulator
[    0.748441] platform f2540000.sata:sata-port@0: f2540000.sata:sata-port@0 supply target not found, using dummy regulator
[    0.760515] spi-nor spi2.0: w25q32 (4096 Kbytes)
[    0.765315] 3 fixed-partitions partitions found on MTD device spi2.0
[    0.771706] Creating 3 MTD partitions on "spi2.0":
[    0.776547] 0x000000000000-0x0000003e0000 : "u-boot"
[    0.784612] 0x0000003e0000-0x0000003f0000 : "hw-info"
[    0.792596] 0x0000003f0000-0x000000400000 : "u-boot-env"
[    0.800904] libphy: Fixed MDIO Bus: probed
[    0.805158] tun: Universal TUN/TAP device driver, 1.6
[    0.810329] e1000e: Intel(R) PRO/1000 Network Driver - 3.2.6-k
[    0.816198] e1000e: Copyright(c) 1999 - 2015 Intel Corporation.
[    0.822171] igb: Intel(R) Gigabit Ethernet Network Driver - version 5.6.0-k
[    0.829168] igb: Copyright (c) 2007-2014 Intel Corporation.
[    0.834788] igbvf: Intel(R) Gigabit Virtual Function Network Driver - version 2.4.0-k
[    0.842656] igbvf: Copyright (c) 2009 - 2012 Intel Corporation.
[    0.848710] orion-mdio f212a200.mdio: IRQ index 0 not found
[    0.854354] libphy: orion_mdio_bus: probed
[    0.859305] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    0.881570] libphy: mdio: probed
[    0.912711] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    0.927539] VFIO - User Level meta-driver version: 0.3
[    0.933136] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
[    0.939703] ehci-pci: EHCI PCI platform driver
[    0.944192] ehci-platform: EHCI generic platform driver
[    0.949509] ehci-orion: EHCI orion driver
[    0.953596] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
[    0.959819] ohci-pci: OHCI PCI platform driver
[    0.964300] ohci-platform: OHCI generic platform driver
[    0.969892] xhci-hcd f2510000.usb3: xHCI Host Controller
[    0.975246] xhci-hcd f2510000.usb3: new USB bus registered, assigned bus number 1
[    0.982843] xhci-hcd f2510000.usb3: hcc params 0x0a000990 hci version 0x100 quirks 0x0000000000010010
[    0.992134] xhci-hcd f2510000.usb3: irq 19, io mem 0xf2510000
[    0.998282] hub 1-0:1.0: USB hub found
[    1.002073] hub 1-0:1.0: 1 port detected
[    1.006153] xhci-hcd f2510000.usb3: xHCI Host Controller
[    1.011521] xhci-hcd f2510000.usb3: new USB bus registered, assigned bus number 2
[    1.019044] xhci-hcd f2510000.usb3: Host supports USB 3.0 SuperSpeed
[    1.025459] usb usb2: We don't know the algorithms for LPM for this host, disabling LPM.
[    1.033805] hub 2-0:1.0: USB hub found
[    1.037590] hub 2-0:1.0: 1 port detected
[    1.041749] usbcore: registered new interface driver cdc_acm
[    1.047439] cdc_acm: USB Abstract Control Model driver for USB modems and ISDN adapters
[    1.055497] usbcore: registered new interface driver cdc_wdm
[    1.061217] usbcore: registered new interface driver usb-storage
[    1.067654] armada38x-rtc f2284000.rtc: registered as rtc0
[    1.073243] i2c /dev entries driver
[    1.092135] sdhci: Secure Digital Host Controller Interface driver
[    1.098360] sdhci: Copyright(c) Pierre Ossman
[    1.102780] Synopsys Designware Multimedia Card Interface Driver
[    1.108885] sdhci-pltfm: SDHCI platform and OF driver helper
[    1.140056] mmc0: SDHCI controller on f06e0000.sdhci [f06e0000.sdhci] using ADMA 64-bit
[    1.149349] ledtrig-cpu: registered to indicate activity on CPUs
[    1.155765] usbcore: registered new interface driver usbhid
[    1.161400] usbhid: USB HID core driver
[    1.165744] NET: Registered protocol family 10
[    1.170614] Segment Routing with IPv6
[    1.174354] sit: IPv6, IPv4 and MPLS over IPv4 tunneling driver
[    1.180552] NET: Registered protocol family 17
[    1.185065] bridge: filtering via arp/ip/ip6tables is no longer available by default. Update your scripts to load br_netfilter if you need this.
[    1.198244] 9pnet: Installing 9P2000 support
[    1.202573] Key type dns_resolver registered
[    1.207062] registered taskstats version 1
[    1.211185] Loading compiled-in X.509 certificates
[    1.217889] hw perfevents: enabled with armv8_cortex_a72 PMU driver, 7 counters available
[    1.227592] armada8k-pcie f2640000.pcie: host bridge /cp0/pcie@f2640000 ranges:
[    1.234968] armada8k-pcie f2640000.pcie:    IO 0xf9020000..0xf902ffff -> 0xf9020000
[    1.242670] armada8k-pcie f2640000.pcie:   MEM 0xf8000000..0xf8efffff -> 0xf8000000
[    1.273434] mmc0: new high speed MMC card at address 0001
[    1.279200] mmcblk0: mmc0:0001 DF4016 14.7 GiB
[    1.283957] mmcblk0boot0: mmc0:0001 DF4016 partition 1 4.00 MiB
[    1.290110] mmcblk0boot1: mmc0:0001 DF4016 partition 2 4.00 MiB
[    1.296149] mmcblk0rpmb: mmc0:0001 DF4016 partition 3 4.00 MiB, chardev (243:0)
[    1.305086]  mmcblk0: p1
[    2.250504] armada8k-pcie f2640000.pcie: Phy link never came up
[    2.256468] armada8k-pcie f2640000.pcie: Link not up after reconfiguration
[    2.263462] armada8k-pcie f2640000.pcie: PCI host bridge to bus 0000:00
[    2.270113] pci_bus 0000:00: root bus resource [bus 00-ff]
[    2.275629] pci_bus 0000:00: root bus resource [io  0x0000-0xffff] (bus address [0xf9020000-0xf902ffff])
[    2.285156] pci_bus 0000:00: root bus resource [mem 0xf8000000-0xf8efffff]
[    2.292080] pci 0000:00:00.0: [11ab:0110] type 01 class 0x060400
[    2.298137] pci 0000:00:00.0: reg 0x10: [mem 0x00000000-0x000fffff]
[    2.304499] pci 0000:00:00.0: supports D1 D2
[    2.308793] pci 0000:00:00.0: PME# supported from D0 D1 D3hot
[    2.316199] pci 0000:00:00.0: BAR 0: assigned [mem 0xf8000000-0xf80fffff]
[    2.323026] pci 0000:00:00.0: PCI bridge to [bus 01-ff]
[    2.635725] pcieport 0000:00:00.0: PME: Signaling with IRQ 33
[    2.641647] pcieport 0000:00:00.0: AER: enabled with IRQ 33
[    2.647475] ahci f2540000.sata: f2540000.sata supply ahci not found, using dummy regulator
[    2.655834] ahci f2540000.sata: f2540000.sata supply phy not found, using dummy regulator
[    2.664101] platform f2540000.sata:sata-port@0: f2540000.sata:sata-port@0 supply target not found, using dummy regulator
[    2.675219] platform f2540000.sata:sata-port@1: f2540000.sata:sata-port@1 supply target not found, using dummy regulator
[    2.688355] ahci f2540000.sata: masking port_map 0x3 -> 0x3
[    2.694006] ahci f2540000.sata: AHCI 0001.0000 32 slots 2 ports 6 Gbps 0x3 impl platform mode
[    2.702575] ahci f2540000.sata: flags: 64bit ncq sntf led only pmp fbs pio slum part sxs
[    2.711373] scsi host0: ahci
[    2.714532] scsi host1: ahci
[    2.717530] ata1: SATA max UDMA/133 mmio [mem 0xf2540000-0xf256ffff] port 0x100 irq 34
[    2.725489] ata2: SATA max UDMA/133 mmio [mem 0xf2540000-0xf256ffff] port 0x180 irq 34
[    2.733590] libphy: SFP I2C Bus: probed
[    2.737616] libphy: SFP I2C Bus: probed
[    2.741835] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    2.760806] libphy: mdio: probed
[    2.786439] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    2.804785] mvpp2 f2000000.ethernet eth0: Using firmware node mac address 00:51:82:11:22:00
[    2.814955] mvpp2 f2000000.ethernet eth1: Using firmware node mac address 00:51:82:11:22:01
[    2.825109] mvpp2 f2000000.ethernet eth2: Using firmware node mac address 00:51:82:11:22:02
[    2.856383] xhci-hcd f2500000.usb3: xHCI Host Controller
[    2.861744] xhci-hcd f2500000.usb3: new USB bus registered, assigned bus number 3
[    2.869346] xhci-hcd f2500000.usb3: hcc params 0x0a000990 hci version 0x100 quirks 0x0000000000010010
[    2.878640] xhci-hcd f2500000.usb3: irq 18, io mem 0xf2500000
[    2.884813] hub 3-0:1.0: USB hub found
[    2.888602] hub 3-0:1.0: 1 port detected
[    2.892686] xhci-hcd f2500000.usb3: xHCI Host Controller
[    2.898032] xhci-hcd f2500000.usb3: new USB bus registered, assigned bus number 4
[    2.905556] xhci-hcd f2500000.usb3: Host supports USB 3.0 SuperSpeed
[    2.911969] usb usb4: We don't know the algorithms for LPM for this host, disabling LPM.
[    2.920343] hub 4-0:1.0: USB hub found
[    2.924120] hub 4-0:1.0: 1 port detected
[    2.928328] pca953x 0-0039: 0-0039 supply vcc not found, using dummy regulator
[    2.935633] pca953x 0-0039: using no AI
[    2.941444] libphy: SFP I2C Bus: probed
[    2.946281] sfp sfp-eth0: Host maximum power 1.0W
[    2.955856] libphy: SFP I2C Bus: probed
[    2.960687] sfp sfp-eth2: Host maximum power 1.0W
[    2.976046] mv88e6085 f212a200.mdio-mii:03: switch 0x3400 detected: Marvell 88E6141, revision 0
[    2.996408] libphy: mdio: probed
[    3.046398] ata1: SATA link down (SStatus 0 SControl 300)
[    3.212204] ata2: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
[    3.219004] ata2.00: ATA-11: WDC  WDS100T1R0B-68A4Z0, 411000WR, max UDMA/133
[    3.226092] ata2.00: 1953525168 sectors, multi 1: LBA48 NCQ (depth 32)
[    3.228197] usb 3-1: new high-speed USB device number 2 using xhci-hcd
[    3.234699] ata2.00: configured for UDMA/133
[    3.243715] scsi 1:0:0:0: Direct-Access     ATA      WDC  WDS100T1R0B 00WR PQ: 0 ANSI: 5
[    3.252272] sd 1:0:0:0: [sda] 1953525168 512-byte logical blocks: (1.00 TB/932 GiB)
[    3.259992] sd 1:0:0:0: [sda] Write Protect is off
[    3.264847] sd 1:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
[    3.342726] sd 1:0:0:0: [sda] Attached SCSI removable disk
[    3.388884] hub 3-1:1.0: USB hub found
[    3.392717] hub 3-1:1.0: 4 ports detected
[    3.516219] usb 4-1: new SuperSpeed Gen 1 USB device number 2 using xhci-hcd
[    3.540809] hub 4-1:1.0: USB hub found
[    3.544611] hub 4-1:1.0: 4 ports detected
[    3.654416] mv88e6085 f212a200.mdio-mii:03 lan0 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch0@1!mdio:11] driver [Marvell 88E6390]
[    3.671821] mv88e6085 f212a200.mdio-mii:03 lan1 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch0@1!mdio:12] driver [Marvell 88E6390]
[    3.689132] mv88e6085 f212a200.mdio-mii:03 lan2 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch0@1!mdio:13] driver [Marvell 88E6390]
[    3.706437] mv88e6085 f212a200.mdio-mii:03 lan3 (uninitialized): PHY [!cp0!config-space@f2000000!mdio@12a200!switch0@1!mdio:14] driver [Marvell 88E6390]
[    3.727008] mv88e6085 f212a200.mdio-mii:03: configuring for inband/2500base-x link mode
[    3.748274] mvpp2 f2000000.ethernet: all ports have a low MTU, switching to per-cpu buffers
[    3.775139] mvpp2 f2000000.ethernet: using 8 per-cpu buffers
[    3.783881] DSA: tree 0 setup
[    3.787135] armada38x-rtc f2284000.rtc: setting system clock to 2022-03-14T22:24:02 UTC (1647296642)
[    3.858729] random: fast init done
[    3.889360] EXT4-fs (mmcblk0p1): recovery complete
[    3.894868] EXT4-fs (mmcblk0p1): mounted filesystem with ordered data mode. Opts: (null)
[    3.903057] VFS: Mounted root (ext4 filesystem) on device 179:1.
[    3.916752] devtmpfs: mounted
[    3.920578] Freeing unused kernel memory: 1792K
[    3.925255] Run /sbin/init as init process
[    4.507533] systemd[1]: systemd 237 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD -ID)
[    4.529163] systemd[1]: Detected architecture arm64.

Welcome to Ubuntu 18.04 LTS!

[    4.564888] systemd[1]: Set hostname to <moca112202>.
[    4.694534] systemd[1]: File /lib/systemd/system/systemd-journald.service:36 configures an IP firewall (IPAddressDeny=any), but the local system does not support BPF/cgroup based firewalling.
[    4.711672] systemd[1]: Proceeding WITHOUT firewalling in effect! (This warning is only shown for the first loaded unit using IP firewalling.)
[    4.806852] random: systemd: uninitialized urandom read (16 bytes read)
[    4.813697] systemd[1]: Started Dispatch Password Requests to Console Directory Watch.
[  OK  ] Started Dispatch Password Requests to Console Directory Watch.
[    4.840270] random: systemd: uninitialized urandom read (16 bytes read)
[    4.846950] systemd[1]: Reached target Remote File Systems.
[  OK  ] Reached target Remote File Systems.
[    4.868236] random: systemd: uninitialized urandom read (16 bytes read)
[    4.874910] systemd[1]: Reached target Swap.
[  OK  ] Reached target Swap.
[    4.892628] systemd[1]: Created slice User and Session Slice.
[  OK  ] Created slice User and Session Slice.
[    4.912384] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Started Forward Password Requests to Wall Directory Watch.
[  OK  ] Reached target Local Encrypted Volumes.
[  OK  ] Created slice System Slice.
[  OK  ] Listening on Journal Socket (/dev/log).
[  OK  ] Reached target Slices.
[  OK  ] Listening on udev Control Socket.
[  OK  ] Listening on Syslog Socket.
[  OK  ] Listening on /dev/initctl Compatibility Named Pipe.
[  OK  ] Listening on udev Kernel Socket.
[  OK  ] Listening on Journal Audit Socket.
[  OK  ] Listening on Journal Socket.
         Starting Journal Service...
         Mounting Kernel Debug File System...
         Mounting Huge Pages File System...
         Starting udev Coldplug all Devices...
         Starting Load Kernel Modules...
         Starting Remount Root and Kernel File Systems...
         Starting Set the console keyboard layout...
         Starting Create list of required st�…ce nodes for the current kernel...
         Mounting POSIX Message Queue File System...
[  OK  ] Created slice system-serial\x2dgetty.slice.
[  OK  ] Reached target System Time Synchronized.
[  OK  ] Reached target Paths.
[  OK  ] Started Journal Service.
[  OK  ] Mounted Kernel Debug File System.
[  OK  ] Mounted Huge Pages File System.
[  OK  ] Started Remount Root and Kernel File Systems.
[  OK  ] Started Create list of required sta�…vice nodes for the current kernel.
[  OK  ] Mounted POSIX Message Queue File System.
         Starting Create Static Device Nodes in /dev...
         Starting Load/Save Random Seed...
         Starting Flush Journal to Persistent Storage...
[  OK  ] Started udev Coldplug all Devices.
[    5.708587] cfg80211: Loading compiled-in X.509 certificates for regulatory database
[    5.713749] systemd-journald[189]: Received request to flush runtime journal from PID 1
[  OK      5.725092] cfg80211: Loaded X.509 cert 'sforshee: 00b28ddf47aef9cea7'
0m] Started Load/Save Random Seed.
[  OK  ] Started Load Kernel Modules.
[    5.759484] systemd-journald[189]: File /var/log/journal/2774dafc55914fa3a7fbbdf74a85d819/system.journal corrupted or uncleanly shut down, renaming and replacing.
[  OK  ] Started Create Static Device Nodes in /dev.
         Starting udev Kernel Device Manager...
         Mounting Kernel Configuration File System...
         Starting Apply Kernel Variables...
[  OK  ] Started Set the console keyboard layout.
[  OK  ] Mounted Kernel Configuration File System.
[  OK  ] Reached target Local File Systems (Pre).
[  OK  ] Reached target Local File Systems.
         Starting Set console font and keymap...
[  OK  ] Started Set console font and keymap.
[  OK  ] Started Flush Journal to Persistent Storage.
[  OK  ] Started Apply Kernel Variables.
[  OK  ] Started udev Kernel Device Manager.
         Starting Raise network interfaces...
         Starting Create Volatile Files and Directories...
[  OK  ] Started Create Volatile Files and Directories.
[  OK  ] Listening on Load/Save RF Kill Switch Status /dev/rfkill Watch.
         Starting Update UTMP about System Boot/Shutdown...
         Starting Network Name Resolution...
[  OK  ] Started Entropy daemon using the HAVEGE algorithm.
[  OK  ] Found device /dev/ttyS0.
[  OK  ] Started Update UTMP about System Boot/Shutdown.
[  OK  ] Reached target System Initialization.
[  OK  ] Started Discard unused blocks once a week.
[  OK  ] Started Message of the Day.
[  OK  ] Listening on D-Bus System Message Bus Socket.
[  OK  ] Reached target Sockets.
[  OK  ] Started Daily Cleanup of Temporary Directories.
[  OK  ] Reached target Basic System.
         Starting Restore /etc/resolv.conf i�…fore the ppp link was shut down...
[  OK  ] Started Set the CPU Frequency Scaling governor.
         Starting Login Service...
         Starting System Logging Service...
[  OK  ] Started D-Bus System Message Bus.
[  OK  ] Started Login Service.
         Starting WPA supplicant...
[  OK  ] Started Regular background program processing daemon.
[  OK  ] Started Daily apt download activities.
[  OK  ] Started Daily apt upgrade and clean activities.
[  OK  ] Reached target Timers.
[  OK  ] Started Network Name Resolution.
[  OK  ] Started System Logging Service.
[  OK  ] Started Restore /etc/resolv.conf if�…before the ppp link was shut down.
[  OK  ] Started WPA supplicant.
[  OK  ] Created slice system-usbmount.slice.
         Starting usbmount@dev-sda.service...
[  OK  ] Started ifup for eth1.
[  OK  ] Started ifup for lan2.
[  OK  ] Started ifup for lan3.
[  OK  ] Started ifup for eth2.
[  OK  ] Started ifup for eth0.
[  OK  ] Started ifup for lan1.
[  OK  ] Started ifup for lan0.
[  OK  ] Reached target Host and Network Name Lookups.
[FAILED] Failed to start usbmount@dev-sda.service.
See 'systemctl status usbmount@dev-sda.service' for details.
[  OK  ] Found device /sys/subsystem/net/devices/bond0.
[  OK  ] Started ifup for bond0.
         Stopping Network Name Resolution...
[  OK  ] Stopped Network Name Resolution.
         Starting Network Name Resolution...
[  OK  ] Started Network Name Resolution.
[  OK  ] Found device /sys/subsystem/net/devices/br0.
[  OK  ] Started ifup for br0.
[  OK  ] Started Raise network interfaces.
[  OK  ] Reached target Network.
         Starting OpenBSD Secure Shell server...
         Starting Network Time Service...
         Starting Permit User Sessions...
[  OK  ] Reached target Network is Online.
         Starting /etc/rc.local Compatibility...
         Starting LSB: Brings up/down network automatically...
[  OK  ] Started Permit User Sessions.
[  OK  ] Started /etc/rc.local Compatibility.
         Starting Set console scheme...
[  OK    OK  ] Started Set console scheme.
[  OK  ] Created slice system-getty.slice.
[  OK  ] Started Getty on tty1.
[  OK  ] Reached target Login Prompts.
[  OK  ] Started Network Time Service.
[  OK  ] Started LSB: Brings up/down network automatically.
[  OK  ] Started OpenBSD Secure Shell server.
[  OK  ] Reached target Multi-User System.
[  OK  ] Reached target Graphical Interface.
         Starting Update UTMP about System Runlevel Changes...
[  OK  ] Started Update UTMP about System Runlevel Changes.

Ubuntu 18.04 LTS moca112202 ttyS0

######################################
the default root password is 'admin'.
######################################

moca112202 login:
</details>

<details>
  <summary>Click to expand first login to factory Ubuntu with some few commands...</summary>
moca112202 login: root
Password:
Last login: Sat Jan 15 17:44:07 UTC 2022 on ttyS0
Welcome to Ubuntu 18.04 LTS (GNU/Linux 5.4.108-00028-gaa0ecb9744ee aarch64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage


  __  __  ___   ___ _  _   _   _    _
 |  \/  |/ _ \ / __| || | /_\ | |__(_)_ _
 | |\/| | (_) | (__| __ |/ _ \| '_ \ | ' \
 |_|  |_|\___/ \___|_||_/_/ \_\_.__/_|_||_|


Welcome to MOCHAbin development board!

For security reason, we recommended to change the password after first login.


Do you want to change default password? [Y/n]: n

Thanks! Enjoy it.

root@moca112202:~#

root@moca112202:~# uname -ar
Linux moca112200 5.4.108-00028-gaa0ecb9744ee #1 SMP PREEMPT Thu Dec 30 14:46:14 CST 2021 aarch64 aarch64 aarch64 GNU/Linux

root@moca112202:~# cat /proc/cmdline
console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000 root=PARTUUID=89708921-01 rw rootwait net.ifnames=0 biosdevname=0

root@moca112202:~# cat /proc/cpuinfo
processor       : 0
BogoMIPS        : 50.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd08
CPU revision    : 1

processor       : 1
BogoMIPS        : 50.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd08
CPU revision    : 1

processor       : 2
BogoMIPS        : 50.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd08
CPU revision    : 1

processor       : 3
BogoMIPS        : 50.00
Features        : fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid
CPU implementer : 0x41
CPU architecture: 8
CPU variant     : 0x0
CPU part        : 0xd08
CPU revision    : 1

root@moca112202:~# cat /proc/mtd
dev:    size   erasesize  name
mtd0: 003e0000 00001000 "u-boot"
mtd1: 00010000 00001000 "hw-info"
mtd2: 00010000 00001000 "u-boot-env"

root@moca112202:~# cat /etc/fw_env.config
# MTD device name   Device offset   Env. size   Flash sector size  Number of sectors
/dev/mtdblock2      0x0000          0x10000     0x1000             16

root@moca112202:~# fw_printenv
arch=arm
baudrate=115200
board=mvebu_armada-8k
board_name=mvebu_armada-8k
bootargs=console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000 root=/dev/nfs rw ip=0.0.0.0:0.0.0.0:10.4.50.254:255.255.255.0:marvell:eth0:none nfsroot=0.0.0.0:/srv/nfs/,tcp,v3 pci=pcie_bus_safe
bootcmd=ev 0; ext4load mmc 0:1 $kernel_addr_r $image_name; ext4load mmc 0:1 $fdt_addr_r $fdt_name; setenv bootargs $console root=PARTUUID=89708921-01 rw rootwait net.ifnames=0 biosdevname=0; booti $kernel_addr_r - $fdt_addr_r
bootdelay=2
console=console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000
cpu=armv8
eth1addr=00:51:82:11:22:01
eth2addr=00:51:82:11:22:02
ethact=mvpp2-0
ethaddr=00:51:82:11:22:00
ethprime=eth0
extra_params=pci=pcie_bus_safe
fdt_addr_r=0x6f00000
fdt_high=0xffffffffffffffff
fdt_name=boot/armada-7040-mochabin.dtb
fdtcontroladdr=7f625230
gatewayip=10.4.50.254
get_images=tftpboot $kernel_addr_r $image_name; tftpboot $fdt_addr_r $fdt_name; run get_ramfs
get_ramfs=if test "${ramfs_name}" != "-"; then setenv ramdisk_addr_r 0x8000000; tftpboot $ramdisk_addr_r $ramfs_name; else setenv ramdisk_addr_r -;fi
hostname=marvell
image_name=boot/Image
initrd_addr=0xa00000
initrd_size=0x2000000
ipaddr=0.0.0.0
kernel_addr_r=0x7000000
loadaddr=0x6000000
netdev=eth0
netmask=255.255.255.0
ramdisk_addr_r=-
ramfs_name=-
root=root=/dev/nfs rw
rootpath=/srv/nfs/
serverip=0.0.0.0
set_bootargs=setenv bootargs $console $root ip=$ipaddr:$serverip:$gatewayip:$netmask:$hostname:$netdev:none nfsroot=$serverip:$rootpath,tcp,v3 $extra_params $cpuidle
soc=mvebu
stderr=serial@512000
stdin=serial@512000
stdout=serial@512000
vendor=Marvell
root@moca112202:~#

root@moca112202:~# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04 LTS
Release:        18.04
Codename:       bionic

root@moca112202:~# free -h
              total        used        free      shared  buff/cache   available
Mem:           7.8G         87M        7.6G        3.0M         95M        7.6G
Swap:            0B          0B          0B

root@moca112202:~# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: sit0@NONE: <NOARP> mtu 1480 qdisc noop state DOWN group default qlen 1000
    link/sit 0.0.0.0 brd 0.0.0.0
3: eth0: <NO-CARRIER,BROADCAST,MULTICAST,SLAVE,UP> mtu 1500 qdisc mq master bond0 state DOWN group default qlen 2048
    link/ether 00:51:82:11:22:00 brd ff:ff:ff:ff:ff:ff
4: eth1: <BROADCAST,MULTICAST,PROMISC,UP,LOWER_UP> mtu 1508 qdisc mq state UP group default qlen 2048
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
    inet6 fe80::251:82ff:fe11:2201/64 scope link
       valid_lft forever preferred_lft forever
5: eth2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc mq master bond0 state UP group default qlen 2048
    link/ether 00:51:82:11:22:00 brd ff:ff:ff:ff:ff:ff
6: lan0@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br0 state LOWERLAYERDOWN group default qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
7: lan1@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br0 state LOWERLAYERDOWN group default qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
8: lan2@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br0 state LOWERLAYERDOWN group default qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
9: lan3@eth1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue master br0 state LOWERLAYERDOWN group default qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
10: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
    link/ether 00:51:82:11:22:00 brd ff:ff:ff:ff:ff:ff
    inet 10.4.2.110/24 brd 10.4.2.255 scope global bond0
       valid_lft forever preferred_lft forever
    inet6 2a01:e0a:8ab:34b0:a0d7:3dfe:5ce7:17d6/64 scope global temporary dynamic
       valid_lft 86153sec preferred_lft 85661sec
    inet6 2a01:e0a:8ab:34b0:251:82ff:fe11:2200/64 scope global dynamic mngtmpaddr
       valid_lft 86153sec preferred_lft 86153sec
    inet6 fe80::251:82ff:fe11:2200/64 scope link
       valid_lft forever preferred_lft forever
11: br0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 00:51:82:11:22:01 brd ff:ff:ff:ff:ff:ff
    inet 192.168.84.1/24 brd 192.168.84.255 scope global br0
       valid_lft forever preferred_lft forever

root@moca112202:~# lsblk
NAME         MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda            8:0    1 931.5G  0 disk
mtdblock0     31:0    0   3.9M  0 disk
mtdblock1     31:1    0    64K  1 disk
mtdblock2     31:2    0    64K  0 disk
mmcblk0      179:0    0  14.7G  0 disk
`-mmcblk0p1  179:1    0  14.7G  0 part /
mmcblk0boot0 179:32   0     4M  1 disk
mmcblk0boot1 179:64   0     4M  1 disk

root@moca112202:~# blkid
/dev/mmcblk0: PTUUID="89708921" PTTYPE="dos"
/dev/mmcblk0p1: LABEL="rootfs" UUID="136f4d0c-df1f-4617-96f1-1e18ff2578fd" TYPE="ext4" PARTUUID="89708921-01"

root@moca112202:~# lsusb
Bus 002 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 001 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub
Bus 004 Device 002: ID 0424:5434 Standard Microsystems Corp. Hub
Bus 004 Device 001: ID 1d6b:0003 Linux Foundation 3.0 root hub
Bus 003 Device 002: ID 0424:2134 Standard Microsystems Corp. Hub
Bus 003 Device 001: ID 1d6b:0002 Linux Foundation 2.0 root hub

root@moca112202:~# lspci
00:00.0 PCI bridge: Marvell Technology Group Ltd. Device 0110

root@moca112202:~# lscpu
Architecture:        aarch64
Byte Order:          Little Endian
CPU(s):              4
On-line CPU(s) list: 0-3
Thread(s) per core:  1
Core(s) per socket:  4
Socket(s):           1
NUMA node(s):        1
Vendor ID:           ARM
Model:               1
Model name:          Cortex-A72
Stepping:            r0p1
CPU max MHz:         1400.0000
CPU min MHz:         350.0000
BogoMIPS:            50.00
NUMA node0 CPU(s):   0-3
Flags:               fp asimd evtstrm aes pmull sha1 sha2 crc32 cpuid

</details>

<details>
  <summary>Click to expand first play with leds on factory Ubuntu...</summary>
root@moca112202:~# pwd
/root
root@moca112202:~# ls
leds-test.sh
root@moca112202:~# cat leds-test.sh
#!/bin/bash

function rgbled {
    local idx=$1
    local color=$2
    local r=0
    local g=0
    local b=0

    case "$color" in
    black)
      r=0; g=0; b=0;
      ;;
    blue)
      r=0; g=0; b=255;
      ;;
    green)
      r=0; g=255; b=0;
      ;;
    cyna)
      r=0; g=255; b=255;
      ;;
    red)
      r=255; g=0; b=0;
      ;;
    magenta)
      r=255; g=0; b=255;
      ;;
    yellow)
      r=255; g=255; b=0;
      ;;
    white)
      r=255; g=255; b=255;
      ;;
    *)
      r=0; g=0; b=0;
      ;;
    esac

    echo $r > /sys/class/leds/led${idx}\:red/brightness
    echo $g > /sys/class/leds/led${idx}\:green/brightness
    echo $b > /sys/class/leds/led${idx}\:blue/brightness
}

# turn off all leds
for led in {1..3};
do
    rgbled $led
done

# leds demo
for color in blue green cyna red magenta yellow white;
do
    for led in {1..3};
    do
        rgbled $led $color
        sleep 0.3
    done

    sleep 1
    for led in {1..3};
    do
        rgbled $led
    done
    sleep 0.3
done

</details>

MOCHAbin-V1-2-0 #22 Early Bird - LEDS video at x30 speed:
<video autosize="true" controls>
  <source src="/uploads/images/MochaBin-5G/MochaBin-5G@GlobalScaleTechnologies-LEDS.mp4" type="video/mp4">
</video>

```
gke@PRECISION:~/DEVEL/GST/MOCHAbin$ minicom -D /dev/ttyUSB0
```
<details>
  <summary>Click to expand first init to factory U-Boot with some few commands...</summary>
Bienvenue avec minicom 2.7.1

OPTIONS: I18n
Compilé le Dec 23 2019, 02:06:26.
Port /dev/ttyUSB0, 12:58:10

Tapez CTRL-A Z pour voir l'aide concernant les touches spéciales


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
Marvell>>
Marvell>>

Marvell>> version
U-Boot 2018.03-devel-18.12.3-ga49bd540df (Dec 30 2021 - 16:06:18 +0800)

aarch64-linux-gnu-gcc (Linaro GCC 7.3-2018.05) 7.3.1 20180425 [linaro-7.3-2018.]
GNU ld (Linaro_Binutils-2018.05) 2.28.2.20170706

Marvell>> help
?       - alias for 'help'
avs     - Set/Get Adaptive Voltage Scaling (AVS) value

base    - print or set address offset
bdinfo  - print Board Info structure
blkcache- block cache diagnostics and control
boot    - boot default, i.e., run 'bootcmd'
bootd   - boot default, i.e., run 'bootcmd'
bootefi - Boots an EFI payload from memory
bootelf - Boot from an ELF image in memory
booti   - boot arm64 Linux Image image from memory
bootm   - boot application image from memory
bootp   - boot image via network using BOOTP/TFTP protocol
bootvx  - Boot vxWorks from an ELF image
bubt    - Burn a u-boot image to flash
cmp     - memory compare
coninfo - print console devices and information
cp      - memory copy
crc32   - checksum calculation
dcache  - enable or disable data cache
dhcp    - boot image via network using DHCP/TFTP protocol
dm      - Driver model low level access
echo    - echo args to console
editenv - edit environment variable
env     - environment handling commands
exit    - exit script
ext2load- load binary file from a Ext2 filesystem
ext2ls  - list files in a directory (default /)
ext4load- load binary file from a Ext4 filesystem
ext4ls  - list files in a directory (default /)
ext4size- determine a file's size
ext4write- create a file in the root directory
false   - do nothing, unsuccessfully
fatinfo - print information about filesystem
fatload - load binary file from a dos filesystem
fatls   - list files in a directory (default /)
fatsize - determine a file's size
fdt     - flattened device tree utility commands
fstype  - Look up a filesystem type
go      - start application at address 'addr'
gpio    - query and control gpio pins
gzwrite - unzip and write memory to block device
help    - print command description/usage
hw_info - hw_info

i2c     - I2C sub-system
icache  - enable or disable instruction cache
iminfo  - print header information for application image
imxtract- extract a part of a multi-image
ir      - ir    - Reading and changing internal register values.

itest   - return true/false on integer compare
led     - manage LEDs
load    - load binary file from a filesystem
loadb   - load binary file over serial line (kermit mode)
loads   - load S-Record file over serial line
loadx   - load binary file over serial line (xmodem mode)
loady   - load binary file over serial line (ymodem mode)
loop    - infinite loop on address range
ls      - list files in a directory (default /)
lzmadec - lzma uncompress a memory region
map     - Display address decode windows

md      - memory display
mdio    - MDIO utility commands
mii     - MII utility commands
mm      - memory modify (auto-incrementing address)
mmc     - MMC sub system
mmcinfo - display MMC info
mw      - memory write (fill)
nfs     - boot image via network using NFS protocol
nm      - memory modify (constant address)
part    - disk partition related commands
pci     - list and access PCI Configuration Space
ping    - send ICMP ECHO_REQUEST to network host
printenv- print environment variables
pxe     - commands to get and boot from pxe files
regulator- uclass operations
reset   - Perform RESET of the CPU
run     - run commands in an environment variable
rx_training- rx_training <cp id> <comphy id>

save    - save file to a filesystem
saveenv - save environment variables to persistent storage
scsi    - SCSI sub-system
scsiboot- boot from SCSI device
setenv  - set environment variables
setexpr - set environment variable as the result of eval expression
sf      - SPI flash sub-system
showvar - print local hushshell variables
size    - determine a file's size
sleep   - delay execution for some time
source  - run script from memory
sspi    - SPI utility command
switch  - Switch Access commands
sysboot - command to get and boot from syslinux files
test    - minimal test like /bin/sh
tftpboot- boot image via network using TFTP protocol
time    - run commands and summarize execution time
true    - do nothing, successfully
tsen    - tsen - Display the SoC temperature.

unzip   - unzip a memory region
usb     - USB sub-system
usbboot - boot from USB device
version - print monitor, compiler and linker version
Marvell>>

Marvell>> print
arch=arm
baudrate=115200
board=mvebu_armada-8k
board_name=mvebu_armada-8k
bootargs=console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000 root=/dev/nfs rw ip=0.0.0.0:0.0.0.0:10.4.50.254:255.255.255.0:marvell:eth0:none nfsroot=0.0.0.0:/srv/nfs/,tcp,v3 pci=pcie_bus_safe
bootcmd=ev 0; ext4load mmc 0:1 $kernel_addr_r $image_name; ext4load mmc 0:1 $fdt_addr_r $fdt_name; setenv bootargs $console root=PARTUUID=89708921-01 rw rootwait net.ifnames=0 biosdevname=0; booti $kernel_addr_r - $fdt_addr_r
bootdelay=2
console=console=ttyS0,115200 earlycon=uart8250,mmio32,0xf0512000
cpu=armv8
eth1addr=00:51:82:11:22:01
eth2addr=00:51:82:11:22:02
ethact=mvpp2-0
ethaddr=00:51:82:11:22:00
ethprime=eth0
extra_params=pci=pcie_bus_safe
fdt_addr_r=0x6f00000
fdt_high=0xffffffffffffffff
fdt_name=boot/armada-7040-mochabin.dtb
fdtcontroladdr=7f625230
gatewayip=10.4.50.254
get_images=tftpboot $kernel_addr_r $image_name; tftpboot $fdt_addr_r $fdt_name; run get_ramfs
get_ramfs=if test "${ramfs_name}" != "-"; then setenv ramdisk_addr_r 0x8000000; tftpboot $ramdisk_addr_r $ramfs_name; else setenv ramdisk_addr_r -;fi
hostname=marvell
image_name=boot/Image
initrd_addr=0xa00000
initrd_size=0x2000000
ipaddr=0.0.0.0
kernel_addr_r=0x7000000
loadaddr=0x6000000
netdev=eth0
netmask=255.255.255.0
ramdisk_addr_r=-
ramfs_name=-
root=root=/dev/nfs rw
rootpath=/srv/nfs/
serverip=0.0.0.0
set_bootargs=setenv bootargs $console $root ip=$ipaddr:$serverip:$gatewayip:$netmask:$hostname:$netdev:none nfsroot=$serverip:$rootpath,tcp,v3 $extra_params $cpuidle
soc=mvebu
stderr=serial@512000
stdin=serial@512000
stdout=serial@512000
vendor=Marvell

Environment size: 1702/65532 bytes
Marvell>>

Marvell>> base
Base Address: 0x00000000
Marvell>> bdinfo
arch_number = 0x00000000
boot_params = 0x00000100
DRAM bank   = 0x00000000
-> start    = 0x00000000
-> size     = 0xC0000000
DRAM bank   = 0x00000001
-> start    = 0x100000000
-> size     = 0x140000000
baudrate    = 115200 bps
TLB addr    = 0x7FFF0000
relocaddr   = 0x7FF39000
reloc off   = 0x7FF39000
irq_sp      = 0x7F625220
sp start    = 0x7F625220
Early malloc usage: 3b8 / 2000
fdt_blob = 000000007f625230

Marvell>> mmcinfo
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

Marvell>> mmc list
sdhci@6e0000: 0 (eMMC)
Marvell>> mmc dev
switch to partitions #0, OK
mmc0(part 0) is current device
Marvell>> mmc part

Partition Map for MMC device 0  --   Partition Type: DOS

Part    Start Sector    Num Sectors     UUID            Type
  1     2048            30775296        89708921-01     83 Boot

Marvell>> fstype mmc 0:1
ext4
Marvell>> ext4ls mmc 0:1
<DIR>       4096 .
<DIR>       4096 ..
<DIR>      16384 lost+found
<DIR>       4096 bin
<DIR>       4096 boot
<DIR>       4096 dev
<DIR>       4096 etc
<DIR>       4096 home
<DIR>       4096 lib
<DIR>       4096 media
<DIR>       4096 mnt
<DIR>       4096 opt
<DIR>       4096 proc
<DIR>       4096 root
<DIR>       4096 run
<DIR>       4096 sbin
<DIR>       4096 srv
<DIR>       4096 sys
<DIR>       4096 tmp
<DIR>       4096 usr
<DIR>       4096 var

Marvell>> ext4ls mmc 0:1 /boot
<DIR>       4096 .
<DIR>       4096 ..
           23512 armada-7040-mochabin.dtb
<DIR>       4096 bootloader
        16519680 Image

Marvell>> map
AP-0 address decoding:
-----------
AP-0 CCU:
bank  id target   start              end
----------------------------------------------------
ccu   00 10  0x00000000f0000000 0x00000000f2000000
ccu   01 00  0x00000000f2000000 0x0000000100000000
ccu   02 00  0x00000000c0000000 0x00000000f0000000
ccu   03 00  0x0000000800000000 0x0000000900000000
ccu   GCR 0x3
-----------
AP-0 IOW:
bank  target     start              end
----------------------------------------------------
io-win 0  0x00000000fff00000 0x0000000000100000
io-win 0  0x00000000fd000000 0x00000000fd100000
io-win 1  0x00000000fe000000 0x00000000fe100000
io-win GCR - 0x3

AP-0 CP-0 address decoding:
AP-0 CP-0 IOB:
bank  id target  start              end
----------------------------------------------------
iob   00 CFG     0x00000000f2000000 0x00000000f3000000
iob   01 PEX1    0x00000000f7000000 0x00000000f8000000
iob   02 PEX2    0x00000000f8000000 0x00000000f9000000
iob   03 PEX2    0x00000000c0000000 0x00000000f0000000
iob   04 PEX2    0x0000000800000000 0x0000000900000000
iob   05 PEX0    0x00000000f6000000 0x00000000f7000000
iob   06 RUNIT   0x00000000f9000000 0x00000000fa000000
AP-0 CP-0 AMB addr.decode:
bank  attribute     base          size
--------------------------------------------
amb   0x001a        0xf9000000    0x01000000
Marvell>>

Marvell>> sspi
SF: Detected w25q32bv with page size 256 Bytes, erase size 4 KiB, total 4 MiB

Marvell>> scsi scan
scanning bus for devices...
  Device 0: (1:0) Vendor: ATA Prod.: WDC  WDS100T1R0B Rev: 4110
            Type: Hard Disk
            Capacity: 953869.7 MB = 931.5 GB (1953525168 x 512)

</details>
