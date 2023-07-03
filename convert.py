import PySimpleGUI as sg

layout = [
	[	
		sg.Input(key = '-INPUT-'), 
		sg.OptionMenu(values = ['m to km','g to kg','sec to min'],default_value = 'm to km', key = '-UNITS-'),
		sg.Button('Convert', key = '-BUTTON-')
	],
	[sg.Text('Result', enable_events = True, key = '-RESULT-')]
]
win = sg.Window('Converter-dEfy',layout)

while True:
	event,values = win.read()
	if event == sg.WIN_CLOSED:
		break

	if event == '-BUTTON-':
		entry = (values['-INPUT-'])
		if entry.isnumeric():
			match values['-UNITS-']:
				case 'm to km':
					result = float(entry) / 1000
					result_strg = f'{entry} m are {result} kilometers.'

				case 'g to kg':
					result = round(float(entry) / 1000,3)
					result_strg = f'{entry} g are {result} kilograms.'

				case 'sec to min':
					result = round(float(entry) / 60,2)
					result_strg = f'{entry} seconds are {result} minutes.'

			win['-RESULT-'].update(result_strg)

		else:
			win['-RESULT-'].update('Please enter a number')

win.close()
