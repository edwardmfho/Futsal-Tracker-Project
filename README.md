# Futsal Tracker Project


### The Situation
As a regular futsal player, it is important to reflect on how we played in previous games, and improve upon it. Yet currently there is no "economic" options (There are expensive option such as as Veo) for us to keep track of how we play, do some simple analysis, and heck, who doesn't want to capture the sensational moment of play? 
### The Task

One of the challenges to accomplish this task is the limitation of camera equipment, with a huge indoor court, we simply do not have the sufficient angle to capture the whole scene. To resolve this issue, we propose the use of a ball-tracking algorithm, which enables the camera to follow the motion of the football, and to film the whole game.

### The Action

#### Ball Tracking Algorithm

This is an on-going project, we have currently implemented a simple movement tracking algorithm, but looking to develop a simple classifier to enable the model to "track the football" instead of all moving objects on scene. 

#### Hardware
We proposed to leverage a servo to enable camera movement. Hardwares to be used:
- Rasberry Pi Board
- Raspberry Pi Camera (for tracking, not for filiming)
- Tripod
- Servo
- Camera for filming

### The Response

To be written.

## Installation

The tracking tool is developed based on Python 3.7. We recommend using a virtual environment to achieve the task. Also you will require the following packages for the tool to run properly:

```bash
pip install opencv-python
```

## Usage

```bash
python tracking_bbox_trial.py
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
