"""Drivers for the simulation"""

from location import Location, manhattan_distance
from rider import Rider, CANCELLED


class Driver:
    """A driver for a ride-sharing service.

    === Attributes ===
    id: A unique identifier for the driver.
    location: The current location of the driver.
    is_idle: True if the driver is idle and False otherwise.
    speed: The speed of the driver.
    """

    id: str
    location: Location
    is_idle: bool
    speed: int
    driver_destination: Location

    def __init__(self, identifier: str, location: Location, speed: int) -> None:
        """Initialize a Driver.

        """
        self.id = identifier
        self.location = location
        self.speed = speed
        self.is_idle = True  # true by default
        self.driver_destination = None  # add this attribute

    def __str__(self) -> str:
        """Return a string representation.

        """
        return str(self.id)

    def __eq__(self, other: object) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self is other

    def get_travel_time(self, destination: Location) -> int:
        """Return the time it will take to arrive at the destination,
        rounded to the nearest integer.

        """
        # time it takes to travel = manhattan_distance to travel/speed of driver
        # print('TYPE LOCATION', type(self.location))
        # print('DESTINATION', type(destination))
        time_it_takes = (manhattan_distance(self.location,
                                            destination)) / self.speed
        return round(time_it_takes)

    def start_drive(self, location: Location) -> int:
        """Start driving to the location.
        Return the time that the drive will take.

        """
        # start_drive is FOR DRIVER
        self.is_idle = False  # no longer idle
        self.driver_destination = location
        return self.get_travel_time(location)  # location = destination

    def end_drive(self) -> None:
        """End the drive and arrive at the destination.

        Precondition: self.destination is not None.

        """
        self.location = self.driver_destination
        # print('self.location', self.location, 'for', self.id, 'at destination'
        # , self.driver_destination)
        # print('self.location', self.location, 'self.destiantion',
        # self.driver_destination)
        self.driver_destination = None
        self.is_idle = True  # driver is idle

    def start_ride(self, rider: Rider) -> int:
        """Start a ride and return the time the ride will take.

        """
        # print('STARTING! the driver', self.id, 'picks up',
        # rider.identifier, 'at', self.location)
        self.driver_destination = rider.destination
        # ^^ add THIS
        # start_ride is FOR RIDER
        rider.is_satisfied()
        # if the rider doesn't cancel before pickup,
        # the driver picks up the rider
        # return self.start_drive(rider.destination)
        # if the rider doesn't cancel before pickup,
        # the driver picks up the rider
        return self.get_travel_time(
            rider.destination)  # get destination from rider class

    def end_ride(self) -> None:
        """End the current ride, and arrive at the rider's destination.

        Precondition: The driver has a rider.
        Precondition: self.destination is not None.

        """
        # this signals the driver to end the DRIVER b/c
        # the rider is already satisfied with their request
        self.end_drive()
        # self.location = self.driver_destination
        # WORK ON THIS


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(
        config={'extra-imports': ['location', 'rider']})
