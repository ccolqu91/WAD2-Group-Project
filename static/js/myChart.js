
// this is a very basic example 
var ctx = document.getElementById("myChart").getContext('2d');

        var  charData= {
                labels: ['Food Quality', 'Customer Service', 'Hygiene', 'Value for Money', 'Menu Variety'],
                datasets: [{
                    label: 'average score',
                    backgroundColor: 'rgb(128, 0, 128)',
                    borderColor: 'rgb(128, 0, 128)',
                    data: [7, 5, 5, 2, 10]
                }]
            };

        var myChart = new Chart(ctx,{
            type:'bar',
            data:charData,
            oprions:{}


        });

var ctx = document.getElementById('myChart').getContext('2d');
var data = {
    labels: ['Food Quality', 'Customer Service', 'Hygiene', 'Value for Money', 'Menu Variety'],
    datasets: [{
        label: 'Average Scores',
        data: [
            { avg_food_quality_score },
            { avg_customer_service_score },
            { avg_hygiene_score },
            { avg_value_for_money_score },
            { avg_menu_variety_score }
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
