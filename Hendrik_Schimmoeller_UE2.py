import math

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx ** 2 + dy ** 2)#Euclidian Distance Formula
    
    def area(self):
        return 0
    
earth_radius = 6371

class Geographic_Point(Point): #Like Point Class: just uses lon/lat instead of x,y
    def __init__(self, lon, lat):
        super().__init__(lon, lat)

    def distance_on_earth(self, other):
        r = earth_radius

        phi1 = math.radians(self.y) #define different values / angles
        phi2 = math.radians(other.y)
        delta_phi = math.radians(other.y - self.y)
        delta_lambda = math.radians(other.x - self.x)

        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2 #Formula from PDF
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a)) #Formula from PDF

        return r * c

# Tests
p1 = Point(10, 10)
p2 = Point(5, 6)
print("Euclidean Distance:", p1.distance(p2))

"""lon1 = float(input("Enter lon for point 1: ")) #input if user wants to choose their own lat/lon coordinates
lat1 = float(input("Enter lat for point 1: "))
lon2 = float(input("Enter lon for point 2: "))
lat2 = float(input("Enter lat for point 2: "))"""

gp1 = Geographic_Point(53.3, 10) #Coordinates Hamburg
gp2 = Geographic_Point(48.8, 11.3)#Coordinates Munich
print("The Haversine Distance is :", gp1.distance_on_earth(gp2))

print("MRO:", Geographic_Point.mro()) 