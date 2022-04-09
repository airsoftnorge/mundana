---
layout: post
title: "WinTAK setup guide"
author: "staff"
categories: [tak, guides]
tags: [asn-tak, wintak, tak]
image: assets/images/003_asn-tak/2022-04-06-wintak-setup/WINTAK_001.png
---

Please be aware of potential privacy concerns when using this software, read more [here]({{site.baseurl}}asn-tak-overview).

Note: WinTAK requires your Windows installation to have English as the display language.

* Download WinTAK from [TAK.gov](https://tak.gov) (Registration required)

* Download the following files and save them to your computer:

	* <a href="https://github.com/airsoftnorge/wintaksetup/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Certificate package for WinTAK</a> (Required to connect to ASN-TAK servers)
	* <a href="https://github.com/airsoftnorge/DTED2-Norway/archive/refs/heads/master.zip" target="_blank">ASN-TAK: Norway DTED2 Digital Elevation Data Package</a> (optional)
	* <a href="https://github.com/airsoftnorge/DTED2-Sweden/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Sweden DTED2 Digital Elevation Data Package</a> (optional)
	* <a href="https://github.com/airsoftnorge/DTED0-World/archive/refs/heads/main.zip" target="_blank">ASN-TAK: Worldwide DTED0 Digital Elevation Data Package</a> (optional)<br>


### Setting up the servers.

Exctract the certificates to a folder of your choice

Open up WinTAK and in the bottom right corner click the TAK Network Status
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/1.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/1.png" width="640"/>
	</a>
</div>

From there select Manage Server Connections
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/2.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/2.png" width="640"/>
	</a>
</div>

This is where you add servers, for each one (Red, Blue, Yellow) you will need to complete the following steps:

Click Add Item
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/3.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/3.png" width="640"/>
	</a>
</div>

Fill in as follows
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/4.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/4.png" width="640"/>
	</a>
</div>

Select Install Certificate Authority:
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/5.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/5.png" width="640"/>
	</a>
</div>
Here you select the server.p12 file and use the password `atakatak` and click OK

Select Install Client Certificate
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/6.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/6.png" width="640"/>
	</a>
</div>
Here you select the ASN-TAK.p12 file and use the password `atakatak` and click OK

Click OK until you see the server as shown here
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/7.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/7.png" width="640"/>
	</a>
</div>

Repeat the steps for the remaining servers you want to add. 



### Importing elevation data.

Extract the DTED data to `C:\ProgramData\WinTAK\DTED`

Make sure the folder looks like this when done.
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/11.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/11.png" width="640"/>
	</a>
</div>

Restart WinTAK and you now will have elevation data.

Verify in the bottom when you mouse over an area.
<div class="image-thumbnail">
	<a href="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/10.png">
		<img src="{{site.baseurl}}/assets/images/003_asn-tak/2022-04-06-wintak-setup/10.png" width="640"/>
	</a>
</div>
