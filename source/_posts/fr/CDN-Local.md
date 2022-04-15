---
title: CDN Local
lang: fr
date: 2014-11-11 00:00:00
tags: 
- CLOUD
- CyberSecurity
categories: Cyber
---

= CDN Local =

À l'origine le billet suivant m'a beaucoup interpelé :
[Héberger son propre CDN local](http://blog-libre.org/index.php/post/2014/10/29/heberger-son-propre-cdn-local)

<blockquote>
Dernièrement, je vous parlais d’une petite astuce de pistage et m’interrogeais sur la recherche d’une solution à cette problématique.
Aujourd’hui, je vous propose de mettre en place votre propre CDN pour des ressources de plus en plus utilisées (script jquery par exemple) à partir d’autres CDN ou du site de leur éditeur respectif.
</blockquote>

<!-- more -->

Un CDN, ou [Content delivery network](https://fr.wikipedia.org/wiki/Content_delivery_network) est une manière simple de se faire tracer.

Tous les sites utilises ces contenus pour créer et diffuser leur pages, et nous, utilisateurs, sommes ainsi surveillables par les hébergeur de ces CDN (google entre autre) !

Pouvoir utiliser les api google sans se faire tracer par google ?

Tout au moins sans télécharger les .js depuis google…

J'ai donc tenté d'adapter sur OpenWRT pour un mode transparent sur mon routeur, mais l'espace nécessaire est trop important et mon routeur ne fait que 4Mo !

Par contre, techniquement, ça marche !!!

== Privoxy Redirect et CDN Local (Debian) ==

LOCALCDN → 192.168.5.55:8180

CACHE → 192.168.5.55:8118

=== PRIVOXY ===

```
$ apt-get install privoxy
```

==== CONFIG ====

```
# cat /etc/privoxy/config
```

<details>
  <summary>/etc/privoxy/config</summary>
```
confdir /etc/privoxy
logdir /var/log/privoxy/
filterfile default.filter
logfile privoxy.log
actionsfile match-all.action # Actions that are applied to all sites and maybe overruled later on.
actionsfile default.action   # Main actions file
actionsfile user.action   # User customizations
##listen-address  127.0.0.1:8118
listen-address    192.168.5.55:8118
toggle  1
enable-remote-toggle  1
enable-remote-http-toggle  0
enable-edit-actions 1
enforce-blocks 0
buffer-limit 4096
forwarded-connect-retries  0
##accept-intercepted-requests 0
# We will be doing intercepting proxying
accept-intercepted-requests 1
allow-cgi-request-crunching 0
split-large-forms 0
keep-alive-timeout 300
socket-timeout 300
permit-access  192.168.1.0/24
debug   1    # show each GET/POST/CONNECT request
debug   128  # show redirects
debug   4096 # Startup banner and warning
debug   8192 # Errors - *we highly recommended enabling this*
#admin-address privoxy-admin@example.com
#proxy-info-url http://www.example.com/proxy-service.html
```
</details>

==== USER.ACTION ====

```
# cat /etc/privoxy/user.action
```

<details>
  <summary>/etc/privoxy/user.action</summary>
```
#####
##
## LOCAL CDN PROXY
##
#####

# Redirect remote requests to the local version delivered localhost
{ +redirect{s@^http:/[^(.*)]@http://192.168.5.55:8180/index.php?q=$1@} }

# AngularJS
ajax.googleapis.com/ajax/libs/angularjs/[0-9\.]*/angular.min.js

# Dojo
ajax.googleapis.com/ajax/libs/dojo/[0-9\.]*/dojo/dojo.js

# Ext Core
ajax.googleapis.com/ajax/libs/ext\-core/[0-9\.]*/ext\-core.js

# Jquery
ajax.googleapis.com/ajax/libs/jquery/[0-9\.]*/jquery(.min)?.js.*
ajax.aspnetcdn.com/ajax/jQuery/jquery-[0-9\.]*(.min)?.js
cdn.jsdelivr.net/jquery/([0-9\.]*)/jquery(-[0-9\.]*)?(.min)?.js
cdnjs.cloudflare.com/ajax/libs/jquery/[0-9\.]*\-?(rc|beta)?[0-9]?/jquery(.min)?.js

# MooTools
ajax.googleapis.com/ajax/libs/mootools/[0-9\.]*/mootools-yui-compressed.js

# Prototype
ajax.googleapis.com/ajax/libs/prototype/[0-9\.]*/prototype.js

# script.aculo.us
ajax.googleapis.com/ajax/libs/scriptaculous/[0-9\.]*/scriptaculous.js

# SWFObject
ajax.googleapis.com/ajax/libs/swfobject/[0-9\.]*/swfobject.js
cdnjs.cloudflare.com/ajax/libs/swfobject/[0-9\.]*/swfobject.js

# three.js
ajax.googleapis.com/ajax/libs/threejs/r[0-9]*/three.min.js
cdn.jsdelivr.net/threejs/r[0-9]*/three.min.js
cdnjs.cloudflare.com/ajax/libs/three.js/r[0-9]*/three(.min)?.js

# Web Font Loader
ajax.googleapis.com/ajax/libs/webfont/[0-9\.]*/webfont.js
```
</details>

```
# service privoxy restart
```

==== apache2 ====

```
$ apt-get install apache2
$ apt-get install php5-cgi
$ apt-get install php5-curl
```

===== LOCAL CDN =====

```
# cat /etc/apache2/ports.conf
```

```
NameVirtualHost *:8180
Listen 8180
```

```
# cat /etc/apache2/sites-available/privoxy
```

<details>
  <summary>/etc/apache2/sites-available/privoxy</summary>
```
<VirtualHost *:8180>
    ServerAdmin webmaster@localhost

    DocumentRoot /var/www/redirect
    <Directory />
   Options FollowSymLinks
        AllowOverride None
    </Directory>
    <Directory /var/www/redirect>
        Options Indexes FollowSymLinks MultiViews
        AllowOverride None
        Order allow,deny
        allow from all
    </Directory>

    ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
    <Directory "/usr/lib/cgi-bin">
        AllowOverride None
        Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
        Order allow,deny
        Allow from all
    </Directory>

    ErrorLog ${APACHE_LOG_DIR}/privoxy_error.log

    # Possible values include: debug, info, notice, warn, error, crit,
    # alert, emerg.
    LogLevel warn

    CustomLog ${APACHE_LOG_DIR}/privoxy_access.log combined
</VirtualHost>
```
</details>

```
# a2ensite privoxy
```

===== REDIRECT =====

```
# cd /var/www/
# mkdir redirect
# cd redirect/
# wget http://blog-libre.org/wp-content/uploads/2014/10/redirect.tar.gz|http://blog-libre.org/wp-content/uploads/2014/10/redirect.tar.gz
# tar -zxf redirect.tar.gz
```

===== CUSTOM =====

```
# mv .htaccess .htaccess.off
```

```
# mv index.php index.php.orig
```

```
# nano index.php
# cat index.php
```

<details>
  <summary>/var/www/redirect/index.php</summary>
```
<?php

//echo '<pre>'.print_r($_SERVER, true).'</pre>';
//die();

// Adresse comunne pour toutes nos redirections
$mainUrl = 'http://'.$_SERVER['SERVER_NAME'].':'.$_SERVER['SERVER_PORT'];

// On rajoute 'http:/' devant l'adresse passée par Privoxy
// Pour déterminer l'url de la ressource que l'on redirige
$requestedUrl = 'http:/'.str_replace('index.php?q=','',$_SERVER['REQUEST_URI']);

// Liste des différents cdn supportés avec leur modèle d'url
$angularjsPatterns = include('patterns/angularjs.php');
$dojoPatterns = include('patterns/dojo.php');
$extcorePatterns = include('patterns/extcore.php');
$jqueryPatterns = include('patterns/jquery.php');
$mootoolsPatterns = include('patterns/mootools.php');
$prototypePatterns = include('patterns/prototype.php');
$scriptaculousPatterns = include('patterns/scriptaculous.php');
$swfobjectPatterns = include('patterns/swfobject.php');
$threejsPatterns = include('patterns/threejs.php');
$webfontPatterns = include('patterns/webfont.php');

/*
Non géré pour le moment, en attente d'une solution viable

jQuery Mobile
    snippet: <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jquerymobile/1.4.3/jquery.mobile.min.css" />
    <script src="//ajax.googleapis.com/ajax/libs/jquerymobile/1.4.3/jquery.mobile.min.js"></script>
    site: http://jquerymobile.com/

jQuery UI
    snippet: <link rel="stylesheet" href="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css" />
    <script src="//ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/jquery-ui.min.js"></script>
    site: http://jqueryui.com/
*/

/* AngularJS
   snippet: <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.26/angular.min.js"></script>
   site: http://angularjs.org
*/
if (preg_match('/('.implode('|', $angularjsPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/angularjs.php');
    $cdn = new Angularjs($matches[2]);
}

/* Dojo
   snippet: <script src="//ajax.googleapis.com/ajax/libs/dojo/1.10.1/dojo/dojo.js"></script>
   site: http://dojotoolkit.org/
*/
if (preg_match('/('.implode('|', $dojoPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/dojo.php');
    $cdn = new Dojo($matches[2]);
}

/* Ext Core
   snippet: <script src="//ajax.googleapis.com/ajax/libs/ext-core/3.1.0/ext-core.js"></script>
   site: https://www.sencha.com/products/extcore/
*/
if (preg_match('/('.implode('|', $extcorePatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/extcore.php');
    $cdn = new Extcore($matches[2]);
}

/* jQuery
     Marche pour les versions min ou normale => force à télécharger la version min si absente
     snippet: <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
   snippet: <script src="//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js"></script>
   site: http://jquery.com/
*/
if (preg_match('/('.implode('|', $jqueryPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/jquery.php');
    $cdn = new Jquery($matches[2]);
}

/* MooTools
   snippet: <script src="//ajax.googleapis.com/ajax/libs/mootools/1.5.1/mootools-yui-compressed.js"></script>
   site: http://mootools.net/
*/
if (preg_match('/('.implode('|', $mootoolsPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/mootools.php');
    $cdn = new Mootools($matches[2]);
}

/* Prototype
   snippet: <script src="//ajax.googleapis.com/ajax/libs/prototype/1.7.2.0/prototype.js"></script>
   site: http://prototypejs.org/
*/
if (preg_match('/('.implode('|', $prototypePatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/prototype.php');
    $cdn = new Prototype($matches[2]);
}

/* script.aculo.us
    snippet: <script src="//ajax.googleapis.com/ajax/libs/scriptaculous/1.9.0/scriptaculous.js"></script>
    site: http://script.aculo.us/
*/
if (preg_match('/('.implode('|', $scriptaculousPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/scriptaculous.php');
    $cdn = new Scriptaculous($matches[2]);
}

/* SWFObject
   snippet: <script src="//ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js"></script>
   site: http://code.google.com/p/swfobject/
*/
if (preg_match('/('.implode('|', $swfobjectPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/swfobject.php');
    $cdn = new Swfobject($matches[2]);
}

/* three.js
     Marche pour les versions min ou normale => force à télécharger la version min si absente
   snippet: <script src="//ajax.googleapis.com/ajax/libs/threejs/r67/three.min.js"></script>
   site: http://threejs.org/
*/
if (preg_match('/('.implode('|', $threejsPatterns).')/i', $requestedUrl, $matches)){
    require_once('classes/threejs.php');
    $cdn = new Threejs($matches[2]);
}

/* Web Font Loader
   snippet: <script src="//ajax.googleapis.com/ajax/libs/webfont/1.5.3/webfont.js"></script>
   site: https://github.com/typekit/webfontloader
*/
if (preg_match('/('.implode('|', $webfontPatterns).')/i', $requestedUrl, $matches)){
//echo '<pre>'.print_r($matches, true).'</pre>'; die();
    require_once('classes/webfont.php');
    $cdn = new Webfont($matches[2]);
}

if ($cdn){

    // Fichier local manquant ?
    if (!file_exists($cdn->getFilename())){
    // On télécharge et stocke
   $cdn->get();
    }
    // On redirige vers notre ressource locale
    $requestedUrl = $mainUrl.$cdn->file;

    // On redirige et sort du script
    header("Status: 302 Found", true, 302);
    header("Location: {$requestedUrl}");
}else{
        echo '<pre>';
        echo print_r($_SERVER, true);
        echo "NO MATCH";
        echo $requestedUrl;
        echo $mainURL;
        echo '</pre>';

//        die();
}

?>
```
</details>

```
# chown www-data:www-data -R /var/www/redirect
```

```
# service apache2 restart
```

==== TEST ====

==== LOCAL CDN ====

>> [http://192.168.5.55:8180/index.php](http://192.168.5.55:8180/index.php)

===== PROXY =====

PROXY : 80
192.168.5.55:8118

===== PRIVOXY STATUS =====

>> [http://config.privoxy.org/](http://config.privoxy.org/)

==== DEMO ====

===== ACCESS =====

```
# tail /var/log/apache2/privoxy_access.log
```

<details>
  <summary>/var/log/apache2/privoxy_access.log</summary>
```
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js HTTP/1.1" 302 384 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /libs/swfobject/2.2/swfobject.js HTTP/1.1" 404 515 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /index.php?q=ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js HTTP/1.1" 302 384 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /libs/jquery/1.8.2/jquery.min.js HTTP/1.1" 404 516 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js HTTP/1.1" 302 383 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:36:22 +0100] "GET /libs/swfobject/2.2/swfobject.js HTTP/1.1" 404 514 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:38:05 +0100] "GET /index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js HTTP/1.1" 302 384 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:38:05 +0100] "GET /libs/swfobject/2.2/swfobject.js HTTP/1.1" 200 4299 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:38:05 +0100] "GET /index.php?q=ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js HTTP/1.1" 302 384 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"\\
192.168.5.55- - [11/Nov/2014:16:38:06 +0100] "GET /libs/jquery/1.8.2/jquery.min.js HTTP/1.1" 200 33753 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:33.0) Gecko/20100101 Firefox/33.0"
```
</details>

===   ===

=== PROXY ===

```
# tail /var/log/privoxy/privoxy.log
```

<details>
  <summary>/var/log/privoxy/privoxy.log</summary>
```
2014-11-11 16:47:12.233 b3d52470 Redirect: pcrs command "s@^http:/[^(.*)]@http://192.168.5.55:8180/index.php?q=$1@" changed "http://ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js" to "http://192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js" (1 hit).
2014-11-11 16:47:12.233 b4d52470 Redirect: pcrs command "s@^http:/[^(.*)]@http://192.168.5.55:8180/index.php?q=$1@" changed "http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" to "http://192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js" (1 hit).
2014-11-11 16:47:12.234 b3d52470 Redirect: New URL is: http://192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js
2014-11-11 16:47:12.234 b4d52470 Redirect: New URL is: http://192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js
2014-11-11 16:47:12.296 b4d52470 Request: 192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js
2014-11-11 16:47:12.296 b3d52470 Request: 192.168.5.55:8180/index.php?q=ajax.googleapis.com/ajax/libs/swfobject/2.2/swfobject.js
2014-11-11 16:47:12.314 b4d52470 Request: 192.168.5.55:8180/libs/swfobject/2.2/swfobject.js
2014-11-11 16:47:12.316 b3d52470 Request: 192.168.5.55:8180/libs/jquery/1.8.2/jquery.min.js
```
</details>

=== CACHE ===

```
# ls /var/www/redirect/libs/ -R
```

<details>
  <summary>/var/log/privoxy/privoxy.log</summary>
```
/var/www/redirect/libs/:
jquery    swfobject

/var/www/redirect/libs/jquery:
1.8.2

/var/www/redirect/libs/jquery/1.8.2:
jquery.min.js

/var/www/redirect/libs/swfobject:
2.2

/var/www/redirect/libs/swfobject/2.2:
swfobject.js
```
</details>

==== Utilisation avec Firefox ====

Pour le mode proxy non transparent, définir l'IP et le port de privoxy :
```
PROXY (HTTP uniquement) -> 192.168.5.55
PORT -> 8118
```
et ajouter les exclusions du réseau local :
```
localhost, 127.0.0.1, local, 192.168.5.0/24
```