class Visitor:
    all = []

    def __init__(self, name):
        self.name = name
        self.trip = []
        self.national_park = []
        # Visitor.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
    
    # the fuckin read me is wrong i am fucking dead
    # @name.setter
    # def name(self, name):
    #     if isinstance(name, str) and 1 <= len(name) <= 15:
    #         self._name = name
    #     else: 
    #         raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            # self.trip = new_trip WRONG
            self.trip.append(new_trip)
        return self.trip
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        if new_national_park not in self.national_park and isinstance(new_national_park, NationalPark):
            self.national_park.append(new_national_park)
        return self.national_park
    
# made 5 mistakes 
# did not invoke in trip so was not being called in other modules 
# also could not figure out llast function 
# wrote returns wrong for a couple 4 functions did not return or did not put self




