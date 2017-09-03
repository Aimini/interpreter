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
'''

INTEGER = 'INTEGER'
OPERATOR = 'OPERATOR'
EOF = 'EOF'


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
        return ('Token({type}, {value})').format(type = self.type,value = repr(self.value))

    def __repr__(self):
        return self.__str__()

class Interpreter(object):
    '''解释器 类
    '''
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('Error parsing input')

    def advance(self):
        '''Advance the 'pos' and set current char'''
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        '''return a (multidigit) integer consumed from the input'''
        num_str = ''
        while self.current_char is not None and self.current_char.isdigit():
            num_str += self.current_char
            self.advance()
        return int(num_str)
        
    def get_next_token(self):
        '''Lexical analyzer (also know as scanner or tokenizer)
        词法分析器（也叫做 扫描程序 或 分词器）
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        该方法负责将句子分割成标记。一次分割出一个
        '''
        #lexeme是组token的字符序列，如加法token对应的lexeme就是‘+’
        if self.current_char is None:
            return Token(EOF, None)

        if self.current_char.isspace():
            self.skip_whitespace()

        if self.current_char.isdigit():
            return Token(INTEGER,self.integer())
        
        if self.current_char in ['+','-','*','/','^']:
            temp_token = Token(OPERATOR, self.current_char)
            self.advance()
            return temp_token
        self.error()
        

    def eat(self, token_type):
        # 将当前的token的type(self.current_token.type)与传进来的
        # type比较，如果两者相同，当前的token被使用掉(eat)并将下一个token
        # 赋值给current_token；否则抛出一个异常
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()
    def term(self):
        '''
         获取一个项
         return an INTEGER token value
        '''
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        '''
            既做语法分析，又做解释过程
            expr -> INTEGER PLUS INTEGER
            语法分析(parsing)
            识别 token 流中的短语的过程称之为 parsing(语法分析)
        '''
        # we expect the current token to be a single-digit integer
        self.current_token = self.get_next_token()
        result = self.term()
        while self.current_token.type is not EOF:
            op = self.current_token
            if op.type == OPERATOR:
                self.eat(OPERATOR)
                # we expect the current token to be a single-digit integer
                right = self.term()
                if op.value == '+':
                    result += right
                elif op.value == '-':
                    result -= right
                elif op.value == '*':
                    result *= right
                elif op.value == '/':
                   result /= right
                elif op.value == '^':
                    result = result ** right
        
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