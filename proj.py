import tkinter
import tkinter.messagebox
import customtkinter
import tkintermapview as tkmap
import math

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# tkinter window
window = tkinter.Tk()
window.geometry('1020x620')
window.configure(bg='black')
window.resizable(False, False)
window.title("University of Karachi - Travel Guide")

# frames
frame1 = customtkinter.CTkFrame(master=window, width=340, height=600, corner_radius=10, fg_color='#676C6E')
frame1.pack(padx=10, pady=10, side='left')

frame2 = customtkinter.CTkFrame(master=window, width=660, height=600, corner_radius=10, fg_color='#3E4548')
frame2.pack(padx=10, pady=10, anchor='center')

# map widget
map_widget = tkmap.TkinterMapView(frame2, width=600, height=500, corner_radius=20)
map_widget.place(relx=0.5, rely=0.53, anchor=tkinter.CENTER, bordermode="outside")
map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal

# satellite view button
def satellite():
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google satellite

button = customtkinter.CTkButton(master=frame2, width=120, height=32, border_width=0, corner_radius=8, text="Satellite View", command=satellite)
button.place(relx=0.85, rely=0.05, anchor=tkinter.CENTER)

# normal view button
def normal():
    map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)  # google normal

button = customtkinter.CTkButton(master=frame2, width=120, height=32, border_width=0, corner_radius=8, text="Normal View", command=normal)
button.place(relx=0.638, rely=0.05, anchor=tkinter.CENTER)

# set current widget position and zoom
map_widget.set_position(24.940508358616473, 67.11723194010298) 
#map_widget.set_zoom(15)

# tabs
tabview = customtkinter.CTkTabview(frame1,width=340, height=600)
tabview.pack(padx=10, pady=10)

tabview.add("Home") 
tabview.add("About")  
tabview.set("Home")  

# About Tab
aboutTextbox = customtkinter.CTkTextbox(master=tabview.tab("About"), fg_color='#666666', width=300, height=400, font=('Calibri',15), activate_scrollbars=False)
aboutTextbox.place(relx=0.5, rely=0.41, anchor=tkinter.CENTER)

aboutTextbox.insert("0.0", "Built using: \n--------------\n-> Python\n-> Custom Tkinter by Tom Schimansky\n-> Tkinter\n\n")
aboutTextbox.insert("8.0", "Algorithm Used: \n--------------------\nDijkstra Algo. (Single Source Shortest Path)\n\n")
aboutTextbox.insert("11.0", "Map Tile Server Source: \n------------------------------\nSatellite and Normal View  =>  Google Maps\n\n")
aboutTextbox.insert("14.0", "\n****************************************\nBy Muhammad Habib Khan - B20102088\n4th Semester Project -- Data Structures \n@ DCS - UBIT  |  CS-B \n\nInstructed by 'Dr. Muhammad Saeed'")

aboutLabel = customtkinter.CTkLabel(master=tabview.tab("About"), text="Version 1.0.1", fg_color='transparent')
aboutLabel.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)

# Home
welcomeLabel = customtkinter.CTkLabel(master=tabview.tab("Home"), text="Bonjour!", fg_color='transparent', font=('Arial',35))
welcomeLabel.place(relx=0.22, rely=0.062, anchor=tkinter.CENTER)

# Textbox
textbox = customtkinter.CTkTextbox(master=tabview.tab("Home"), fg_color='#666666', width=300, height=200, font=('Calibri',15), scrollbar_button_color='#537BC0', scrollbar_button_hover_color='light blue')
textbox.place(relx=0.5, rely=0.32, anchor=tkinter.CENTER)

