import pygame as pg
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from Tokeniser import *
from Parser import *
from Generator import *

def usage():
    print("Usage:")
    print("python Logo3D.py source-file [options]")
    print("       [options] - /r a:x:y:z (rotate at angle 'a' around '(x,y,z)')")
    print("                              (defaults to 1:1:1:1)")
    print()
    print("e.g. python Logo3D.py cude.lgo")
    os._exit(0)

def read_from_file(filename):
    try:
        with open(filename) as f:
            lines = f.readlines()
            return " ".join(lines)
    except:
        print(f"Unable to read from file {filename}")
        os._exit(1)

def parse_args(argv):
    if (len(argv) < 2):
        usage()
    filename = argv[1]
    (rot_angle, rot_x, rot_y, rot_z) = (1, 1, 1, 1)

    i = 2
    while (i < len(argv)):
        if (argv[i] == "/r"):
            i += 1
            if (i == len(argv)):
                print("Expected additional value after '/r'")
                os._exit(1);
            vals = argv[i].split(":")
            if (len(vals) != 4):
                print("Expected additional value after '/r' in the form 'a:x:y:z'")
            try:
                rot_angle = float(vals[0])
                rot_x = float(vals[1])
                rot_y = float(vals[2])
                rot_z = float(vals[3])
            except:
                print(f"Problem parsing {argv[i]}")
                os._exit(1)

        else:
            print(f"{argv[i]} is an unknown parameter")
            os._exit(1)
        i += 1
    return (filename, (rot_angle, rot_x, rot_y, rot_z))

def main():
    (filename, (rot_angle, rot_x, rot_y, rot_z)) = parse_args(sys.argv)
    text = read_from_file(filename)
    text = ' '.join(text.split())
    lexer = Lexer(text)
    
    test_lexer = Lexer(text)
    curr_token = test_lexer.get_next_token()
    
    print("Tokens are as follows:")
    while curr_token.type is not EOF:
        print(curr_token)
        curr_token = test_lexer.get_next_token()
        
    parser = Parser(lexer)
    parser.parse()
    get_tokens = Lexer(text)
    all_pos_sequences = generate(get_tokens)
    pg.init()
    display = (1300, 800)
    pg.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    perspective = -10
    glTranslatef(0.0, 0.0, perspective)

    (x, y, z) = (0, 0, 0)
    rotate = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                return
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    return
                elif event.key == pg.K_RIGHT:
                    x = 0.1
                elif event.key == pg.K_LEFT:
                    x = -0.1
                elif event.key == pg.K_UP:
                    y = 0.1
                elif event.key == pg.K_DOWN:
                    y = -0.1
                elif event.key == pg.K_EQUALS:
                    z = 0.1
                elif event.key == pg.K_MINUS:
                    z = -0.1
                elif event.key == pg.K_SPACE:
                    rotate = not rotate
            elif event.type == pg.KEYUP:
                if event.key == pg.K_RIGHT and x > 0:
                    x = 0
                elif event.key == pg.K_LEFT and x < 0:
                    x = 0
                elif event.key == pg.K_UP and y > 0:
                    y = 0
                elif event.key == pg.K_DOWN and y < 0:
                    y = 0
                elif event.key == pg.K_EQUALS and z > 0:
                    z = 0
                elif event.key == pg.K_MINUS and z < 0:
                    z = 0


        if (rotate):
            glRotatef(rot_angle, rot_x, rot_y, rot_z)

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    
        glBegin(GL_LINES)    
        for pos_seq in all_pos_sequences:
            for pos in pos_seq:
                glVertex3fv(pos)
        glEnd()

        glTranslatef(x, y, z)

        pg.display.flip()
        pg.time.wait(1)

if __name__ == "__main__":
    main()
