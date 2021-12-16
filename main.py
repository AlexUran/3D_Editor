import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def draw_cube():
    p = [
        (1, 1, -1),
        (1, -1, -1),
        (-1, -1, -1),
        (-1, 1, -1),
        (1, 1, 1),
        (1, -1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
    ]
    edges = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 0),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 4),
        (0, 4),
        (1, 5),
        (2, 6),
        (3, 7),
    ]
    glBegin(GL_LINES)
    glVertex3fv((0, 0, 0))
    glVertex3fv((2, 0, 0))
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 2, 0))
    glVertex3fv((0, 0, 0))
    glVertex3fv((0, 0, 2))
    for edge in edges:
        glVertex3fv(p[edge[0]])
        glVertex3fv(p[edge[1]])
    glEnd()

def main():
    pg.init()
    display = (800, 600)
    pg.display.set_mode(display, DOUBLEBUF | OPENGL)
    clock = pg.time.Clock()

    gluPerspective(45, display[0] / display[1], 0.1, 50.0)

    glTranslatef(0, 0, -10)

    run = True
    while run:
        clock.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        glRotate(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_cube()
        pg.display.flip()


if __name__ == '__main__':
    main()