import math

class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def distance(self):
        # Calculates the distance between the star and Earth
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

def k_closest_stars(stars, k):
    # Calculates the distance of each star from Earth
    distances = [star.distance() for star in stars]
    
    # Sorts the stars based on their distance from Earth
    sorted_stars = [star for _, star in sorted(zip(distances, stars))]
    
    # Returns the k closest stars
    return sorted_stars[:k]


class Star (self, name, pos)