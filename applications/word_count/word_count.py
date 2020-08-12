def word_count(s):
    # Your code here
    d = {}
    check_set = {',',':',';','\'','"','.','-', '+', '=', '/', '\r', '|', '[' ,']', '{', '}', '(', ')', '*', '^', '&'}
    if s == '':
        return d
    split_s = s.lower().split(' ')
    for i in range(len(split_s)):
        test = [i.split('\t',1)[0] for i in split_s[i] if i not in check_set]
        new_str = ''.join(test)
        if new_str in d:
            d[new_str] += 1
        else:
            d[new_str] = 1
    return d
        


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))