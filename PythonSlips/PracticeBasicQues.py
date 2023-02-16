class PracticeQues:
    def __init__(self, str):
        self.str = str

    def count_no_chars(self):
        my_dict = {}
        for ch in str:
            keys = my_dict.keys()
            if ch in keys:
                my_dict[ch] += 1
            else:
                my_dict[ch] = 1
        return my_dict


my_dict = {'c': 3, 'f': 5}
keys = my_dict.keys()
print(keys)

