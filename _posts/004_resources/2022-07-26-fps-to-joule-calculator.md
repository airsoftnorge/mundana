---
layout: post
title: "FPS to joule calculator"
author: "adakar"
categories: resources
tags: [bb, velocity, energy, joule]
image: assets/images/004_resources/math.jpg
---

Calculator that allows you to quickly convert from FPS to Joule.


<script type = "text/javascript">
function calc() {
   var weight = document.getElementById("weight").value;
   var fps = document.getElementById("fps").value;
   console.log("fps");
   console.log(fps);

   console.log("weight");
   console.log(weight);

   var weight=parseFloat(weight);
   var fps=parseFloat(weight);

   var ms = fps / 3.2808399;
   var weight_kg = weight / 1000;
   var joule = 0.5*(weight_kg)*(ms**2);
   console.log("joule");
   console.log(joule);

   document.getElementById("total").value = parseFloat(joule).toFixed(2);
}
</script> 

<div>
   <b> Variables </b> <br>
   <input type = "text"
      placeholder = "0.2"
      id = "weight"> Weight (Grams)<br>
   <input type = "text"
      placeholder = "290"
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


Want a quick lookup instead? Check out the [FPS to joule chart](https://airsoftnorge.com/fps-joule-chart/) with the most common BB weights. 