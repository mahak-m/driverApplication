"""
The rider module contains the Rider class. It also contains
constants that represent the status of the rider.

=== Constants ===
WAITING: A constant used for the waiting rider status.
CANCELLED: A constant used for the cancelled rider status.
SATISFIED: A constant used for the satisfied rider status
"""

from location import Location

WAITING = "waiting"
CANCELLED = "cancelled"
SATISFIED = "satisfied"


class Rider:
    """A rider for a ride-sharing service.

    """
    identifier: str
    patience: int
    origin: Location
    destination: Location
    status: str

    def __init__(self, identifier: str, patience: int, origin: Location,
                 destination: Location) -> None:
        """Initialize a Rider.

        """
        self.identifier = identifier
        self.patience = patience
        self.origin = origin
        self.destination = destination
        self.status = WAITING  # waiting by default

    # helper methods made public b/c of that one piazza post

    def __str__(self) -> str:
        return str(self.identifier)

    def is_cancelled(self) -> None:
        """
        If the rider's ride is cancelled, set their status
        to "CANCELLED."
        """
        self.status = CANCELLED  # do i do this?

    def is_satisfied(self) -> None:
        """
        If the rider has reached their destination, set
        their status to "SATISFIED"
        """
        self.status = SATISFIED


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={'extra-imports': ['location']})
