
def isNumber(s: str) -> bool:
    end_states = ("s3", "s4", "s7")
    dic = {
        "digit": [("s0", "s3"), ("s3", "s3"), ("s5", "s7"), ("s6", "s7"), ("s4", "s4"), ("s2", "s4"), ("s1", "s3"),
                  ("s7", "s7")],
        "+": [("s0", "s1"), ("s5", "s6")],
        "-": [("s0", "s1"), ("s5", "s6")],
        "e": [("s4", "s5"), ("s3", "s5")],
        "E": [("s4", "s5"), ("s3", "s5")],
        ".": [("s0", "s2"), ("s1", "s2"), ("s3", "s4")]
    }
    cur_state = "s0"
    for char in s:
        if char not in dic:
            if not char.isdigit():
                return False
            key = "digit"
        else:
            key = char
        items = dic[key]
        get_next_state = False
        for start_state, end_state in items:
            if start_state == cur_state:
                cur_state = end_state
                get_next_state = True
                break
        if not get_next_state:
            return False
    return cur_state in end_states

if __name__ == '__main__':
    isNumber("e")
