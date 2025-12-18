today_is_opp_day = False

# Set it_is_opp_day bassed on today_is_opp_day
if today_is_opp_day == True:
    say_it_is_opp_day = True
else:
    say_it_is_opp_day = False

# If it is opp day, toggle say_it_is_opp_day
if today_is_opp_day :
    say_it_is_opp_day = not say_it_is_opp_day

# Say what day it is
if say_it_is_opp_day == True:
    print("Today is Opposite Day")
elif say_it_is_opp_day == False:
    print("Today is not an Opposite day")