# Kourosh Arfania, arfania@usc.edu
# ITP 116 11-11:50am, Spring 2022
# Final Project
# Description:
# A meal information and inspiration program
# that utilizes API calls, math libraries,
# dictionaries, lists, and arithmetic to
# give the user information about their foods,
# generate meal ideas, and allow users to download.
# download recipes in of any saved food into a .txt file.

import json
import requests
import random

breakfast = {}
lunch = {}
dinner = {}
snack = {}


# --- Ensures JSON Calls are correct --- #
def jsonErrors(code):
    if code != 200:
        print("I'm sorry, that is not a valid meal option.")
        # returns true because value is held in variable "fail"
        return True


def callMoreInfo(mealId):
    fail = True
    while fail:
        url = "https://www.themealdb.com/api/json/v1/1/lookup.php?i=" + str(mealId)
        response = requests.get(url)
        status = response.status_code
        fail = jsonErrors(status)
        if not fail:  # will continue using the API call and also break the loop
            responseJson = response.json()
            mealAPI = responseJson["meals"]
            if mealAPI == None:  # the api can return 200 but still have no meal
                print("I'm sorry, that is not a valid meal option.")
                fail = True
            else:
                return mealAPI[0]


# --- Specific Meal API Call -- #
def callName(timeOfDay):
    meal_time = timeOfDay.lower()
    fail = True
    added = False
    while fail:

        # --- Calling the API with the appropriate URL and user-input --- #
        meal = input("What meal would you like to eat for " + meal_time + "? ")
        url = "https://www.themealdb.com/api/json/v1/1/search.php?s=" + str(meal)
        response = requests.get(url)
        status = response.status_code
        fail = jsonErrors(status)
        if not fail: # will continue using the API call and also break the loop

            # --- Scraping the meal from the dataset ---#
            responseJson = response.json()
            mealAPI = responseJson["meals"]
            if mealAPI == None: # the api can return 200 but still have no meal
                print("I'm sorry, that is not a valid meal option.")
                fail = True
            else:
                # the API returns a list of dictionaries, each dictionary being a meal:
                # the program will loop through all options and allow the user to choose which item they want
                print("The following meals can be added as a " + meal_time + " item:")

                meal_options = []
                for i in range(0, len(mealAPI)):
                    print("\t" + str(i+1) + ". " + mealAPI[i]["strMeal"])
                    meal_options.append(mealAPI[i]["strMeal"].lower())

                # --- Ensures a valid meal was chosen by the user (case-insensitive) --- #
                while not added:
                    meal_choice = input("Please enter which " + meal + " you would like to add: ").lower()
                    if not meal_choice in meal_options:
                        print("Sorry, that is not a valid option.")
                    else:
                        added = True
                        i = meal_options.index(meal_choice)
                        mealName = mealAPI[i]["strMeal"] # value
                        mealID = mealAPI[i]["idMeal"] # key

                        # --- Adding the meal pulled from the API into the appropriate dictionary --- #
                        if meal_time == "breakfast":
                            breakfast[mealID] = mealName # add to breakfast dictionary
                            print("Yum! " + mealName + " has been added as a breakfast meal.")
                        elif meal_time == "lunch":
                            lunch[mealID] = mealName # add to lunch dictionary
                            print("Yum! " + mealName + " has been added as a lunch meal.")
                        elif meal_time == "dinner":
                            dinner[mealID] = mealName # add to dinner dictionary
                            print("Yum! " + mealName + " has been added as a dinner meal.")
                        else: # can assume it is a snack
                            snack[mealID] = mealName # add to snack dictionary
                            print("Yum! " + mealName + " has been added as a snack.")

