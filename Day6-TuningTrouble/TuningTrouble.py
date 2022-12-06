test_1 = ''

def find_first_set(word):
    i = 0
    while True:
        if len(set(word[i:i+14])) == 14:
            return i + 14
        i += 1

def main():
    print(find_first_set(test_1))

if __name__=='__main__':
    main()