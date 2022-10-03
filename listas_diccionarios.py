def repetidos(lista):
    dic_num = {}
    for i in lista:
        if i in dic_num:
            dic_num[i] += 1
        else:
            dic_num[i] = 1
    return dic_num    
