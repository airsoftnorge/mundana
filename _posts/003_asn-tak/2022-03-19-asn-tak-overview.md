---
layout: post
title: "ASN-TAK introduction and information"
author: "staff"
categories: [tak]
tags: [asn-tak, featured]
image: assets/images/003_asn-tak/2022-03-19-asn-tak-overview/ASN-TAK.png
---

#### ASN-TAK
For the purposes of airsoft, the <a href="https://en.wikipedia.org/wiki/Android_Team_Awareness_Kit" target="_blank">Team Awareness Kit (TAK)</a> is a software suite capable of supporting mission planning and navigation, as well as communication and coordination between individuals, squads and entire teams on the airsoft field.
To facilitate the use of TAK in support of airsoft games in Norway, AirsoftNorge has set up the ASN-TAK infrastructure, consisting of three dedicated TAK servers for public use by airsofters across Norway. 

We also offer free to use [RTSP servers](https://airsoftnorge.com/rtps-asn/) for video feeds from drones or other sensors.

The servers are pruned on regular intervals to avoid cluttering. If you have a game area you want visible this should be done with data packages and uploaded to the servers when games are organized.

#### TAK software
TAK comes in 3 main flavors that is relevant for airsoft, but have a different origin and purpose behind them, resulting in some key differences that may or may not be relevant for you.

<i class="fa-brands fa-android"></i> [ATAK](/atak-setup) is the android version of the software originally created for the US department of defense and has features that match up with this. More focus on elevation data, night vision compatibility and radio interfaces for non permissive use. <br>
<i class="fa-brands fa-apple"></i> [ITAK](/itak-setup) was created on iOS for the US department of homeland security, and therefore is better suited for law enforcement and permissive environments. It features superior in city maps and support most basic TAK features. <br>
<i class="fa-brands fa-windows"></i> [WinTAK](/wintak-setup) was created for the ops center and runs on Windows. <br>



#### Supportive software:

* [TAK Tracker](https://play.google.com/store/apps/details?id=gov.tak.taktracker&hl=en&gl=US) is a less resource intensive app that allows you to passively feed location data into a TAK network of your choosing. Unlike the ATAK app, it features no maps, messaging or interaction with data packages. Despite these limited features, it could be useful for tracking individuals that do not have a need to actually interact actively with the TAK network, or if you have a spare *Android End User Device*, it could be used to track game objectives, vehicles or just about anything else you can think of.
* [ATAK UAS](https://tak.gov/plugins/uas-tool) Let's you controll drones via ATAK and share the [video stream](https://airsoftnorge.com/rtps-asn/) via a TAK server to your team. Available as a plugin for both ATAK and WinTAK.


#### Privacy concerns
* All TAK products use the GPS/Location Services of your device to display your current geographic location, with a high degree of accuracy.
* Your location is visible to anyone else connected to the same server(s).
* While ASN does not record or store data sent through ASN-TAK any user can.
* Unless you turn on location Services before opening the app, your position will be displayed to other users on the server immediately upon launching the app.
* Turning off location Services after opening app, will leave a marker displaying the location where Location Services were turned off.
**With this in mind, we highly recommend that you do not use any TAK app with Location Services activated, while located in or around your home, or your workplace.**<br>

While experimenting or familiarizing yourself with the app, keep Location Services turned off - and ensure that you close the app properly before turning them back on.
Another option is to use an Android emulator for PC (we have used <a href="https://www.bluestacks.com" target="_blank">Bluestacks</a> for this purpose in the past - which without GPS hardware will not give away your accurate location (*but may give the location of an ISP node near you*).
