# '/usr/share/dict/words'
def get_words():
    with open('/usr/share/dict/words', 'r') as rf:
        with open('./assets/words.txt', 'w') as wf:
            for line in rf:
                if len(line) > 3:
                    wf.write(line)


def get_nonexists():
    try:
        # print('I ran second')
        with open('somefile.blarp', 'r') as f:
            print(f.read())
    except (FileNotFoundError, TypeError)as e:
        print(e)

    finally:
        print('I ran last')


def get_binary():
    with open('./assets/text.txt', 'rb') as f:
        print(f.read())


if __name__ == '__main__':
    # get_words()
    get_nonexists()
    # get_binary()
