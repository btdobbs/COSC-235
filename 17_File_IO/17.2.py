import uuid


def copy_file(src_filename, tgt_filename):
    source_file = open(src_filename, 'r')
    target_file = open(tgt_filename, 'w')
    source_data = source_file.read()
    target_file.write(source_data)
    source_file.close()
    target_file.close()


def main():
    data_filename = input('Enter the file name: ').strip()
    copy_file(data_filename, data_filename + "-" + str(uuid.uuid1()))


main()
