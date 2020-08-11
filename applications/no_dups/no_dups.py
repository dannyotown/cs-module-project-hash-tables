def no_dups(s):
    # Your code here
    d = dict()
    arr = []
    if len(s) == 0:
        return ''
    else:
        for i in s.split(' '):
            if i not in d:
                d[i] = 1
            else:
                d[i]+=1
        for key in d.keys():
            arr.append(key)
        return ' '.join(arr)

            


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))