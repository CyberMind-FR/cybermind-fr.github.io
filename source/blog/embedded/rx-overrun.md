---
title: "RX Overrun : chronique d’un débordement réseau"
date: 2026-01-12 11:42:33
tags:
  - réseau
  - openwrt
  - kernel
  - debugging
  - rétro-tech
categories:
  - Embedded
  - Cybermind
description: "Analyse technique d’un bug RX overrun sur interface Ethernet, rédigée à la manière d’un magazine informatique vintage."
---

> *Rubrique : entrailles du système, papier mat et café froid.*

## Introduction

Il arrive que la machine, pourtant stable depuis des jours, se mette à murmurer.
Non pas par l’interface graphique, mais dans les profondeurs du journal noyau,
là où les messages sont rares et précis.

Un soir, entre deux paquets, cette ligne apparaît :

```
bad rx status (overrun error), size=984
```

Phrase courte. Ton sec. Diagnostic implicite.
Nous sommes face à un **RX overrun**.

## Autopsie du message noyau

Un *overrun* en réception signifie une chose simple :
le contrôleur Ethernet a reçu plus de données que le système
n’a pu en traiter dans le temps imparti.

Les buffers débordent,
le descripteur DMA signale l’erreur,
le paquet est abandonné.

La taille indiquée (984 octets) est modeste.
Ce n’est pas la trame qui est excessive,
c’est le **rythme** qui est en cause.

## Anatomie d’un RX overrun

### 1. Anneaux DMA sous-dimensionnés

Les contrôleurs Ethernet fonctionnent avec des anneaux de descripteurs.
Trop petits, ils saturent lors de rafales réseau.

Dans l’ancienne école,
on appelait cela une économie mal placée.

### 2. CPU et interruptions

Sur nombre de plateformes embarquées,
un seul cœur gère les interruptions réseau.
Lorsque les softirq s’accumulent,
la réception prend du retard.

Symptôme classique :
`ksoftirqd` s’emballe,
les compteurs RX erreurs augmentent.

### 3. Offloads matériels trop ambitieux

GRO, TSO, checksum offload.
Des promesses de performance,
mais parfois des pièges subtils
selon la version du noyau et du pilote.

Désactiver ces raffinements
permet souvent de rétablir un comportement sain.

### 4. Absence de régulation du flux

Sans flow control,
l’émetteur parle sans se soucier
de la capacité d’écoute du récepteur.

Le réseau devient un monologue.

## Méthode de dépannage recommandée

### Observer avant d’agir

Consulter les compteurs :
- erreurs RX
- paquets perdus
- FIFO overruns

Noter l’instant, la charge, le contexte.

### Élargir les buffers

Augmenter la taille des rings RX/TX
lorsque le pilote le permet.
C’est souvent la correction la plus efficace.

### Simplifier la chaîne

Désactiver temporairement les offloads matériels.
Revenir à un chemin de données plus direct.

Dans les années 80,
on appelait cela retirer les options inutiles.

### Répartir la charge CPU

Activer la répartition de réception (RPS)
afin que le réseau ne repose pas sur un seul cœur.

Une machine équilibrée est une machine discrète.

### Vérifier le monde physique

Changer de câble.
Changer de port de switch.
Vérifier duplex et négociation.

Le bug le plus abstrait
disparaît parfois avec un geste très concret.


## Commandes OpenWrt : diagnostic & remèdes

> *Outils de terrain. Rien de magique : on mesure, on ajuste, on confirme.*

### Pré-requis (si nécessaire)

Sur OpenWrt, certains outils ne sont pas installés par défaut :

```sh
opkg update
opkg install ethtool ip-full kmod-sched-core
# optionnel selon le besoin
opkg install irqbalance
```

> Si `ethtool` n’existe pas sur ta cible (build minimal), utilise au moins `ip`, `logread` et `/proc`.

### 1) Confirmer les symptômes

Voir l’état du lien et les compteurs d’erreurs :

```sh
ip -s link show dev eth0
ip -d link show dev eth0
```

Chercher les messages noyau associés :

```sh
logread -k | grep -iE 'mvneta|eth0|overrun|bad rx status'
dmesg | grep -iE 'mvneta|eth0|overrun|bad rx status'
```

Si `ethtool` est disponible, récupérer les statistiques du pilote (très parlant) :

```sh
ethtool eth0
ethtool -S eth0 | egrep -i 'rx|drop|over|err|fifo|miss|buf'
```

### 2) Regarder la charge IRQ et softirq

Le RX overrun est souvent un “CPU trop lent pour avaler”.

```sh
cat /proc/interrupts | grep -iE 'eth|mvneta'
top -H   # surveille ksoftirqd, sirq et la saturation d’un seul cœur
cat /proc/softirqs | head -n 30
```

