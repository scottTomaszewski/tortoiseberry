#!/usr/bin/env python

import FakeRelayChannel
import ScheduledRelayChannel
import Schedule

#temp
import datetime

pageTitle = "Spike!"
now = datetime.datetime.now()

actual = FakeRelayChannel.FakeRelayChannel()
actual.on()
actual.off()
schedule = Schedule.Schedule()
schedule.add('on', '*', '*', str(now.minute+1))
scheduled = ScheduledRelayChannel.ScheduledRelayChannel(actual, schedule)

scheduled.on()

print "Content-type: text/html"
print
print "<title>" + pageTitle + "</title>"
print "<h1>Spike!</h1>"
print "<p>Status: </p>"
print "<p>Relay: " + scheduled.status() + "</p>"
print ""
