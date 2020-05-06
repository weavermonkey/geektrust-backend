import sys
from define_kingdom import Kingdom
from utils_input_output import read_input_file
from message import TransmitMessage
from check_allegiance import CheckAllegiance


def main():
    input_file = sys.argv[1]
    input_sequence = read_input_file(input_file)
    allies_list = []
    for curr_line in input_sequence:
        curr_sequence = curr_line.split(' ')
        curr_kingdom = Kingdom(curr_sequence[0])
        curr_message = ''.join(curr_sequence[1:]).replace(" ", '').upper()
        curr_decrypted_message = TransmitMessage(curr_kingdom, curr_message).deciphered_message
        check_curr_allies = CheckAllegiance(curr_kingdom, curr_decrypted_message)
        kingdom_character_map = check_curr_allies.required_counts
        actual_character_map = check_curr_allies.actual_counts
        if curr_kingdom.is_ally:
            allies_list.append(curr_kingdom.kingdom)

    if not allies_list or len(set(allies_list)) < 3:
        print('NONE')
    else:
        print('SPACE ' + ' '.join(allies_list))


if __name__ == '__main__':
    main()
