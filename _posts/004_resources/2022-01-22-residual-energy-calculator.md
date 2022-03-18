---
layout: post
title: "Residual energy at distance calculator"
author: "adakar"
categories: resources
tags: [bb, velocity, energy, joule, residual]
image: assets/images/math.png
---

A small calculator to determine the residual energy of a BB at a certain distance. It's meant to help you pick the right bullet weight for your area and verify observations made ingame. 
As a general rule, a heavier BB will be more accurate and reach longer, but it will be slower in the relatively close distances, meaning you must balance what you want vs. the area you play, the skill of the opponents and your playstyle.

Compromises in the calculator:
* Zero meters above sea level assumption
* Air density setup for maximized range, high moisture content will lower range.
* Rounding down
* This is accurate energy levels at range, it does not care if your BB would have hit the ground by now. 

<script type = "text/javascript">
function calc() {
<!-- Values from input -->
	var weight = document.getElementById("weight");
	var weightValue = parseFloat(weight.value);
<!-- Values from input -->
	var energy = document.getElementById("energy");
	var energyValue = parseFloat(energy.value);
<!-- Values from input -->
	var distance = document.getElementById("distance");
	var distanceValue = parseFloat(distance.value);
<!-- Quick maths -->	
	var weight_kg = weight.value / 1000
<!-- Constants -->	
    var dragcoefficient = 0.47
    var airdensity_kgm3 = 1.225
	var radius_m = 0.003
    var crossection_m2 = 0.0000282743
    var speed_ms = Math.sqrt(energy.value / (0.5 * weight_kg))
    var drag_ish = airdensity_kgm3 * crossection_m2 * dragcoefficient
    var speed_at_distance = speed_ms * Math.exp(-(drag_ish / (weight_kg * 2) * distanceValue))
    var energy_at_distance = 0.5 * weight_kg * speed_at_distance ** 2
	
	document.getElementById("total").value = energy_at_distance.toString();
}
</script> 
<div>
   <b> Variables </b> <br>
   <input type = "text"
      placeholder = "0.2"
      id = "weight"> Weight (Grams)<br>
   <input type = "text"
      placeholder = "0.9"
      id = "energy"> Muzzle energy (Joule)<br>
   <input type = "text"
      placeholder = "30"
      id = "distance"> Distance (Meters)<br>
   <button type = "button"
      onclick = "javascript:calc();"> Calculate </button> <br>
   <b> Residual energy in joule at selected distance: </b> <br>
   <input type = "text"
      placeholder = "Residual energy"
      id = "total"
      disabled />
   <br>
</div>

<!-- weight energy distance-->