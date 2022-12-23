# University of Karachi - Travel Guide

A graphical user interface navigation application built for navigating between departments in University of Karachi. The backend works on single source shortest path greedy algorithm - Dijkstra Algorithm. The front end is built on a custom version of Tkinter by Tom Schimansky. Visit https://github.com/TomSchimansky/CustomTkinter for more details on Custom Tkinter. The entire thing is coded in Python. To run the project, download and run the 'proj.py' file. 

![Application](https://github.com/MuhammadHabibKhan/uok-travel-guide/blob/main/start.png)

Pre-Requisites:
- Python. Visit https://www.python.org/downloads/ to download Python
- Pip. To install pip, type the following commands in command prompt
```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```
- Tkinter. Type the following in the command prompt to install Tkinter.
```
pip install tkinter
```
- Custom Tkinter. Type the following in the command prompt to install Custom Tkinter.
```
pip install customtkinter
```

NOTE: Not all departments were mapped in this project. They can be easily added by improving upon the existing graph and creating new vertices and edges, assigning weights according to the scale, noting down the new departments' coordinates and making those changes in the adjacency matrix in the code. 

The image attached below is the graph constructed for the 14 selected departments in University of Karachi.  

![Graph](https://github.com/MuhammadHabibKhan/uok-travel-guide/blob/main/Graph.png)


Based on Dijkstra's Algorithm, a source department can be selected and the shortest path to the destination department is shown. The path traced is not through the proper roads that must be taken to reach the department but instead similar to how you would trace the shortest path in the graph attached above. Path tracing through roads can be added with some changes to the code and storing coordinates of each turn in the path and coordinates of road at the front of the department. An image attached below shows the working of the application.


![Graph](https://github.com/MuhammadHabibKhan/uok-travel-guide/blob/main/path.png)

As expected and clear from the graph, to reach the Department of Zoology from UBIT, a shorter path is available through the Department of Botany instead of going all the way through Depart. of Microbiology. 

The map widget of the custom tkinter provides the interactive map on the application with google's tile servers running at the background. Users may switch to google's satellite tile server using the 'Satellite View' button at the top right corner. 

The complete instructions to use the app are provided in the text box to the left of the start screen below the introductory welcome message. Details about the application are also provided in the 'About' Tab. 

## Possible Improvements:
- Dijkstra can be implemented using Adjacency List instead of Adjacency matrix to save computation and reduce time complexity since only the neighbors are required.
- The alogrithm can also be implemented using Priority Queues to reduce the time complexity even further.
- Path tracing can be improved as suggested above.
