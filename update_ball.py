
## Returns a tuple of current x, y and ball direction
def update_ball_info(ball_x_y: tuple, ball_direction: tuple, SCREEN_WIDTH: int, SCREEN_HEIGHT: int):
    new_x_y_for_ball = list(ball_x_y)
    new_ball_direction = list(ball_direction)

    print ('update_ball_info: ball_x_y, ball_direction', ball_x_y, ball_direction)

    ## See this page for adding two tuples
    ## https://stackoverflow.com/questions/1169725/adding-values-from-tuples-of-same-length
    new_x_y_for_ball = [ sum(x) for x in zip(ball_x_y, ball_direction) ]

    ## If the x goes outside of the area, then stop it, and change direction.
    if new_x_y_for_ball[0] >= SCREEN_WIDTH or new_x_y_for_ball[0] <= 0:
        new_x_y_for_ball[0] = ball_x_y[0]
        new_ball_direction[0]  = ball_direction[0] * -1

    if new_x_y_for_ball[1] >= SCREEN_HEIGHT or new_x_y_for_ball[1] <= 0:
        new_x_y_for_ball[1] = SCREEN_HEIGHT
        new_ball_direction[1]  = ball_direction[1] * -1

    return (tuple(new_x_y_for_ball), tuple(new_ball_direction))