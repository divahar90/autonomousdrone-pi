import math

from sg.nus.iss.autonomousdrone.sensors import simulator
from sg.nus.iss.autonomousdrone.vehicle.vehicle import Vehicle


class FlightData:

    __EARTH_RADIUS_IN_METERS = 6371000
    def __init__(self, vehicle):
         # Check for correct input
         if isinstance(vehicle, Vehicle) is False:
             raise TypeError('Expected object of type Vehicle, got '+type(vehicle).__name__)

         self.__vehicle = vehicle
         return

    #Haversine Formula
    # Returns the distance between 2 GPS coordiantes represented by latitude-longitude parameters.
    def calculate_distance(self, lat1, lon1, lat2, lon2):
        if not isinstance(lat1, float) or not isinstance(lon1, float) or not isinstance(lat2, float) or not isinstance(lon2, float):
            raise TypeError('Expected type float')

        phi1 = self.__degree_to_radian(lat1)
        phi2 = self.__degree_to_radian(lat2)
        dPhi = self.__degree_to_radian((lat2-lat1))
        dLambda = self.__degree_to_radian(lon2-lon1)

        a = math.sin(dPhi/2)*math.sin(dPhi/2) + math.cos(phi1)*math.cos(phi2)*math.sin(dLambda/2)*math.sin(dLambda/2)
        c = 2* math.atan2(math.sqrt(a), math.sqrt(1-a))
        distance_in_meters = self.__EARTH_RADIUS_IN_METERS*c
        return distance_in_meters

    # Returns the equivalent degree in radians.
    def __degree_to_radian(self, deg):
        if not isinstance(deg, float):
            raise TypeError('Expected variable of type float and got a variable of type ' + type(deg).__name__)

        return deg * (math.pi/180)

    # Return the current latitude of the drone according to its GPS device
    def get_current_latitude(self):
        return float(simulator.latitude_reading())
        #return self.__vehicle.get_location_latitude()

    # Return the current longitude of the drone according to its GPS device
    def get_current_longitude(self):
        return float(simulator.longitude_reading())
        #return self.__vehicle.get_location_longitude()

    # Return the current height of the drone according to its devices in centimeters
    def get_current_height(self):
        #return int(simulator.height_reading())
        return self.__vehicle.get_location_altitude()
