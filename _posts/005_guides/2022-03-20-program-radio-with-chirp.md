---
layout: post
title: "How to program a radio with CHIRP"
author: "adakar"
categories: guides
tags: [programming, radio, communications, chirp]
image: assets/images/005_guides/2022-03-20-program-radio-with-chirp/uv5rprogramming.png
---
In this guide we will go through the steps to program the most common handheld radios, icom, baofeng and puxxing among the most widespread. We will do this using [CHIRP](https://chirp.danplanet.com/projects/chirp/wiki/Download), a open source community driven radio programming software.  

Make sure to verify that your radio is on the [supported radios list](https://chirp.danplanet.com/projects/chirp/wiki/Home#Supported-Radio-Models), if your model is not there it might be available as a custom driver if you google your radio name + chirp. 

Always download the config first - as you cannot safely assume equal model names means equal firmware.

This guide assumes you have a functional programming cable for you radio. 

* Download [CHIRP](https://chirp.danplanet.com/projects/chirp/wiki/Download).

* Connect the radio to your computer, open chirp and turn on the radio.

* Download the radio's current setup: Radio -> Download from Radio

<div class="image-thumbnail">
	<a href="https://user-images.githubusercontent.com/25975089/153761257-d1645312-a2b0-423e-8a82-fefe1a931631.png">
		<img src="https://user-images.githubusercontent.com/25975089/153761257-d1645312-a2b0-423e-8a82-fefe1a931631.png" width="640"/>
	</a>
</div>



* Save a copy of the setup: File -> Save as

* Edit the channels to match the [legal PMR446 channels](../PMR446-channels)

<div class="image-thumbnail">
	<a href="https://user-images.githubusercontent.com/25975089/153761194-5c481bb7-6d04-4c29-9cc0-908e5dee6ac4.png">
		<img src="https://user-images.githubusercontent.com/25975089/153761194-5c481bb7-6d04-4c29-9cc0-908e5dee6ac4.png" width="640"/>
	</a>
</div>



* Upload the configuration to your radio:

<div class="image-thumbnail">
	<a href="https://user-images.githubusercontent.com/25975089/153761246-be65d35f-359b-4e4a-b2b7-ab08580f8941.png">
		<img src="https://user-images.githubusercontent.com/25975089/153761246-be65d35f-359b-4e4a-b2b7-ab08580f8941.png" width="640"/>
	</a>
</div>



* Upon confirmation of success turn off your radio and disconnect.


