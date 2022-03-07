---
layout: post
title: "BB residual energy calculator"
author: "ASN | Staff"
categories: resources
tags: [bb, velocity, energy, joule, residual]
image: /assets/images/math.png
---

Small calculator to determin the residual energy of a BB at a certain distance. It's meant to help you pick the right bullet weight for your area and verify observations made ingame. 
As a general rule, a heavier BB will be more accurate and reach longer, but it will be slower in the relatively close distances, meaning you must balance what you want vs the area you play, the skill of the oponents and your playstyle.

### NOT COMPLETED YET


<script type = "text/javascript">
function calc(energyValue, weightValue, distanceValue) {
  var airdensity_kgm3, crossection_m2, diameter_mm, drag_ish, dragcoefficient, energy_at_distance, radius_m, speed_at_distance, speed_ms, weight_kg;
  weight_kg = weightValue / 1000;
  dragcoefficient = 0.47;
  airdensity_kgm3 = 1.225;
  diameter_mm = 6;
  radius_m = diameter_mm / 1000 / 2;
  crossection_m2 = math.pi * Math.pow(radius_m, 2);
  speed_ms = math.sqrt(energyValue / (0.5 * weight_kg));
  drag_ish = airdensity_kgm3 * crossection_m2 * dragcoefficient;
  energy_at_distance = 0.5 * weight_kg * Math.pow(speed_at_distance, 2);
  return [energy_at_distance];
  document.getElementById("energy_at_distance").value = total.toString();
}
</script> 
<div>
   <b> Variables </b> <br>
   <input type = "text"
      placeholder = "0.2"
      id = "weight"> Weight in grams <br>
   <input type = "text"
      placeholder = "0.9"
      id = "energy"> Muzzle energy <br>
   <input type = "text"
      placeholder = "30"
      id = "distance"> Distance in meters <br>
   <button type = "button"
      onclick = "javascript:calc();"> Calculate </button> <br>
   <b> Residual energy in joule at selected distance: </b> <br>
   <input type = "text"
      placeholder = "Residual energy"
      id = "total"
      disabled />
   <br>
</div>
