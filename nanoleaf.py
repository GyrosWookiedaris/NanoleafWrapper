

import requests
import json

with open("nl_config.json") as file:
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

        with open("nl_config.json", "w") as file:
            json.dump(data, file)

        with open("nl_config.json") as file:
            config = json.load(file)

class Nanoleaf:
    baseurl = str()
    token = str()

    def __init__(self):
        ip = config["ip"]
        token = config["token"]
        self.baseurl = f"http://{ip}:16021/api/v1/{self.token}"
        self.token = token

    def get_all_controller_info(self):
        addurl = "/"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_status(self):
        addurl = "/state/on"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_status(self, state):
        if state.lower() == "on":
            state = True
        else:
            state = False
        addurl = "/state"
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
        addurl = "/state/brightness"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_brightness(self, brightness, duration=None):
        addurl = "/state"
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
        addurl = "/state/hue"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_color(self, color):
        addurl = "/state"
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
        addurl = "/state/sat"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_saturation(self, saturation):
        addurl = "/state/sat"
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
        addurl = "/state/ct"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_ct(self, ct):
        addurl = "/state"
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
        addurl = "/state/colorMode"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_current_scene(self):
        addurl = "/effects/select"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def get_scenes(self):
        addurl = "/effects/effectsList"
        url = self.baseurl + addurl
        result = requests.get(url)
        return json.loads(result.text)

    def set_scene(self, scene):
        scene = scene.replace("\"", "")
        addurl = "/effects"
        url = self.baseurl + addurl
        headers = {
            "Content-Type": "application/json"
        }
        data = {
            "select": scene
        }
        result = requests.put(url, headers=headers, data=json.dumps(data))
        return json.loads(result.text)
