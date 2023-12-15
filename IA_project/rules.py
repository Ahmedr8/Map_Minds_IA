from experta import Fact, Rule, KnowledgeEngine
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
        self.recommendations.append("Tunis")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="desert"))
    def recommend_sunny_desert(self):
        self.recommendations.append("Touzer")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"),BudgetPreference(budget="cheap"),CulturePreference(culture="Urbanized"),AccomodationPreference(accomodation="Hotels"),FoodPreference(food="spicy"))
    def recommend_sunny_desert(self):
        self.recommendations.append("Hmmamet")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"), FoodPreference(food="spicy"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"), CulturePreference(culture="Urbanized"))
    def recommend_beach_destination(self):
        self.recommendations.append("Bali")
    @Rule(WeatherPreference(weather="cold"), NaturePreference(nature="mountains"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"), CulturePreference(culture="Wildlife"))
    def recommend_mountain_resort(self):
        self.recommendations.append("Swiss Alps")
    @Rule(WeatherPreference(weather="rainy"), NaturePreference(nature="forest"), FoodPreference(food="tropical fruits"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="moderate"),CulturePreference(culture="Wildlife"))
    def recommend_rainforest_resort(self):
        self.recommendations.append("Amazon Rainforest")
    @Rule(WeatherPreference(weather="snowy"), NaturePreference(nature="mountains"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Wildlife"))
    def recommend_snowy_mountains_resort(self):
        self.recommendations.append("Swiss Alps")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="island"), FoodPreference(food="seafood"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_island_resort(self):
        self.recommendations.append("Maldives")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="tropical"),FoodPreference(food="tropical fruits"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="Urbanized"))
    def recommend_tropical_hotel(self):
        self.recommendations.append("Hawaii")
    @Rule(WeatherPreference(weather="cold"), NaturePreference(nature="island"), FoodPreference(food="seafood"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_cold_island_resort(self):
        self.recommendations.append("Iceland")
    @Rule(WeatherPreference(weather="rainy"), NaturePreference(nature="beaches"), FoodPreference(food="Arab food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_beach_history(self):
        self.recommendations.append("Istanbul")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"), FoodPreference(food="Arab food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_beach_history(self):
        self.recommendations.append("Egypt")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"), FoodPreference(food="seafood"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_sunny_beach_resort(self):
        self.recommendations.append("Thailand")
    @Rule(WeatherPreference(weather="snowy"), NaturePreference(nature="mountains"), FoodPreference(food="local"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="History"))
    def recommend_snowy_mountains_history(self):
        self.recommendations.append("Swiss Alps")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="island"), FoodPreference(food="tropical fruits"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_island_tropical_resort(self):
        self.recommendations.append("Bora Bora")
    @Rule(WeatherPreference(weather="rainy"), NaturePreference(nature="island"), FoodPreference(food="seafood"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_rainy_island_history(self):
        self.recommendations.append("Greece")
    @Rule(WeatherPreference(weather="cold"), NaturePreference(nature="mountains"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="Urbanized"))
    def recommend_cold_mountains_urbanized(self):
        self.recommendations.append("Austria")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="forest"), FoodPreference(food="fast food"),AccomodationPreference(accommodation="Hotels"), BudgetPreference(price="moderate"),CulturePreference(culture="History"))
    def recommend_sunny_forest_history(self):
        self.recommendations.append("Japan")
    @Rule(WeatherPreference(weather="rainy"), NaturePreference(nature="island"), FoodPreference(food="seafood"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="Urbanized"))
    def recommend_rainy_island_urbanized(self):
        self.recommendations.append("Singapore")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"), FoodPreference(food="Arab food"),AccomodationPreference(accommodation="Resorts"), BudgetPreference(price="expensive"),CulturePreference(culture="History"))
    def recommend_sunny_beach_arab_history(self):
        self.recommendations.append("Dubai")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="beaches"))
    def recommend_sunny_beach(self):
        self.recommendations.append("USA")
    @Rule(WeatherPreference(weather="rainy"), NaturePreference(nature="forest"))
    def recommend_rainy_forest(self):
        self.recommendations.append("Brazil")
    @Rule(WeatherPreference(weather="cold"), NaturePreference(nature="mountains"))
    def recommend_cold_mountains(self):
        self.recommendations.append("Canada")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="island"))
    def recommend_sunny_island(self):
        self.recommendations.append("Greece")
    @Rule(WeatherPreference(weather="sunny"), NaturePreference(nature="island"))
    def recommend_sunny_island_djerba(self):
        self.recommendations.append("Djerba")
    @Rule(WeatherPreference(weather="snowy"), NaturePreference(nature="mountains"))
    def recommend_snowy_mountains(self):
        self.recommendations.append("USA")




