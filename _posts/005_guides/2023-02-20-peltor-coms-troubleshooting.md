---
layout: post
title: "Peltor coms troubleshooting"
author: "adakar"
categories: guides
tags: [peltor, j11, nato, pinout, troubleshooting]
image: assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/heading.png
---

This guide will cover the basic steps to troubleshoot and solve your peltor to radio issues. 

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


#### Scenario 2: Microphone or sound in is does not work
In this scenarie you probably have a mix and match between Peltor and Nato wiring. Typically if either headset or PTT is the wrong pinout for you you get sound in but not out. 


##### Identifying pinout by model number.
- Google the model number on the silver sticker on your headset and your PTT

<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/headset.jpg">
		<img src="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/headset.jpg" width="640"/>
		<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
	</a>
</div>
- Look for "NATO Wired" or "Peltor Wired"


##### Identifying pinout without the model number.
These options are verified using a multimeter to verify pinouts.

- Headset
	- Use the microphone socket and the J11 plug to verify pinout of the headset according to [this overview](https://airsoftnorge.com/Peltor-J11-4pin/). `To be verified`
	- Depending on the diameter of your voltmeter prongs you might want to use a little wire as inbetween to not mess up the socket.

- PTT
	- Open the PTT and match the pins to your radio pinout, as there are too many options here we'll focus on the two most common, [U283 6pin](https://airsoftnorge.com/6pinout/) and the [Kenwood](https://airsoftnorge.com/kenwood-pinout/) plug used in most chinese radios.
	- This must be matched with the appropriate input from your headset plug, see [this overview](https://airsoftnorge.com/Peltor-J11-4pin/).


##### Solutions:
- Option 1: Switching wiring in the PTT.
	 -You can swap wiring in the PTT by changing the output of your B and C pole. 
<div class="image-thumbnail">
	<a href="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/ptt.png">
		<img src="/assets/images/005_guides/2023-02-21-peltor-coms-troubleshooting/ptt.png" width="640"/>
		<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
	</a>
</div>

- Option 2: Buying an adapter cable.
	- [Example 1](https://shop.reconbrothers.com/product/3m-peltor-nato-adapter-custom/)
	- [Example 2](https://fivefourcommunications.com/product/peltor-wired-to-nato-wiring-adapter/)
	- [Example 3](https://sambandsradio.no/alfagear/an-1030/adapter-nexus-peltor-nato-20cm)

### Alternative solution: Throw money at it.

If you are stuck or found a solution you want, but do not have the skills/gear to do it yourself or friends that do there is only one commercial option we can wholly recommend, which is [JCI Coms](https://www.facebook.com/profile.php?id=100040638679937). 
You will have to ship your gear to the UK, pay for his time and shipping back. Rates are reasonable and turnaround is acceptable, but more importantly quality is excellent. 