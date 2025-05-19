import pygame
import time


pygame.init()
pygame.joystick.init()

joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    print("No joystick found")
    pygame.quit()
    exit()

joysticks = []
for i in range(joystick_count):
    joystick = pygame.joystick.Joystick(i)
    joystick.init()
    print(f"Detected Devices {i}: {joystick.get_name()}")
    joysticks.append(joystick)


# Print data of all connected joysticks input
try:
    while True:
        pygame.event.pump()

        all_data = {}

        for i, js in enumerate(joysticks):
            axes = [js.get_axis(a) for a in range(js.get_numaxes())]
            buttons = [js.get_button(b) for b in range(js.get_numbuttons())]
            hats = [js.get_hat(h) for h in range(js.get_numhats())]

            all_data[f'joystick_{i}'] = {
                'name': js.get_name(),
                'axes': axes,
                'buttons': buttons,
                'hats': hats
            }

        print(f"Data: {all_data}")

except KeyboardInterrupt:
    print("\nProgram terminated.")

finally:
    pygame.quit()