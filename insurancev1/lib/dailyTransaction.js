/**
 * Create car dailyLog transaction
 * @param {org.seniordesign.dailylog.CreateDailyLog} dailyData
 * @transaction
 */
function createDailyLog(dailyData) {
    return getAssetRegistry('org.seniordesign.dailylog.DrivingLog')
       .then(async function(dailyRegistry){
           //Add daily
           var factory = getFactory();
           var NS = 'org.seniordesign.dailylog';

           var dailyID = 'BHANDSOME';

           var vehicleRegistry = await getAssetRegistry('org.seniordesign.vehicle.Vehicle');
           var vehicle = await vehicleRegistry.get(dailyData.VIN);
              console.log(vehicle.VIN);

           if(typeof vehicle.dailyLog !== 'object' || vehicle.dailyLog.constructor !== Array) {
              vehicle.dailyLog = [];
           }

           var dailyLog = factory.newResource(NS, 'DrivingLog', 'Log ' + dailyData.timeSubmitted);

           dailyLog.timeSubmitted = dailyData.timeSubmitted;
           dailyLog.avgSpeed =  dailyData.avgSpeed;
           dailyLog.totalDriveTimeMins = dailyData.totalDriveTimeMins;
           dailyLog.avgBrakingForce= dailyData.avgBrakingForce;
           dailyLog.avgAccelerationForce = dailyData.avgAccelerationForce;
           dailyLog.VIN = dailyData.VIN;
           vehicle.dailyLog.push(dailyLog);
           await vehicleRegistry.update(vehicle);  
        


           //Emit the event Accident
           var event = factory.newEvent(NS, 'DailyLogCreated');
           event.dailyID= dailyID;
           emit(event);
           return dailyRegistry.add(dailyLog);
       })
}