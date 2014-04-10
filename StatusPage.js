function startTime() {
  var today=new Date();
  var h=today.getHours();
  var m=today.getMinutes();
  var s=today.getSeconds();
  if (s % 30 == 0) { location.reload() }
  h = h > 12 ? h-12 : h;
  h = h == 0 ? 12 : h;
  // add a zero in front of numbers < 10
  m=checkTime(m);
  s=checkTime(s);
  document.getElementById('timeHourMinutes').innerHTML=h+":"+m;
  document.getElementById('timeSeconds').innerHTML=s;
  t=setTimeout(function(){ startTime() },500);
}
 
function foo() { alert("bar"); }

function checkTime(i) {
  if (i<10) {
    i="0" + i;
  }
  return i;
}
