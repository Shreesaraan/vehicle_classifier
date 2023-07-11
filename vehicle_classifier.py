class Vehicle:
    def Start(self):
        print("Vehicle Started")
    def Stop(self):
        print("Vehicle Stopped")
class Car(Vehicle):
     def Start(self):
         print("Car Started")
     def Stop(self):
         print("Car Stopped")
class MotorCycle(Vehicle):
    def Start(self):
        print("MotorCycle Started")
    def Stop(self):
        print("MotorCycle Stopped")

veh=Vehicle()
veh.Start()
veh.Stop()
print() #for space
i10=Car()
i10.Start()
i10.Stop()
print()#for space
ktm=MotorCycle()
ktm.Start()
ktm.Stop()