###
# Describes a mobile phone using a dictionary
#
mobile = {
    "OS": "Android",
    "Brand": "Samsung",
    "Model": "Galaxy S35",
    "RAM": "8 GB",
    "Storage": "256 GB",
    "Battery": "5000 mAh"
}

for key, value in mobile.items():
    print(f"{key} : {value}")