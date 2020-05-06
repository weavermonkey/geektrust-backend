def read_input_file(file_path):
    with open(file_path,'r') as inp_file:
        messages_sequence = inp_file.read().splitlines()
    return messages_sequence