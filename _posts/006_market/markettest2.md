---
layout: post
title: "MARKETTEST"
author: "ulfhednar"
categories: market
tags: []
image: assets/images/test.jpg
hidden: true
---

This guide covers the real time streaming protocol server available for use with [ASN-TAK](https://airsoftnorge.com/asn-tak-overview/).
Typical usecases for this is with drones using [ATAK UAS](https://www.civtak.org/2021/09/22/uas-tool-now-publicly-available/), your cellphone camera using ATAK ICU or any other RTSP compatible device/software feed to others in TAK.

ATAK ICU comes with the ATAK package, UAS tool can be downloaded from [tak.gov](https://tak.gov/).


#### Settings for ASN-TAK

It's important to only stream on your assigned team, as you do not want to broadcast your location to the other side.

* rtsp://red.airsoftnorge.com:8554/`YourCallsignHere`
* rtsp://blue.airsoftnorge.com:8554/`YourCallsignHere`
* rtsp://yellow.airsoftnorge.com:8554/`YourCallsignHere`

ASN-TAK will attempt to associate your callsigns last known location with the stream.

If your callsign does not match it will still be available in the video feed tab and location is assumed Lon/Lat 0.0.


Videofeed seen in WinTAK
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2022-05-27-rtps-asn/wintak-stream.png">
		<img src="/assets/images/005_guides/2022-05-27-rtps-asn/wintak-stream.png" width="640"/>
	</a>
</div>

Videofeed seen in ATAK
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2022-05-27-rtps-asn/atak-video.png">
		<img src="/assets/images/005_guides/2022-05-27-rtps-asn/atak-video.png" width="640"/>
	</a>
</div>

Feed from simulated drone shown in ATAK on a tablet.
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2022-05-27-rtps-asn/169atakuascrop.jpg">
		<img src="/assets/images/005_guides/2022-05-27-rtps-asn/169atakuascrop.jpg" width="640"/>
	</a>
</div>
