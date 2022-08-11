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
        if response.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
        print("Timeout!! Return False")
        return False
    
def deleteAction(_hermes_url: str = "http://192.168.11.1:1448/") -> bool:
    if not _hermes_url[-1] == '/':
        _hermes_url += '/'
        
    api_address = "api/core/motion/v1/actions/:current"
    try:
        response = requests.post(_hermes_url + api_address, timeout=3)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
        print("Timeout!! Return False")
        return False
    
if __name__ == '__main__':
    url = "http://192.168.11.1:1448"
    go_home_flag = False
    go_home_threshold = 20
    setGoHomeAction(url)

    
    while True:
        battery_percent = getBatteryPercentage(url)
        print("Battery Percentage of Hermes is {}%".format(battery_percent))
        
        if battery_percent < go_home_threshold and go_home_flag == False:
            print("Battery is lower than {}%, Set GoHome Action".format(go_home_threshold))
            
            go_home_flag = setGoHomeAction(url)
        elif battery_percent >= go_home_threshold:
            print("Battery is enough")
            go_home_flag = False
        elif go_home_flag == True:
            print("Battery is lower than {}%, Set GoHome Action".format(go_home_threshold))
        time.sleep(10)
