import pandas as pd 
import sys
import matplotlib.pyplot as plt 


def loadData():
    global df
    df = pd.read_csv("smhi_temp.csv", skiprows=9, usecols=[0,1,2,3,4], sep=";")
    df.columns = ["Datum", "Tid", "Lufttemperatur", "Kvalitet", "Tidsutsnitt"]
    return df

def loadData2():
    global df
    df = pd.read_csv("smhi_ned.csv", skiprows=9, usecols=[0,1,2,3,4], sep=";")
    df.columns = ["Datum", "Tid", "Nederbördsmängd", "Kvalitet", "Tidsutsnitt"]
    return df

def menu():
    global choice1
    print("------Weather menu------")
    choice1 = input("What atributes you want to see?\n 1.What do you want to analyze\n 2. View the data frame\n Q: Quit\n Choice: ")
    choice1 = choice1.upper()
    if choice1 == "1":
        menu2()
    elif choice1 == "2":
        choice_1 = input("Which one?\n 1. Lufttemperatur\n 2. Nederbördsmängd\n Choice: ")
        if(choice_1 == "1"):
            df = pd.read_csv("smhi_temp.csv", skiprows=9, usecols=[0,1,2,3,4], sep=";")
            print(df)
        if(choice_1 == "2"):
            df = pd.read_csv("smhi_ned.csv", skiprows=9, usecols=[0,1,2,3,4], sep=";")
            print(df)
        menu()
    else:
        if choice1 == "Q" or choice1 == "q":
            sys.exit()
        else:
            print("Choose from the menu!") 
            menu()
def menu2():
    global attribut
    attribut = ""
    print("---Welcome to our second menu---")
    choice2 = input("1. Tempreatures\n 2. Nederbörd\n Q. Quit\n Choice: ")
    choice2 = choice2.upper()
    if choice2 == "1":
        attribut = "Lufttemperatur"
        dataFrame = loadData()
        analyze(dataFrame)
    elif choice2 == "2":
        attribut = "Nederbördsmängd"
        dataFrame = loadData2()
        analyze(dataFrame)
    else:
        if choice2 == "Q" or choice2 == "q":
            sys.exit()
        else:
            print("Choose from the menu!") 
            menu2()
    
def analyze(x):
    print("---Welcome to our analyze section---")
    choice3 = input("What do you want to do\n 1. View graph\n 2. View categories\nQ. Quit\n Choice: ")
    choice3 = choice3.upper()
    if choice3 == "1":
        viewGraph()
        menu2()
        analyze(0)
    elif choice3 == "2":
        print(df.iloc[0]) 
        analyze(0)
    elif choice3 == "Q" or choice3 == "q":
        sys.exit()
    else:
        print("You must only input 1 or 2, please try again.")

def viewGraph():
    x_value = df["Datum"] + " " + df["Tid"] 
    y_value = df[attribut]
    
    x_label = "X"
    y_label = "Y"
    plt.rcParams["font.size"] = 5.8
    
    fig, ax = plt.subplots()
    choice_title = input("Write your graph title: ")
    ax.set_title(choice_title)
    plt.xticks(rotation=90)
    
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.plot(x_value, y_value)
    
    start_limit_x = int(input("Write your start x limit: "))
    end_limit_x = int(input("Write your end x limit: "))
    ax.set_xlim(start_limit_x, end_limit_x)
    
    start_limit_y = int(input("Write your start y limit: "))
    end_limit_y = int(input("Write your end y limit: "))
    ax.set_ylim(start_limit_y, end_limit_y)
    
    ax.grid(True)
    plt.show()

menu()

