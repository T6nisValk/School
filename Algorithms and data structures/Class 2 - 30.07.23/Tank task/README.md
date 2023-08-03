# Random task

## Stage 1

Class: Tank

Methods:

- MoveForward
- MoveBack
- MoveLeft
- MoveRight
- Shoot
- Info

Variables for the Tank:

- Coordinates
- Direction
- Amount of shots to each direction

Tank can move to 4 directions, forward, left, right, back for one position at a time, after each
move there should be a console output that the tank moved, e.g ``Tank moved left``.

After the tank moved a certain direction it should be saved that the tank is facing the right
direction.

Tank can shoot at the direction that it is facing.

Info method should show where the tank is facing, it's coordinates, how many shots were made in
total and how many shots were made to each direction

All the controls of the tank should be done from console.

There is no need for any visual representation of where the tank is.

Create a meny with the user to get all the actions on what needs to happen.

## Stage 2

Update the program to have a target. The mission of the tank will be to be in a correct position
so that after the shot is done the target would be destroyed. After the target is destroyed, a
new target should instantly show up, at a random location, but it can not generate at the same
location of the tank.

Class: Target

Variables:

- Coordinates

## Stage 3

Figure out a points system.

For example:

- If you hit the target you get 100 points.
- Every move would cost 10 points.
- Every missed shot costs 20 points unless you hit.

Two suggestions how to end game:

- Sum up points and save the amount of points that was collected until 10 targets is shot.
- When you run out of points, show how much targets where destroyed.

Extra credit:

After the game is over, ask the player name and save the name and score to the file, and load that
data up whenever the user wants to see the top scores on the game.