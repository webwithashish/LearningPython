def myfunc(str):
    final_str = []
    for i in range(len(str)):
        if i % 2 == 0:
            final_str.append(str[i].upper())
        else:
            final_str.append(str[i].lower())
    print(final_str)
    return ''.join(final_str)


print(myfunc('ashishkumarlatake'))
