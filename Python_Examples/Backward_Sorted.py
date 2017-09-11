

def FirstReverse(ourstr):
    s = ourstr[::-1]
	print ("Backward String:")
    print(s)
    ss = sorted(ourstr)
	print ("Sorted String:")
    print(ss)
    return s, ss

def main():
    ourstr = "Hello World and Coders"
    FirstReverse(ourstr)
main()