# --- First Letter of Meal API Call --- #
def callLetter(timeOfDay):
    meal_time = timeOfDay.lower()
    fail = True
    added = False
    while fail:

        # --- Calling the API with the appropriate URL and user-input --- #
        letter = input("What letter would you like to use to search for a " + meal_time + " meal? ")
        url = "https://www.themealdb.com/api/json/v1/1/search.php?f=" + str(letter)
        response = requests.get(url)
        status = response.status_code
        fail = jsonErrors(status)
        if not fail:  # will continue using the API call and also break the loop

            # --- Scraping the meal from the dataset ---#
            responseJson = response.json()
            mealAPI = responseJson["meals"]
            if mealAPI == None: # the api can return 200 but still have no meal
                print("I'm sorry, that is not a valid meal option.")
                fail = True
            else:
                # the API returns a list of dictionaries, each dictionary being a meal:
                # the program will loop through all options and allow the user to choose which item they want
                print("The following meals start with the letter " + letter + ":")
                meal_options = []
                for i in range(0, len(mealAPI)):
                    print("\t" + str(i + 1) + ". " + mealAPI[i]["strMeal"])
                    meal_options.append(mealAPI[i]["strMeal"].lower())

                # --- Ensures a valid meal was chosen by the user (case-insensitive) --- #
                while not added:
                    meal_choice = input("Please enter which meal you would like to add: ").lower()
                    if not meal_choice in meal_options:
                        print("Sorry, that is not a valid option.")
                    else:
                        added = True
                        i = meal_options.index(meal_choice)
                        mealName = mealAPI[i]["strMeal"]  # value
                        mealID = mealAPI[i]["idMeal"]  # key

                        # --- Adding the meal pulled from the API into the appropriate dictionary --- #
                        if meal_time == "breakfast":
                            breakfast[mealID] = mealName  # add to breakfast dictionary
                            print("Yum! " + mealName + " has been added as a breakfast meal.")
                        elif meal_time == "lunch":
                            lunch[mealID] = mealName  # add to lunch dictionary
                            print("Yum! " + mealName + " has been added as a lunch meal.")
                        elif meal_time == "dinner":
                            dinner[mealID] = mealName  # add to dinner dictionary
                            print("Yum! " + mealName + " has been added as a dinner meal.")
                        else:  # can assume it is a snack
                            snack[mealID] = mealName  # add to snack dictionary
                            print("Yum! " + mealName + " has been added as a snack.")

# --- Randomly Chosen Meal API Call --- #
def callRandom(timeOfDay):
    meal_time = timeOfDay.lower()
    fail = True
    while fail:

        # --- Calling the API with the appropriate URL (no user input because it is random) --- #
        url = "https://www.themealdb.com/api/json/v1/1/random.php"
        response = requests.get(url)
        status = response.status_code
        fail = jsonErrors(status)
        if not fail:  # will continue using the API call and also break the loop

            # --- Scraping the meal from the dataset --- #
            responseJson = response.json()
            mealAPI = responseJson["meals"][0] # only one food item called, so index 0 of list
            if mealAPI == None: # the api can return 200 but still have no meal
                print("I'm sorry, that is not a valid meal option.")
                fail = True
            else:
                # the API returns a list of dictionaries, each dictionary being a meal:
                # mealAPI uses index 0 since only one meal will be returned from the API
                mealName = mealAPI["strMeal"]  # value
                mealID = mealAPI["idMeal"]  # key, which will be used to get more information on the food later in the code
                # --- Adding the meal pulled from the API into the appropriate dictionary --- #
                if meal_time.lower() == "breakfast":
                    breakfast[mealID] = mealName  # add to breakfast dictionary
                    print("Yum! " + mealName + " has been added as a breakfast meal.")
                elif meal_time.lower() == "lunch":
                    lunch[mealID] = mealName  # add to lunch dictionary
                    print("Yum! " + mealName + " has been added as a lunch meal.")
                elif meal_time.lower() == "dinner":
                    dinner[mealID] = mealName  # add to dinner dictionary
                    print("Yum! " + mealName + " has been added as a dinner meal.")
                else:  # can assume it is a snack
                    snack[mealID] = mealName  # add to snack dictionary
                    print("Yum! " + mealName + " has been added as a snack.")

