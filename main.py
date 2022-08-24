# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def get_from_dict(prefix):
    max_value = max(word_dict.values())
    selected_items = {key: val for key, val in word_dict.items() if (key.startswith(prefix) and val == max_value)}
    if len(selected_items) <= 0:
        return
    res_words = list(selected_items.keys())
    res_words.sort()
    return res_words[0]

def add_to_dict(word, count):
    # print('add')
    if word in word_dict.keys():
        loc_count = int(word_dict[word])
        loc_count += count
        word_dict[word] = loc_count
        # print(word_dict[word])
    else:
        word_dict[word] = count

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        word_dict = {}
        f = open("output.txt", "w")
        num_of_iter = int(input())
        if num_of_iter > 10000:
            # f.write('Too much commands to process')
            exit(1)
        while True:
            line = input()
            command = line.split()
            if len(command) != 2 and len(command) != 3:
                # f.write('Empty line. Please, input a line in a valid format.')
                break
            # print(len(command))
            if command[0] == '+':
                wrd = command[2].lower()
                if len(wrd) > 100:
                    # f.write('The word is too long. Please, try another input')
                    break
                add_to_dict(wrd, int(command[1]))
            elif command[0] == '?':
                smb = command[1].lower()
                f.write((get_from_dict(smb)))
                f.write('\n')
            # else:
                # f.write('Unknown command')
            num_of_iter -= 1
            if num_of_iter <= 0:
                break
        f.close()
    except ValueError:
        # f.write("No valid integer! Please try again ...")
        f.close()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
