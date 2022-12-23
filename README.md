# University of Karachi - Travel Guide

A graphical user interface navigation application built for navigating between departments in University of Karachi. The backend works on single source shortest path greedy algorithm - Dijkstra Algorithm. The front end is built on a custom version of Tkinter by Tom Schimansky. Visit https://github.com/TomSchimansky/CustomTkinter for more details on Custom Tkinter. The entire thing is coded in Python. To run the project, download and run the 'proj.py' file. 

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

![Graph](https://github.com/MuhammadHabibKhan/uok-travel-guide/Graph.png)

