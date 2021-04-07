import PySimpleGUI as sg

def fillFunc(message):
    print(message)

layout = [[sg.Text("Alerts", background_color = "white",text_color="black",justification ="left",font = ("Helvetica", 30),key = "alert"),sg.Graph(canvas_size=(50,50),graph_bottom_left=(0, 0),graph_top_right=(50,50),key = "graph", background_color = "white",pad=((5,0),3)),sg.Text("Water Tank Needs to be Filled",background_color= "#800000",text_color="white",k="banner",font = ("Helvetica", 31),pad=((0,5),3))],
          [sg.Text("Water Stations", background_color = "white",text_color="black",size= (20,1),justification = "right",font = ("Helvetica", 30)),sg.Button("Select All",button_color  = "#800000",font = ("Helvetica", 30))],
          [sg.Button("1",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("2",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("3",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("4",button_color  = "#800000",font = ("Helvetica", 90))]]

window = sg.Window("Liquid Dispenser", layout, element_justification='c', background_color = "white").Finalize()
graph = window.Element("graph")
graph.draw_polygon([(0,25),(50,0),(50,50)], fill_color="#800000")
window["graph"].update()
window["graph"].update(visible =False)
window["banner"].update(visible=False)
window["alert"].update(visible=False)

while True:
    if True:
        window["graph"].update(visible =False)
        window["banner"].update(visible=False)
        window["alert"].update(visible=False)
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '1':
        fillFunc("1")
    if event == '2':
        fillFunc("2")
    if event == '3':
        fillFunc("3")
    if event == '4':
        fillFunc("4")
    if event == 'Select All':
        fillFunc("All")

window.close()
