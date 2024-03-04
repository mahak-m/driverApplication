"""Locations for the simulation"""

from __future__ import annotations


class Location:
    """A two-dimensional location."""

    row: int
    column: int

    def __init__(self, row: int, column: int) -> None:
        """Initialize a location.

        """
        self.row = row
        self.column = column

    def __str__(self) -> str:
        """Return a string representation.

        """
        a = str(self.row)
        b = str(self.column)
        return '(' + a + ',' + b + ')'

    def __eq__(self, other: Location) -> bool:
        """Return True if self equals other, and false otherwise.

        """
        return self.row == other.row and self.column == other.column


def manhattan_distance(origin: Location, destination: Location) -> int:
    """Return the Manhattan distance between the origin and the destination.

    """
    rows = abs(origin.row - destination.row)
    columns = abs(origin.column - destination.column)
    return rows + columns


def deserialize_location(location_str: str) -> Location:
    """Deserialize a location.

    location_str: A location in the format 'row,col'
    """
    # first split at the comma b/c format = (r,c)
    r, c = location_str.split(',')
    # convert into integer
    r, c = int(r), int(c)
    return Location(r, c)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all()
