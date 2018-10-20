def check_words_formation(words, input_string):
    for i in range(len(input_string)):
        if input_string[:i+1] in words:
            if i == len(input_string)-1:
                return True
            else:
                if check_words_formation(words, input_string[i+1:]):
                    return True
    return False


def can_create(list_of_strings, input_string):
    words = {i: 1 for i in list_of_strings}
    return check_words_formation(words, input_string)


def main():
    list_of_strings = ['back', 'end', 'endback', 'front', 'tree']
    print can_create(list_of_strings, 'backendback')
    print can_create(list_of_strings, 'frontyard')
    print can_create(list_of_strings, 'frontend')


if __name__ == '__main__':
    main()
