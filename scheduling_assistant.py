
default_allowed_times = [9,10,11,12,13,14,15,16]
test_schedule = [10,12]
test_schedule2 = [12,14]

def scheduling_logic():
    
    # The logic is that the allowed times list sets out the time range throughout a day , 9-5, that is allowed for scheduling meetings
    # The program should take in two additional lists but these will act as peoples schedules for the day
    # The times in these lists will be off limits for scheduling new meetings
    # In the test schedules for now a number for example: [9] represents a 1 hour meeting at 9 until 10 which means 10 is still free

    # This list is the combination of both schedules
    test_schedule3 = test_schedule + test_schedule2
    
    # This list is the sorted combination
    test_schedule3.sort()
    
    # This removes duplicated from the combination list
    test_schedule3 = list(dict.fromkeys(test_schedule3))
    
    print("These are the times that cannot be used " + str(test_schedule3))
    
    
    # Function to remove times that cannot be used from allowed times list
    def remove_times(default_allowed_times, test_schedule3):
        allowed_times = []
        for i in default_allowed_times:
            if i not in test_schedule3:
                allowed_times.append(i)
        return allowed_times

    allowed_times = remove_times(default_allowed_times, test_schedule3)
    
    print("These are the times that can be used to schedule a meeting: " + str(allowed_times))
    


scheduling_logic()



    
     
