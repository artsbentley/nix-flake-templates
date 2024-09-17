from pydantic import BaseModel, conint, confloat
from enum import Enum
from typing import Union


# Define the GameState as a placeholder (you can expand it based on your needs)
class GameState(str, Enum):
    PLAYING = "Playing"
    PAUSED = "Paused"
    GAME_OVER = "GameOver"


# The Model representing the current state (similar to Gleam's Model)
class Model(BaseModel):
    sides: conint(ge=0)  # Integer greater than or equal to 0
    angle: conint(ge=0)
    pointiness: conint(ge=0)
    arm_ratio: confloat(ge=0.0)  # Float greater than or equal to 0
    eye_distance: conint(ge=0)
    eye_height: conint(ge=0)
    mouth_size: conint(ge=0)
    mouth_height: conint(ge=0)
    face_scale: conint(ge=0)
    cassie: str
    can_lucy_me: bool
    happy: bool
    blink: bool
    game_state: GameState


# Define the possible messages (similar to Elm's Msg)
class Msg(Enum):
    RESET = "Reset"
    DOWNLOAD_SVG = "DownloadSvg"
    SET_SIDES = "SetSides"
    SET_ANGLE = "SetAngle"
    SET_POINTINESS = "SetPointiness"
    SET_ARM_RATIO = "SetArmRatio"
    SET_EYE_DISTANCE = "SetEyeDistance"
    SET_EYE_HEIGHT = "SetEyeHeight"
    SET_MOUTH_SIZE = "SetMouthSize"
    SET_MOUTH_HEIGHT = "SetMouthHeight"
    SET_FACE_SCALE = "SetFaceScale"
    SET_CASSIE = "SetCassie"
    SET_CAN_LUCY_ME = "SetCanLucyMe"
    SET_HAPPY = "SetHappy"
    SET_BLINK = "SetBlink"


# Initialize the model with some default values
def init() -> Model:
    return Model(
        sides=4,
        angle=45,
        pointiness=5,
        arm_ratio=0.8,
        eye_distance=10,
        eye_height=15,
        mouth_size=20,
        mouth_height=10,
        face_scale=100,
        cassie="Initial",
        can_lucy_me=False,
        happy=True,
        blink=False,
        game_state=GameState.PLAYING,
    )


# Update function handling different messages
def update(model: Model, msg: Msg, value: Union[str, bool]) -> Model:
    match msg:
        case Msg.RESET:
            return init()
        case Msg.SET_SIDES:
            model.sides = int(value)
        case Msg.SET_ANGLE:
            model.angle = int(value)
        case Msg.SET_POINTINESS:
            model.pointiness = int(value)
        case Msg.SET_ARM_RATIO:
            model.arm_ratio = float(value)
        case Msg.SET_EYE_DISTANCE:
            model.eye_distance = int(value)
        case Msg.SET_EYE_HEIGHT:
            model.eye_height = int(value)
        case Msg.SET_MOUTH_SIZE:
            model.mouth_size = int(value)
        case Msg.SET_MOUTH_HEIGHT:
            model.mouth_height = int(value)
        case Msg.SET_FACE_SCALE:
            model.face_scale = int(value)
        case Msg.SET_CASSIE:
            model.cassie = value
        case Msg.SET_CAN_LUCY_ME:
            model.can_lucy_me = bool(value)
        case Msg.SET_HAPPY:
            model.happy = value
        case Msg.SET_BLINK:
            model.blink = value
    return model


# View function that returns a simplified string representation
def view(model: Model) -> str:
    return f"""
    <div>
        <p>Sides: {model.sides}</p>
        <p>Angle: {model.angle}</p>
        <p>Pointiness: {model.pointiness}</p>
        <p>Arm Ratio: {model.arm_ratio}</p>
        <p>Eye Distance: {model.eye_distance}</p>
        <p>Eye Height: {model.eye_height}</p>
        <p>Mouth Size: {model.mouth_size}</p>
        <p>Mouth Height: {model.mouth_height}</p>
        <p>Face Scale: {model.face_scale}</p>
        <p>Cassie: {model.cassie}</p>
        <p>Can Lucy Me: {model.can_lucy_me}</p>
        <p>Happy: {model.happy}</p>
        <p>Blink: {model.blink}</p>
        <p>Game State: {model.game_state}</p>
    </div>
    """


# Main function to simulate the app loop
def main():
    # Initialize the app state
    model = init()

    # Display the initial state
    print(view(model))

    # Simulate updating the sides, angle, and happiness
    model = update(model, Msg.SET_SIDES, "6")
    model = update(model, Msg.SET_ANGLE, "90")
    model = update(model, Msg.SET_HAPPY, True)

    # View the updated state
    print(view(model))

    # Reset the model
    model = update(model, Msg.RESET, "")
    print("After reset:")
    print(view(model))


if __name__ == "__main__":
    main()
