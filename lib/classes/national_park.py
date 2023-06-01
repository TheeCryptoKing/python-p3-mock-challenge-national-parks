class NationalPark:

    def __init__(self, name):
        self.name = name
        self._trips = []
        self._visitors = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and not hasattr(self, 'name'):
            self._name = name
        else:
            raise Exception
        
    def trips(self, new_trip=None):
        from classes.trip import Trip
        if new_trip and isinstance(new_trip, Trip):
            self._trips.append(new_trip)
        return self._trips
        pass
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        if new_visitor and isinstance(new_visitor, Visitor):
            self._visitors.append(new_visitor)
        return list(set(self._visitors))
        pass
    
    
    def total_visits(self):
        return len(self._trips)
        # return len(self._visitors)
        pass
    
    def best_visitor(self):
        return max(set(self._visitors), key=self._visitors.count)
        # pass
        # visitor = None
        # visits = 0
        # for v in self._visitors:
        #     if self._visitors.count(v) > visits:
        #         visitor = v
        #         visits =  self._visitors.count(v)
        #     return visitor
        
        # for v in self._trips:
        #     # self._trips.visitor
        #     if self._trips.count(v) > visits:
        #         visitor = v.visitor
        #         visits = self._trips.count(v)
        #     return visitor

    # Syntax of sorted() 
    #  sorted(self.trip, key=lambda index: index.end_date)
    # Syntax of sort()
    #  list.sort(key=lambda index, reverse)