# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
import random
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionPlayRPS(Action):

    def name(self) -> Text:
        return "action_play_rps"

    @staticmethod
    def computer_choice() -> str:
        return random.choice(["rock", "paper", "scissors"])

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_choice = tracker.get_slot("choice")
        if user_choice not in ["rock", "paper", "scissors"]:
            dispatcher.utter_message(text=f"Unknown choice {user_choice}.")
            return []

        dispatcher.utter_message(text=f"You chose {user_choice}")
        comp_choice = self.computer_choice()
        dispatcher.utter_message(text=f"The computer chose {comp_choice}")

        user_won = {
            # user, computer
            ("rock", "scissors"): True,
            ("rock", "paper"): False,
            ("paper", "rock"): True,
            ("paper", "scissors"): False,
            ("scissors", "paper"): True,
            ("scissors", "rock"): False,
        }
        
        if user_choice == comp_choice:
            dispatcher.utter_message(text="It's a tie!")

        if user_won[user_choice, comp_choice]:
            dispatcher.utter_message(text="Congrats, you won!")
        else:
            dispatcher.utter_message(text="The computer won this round.")

        return []
