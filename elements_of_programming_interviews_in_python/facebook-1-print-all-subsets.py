# Create a function that prints all subsets of a set

S = {1,2,3,4}
def get_binary_string(n, padding_length):

    string = str(bin(n))[2:]

    padding_length = num - len(string)


    return padding_length * "0" + string



def get_subsets(S):
    n = len(S)
    for i in range(2**n):

        pad_string()

        print(get_binary_string(i,n))

get_binary_string(12, 5):
