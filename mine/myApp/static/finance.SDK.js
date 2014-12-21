//  $.getJSON()
//var url = "http://blistering-winterfell-72-128554.use1.nitrousbox.com/";
//var url = "https://localhost:8000/"
var url = "http://71.70.253.221:8000/"
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


$(document).ready(function(){
    //getFinanceRequest("sectors", "price_to_free_cash_flow", "2014", "08", "14");
    //getFinanceRequest("industry", "price_to_free_cash_flow", "2014", "08", "14");
    //getFinanceRequest("companies", "price_to_free_cash_flow", "2014", "08", "07", "2014", "08", "08");
    //getFinanceRequest("companies");
});
