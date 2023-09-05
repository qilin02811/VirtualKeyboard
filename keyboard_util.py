# keyboard_util.py
from singleton_util import singleton


@singleton
class KeyBoardUtil(object):
    def __init__(self):
        super().__init__()
        self.all_char = [[]]
        self.lower_to_upper = {}
        self.upper_to_lower = {}

    def get_normal_all(self):
        line1 = [
            '`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<-'
        ]
        line2 = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\'
        ]
        line3 = [
            'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', '\'', 'close'
        ]
        line4 = [
            'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', 'shift', 'clear'
        ]
        self.all_char = [line1, line2, line3, line4]
        return self.all_char

    def get_shift_all(self):
        line1 = [
            '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '<-'
        ]
        line2 = [
            'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'
        ]
        line3 = [
            'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '\"', 'close'
        ]
        line4 = [
            'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?', 'shift', 'clear'
        ]
        self.all_char = [line1, line2, line3, line4]
        return self.all_char

    def get_lower_to_upper_dict(self):
        normal_chars = self.get_normal_all()
        shift_chars = self.get_shift_all()
        for i in range(len(normal_chars)):
            for j in range(len(normal_chars[i])):
                self.lower_to_upper[normal_chars[i][j]] = shift_chars[i][j]
        return self.lower_to_upper

    def get_upper_to_lower_dict(self):
        normal_chars = self.get_normal_all()
        shift_chars = self.get_shift_all()
        for i in range(len(normal_chars)):
            for j in range(len(normal_chars[i])):
                self.upper_to_lower[shift_chars[i][j]] = normal_chars[i][j]
        return self.upper_to_lower

