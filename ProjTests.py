import pytest
from location import Location, deserialize_location, manhattan_distance
from monitor import Monitor
from dispatcher import Dispatcher
from simulation import Simulation
from event import create_event_list, RiderRequest, DriverRequest, Pickup, \
    Dropoff, Cancellation
from driver import Driver
from rider import Rider

"""
# ['blue', 'green', 'red', 'yellow']

#lst = ['blue', 'green', 'red', 'yellow']
lst = [2, 4, 6, 8]
# add orange into your list

def add(item):
    if item.__lt__(lst[0]):
        lst.insert(0, item)
        return

    for i in range(len(lst)):
        if lst[i].__gt__(item):
            print("we will add before number:", lst[i], "which is", i)
            lst.insert(i, item)
            return
    lst.append(item)

add(9)
print(lst)
add(1)
print(lst)

rider = Rider('Eve', 100, Location(2, 4), Location(5, 7))
driver = Driver('Abel', Location(2, 4), 3)

distance = manhattan_distance(rider.origin, rider.destination)
print('distance', distance, '/ speed ', driver.speed)
eta = distance / driver.speed
print('eta' , eta)

print("rider", rider)
print("driver", driver)
travel_time = driver.start_ride(rider)
print("travel time = ", travel_time, " type:", type(travel_time))
"""

events = create_event_list("events.txt")
# print(events)
# for event in events:
#     print(event)

dvr_request, psg_request = events[0], events[-1]
print("driver request", dvr_request)
print("rider request", psg_request)
driver, rider = dvr_request.driver, psg_request.rider
monitor = Monitor()
dispatcher = Dispatcher()
dvr_request.do(dispatcher, monitor)
print("HERE: I should have 1 driver:", dispatcher.curr_drivers)
psg_request.do(dispatcher, monitor)
trip = Pickup(0, rider, driver)
dropoff = trip.do(dispatcher, monitor)
print("dropoff type", type(dropoff[0]))

# my own tests
# test part two of fourth test
cancel = Cancellation(0, rider)
result = cancel.do(dispatcher, monitor)
print(result)

events = create_event_list("events.txt")
#for event in events:
#    print('EVENT', event)

# test fourth test case
# part one: creating events
# events = create_event_list("events.txt")
# print(len(events))

# part two: setting up the simulation
events = create_event_list("events.txt")
print('len(events):', len(events))
# ^^ this works now
sim = Simulation()
report = sim.run(events)
value = report['rider_wait_time']
print("Average wait time = ", value)
# print('type:', type(report))
# print('length of simulation: ', len(report))

value_distance = report['driver_total_distance']
print("Average distance ", value_distance)

# rider = Rider('Eve', 100, Location(3, 1), Location(3, 4))
# driver = Driver('Abel', Location(2, 4), 3)
# a = manhattan_distance(rider.origin, rider.destination)

# print('manhattan_distance:', a, 'rider.origin: ', rider.origin, 'rider.destination:', rider.destination)

k = report['driver_ride_distance']
print('average ride distance', k)



