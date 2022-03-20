---
layout: post
title: "cheatsheet"
author: "staff"
categories: test
tags: [cheatsheet]
image: assets/images/test.jpg
---

<!-- Styling -->
#### In post content headline

* This produce a dotted list
* One dot pr item and soforth



<!-- Features -->
	<!-- Expandable text area -->
	<details>
	<summary><b><u>TEXT FOR EXPANSION</u></b></summary>
		<div>
			CONTENT GOES HERE
		</div>
	</details>


<!-- Pathing -->
	These two produce the same result:

	[Link]({{site.baseurl}}/TEST)
	[Link](../TEST)



<!-- Media links -->

	<!-- Youtube video with thumbnail-->
	<div class="video-thumbnail">
	  <a href="https://youtu.be/zT0gNbwesM4">
		<img src="https://i.ytimg.com/vi/aowfiOAUJhY/sddefault.jpg" width="640"/>
		<div class="video-thumbnail-centered"><i class="fa-solid fa-play"></i></div>
	  </a>
	</div>



	<!-- Image with zoom -->

	<div class="image-thumbnail">
		<a href="{{site.baseurl}}assets/images/PeltorWiring.png">
			<img src="{{site.baseurl}}assets/images/PeltorWiring.png" width="640"/>
			<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
		</a>
	</div>


	<!-- Image with zoom -->

	<div class="image-thumbnail">
		<a href="AAAAAAAAAAAAAAAAAA">
			<img src="AAAAAAAAAAAAA" width="640"/>
			<div class="image-thumbnail-centered"><i class="fa-solid fa-magnifying-glass"></i></div>
		</a>
	</div>



	<!-- Image with zoom no magnifying-glass -->

	<div class="image-thumbnail">
		<a href="AAAAAAAAAAAAAAAAAA">
			<img src="AAAAAAAAAAAAA" width="640"/>
		</a>
	</div>





	<!-- Youtube link without thumbnail -->

	[video link](https://youtu.be/aowfiOAUJhY)



