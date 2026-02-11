device_status = True
temperature = 49

if device_status:
    if temperature > 35:
        print("High temperature warning!")
    else:
        print("Normal temperature")
else:
    print("Device is offline")