from abc import ABCMeta, abstractmethod
import re
whitespace_regex = re.compile(r'\s+')


class Validator(metaclass=ABCMeta):
    @abstractmethod
    def validate(self, string):
        pass


class TrailingWhitespaceValidator(Validator):
    def validate(self, string):
        lines = string.splitlines()
        valid_string = ''
        for line in lines:
            if line[-1] is ' ':
                line = line[:-1]
            valid_string += line + '\n'
        return valid_string


class BlankLineValidator(Validator):
    def validate(self, string):
        lines = string.splitlines()
        for i in range(len(lines), 0, -1):
            if whitespace_regex.fullmatch(lines[-1]):
                lines.pop()
            else:
                break
        if lines[-1] is not '':
            lines.append('')
        valid_string = ''
        for line in lines:
            valid_string += line + '\n'
        return valid_string
