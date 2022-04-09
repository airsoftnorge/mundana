---
layout: post
title: "ASN-TAK introduction and privacy"
author: "staff"
categories: [tak, guides]
tags: [asn-tak, atak, tak, featured]
image: assets\images\003_asn-tak\2022-03-19-introduction-to-tak\ASN-TAK.png
---

### ASN-TAK
For the purposes of airsoft, the <a href="https://en.wikipedia.org/wiki/Android_Team_Awareness_Kit" target="_blank">Team Awareness Kit (TAK)</a> is a software suite capable of supporting mission planning and navigation, as well as communication and coordination between individuals, squads and entire teams on the airsoft field.
To facilitate the use of TAK in support of airsoft games in Norway, AirsoftNorge has set up the ASN-TAK infrastructure, consisting of three dedicated TAK servers for public use by airsofters across Norway.

### Flavors of TAK
TAK comes in 3 main flavors that is relevant for airsoft, but have a different origin and purpose behind them, resulting in some key differences that may or may not be relevant for you.

[ATAK]({{site.baseurl}}/atak-setup) is the android version of the software originally created for the department of defense and has features that match up with this. More focus on elevation data, night vision compatibility and radio interfaces than the other.

[WinTAK]({{site.baseurl}}/wintak-setup) was created for the ops center and runs on Windows.

[ITAK]({{site.baseurl}}/itak-setup) was created on ios for the department of homeland security, and therefore is better suited for law enforcement and permissive environments. 


### Privacy concerns
* WinTAK, ITAK and ATAK uses the GPS/Location Services of your device to display your current geographic location, with a high degree of accuracy.
* This location is visible to anyone else connected to the same server(s).
* Unless you turn on location Services before opening the app, your position will be displayed to other users on the server immediately upon launching the app.
* Turning off location Services after opening app, will leave a marker displaying the location where Location Services were turned off.

**With this in mind, we highly recommend that you do not use any TAK app with Location Services activated, while located in or around your home, or your workplace.**<br>

Instead, while experimenting or familiarizing yourself with the app, keep Location Services turned off - and ensure that you close the app properly before turning them back on.
Another option is to use an Android emulator for PC (we have used <a href="https://www.bluestacks.com" target="_blank">Bluestacks</a> for this purpose in the past - which without GPS hardware will not give away your accurate location (*but may give the location of an ISP node near you*).
