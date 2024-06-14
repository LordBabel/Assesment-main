'''
Brawl Stars database application by William Li Chen

'''
# imports
import sqlite3

# constants and variables
DATABASE = "assessment.db"


# functions, it just outputs the results from a specific SQL statements


def print_all_brawlers():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY ID"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_new():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers ORDER BY Year_Released desc"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_og():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Year_Released == 2017"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_high_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_low_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers ORDER BY HP;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_under10000_HP():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT Name, HP FROM Brawlers WHERE HP < 10000 ORDER BY HP desc;"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("Brawler        HP")
    for brawler in result:
        print(f"{brawler[0]:<15}{brawler[1]:<5}")
    db.close()


def print_no_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'No'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_kit():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Name == 'Kit'"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_epic_wallbreak():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Wallbreak == 'Yes' AND Rarity_ID = 4"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_legendary_assassin():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Rarity_ID == 6 AND Class_ID = 2"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def print_damagedealer():
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = "SELECT * FROM Brawlers WHERE Class_ID == 4"
    conn.execute(sql)
    result = conn.fetchall()    # loop through results, print it nicely
    print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
    for brawler in result:
        print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
    db.close()


def brawl_stardle():
    # important variables, these checkers help look for valid inputs and loops
    checker2 = 0
    checker = 0
    wallbreak = ""
    hp = 0
    hplow = 0
    year = 0
    yearlow = 0
    rarity = 0
    # SQL statements that will be used to find data at the end
    statementwallbreak = " AND Wallbreak != 0"
    statementhp = " AND HP != 0"
    statementyear = " AND Year_Released != 0"
    statementrarity = " AND Rarity_ID != 0"
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    print("This is a tool to help search for brawlers using data. This can be used as both a search function, and as a brawl stardle helper.")
    print("All you need to do is select an option and follow the instructions.") 
    print("At the end of every piece of inputted data, it will print the results of every brawler that matches the data.")
    print("Then it will ask if you want to continue or not. Selecting No stops the function, while selecting Yes continues it.")
    print("Goodluck!")
    print('''
    1. Wallbreak
    2. HP
    3. Year Released
    4. Rarity
    5. Reset collected data
          ''')
    while checker == 0:  # loop until valid answer
        inputs = input("Please select an option, 1 for Wallbreak, 2 for HP, 3 for Year Released, 4 for Rarity and 5 to reset the collected data. ")
        # checking what option was selected
        # running different code based on each option, that stores user inputed data
        if inputs == "1":
            checker = 1
            print('''
                  1. Wallbreak
                  2. No Wallbreak
                  ''')
            inputwall = input("Please enter an option: ")
            if inputwall == "1":
                wallbreak = '"Yes"'
            elif inputwall == "2":
                wallbreak = '"No"'
            else:
                print("Please enter a valid option.")
                checker = 0
        elif inputs == "2":
            checker = 1
            print('''
                  1. Above
                  2. Below
                  3. Equal
                  ''')
            inputHP = input("Please enter an option, if the HP was Above, Below, or Equal to your guess: ")
            if inputHP == "1":
                hplow = 1
                checker2 = 1
            elif inputHP == "2":
                hplow = 2
                checker2 = 1
            elif inputHP == "3":
                hplow = 3
                checker2 = 1
            else:
                print("Please pick a valid option next time.")
            if checker2 != 0:
                inputHPValue = input("Please enter the HP value: ")
                try:
                    inputHPValueINT = int(inputHPValue)
                    hp = inputHPValueINT
                except:
                    print("Please enter a valid number next time.")
                
        elif inputs == "3":
            checker = 1
            print('''
                  1. Above
                  2. Below
                  3. Equal
                  ''')
            inputYear = input("Please enter an option, if the Year was Above, Below, or Equal to your guess: ")
            if inputYear == "1":
                yearlow = 1
            if inputYear == "2":
                yearlow = 2
            if inputYear == "3":
                yearlow = 3
            print('''
                  1. 2017
                  2. 2018
                  3. 2019
                  4. 2020
                  5. 2021
                  6. 2022
                  7. 2023
                  8. 2024
                  ''')
            inputYearValue = input("Please enter one of those years: ")
            if inputYearValue == "1":
                year = 2017
            elif inputYearValue == "2":
                year = 2018
            elif inputYearValue == "3":
                year = 2019
            elif inputYearValue == "4":
                year = 2020
            elif inputYearValue == "5":
                year = 2021
            elif inputYearValue == "6":
                year = 2022
            elif inputYearValue == "7":
                year = 2023
            elif inputYearValue == "8":
                year = 2024
            else:
                print("Please pick a valid option next time.")
            
        elif inputs == "4":
            checker = 1
            print('''
                  1. Common
                  2. Rare
                  3. Super Rare
                  4. Epic
                  5. Mythic
                  6. Legendary
                  7. Starter
                  ''')
            inputrarity = input("Please pick an option: ")
            try:
                inputrarityINT = int(inputrarity)
                rarity = inputrarityINT
            except:
                print("Please pick a valid option next time.")
        elif inputs == "5":
            wallbreak = ""
            hp = 0
            hplow = 0
            year = 0
            yearlow = 0
            rarity = 0
        else:
            print(" Invalid Input.")
        if wallbreak != "":
            statementwallbreak = " AND Wallbreak == "+wallbreak
        if hp != 0:
            if hplow == 1:
                statementhp = " AND HP > "+str(hp)
            if hplow == 2:
                statementhp = " AND HP < "+str(hp)
            if hplow == 3: 
                statementhp = " AND HP == "+str(hp)
        if year != 0:
            if yearlow == 1:
                statementyear = " AND Year_Released > "+str(year)
            if yearlow == 2:
                statementyear = " AND Year_Released < "+str(year)
            if yearlow == 3: 
                statementyear = " AND Year_Released == "+str(year)
        if rarity != 0:
            statementrarity = " AND Rarity_ID == "+str(rarity)
        db = sqlite3.connect(DATABASE)
        conn = db.cursor()
        sql = "SELECT * FROM Brawlers WHERE ID != 0"+str(statementwallbreak)+str(statementhp)+str(statementyear)+str(statementrarity)
        conn.execute(sql)
        result = conn.fetchall()    # loop through results, print it nicely
        print("ID   Wallbreak   Name           HP      Rarity ID   Year Released   Class ID")
        for brawler in result:
            print(f"{brawler[0]:<5}{brawler[1]:<12}{brawler[2]:<15}{brawler[3]:<8}{brawler[4]:<12}{brawler[5]:<16}{brawler[6]:<5}")
        db.close()
        print("")
        extrainfo = input("Do you have more info from another guess to input? Choosing No means restarting a game of Brawl Stardle. 1 for Yes, 2 for No: ")
        if extrainfo == "1":
            checker = 0
        elif extrainfo == "2":
            checker = 1
        else:
            print("Please enter a valid option next time.")


