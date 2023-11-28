import pyperclip

# switch_lat_long will change the order of single pair coordinates that have copied to the clipboard 
# and are seperated by a comma ","
# It returns them seperated by a comman and a space ", " which can be modified by the .join function

# store lat/long as variable called text
text = pyperclip.paste()

# split the lat/long at the comma
coordinates = text.split(',')

# reverse lat/long
coordinates.reverse()

# strip white space
striped_coordinates = [item.strip() for item in coordinates]

# join the long/lat back together
new_coordinates = ', '.join(striped_coordinates)

# add the new coordinates to the clipboard
pyperclip.copy(new_coordinates)

# (optional) you may print the coordinates to the terminal
print("clipboard updated = " + pyperclip.paste())