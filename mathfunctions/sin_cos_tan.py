#program to find sin,cos and tan of an angle
import math

# Get angle input in degrees from user
angle_degrees = float(input("Enter angle in degrees: "))

# Convert degrees to radians (math trigonometric functions expect radians)
angle_radians = math.radians(angle_degrees)

# Calculate sine, cosine, and tangent
sin_value = math.sin(angle_radians)
cos_value = math.cos(angle_radians)

# Display results
print(f"sin({angle_degrees}°) = {sin_value}")
print(f"cos({angle_degrees}°) = {cos_value}")

# Tangent is undefined at 90°, 270°, etc. (where cosine is zero)
if math.isclose(cos_value, 0, abs_tol=1e-9):
    print(f"tan({angle_degrees}°) is undefined")
else:
    tan_value = math.tan(angle_radians)
    print(f"tan({angle_degrees}°) = {tan_value}")