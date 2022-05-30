---
title: EspressoBin@GlobalScaleTechnologies - UEFI BOOT
lang: en
date: 2022-05-30 22:00:00
tags:
- EspressoBin
- Armada
- SECUBOX
- UEFI
- BOOT
categories: Cyber
---

Here are some notes about pasts and successfull experiments with UEFI boot from u-boot on ARM64 EspressoBin.

They were done on the 8th of september 2020 for OPNSense and on the 19th oo july 2021.
I still had to make a detailed howto, but it may be usefull for advanced users waiting for some tests.

They may also work 'as-is' or mainly close to on MochaBIn but I have not tested.

<!-- more -->

## IPFIRE TRY

```
usb reset
load usb 0:2 $kernel_addr_r /efi/boot/bootaa64.efi
load usb 0:1 $fdt_addr_r /dtb-5.10.50-ipfire/marvell/armada-3720-espressobin-v7-emmc.dtb
bootefi $kernel_addr_r $fdt_addr_r
... BOOT OK Linux lts
```

USB2 = KO
USB3 = OK

## OPNSENSE TRY

```
=> setenv fdt_name 'dtb/marvell/armada-3720-espressobin.dtb'
=> setenv image_name 'EFI/BOOT/bootaa64.efi'
=> setenv bootmmc 'mmc dev 0;fatload mmc 0:1 $kernel_addr $image_name;fatload mmc 0:1 $fdt_addr $fdt_name; bootefi $kernel_addr'
=> run bootmmc
```

Will be updated soon...
Keep your eyes open.

Take care, shared as is, use it at your own risks !