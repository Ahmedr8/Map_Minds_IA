from experta import Fact, Rule, KnowledgeEngine
from .models import Suggession
class CulturePreference(Fact):
    pass
class BudgetPreference(Fact):
    pass
class AccomodationPreference(Fact):
    pass
class FoodPreference(Fact):
    pass
class NaturePreference(Fact):
    pass
class WeatherPreference(Fact):
    pass

class RecommendationEngine(KnowledgeEngine):
    pass

class RecommendationEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.recommendations = []

    def get_recommendations(self):
        return self.recommendations

    @Rule(BudgetPreference(budget="cheap"))
    def recommend_cheap_nature(self):
        res=Suggession("Tunisia","")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="desert"))
    def recommend_sunny_desert(self):
        res = Suggession("Tunisia", "Touzer")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"),BudgetPreference(budget="cheap"),CulturePreference(culture="Urbanized"),AccomodationPreference(accomodation="Hotels"),FoodPreference(food="spicy"))
    def recommend_sunny_desert(self):
        res = Suggession("Tunisia", "Hmmamet")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"), FoodPreference(food="spicy"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"), CulturePreference(culture="Urbanized"))
    def recommend_beach_destination(self):
        res = Suggession("Bali", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cold"), NaturePreference(nature="Mountains"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"), CulturePreference(culture="Wildlife"))
    def recommend_mountain_resort(self):
        res = Suggession("Swiss", "Alps")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Rainy"), NaturePreference(nature="Tropical"), FoodPreference(food="Tropical Fruits"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="moderate"),CulturePreference(culture="Wildlife"))
    def recommend_rainforest_resort(self):
        res=Suggession("Amazon","RainTropical")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cloudy"), NaturePreference(nature="Mountains"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Wildlife"))
    def recommend_snowy_mountains_resort(self):
        res = Suggession("Swiss", "Alps")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Islands"), FoodPreference(food="Sea Food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_island_resort(self):
        res = Suggession("Maldives", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="tropical"),FoodPreference(food="Tropical Fruits"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="Urbanized"))
    def recommend_tropical_hotel(self):
        res = Suggession("USA", "Hawaii")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cold"), NaturePreference(nature="Islands"), FoodPreference(food="Sea Food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_cold_island_resort(self):
        res = Suggession("Iceland", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Rainy"), NaturePreference(nature="Beaches"), FoodPreference(food="Arab Food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_beach_history(self):
        res = Suggession("Turkey", "Istanbul")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"), FoodPreference(food="Arab Food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_beach_history_egypt(self):
        res = Suggession("Egypt", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"), FoodPreference(food="Sea Food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_sunny_beach_resort(self):
        res = Suggession("Thailand", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cloudy"), NaturePreference(nature="Mountains"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="History"))
    def recommend_snowy_mountains_history(self):
        res = Suggession("Swiss", "Alps")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Islands"), FoodPreference(food="Tropical Fruits"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_island_tropical_resort(self):
        res = Suggession("Tahiti", "Bora Bora")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Rainy"), NaturePreference(nature="Islands"), FoodPreference(food="Sea Food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_island_history(self):
        res = Suggession("Greece", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cold"), NaturePreference(nature="Mountains"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="Urbanized"))
    def recommend_cold_mountains_urbanized(self):
        res = Suggession("Austria", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Tropical"), FoodPreference(food="Fast Food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_sunny_forest_history(self):
        res = Suggession("Japan", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Rainy"), NaturePreference(nature="Islands"), FoodPreference(food="Sea Food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_rainy_island_urbanized(self):
        res = Suggession("Singapore", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"), FoodPreference(food="Arab Food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="History"))
    def recommend_sunny_beach_arab_history(self):
        res = Suggession("EAU", "Dubai")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Beaches"))
    def recommend_sunny_beach(self):
        res = Suggession("USA", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Rainy"), NaturePreference(nature="Tropical"))
    def recommend_rainy_forest(self):
        res = Suggession("Brazil", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cold"), NaturePreference(nature="Mountains"))
    def recommend_cold_mountains(self):
        res = Suggession("Canada", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Islands"))
    def recommend_sunny_island(self):
        res = Suggession("Greece", "")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Sunny"), NaturePreference(nature="Islands"))
    def recommend_sunny_island_djerba(self):
        res = Suggession("Tunisia", "Djerba")
        self.recommendations.append(res)
    @Rule(WeatherPreference(weather="Cloudy"), NaturePreference(nature="Mountains"))
    def recommend_snowy_mountains(self):
        res = Suggession("USA", "")
        self.recommendations.append(res)




