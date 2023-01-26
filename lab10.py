import PySimpleGUI as sg
import re

layout1 = [[sg.Input('',tooltip='Number 1', size=(10, 1), key='N1'), sg.Combo(['+','-','*', '/'], default_value='+', key='operation'), sg.Input('',tooltip='Number 2', size=(10, 1), key='N2'), sg.Text('=', size=(1,1)), sg.Multiline('', tooltip='Answer', auto_refresh = True, no_scrollbar = True, size=(10, 1), key='answer')],
           [sg.Button('Calculate')]]

layout2=[[sg.Checkbox(text='1', key='ch1')],
         [sg.Checkbox(text='2', key='ch2')],
         [sg.Checkbox(text='3', key='ch3')],
         [sg.Button('Check')]]

layout3= [[sg.FileBrowse(file_types=(("TXT Files", "*.txt")), key='browse'), sg.Input(size=(43, 1), key='in')],
          [sg.Button('Get started')],
          [sg.Multiline('', tooltip='Text', auto_refresh = True, size=(50, 20), key='textBox')]]

      
tabs = [[sg.TabGroup([[sg.Tab('      Calculator      ', layout1, element_justification = 'center'),
                       sg.Tab('      Checkboxes      ', layout2, element_justification = 'center'),
                       sg.Tab('         Text         ', layout3, element_justification = 'left')]],
                       tab_location = "centertop",
                       border_width=5)]]  
        
window = sg.Window("Нурулаев Эльдар Сиражудинович", tabs)

while True:
    event, values = window.read()

    # Событие выхода:
    if event in (None, 'Exit'):
        break

    # Событие нажатия кнопки Calculate в калькуляторе
    if event == 'Calculate':
        window['answer'].update('')
        a = values['N1']
        b = values['N2']
        
        #Валидация полей регулярным выражением
        if re.fullmatch(r'[+-]?\d+[.]?\d*', a) and re.fullmatch(r'[+-]?\d+[.]?\d*', b):
            a = float(values['N1'])
            b = float(values['N2'])

            c = values['operation']

            if c == "+":
                window['answer'].update(a + b)
            if c == "-":
                window['answer'].update(a - b)
            if c == "*":
                window['answer'].update(a * b)
            if c == "/":
                window['answer'].update(a / b)
    
        else:
            sg.Popup('Use only numbers')

    #События нажатия кнопки Check на вкладке с чекбоксами
    if event == 'Check':    
        checkbox_values = [values['ch1'], values['ch2'], values['ch3']]
        check_message = "Selected options: "

        index_elem = 0
        index_true = 0

        for value in checkbox_values:
            index_elem += 1
            if value == True:
                check_message += f'{index_elem}  '
                index_true += 1

        if index_true > 0:
            sg.Popup(check_message)
        else:
            sg.Popup('No options selected')

    if event == 'Get started':
        f = open(values['in'], encoding='utf-8',  mode='r')
        text = f.read() 
        window['textBox'].update(text)
        f.close()

window.close()    