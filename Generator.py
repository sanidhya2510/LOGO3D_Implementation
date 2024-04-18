from Parser import *
from Head import Head

def generate_moves(lexer, sequence, temp_sequence, head, debug_mode):
    token = lexer.get_next_token()
    while(token.type != EOF):
        if token.type == PEN_UP:
            head.pendown = False
            sequence.append(temp_sequence)
            temp_sequence = []
        elif token.type == PEN_DOWN:
            head.pendown = True
        elif token.type == HOME:
            head.x = 0
            head.y = 0
            head.horizontal_angle = 0
            head.vertical_angle = 0
        elif token.type == FORWARD:
            token = lexer.get_next_token()
            (x1, y1, z1) = (head.x, head.y, head.z)
            head.move(token.value)
            (x2, y2, z2) = (head.x, head.y, head.z)
            
            if head.pendown:
                temp_sequence.append((x1, y1, z1))
                temp_sequence.append((x2, y2, z2))
        
        elif token.type == BACKWARD:
            token = lexer.get_next_token()
            (x1, y1, z1) = (head.x, head.y, head.z)
            head.move(-token.value)
            (x2, y2, z2) = (head.x, head.y, head.z)
            
            if head.pendown:
                temp_sequence.append((x1, y1, z1))
                temp_sequence.append((x2, y2, z2))
        
        elif token.type == UP_ROTATION:
            token = lexer.get_next_token()
            head.vertical_turn(token.value)
        
        elif token.type == DOWN_ROTATION:
            token = lexer.get_next_token()
            head.vertical_turn(-token.value)
        
        elif token.type == LEFT_ROTATION:
            token = lexer.get_next_token()
            head.horizontal_turn(-token.value)
        
        elif token.type == RIGHT_ROTATION:
            token = lexer.get_next_token()
            head.horizontal_turn(token.value)
            
        elif token.type == REPEAT:
            token = lexer.get_next_token()
            count = token.value
            text = ''
            token = lexer.get_next_token()
            token = lexer.get_next_token()
            counter = 1
            while counter != 0:
                text = text + str(token.value)
                token = lexer.get_next_token()
                if token.type == LEFT_SQUARE_BRACKET: counter = counter + 1
                if token.type == RIGHT_SQUARE_BRACKET: counter = counter - 1
            # print(text)
            
            while count:
                new_lexer = Lexer(text, False)
                generate_moves(new_lexer, sequence, temp_sequence, head, debug_mode)
                count = count - 1
        token = lexer.get_next_token()

def generate(lexer, debug_mode):
    head = Head()
    sequence = []
    temp_sequence = []
    generate_moves(lexer, sequence, temp_sequence, head, debug_mode)
    sequence.append(temp_sequence)
    
    return sequence

if __name__ == "__main__":
    lines = ""
    debug_mode = False
    with open("input.lgo") as f:
            lines = f.readlines()
    text = ''.join(lines)
    text = text.lower()
    lexer = Lexer(text, debug_mode)
    lexer2 = Lexer(text, debug_mode)
    lexer3 = Lexer(text, debug_mode)
    parser = Parser(lexer)
    parser.parse()
    curr_token = lexer2.get_next_token()
    while curr_token.type is not EOF:
        print(curr_token)
        curr_token = lexer2.get_next_token()
    sequence = generate(lexer3, debug_mode)
    print(sequence)
    print(len(sequence[0]))
            