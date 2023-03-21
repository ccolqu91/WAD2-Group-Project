
// fake data just in case.
var ctx = document.getElementById('myChart').getContext('2d');
        var data = {
            labels: ['Food Quality', 'Customer Service', 'Hygiene', 'Value for Money', 'Menu Variety'],
            datasets: [{
            label: 'Average Scores',
            data: [
                2,10,5,9,8
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



// Another possible idea
// var ctx = document.getElementById("myChart").getContext('2d');
//         var  charData= {
//                 labels: ['Food Quality', 'Customer Service', 'Hygiene', 'Value for Money', 'Menu Variety'],
//                 datasets: [{
//                     label: 'Average Score',
//                     data: JSON.parse('{{ avg_scores_json }}'),
//                     backgroundColor: [
//                         'rgba(255, 99, 132, 0.2)',
//                         'rgba(54, 162, 235, 0.2)',
//                         'rgba(255, 206, 86, 0.2)',
//                         'rgba(75, 192, 192, 0.2)',
//                         'rgba(153, 102, 255, 0.2)'
//                       ],
//                       borderColor: [
//                         'rgba(255, 99, 132, 1)',
//                         'rgba(54, 162, 235, 1)',
//                         'rgba(255, 206, 86, 1)',
//                         'rgba(75, 192, 192, 1)',
//                         'rgba(153, 102, 255, 1)'
//                       ],
//                       borderWidth: 1


//                 }]
//             };

//         var myChart = new Chart(ctx,{
//             type:'bar',
//             data:charData,
//             oprions:{}
//         });
