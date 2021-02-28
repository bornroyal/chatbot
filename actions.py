
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionRecipeRequest(Action):
#
    def name(self) -> Text:
        return "action_recipe"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        """

        :type dispatcher: object
        """
        food = tracker.get_slot('food')
        api_key = '7075a0af87f14d49b970760944d77ef3'
        params = {'query': food , 'apiKey': api_key}
        url = 'https://api.spoonacular.com/recipes/complexSearch'
        status = requests.get(url, params)
        response = status.json()
        recipe = response['results'][0]
        url2 = 'https://api.spoonacular.com/recipes/716429/information?includeNutrition=false'
        params2 = {'id': recipe['id'], 'apiKey': api_key}
        res2 = requests.get(url2, params2)
        json2 = res2.json()
        link_recipe = 'The title of the recipe is: ' + json2['title'] + ' The link to the recipe is: ' + json2['sourceUrl']





        dispatcher.utter_message('Here is your recipe ' + link_recipe)


        return []








