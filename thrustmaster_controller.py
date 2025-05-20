import pygame
import sys


# Apply Center Dead Zone for Roll Pitch Yaw
def apply_center_deadzone(val, deadzone=0.05):
    if abs(val) < deadzone:
        return 0.0
    return val


# Apply Center Dead Zone for Throttle
def apply_throttle_deadzone(val, deadzone=0.02):
    if val < -1 + deadzone:
        return -1.0
    return val


def get_flight_controls(stick_js, throttle_js,
                        axis_roll_idx, axis_pitch_idx,
                        axis_yaw_idx, axis_throttle_idx):
    pygame.event.pump()

    raw_roll = stick_js.get_axis(axis_roll_idx)
    raw_pitch = stick_js.get_axis(axis_pitch_idx)
    raw_yaw = throttle_js.get_axis(axis_yaw_idx)
    raw_throttle = throttle_js.get_axis(axis_throttle_idx)

    roll = apply_center_deadzone(raw_roll)
    pitch = -apply_center_deadzone(raw_pitch)  # Invert: forward stick gives negative pitch
    yaw = apply_center_deadzone(raw_yaw)
    throttle = -apply_throttle_deadzone(raw_throttle)

    # # Clamp values to [-1, 1]
    roll = max(-1.0, min(1.0, roll))
    pitch = max(-1.0, min(1.0, pitch))
    yaw = max(-1.0, min(1.0, yaw))
    throttle = max(-1.0, min(1.0, throttle))

    return roll, pitch, yaw, throttle


def main():
    pygame.init()
    pygame.joystick.init()

    # Get name->index map
    mapping = {}
    for idx in range(pygame.joystick.get_count()):
        js = pygame.joystick.Joystick(idx)
        js.init()
        name = js.get_name()
        print(f"[{idx}] found joystick: {name!r}")
        mapping[name] = idx

    # Get T.16000M Joystick and TWCS Throttle
    try:
        stick_js = pygame.joystick.Joystick(mapping['T.16000M Joystick'])
        throttle_js = pygame.joystick.Joystick(mapping['TWCS Throttle'])
    except KeyError:
        print("Can't find T.16000M Joystick or TWCS Throttle.")
        pygame.quit()
        sys.exit(1)
    stick_js.init()
    throttle_js.init()

    # Set the index of axis
    axis_roll_index = 0  # stick roll
    axis_pitch_index = 1  # stick pitch
    axis_yaw_index = 7  # Paddle for yaw [connected on throttle]
    axis_throttle_index = 2  # throttle

    while True:
        all_data = {}
        roll, pitch, yaw, throttle = get_flight_controls(
            stick_js, throttle_js,
            axis_roll_index, axis_pitch_index,
            axis_yaw_index, axis_throttle_index
        )

        all_data['flight_controls'] = {
            'roll': round(roll, 3),
            'pitch': round(pitch, 3),
            'yaw': round(yaw, 3),
            'throttle': round(throttle, 3)
        }

        # 6) dump everything in one go
        print(f"Data: {all_data}")


if __name__ == '__main__':
    main()
