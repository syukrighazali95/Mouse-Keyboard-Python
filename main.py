import mouse
import keyboard
import time

def place_block(block_coordinates, platform_coordinates, scale=1):
    # Get origin
    (x_original, y_original) = mouse.get_position()
    mouse.move(-x_original, -y_original, absolute=False, duration=0.2)
    print(mouse.get_position())

    # Specify coordinates for block and platform
    (x_block, y_block) = block_coordinates
    (x_plat, y_plat) = platform_coordinates

    # Move mouse to choose block
    mouse.move(x_block, y_block, absolute=False, duration=0.2)
    print(mouse.get_position())
    mouse.click(button='left')

    # Move mouse to platform
    # Move from end to end for 12 seconds
    duration = 12
    mouse.move(x_plat-x_block, y_plat-y_block, absolute=False, duration=0.1)

    t0 = time.perf_counter()
    t1 = 0
    time_elapsed = 0
    count = 0

    while t1 < duration:
        t1 = time.perf_counter()
        print(f"{count} t1: {t1}")
        time_elapsed = t1-t0 
        print(f"{count} time_elapsed: {time_elapsed}")
        mouse.press(button='left')
        keyboard.press("c")

    print(t1)
    keyboard.release("c")
    mouse.release(button='left')

place_block((900, 500), (800, 400))
