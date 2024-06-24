"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

This file creates the class, BreakoutGraphics.
Users can run the default of BreakoutGraphics in breakout.py.
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.paddle_offset = paddle_offset
        self.started = False
        self.total = brick_rows*brick_cols
        self.score_label = None
        self.INITIAL_Y_SPEED = INITIAL_Y_SPEED

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=self.window.width/2-self.paddle.width/2, y=self.window.height-paddle_offset-self.paddle.height)

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width/2-self.ball.width/2, y=self.window.height/2-self.ball.height/2)

        # Default initial velocity for the ball
        self._vx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self._vx = -self._vx
        self._vy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        onmouseclicked(self.ball_move)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(BRICK_ROWS):
            for j in range(BRICK_COLS):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                if i == 0 or i == 1:
                    self.brick.fill_color = 'red'
                    self.brick.color = 'red'
                if i == 2 or i == 3:
                    self.brick.fill_color = 'orange'
                    self.brick.color = 'orange'
                if i == 4 or i == 5:
                    self.brick.fill_color = 'yellow'
                    self.brick.color = 'yellow'
                if i == 6 or i == 7:
                    self.brick.fill_color = 'green'
                    self.brick.color = 'green'
                if i == 8 or i == 9:
                    self.brick.fill_color = 'blue'
                    self.brick.color = 'blue'
                self.window.add(self.brick, x=j*brick_width+j*brick_spacing, y=brick_offset+i*brick_height+i*brick_spacing)

    def move_paddle(self, event):    # cannot be above "draw bricks"
        if event.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif event.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = event.x-self.paddle.width/2

    def get_vx(self):
        return self._vx

    def get_vy(self):
        return self._vy

    def ball_move(self, event):
        if self.ball.x == self.window.width/2-self.ball.width/2 and self.ball.y == self.window.height/2-self.ball.height/2:
            self.started = True

    def set_vx(self):
        self._vx = random.randint(1, MAX_X_SPEED)
        if random.random() < 0.5:
            self._vx = -self._vx

    def you_win(self):
        win_label = GLabel('You win!')
        win_label.color = 'magenta'
        win_label.font = '-30'
        self.window.add(win_label, x=self.window.width/2-win_label.width/2, y=self.window.height/2-win_label.height/2)

    def try_again(self):
        try_again = GLabel('Try again!')
        try_again.color = 'magenta'
        try_again.font = '-30'
        self.window.add(try_again, x=self.window.width/2-try_again.width/2, y=self.window.height/2-try_again.height/2)

    def create_score_label(self):
        score_label = GLabel('Score: 0')
        score_label.color = 'magenta'
        score_label.font = '-30'
        self.window.add(score_label, x=0, y=self.window.height)
        self.score_label = score_label
