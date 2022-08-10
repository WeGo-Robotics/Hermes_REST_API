import requests
import json
import time
    
def getBatteryPercentage(_hermes_url: str = "http://192.168.11.1:1448/") -> int:
    if not _hermes_url[-1] == '/':
        _hermes_url += '/'
    
    api_address = "api/core/system/v1/power/status"
    try:
        response = requests.get(_hermes_url + api_address, timeout=3)
        return response.json()['batteryPercentage']
    except Exception as e:
        print("Timeout!! Return -1")
        return -1
        
  
def setGoHomeAction(_hermes_url: str = "http://192.168.11.1:1448/") -> bool:
    if not _hermes_url[-1] == '/':
        _hermes_url += '/'
        
    api_address = "api/multi-floor/motion/v1/gohomeaction"
    try:
        response = requests.post(_hermes_url + api_address, timeout=3)
        return True
        
    except Exception as e:
        print("Timeout!! Return False")
        return False
    
if __name__ == '__main__':
    url = "http://192.168.11.1:1448"
    
    battery_percent = getBatteryPercentage(url)
        
    go_home_threshold = 20
    while True:
        print("Battery Percentage of Hermes is {}%".format(battery_percent))
        
        if battery_percent < go_home_threshold:
            print("Battery is lower than {}%, Set GoHome Action".format(go_home_threshold))
            setGoHomeAction(url)    
        else:
            print("Battery is enough")
        time.sleep(10)
