

<h1 align="center">RPG Game - Vintage Style</h1>

<p align="center">Single-player RPG Gamebook</p>

<div align="center"><a href="">
<img src="https://img.shields.io/static/v1?label=Game&labelColor=black&message=Download&color=7159c1&style=for-the-badge&logo=python"/></a>
</div>

Table of contents
===============
<!--ts-->

- [About](#about)
- [Autor](#autor)


<!--
- [Features](#features)
- [Instalation and how to use](#instalation-and-how-to-use)
	- [Requirements](#requirements)
	
	- [GUI - Graphical User Interface](#gui)
	
	- [Command-line interface](#cli)
	
	- [Windows Standalone](#standalone)
-	[Public key](#public-key)
-	[Tecnologies](#tecnologies)

<!--te-->
>
<br>

<div align="center">
<img src="https://i.postimg.cc/1tyqnY5B/citadel-07.png" alt="Dungeon" width="240"  title="Dungeon" />
</div>


## About

<p>Hi.</p>
<p> This is a scratch version of a RPG game. </p>
<p> You can switch between the frames in a click of a button. Thanks for youtuber sentdex for the great idea of using dictionaries and tkraise to enable this switching frames.</p>
<p>This game engine is the same of those old RPG game books, where you were given options and would go to page X or Y according to your choice. </p>




## Autor

[![flag-br-mini-mini.png](https://i.postimg.cc/DyXTfVHf/flag-br-mini-mini.png)](https://postimg.cc/Xp4hxPnt)
 [![flag-de-mini-mini.png](https://i.postimg.cc/4xGNrNyR/flag-de-mini-mini.png)](https://postimg.cc/nCdJmxq3)
 ✈️ ::statue_of_liberty::
 
<a href="https://github.com/AndersonFrossard" title="GitHub">
<img style="border-radius: 50%;" src="https://i.postimg.cc/Rqf7nM29/maxresdefault.jpg" width="100px;" alt=""/>
 <sub><b><br />Anderson Frossard</b></sub></a>
  
<br />
Done with ❤️ by Anderson Frossard 👋🏽 Get in contact!<br/><br/>

[![Gmail Badge](https://img.shields.io/badge/frossard2008@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:frossard2008@gmail.com)](mailto:frossard2008@gmail.com)
<!--

## Features
- [X] Gui Interface
- [x] Download video
- [x] Download audio
- [ ] Download full-playlist

## Instalation-and-how-to-use


### Requirements

>pytube 11.0.2 or greater

If you do not have pytube installed, you can install it by running this command:

	pip install pytube


## GUI - Graphical User Interface

This version runs both on GUI and CLI.

<h2>Running with GUI :</h2>

	python youtube_download.py

![GUI interface](./img/image01.png)

## CLI - Command Line Interface

<h2>Running with CLI :</h2>

	python youtube_download.py --nogui

![CLI interface](./img/image02.png)

## Standalone
## Standalone executable for Windows:

Perhaps you just want a fast way to get things running. The standalone executable will suit you well.
<ul>
	<li>Download the zip file</li>
	<li>Unzip the zip file into a new folder</li>
	<li>Check  integrity of zip file's content (optional)</li>
	<li>Double click on youtube_download.exe </li>
</ul>

### How to check whether the zipfile has not been tampered with:

First, you need to download my pgp public key and check if my public key has not been hacked or tampered with. In order to do that, you should download my public pgp key from two different sources.
They must have the same fingerprint and must not have been revoked.

[Check my Fingerprint here](#fingerprint)

### How to obtain my Public keys

[Public key](#public-key)


### How to check if the keys are correct and valid:

 Run this command to check fingerprint from diferent files:

	gpg --show-keys filename1.asc
 
 ![Checking fingerprints](./img/image04.png)
 
 If they both have my [fingerprint](#fingerprint) and have not been revoked, good, the key is valid and secure for use. 

Import my pgp public signature key:

	gpg --import frossard.public.key.asc

Check wether youtube_download.zip has been signed by myself:

	gpg --verify youtube_download.sig

To pass verification you should see a message saying
>Good signature from Anderson Frossard. (Das ist meine key. Wir ziehen voran!)

gpg will probably also say this signature is not certified. That´s because you have just downloaded it and have not applied command *trust* to it.

Once the gpg has verified the  file has been signed by myself, you are safe to unzip it and run its executable. 

Optionally, for aditional security you can hash your youtube_download.exe file and compare with my hash:

<table>
	<tr>
		<td>SHA-256</td>
		<td>File</td>
	<tr>
		<td>36F4E8E51035045AD3A79DD7067317DC54CE2ADB6690D6D0972238F1B0AA9D6D</td>
		<td>youtube_download.exe</td>
	</tr>
</table>

The hash must be exactly the same. 

## Public-key

My PGP public key is avaiable at:

[Public Key at Github](https://github.com/AndersonFrossard/karoua_youtube_download_gui/tree/main/standalone/frossard_public_key.asc)

[PGP Global Directory](https://keyserver2.pgp.com/vkd/DownloadKey.event?keyid=0xB79AAE8846C18DF7)

[![PGP 0x46C18DF7](https://peegeepee.com/badge/orange/46C18DF7.svg)](https://d.peegeepee.com/921D2E998D1E3213DFCF74F7B79AAE8846C18DF7.asc)

### Fingerprint
My PGP public key full fingerprint is:

	921D 2E99 8D1E 3213 DFCF 74F7 B79A AE88 46C1 8DF7
	
My PGP public key fingerprint key ID is:

	46C1 8DF7

Enjoy!



## Tecnologies

Solely written in Python 3.8.7.<br />
Libraries imported:
<ul>
<li>pytube</li>
<li>sys</li>
<li>tkinter</li>
<li>threading</li>
<li>Pillow</li>
<li>io</li>
</ul>
<br />
