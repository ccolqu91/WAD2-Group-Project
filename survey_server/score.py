def CalculateScore(Survey):

    # These variables set the maximum score for each sub-catagory
    max_food_quality_score = 0
    max_customer_service_score = 0
    max_hygiene_score  = 0
    max_value_for_money_score = 0
    max_menu_variety_score = 0

    # These variables track the points each sub-catagory have earned
    food_quality_score = 0
    customer_service_score = 0
    hygiene_score  = 0
    value_for_money_score = 0
    menu_variety_score = 0

    # These if statements check that the survey questions has been answered. if it has been answered the appropiate 
    # points will be added to the max score for the appropiate sub-catagory 
    if Survey.time_starter != "":
        max_customer_service_score += 1

    if Survey.size_starter != "":
        max_value_for_money_score += 2

    if Survey.presentation_starter != "":
        max_food_quality_score += 4

    if Survey.variety_starter != "":
        max_menu_variety_score += 2
    
    if Survey.time_maincourse != "":
        max_customer_service_score += 2

    if Survey.size_maincourse != "":
        max_value_for_money_score += 4

    if Survey.presentation_maincourse != "":
        max_food_quality_score += 8

    if Survey.variety_maincourse != "":
        max_menu_variety_score += 4

    if Survey.time_dessert != "":
        max_customer_service_score += 1

    if Survey.size_dessert != "":
        max_value_for_money_score += 2

    if Survey.presentation_dessert != "":
        max_food_quality_score += 4

    if Survey.variety_dessert != "":
        max_menu_variety_score += 2

    if Survey.time_drink != "":
        max_customer_service_score += 1

    if Survey.size_drink != "":
        max_value_for_money_score += 2

    if Survey.presentation_drink != "":
        max_food_quality_score += 4

    if Survey.variety_drink != "":
        max_menu_variety_score += 2
    
    if Survey.greeting_entry != "":
        max_customer_service_score += 2

    if Survey.greeting_waiting != "":
        max_customer_service_score += 2

    if Survey.greeting_clean != "":
        max_customer_service_score += 2
        max_hygiene_score += 2
    
    if Survey.greeting_order != "":
        max_customer_service_score += 1

    if Survey.restroom_clean != "":
        max_hygiene_score += 4

    if Survey.missing_restroom != "":
        max_hygiene_score += 2
        max_customer_service_score += 1

    if Survey.clean_restaurant != "":
        max_hygiene_score += 2
        max_customer_service_score += 1

    if Survey.pay_bill_restaurant != "":
        max_customer_service_score += 1

    if Survey.service_staff != "":
        max_customer_service_score += 5

    # These if statements will look at the answer and award the correct amount of points

    #Q1
    if Survey.time_starter == "fast":
        customer_service_score += 1
    elif Survey.time_starter == "slow":
        customer_service_score -= 1
    
    #Q3
    if Survey.size_starter == "yes":
        value_for_money_score += 2
    elif Survey.size_starter == "no":
        value_for_money_score -= 2

    #Q4
    if Survey.presentation_starter == "Excellent":
        food_quality_score += 4
    elif Survey.presentation_starter == "Great":
        food_quality_score += 2
    elif Survey.presentation_starter == "Somewhat":
        food_quality_score += 1
    elif Survey.presentation_starter == "No":
        food_quality_score -= 4

    #Q5
    if Survey.variety_starter == "Excellent":
        menu_variety_score += 2
    elif Survey.variety_starter == "Great":
        menu_variety_score += 1
    elif Survey.variety_starter == "Somewhat":
        menu_variety_score -= 1
    elif Survey.variety_starter == "No":
        menu_variety_score -= 2

    #Q7
    if Survey.time_maincourse == "fast":
        customer_service_score += 2
    elif Survey.time_maincourse == "slow":
        customer_service_score -= 2

    #Q8
    if Survey.size_maincourse == "yes":
        value_for_money_score += 4
    elif Survey.size_maincourse == "no":
        value_for_money_score -= 4

    #Q9
    if Survey.presentation_maincourse == "Excellent":
        food_quality_score += 8
    elif Survey.presentation_maincourse == "Great":
        food_quality_score += 4
    elif Survey.presentation_maincourse == "Somewhat":
        food_quality_score += 2
    elif Survey.presentation_maincourse == "No":
        food_quality_score -= 8
    
    #Q10
    if Survey.variety_maincourse == "Excellent":
        menu_variety_score += 4
    elif Survey.variety_maincourse == "Great":
        menu_variety_score += 2
    elif Survey.variety_maincourse == "Somewhat":
        menu_variety_score += 1
    elif Survey.variety_maincourse == "No":
        menu_variety_score -= 4

    #Q12
    if Survey.time_dessert == "fast":
        customer_service_score += 1
    elif Survey.time_dessert == "slow":
        customer_service_score -= 1

    #Q13
    if Survey.size_dessert == "yes":
        value_for_money_score += 2
    elif Survey.size_dessert == "no":
        value_for_money_score -= 2

    #Q14
    if Survey.presentation_dessert == "Excellent":
        food_quality_score += 4
    elif Survey.presentation_dessert == "Great":
        food_quality_score += 2
    elif Survey.presentation_dessert == "Somewhat":
        food_quality_score += 1
    elif Survey.presentation_dessert == "No":
        food_quality_score -= 4

    #Q15
    if Survey.variety_dessert == "Excellent":
        menu_variety_score += 2
    elif Survey.variety_dessert == "Great":
        menu_variety_score += 1
    elif Survey.variety_dessert == "Somewhat":
        menu_variety_score -= 1
    elif Survey.variety_dessert == "No":
        menu_variety_score -= 2

    #Q17
    if Survey.time_drink == "fast":
        customer_service_score += 1
    elif Survey.time_drink == "slow":
        customer_service_score -= 1

    #Q18
    if Survey.size_drink == "yes":
        value_for_money_score += 2
    elif Survey.size_drink == "no":
        value_for_money_score -= 2

    #Q19
    if Survey.presentation_drink == "Excellent":
        food_quality_score += 4
    elif Survey.presentation_drink == "Great":
        food_quality_score += 2
    elif Survey.presentation_drink == "Somewhat":
        food_quality_score += 1
    elif Survey.presentation_drink == "No":
        food_quality_score -= 4

    #Q20
    if Survey.variety_drink == "Excellent":
        menu_variety_score += 2
    elif Survey.variety_drink == "Great":
        menu_variety_score += 1
    elif Survey.variety_drink == "Somewhat":
        menu_variety_score -= 1
    elif Survey.variety_drink == "No":
        menu_variety_score -= 2

    #Q21
    if Survey.greeting_entry == "Excellent":
        customer_service_score += 2
    elif Survey.greeting_entry == "Great":
        customer_service_score += 1
    elif Survey.greeting_entry == "Somewhat":
        customer_service_score -= 1
    elif Survey.greeting_entry == "No":
        customer_service_score -= 2

    #Q22
    if Survey.greeting_waiting == "Excellent":
        customer_service_score += 2
    elif Survey.greeting_waiting == "Great":
        customer_service_score += 1
    elif Survey.greeting_waiting == "Somewhat":
        customer_service_score -= 1
    elif Survey.greeting_waiting == "No":
        customer_service_score -= 2

    #Q23
    if Survey.greeting_clean == "Excellent":
        customer_service_score += 2
        hygiene_score += 2
    elif Survey.greeting_clean == "Great":
        hygiene_score += 1
    elif Survey.greeting_clean == "Somewhat":
        hygiene_score -= 2
    elif Survey.greeting_clean == "No":
        customer_service_score -= 2
        hygiene_score -= 2

    #Q24
    if Survey.greeting_order == "yes":
        customer_service_score += 1
    elif Survey.greeting_order == "no":
        customer_service_score -= 1

    #Q26
    if Survey.restroom_clean == "Excellent":
        hygiene_score += 4
    elif Survey.restroom_clean == "Great":
        hygiene_score += 2
    elif Survey.restroom_clean == "Somewhat":
        hygiene_score -= 2
    elif Survey.restroom_clean == "No":
        hygiene_score -= 4

    #27
    if Survey.missing_restroom == "yes":
        hygiene_score -= 2
    elif Survey.missing_restroom == "no":
        hygiene_score += 2
        customer_service_score += 1

    #28
    if Survey.clean_restaurant == "very bad":
        hygiene_score -= 2
        customer_service_score -= 1
    elif Survey.clean_restaurant == "bad":
        hygiene_score -= 1
        customer_service_score -= 1
    elif Survey.clean_restaurant == "great":
        hygiene_score += 2
        customer_service_score += 1

    #29
    if Survey.pay_bill_restaurant == "great":
        customer_service_score += 1
    elif Survey.pay_bill_restaurant == "bad":
        customer_service_score -= 1
    elif Survey.pay_bill_restaurant == "very bad":
        customer_service_score -= 1

    #30
    if Survey.greeting_clean == "Excellent":
        customer_service_score += 5
    elif Survey.greeting_clean == "Great":
        customer_service_score += 3
    elif Survey.greeting_clean == "poor":
        customer_service_score += 1
    elif Survey.greeting_clean == "bad":
        customer_service_score -= 5




    




    

    

    

    


