# Your code here

file = open('robin.txt','r')

txt = file.read().lower().replace('\n',' ').split(' ')
add_set = {}
check_set = {',',':',';','\'','"','.','-', '+', '=', '/', '\r', '|', '[' ,']', '{', '}', '(', ')', '*', '^', '&'}
for i in range(0,len(txt)):
    test = [k.split('\t', 1)[0] for k in txt[i]]
    for j in range(0,len(test)):
        if test[j] in check_set:
            test[j] = ''
    joinedstr = "".join(test[j])
    txt[i] = joinedstr
print(txt)