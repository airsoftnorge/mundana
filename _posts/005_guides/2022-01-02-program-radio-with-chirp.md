---
layout: post
title: "Guide: How to program a radio with CHIRP"
author: "adakar"
categories: guides
tags: [guide, programming, program, baofeng, puxxing, icom, Abbree, Pofung, puxing, Baojie, chipr, uv5r, uv-5r, uv82, uv-82, BTech, ]
image: uv5rprogramming.png
---

The guide assumes you have a functional programming cable for you radio. 
Verify that your radio is on the [supported radios list](https://chirp.danplanet.com/projects/chirp/wiki/Home#Supported-Radio-Models).

Always download the config first - as you cannot safely assume equal model names means equal firmware.

Download [CHIRP](https://chirp.danplanet.com/projects/chirp/wiki/Download).

Connect the radio to your computer, open chirp and turn on the radio.

Download the radios current setup: Radio -> Download from Radio

![image](https://user-images.githubusercontent.com/25975089/153761257-d1645312-a2b0-423e-8a82-fefe1a931631.png)


Save a copy of the setup: File -> Save as

Edit the channels to match the [PMR446 Legal channels](446-channels)

![image](https://user-images.githubusercontent.com/25975089/153761194-5c481bb7-6d04-4c29-9cc0-908e5dee6ac4.png)

Upload the configuration to your radio:

![image](https://user-images.githubusercontent.com/25975089/153761246-be65d35f-359b-4e4a-b2b7-ab08580f8941.png)

Upon confirmation of success turn of your radio and disconnect.
