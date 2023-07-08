---
layout: post
title: "BB weight travel time chart"
author: "adakar"
categories: resources
tags: [bb, weight, travel, time]
image: assets/images/004_resources/bbcalc.png
---

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>


0.9 Joule 0.20 to 0.36g BBs
 <canvas id="myChart" width="400" height="400"></canvas>


 <script>
     // Sample data
     var distanceData = [0, 150]; // Meters
     var timeData = [[1, 2, 3, 4, 5], [2, 4, 6, 8]]; // Time per meter

     // Create the chart
     var ctx = document.getElementById('myChart').getContext('2d');
     var chart = new Chart(ctx, {
         type: 'line',
         data: {
             labels: distanceData.map((label, index) => `Label ${label}`),
             datasets: distanceData.map((_, index) => ({
                 label: `Time per Meter (${distanceData[index]} m)`,
                 data: timeData[index],
                 backgroundColor: 'rgba(0, 123, 255, 0.2)',
                 borderColor: 'rgba(0, 123, 255, 1)',
                 borderWidth: 2,
                 fill: 'start'
             }))
         },
         options: {
             scales: {
                 x: {
                     title: {
                         display: true,
                         text: 'Meters'
                     }
                 },
                 y: {
                     title: {
                         display: true,
                         text: 'Time per Meter (seconds)'
                     }
                 }
             }
         }
     });
 </script>



