
default_allowed_times = [9,10,11,12,13,14,15,16]
test_schedule = [10,12]
test_schedule2 = [12,14]

def scheduling_logic():
    
    # The logic is that the allowed times list sets out the time range throughout a day , 9-5, that is allowed for scheduling meetings
    # The program should take in two additional lists but these will act as peoples schedules for the day
    # The times in these lists will be off limits for scheduling new meetings
    # In the test schedules for now a number for example: [9] represents a 1 hour meeting at 9 until 10 which means 10 is still free

    # This list is the combination of both schedules
    unavailable_times = test_schedule + test_schedule2
    
    # This list is the sorted combination
    unavailable_times.sort()
    
    # This removes duplicates from the combination list
    unavailable_times = list(dict.fromkeys(unavailable_times))
    
    print("These are the times that cannot be used " + str(unavailable_times))
    
    
    # Function to add times that are not in the list of unavailable times list to a new list of allowed times
    def remove_times(default_allowed_times, unavailable_times):
        allowed_times = []
        for i in default_allowed_times:
            if i not in unavailable_times:
                allowed_times.append(i)
        return allowed_times

    allowed_times = remove_times(default_allowed_times, unavailable_times)
    
    print("These are the times that can be used to schedule a meeting: " + str(allowed_times))
    
    chosen_time=  input("Choose an available time " + str(allowed_times) + ": ")
    
    # Determine whether the meeting takes place am or pm and display to user
    if int(chosen_time) < 13:
        print("You have booked a meeting for " + str(chosen_time) + ":00 am.")
    else:
        print("You have booked a meeting for " + str(chosen_time) + ":00 pm.")
         
    
    
    # Add the chosen time from the user input to the unavailable times list
    unavailable_times.append(int(chosen_time))
    
    # Function to add the additional time from the user input to a new allowed times list
    def remove_chosen_times(allowed_times, unavailable_times):
        allowed_times2 = []
        for i in allowed_times:
            if i not in unavailable_times:
                allowed_times2.append(i)
        return allowed_times2
    
    allowed_times2 = remove_chosen_times(allowed_times, unavailable_times)
    
    print("These are the updated available times: "+ str(allowed_times2))
    
    
    


scheduling_logic()



    
     
