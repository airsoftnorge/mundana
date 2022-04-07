---
layout: post
title: "An Introduction to WinTAK"
author: "staff"
categories: [tak, guides]
tags: [asn-tak, wintak, tak]
image: assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/WINTAK_001.png
---


For the purposes of airsoft, the <a href="https://en.wikipedia.org/wiki/Android_Team_Awareness_Kit" target="_blank">Team Awareness Kit (TAK)</a> is a software suite capable of supporting mission planning and navigation, as well as communication and coordination between individuals, squads and entire teams on the airsoft field.
To facilitate the use of TAK in support of airsoft games in Norway, AirsoftNorge has set up the ASN-TAK infrastructure, consisting of three dedicated TAK servers for public use by airsofters across Norway.

In this article, we will cover the installation and initial setup of WinTAK on the windows platform for use with our ASN-TAK servers.

### WinTAK is only available through <a href="https://www.tak.gov" target="_blank">tak.gov</a>, which requires registration. 


**That being said, before installation, there are a few things you should consider with privacy in mind:**
* WinTAK can use the GPS/Location Services of your device to display your current geographic location, with a high degree of accuracy.
* This location is visible to anyone else connected to the same server(s).


With that out of the way, this is how you install and set up WinTAK-Civ for use with ASN-TAK:

Note: WinTAK requires your Windows installation to have English as the display language.


* First, download the following files and save them to your computer:

	* <a href="https://github.com/airsoftnorge/wintaksetup/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Certificate package for WinTAK</a> (Required to connect to ASN-TAK servers)
	* <a href="https://github.com/airsoftnorge/DTED2-Norway/archive/refs/heads/master.zip" target="_blank">ASN-TAK: Norway DTED2 Digital Elevation Data Package</a> (optional)
	* <a href="https://github.com/airsoftnorge/DTED2-Sweden/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Sweden DTED2 Digital Elevation Data Package</a> (optional)
	* <a href="https://github.com/airsoftnorge/DTED0-World/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Worldwide DTED0 Digital Elevation Data Package</a> (optional)<br>
<br>


### Setting up the servers.

Exctract the certificates to a folder of your choice

Open up WinTAK and in the bottom right corner click the TAK Network Status
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/1.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/1.png" width="640"/>
	</a>
</div>

From there select Manage Server Connections
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/2.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/2.png" width="640"/>
	</a>
</div>

This is where you add servers, for each one (Red, Blue, Yellow) you will need to complete the following steps:

Click Add Item
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/3.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/3.png" width="640"/>
	</a>
</div>

Fill in as follows
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/4.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/4.png" width="640"/>
	</a>
</div>

Select Install Certificate Authority:
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/5.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/5.png" width="640"/>
	</a>
</div>
Here you select the server.p12 file and use the password `atakatak` and click OK

Select Install Client Certificate
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/6.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/6.png" width="640"/>
	</a>
</div>
Here you select the ASN-TAK.p12 file and use the password `atakatak` and click OK

Click OK until you see the server as shown here
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/7.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/7.png" width="640"/>
	</a>
</div>

Repeat the steps for the remaining servers you want to add. 



### Importing elevation data.

Extract the DTED data to `C:\ProgramData\WinTAK\DTED`

Make sure the folder looks like this when done.
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/11.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/11.png" width="640"/>
	</a>
</div>

Restart WinTAK and you now will have elevation data.

Verify in the bottom when you mouse over an area.
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/10.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-introduction-to-wintak/10.png" width="640"/>
	</a>
</div>
