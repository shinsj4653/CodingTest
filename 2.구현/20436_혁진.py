import sys
keyboard_left = [['q', 'w', 'e', 'r', 't'], ['a','s','d','f','g'], ['z','x','c','v']]
keyboard_right = [['y', 'u', 'i', 'o', 'p'], ['h','j','k','l'],['b','n','m']]
si, sr = sys.stdin.readline().rstrip().split()
inp_str = sys.stdin.readline().rstrip()

def find_key_left(ch):
    for i in range(3):
        if ch in keyboard_left[i]:
            return i, keyboard_left[i].index(ch)
        else:
            continue
    return -1, -1

def find_key_right(ch):
    for i in range(3):
        if ch in keyboard_right[i]:
            if i==2:
                return i, 4+keyboard_right[i].index(ch)
            else:
                return i, 5+keyboard_right[i].index(ch)
        else:
            continue
    return -1, -1

left_hand_y, left_hand_x = list(find_key_left(si))
right_hand_y, right_hand_x = list(find_key_right(sr))
ans = len(inp_str)

for i in inp_str:
    if find_key_left(i) == (-1, -1):
        y, x = find_key_right(i)
        is_Left = False
    else:
        y, x = find_key_left(i)
        is_Left = True

    if is_Left:
        ans += abs(y-left_hand_y) + abs(x-left_hand_x)
        left_hand_y, left_hand_x =y, x
    else:
        ans+=abs(y-right_hand_y) + abs(x-right_hand_x)
        right_hand_y, right_hand_x = y, x

print(ans)