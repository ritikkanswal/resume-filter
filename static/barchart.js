function drawChart() {
    /* Define the chart to be drawn.*/
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
        ['Page Vist', 'Students Tutorial'],
        ['2012', 10000],
        ['2013', 23000],
        ['2014', 46000],
        ['2015', 49000],
        ['2016', 55000],
        ['2017', 100000]
    ]);
    var options = {
        title: 'Page visit per year',
        isStacked: true,
        backgroundColor: 'white'
    };
    /* Instantiate and draw the chart.*/
    var chart = new google.visualization.BarChart(document.getElementById('container'));
    chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);