# --- Main Ingredient API Call --- #
def callMainIngredient(timeOfDay):
    meal_time = timeOfDay.lower()
    fail = True
    added = False
    while fail:

        # --- Calling the API with the appropriate URL and user-input --- #
        print("What ingredient would you like to use to search for foods for " + meal_time + "?")
        ingredient = input("(connect multiple words with underscore(s)) ").lower().replace(" ", "_")
        url = "https://www.themealdb.com/api/json/v1/1/filter.php?i=" + str(ingredient)
        response = requests.get(url)
        status = response.status_code
        fail = jsonErrors(status)
        if not fail:  # will continue using the API call and also break the loop

            # --- Scraping the meal from the dataset ---#
            responseJson = response.json()
            mealAPI = responseJson["meals"]
            if mealAPI == None: # the api can return 200 but still have no meal
                print("I'm sorry, that is not a valid meal option.")
                fail = True
            else:
                # the API returns a list of dictionaries, each dictionary being a meal:
                # the program will loop through all options and allow the user to choose which item they want
                print("The following meals can be added as a " + meal_time + " item:")
                mealAPI = responseJson["meals"]
                meal_options = []
                for i in range(0, len(mealAPI)):
                    print("\t" + str(i + 1) + ". " + mealAPI[i]["strMeal"])
                    meal_options.append(mealAPI[i]["strMeal"].lower())

                # --- Ensures a valid meal was chosen by the user (case-insensitive) --- #
                while not added:
                    meal_choice = input("Please enter which meal you would like to add: ").lower()
                    if not meal_choice in meal_options:
                        print("Sorry, that is not a valid option.")
                    else:
                        added = True
                        i = meal_options.index(meal_choice)
                        mealName = mealAPI[i]["strMeal"]  # value
                        mealID = mealAPI[i]["idMeal"]  # key

                        # --- Adding the meal pulled from the API into the appropriate dictionary --- #
                        if meal_time == "breakfast":
                            breakfast[mealID] = mealName  # add to breakfast dictionary
                            print("Yum! " + mealName + " has been added as a breakfast meal.")
                        elif meal_time == "lunch":
                            lunch[mealID] = mealName  # add to lunch dictionary
                            print("Yum! " + mealName + " has been added as a lunch meal.")
                        elif meal_time == "dinner":
                            dinner[mealID] = mealName  # add to dinner dictionary
                            print("Yum! " + mealName + " has been added as a dinner meal.")
                        else:  # can assume it is a snack
                            snack[mealID] = mealName  # add to snack dictionary
                            print("Yum! " + mealName + " has been added as a snack.")


# --- Takes the return value from the API Menu and calls the appropriate API-calling function --- #
def chooseAPICall(num, timeOfDay):
    if num == "1":
        callName(timeOfDay)
    elif num == "2":
        callLetter(timeOfDay)
    elif num == "3":
        callRandom(timeOfDay)
    else:
        callMainIngredient(timeOfDay)

# --- All steps to print the API menu of the program --- #
# based on the users input, it will call the API with a different URL
# different calls are defined within each of the function calls
def printAPIMenu(timeOfDay):
    print()
    time = timeOfDay
    apiMenuNumber = "0"
    valid = False
    print("How would you like to add/find your food item?")
    while not valid:
        # --- User-Selection checks for the API menu of the program --- #
        # (kept as a string to check if it is alphanumeric and not crash when the user enters a string)
        while not (apiMenuNumber == "1" or apiMenuNumber == "2" or apiMenuNumber == "3" or apiMenuNumber == "4"):
            print("\t1. Search a specific meal by name.")
            print("\t2. List all meal options by first letter of your choice.")
            print("\t3. Lookup a single, random meal.")
            print("\t4. Filter meal options by main ingredient.")

            apiMenuNumber = input("Please enter an integer corresponding to the menu above: ")
            if not (apiMenuNumber == "1" or apiMenuNumber == "2" or apiMenuNumber == "3" or apiMenuNumber == "4"):
                if not apiMenuNumber.isdigit():
                    print("Only positive integers are allowed to be inputted.")
                else:
                    print("Sorry, " + apiMenuNumber + " is not an option.")
            else:
                print("--------")
                valid = True
                return apiMenuNumber

