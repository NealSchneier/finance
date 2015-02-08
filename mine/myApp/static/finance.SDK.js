//  $.getJSON()
//var url = "http://blistering-winterfell-72-128554.use1.nitrousbox.com/";
//var url = "https://localhost:8000/"
//var url = "http://71.70.253.221:8000/"
var url = "http://192.168.1.119:8000/"
//this makes the ajax call
//need to check if the date range is valid
// - if the range is valid
// - if the date is a weekend
function getFinanceRequest(table, field, year, month, day, toYear, toMonth, toDay){
    //var isWeekend = yourDateObject.getDay()%6==0;
    //new Date(year, month, day, hours, minutes, seconds, milliseconds);
    requestURL = url + table + "/";
    //request for 1 date
    if (field != undefined){
            requestURL += field + "/" + year + "/" + month + "/" + day + "/";
    }
    //request for a range from previous to this date
    //handle if the from date is a wekeend but the to date is not
    if (toYear != undefined){
            requestURL += "to/" + toYear + "/" + toMonth + "/" + toDay + "/";
    }
    //check if fields are undefined or null - chcck JS book
    alert(requestURL);
    $.getJSON(
        requestURL,
        {},
        function(data, status, xhr) {
            //converts JSON object to string for display
            data = JSON.stringify(data);
            $("#result").html(data);
            //alert("done");
        }
    );
}

var lineChartData = {
             labels: ["January", "February", "March", "April", "May", "June", "July"],
                datasets: [
                    {
                        label: "My First dataset",
                        fillColor: "rgba(220,220,220,0.2)",
                        strokeColor: "rgba(220,220,220,1)",
                        pointColor: "rgba(220,220,220,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(220,220,220,1)",
                        data: [20, 20, 20, 21, 26, 25, 20]
                    },
                    {
                        label: "My Second dataset",
                        fillColor: "rgba(151,187,205,0.2)",
                        strokeColor: "rgba(151,187,205,1)",
                        pointColor: "rgba(151,187,205,1)",
                        pointStrokeColor: "#fff",
                        pointHighlightFill: "#fff",
                        pointHighlightStroke: "rgba(151,187,205,1)",
                        data: [28, 28, 20, 29, 26, 27, 20]
                    }
                ]
        };

window.onload = function(){
        var ctx = document.getElementById("myChart").getContext("2d");
        window.myLine = new Chart(ctx).Line(lineChartData, {
            responsive: true
        });
};


//$(document).ready(function(){
    //getFinanceRequest("sectors", "price_to_free_cash_flow", "2014", "08", "14");
    //getFinanceRequest("industry", "price_to_free_cash_flow", "2014", "08", "14");
    //getFinanceRequest("companies", "price_to_free_cash_flow", "2014", "08", "07", "2014", "08", "08");
    //getFinanceRequest("companies");
   
//});


