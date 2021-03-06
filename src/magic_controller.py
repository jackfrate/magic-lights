"""
class that sets up a controller for the lgihts with the right IP 
"""

from magichue import discover_bulbs, Light


class LightLister:
    # this needs to be static || im tripping
    ip_list = discover_bulbs()

    def __init__(self):
        self.refresh_list()

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

    def get_ip_list(self):
        """
        get list of every ip
        """
        return self.ip_list

    def refresh_list(self):
        """
        rescan the network for lights
        """
        # self.ip_list = discover_bulbs()
        self.light_list = [Light(ip) for ip in self.ip_list]

    def change_color(self, r: int, g: int, b: int, index: int):
        """
        change color of a light with rgb values
        """
        light = self.light_list[index]
        # make sure its not in white mode
        light.is_white = False 
        light.rgb = (r, g, b)
    
    def change_brightness(self, brightness: int, index: int):
        """
        change the brighness of a light
        """
        light = self.light_list[index]
        light.brightness = brightness

    def get_light_status(self, index: int):
        """
        get the status of a light in a dictionary
        """
        light = self.light_list[index]
        ret = {}
        ret["bright"] = light.brightness
        ret['r'] = light.rgb[0]
        ret['g'] = light.rgb[1]
        ret['b'] = light.rgb[2]
        ret['a'] = 255
        return ret
