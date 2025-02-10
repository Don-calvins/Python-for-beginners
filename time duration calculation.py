hour = int(input("Starting time (hours): "))
minutes = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))
minutes = minutes + dura # find a total of all minutes
hour = hour + minutes // 60 # find a number of hours hidden in minutes and update the hour
minutes = minutes % 60 # correct minutes to fall in the (0..59) range
hour = hour % 24 # correct hours to fall in the (0..23) range
print(hour, ":", minutes, sep='')