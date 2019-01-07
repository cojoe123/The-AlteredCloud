var data = "{{ chart }}"
var symbol = "{{ book.quote.symbol }}/"
var endpoint = '/stocks/api/chart/data/' + symbol
$.ajax({
  method:"GET",
  url: endpoint,
  success: function(data) {
    console.log(data);
  },
  error: function(err) {
    console.log('Error');
    console.log(endpoint);
    console.log(err);
  }
})

var ctx = document.getElementById("myChart").getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ["January", "February", "March", "April", "May", "June", "July"],
        datasets: [{
            label: "Past 20 days",
            backgroundColor: '#666', //'rgb(255, 99, 132)',
            borderColor: '#666', //'rgb(255, 99, 132)',
            data: [0, 10, 5, 2, 20, 30, 45],
            fill: false,
        }]
    },

    // Configuration options go here
    options: {
      scales: {
        xAxes: [{
          gridLines: {
          display:false
          }
        }],
        yAxes: [{
          gridLines: {
          display:false
          }
        }]
      },
    }
});
