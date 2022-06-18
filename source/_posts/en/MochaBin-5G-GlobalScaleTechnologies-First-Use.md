---
title: MochaBin-5G@GlobalScaleTechnologies - First Use
lang: en
date: 2022-05-10 07:07:07
tags:
- MOCHAbin
- Armada
- SECUBOX
- OpenWrt
- contribute
categories: Cyber
---

I already plan to Sell or CrowdFund a personal, secure, home cloud box.
It is only in prototyping stage.
The first candidate was the ESPRESSOBIN which came in a trap, because of a annoying MARVELL CPU BUGS which is still unresolved !
I actually use and customize one of the first 20th sale MOCHABIN from the first CrowdFunded campaign of GlobalScaleTechnologies...

Software will mainly be based on OpenWrt, NextCloud and CrowdSec, and will be enhanced with some other cool add-ons.
It is all based on GNU softwares.

Some for OpenWrt main system itself, others for the Dockerized components, and also some cool tweaks, scripts and features developed from my now long experiences about all these usage.

It make years now my own servers are daily used, from the first SheevaPlugs through GuruPlugs and others...

It makes more form my first PC (One of the first PENTIUM Pro 200 bought directly from a trip to USA/California, called Milenium, installed with a REDHAT and becoming the GK2.NET ISP provider at the very first beginning of what become the Internet...)

May be I will shared this story, also, one day ! 


<!-- more -->

Soon to come:
- how to expand the file system at upgrade and at first flash
- how to automatically reinstall packages while upgrade OS
- how to flash and boot on SD/USB/SATA
- how to install DOCKER (NPM, NC, CALIBRE,...)
- how to secure your home cloud with CrowdSec & FireWall
- how to monitor with glances
- how to send alerts by email on SSH successful attempts

<details>
  <summary>Click to expand first Flash to Snapshot OpenWrt from factory U-Boot...</summary>

[Get the squashfs SnapShot firmware binary file @openWrt](https://downloads.openwrt.org/snapshots/targets/mvebu/cortexa72/openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz)

Copy the downloaded archive on an USB key format in FAT32 or EXT4 (untested)

# 1 - Command for fast flash
```
setenv refactory 'usb stop; usb start; load usb 0:1 $kernel_addr_r $firmware_file; gzwrite mmc 0 $kernel_addr_r $filesize;'
setenv firmware_file 'openwrt-mvebu-cortexa72-globalscale_mochabin-squashfs-sdcard.img.gz'

saveenv
run refactory

Marvell>> run refactory;
reset;
```
</details>

I share also some snapshots.
The first use and tests give very attractive specs !

<img src="/uploads/images/MochaBin-5G/FIRST-TEST/GST@MochaBin-5G_STARGATE - Overview - LuCI.png" width="500px">
Overview - LuCI

<img src="/uploads/images/MochaBin-5G/FIRST-TEST/GST@MochaBin-5G_STARGATE - Containers - LuCI.png" width="500px">
Dockers' Containers - LuCI

<img src="/uploads/images/MochaBin-5G/FIRST-TEST/GST@MochaBin-5G_OpenWrt - Glances.png" width="500px">
Glances Monitoring

<img src="/uploads/images/MochaBin-5G/FIRST-TEST/GST@MochaBin-5G_Paramètres - TRIBU.png" width="500px">
NextCloud


Stay tuned...