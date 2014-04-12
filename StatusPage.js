var refreshEnabled = true;
var monthNames = [ "January", "February", "March", "April", "May", "June",
      "July", "August", "September", "October", "November", "December" ];

function startTime() {
  var today=new Date();
  var h=today.getHours();
  var m=today.getMinutes();
  var s=today.getSeconds();
  var mth=monthNames[today.getMonth()]
  var day=today.getDay()
  if (s % 30 == 0 && refreshEnabled) { location.reload() }
  h = h > 12 ? h-12 : h;
  h = h == 0 ? 12 : h;
  // add a zero in front of numbers < 10
  m=checkTime(m);
  s=checkTime(s);
  document.getElementById('timeHourMinutes').innerHTML=h+":"+m;
  document.getElementById('timeSeconds').innerHTML=s;
  document.getElementById('dateContainer').innerHTML=mth+" "+day;
  t=setTimeout(function(){ startTime() },500);
}

function enableRefresh() {
  refreshEnabled = true;
}

function disableRefresh() {
  refreshEnabled = false;
}

function checkTime(i) {
  if (i<10) {
    i="0" + i;
  }
  return i;
}
