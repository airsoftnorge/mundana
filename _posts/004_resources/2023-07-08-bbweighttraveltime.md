---
layout: post
title: "BB weight travel time chart"
author: "adakar"
categories: resources
tags: [bb, weight, travel, time]
image: assets/images/004_resources/bbcalc.png
---

<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<body>
  <canvas id="myChart"></canvas>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          labels: ['0.2', '0.25'],
          datasets: [{
            label: 'Value 0.2',
            data: [0, 1, 2, 3, 4, 5],
            borderColor: 'rgba(255, 99, 132, 1)',
            fill: false
          },
          {
            label: 'Value 0.25',
            data: [2, 4, 6, 8],
            borderColor: 'rgba(54, 162, 235, 1)',
            fill: false
          }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        }
      });
    });
  </script>
</body>


