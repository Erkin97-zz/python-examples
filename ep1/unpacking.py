my_tuple = (32, 412, 12)
my_list = [12, 1, "Erkin"]
my_string = "abcd"
# let's unpack
# number of variables equal to size of sequence
(a, be, c) = my_tuple
print(a, be, c)
(a, b, c) = my_list
print(a, b, c)
(a, b, c, d) = my_string
print(a, b, c, d)