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
    data_buf = []
    data_buf = data.copy()
    values = []
    max_occurence = 0

    for i in range(len(data)):
        if(len(data_buf) > 0):
            value_buffer = data_buf[0]

            if(data_buf.count(value_buffer) > max_occurence):
                values.clear()
                max_occurence = data_buf.count(value_buffer)
                values.append(value_buffer)
                for n in range(max_occurence):
                    data_buf.remove(value_buffer)

            elif(data_buf.count(value_buffer) == max_occurence):
                values.append(value_buffer)
                for n in range(data_buf.count(value_buffer)):
                    data_buf.remove(value_buffer)

            else:
                for n in range(data_buf.count(value_buffer)):
                    data_buf.remove(value_buffer)

        else:
            return values
                

    return None

def test_function():
    print("test")
    
if __name__ == "__main__":
    pass