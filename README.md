# EVtol_FlightPack

- Requirements:

  1. Download driver of the flght pack

     https://support.thrustmaster.com/en/product/t-16000m-fcs-flight-pack-en/

  2. Install pygame

     ```
     pip install pygame
     ```



- Joystick Input Reader

  ```
  python joystick_reader.py
  ```

  This script initializes and reads input from all connected joystick devices
  using the pygame library. It collects data including:

  - Axis positions (e.g., X/Y sticks, throttle, twist)
  - Button press states
  - Hat (D-pad) directions

  Run the script to print the current state of all inputs for each 
  connected joystick in a structured dictionary format:

  Example output:

  ```
  Data: {
      'joystick_0': {
          'name': 'T.16000M Joystick',
          'axes': [0.0, 0.0, 0.0, 0.0],
          'buttons': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          'hats': [(0, 0)]
      },
      'joystick_1': {
          'name': 'TWCS Throttle',
          'axes': [...],
          'buttons': [...],
          'hats': [...]
          }
     }
  ```

  

- Joystick Input GUI 

  ```
  python joystick_gui.py <joystick_index>
  ```

  It monitors the real-time state of a connected joystick device.

