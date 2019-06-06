import json
import requests
import tkinter
from tkinter import *



def getData(collection):
    data = requests.get('https://uinames.com/api/').json()

    # print usable collection names
    print('Possible collections are: ')
    for key in data:
        print(key)

    # select wanted collection from data
    response = data[collection]
    saveData(response, collection)


def saveData(data, collection):
    try:
        with open('users.txt', 'a+') as file:
            # a+ = append + create file if doesn't exist
            file.write( collection + ': ' + data + "\n")
    except:
        print('Something went wrong while saving the data, try again')
    loadView(data)

def loadView(data):
    # create tkinter view
    root = Tk()
    nameVar = StringVar()
    label = Label( root, textvariable = nameVar, relief = RAISED )
    button = Button(root, text="New User", command=root.destroy)
    nameVar.set(data)
    label.pack()
    button.pack()
    root.mainloop()

# pass wanted collection name to the function
getData( collection = 'region')
