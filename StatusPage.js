var monthNames = [ "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December" ];
var refreshed = new Date();

function startTime() {
  dateTime();
}

function dateTime() {
  var today=new Date();
  var h=today.getHours();
  var m=today.getMinutes();
  var s=today.getSeconds();
  var mth=monthNames[today.getMonth()]
  var day=today.getDay()
  h = h > 12 ? h-12 : h;
  h = h == 0 ? 12 : h;
  // add a zero in front of numbers < 10
  m=checkTime(m);
  s=checkTime(s);
  document.getElementById('timeHourMinutes').innerHTML=h+":"+m;
  document.getElementById('timeSeconds').innerHTML=s;
  document.getElementById('dateContainer').innerHTML=mth+" "+day;
  if (s % 5 == 0) { refreshData() }
  $("#lastUpdated").html(Math.ceil((today - refreshed)/1000));
  t=setTimeout(function(){ dateTime() },500);
}

function checkTime(i) {
  if (i<10) {
    i="0" + i;
  }
  return i;
}

function refreshData() {
  $.getJSON( "/update", function( data ) {
    refreshed = new Date();
    var items = [];
    $.each( data, function( key, val ) {
      if (key == 'topLeftTempValue') {
        $("#topLeftTemp").html(temperatureRangeHtml(val))
      } else if (key == 'topLeftHumidityValue') {
        $("#topLeftHumidity").html(humidityRangeHtml(val))

      } else if (key == 'topRightTempValue') {
        $("#topRightTemp").html(temperatureRangeHtml(val))
      } else if (key == 'topRightHumidityValue') {
        $("#topRightHumidity").html(humidityRangeHtml(val))

      } else if (key == 'bottomLeftTempValue') {
        $("#bottomLeftTemp").html(temperatureRangeHtml(val))
      } else if (key == 'bottomLeftHumidityValue') {
        $("#bottomLeftHumidity").html(humidityRangeHtml(val))
      
      } else if (key == 'bottomRightTempValue') {
        $("#bottomRightTemp").html(temperatureRangeHtml(val))
      } else if (key == 'bottomRightHumidityValue') {
        $("#bottomRightHumidity").html(humidityRangeHtml(val))

      } else if (key == 'uvbStatus') {
        $("#uvbLightStatus").html(val)
      } else if (key == 'baskingStatus') {
        $("#baskingLightStatus").html(val)
      
      } else if (key == 'outsideMinTemp') {
        $("#minTemp").html(val)
      } else if (key == 'outsideTemp') {
        $("#currTemp").html(val)
      } else if (key == 'outsideMaxTemp') {
        $("#maxTemp").html(val)
      } else if (key == 'weatherIcon') {
        $("#weatherIcon").attr('src', val);
      } 
    });
  });
}

function temperatureRangeHtml(value) {
  return rangeHtml(value, "F", 50, 100, 'blueRedFullRange')
}

function humidityRangeHtml(value) {
  return rangeHtml(value, "%", 30, 90, 'redBlueFullRange')
}

function rangeHtml(value, units, min, max, cssBackground) {
  var html = "<div class='rangeTitle'>";
  html += "<span class='rangeValue'>" + value + "</span>";
  html += "<span class='rangeTitleUnits'>" + units + "</span>";
  html += "</div>";
  html += "<div class='rangeBar " + cssBackground + "'>";
  var perc = (value-min) / (max-min);
  var mark = perc > 0 ? Math.floor(perc * 45) : 1;
  for (var i in range(1, 45)) {
    if (i == mark-1 || i == mark+1) {
      html += "<div class='rangeTick rangeTickMed'></div>";
    } else if (i == mark) {
      html += "<div class='rangeTick rangeTickLarge'>";
      html += "</div>";
    } else {
      html += "<div class='rangeTick'></div>";
    }
  }
  html += "</div>";
  return html;
}

function range(start, end){
    var array = new Array();
    for(var i = start; i < end; i++){
        array.push(i);
    }
    return array;
}
