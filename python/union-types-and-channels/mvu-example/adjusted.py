from pydantic import BaseModel, PositiveInt, Field
from typing import Union
from loguru import logger


# Define the GameState (example placeholder, can be expanded as needed)
class GameState(str, Enum):
    PLAYING = "Playing"
    PAUSED = "Paused"
    GAME_OVER = "GameOver"


# The Model representing the current state
class Model(BaseModel):
    sides: int = Field(ge=0, default=4)
    angle: int = Field(ge=0, default=45)
    pointiness: int = Field(ge=0, default=5)
    arm_ratio: float = Field(ge=0.0, default=0.8)
    eye_distance: int = Field(ge=0, default=10)
    eye_height: int = Field(ge=0, default=15)
    mouth_size: int = Field(ge=0, default=20)
    mouth_height: int = Field(ge=0, default=10)
    face_scale: int = Field(ge=0, default=100)
    cassie: str = "Initial"
    can_lucy_me: bool = False
    happy: bool = True
    blink: bool = False
    game_state: GameState = GameState.PLAYING


# Define messages (actions) as Pydantic models
class Msg(BaseModel):
    pass


class Reset(Msg):
    pass


class DownloadSvg(Msg):
    pass


class SetSides(Msg):
    sides: str


class SetAngle(Msg):
    angle: str


class SetPointiness(Msg):
    pointiness: str


class SetArmRatio(Msg):
    arm_ratio: str


class SetEyeDistance(Msg):
    eye_distance: str


class SetEyeHeight(Msg):
    eye_height: str


class SetMouthSize(Msg):
    mouth_size: str


class SetMouthHeight(Msg):
    mouth_height: str


class SetFaceScale(Msg):
    face_scale: str


class SetCassie(Msg):
    cassie: str


class SetCanLucyMe(Msg):
    can_lucy_me: str


class SetHappy(Msg):
    happy: bool


class SetBlink(Msg):
    blink: bool


# Initialize the model
def init() -> Model:
    return Model()


# Update function based on message types
def update(model: Model, msg: Msg) -> Model:
    match msg:
        case Reset():
            return init()
        case SetSides(sides=sides):
            model.sides = int(sides)
        case SetAngle(angle=angle):
            model.angle = int(angle)
        case SetPointiness(pointiness=pointiness):
            model.pointiness = int(pointiness)
        case SetArmRatio(arm_ratio=arm_ratio):
            model.arm_ratio = float(arm_ratio)
        case SetEyeDistance(eye_distance=eye_distance):
            model.eye_distance = int(eye_distance)
        case SetEyeHeight(eye_height=eye_height):
            model.eye_height = int(eye_height)
        case SetMouthSize(mouth_size=mouth_size):
            model.mouth_size = int(mouth_size)
        case SetMouthHeight(mouth_height=mouth_height):
            model.mouth_height = int(mouth_height)
        case SetFaceScale(face_scale=face_scale):
            model.face_scale = int(face_scale)
        case SetCassie(cassie=cassie):
            model.cassie = cassie
        case SetCanLucyMe(can_lucy_me=can_lucy_me):
            model.can_lucy_me = bool(can_lucy_me)
        case SetHappy(happy=happy):
            model.happy = happy
        case SetBlink(blink=blink):
            model.blink = blink
        case _:
            logger.warning(f"Unrecognized message: {msg}")
    return model


# View function that outputs a string representation of the model (for rendering HTML or similar)
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


# Main loop to simulate the app's behavior
def main():
    # Initialize the model
    model = init()

    # Simulate some updates
    logger.info("Initial state:")
    print(view(model))

    model = update(model, SetSides(sides="6"))
    model = update(model, SetAngle(angle="90"))
    model = update(model, SetHappy(happy=False))

    logger.info("Updated state:")
    print(view(model))

    # Reset the model
    model = update(model, Reset())
    logger.info("State after reset:")
    print(view(model))


if __name__ == "__main__":
    main()
