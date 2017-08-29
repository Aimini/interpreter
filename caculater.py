'''
      time: 2017-8-27 21:15:15
    author: AI
university: NCU
     intro: 一个简单的解释器，来源： http://blog.jobbole.com/88152/

- 2017-8-27 21:19:23
+ 简单的个位数加法实现
'''

INTEGER, OP, EOF = 'INTEGER', 'OP', 'EOF'


class Token(object):
    '''标记 类

        标记是组成表达式的基本单元
        一个标记可以是数字，也可以是操作符（从广泛的范围来讲，操作符属于函数的一个子集）
    '''
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __str__(self):
        '''String representation of the class instance.abs
            "类的实例的字符串表示"

            Examples:
                Token(INTEGER, 3)
                TOKen(PLUS, '+')
        '''
        #repr() 将值转化为供解释器读取的形式的字符串
        return ('Token({type}, {value}').format(type = self.type,value = repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    '''解释器 类
    '''
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('Error parsing input')

    def get_next_token(self):
        '''Lexical analyzer (also know as scanner or tokenizer)

        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        '''

        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)


        current_char = text[self.pos]
        while current_char == ' ' and self.pos < len(text):
            current_char = text[self.pos]
            if self.pos < len(text):
                current_char = text[self.pos]
            else:
                break
           

        #如果当前字符串是数字
        number_str = ''
        while current_char.isdigit():
            number_str += current_char
            self.pos += 1
            if self.pos < len(text):
                current_char = text[self.pos]
            else:
                break         
        if number_str is not '':
            token = Token(INTEGER, int(number_str))
            return token

        #如果当前字符串是加号
        if current_char in ['+','-'] :
            token = Token(OP, current_char)
            self.pos += 1
            return token

        self.error()


    def eat(self, token_type):
        # 将当前的token的type(self.current_token.type)与传进来的
        # type比较，如果两者相同，当前的token被使用掉(eat)并将下一个token
        # 赋值给current_token；否则抛出一个异常
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        '''expr -> INTEGER PLUS INTEGER'''
        # set current token to the first token taken from the input
        self.current_token = self.get_next_token()

        # we expect the current token to be a single-digit integer
        left = self.current_token
        self.eat(INTEGER)

        # we expect the current token to be a '+' token
        op = self.current_token
        self.eat(OP)

        # we expect the current token to be a single-digit integer
        right = self.current_token
        self.eat(INTEGER)
        # after the above call the self.current_token is set to
        # EOF token

        # at this point INTEGER PLUS INTEGER sequence of tokens
        # has been successfully found and the method can just
        # return the result of adding two integers, thus
        # effectively interpreting client input
        result = None
        if op.value == '+':
            result = left.value + right.value
        if op.value == '-':
            result = left.value - right.value
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
            interpreter = Interpreter(text)
            result = interpreter.expr()
            print(result)
 
if __name__ == '__main__':
    main()