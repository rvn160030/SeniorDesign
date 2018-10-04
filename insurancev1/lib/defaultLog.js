/*  Default log that starts with cx entering car
  */
function createDailyLog() {
     return getAssetRegistry('org.seniordesign.vehicle.Vehicle')
        .then(function(crashRegistry){
       		var def=0;
       		var currentTime = new Date();
        	var hrs = currentTime.getHours(),
                min = currentTime.getMinutes(),
          		sec = currentTime.getSeconds();
        if (min < 10)
            	min = "0" + min;
        if (sec < 10)
            	sec = "0" + sec;
        var formatHrs = hrs + ":" + min + ":" + sec + ((hrs > 11)?"PM":formatHrs+="AM");
       		var tme=formatHrs
            var factory = getFactory();
            var NS = 'org.seniordesign.vehicle';
            var logID = '000123';
            var vehicle = factory.newResource(NS,'Vehicle', logID);
            var defLog = factory.newConcept(NS, "Log#",def+1);
            defLog.time = tme;
            defLog.driveTime = seconds;
            defLog.brkForce = vehicle.avgBrakingForce;
       		defLog.avgBrkForce=vehicle.avgAccelerationForce;
            vehicle.defLog = dailyLog;
            var event = factory.newEvent(NS, 'Log created');
            event.logID= logID;
            emit(event);
            return defaultLog.addAll([vehicle]);
        })
 }