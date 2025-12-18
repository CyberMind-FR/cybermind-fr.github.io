---
title: "Développement Kernel Linux"
date: 2025-12-14
categories:
  - Linux Kernel
  - Open Source
tags:
  - linux
  - kernel
  - drivers
  - arm
---

Article d'exemple sur le développement kernel.

## Prérequis

- Connaissance C
- Environnement de compilation
- Device Tree

## Créer un module

```c
#include <linux/module.h>
#include <linux/kernel.h>

static int __init hello_init(void) {
    printk(KERN_INFO "Hello World!\n");
    return 0;
}
```