def custom_sql():
    user = input("Please enter a Username: ")  # username and password system
    if user == "Babel":
        password = input("Please enter your Password: ")
        if password == "password123":
            pass
            print("Here are the columns in the table Brawlers:")
            print("ID  Wallbreak  Name  HP  Rarity_ID  Year_Released  Class_ID")
            print("ID is an Int, 1-80. Name is a string. HP is an Int. Rarity_ID is an Int, table below. Year_Released is an Int, 2017-2024. Class_ID is an Int, table below.")
            print("")
            print('''
                  Rarity table:
                  1	Common
                  2	Rare
                  3	Super Rare
                  4	Epic
                  5	Mythic
                  6	Legendary
                  7	Starting Brawler
                         ''')
            print("")
            print('''
                  Class table:
                  1	Artillery
                  2	Assassin
                  3	Controller
                  4	Damage Dealer
                  5	Marksman
                  6	Support
                  7	Tank
                         ''')
            print("Please enter a SQL statement: ")
            db = sqlite3.connect(DATABASE)
            try:  # try to do a custom sql statement
                conn = db.cursor()
                sql = input("")
                conn.execute(sql)
                db.commit()
                result = conn.fetchall()   
                for brawler in result:
                    print(brawler)
                db.close()
            except:
                print("Please retry with a valid SQL statement.")  # except to catch errors




        else:
            print("Please enter a valid Password next time.")
    else:
        print("Please enter a valid Username next time.")


