'''
      time: 2017-8-27 21:15:15
    author: AI
university: NCU
     intro: 一个简单的解释器，来源： http://blog.jobbole.com/88152/

- 2017-8-27 21:19:23
+ 简单的个位数加法实现

- 2017-8-29 16:55:52
+ 整数加法和减法实现

- 2017-8-30 02:52:51
+ 整数乘法和除法实现，可以过滤空格

- 2017-09-03 23:44:32
+ 修复上一功能完全不能运行的问题

- 2017-09-24 22:30:21
+ 添加括号支持

- 2017-09-26 10:21:33
+ 小数支持
+ 简单内置常量支持
+ 分割文件

- 2017-09-28 16:52:09
+ 函数调用的支持 （少于两位参数）

- 2017-10-03 14:40:40
+ 任意长度参数函数调用
'''
from lexer import *

        
class Interpreter(object):
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = None
        self.next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def next_token(self):
        self.current_token = self.lexer.get_next_token()
        return self.current_token

    def eatInt(self):
        # 将当前的token的type(self.current_token.type)与传进来的
        # type比较，如果两者相同，当前的token被使用掉(eat)并将下一个token
        # 赋值给current_token；否则抛出一个异常
        if self.current_token.type == INTEGER:
            self.next_token()
        else:
            self.error()
            
    def eatVar(self):
        if self.current_token.type == VAR:
             self.next_token()
        else:
            self.error()

    def eatOp(self,level):
        '''
            cosume a opeartor from tokens stream
        '''
        if self.current_token.type == OPERATOR:
            if (level == 0 and self.current_token.value == '^')\
            or (level == 1 and self.current_token.value in ['*','/'])\
            or (level == 2 and self.current_token.value in ['+','-']):
                self.next_token()
            else:     
                self.error()
        else:
            self.error()

    def func(self,func_var):
        func = func_var
        token = self.next_token()
        if token.type is RPAREN:
            return func()

        parlist = list()
        while True:
            parlist.append(self.expr())   
            token = self.current_token
            
            if token.type is COMMA:
                token = self.next_token()
            elif token.type is RPAREN:
                self.next_token()
                return func(*parlist)
                
                   
            
                

    def factor(self):
        '''factor : INTERGER'''
        token = self.current_token
        if token.type == INTEGER:
            self.eatInt()
            return token.value

        if token.type == VAR:
            self.eatVar()
            var = var_table.get(token.value)
            if self.current_token.type == LPAREN:
                return self.func(var)
            return 

        if token.type == LPAREN:
            self.next_token()
            result = self.expr()
            self.next_token()
            return result

    def pwrs(self):
        '''
         pwrs: factor((PWR) factor)*
        '''
        result = self.factor()
        while self.current_token.value is '^':
            self.eatOp(0)
            result = result ** self.pwrs()
        return result

    def term(self):
        '''
         term: pwrs((MUL | DIV) pwrs)*
        '''
        result = self.pwrs()
        
        
        while self.current_token.value in ['*','/']:
            token = self.current_token
            self.eatOp(1)
            if token.value == '*':
                result = result * self.pwrs()
            elif token.value == '/':
                result = result / self.pwrs()
        return result

    def expr(self):
        '''
            既做语法分析，又做解释过程
            expr -> INTEGER PLUS INTEGER
            语法分析(parsing)
            识别 token 流中的短语的过程称之为 parsing(语法分析)
             expr   : term ((PLUS | MINUS) term)*
            term   : factor ((MUL | DIV) factor)*
            factor : INTEGER
        '''
        # we expect the current token to be a single-digit integer
        result = self.term()
        
        while self.current_token.value in ['-','+']:
            op = self.current_token
            self.eatOp(2)
            # we expect the current token to be a single-digit integer
            right = self.term()
            if op.value == '+':
                result += right
            elif op.value == '-':
                result -= right
        return result

def main():
    while True:
        try:
            # To run under Python3 replace 'raw_input' call
            # with 'input'
            text = input('calc> ')
        except EOFError:
            break
        if not text:
            continue
        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)

if __name__ == '__main__':
    main()