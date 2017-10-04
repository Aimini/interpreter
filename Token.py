#################################
# time:2017-09-25 18:52:20
# author:AI
# note: token class.
#
# time:2017-09-28 16:51:34
# + 数学常量和三角函数以及一个自定义函数
#################################

import math
import decimal

INTEGER = 'INTEGER'
OPERATOR = 'OPERATOR'
EOF = 'EOF'
LPAREN = '('
RPAREN = ')'
VAR = 'VAR'
COMMA = 'COMMA'
def info():
    print("create by AI, 2017-09-28 16:25:35,NCU.")

var_table = {'sin' : math.sin, 'cos' : math.cos ,'info': info,'PI':math.pi,"E":math.e,'pow':math.pow,}




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

if __name__  =='__main__' :
    print(Token(INTEGER,23))
    print(Token(VAR,'PI'))
    print(Token(VAR,info))
