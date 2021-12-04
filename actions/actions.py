# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType
from rasa_sdk.types import DomainDict

import requests, json
from datetime import datetime

class ValidarFormulario(FormValidationAction):
        telefono = 0
        nombre = ''
        def name(self) -> Text:
            return 'validacion_formulario'

        def run(self,
                dispatcher: "CollectingDispatcher", 
                tracker: "Tracker", 
                domain: "DomainDict"
                ) -> List[EventType]:
                nombre = str(tracker.get_slot('nombreFormulario'))
                telefono = str(tracker.get_slot('telefonoFormulario'))
                if nombre is not None and telefono is not None:
                        print('Nombre:', nombre)
                        print('Telefono:', telefono)
                        conversacion = tracker.events
                        arreglo = []
                        user = ''
                        bot = ''
                        for i in conversacion:
                                if i['event'] == 'user':
                                        user = '- Usuario: '+ str(i['text'])
                                        #print(user)
                                        arreglo.append(user)
                                elif i['event'] == 'bot':
                                        bot = '- Bot: '+ str(i['text'])
                                        #print(bot)
                                        arreglo.append(bot)
                        #print(arreglo)
                        #dispatcher.utter_message(response='utter_ask_validarDatosFormulario')
                        if len(arreglo) > 0:
                                fecha = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                                response = requests.post('https://get-data-chatbot.josluisluis13.repl.co/data', data= {'fecha': fecha, 'nombre': nombre, 'telefono': telefono, 'conversacion': json.dumps(arreglo)})
                                if response.status_code == 200:
                                        dispatcher.utter_message(response='utter_Formulario_validado')
                else:
                        print('Falta algún dato')
                        dispatcher.utter_message(text='Algo está mal')
                return []
                        

