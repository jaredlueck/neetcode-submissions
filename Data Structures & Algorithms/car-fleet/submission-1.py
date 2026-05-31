class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(speed))]
        cars.sort(key=lambda car: car[0], reverse=True)
        front_car = cars[0]
        time_front = (target - front_car[0]) / front_car[1]
        
        fleets = len(speed)
        print(cars)
        for i, val in enumerate(cars[1:]):
            # will this car catch up to the one in front
            # how long it would take to get to end at current pace
            time_current = (target - val[0]) / val[1]
            print(time_current)
            # this car will catch up to the one in front
            if time_current <= time_front:
                print(str(val) + " catches up")
                fleets -= 1
            else:
                time_front = time_current
        return fleets
