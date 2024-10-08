import json

file_1 = json.load(open('file1.json'))
file_2 = json.load(open('file2.json'))

def gendiff(file_1, file_2):
    f_list = []
    keys_list = list(set(file_1) | set(file_2))
    keys_list.sort()
    for key in keys_list:
        if key in file_1 and key in file_2:
            if file_1[key] == file_2[key]:
                f_list.append('  ' + str(key) + ': ' + (str(file_1[key])).lower())
            else:
                f_list.append('- ' +  str(key) + ': ' + (str(file_1[key])).lower())
                f_list.append('+ ' +  str(key) + ': ' + (str(file_2[key])).lower())
        else:
            if key in file_1:
                f_list.append('- ' +  str(key) + ': ' + (str(file_1[key])).lower())
            else:
                f_list.append('+ ' +  str(key) + ': ' + (str(file_2[key])).lower())
    f_string = '{\n  ' + '\n  '.join(f_list) + '\n}'
    print(f_string)
    return f_string


def main():
    gendiff(file_1, file_2)


if __name__ == '__main__':
    main()
