"""
Funkcja Index
"""

def find_index(user_list, obj):
    for i, o in enumerate(user_list):
        if obj == o:
            return i
    return -1

if __name__ == '__main__':
    test_list = [1, 2, 3]
    value = find_index(test_list, 2)
    assert value == 1
    print(value)
