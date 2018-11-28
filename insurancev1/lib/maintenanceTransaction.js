/**
 * Create maintenacne log transaction
 * @param {org.seniordesign.maintenance.CreateMaintenanceLog} maintenanceData
 * @transaction
 */

function createMaintenanceLog(maintenanceData) {
    return getAssetRegistry('org.seniordesign.maintenance.MaintenanceLog')
       .then(async function(maintRegistry){
           //Add crash
           var factory = getFactory();
           var NS = 'org.seniordesign.maintenance';

           var vehicleRegistry = await getAssetRegistry('org.seniordesign.vehicle.Vehicle');
           var vehicle = await vehicleRegistry.get(maintenanceData.VIN);
              console.log(vehicle.VIN);

           if(typeof vehicle.maintenanceLog !== 'object' || vehicle.maintenanceLog.constructor !== Array) {
               vehicle.maintenanceLog = [];
           }

           var maintenanceLog = factory.newResource(NS, 'MaintenanceLog', 'Log ' + vehicle.VIN + maintenanceData.time);

           maintenanceLog.service = maintenanceData.service;
           maintenanceLog.time = maintenanceData.time;
           maintenanceLog.mechID = maintenanceData.mechID;
           maintenanceLog.VIN = maintenanceData.VIN;
           vehicle.maintenanceLog.push(maintenanceLog);
           await vehicleRegistry.update(vehicle);  
          
           //Emit the event Accident
           var event = factory.newEvent(NS, 'MaintenanceLogCreated');
           event.serviceID = maintenanceLog.serviceID;
           emit(event);
           return maintRegistry.add(maintenanceLog);
       })
}