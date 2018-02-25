# def multi(x,y,z=1):
#     result = x * y * z
#     print(result)
#     
# multi(5,2)



fishlist = ['fish', 'dish', 'frigs', 'digs']

def convertdic(list):
    newdic = {}
    for i in list:
        newdic[i] = ''
    return newdic
    
value = convertdic(fishlist)

print(value)