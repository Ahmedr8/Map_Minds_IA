
class UserPreferences:
    def __init__(self, weather, nature, budget,food,culture,accomodation):
        self.weather = weather
        self.nature = nature
        self.budget = budget
        self.food=food
        self.culture=culture
        self.accomodation=accomodation

class Suggession:
    def __init__(self,pays,gouvernorat):
        self.pays=pays
        self.gouvernorat=gouvernorat

    def serialize(self):
        return {'pays': self.pays, 'gouvernorat': self.gouvernorat}
