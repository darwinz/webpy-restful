import json
import random
from itertools import count


class ThermostatModel:
    _ids = count(98)

    def __init__(self):
        self.ID = next(self._ids)
        self.Name = None
        self.Operating_Mode = None
        self.Fan_Mode = None
        self.Cool_Set_Point = None
        self.Heat_Set_Point = None
        self.set_point_min = 30
        self.set_point_max = 100
        self.operating_modes = ['cool', 'heat', 'off']
        self.fan_modes = ['auto', 'on']

    @property
    def get_ID(self):
        return self.ID

    @property
    def get_name(self):
        return self.Name

    def set_name(self, name):
        self.Name = name
        return self

    @property
    def get_temp(self):
        return random.randint(63, 78)

    @property
    def get_operating_mode(self):
        return self.Operating_Mode

    def set_operating_mode(self, mode):
        if mode in self.operating_modes:
            self.Operating_Mode = mode
        else:
            raise ValueError('Invalid operating mode provided')
        return self

    @property
    def get_fan_mode(self):
        return self.Fan_Mode

    def set_fan_mode(self, mode):
        if mode in self.fan_modes:
            self.Fan_Mode = mode
        else:
            raise ValueError('Invalid fan mode provided')
        return self

    @property
    def get_cool_set_point(self):
        return self.Cool_Set_Point

    def set_cool_set_point(self, point):
        if self.set_point_min <= point <= self.set_point_max:
            self.Cool_Set_Point = point
        else:
            raise ValueError('Invalid cool set point provided')
        return self

    @property
    def get_heat_set_point(self):
        return self.Heat_Set_Point

    def set_heat_set_point(self, point):
        if self.set_point_min <= point <= self.set_point_max:
            self.Heat_Set_Point = point
        else:
            raise ValueError('Invalid heat set point provided')
        return self

    def set_data(self, data):
        self.set_name(data['Name'])
        self.set_operating_mode(data['Operating_Mode'])
        self.set_fan_mode(data['Fan_Mode'])
        self.set_cool_set_point(data['Cool_Set_Point'])
        self.set_heat_set_point(data['Heat_Set_Point'])
        return self

    def to_json(self):
        data = {
            'ID': self.get_ID,
            'Name': self.get_name,
            'Current_Temp': self.get_temp,
            'Operating_Mode': self.get_operating_mode,
            'Fan_Mode': self.get_fan_mode,
            'Cool_Set_Point': self.get_cool_set_point,
            'Heat_Set_Point': self.get_heat_set_point
        }
        return data