# --- Prints all of the options users can choose to do with their saved food --- #
# --- Saves the user input and returns it to main, which then calls the info choice function --- #
def printInfoMenu():
    print("--------")
    infoMenuNumber = 0
    print("What would you like to do with your inputs?")
    while not (infoMenuNumber == "1" or infoMenuNumber == "2"):
        print("\t1. Generate a day of yummy eats!")
        print("\t2. Download a recipe.")
        infoMenuNumber = input("Please enter an integer corresponding to the menu above: ")
        # if exit, return exit so the loop breaks in main and the program concludes
        if infoMenuNumber.lower() == "exit":
            choice = "exit"
            return choice
        elif not (infoMenuNumber == "1" or infoMenuNumber == "2"):
            # specific error thrown when the user enters a string
            if not infoMenuNumber.isdigit():
                print("Only positive integers are allowed to be inputted.")
            # basic error thrown when the user enters an incorrect number
            else:
                print("Sorry, " + infoMenuNumber + " is not an option.")

        # --- Correct input is given from the user, return to main so it can be used by the info choice function --- #
        else:
            if (infoMenuNumber == "1"):
                choice = infoMenuNumber
                return choice
            elif (infoMenuNumber == "2"):
                choice = infoMenuNumber
                return choice

# --- Algorithm to generate a day of eats into the terminal --- #
# --- Addresses all possible combinations of breakfast, lunch, dinner, and snack --- #
def generateEats():

    # variables to differentiate combinations of B, L, D, and S
    count = 0 # how many meal times have a food item in it
    eatBreakfast = False
    eatLunch = False
    eatDinner = False
    eatSnack = False

    # if there is an element in the breakfast dictionary, turn on the flag and add 1 to count
    # select a random value from the dictionary and save it under breakfast_meal variable
    if breakfast != None and len(breakfast) > 0:
        count += 1
        eatBreakfast = True
        breakfast_keys = list(breakfast)
        breakfast_random_key = random.choice(breakfast_keys)
        breakfast_meal = breakfast[breakfast_random_key]

    # if there is an element in the lunch dictionary, turn on the flag and add 1 to count
    # select a random value from the dictionary and save it under lunch_meal variable
    if lunch != None and len(lunch) > 0:
        print(str(len(lunch)))
        count += 1
        eatLunch = True
        lunch_keys = list(lunch)
        lunch_random_key = random.choice(lunch_keys)
        lunch_meal = lunch[lunch_random_key]

    # if there is an element in the dinner dictionary, turn on the flag and add 1 to count
    # select a random value from the dictionary and save it under dinner_meal variable
    if dinner != None and len(dinner) > 0:
        print(str(len(dinner)))
        count += 1
        eatDinner = True
        dinner_keys = list(dinner)
        dinner_random_key = random.choice(dinner_keys)
        dinner_meal = dinner[dinner_random_key]

    # if there is an element in the snack dictionary, turn on the flag and add 1 to count
    # select a random value from the dictionary and save it under snack_meal variable
    if snack != None and len(snack) > 0:
        print(str(len(snack)))
        count += 1
        eatSnack = True
        snack_keys = list(snack)
        snack_random_key = random.choice(snack_keys)
        snack_meal = snack[snack_random_key]


    # --- Addresses all possible combinations of breakfast, lunch, and dinner --- #
    # --- given the number of inputs each dictionary has -------------------------#

    # if the count is 1, only 1 food item from 1 dictionary can be called
    if count == 1:
        if eatBreakfast:
            print("Enjoy a hearty, filling serving of " + breakfast_meal.lower() + " today!")
        elif eatLunch:
            print("Enjoy a hearty, filling serving of " + lunch_meal.lower() + " today!")
        elif eatDinner:
            print("Enjoy a hearty, filling serving of " + dinner_meal.lower() + " today!")
        elif eatSnack:
            print("Enjoy a hearty, filling serving of " + snack_meal.lower() + " today!")

    # if the count is 2, there are the following possible combinations:
    # B-L, B-D, B-S, L-D, L-S, D-S
    elif count == 2:
        if eatBreakfast:
            # breakfast-lunch combo
            if eatLunch:
                print("Start your day with a delicious breakfast of " + breakfast_meal.lower() + "! And for")
                print("a filling lunch, try " + lunch_meal.lower() + ".")

            # breakfast-dinner combo
            elif eatDinner:
                print("Start your day with a delicious breakfast of " + breakfast_meal.lower() + "! And for")
                print("a filling dinner, try " + dinner_meal.lower() + ".")

            #breakfast-snack combo
            elif eatSnack:
                print("Start your day with a delicious breakfast of " + breakfast_meal.lower() + "! And for")
                print("a filling snack, try " + snack_meal.lower() + ".")
        elif eatLunch:
            # lunch-dinner combo
            if eatDinner:
                print("Get excited for lunch. You'll be having " + lunch_meal.lower() + " with some")
                print(dinner_meal.lower() + " for dinner!")

            # lunch-snack combo
            elif eatSnack:
                print("Get excited for lunch. You'll be having " + lunch_meal.lower() + " with some")
                print(snack_meal.lower() + " as a late-night snack!")
        # dinner-snack combo
        elif eatDinner:
            print("Jeez, you must be hungry! For dinner, be sure to have a LARGE portion of")
            print(dinner_meal.lower() + " and " + snack_meal.lower() + " as a snack.")

    # if the count is 3, there are the following possible combinations:
    # B-L-D, B-L-S, B-D-S, L-D-S
    elif count == 3:
        if eatBreakfast:
            if eatLunch:
                # breakfast-lunch-dinner combo
                if eatDinner:
                    print("Start your day with a delicious meal of " + breakfast_meal.lower() + "! For lunch, spice things")
                    print("up with your next meal – " + lunch_meal.lower() + ". And for dinner, " + dinner_meal.lower() + ".")

                # breakfast-lunch-snack combo
                elif eatSnack:
                    print("Start your day with a delicious meal of " + breakfast_meal.lower() + "! For lunch, spice things")
                    print("up with your next meal – " + lunch_meal.lower() + ". And as a snack, " + snack_meal.lower() + ".")

            # breakfast-dinner-snack combo
            elif eatDinner:
                print("Start your day with a delicious meal of " + breakfast_meal.lower() + "! Since you'll be pretty hungry")
                print("by the time dinner rolls around, have a sizeable portion of " + dinner_meal.lower() + ".")
                print("And munch on " + snack_meal.lower() + " as a snack!")
        # lunch-dinner-snack-combo
        elif eatLunch:
            print("Late start to your day? Have some " + lunch_meal.lower() + " to perk you right up! For dinner, enjoy")
            print(dinner_meal.lower() + " with a nice snack of " + snack_meal.lower() + " to ends things off.")

    # if the count is 4, one of each meal option must be included
    elif count == 4:
        print("Start your day with a delicious meal of " + breakfast_meal.lower() + "! For lunch, spice things")
        print("up with your next meal – " + lunch_meal.lower() + ". For dinner, try " + dinner_meal.lower() + ".")
        print("And ends things off with " + snack_meal.lower() + " as a yummy snack!")


