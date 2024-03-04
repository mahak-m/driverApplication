"""Dispatcher for the simulation"""

from typing import Optional
from driver import Driver
from rider import Rider


class Dispatcher:
    """A dispatcher fulfills requests from riders and drivers for a
    ride-sharing service.

    When a rider requests a driver, the dispatcher assigns a driver to the
    rider. If no driver is available, the rider is placed on a waiting
    list for the next available driver. A rider that has not yet been
    picked up by a driver may cancel their request.

    When a driver requests a rider, the dispatcher assigns a rider from
    the waiting list to the driver. If there is no rider on the waiting list
    the dispatcher does nothing. Once a driver requests a rider, the driver
    is registered with the dispatcher, and will be used to fulfill future
    rider requests.
    """

    curr_drivers: list
    waiting_list: list

    def __init__(self) -> None:
        """Initialize a Dispatcher.
        """
        self.curr_drivers = []
        self.waiting_list = []  # riders

    def __str__(self) -> str:
        """Return a string representation.

        """
        return 'There are ' + str(len(self.waiting_list)) + ' riders waiting'

    def request_driver(self, rider: Rider) -> Optional[Driver]:
        """Return a driver for the rider, or None if no driver is available.

        Add the rider to the waiting list if there is no available driver.

        """
        # first make a list of available drivers
        available = []
        for i in self.curr_drivers:
            if i.is_idle is True:
                available.append(i)

        # calculate the manhattan distance between each driver + rider
        # divide distance by speed to get estimated time of arrival (ETA)
        if available:
            chosen = available[0]
            # start with first in list as default
            total_eta = chosen.get_travel_time(rider.origin)

            # now compare the ETA's of every available driver
            for i in available:
                ETA = i.get_travel_time(rider.origin)
                if ETA < total_eta:
                    chosen = i
                    total_eta = ETA

            # change rider status to SATISFIED when they get a driver

            return chosen
        else:
            # add to waiting list and return None
            self.waiting_list.append(rider)
            return None

    def request_rider(self, driver: Driver) -> Optional[Rider]:
        """Return a rider for the driver, or None if no rider is available.

        If this is a new driver, register the driver for future rider requests.

        """
        if driver not in self.curr_drivers:  # new driver = add
            self.curr_drivers.append(driver)

        if self.waiting_list:  # if self.waiting_list != []
            assigned = self.waiting_list.pop(0)
            driver.driver_destination = assigned.destination
            return assigned  # return first in waiting list
        else:
            return None  # no rider in waiting list

    def cancel_ride(self, rider: Rider) -> None:
        """Cancel the ride for rider.

        """
        # change rider status to CANCELLED (piazza post @227):
        rider.is_cancelled()
        # if in waiting list, remove
        if rider in self.waiting_list:
            self.waiting_list.remove(rider)
        else:  # rider already has a driver
            pass


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['typing', 'driver', 'rider']})
