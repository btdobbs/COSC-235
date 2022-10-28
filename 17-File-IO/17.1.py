def bmi(height, weight):
    return (703. * weight) / height ** 2


def process_bmi_data(filename):
    input_file = open(filename, 'r')
    for line in input_file:
        bmi_data = line.split(" ")
        id_number = bmi_data[0]
        height = float(bmi_data[1])
        weight = float(bmi_data[2])
        a_bmi = bmi(height, weight)
        print(id_number, ": ", round(a_bmi, 1), sep="")
    input_file.close()


def main():
    data_filename = input('Enter the file name: ').strip()
    process_bmi_data(data_filename)


main()
