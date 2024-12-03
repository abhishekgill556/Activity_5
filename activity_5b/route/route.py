"""
Description: Defines the Route class to represent a bus route in the transit system.
Author: Abhishek Gill
"""

from bus.bus import Bus

class Route:
    """
    A class to represent a bus route.
    """

    def __init__(self, route_id, start_point, end_point):
        """
        Constructs all the necessary attributes for the route object.

        Args:
            route_id (str): The unique identifier for the route.
            start_point (str): The starting point of the route.
            end_point (str): The end point of the route.

        Raises:
            ValueError: If route_id, start_point, or end_point is not a string.
        """
        if not isinstance(route_id, str):
            raise ValueError("route_id must be a string")
        if not isinstance(start_point, str):
            raise ValueError("start_point must be a string")
        if not isinstance(end_point, str):
            raise ValueError("end_point must be a string")
        
        self.__route_id = route_id
        self.__start_point = start_point
        self.__end_point = end_point
        self.__buses = []

    @property
    def route_id(self):
        """
        Returns the route id.
        Returns:
            str: the route id of the route instance.
        """
        return self.__route_id

    @property
    def start_point(self):
        """
        Returns the start point.
        Returns:
            str: the start point of the route instance.
        """
        return self.__start_point

    @property
    def end_point(self):
        """
        Returns the end point.
        Returns:
            str: the end point of the route instance.
        """
        return self.__end_point

    @property
    def buses(self):
        """
        Returns a list of busses.
        Returns:
            list: A list of busses for the route instance.
        """
        return self.__buses

    def add_bus(self, bus):
        """
        Adds a bus to the route.

        Args:
            bus (Bus): An instance of the Bus class to be added to the route.

        Raises:
            ValueError: If the bus is not an instance of the Bus class.
        """
        if not isinstance(bus, Bus):
            raise ValueError("bus must be an instance of Bus")
        
        self.__buses.append(bus)

    def __str__(self):
        """
        Returns a string representation of the route.

        Returns:
            str: A string containing the route's details.
        """
        bus_details = ', '.join(str(bus) for bus in self.__buses)
        return f"Route ID: {self.__route_id}, Start: {self.__start_point}, End: {self.__end_point}, Buses: [{bus_details}]"
