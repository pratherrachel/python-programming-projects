# SmartFit Fitness Program for New Customers Eligibility

# Asks for the customer for their age to determine which program they are eligible for
New_Customer_Age = int(input("Hello there new customer, can you please enter your age? "))

# Checks which of three fitness programs the new customer can sign up
if New_Customer_Age < 18:
    print("Welcome! You can enroll in the Teen Fitness Program.")
elif New_Customer_Age <= 40:
    print("Welcome! You can enroll in the Regular Fitness Program.")
else:
    print("Welcome! You can enroll in the Senior Wellness Program.")

# Asks the customer to provide their medical history before continuing registration
New_Customer_Medical_History = str(input("For safety reasons, please disclose if you have any medical conditions: "))

# Forces the medicalHistory input from the customer to be capitalized
New_Customer_Medical_History = New_Customer_Medical_History.capitalize()

# Determines if the customer requires medical clearance
if New_Customer_Medical_History != "Yes" and New_Customer_Medical_History != "No":
    print("You provided an invalid input, please enter a 'yes' or 'no' response and try again.")
elif New_Customer_Age >= 40 and New_Customer_Medical_History == "Yes":
    print("Apologies, but for your safety medical clearance from your doctor is required before you can join.")

elif New_Customer_Age < 40 or New_Customer_Medical_History == "No":
    print("Thank you for verifying your medical conditions, you can proceed with the new customer registration.")

    #Prompts the customer to select their desired membership plan
    New_Customer_Plan_Option = str(input("Would you like a basic or premium plan? Please type basic or premium: "))

    # Repeats the force capitalization that we saw for medical history
    New_Customer_Plan_Option = New_Customer_Plan_Option.capitalize()

    if New_Customer_Plan_Option != "Basic" and New_Customer_Plan_Option != "Premium":
        print("You provided an invalid input, please enter basic or premium at this stage.")
    elif New_Customer_Plan_Option == "Basic":
        Personal_Trainer_Response = str(input("Would like to sign up for a personal trainer? Yes or No: "))

        # Repeats the force capitalization that we saw for medical history
        Personal_Trainer_Response = Personal_Trainer_Response.capitalize()
        if Personal_Trainer_Response == "Yes":
            print("The cost of a basic plan with a personal trainer is $45 per month.")

        elif Personal_Trainer_Response == "No":
            print("The cost of the basic plan without the personal trainer is $30 per month.")

            if New_Customer_Plan_Option == "Basic" and Personal_Trainer_Response == "No":
                print("Did you know, if you sign up for the premium plan you can get more benefits!")

    elif New_Customer_Plan_Option == "Premium":
        print("The premium plan you selected is $60 per month.")

        if New_Customer_Plan_Option == "Premium" and New_Customer_Age < 30 :
            print ("Congratulations! You qualify for a youth discount on the premium plan.")
        if New_Customer_Plan_Option == "Premium" and New_Customer_Medical_History == "Yes":
            print("Your plan selection comes with a free health consultation, please consider taking advantage of this "
              "before starting.")
