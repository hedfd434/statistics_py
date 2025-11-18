import math

# def range(data):
#     min_val = min(data)
#     max_val = max(data)
#     return [min_val, max_val, abs(max_val - min_val)]

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

def weighted_mean(list):
    #first row are values, seconds row ale assigned weighths

    if(len(list[0]) == len(list[1])):
        #calculate the top sum
        top_sum = 0
        for i in range(len(list[0])):
            top_sum += list[0][i] * list[1][i]

        #calulate the bottom sum
        bottom_sum = 0
        for n in range(len(list[1])):
            bottom_sum += list[1][n]

        print(top_sum, ", ", bottom_sum)

        return top_sum / bottom_sum
    return None

def variation(data):
    avg = arithemtic_mean(data)
    top_sum = 0
    for k in range(len(data)):
        top_sum += math.pow(data[k], 2)

    return (top_sum / len(data)) - pow(avg, 2)

def standard_deviation(data):
    var = variation(data)
    # max(0, var) for return to make sure that there will not be a aquare of negative value
    return max(math.sqrt(var), 0)

def average_absolute_deviation(data):
    avg = arithemtic_mean(data)

    top_sum = 0
    for k in range(len(data)):
        top_sum += abs((data[k] - avg))

    return top_sum / len(data)

def correlation(data):
    # uses 2d array
    x_mean = arithemtic_mean(data[0])
    y_mean = arithemtic_mean(data[1])

    top_sum = 0
    for k in range(len(data[0])):
        top_sum += ((data[0][k]) - x_mean) * (data[1][k] - y_mean)
    
    bottom_x_square = 0
    for z in range(len(data[0])):
        bottom_x_square += math.pow((data[0][z] - x_mean), 2)
    
    bottom_x_square = math.sqrt(bottom_x_square)

    bottom_y_square = 0
    for z in range(len(data[1])):
        bottom_y_square += math.pow((data[1][z] - y_mean), 2)
    bottom_y_square = math.sqrt(bottom_y_square)

    bottom_product = bottom_x_square * bottom_y_square

    return top_sum / bottom_product
    print(x_mean, y_mean)

    return None

#next relations
def test_function():
    print("test")
    return None
    
if __name__ == "__main__":
    print("test")

    list = [4, 9, 11, 13, 13]

    list_2 = [
        [10, 25, 5, 40, 15],          # Row 1: Values
        [1, 2, 3, 4, 5]   # Row 2: Weights
    ]

    list_3 = [
        [1, 2, 3, 4, 5], # x 
        [10, 25, 5, 40, 15], # y

    ]

    # print("range = ", range(list))

    print("arithmetic mean = ", arithemtic_mean(list))

    print("median = ", median(list))

    print("weighted mean = ", weighted_mean(list_2))

    print("variance = ", variation(list))

    print("standard deviation = ", standard_deviation(list))

    print("average absolute deviation = ", average_absolute_deviation(list))

    print(correlation(list_3))