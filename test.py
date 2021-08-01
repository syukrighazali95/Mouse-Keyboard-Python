import mouse 

# Note this is just for testing

# This is to move mouse without dragging
print(mouse.get_position())
(x_original, y_original) = mouse.get_position()
mouse.move(-x_original, -y_original, absolute=False, duration=0.2)
print(mouse.get_position())
mouse.move(900, 500, absolute=False, duration=0.2)
print(mouse.get_position())

# This is to move mouse while dragging
# mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)

# This is to check if the mouse is pressed
# print(mouse.is_pressed("right"))

