#################################
# time:2017-09-25 18:52:20
# author:AI
# note: token class.
#################################
INTEGER = 'INTEGER'
OPERATOR = 'OPERATOR'
EOF = 'EOF'
LPAREN = '('
RPAREN = ')'
VAR = 'VAR'

var_table = {'a' : 0, 'b' : 1 ,'c': 3,'PI':3.141592654}


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