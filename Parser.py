from Tokeniser import *
import copy
#parsing table -> ll(1)

parsing_table = dict()

parsing_table[("S", FORWARD)] = ("S", [FORWARD, "K", "S"])
parsing_table[("S", BACKWARD)] = ("S", [BACKWARD, "K", "S"])
parsing_table[("S", UP_ROTATION)] = ("S", [UP_ROTATION, "K", "S"])
parsing_table[("S", DOWN_ROTATION)] = ("S", [DOWN_ROTATION, "K", "S"])
parsing_table[("S", RIGHT_ROTATION)] = ("S", [RIGHT_ROTATION, "K", "S"])
parsing_table[("S", LEFT_ROTATION)] = ("S", [LEFT_ROTATION, "K", "S"])
parsing_table[("S", FLOATING_POINT)] = None
parsing_table[("S", LEFT_SQUARE_BRACKET)] = None
parsing_table[("S", RIGHT_SQUARE_BRACKET)] = ("S", [])
parsing_table[("S", EOF)] = ("S", [EOF])
parsing_table[("S", HOME)] = ("S", [HOME, "S"])
parsing_table[("S", PEN_UP)] = ("S", [PEN_UP, "S"])
parsing_table[("S", PEN_DOWN)] = ("S", [PEN_DOWN, "S"])
parsing_table[("S", REPEAT)] = ("S", [REPEAT, "K", LEFT_SQUARE_BRACKET, "S", RIGHT_SQUARE_BRACKET, "S"])

parsing_table[("K", FORWARD)] = None
parsing_table[("K", BACKWARD)] = None
parsing_table[("K", UP_ROTATION)] = None
parsing_table[("K", DOWN_ROTATION)] = None
parsing_table[("K", RIGHT_ROTATION)] = None
parsing_table[("K", LEFT_ROTATION)] = None
parsing_table[("K", FLOATING_POINT)] = ("K", [FLOATING_POINT])
parsing_table[("K", LEFT_SQUARE_BRACKET)] = None
parsing_table[("K", RIGHT_SQUARE_BRACKET)] = None
parsing_table[("K", EOF)] = None
parsing_table[("K", HOME)] = None
parsing_table[("K", PEN_UP)] = None
parsing_table[("K", PEN_DOWN)] = None
parsing_table[("K", REPEAT)] = None

class Stack:
    def __init__(self):
        self.list = []
        
    def push(self, value):
        self.list.append(value)
    
    def pop(self):
        self.list.pop()
    
    def peek(self):
        if len(self.list) >= 1:
            return self.list[-1]
        return None
    
    # def is_empty(self):
    #     if len(self.list) == 0:
    #         return True
    #     return False
    

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.curr_token = self.lexer.get_next_token()
        
    def syntax_error(self):
        print("Syntax Error!")
        quit()
    
    def parse(self):
        stack = Stack()
        stack.push("S")
        # self.curr_token = self.lexer.get_next_token()
        # print(self.curr_token.type)
        while not (stack.peek() == EOF and self.curr_token.type == EOF):
            # stack2 = copy.deepcopy(stack)
            # while stack2.peek() != None:
            #     print(stack2.peek(), end = " ")
            #     stack2.pop()
            # print()
            if stack.peek() == "S":
                if parsing_table[("S", self.curr_token.type)] is not None:
                    stack.pop()
                    for i in parsing_table[("S", self.curr_token.type)][1][::-1]:
                            stack.push(i)
                else: self.syntax_error()

            elif stack.peek() == "K":
                if parsing_table[("K", self.curr_token.type)] is not None:
                    stack.pop()
                    for i in parsing_table[("K", self.curr_token.type)][1][::-1]:
                        stack.push(i)
                else: self.syntax_error()
                
            else:
                if stack.peek() == self.curr_token.type:
                    stack.pop()
                    self.curr_token = self.lexer.get_next_token()
                else: self.syntax_error()
            
        print("Syntax is correct!")
            
            

if __name__ == "__main__":
    # print(parsing_table[("S", FORWARD)][1][1])
    lines = ""
    with open("input.lgo") as f:
            lines = f.readlines()
    text = ''.join(lines)
    text = text.lower()
    lexer = Lexer(text)
    lexer2 = Lexer(text)
    curr_token = lexer2.get_next_token()
    while curr_token.type is not EOF:
        print(curr_token)
        curr_token = lexer2.get_next_token()
    parser = Parser(lexer)
    parser.parse()
                
                
                