**Indice** : si une seule CPU concentre les IRQ réseau, les overruns montent sous rafale.

Optionnel : activer `irqbalance` (si pertinent sur ta plateforme SMP) :

```sh
/etc/init.d/irqbalance enable
/etc/init.d/irqbalance start
```

### 3) Augmenter les rings RX/TX (buffers DMA)

Afficher les valeurs actuelles :

```sh
ethtool -g eth0
```

Tenter d’augmenter (valeurs à adapter à ce que le driver accepte) :

```sh
ethtool -G eth0 rx 1024 tx 1024
```

Re-tester trafic + compteurs.

### 4) Tester en désactivant les offloads (GRO/GSO/TSO…)

C’est une étape de diagnostic rapide : si les erreurs chutent, tu as trouvé un levier.

```sh
ethtool -k eth0
ethtool -K eth0 gro off gso off tso off rx off tx off sg off
```

> Si ta perf baisse mais que la stabilité revient, garde une config “mixte” : réactive un offload à la fois pour trouver le coupable.

### 5) Flow control (pause frames)

Vérifier puis activer RX/TX pause :

```sh
ethtool -a eth0
ethtool -A eth0 rx on tx on
```

Utile quand un équipement en amont “arrose” trop vite (NAS, switch, backbone).

### 6) EEE (Energy Efficient Ethernet) et négociation du lien

EEE peut provoquer des latences ou micro-coupures sur certains combos matériel/switch.

```sh
ethtool --show-eee eth0 2>/dev/null
ethtool --set-eee eth0 eee off 2>/dev/null
```

Vérifier vitesse/duplex :

```sh
ethtool eth0
```

Et, pour tester, forcer temporairement (à utiliser prudemment) :

```sh
# exemple : forcer 1G full duplex (si supporté)
ethtool -s eth0 speed 1000 duplex full autoneg off
```

### 7) MTU et trames “jumbo”

S’assurer que tout le segment LAN parle la même langue (1500 vs 9000).

```sh
ip link show dev eth0
ip link set dev eth0 mtu 1500
```

### 8) RPS/RFS (répartir la réception sur plusieurs cœurs)

Sur systèmes multi-cœurs, RPS aide parfois beaucoup.

Lister les queues RX :

```sh
ls -1 /sys/class/net/eth0/queues/ | grep rx
```

Exemple : activer RPS sur `rx-0` pour CPU0-CPU1 (masque `3` = binaire `11`) :

```sh
echo 3 > /sys/class/net/eth0/queues/rx-0/rps_cpus
cat /sys/class/net/eth0/queues/rx-0/rps_cpus
```

> Adapte le masque à ton nombre de CPU. (CPU0-CPU3 => masque `f`)

### 9) Capturer le moment où ça casse

Si l’erreur arrive sous charge, lance un petit stress test et observe :

```sh
# depuis un autre hôte : iperf3 -c <IP_DU_ROUTEUR> -P 4 -t 30
# côté routeur :
logread -f | grep -iE 'mvneta|overrun|bad rx'
```

### 10) Rendre les réglages persistants

OpenWrt n’applique pas forcément ces réglages au reboot.
Deux approches simples :

**A. /etc/rc.local** (rapide)

```sh
# /etc/rc.local (avant 'exit 0')
ethtool -G eth0 rx 1024 tx 1024
ethtool -K eth0 gro off gso off tso off rx off tx off sg off
ethtool -A eth0 rx on tx on
exit 0
```

**B. Hotplug net** (propre quand l’interface monte)

Créer `/etc/hotplug.d/net/99-eth0-tuning` :

```sh
#!/bin/sh
[ "$ACTION" = "ifup" ] || exit 0
[ "$INTERFACE" = "lan" ] || exit 0

# Adapter si ton eth0 est bien derrière 'lan'
ethtool -G eth0 rx 1024 tx 1024 2>/dev/null
ethtool -K eth0 gro off gso off tso off rx off tx off sg off 2>/dev/null
ethtool -A eth0 rx on tx on 2>/dev/null
```

Puis :

```sh
chmod +x /etc/hotplug.d/net/99-eth0-tuning
```

---


## Conclusion

Le RX overrun n’est pas une panne brutale.
C’est un avertissement.

Il rappelle que le réseau reste
une affaire de temps,
de buffers,
et de discipline.

Dans un monde de couches abstraites,
ce message noyau nous ramène
à une vérité ancienne :

> quand la machine parle bas,
> il faut l’écouter attentivement.

---

*Cybermind.fr – Embedded, rétro-futur et entrailles numériques.*
