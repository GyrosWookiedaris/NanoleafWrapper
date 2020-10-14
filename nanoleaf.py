

import requests
import json

with open("config.json") as file:
    config = json.load(file)
    if config["ip"] == "ENTER IP HERE":
        print("----------------------------------------------------------")
        print("Nanoleafs not connected.")
        ip = input("Enter the IP of the Nanoleaf: ")
        print("Start pairing mode and then press ENTER within 30 Seconds!")
        print("(You can start the pairing mode by pressing the on/off button for more than 5 sec, "
              "until it starts blinking)")
        wait = input("")
        url = f"http://{ip}:16021/api/v1/new"
        token = json.loads(requests.post(url).text)
        token = token["auth_token"]

        data = {
            "ip": ip,
            "token": token,
        }

        with open("config.json", "w") as file:
            json.dump(data, file)

        with open("config.json") as file:
            config = json.load(file)

class Nanoleaf:
    baseurl = str()
    token = str()

    def __init__(self):
        ip = config["ip"]
        token = config["token"]
        self.baseurl = f"http://{ip}:16021"
        self.token = token

    def get_all_controller_info(self):
        addurl = f"/api/v1/{self.token}/"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_status(self):
        addurl = f"/api/v1/{self.token}/state/on"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_status(self, state):
        if state.lower() == "on":
            state = True
        else:
            state = False
        addurl = f"/api/v1/{self.token}/state"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "on": {
                "value": state
            }
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)

    def get_brightness(self):
        addurl = f"/api/v1/{self.token}/state/brightness"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_brightness(self, brightness, duration=None):
        addurl = f"/api/v1/{self.token}/state"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        if duration is None:
            data = {
                "brightness": {
                    "value": brightness
                }
            }
        else:
            data = {
                "brightness": {
                    "value": brightness,
                    "duration": duration
                }
            }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)

    def get_color(self):
        addurl = f"/api/v1/{self.token}/state/hue"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_color(self, color):
        addurl = f"/api/v1/{self.token}/state"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "hue": {
                "value": color
            }
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)

    def get_saturation(self):
        addurl = f"/api/v1/{self.token}/state/sat"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_saturation(self, saturation):
        addurl = f"/api/v1/{self.token}/state/sat"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "sat": {
                "value": saturation
            }
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)

    def get_ct(self):
        addurl = f"/api/v1/{self.token}/state/ct"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_ct(self, ct):
        addurl = f"/api/v1/{self.token}/state"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "ct": {
                "value": ct
            }
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)

    def get_colormode(self):
        addurl = f"/api/v1/{self.token}/state/colorMode"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_current_scene(self):
        addurl = f"/api/v1/{self.token}/effects/select"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_scenes(self):
        addurl = f"/api/v1/{self.token}/effects/effectsList"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_scene(self, scene):
        scene = scene.replace("\"", "")
        addurl = f"/api/v1/{self.token}/effects"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "select": scene
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)
