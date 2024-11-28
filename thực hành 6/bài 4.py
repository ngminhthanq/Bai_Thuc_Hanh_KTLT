class ReverseString:
    def __init__(self, input_string):
        self.input_string = input_string

    def reverse_words(self):
        return ' '.join(self.input_string.split()[::-1])

input_data = "hello .py"

reverser = ReverseString(input_data)
output = reverser.reverse_words()

print("Đầu ra:", output)