def add_data():
    Id = IDd
    name = input("Please enter a name for the new brawler: ") 
    wallbreak = input("Please enter Yes or No for wallbreak: ")
    hp = input("Please enter an Int for hp: ")
    year = input("Please enter a year released: ")
    rarityid = input('''
                  Based on this table:
                  1. Common
                  2. Rare
                  3. Super Rare
                  4. Epic
                  5. Mythic
                  6. Legendary
                  7. Starter
                  Please enter a number that corrosponds to a rarity: ''')
    classid = input('''
                  Based on this table:
                  1. Artillery
                  2. Assassin
                  3. Controller
                  4. Damage Dealer
                  5. Marksman
                  6. Support
                  7. Tank
                  Please enter a number that corrosponds to a class: ''')
    try:
        db = sqlite3.connect(DATABASE)
        conn = db.cursor()
        sql = "INSERT INTO Brawlers (ID, Wallbreak, Name, HP, Rarity_ID, Year_Released, Class_ID) VALUES ("+str(Id)+", "+'"'+wallbreak+'"'+", "+name+", "+hp+", "+rarityid+", "+year+", "+classid +")"
        conn.execute(sql)
        db.commit()
        print("All done!")
        db.close()
    except:
        print("Please check your inputs and try again. Make sure hp and year are both intergers, wall break is Yes or No, and rarity and class details are correct.")


def remove_data():
    try:
        inputremove = input("Please type the Name of the brawler you want to delete. Use correct spelling and punctuation. ")
        db = sqlite3.connect(DATABASE)
        conn = db.cursor()
        sql = "DELETE FROM Brawlers WHERE Name = "+'"'+inputremove+'"'
        conn.execute(sql)
        db.commit()
        print("All done!")
        db.close()
    except:
        print("Please enter a valid input next time.")

   
def modify_data():
    try:
        inputmodifybrawler = input("Please enter a brawler to alter their infomation. Use correct spelling and punctuation. ")
        sqlmodify = "SELECT * FROM Brawlers"
        print('''
            1. Wallbreak
            2. HP
            3. Rarity_ID
            4. Class_ID
            ''')
        inputmodify = input("Which of these columns would you like to change? ")
        if inputmodify == "1":
            print('''
                  1. Yes
                  2. No
                  ''')
            inputmodifywallbreak = input("Please pick an option to change Wallbreak to. ")
            if inputmodifywallbreak == "1":
                sqlmodify = '''UPDATE Brawlers SET Wallbreak="Yes" WHERE Name='''+'"'+inputmodifybrawler+'"'
            elif inputmodifywallbreak == "2":
                sqlmodify = 'UPDATE Brawlers SET Wallbreak="No" WHERE Name='+'"'+inputmodifybrawler+'"'
            else: 
                print("Please enter a valid option next time.")
        elif inputmodify == "2":
            inputmodifyhp = input("Please type an HP value to change HP to. ")
            try:
                 
                intinputmodifyhp = int(inputmodifyhp)
                sqlmodify = "UPDATE Brawlers SET HP = "+intinputmodifyhp+" WHERE Name = "+'"'+inputmodifybrawler+'"'  
            except:
                print("Please enter a valid value next time.")
        elif inputmodify == "3":
            print('''
                  1. Common
                  2. Rare
                  3. Super Rare
                  4. Epic
                  5. Mythic
                  6. Legendary
                  7. Starter
                  ''')
            inputmodifyrarity = input("Please pick an option to change rarity to. ")
            if inputmodifyrarity == "1":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 1 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "2":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 2 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "3":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 3 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "4":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 4 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "5":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 5 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "6":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 6 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyrarity == "7":
                sqlmodify = "UPDATE Brawlers SET Rarity_ID = 7 WHERE Name == "+'"'+inputmodifybrawler+'"'
            else:
                print("Please enter a valid option next time.")
        elif inputmodify == "4":
            print('''
                  1. Artillery
                  2. Assassin
                  3. Controller
                  4. Damage Dealer
                  5. Marksman
                  6. Support
                  7. Tank
                  ''')
            inputmodifyclass = input("Please pick an option to change class to. ")
            if inputmodifyclass == "1":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 1 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "2":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 2 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "3":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 3 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "4":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 4 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "5":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 5 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "6":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 6 WHERE Name == "+'"'+inputmodifybrawler+'"'
            elif inputmodifyclass == "7":
                sqlmodify = "UPDATE Brawlers SET Class_ID = 7 WHERE Name == "+'"'+inputmodifybrawler+'"'
            else:
                print("Please enter a valid option next time.")
        else:
            print("Please enter a valid option next time.")        
    except:
        print("Please enter a valid brawler next time.")
    db = sqlite3.connect(DATABASE)
    conn = db.cursor()
    sql = sqlmodify
    conn.execute(sql)
    db.commit()
    db.close()