textbox.insert("0.0", "Welcome to University of Karachi - Travel \nGuide Application!\n-------------------------------------------------------\nNavigate easily between departments using\nthe shortest path avaiable.\n\n") 
textbox.insert("7.0", "                              Instructions: \n")
textbox.insert("8.0", "------------------------------------------------------- \n")
textbox.insert("9.0", "->  Select the buttons at 'top right' corner to\ntoggle between satellite and normal view\n\n")
textbox.insert("12.0", "->  Use the '+'  '-' buttons on the map or \nmouse scroll to zoom in / out of map\n\n")
textbox.insert("15.0", "->  Use the combo-box below to select the    source and destination from the drop down menu\n\n")
textbox.insert("18.0", "->  Click the 'Calculate' button to display the shortest path\n\n")
textbox.insert("21.0", "->  Click the 'Reset' button to clear the path")

textbox.configure(state="disabled") 

# Source
sourceLabel = customtkinter.CTkLabel(master=tabview.tab("Home"), text="Select Source", fg_color='transparent', font=('Arial',17))
sourceLabel.place(relx=0.2, rely=0.6, anchor=tkinter.S)

sourceCombo_var = customtkinter.StringVar(value="Select")
sourceCombo = customtkinter.CTkComboBox(master=tabview.tab("Home"), variable=sourceCombo_var, button_color='#537BC0', corner_radius=10)
sourceCombo.configure(values=["Select", "UBIT","IBA","KUBS","Pharmacy (old)","Botany","Microbiology","Zoology","Chemistry","App. Physics","App. Chemistry","Physics","Geology","Physiology","Food Science & Tech."])
sourceCombo.place(relx=0.34, rely=0.67, width=200, anchor=tkinter.S)

# Destination
destinationLabel = customtkinter.CTkLabel(master=tabview.tab("Home"), text="Select Destination", fg_color='transparent', font=('Arial',17))
destinationLabel.place(relx=0.24, rely=0.78, anchor=tkinter.S)

destinationCombo_var = customtkinter.StringVar(value="Select")
destinationCombo = customtkinter.CTkComboBox(master=tabview.tab("Home"), variable=destinationCombo_var, button_color='#537BC0', corner_radius=10)
destinationCombo.configure(values=["Select", "UBIT","IBA","KUBS","Pharmacy (old)","Botany","Microbiology","Zoology","Chemistry","App. Physics","App. Chemistry","Physics","Geology","Physiology","Food Science & Tech."])
destinationCombo.place(relx=0.34, rely=0.85, width=200, anchor=tkinter.S)

# Calculate Button 

coordinates = [(24.945472892212237, 67.11545122245124),(24.94038570395036, 67.11592157114106),
(24.938238049081818, 67.11120542558783),(24.940834371740422, 67.11753064285325),
(24.941586094981886, 67.11931111815348),(24.939789123286474, 67.11849103036658),
(24.940427444416777, 67.11943924188786),(24.94179062091621, 67.12090707546359),
(24.94286332774135, 67.1204828906196),(24.942807692922084, 67.1215588372739),
(24.94178435397302, 67.12191664600729),(24.941287198744874, 67.12210166935482),
(24.94374498463301, 67.1212964138957),(24.94747550158631, 67.12011977736228)]

