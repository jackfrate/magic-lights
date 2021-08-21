"""
class that sets up a controller for the lgihts with the right IP 
"""

from magichue import discover_bulbs, Light


class ListLister:
    def __init__(self):
        self.ip_list = discover_bulbs()
        self.light_list = [Light(ip) for ip in self.light_list]

    def get_light(self, index: int):
        """
        return a light from the light list  
        """
        return self.light_list[index]

    def get_light_indicies(self):
        """
        get a list of light indexes
        """
        return [i for i in range(0, len(self.light_list))]
    