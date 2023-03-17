
// this is a very basic example 
var ctx = document.getElementById('myChart').getContext('2d');

        var  charData= {
                labels: ['7th','6th', '5th', '4th','3th', 'second', 'lastest'],
                datasets: [{
                    label: 'last five score',
                    backgroundColor: 'rgb(128, 0, 128)',
                    borderColor: 'rgb(128, 0, 128)',
                    data: [7, 5, 5, 2, 10, 10, 10]
                }]
            };

        var myChart = new Chart(ctx,{
            type:'bar',
            data:charData,
            oprions:{}


        });


// here is the skeleton i will use for our final version once I figure the relationship between views and js and html we can get a acceptable chart
// <script>
//         $(document).ready(function() {
//             var ctx = document.getElementById('myChart').getContext('2d');
//             var myChart = new Chart(ctx, {
//                 type: 'line',
//                 data: {
//                     labels: [],
//                     datasets: [{
//                         label: 'Score',
//                         data: [],
//                         borderColor: 'rgb(255, 99, 132)',
//                         backgroundColor: 'rgba(255, 99, 132, 0.5)',
//                         fill: true,
//                     }]
//                 },
//                 options: {
//                     scales: {
//                         yAxes: [{
//                             ticks: {
//                                 beginAtZero: true,
//                                 stepSize: 10,
//                             }
//                         }]
//                     }
//                 }
//             });

//             setInterval(function() {
//                 $.ajax({
//                     url: '/chart_data',
//                     type: 'get',
//                     success: function(data) {
//                         myChart.data.labels = data.labels;
//                         myChart.data.datasets[0].data = data.values;
//                         myChart.update();
//                     }
//                 });
//             }, 3000);
//         });
//     </script>
   