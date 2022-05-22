class ParkingLot:
    def __init__(self) -> None:
        # Initializing database
        self.data = {}

    def _convert_tuple_to_csv(tuple_to_be_converted) -> str:
        return_string = ""
        for i in tuple_to_be_converted:
            return_string += "," + str(i)
        return return_string[1:]

    def create_parking_space(self,size:int) -> str:
        '''
        Creates parking space of given size.
        size: Total slots in parking lot.
        '''
        for i in range(1,size + 1):
            self.data[i] = {
                "reg_no": None,
                "driver_age": None,
            }
        return f"Created parking of {size} slots"

    def park(self,reg_no:str,driver_age:int) -> str:
        '''
        Parks the car in an vacant spot.
        reg_no: Registration number of the vehicle
        driver_age: Age of the driver
        '''
        vacant = None
        for key in self.data.keys():
            if self.data[key]["reg_no"] is None:
                vacant = key
                break

        if vacant is None:
            return "Error: No empty spot. Parking lot full."
        else:
            self.data[vacant]["reg_no"] = reg_no
            self.data[vacant]["driver_age"] = driver_age
            return f'Car with vehicle registration number "{reg_no}" has been parked at slot number {vacant}'

    def leave(self,slot:int) -> str:
        '''
        Marks the slot empty in Parking lot.
        slot: Slot number to be vacated.
        '''
        if self.data[slot]["reg_no"] is None:
            return "Error: Slot already vacant."
        else:
            return_sting = f'Slot number {slot} vacated, the car with vehicle registration number "{self.data[slot]["reg_no"]}" left the space, the driver of the car was of age {self.data[slot]["driver_age"]}'
            self.data[slot]["reg_no"] = None
            self.data[slot]["driver_age"] = None
            return return_sting

    def slot_numbers_for_drivers(self,age:int) -> str:
        '''
        Returns all slot numbers occupied by by the driver of given age.
        age: Age of the drivers
        '''
        slot_numbers = []
        for key in self.data.keys():
            if self.data[key]["driver_age"] == age:
                slot_numbers.append(key)

        if len(slot_numbers) > 0:
            return ParkingLot._convert_tuple_to_csv(slot_numbers)
        else:
            return f"No slots occupied by drivers with age {age}"

    def slot_number_for_car_with_number(self,reg_no:str) -> int:
        '''
        Returns the slot number for car with given regestration number and -1 if not present.
        reg_no: Registration number of the car.
        '''
        slot_number = -1
        for key in self.data.keys():
            if self.data[key]["reg_no"] == reg_no:
                slot_number = key
                break

        return slot_number

    def reg_numbers_for_drivers(self,age:int) -> tuple:
        '''
        Returns the registration numbers of drivers of given age.
        age: Age of the drivers.
        '''
        reg_numbers = []
        for key in self.data.keys():
            if self.data[key]["driver_age"] == age:
                reg_numbers.append(self.data[key]["reg_no"])

        if len(reg_numbers) > 0:
            return ParkingLot._convert_tuple_to_csv(reg_numbers)
        else:
            return f"No drivers of age {age}"

if __name__ == "__main__":
    with open('input.txt','r') as rf:
        lines = rf.readlines()

    # Initializing parking lot object
    park_lot = ParkingLot()
    
    for line in lines:
        try:
            command = line.strip().split(' ')
            if command[0].lower() == 'create_parking_lot':
                print(park_lot.create_parking_space(int(command[1])))
            elif command[0].lower() == 'park':
                print(park_lot.park(command[1],int(command[3])))
            elif command[0].lower() == 'leave':
                print(park_lot.leave(int(command[1])))
            elif command[0].lower() == 'slot_numbers_for_driver_of_age':
                print(park_lot.slot_numbers_for_drivers(int(command[1])))
            elif command[0].lower() == 'slot_number_for_car_with_number':
                print(park_lot.slot_number_for_car_with_number(command[1]))
            elif command[0].lower() == 'vehicle_registration_number_for_driver_of_age':
                print(park_lot.reg_numbers_for_drivers(int(command[1])))
            else:
                print(f'Error in command "{line.strip()}"')
        except IndexError:
            print(f'Error in command "{line.strip()}"')
        
