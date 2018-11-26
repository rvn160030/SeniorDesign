/**
 * Create car crash transaction
 * @param {org.seniordesign.crashlog.CreateCrashLog} crashData
 * @transaction
 */

function createCrashLog(crashData) {
    return getAssetRegistry('org.seniordesign.crashlog.CrashLog')
       .then(async function(crashRegistry){
           //Add crash
           var factory = getFactory();
           var NS = 'org.seniordesign.crashlog';

           var crashID = 'BQT-140030';

           var vehicleRegistry = await getAssetRegistry('org.seniordesign.vehicle.Vehicle');
           var vehicle = await vehicleRegistry.get(crashData.VIN);
              console.log(vehicle.VIN);

           if(typeof vehicle.crashLog !== 'object' || vehicle.crashLog.constructor !== Array) {
               vehicle.crashLog = [];
           }

           var crashLog = factory.newResource(NS, 'CrashLog', 'Log ' + vehicle.VIN + crashData.time);

           crashLog.time = crashData.time;
           crashLog.speed =  crashData.speed;
           crashLog.passengers = crashData.passengers;
           crashLog.airbagDeployment = crashData.airbagDeployment;
           crashLog.VIN = crashData.VIN;
           vehicle.crashLog.push(crashLog);
           await vehicleRegistry.update(vehicle);  
           //vehicle.crashLog = crashLog;
           //vehicle.aliasVehicleNumber = [];


           //Emit the event Accident
           var event = factory.newEvent(NS, 'CrashLogCreated');
           event.crashID= crashID;
           emit(event);
           return crashRegistry.add(crashLog);
       })
}