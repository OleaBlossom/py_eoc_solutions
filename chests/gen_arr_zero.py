#!/usr/bin/env checkio --domain=epy run gen-arr-zero
def gen_arr_zero(a):
	    result = []
	    while a > 0:
	    	result.append(0)
	    	a -= 1
    	return result


if __name__ == '__main__':
    print("Example:")
    print(gen_arr_zero(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert gen_arr_zero(0) == []
    assert gen_arr_zero(1) == [0]
    assert gen_arr_zero(5) == [0, 0, 0, 0, 0]
    print("Coding complete? Click 'Check' to earn cool rewards!")
