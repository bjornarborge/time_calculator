def add_time(start, duration, day=None):
    # Split start time into hours and minutes
    start_time = start.split()
    start_hours = int(start_time[0].split(':')[0])
    start_minutes = int(start_time[0].split(':')[1])
    start_period = start_time[1]

    # Split duration into hours and minutes
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    # Calculate new time
    new_hours = start_hours + duration_hours
    new_minutes = start_minutes + duration_minutes
    
    # Calculate new period
    new_period = start_period
    if new_minutes >= 60:
        new_hours += 1
        new_minutes -= 60
    if new_hours >= 12:
        if start_period == 'AM':
            new_period = 'PM'
        else:
            new_period = 'AM'
        new_hours -= 12
    
    if new_hours == 0:
        new_hours = 12

    
    # Calculate days later
    days_later = 0
    if new_hours >= 12:
        days_later = 1
        if new_day == 'next day':
            new_day = None
        else:
            # Make case sensitive
            new_day = new_day.lower()
            # Create list of days
            days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
            day_index = days.index(new_day)
            new_day = days[(day_index + 1) % 7]

    # Format new time
    new_time = str(new_hours) + ':' + str(new_minutes).zfill(2) + ' ' + new_period
    if new_day != None:
        new_time += ', ' + new_day.capitalize()

    return new_time
