#################################
# time:2017-09-26 10:21:13
# author:AI
# note: Lexer class.
#################################
from Token import *

class Lexer(object):
    
    '''解释器 类
    '''
    def __init__(self,text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]
        self.token_list = list()
        self.current_token_pos = -1
        

    def error(self,information):
        indicator = '^';
        for i in range(self.pos + 1):
            indicator = ' ' + indicator;
        except_text = ('at {index}:\n {text}\n{indicator}\n{info}').format(index = self.pos,text = self.text,indicator = indicator,info = information)
        raise Exception(except_text)

    def __advance__(self):
        '''Advance the 'pos' and set current char'''
        self.pos += 1
        if self.pos < len(self.text):
            self.current_char = self.text[self.pos]
        else:
            self.current_char = None



    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.__advance__()



    def var(self):
        var_name = ''
        if self.current_char is not None and(self.current_char.isalpha() or self.current_char in [ '_' , '$']):
            var_name += self.current_char
            self.__advance__()

        while self.current_char is not None and(self.current_char.isalnum() or self.current_char in [ '_' , '$']):
            var_name += self.current_char
            self.__advance__()
        return var_name



    def number(self):
        '''return a (multidigit) integer consumed from the input'''
        num_str = ''
        dot_count = 0
        while self.current_char is not None:
            if self.current_char.isdigit():
                num_str += self.current_char
            elif self.current_char == '.' :
                if dot_count > 0:
                    self.error("redundant decimal point")
                num_str += self.current_char
                dot_count += 1
            else:
                break
            self.__advance__()
        return float(num_str)


    def __get_next_token(self):
        '''Lexical analyzer (also know as scanner or tokenizer)
        词法分析器（也叫做 扫描程序 或 分词器）
        This method is responsible for breaking a sentence
        apart into tokens. One token at a time.
        该方法负责将句子分割成标记。一次分割出一个
        '''
        #lexeme是组token的字符序列，如加法token对应的lexeme就是‘+’
        if self.current_char is None:
            return Token(EOF, None)
        self.skip_whitespace()#skip wihte space

        if self.current_char.isdigit():
            return Token(INTEGER,self.number())

        if self.current_char.isalpha() or self.current_char in [ '_' , '$']:
            return Token(VAR,self.var())

        if self.current_char in ['+','-','*','/','^','=']:
            temp_token = Token(OPERATOR, self.current_char)
            self.__advance__()
            return temp_token

        if self.current_char == "(":
            temp_token = Token(LPAREN,'(')
            self.__advance__()
            return temp_token

        if self.current_char == ")":
            temp_token = Token(RPAREN,')')
            self.__advance__()
            return temp_token

        if self.current_char == ",":
            temp_token = Token(COMMA,',')
            self.__advance__()
            return temp_token
        
        self.error("unrecognizable marks")



    def get_prevn_token(self,n):
        self.current_token_pos -= n
        if self.current_token_pos < 0:
            return Token(EOF,None)
        return self.token_list[self.current_token_pos]



    def get_prev_token(self):
        return self.get_prevn_token(1)


    def get_next_token(self):
        self.current_token_pos += 1
        try:
            return self.token_list[self.current_token_pos]
        except IndexError:
            if len(self.token_list) > 0 and self.token_list[-1].type is EOF:
                return self.token_list[-1]
            self.token_list.append(self.__get_next_token())
            return self.token_list[self.current_token_pos]

        
if __name__  =='__main__' :
    l = Lexer("2.3 + 8")
    print(l.get_next_token())