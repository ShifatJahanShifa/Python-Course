def get_time(seconds):
    hours = (seconds//3600)
    minutes = (seconds - (hours * 3600))//60
    remaining_seconds = (seconds - (hours * 3600)-(minutes*60))
    return hours, minutes, remaining_seconds


hours, minutes, remaining_seconds = get_time(5000)
print("hours: " + str(hours))
print("minutes: " + str(minutes))
print("remaining seconds: " + str(remaining_seconds))