breaker = 0
IDd = 81
while breaker != 1:
    # variables
    checker = 0
    # main
    print("What would you like to do with this Brawl Stars Database?")
    # menu
    print("Please input an option.")
    print('''
    1. Search through data
    2. Modify, Remove or Add data
    3. Brawl Stardle helper
    4. Custom SQL query
    5. Exit
    ''')
    while checker == 0:  # loop until valid answer
        inputs = input("Please type one of the numbers above. ")
        # checking what option was selected
        if inputs == "1":
            checker = 1
            print("Here are some predetermined search functions. For more functionality please choose Brawl Stardle helper or custom search.")
            print('''
                  1. Find the highest hp brawlers
                  2. Find all the brawlers who can wallbreak
                  3. Find the newest brawlers
                  4. Find all the brawlers from 2017
                  5. Find the lowest HP brawlers
                  6. Find all brawlers who cannot wallbreak
                  7. Find brawlers with under 10000 HP
                  8. Find out more about my favourite Brawler!
                  9. Find all epic wallbreakers
                  10. Find all legendary assassins
                  11. Find all damage dealers
                  12. Print all brawlers
                  ''')
            inputsearch = input("Please select a number from above. ")
            if inputsearch == "1":
                print_high_HP()
            elif inputsearch == "2":
                print_wallbreak()
            elif inputsearch == "3":
                print_new()
            elif inputsearch == "4":
                print_og()
            elif inputsearch == "5":
                print_low_HP()
            elif inputsearch == "6":
                print_no_wallbreak()
            elif inputsearch == "7":
                print_under10000_HP()
            elif inputsearch == "8":
                print_kit()
            elif inputsearch == "9":
                print_epic_wallbreak()
            elif inputsearch == "10":
                print_legendary_assassin()
            elif inputsearch == "11":
                print_damagedealer()
            elif inputsearch == "12":
                print_all_brawlers()
            else:
                print("Please enter a valid input next time.")
        elif inputs == "2":
            checker = 1
            Arm = input('''
                  Choose an option.
                  1. Add data
                  2. Remove data
                  3. Modify data
                  ''')
            if Arm == "1":
                add_data()
                IDd += 1
            elif Arm == "2":
                remove_data()
            elif Arm == "3":
                modify_data()
            else:
                print("Please enter a valid option next time.")
        elif inputs == "3":
            checker = 1
            brawl_stardle()
        elif inputs == "4":
            checker = 1
            custom_sql()
        elif inputs == "5":
            breaker = 1
            break
        else:
            print("Invalid Input.")