# --- Allows a user to choose a specific food they saved and download the ingredients + instructions --- #
def downloadRecipe():
    # variables to validate user inputs, store saved foods, and call the API
    valid = False # if the meal-time is breakfast, lunch, or dinner
    accessed = False # if the user chooses an appropriate meal within their meal-time
    meal_choices_name = [] # stores names of all foods within a meal-time
    meal_choices_key = [] # parallel array to store the keys of all foods within a meal-time
    chosen_meal_key = "" # used to call the API for specific meal's recipe information

    # --- Continues asking user for inputs until a valid one is received --- #
    while not valid:
        meal_time = input("For which meal-time would you like to find a recipe for? ")

        # --- Breakfast --- #
        if meal_time.lower() == "breakfast" and len(breakfast) > 0 and breakfast != None:
            valid = True
            print("The following breakfast meals have been saved:")
            # accessing the key and value from breakfast dictionary
            for key, value in breakfast.items():
                meal_choices_name.append(value.lower())
                meal_choices_key.append(key)
                # printing them in correct format
                print("\t- " + value)
            # keeps asking user to choose meal item
            while not accessed:
                meal = input("Please enter the name of the meal you would like to download the recipe for: ").lower()
                if meal not in meal_choices_name:
                    print("Sorry, that is not a saved breakfast option.")
                else:
                    accessed = True
                    chosen_meal_key = meal_choices_key[meal_choices_name.index(meal)]

        # --- Lunch --- #
        elif (meal_time.lower() == "lunch" and len(lunch) > 0 and lunch != None):
            valid = True
            print("The following lunch meals have been saved:")
            # accessing the key and value from lunch dictionary
            for key, value in lunch.items():
                meal_choices_name.append(value.lower())
                meal_choices_key.append(key)
                # printing them in correct format
                print("\t- " + value)
            # keep asking user to choose meal item
            while not accessed:
                meal = input("Please enter the name of the meal you would like to download the recipe for: ").lower()
                if meal not in meal_choices_name:
                    print("Sorry, that is not a saved lunch option.")
                else:
                    accessed = True
                    chosen_meal_key = meal_choices_key[meal_choices_name.index(meal)]

        # --- Dinner --- #
        elif meal_time.lower() == "dinner" and len(dinner) > 0 and dinner != None:
            valid = True
            print("The following dinner meals have been saved:")
            # accessing the key and value from dinner dictionary
            for key, value in dinner.items():
                meal_choices_name.append(value.lower())
                meal_choices_key.append(key)
                # printing them in correct format
                print("\t- " + value)
            # keep asking user to choose meal item
            while not accessed:
                meal = input("Please enter the name of the meal you would like to download the recipe for: ").lower()
                if meal not in meal_choices_name:
                    print("Sorry, that is not a saved dinner option.")
                else:
                    accessed = True
                    chosen_meal_key = meal_choices_key[meal_choices_name.index(meal)]

        # --- Snack --- #
        elif meal_time.lower() == "snack" and len(snack) > 0 and snack != None:
            valid = True
            print("The following snacks have been saved:")
            # accessing the key and value from snack dictionary
            for key, value in snack.items():
                meal_choices_name.append(value.lower())
                meal_choices_key.append(key)
                # printing them in correct format
                print("\t- " + value)
            # keep asking user to choose meal item
            while not accessed:
                meal = input("Please enter the name of the meal you would like to download the recipe for: ").lower()
                if meal not in meal_choices_name:
                    print("Sorry, that is not a saved snack option.")
                else:
                    accessed = True
                    chosen_meal_key = meal_choices_key[meal_choices_name.index(meal)]
        else:
            print("Sorry, " + meal_time + " is not a valid input. If you entered a valid meal-time, you")
            print("might not have saved any food to it!")

    # --- Initiating the read and write file-stream --- #
    # recipe file name in the format: meal_name_recipe.txt
    # create new file and enable writing capabilities
    filename = meal.lower().replace(" ", "_") + "_recipe.txt"
    out_file = open(filename, "w")

    # call more info function on key of selected meal, write recipe into file
    meal_info = callMoreInfo(chosen_meal_key)
    instructions = meal_info["strInstructions"]
    # matching ingredients with their measurements
    print("Required Ingredients:", file = out_file)
    if meal_info["strIngredient1"] != None and meal_info["strIngredient1"] != "":
        print("\t-- " + meal_info["strIngredient1"] + " (" + meal_info["strMeasure1"] + ")", file=out_file)
    for i in range(0,10):
        if meal_info["strIngredient1" + str(i)] != None and meal_info["strIngredient1" + str(i)] != "":
            print("\t-- " + meal_info["strIngredient1" + str(i)] + " (" + meal_info["strMeasure1" + str(i)] + ")", file=out_file)

    if meal_info["strIngredient2"] != None and meal_info["strIngredient2"] != "":
        print("\t-- " + meal_info["strIngredient2"] + " (" + meal_info["strMeasure2"] + ")", file=out_file)

    if meal_info["strIngredient20"] != None and meal_info["strIngredient20"] != "":
        print("\t-- " + meal_info["strIngredient20"] + " (" + meal_info["strMeasure20"] + ")", file=out_file)

    for i in range(3,10):
        if meal_info["strIngredient" + str(i)] != None and meal_info["strIngredient" + str(i)] != "":
            print("\t-- " + meal_info["strIngredient" + str(i)] + " (" + meal_info["strMeasure" + str(i)] + ")", file=out_file)

    # print a newline after all ingredients and measurements are written to the file
    print("",file=out_file)
    # print the instructions to the file
    print("Instructions to prepare " + meal + ":", file = out_file)
    print(instructions, file= out_file)
    # file is done being written to, so close it
    out_file.close()
    print("--------")
    print("Saved!")

