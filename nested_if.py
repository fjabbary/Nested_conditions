# ========================================================  
# ====================|| Task 1 ||======================== 
# ========================================================     
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: 
      pass
        
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("Do you want light a torch or proceed in the dark?")
    if action == "light a torch":
        print("Good choice")
    elif action == "proceed in the dark":
        print("Be careful, it might be dangerous.")
    else:
      pass        
    
    
# ========================================================  
# ====================|| Task 2 ||======================== 
# ========================================================

attendees = int(input("Enter number of attendees: "))
favorite_food_type = input("What is attendees' favorite type of food?: ")

# In this code facilities is dependent of venue type which itself is dependent of number of attendees
venue = "large hall" if attendees > 100 else "conference room"
facilities = "audio systems" if venue == "large hall" else "projector"
food = "Veggie Delight Caterers" if favorite_food_type == "vegetarian" else "Gourmet Meals Caterers"

print("Venue is {}".format(venue))
print("Additional facilities: {}".format(facilities))
print("Recommended food is {}".format(food))