About:
This is python simulation to record and play the movement sequence in a rc car.

How to use:
<Controls>
1. Use arrow keys to control the car(rectangel).
2. Hold 'w' to record stop or break of the car.
3. Press 's' to show the data stored about the car travelled path.
4. Press 'p' to play the recorded travelled path data.
5. Press 'r' to reset or clear the current car travelled path data.

Issues:
1. i cannot yet rotate function here because i have to delete the old car to and rerender the new car when it rotates, that creates a new car on the canvas that cannot be controlled from app.py as the old instance is not updated but a whole new car is made in functions.py 😑

Updates:
test_car2 has been separeted into different file
1. gui - app.py
2. functions - functions.py


