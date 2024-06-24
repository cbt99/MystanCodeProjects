"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

This file includes the animations for the game. Users can play the breakout game here with
three lives. If the ball falls out the bottom of the window, the user will lose one life.
If the ball collides with a brick, the user gets one point, with 100 as the highest possible score.
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.create_score_label()
    score = 0
    while True:
        pause(FRAME_RATE)
        if lives > 0 and score != graphics.total:
            if graphics.started:
                # Add the animation loop here!
                graphics.started = False
                vx = graphics.get_vx()
                vy = graphics.get_vy()
                while True:
                    graphics.ball.move(vx, vy)
                    if graphics.ball.y <= 0:
                        vy = -vy
                    elif graphics.ball.y+graphics.ball.height >= graphics.window.height:
                        lives -= 1
                        graphics.ball.x = graphics.window.width/2-graphics.ball.width/2
                        graphics.ball.y = graphics.window.height/2-graphics.ball.height/2
                        graphics.set_vx()
                        break
                    elif graphics.ball.x <= 0:
                        vx = -vx
                    elif graphics.ball.x+graphics.ball.width >= graphics.window.width:
                        vx = -vx
                    maybe_object_ll = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
                    if maybe_object_ll is graphics.paddle:
                        vy = -graphics.INITIAL_Y_SPEED
                    elif maybe_object_ll is not None and maybe_object_ll is not graphics.paddle and maybe_object_ll is not graphics.score_label:
                        vy = -vy
                        graphics.window.remove(maybe_object_ll)
                        score += 1
                        graphics.score_label.text = 'Score: ' + str(score)
                    else:
                        maybe_object_lr = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)
                        if maybe_object_lr is graphics.paddle:
                            vy = -graphics.INITIAL_Y_SPEED
                        elif maybe_object_lr is not None and maybe_object_lr is not graphics.paddle and maybe_object_lr is not graphics.score_label:
                            vy = -vy
                            graphics.window.remove(maybe_object_lr)
                            score += 1
                            graphics.score_label.text = 'Score: ' + str(score)
                        else:
                            maybe_object_ul = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
                            if maybe_object_ul is not None and maybe_object_ul is not graphics.paddle and maybe_object_ul is not graphics.score_label:
                                vy = -vy
                                graphics.window.remove(maybe_object_ul)
                                score += 1
                                graphics.score_label.text = 'Score: ' + str(score)
                            else:
                                maybe_object_ur = graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
                                if maybe_object_ur is not None and maybe_object_ur is not graphics.paddle and maybe_object_ur is not graphics.score_label:
                                    vy = -vy
                                    graphics.window.remove(maybe_object_ur)
                                    score += 1
                                    graphics.score_label.text = 'Score: ' + str(score)
                    pause(FRAME_RATE)
                    if score == graphics.total:
                        graphics.window.clear()
                        graphics.you_win()
                        break
        else:
            if lives == 0 and score != graphics.total:
                graphics.window.clear()
                graphics.try_again()
            break


if __name__ == '__main__':
    main()