def chooseInfoCall(choice):
    if choice == "1":
        generateEats()
    elif choice == "2":
        downloadRecipe()

# --- All steps to print the main menu of the program --- #
# user selection is used as a parameter in the API menu call
# contains the conditional to end the inputting of foods
def printMainMenu():
    time = ""
    mainMenuNumber = 0
    end = False
    print("--------")
    print("For what time of day would you like to find a food item for?")

    # --- User-Selection checks for the main menu of the program --- #
    # (kept as a string to check if it is alphanumeric and not crash when the user enters a string)
    while not (mainMenuNumber == "1" or mainMenuNumber == "2" or mainMenuNumber == "3" or mainMenuNumber == "4"):
        print("\t1. Breakfast")
        print("\t2. Lunch")
        print("\t3. Dinner")
        print("\t4. Snack")
        mainMenuNumber = input("Please enter an integer corresponding to the menu above: ")
        if mainMenuNumber == "end":
            time = "end"
            return time
        elif not (mainMenuNumber == "1" or mainMenuNumber == "2" or mainMenuNumber == "3" or mainMenuNumber == "4"):
            if not mainMenuNumber.isdigit():
                print("Only positive integers are allowed to be inputted.")
            else:
                print("Sorry, " + mainMenuNumber + " is not an option.")
        else:
            if (mainMenuNumber == "1"):
                time = "Breakfast"
                return time
            elif (mainMenuNumber == "2"):
                time = "Lunch"
                return time
            elif (mainMenuNumber == "3"):
                time = "Dinner"
                return time
            else:
                time = "Snack"
                return time

def startOutput():
    print("--------")
    print("Welcome to your personalized meal inspiration program, Food4U!")

def endOutput():
    print("--------")
    print("Thank you for using Food4U! Any recipes you chose to download")
    print("should now be saved as a .txt file in this directory. Eat up!")


# --- Main Function that calls all other function to run the program --- #
# --- NO PRINT STATEMENTS WITHIN MAIN --- #
def main():
    startOutput()

    end = False
    exit = False

    while not end:
        time = printMainMenu()
        if time.lower() == "end":
            end = True
            break
        else:
            apiChoice = printAPIMenu(time)
            chooseAPICall(apiChoice, time)

    while not exit:
        infoChoice = printInfoMenu()
        if infoChoice.lower() == "exit":
            exit = True
            break
        else:
            chooseInfoCall(infoChoice)

    endOutput()


# --- Calling Main to run --- #
main()
