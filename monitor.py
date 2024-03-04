"""
The Monitor module contains the Monitor class, the Activity class,
and a collection of constants. Together the elements of the module
help keep a record of activities that have occurred.

Activities fall into two categories: Rider activities and Driver
activities. Each activity also has a description, which is one of
request, cancel, pickup, or dropoff.

=== Constants ===
RIDER: A constant used for the Rider activity category.
DRIVER: A constant used for the Driver activity category.
REQUEST: A constant used for the request activity description.
CANCEL: A constant used for the cancel activity description.
PICKUP: A constant used for the pickup activity description.
DROPOFF: A constant used for the dropoff activity description.
"""

from typing import Dict, List
from location import Location, manhattan_distance

RIDER = "rider"
DRIVER = "driver"

REQUEST = "request"
CANCEL = "cancel"
PICKUP = "pickup"
DROPOFF = "dropoff"


class Activity:
    """An activity that occurs in the simulation.

    === Attributes ===
    timestamp: The time at which the activity occurred.
    description: A description of the activity.
    identifier: An identifier for the person doing the activity.
    location: The location at which the activity occurred.
    """

    time: int
    description: str
    id: str
    location: Location

    def __init__(self, timestamp: int, description: str, identifier: str,
                 location: Location) -> None:
        """Initialize an Activity.

        """
        self.time = timestamp
        self.description = description
        self.id = identifier
        self.location = location


class Monitor:
    """A monitor keeps a record of activities that it is notified about.
    When required, it generates a report of the activities it has recorded.
    """

    # === Private Attributes ===
    _activities: Dict[str, Dict[str, List[Activity]]]

    #       A dictionary whose key is a category, and value is another
    #       dictionary. The key of the second dictionary is an identifier
    #       and its value is a list of Activities.

    def __init__(self) -> None:
        """Initialize a Monitor.

        """
        self._activities = {
            RIDER: {},
            DRIVER: {}
        }
        """@type _activities: dict[str, dict[str, list[Activity]]]"""

    def __str__(self) -> str:
        """Return a string representation.

        """
        return "Monitor ({} drivers, {} riders)".format(
            len(self._activities[DRIVER]), len(self._activities[RIDER]))

    def notify(self, timestamp: int, category: str, description: str,
               identifier: str, location: Location) -> None:
        """Notify the monitor of the activity.

        timestamp: The time of the activity.
        category: The category (DRIVER or RIDER) for the activity.
        description: A description (REQUEST | CANCEL | PICKUP | DROP_OFF)
            of the activity.
        identifier: The identifier for the actor.
        location: The location of the activity.
        """
        if identifier not in self._activities[category]:
            self._activities[category][identifier] = []

        #    print('identifier category:', category)

        activity = Activity(timestamp, description, identifier, location)
        self._activities[category][identifier].append(activity)

        # print('-----> OVER HERE self._activities adds activity "',
        #      activity.description, '" for', activity.id, 'at time',
        #      activity.time)

    def report(self) -> Dict[str, float]:
        """Return a report of the activities that have occurred.

        """
        return {"rider_wait_time": self._average_wait_time(),
                "driver_total_distance": self._average_total_distance(),
                "driver_ride_distance": self._average_ride_distance()}

    def _average_wait_time(self) -> float:
        """Return the average wait time of riders that have either been picked
        up or have cancelled their ride.

        """
        wait_time = 0
        count = 0
        for activities in self._activities[RIDER].values():
            # A rider that has less than two activities hasn't finished
            # waiting (they haven't cancelled or been picked up).
            if len(activities) >= 2:
                # print('activities[0]:', activities[0].description, 'for',
                #      activities[0].id, 'at time', activities[0].time)
                # print('activities[1]:', activities[1].description, 'for',
                #      activities[0].id, 'at time', activities[1].time)
                # The first activity is REQUEST, and the second is PICKUP
                # or CANCEL. The wait time is the difference between the two.
                wait_time += activities[1].time - activities[0].time
                count += 1
        return wait_time / count

    def _average_total_distance(self) -> float:
        """Return the average distance drivers have driven.
        """
        total_distance = 0
        count = 0
        for activity in self._activities[DRIVER].values():
            count += 1
            # print('activity:', activity, 'of length', len(activity))

            if len(activity) >= 2:
                for i in range(len(activity) - 1):
                    total_distance += manhattan_distance(activity[i].location,
                                                         activity[
                                                             i + 1].location)
                    # print('--------------', )
                    # print('the activity number', i, 'is a',
                    #      activity[i].description,
                    #      'for', activity[i].id,
                    #      'at', activity[i].location, 'at time',
                    #      activity[i].time)
                    # print('distance added:',
                    #      manhattan_distance(activity[i].location,
                    #                         activity[i + 1].location))

        # print('distance', total_distance, 'divided by',
        #       len(self._activities[DRIVER]))
        # print('distance / len(self._activities[DRIVER])',
        #       total_distance / len(self._activities[DRIVER]))

        return total_distance / count

    def _average_ride_distance(self) -> float:
        """Return the average distance drivers have driven on rides.
        """
        total_ride_distance = 0
        count = 0
        # check all the activities in VALUES
        for k in self._activities[DRIVER].values():
            # increase the count FIRST:
            count += 1
            if len(k) >= 2:
                for i in range(len(k) - 1):
                    # make an extra condition making sure its not another
                    # pickup event (b/c it should be till dropoff)
                    if k[i + 1].description is not PICKUP:
                        if k[i + 1].description is DROPOFF:
                            total_ride_distance += manhattan_distance(
                                k[i].location,
                                k[
                                    i + 1].location)
        return total_ride_distance / count


if __name__ == "__main__":
    import python_ta

    python_ta.check_all(
        config={
            'max-args': 6,
            'extra-imports': ['typing', 'location']})
