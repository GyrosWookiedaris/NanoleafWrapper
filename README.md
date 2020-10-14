# NanoleafWrapper
## Introduction

A simple python wrapper for Nanoleaf API

If you already have the IP and a token, just replace it in the config.json.
Else start the program and it guides you through the process.

If you have problems finding out the IP, check your DHCP or your router for that.

The wrapper will be expanded from time to time. This is the first version, written in about an hour. So don't expect too much.

## How to use it:
Just copy the nanoleaf.py and config.json to your projects source folder.

Then you can just
```
from nanoleaf import Nanoleaf
```
and start working with the wrapper.

Make an object and access the funktions like that:
```
nano = Nanoleaf()
result = nano.get_all_controller_info()
print(result)
```
The wrapper returns all data as json.

## Functions
####get_all_controller_data
Returns all controller data.

####get_status
Returns the current on/off state.

####set_status
Set the status to on or off. Expects a string.
```
nano.set_status("on")
```

####get_brightness
Returns the current brightness.

####set_brightness
Set the brightness. Expects an int from 0 to 100.
```
nano.set_brightness(100)
```

####get_color
Returns the current color.

####set_color
Set the color as hue value. Expects an int from 0 to 360.
```
nano.set_color(120)
```

####get_saturation
Returns the saturation.

####set_saturation
Set the saturation. Expects an int from 0 to 100.
```
nano.set_saturation(25)
```

####get_ct
Returns the color temperature.

####set_ct
Set the color temperature. Expects an int from 1200 to 6000 (uses Kelvin).

####get_colormode
Returns the current colormode.

####get_current_scene
Returns the current scene.

####get_scenes
Returns all scenes.

####set_scene
Set a scene. Expects the name of the scene as string.
```
nano.set_scene("Fireplace")
```


