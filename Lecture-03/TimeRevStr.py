import timeit


def reverse_for_loop(s):
    s1 = ''
    for c in s:
        s1 = c + s1  # appending chars in reverse order
    return s1

def for_loop_time():
    SETUP_CODE = '''
from __main__ import reverse_for_loop
'''
    TEST_CODE = '''
input_str = 'INE-KMUTNB'
reverse_for_loop(input_str)
'''
    times = timeit.repeat(setup=SETUP_CODE,
                          stmt=TEST_CODE,
                          repeat=10,
                          number=20000)

    print('For loop time: {}'.format(min(times)))

if __name__ == "__main__":
    for_loop_time()