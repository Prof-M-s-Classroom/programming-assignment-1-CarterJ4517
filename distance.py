import datetime

class Distance:
    """
    Class to represent a distance measurement with timestamp.
    """
    def __init__(self, distance):
        """Initialize the Distance object with distance and timestamp."""
        self.distance = distance
        self.time = datetime.datetime.now().timestamp()

    def __str__(self):
        """Return a formatted string representation of the Distance object."""
        return f"Distance of {self.distance} taken at {self.time}"
