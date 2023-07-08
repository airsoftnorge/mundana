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


  <canvas id="myChart"></canvas>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      var ctx = document.getElementById('myChart').getContext('2d');
      var myChart = new Chart(ctx, {
        type: 'line',
        data: {
          datasets: [
            {
              label: 'Sibo',
              data: [
                { x: 1, y: 0.0046556795426143435 },
                { x: 2, y: 0.009493862696343827 },
                { x: 3, y: 0.014514111615520329 },
                { x: 4, y: 0.019715698889061075 },
                // ... rest of the data points
              ],
              borderColor: 'rgba(255, 99, 132, 1)',
              fill: false
            },
            {
              label: 'Ute',
              data: [
                { x: 1, y: 0.004979888728743788 },
                { x: 2, y: 0.010130001716832825 },
                { x: 3, y: 0.015450030055191608 },
                { x: 4, y: 0.02093946014004677 },
                // ... rest of the data points
              ],
              borderColor: 'rgba(54, 162, 235, 1)',
              fill: false
            }
          ]
        },
        options: {
          scales: {
            x: {
              type: 'linear',
              position: 'bottom'
            },
            y: {
              beginAtZero: true
            }
          }
        }
      });
    });
  </script>




