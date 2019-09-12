class Classroom:

    classroomIDs = []
    startingTime = 800
    endTime = 2100

    def __init__(self, capacity, roomID):
        self.capacity = capacity
        self.roomID = roomID
        Classroom.classroomIDs.append(roomID)
        self.schedule = []

    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break
        return is_free

    def reserve(self, start, end):
        if self.isFree(start, end) and self.isValidSlot(start, end):
            time_slot = {"start": start, "end": end}
            self.schedule.append(time_slot)
            return True
        else:
            return False

    @classmethod
    def getAvailableRooms(cls):
        return str.join(",", cls.classroomIDs)

    @staticmethod
    def isValidSlot(start, end):
        if Classroom.startingTime <= start and Classroom.endTime >= end and start < end:
            return True
        return False

def main():
    classrooms = []
    classroom1 = Classroom(40, "114W PAB")
    classroom2 = Classroom(50, "214W PAB")
    classroom3 = Classroom(30, "314W PAB")
    classrooms.append(classroom1)
    classrooms.append(classroom2)
    classrooms.append(classroom3)
    print("Hallo, here you can reserve a classroom. Available IDs are:", Classroom.getAvailableRooms())

    while True:
        start = int(input("Please input the starting time: "))
        end = int(input("Please insert the ending time: "))
        if not Classroom.isValidSlot(start, end):
            print("Invalid time slot. Please enter different one")
        else:
            availableClassRooms = []
            for index in range(0, len(classrooms)):
                if classrooms[index].isFree(start, end):
                    availableClassRooms.append(index)
            if not availableClassRooms:
                print("All classrooms are reserved. Please select another time slot")
            else:
                for index in range(0, len(availableClassRooms)):
                    print("     ", index, ") ", classrooms[availableClassRooms[index]].roomID)
            selected_option = int(input("Select one of this classrooms:"))
            while selected_option < 0 or selected_option > (len(availableClassRooms) - 1):
                selected_option = int(input("Invalid option. Please select from the list: "))

            classrooms[availableClassRooms[selected_option]].reserve(start, end)
            print("You just reserved classroom ", classrooms[availableClassRooms[selected_option]].roomID, " from ", start, " to ", end)
            print(classrooms[availableClassRooms[selected_option]].schedule)

if __name__ == "__main__":
    main()
