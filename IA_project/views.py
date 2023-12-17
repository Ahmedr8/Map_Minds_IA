from django.http import JsonResponse
from .models import UserPreferences
from .rules import RecommendationEngine, WeatherPreference, NaturePreference, FoodPreference, AccomodationPreference, \
    BudgetPreference, CulturePreference
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
@csrf_exempt
def recommend_destination(request):
    data = json.loads(request.body)
    if(data.get("budget")<=2000):
        budget="cheap"
    elif (data.get("budget")<=6500):
        budget="moderate"
    else:
        budget="expensive"
    user_preferences = UserPreferences(data.get("weather"),data.get("nature"),budget,data.get("food"),data.get("culture"),data.get("accommodation"))
    engine = RecommendationEngine()
    engine.reset()
    engine.declare(WeatherPreference(weather=user_preferences.weather))
    engine.declare(NaturePreference(nature=user_preferences.nature))
    engine.declare(FoodPreference(food=user_preferences.food))
    engine.declare(AccomodationPreference(accomodation=user_preferences.accommodation))
    engine.declare(BudgetPreference(budget=user_preferences.budget))
    engine.declare(CulturePreference(culture=user_preferences.culture))
    engine.run()
    recommendations = engine.get_recommendations()
    recommendations_serializer = json.dumps([suggestion.serialize() for suggestion in recommendations])
    return JsonResponse(json.loads(recommendations_serializer), safe=False,status=status.HTTP_200_OK)

