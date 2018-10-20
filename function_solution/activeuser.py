from pathlib import Path


def get_active_users(filename):
    chats = open(filename, 'r')
    users = {}
    for line in chats:
        try:
            name = line[:line.index(":")].strip()
            if name not in users:
                users[name] = 1
            else:
                users[name] += 1
        except ValueError:
            pass
    chats.close()
    active_users = sorted(users.iteritems(), key=lambda (k, v): v, reverse=True)[:3]
    return [k.replace("<", "").replace(">", "") for (k, v) in active_users]


def main():
    flag = True
    while flag:
        filename = raw_input("Enter file name(with only txt extention like for chat.txt enter chat): ") + ".txt"
        my_file = Path(filename)
        if my_file.is_file():
            print get_active_users(filename)
            flag = False
        else:
            print "This file with this name doesnt exist, or maybe you using wrong extention"


if __name__ == '__main__':
    main()
