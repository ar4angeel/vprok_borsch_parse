stroka = input()
add_stroka = ''
for perebor in stroka:
    if perebor != ' ':
        add_stroka = add_stroka + perebor
    else:
        add_stroka = add_stroka + '_'

print(add_stroka)