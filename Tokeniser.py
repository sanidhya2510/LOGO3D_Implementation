import os
import sys

FORWARD = 'FORWARD'
BACKWARD = 'BACKWARD'
UP_ROTATION = 'UP-ROTATION'
DOWN_ROTATION = 'DOWN-ROTATION'
RIGHT_ROTATION = 'RIGHT-ROTATION'
LEFT_ROTATION = 'LEFT-ROTATION'
FLOATING_POINT = 'FLOATING-POINT'
LEFT_SQUARE_BRACKET = 'LEFT-SQUARE-BRACKET'
RIGHT_SQUARE_BRACKET = 'RIGHT-SQUARE-BRACKET'
EOF = 'EOF'
HOME = 'HOME'
PEN_UP = 'PEN-UP'
PEN_DOWN = 'PEN-DOWN'
REPEAT = 'REPEAT'

class Token():
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def __str__(self):
        return 'Token({type}, {value})'.format(
            type=self.type,
            value=repr(self.value)
        )

    def __repr__(self):
        return self.__str__()
    
class Lexer():
    
    def print_error(self):
        print("Lexical Error!")
        quit()
        
    def __init__(self, text, debug_mode):
        self.text = text
        self.index = 0
        self.curr_token = None
        self.curr_char = self.text[self.index]
        
    def next_char(self):
        self.index = self.index + 1
        if self.index > len(self.text) - 1:
            self.curr_char = None
        else:
            self.curr_char = self.text[self.index]
            
    def floating_point(self):
        result = ' '
        while self.curr_char is not None and self.curr_char >= '0' and self.curr_char <= '9':
            result = result + self.curr_char
            self.next_char()
        
        if self.curr_char == '.':
            result = result + self.curr_char
            self.next_char()
            while self.curr_char is not None and self.curr_char >= '0' and self.curr_char <= '9':
                result = result + self.curr_char
                self.next_char()
        return float(result)
    
    def forward(self):
        self.next_char()
        if self.curr_char == 'd':
            self.next_char()
            return "fd"
        self.print_error()
    
    def backward(self):
        self.next_char()
        if self.curr_char == 'k':
            self.next_char()
            return "bk"
        self.print_error()
        
    def turn1(self):
        result = self.curr_char
        self.next_char()
        if self.curr_char == 't':
            self.next_char()
            return result + 't'
        self.print_error()
    
    def home(self):
        result = self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        if result == "home":
            return "home"
        self.print_error()
    
    def penup(self):
        self.next_char()
        if self.curr_char == 'p':
            self.next_char()
            return "penup"
        self.print_error()
    
    def pendown(self):
        result = self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        if result == "down":
            return "pendown"
        self.print_error()
        
    
    def repeat(self):
        result = "re"
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        result = result + self.curr_char
        self.next_char()
        if result == "repeat":
            return "repeat"
        self.print_error()
                
    def get_next_token(self):
        while self.curr_char is not None:
            if self.curr_char == ' ' or self.curr_char == '\n':
                while self. curr_char is not None and (self. curr_char == ' ' or self.curr_char == '\n'):
                    self.next_char()
                continue
            
            if self.curr_char >= '0' and self.curr_char <= '9' or (self.curr_char == '.'):
                return Token(FLOATING_POINT, self.floating_point())
                
            
            if self.curr_char == 'f':
                return Token(FORWARD, self.forward())
            
            if self.curr_char == 'b':
                return Token(BACKWARD, self.backward())
            
            if self.curr_char == 'd':
                return Token(DOWN_ROTATION, self.turn1())

            if self.curr_char == 'u':
                return Token(UP_ROTATION, self.turn1())

            if self.curr_char == 'l':
                return Token(LEFT_ROTATION, self.turn1())
            
            if self.curr_char == 'h':
                return Token(HOME, self.home())
            
            if self.curr_char == 'p':
                self.next_char()
                if self.curr_char == 'e':
                    self.next_char()
                    if self.curr_char == 'n':
                        self.next_char()
                    else: 
                        self.print_error()
                else: 
                    self.print_error()                
                if self.curr_char == 'u':
                    return Token(PEN_UP, self.penup())
                elif self.curr_char == 'd':
                    return Token(PEN_DOWN, self.pendown())
                else:
                    self.print_error()
            
            if self.curr_char == 'r':
                self.next_char()
                if self.curr_char == 't':
                    self.next_char()
                    return Token(RIGHT_ROTATION, "rt")
                if self.curr_char == 'e':
                    return Token(REPEAT, self.repeat())
            if self. curr_char == '[':
                self.next_char()
                return Token(LEFT_SQUARE_BRACKET, '[')
            
            if self. curr_char == ']':
                self.next_char()
                return Token(RIGHT_SQUARE_BRACKET, ']')            
            
            self.print_error()
        
        return Token(EOF, None)
        

if __name__ == "__main__":
    lines = ""
    debug_mode = False
    with open("input.lgo") as f:
            lines = f.readlines()
    text = ''.join(lines)
    text = text.lower()
    lexer = Lexer(text, debug_mode)
    curr_token = lexer.get_next_token()
    while curr_token.type is not None:
        print(curr_token)
        curr_token = lexer.get_next_token()
    # print(lexer)
    # print(text)