matrix = [ [0, 7.5, 0, 6.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [7.5, 0, 5.5, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 5.5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [6.5, 2, 0, 0, 1.8, 3, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 1.8, 0, 0, 0.7, 1.8, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 3, 0, 0, 1.2, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0.7, 1.2, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 1.8, 0, 0, 0, 1, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0.7, 0, 0, 1.2, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0.7, 0, 2.3, 0, 1.4, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 2.3, 0, 0.2, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.2, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 1.2, 1.4, 0, 0, 0, 4.5],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4.5, 0] ] # fill graph values here manually 

vertices = 14
check = False
selected = []
previous = [] 
distances = []
path = []

# for x in range(vertices):
#     selected[x] = False
#     distances[x] = math.inf
#     previous[x] = -1

coordinateName = {
    "UBIT": 0,
    "IBA": 1,
    "KUBS": 2,
    "Pharmacy (old)": 3,
    "Botany": 4,
    "Microbiology": 5,
    "Zoology": 6,
    "Chemistry": 7,
    "App. Physics": 8,
    "App. Chemistry": 9,
    "Physics": 10,
    "Geology":11,
    "Physiology":12,
    "Food Science & Tech.": 13
}

def find_minVertex():
    minVertex = -1
    for x in range(vertices):
        if  (not selected[x]) and (minVertex == -1 or distances[x] < distances[minVertex]):
            minVertex = x
    return minVertex

def pathFunction(j):
    if j == -1:
        return
    pathFunction(previous[j])
    print(j) 
    path.append(j)

def dijkstra(source):
    global selected
    global previous
    global distances

    selected = [False] * vertices
    previous = [-1] * vertices
    distances = [math.inf] * vertices

    distances[source] = 0

    for x in range(vertices):
        if matrix[source][x] != 0:
            distances[x] = matrix[source][x] # direct neighbours updated with their weights instead of infinity
    
    for x in range(vertices):
        minVertex = find_minVertex()
        # print("min: " + str(minVertex))
        selected[minVertex] = True

        for y in range(vertices):
            if (matrix[minVertex][y] != 0) and (not selected[y]):
                dist = distances[minVertex] + matrix[minVertex][y]
                if dist < distances[y]:
                    distances[y] = dist
                    # print("distance: " + str(dist))
                    previous[y] = minVertex
                    # print("y: " + str(y))
                    
        # print("Des: " + str(coordinateName[destinationCombo_var.get()]))
        # print("Temp: " + str(temp))
        # print()

    # only run pathFunction for the position at which destination is stored which is accessed through destinationCombo_var.get()

    pathFunction(previous[coordinateName[destinationCombo_var.get()]])

sourceMarker = 0
destinationMarker = 0
path_1 = 0

def calculate():
    map_widget.set_zoom(-19)
    map_widget.set_zoom(15)
    map_widget.set_position(24.940508358616473, 67.11723194010298)

    global check
    if check == False:
        global sourceMarker
        global destinationMarker
        global path_1

        check = True
        if sourceCombo_var.get() == destinationCombo_var.get():
            check = False
            x = tkinter.messagebox.showwarning(title='Wrong Selection', message='Source and Destination are the same')
            return
        s = coordinateName[sourceCombo_var.get()]
        sourceMarker = map_widget.set_marker(coordinates[s][0], coordinates[s][1], text=sourceCombo_var.get())
        d = coordinateName[destinationCombo_var.get()]
        destinationMarker = map_widget.set_marker(coordinates[d][0], coordinates[d][1], text=destinationCombo_var.get())
        
        dijkstra(s)
        path.append(d)
        path.insert(0,s)
        finalCoordinates = []
        for x in range(len(path)):
            finalCoordinates.append(coordinates[path[x]])
            # print(finalCoordinates[x]) 
            # print(" ")
            # print(path[x])
        path_1 = map_widget.set_path(finalCoordinates)
    else:
        tkinter.messagebox.showwarning(title='Reset Required', message='Please reset before calculating again')

calculateButton = customtkinter.CTkButton(master=tabview.tab("Home"), width=120, height=32, border_width=0, corner_radius=8, text="Calculate", command=calculate)
calculateButton.place(relx=0.7, rely=0.93, anchor=tkinter.CENTER)

# reset button
def res():
    #map_widget.set_position(24.940508358616473, 67.11723194010298)
    map_widget.set_zoom(-19)
    map_widget.set_zoom(15)
    map_widget.set_position(24.940508358616473, 67.11723194010298)
    
    global sourceMarker
    global destinationMarker
    global path_1
    global distances
    global previous
    global selected
    global check

    check = False
    sourceMarker.delete()
    destinationMarker.delete()
    path_1.delete()
    path.clear()
    previous.clear()
    distances.clear()
    selected.clear()

resetButton = customtkinter.CTkButton(master=tabview.tab("Home"), width=120, height=32, border_width=0, corner_radius=8, text="Reset", command=res)
resetButton.place(relx=0.27, rely=0.93, anchor=tkinter.CENTER)

window.mainloop()