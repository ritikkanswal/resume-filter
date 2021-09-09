google.charts.load('current', { 'packages': ['corechart'] });
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

  var result = JSON.parse("{{data|escapejs}}");
  var dict = result;
  var arr = [];
  arr.push(['Task', 'Hours per Day'])
  for (var key in dict) {
    if (dict.hasOwnProperty(key)) {
      arr.push([key, dict[key]]);
    }
  }
  // var result = JSON.parse(data);
  var Values = Object.values(result);
  console.log(arr);

  var data = google.visualization.arrayToDataTable([
    ['Task', 'Hours per Day'],
    ['Work', 11],
    ['Eat', 2],
    ['Commute', 2],
    ['Watch TV', 2],
    ['Sleep', 7]
  ]);
  var options = {
    'title': 'Skill Proportion',
    hAxis: {
      title: 'Month'
    },
    vAxis: {
      title: 'Temperature'
    },
    backgroundColor: 'powderblue'
  };
  var chart = new google.visualization.PieChart(document.getElementById('piechart'));
  chart.draw(data, options);
}