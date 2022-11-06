def proc_start(start):
    x = start.split(':')
    x[1] = x[1].split()
    x.extend(x[1])
    del x[1]
    
    if x[2] == "PM":
        hr = 12+int(x[0])
    else:
        hr = int(x[0])
    
    base = [str(hr), x[1]]
    return base

def add_to_base(base, duration):
    duration = duration.split(':')
    
    # Process Minutes
    mt = int(base[1])+int(duration[1])
    mt_60 = int(mt/60)
    mt_remain = mt%60    
    
    # Process Hours
    hr = int(base[0])+int(duration[0]) + mt_60
    days = int(hr/24)
    hours = hr%24
    
    added_time = [days, hours, mt_remain]   
 
    return added_time

def print_time(added_time, week_day = None):
    # Check length of minutes. Need to have 2 digits
    if added_time[2] < 10:
        minutes = "0" + str(added_time[2])
    else:
        minutes = str(added_time[2])
    
    # AM or PM
    am_pm = None
    hour_am_pm = None
    
    if added_time[1] < 12:
        am_pm = "AM"
        hour_am_pm = added_time[1]
    else:
        am_pm = "PM"
        hour_am_pm = added_time[1] - 12
    
    # Make sure that "hour_am_pm" is not zero and convert to string
    if hour_am_pm == 0:
        hour_am_pm = str(12)
    else:
        hour_am_pm = str(hour_am_pm)
        
    # Today, the next day, or n-days
    number_of_days = None
    if added_time[0] == 0:
        number_of_days = ""
    elif added_time[0] == 1:
        number_of_days = " (next day)"
    else:
        number_of_days = " (" + str(added_time[0]) + " days later)"
    
    # Check if week day is required
    if week_day != None:
        week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        week_day = week_days.index(week_day.lower().capitalize()) + added_time[0]
        week_day_number = week_day%7
        
        # Assemble final message
        hour_final = hour_am_pm + ":" + minutes + ' ' + am_pm +', ' + week_days[week_day_number] + number_of_days
        
    else:
        # Assemble final message
        hour_final = hour_am_pm + ":" + minutes + ' ' + am_pm + number_of_days
    
    return hour_final

def add_time(start, duration, week_day = None):
    base = 0
    base = proc_start(start)
    added_time = add_to_base(base, duration)
    new_time = print_time(added_time, week_day)  

    return new_time