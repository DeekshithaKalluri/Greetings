import time

timestamp = input("Enter the time in 24-hour format (HH:MM:SS): ")

hour = int(timestamp.split(':')[0])

if 6 <= hour < 12:
  print("Good Morning!")
elif 12 <= hour < 18:
  print("Good Afternoon!")
else:
  print("Good Evening!")
