import heapq

class ParkingLot:
  available_slots=[]
  d1={}
  d2={}
  d3={}
  def addpark(total_slots):
    total_slots=total_slots
    print("Created parking of "+str(total_slots)+" slots")
    for i in range(1,total_slots+1):
      heapq.heappush(ParkingLot.available_slots,i)

class CarParkingSystem(ParkingLot):

  def addcar(car_registration,age_given):
    if len(ParkingLot.available_slots)==0:
      print("Parking Lot is full, go for other parking areas")
      return
    CarParkingSystem.car_registration_no=car_registration
    CarParkingSystem.age=age_given
    CarParkingSystem.slot()

  def slot(): 
    minimum_slotno=heapq.heappop(ParkingLot.available_slots)
    print('Car with vehicle registration number "'+CarParkingSystem.car_registration_no+'" has been parked at slot number '+str(minimum_slotno))
    if CarParkingSystem.age in ParkingLot.d1:
      ParkingLot.d1[CarParkingSystem.age].append((CarParkingSystem.car_registration_no,minimum_slotno))
    else:
      ParkingLot.d1[CarParkingSystem.age]=[(CarParkingSystem.car_registration_no,minimum_slotno)]
    ParkingLot.d2[CarParkingSystem.car_registration_no]=minimum_slotno
    ParkingLot.d3[minimum_slotno]=(CarParkingSystem.car_registration_no,CarParkingSystem.age)

  def leave(slot_leaved):
    if slot_leaved not in ParkingLot.d3:
      print("Slot already vacant")
      return
    print('Slot number '+str(slot_leaved)+' vacated, the car with vehicle registration number "'+ParkingLot.d3[slot_leaved][0]+'" left the space, the driver of the car was of age '+str(ParkingLot.d3[slot_leaved][1]))
    heapq.heappush(ParkingLot.available_slots,slot_leaved)
    x,y=ParkingLot.d3[slot_leaved]
    ParkingLot.d3.pop(slot_leaved)
    ParkingLot.d2.pop(x)
    for i in range(len(ParkingLot.d1[y])):
      if ParkingLot.d1[y][i][1]==slot_leaved:
        ParkingLot.d1[y].pop(i)
        return

  def vehicle_slot_age_no(given_age,x):
    if given_age not in ParkingLot.d1:
      print()
      return
    k=len(ParkingLot.d1[given_age])
    if k>0:
      for i in range(k):
        print(ParkingLot.d1[given_age][i][x],end="")
        if i!=k-1:
          print(",",end="")
      print()
    
  def vehicleslot(slot_carno):
    print(str(ParkingLot.d2[slot_carno]))

file1=open("input.txt","r")
for eachline in file1:
  l=eachline.split(" ")
  if l[0]=="Create_parking_lot":
    ParkingLot.addpark(int(l[1]))
  elif l[0]=="Park":
    CarParkingSystem.addcar(l[1],int(l[3]))
  elif l[0]=="Slot_numbers_for_driver_of_age":
    CarParkingSystem.vehicle_slot_age_no(int(l[1]),1)
  elif l[0]=="Leave":
    CarParkingSystem.leave(int(l[1]))
  elif l[0]=="Slot_number_for_car_with_number":
    x=l[1]
    x=x[:len(x)-1]
    CarParkingSystem.vehicleslot(x)
  elif l[0]=="Vehicle_registration_number_for_driver_of_age":
    CarParkingSystem.vehicle_slot_age_no(int(l[1]),0)
  else:
    print("Please check the command entered and correct it")
file1.close()
