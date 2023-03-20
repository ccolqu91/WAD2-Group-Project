var ctx = document.getElementById('myChart');
        var data = {
            labels: ['Food Quality', 'Customer Service', 'Hygiene', 'Value for Money', 'Menu Variety'],
            datasets: [{
            label: 'Average Scores',
            data: [
                 canvas.dataset.foodQualityScore,
                 canvas.dataset.customerServiceScore,
                 canvas.dataset.hygieneScore,
                 canvas.dataset.valueForMoneyScore,
                 canvas.dataset.menuVarietyScore
              ],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)'
                ],
                borderWidth: 1
                }]
        };
        var options = {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        };

        var myChart = new Chart(ctx, {
            type: 'bar',
            data: data,
            options: options
        });