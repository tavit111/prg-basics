###
# Tests length conversion functions
#
import converters

print("200 cm =", converters.cm_to_m(200), "m")
print("3 m =", converters.m_to_cm(3), "cm")

print("25.4 cm =", converters.cm_to_inches(25.4), "inches")
print("5 feet 10 inches =", converters.feet_inches_to_cm(5, 10), "cm")