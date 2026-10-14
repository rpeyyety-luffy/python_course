# Get inputs from user
H = int(input("Enter hours (0-12): "))
M = int(input("Enter minutes (0-59): "))
S = int(input("Enter seconds (0-59): "))

# Separate calculations for each unit's contribution to the hour hand angle
hour_angle = H * 30          # 30 degrees per hour
minute_angle = M * 0.5       # 0.5 degrees per minute
second_angle = S * (1 / 120) # 1/120 degree per second

# Total angle of the hour hand
total_angle = hour_angle + minute_angle + second_angle

# Print results
print(f"Angle from hours: {hour_angle} degrees")
print(f"Angle from minutes: {minute_angle} degrees")
print(f"Angle from seconds: {second_angle:.4f} degrees")
print(f"Total hour hand angle: {total_angle:.4f} degrees")