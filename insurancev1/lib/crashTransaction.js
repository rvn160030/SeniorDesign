/**
 * Create car crash transaction
 * @param {org.seniordesign.vehicle.CreateCrashLog} crashData
 * @transaction
 */

 function createCrashLog(crashData) {
     return getAssetRegistry('org.seniordesign.vehicle.Vehicle')
        .then(function(crashRegistry){
            //Add crash
            var factory = getFactory();
            var NS = 'org.seniordesign.vehicle';

            var crashID = 'BQT-140030';
            var vehicle = factory.newResource(NS,'Vehicle', crashID);

            vehicle.VIN = crashData.VIN;

            var crashLog = factory.newConcept(NS, "CrashLog");

            crashLog.time = crashData.time;
            crashLog.speed =  crashData.speed;
            crashLog.passengers = crashData.passengers;
       		crashLog.airbagDeployment = crashData.airbagDeployment;
            vehicle.crashLog = crashLog;
            //vehicle.aliasVehicleNumber = [];

            //Emit the event Accident
            var event = factory.newEvent(NS, 'CrashLogCreated');
            event.crashID= crashID;
            emit(event);

            return crashRegistry.addAll([vehicle]);
        })
 }