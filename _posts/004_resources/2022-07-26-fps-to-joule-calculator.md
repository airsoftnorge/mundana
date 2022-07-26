---
layout: post
title: "FPS to joule calculator"
author: "adakar"
categories: resources
tags: [bb, velocity, energy, joule]
image: assets/images/004_resources/math.jpg
---

Calculator that allows you to quickly convert from FPS to Joule

<script type = "text/javascript">
function calc() {
<!-- Values from input -->
	var weight = document.getElementById("weight");
	var weightValue = parseFloat(weight.value);
<!-- Values from input -->
	var fps = document.getElementById("fps");
	var fpsValue = parseFloat(fps.value);
<!-- Quick maths -->	
	var weight_kg = weight.value / 1000
<!-- Constants -->	
    var joule = 0.5*weight_kg*(fpsValue / 3.2808399) * * 2
    

	
	document.getElementById("total").value = parseFloat(joule).toFixed(2);
}
</script> 
<div>
   <b> Variables </b> <br>
   <input type = "text"
      placeholder = "0.2"
      id = "weight"> Weight (Grams)<br>
   <input type = "text"
      placeholder = "0.9"
      id = "fps"> FPS <br>
   <button type = "button"
      onclick = "javascript:calc();"> Calculate </button> <br>
   <b> Joule: </b> <br>
   <input type = "text"
      placeholder = "Energy in joule"
      id = "total"
      disabled />
   <br>
</div>
