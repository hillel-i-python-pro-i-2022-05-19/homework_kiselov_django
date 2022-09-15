from typing import Final, TypeAlias, Iterable
import string


T_ALPHABET: TypeAlias = str
T_WORD: TypeAlias = str

DEFAULT_ALPHABET: Final[T_ALPHABET] = 'abc'

def generator(word_length: int, quantity: int, alphabet: T_ALPHABET) -> Iterable[T_WORD]:

    min_index_of_char_in_alphabet = 0
    max_index_of_char_in_alphabet = len(alphabet) - 1

    word_as_list_of_indexes = [min_index_of_char_in_alphabet] * word_length

    current_position: int = len(word_as_list_of_indexes) - 1
    previous_position: int = current_position

    last_position: int = word_length - 1

    count = 0

    while count < quantity:

        if previous_position == current_position:
            if word_as_list_of_indexes[current_position] <= max_index_of_char_in_alphabet:
                yield ''.join([alphabet[index] for index in word_as_list_of_indexes])
                word_as_list_of_indexes[current_position] += 1
            else:
                word_as_list_of_indexes[current_position] = min_index_of_char_in_alphabet
                previous_position = current_position
                current_position -= 1

        elif current_position <= previous_position and current_position >=0 and previous_position >= 0:

            yield ''.join(alphabet[index] for index in word_as_list_of_indexes)

            if word_as_list_of_indexes[previous_position] < max_index_of_char_in_alphabet:
                word_as_list_of_indexes[previous_position] += 1
            if word_as_list_of_indexes[current_position] < max_index_of_char_in_alphabet:
                word_as_list_of_indexes[current_position] += 1
            else:
                current_position = 0
                previous_position = 0
                word_as_list_of_indexes[current_position] = 0
                word_as_list_of_indexes[previous_position] = 0
                previous_position = last_position

        count += 1


def main():
    alphabet = "abcd"
    for word in generator(word_length=5, quantity=30, alphabet=alphabet):
        print(word)


if __name__ == "__main__":
    main()










