import PySimpleGUI as sg

layout = [[sg.Text("Alerts", background_color = "white",text_color="black",justification ="center",font = ("Helvetica", 30)),sg.Graph(canvas_size=(50,50),graph_bottom_left=(0, 0),graph_top_right=(50,50),key = "graph", background_color = "white",pad=((5,0),3)),sg.Text("Water Tank Needs to be Filled",background_color= "#800000",text_color="white",k="banner",font = ("Helvetica", 31),pad=((0,5),3))],[sg.Text("Water Stations", background_color = "white",text_color="black",size= (20,1),justification = "right",font = ("Helvetica", 30)),sg.Button("Select All",button_color  = "#800000",font = ("Helvetica", 30))],[sg.Button("1",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("2",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("3",button_color  = "#800000",font = ("Helvetica", 90)),sg.Button("4",button_color  = "#800000",font = ("Helvetica", 90))]]

window = sg.Window("Liquid Dispenser", layout, element_justification='c', background_color = "white").Finalize()
graph = window.Element("graph")
graph.draw_polygon([(0,25),(50,0),(50,50)], fill_color="#800000")
window["graph"].update()

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

window.close()