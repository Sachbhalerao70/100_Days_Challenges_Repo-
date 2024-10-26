def timeConversion(s):
    
    period = s[-2:]  # Last two characters
    # Extract the hour, minute, and second
    hour = int(s[:2])  # First two characters
    minute = s[3:5]    # Characters at index 3 and 4
    second = s[6:8]    # Characters at index 6 and 7

    # Convert hour based on AM/PM
    if period == "AM":
        if hour == 12:
            hour = 0  # Midnight case
    else:  # PM case
        if hour != 12:
            hour += 12  # Convert to 24-hour format

    # Format the hour to two digits
    military_time = f"{hour:02}:{minute}:{second}"
    return military_time

input_time = "07:05:45PM"
# Call the function and print the result
output_time = timeConversion(input_time)
print(output_time)  