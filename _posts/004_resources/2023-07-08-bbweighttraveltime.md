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
        var ctx = document.getElementById('myChart').getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: [0, 1, 2, 3],
                datasets: [{
                    label: '0.20',
                    data: [1, 2, 3, 4],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            },
            options: {
                scales: {
                    y: {
                        title: {
                            display: true,
                            text: 'Time (seconds)'
                        }
                    },
                    x: {
                        title: {
                            display: true,
                            text: 'Distance (meters)'
                        }
                    }
                }
            }
        });
    </script>
</body>


