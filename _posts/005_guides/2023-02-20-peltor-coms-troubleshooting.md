---
layout: post
title: "Peltor coms troubleshooting"
author: "adakar"
categories: guides
tags: [Peltor, j11, TP-120, TP120, NATO, pinout, troubleshooting]
image: assets/images/005_guides/2023-02-21-Peltor-coms-troubleshooting/heading.png
---

This guide will cover the basic steps to troubleshoot and solve your Peltor to radio issues. 

The guide is focused on the two most commonly seen issues, wiring mismatches or a need for microphone amplification. 



### Scenario 1: Everything works, but your microphone is perceived very low.
Depending on your radio one of three things can solve this:
- Enable dynamic microphone on your radio.
	- If your radio supports both types of microphones you might be able to enable dynamic microphone and everything is well.
- Replace your microphone with a replica microphone, negating the need for amplification.
	- Replica microphones generally do not require amplification and can be used on real headsets to bypass the issue.
- You need to buy/solder in amplification for your microphone.
    -  [1: Radio mod](http://www.px-airsoft.com/showroom/model/T0002/templateProductDetails.do?webId=1213907847691&editCurrentLanguage=1213907847692&module=SearchProduct&keyWords=amp&currentPage=1&ParentId=1324666353492015337&productId=1387478681544002075)
    -  [2: Downlead amplifier](http://www.px-airsoft.com/showroom/model/T0002/templateProductDetails.do?webId=1213907847691&editCurrentLanguage=1213907847692&module=SearchProduct&keyWords=amp&currentPage=1&ParentId=1324666353492015337&productId=1429033561572000266)
	-  [3: Adapter with amplification](http://www.px-airsoft.com/showroom/model/T0002/templateProductDetails.do?webId=1213907847691&editCurrentLanguage=1213907847692&module=SearchProduct&keyWords=Amplify+&currentPage=1&ParentId=1324666353492015337&productId=1429033811734000292)
	- 4: You make your own custom amplification circuit and solder it in where appropriate.


### Scenario 2: Microphone or sound in is does not work
This means you probably have a mix between Peltor and NATO wiring. Typically if either headset or PTT is the wrong pinout for you you get sound in but not out. 

Start by identifying the wiring of your headset and PTT:
- Method 1: Identifying pinout by model number.
	- Google the model number on the silver sticker on your headset and your PTT
	- Look for "NATO Wired" or "Peltor Wired"
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/headset.jpg">
		<img src="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/headset.jpg" width="640"/>
		<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
	</a>
</div>

- Method 2: Identifying pinout without the model number.
	- Headset with multimeter
		- Check for continuity on the speaker or mic +/- and and match according to [this overview](https://airsoftnorge.com/Peltor-J11-4pin/). 
	- Headset with an AA or AAA battery and some wires/paperclips
		- Connect the battery negative to base pin 4 of the TP120 and the positive to pin 2.
		- If you hear noise/static in the headphones while wearing them it's NATO wired.
		- Connect battery across 4 and 3 and hear noise/static it's civilian aka Peltor wired. 
	- PTT with a multimeter
		- Open the PTT and match the pins to your radio pinout, as there are too many options here we'll focus on the two most common, [U283 6pin](https://airsoftnorge.com/6pinout/) and the [Kenwood](https://airsoftnorge.com/kenwood-pinout/) plug used in most chinese radios.
		- This must be matched with the appropriate input from your headset plug, see [this overview](https://airsoftnorge.com/Peltor-J11-4pin/).

After confirming that you have a mismatch of headset and ptt wiring you can convert between Peltor and NATO wiring rather easily, or get an adapter.
- Option 1: Switching wiring in the PTT.
	 -You can swap wiring in the PTT by changing the output of your B and C pole. 
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/ptt.png">
		<img src="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/ptt.png" width="640"/>
		<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
	</a>
</div>
- Option 2: Buying an adapter cable.
	- [Example 1](https://shop.reconbrothers.com/product/3m-Peltor-NATO-adapter-custom/)
	- [Example 2](https://fivefourcommunications.com/product/Peltor-wired-to-NATO-wiring-adapter/)
	- [Example 3](https://sambandsradio.no/alfagear/an-1030/adapter-nexus-Peltor-NATO-20cm)

If you are stuck or found a solution you want, but do not have the skills/gear to do it yourself or friends that do there is only one commercial option we can wholly recommend, which is [JCI Coms](https://www.facebook.com/profile.php?id=100040638679937). 
You will have to ship your gear to the UK, pay for his time and shipping back. Rates are reasonable and turnaround is acceptable, but more importantly quality is excellent. 
