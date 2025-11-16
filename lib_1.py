import math
def arithemtic_mean(data):
    #print("data type", type(data))
    return sum(data) / len(data)

def median(data):
    buff_data = data
    
    buff_data.sort()

    print("buf data = ", buff_data)

    if(len(buff_data) % 2 == 0):
        return (buff_data[math.floor(len( buff_data) / 2) - 1] +  buff_data[math.floor(len(buff_data) / 2)]) / 2
    if(len(buff_data) % 2 == 1):
        return  buff_data[math.floor(len(buff_data) / 2)]
    
    return None

def Mode(data):
    buff_array = [0] * len(data) * 10

    for i in range(len(data)):
        buff_array[data[i] - 1] += 1

    # use dictionary
    print(buff_array)
    return None

def test_function():
    print("test")
    
if __name__ == "__main__":
    pass