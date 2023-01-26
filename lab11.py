import requests
import json
from pprint import pprint
import PySimpleGUI as sg

layout= [[sg.Input(size=(43, 1), key='in')],
        [sg.Button('Search')],
        [sg.Multiline('', tooltip='Text', auto_refresh = True, size=(50, 20), key='textBox')]]


window = sg.Window("Задача 11", layout)

while True:
    event, values = window.read()

    # Событие выхода:
    if event in (None, 'Exit'):
        break

    # Событие нажатия кнопки Search
    if event == 'Search':
        #Очищаем поле вывода
        window['textBox'].update('')

        #Получаем инфу
        username = values['in']
        url = f"https://api.github.com/users/{username}"

        #Данные json
        user_data = requests.get(url).json()


        try:
            required_data = f"Company: {user_data['company']},\nCreated at: {user_data['created_at']},\nEmail: {user_data['email']},\nID: {user_data['id']},\nName: {user_data['name']},\nURL: {user_data['url']}"
            window['textBox'].update(required_data)
            f = open('user_info.txt','w')
            f.write(required_data)
            f.close()
        except:
            sg.Popup('User not found')