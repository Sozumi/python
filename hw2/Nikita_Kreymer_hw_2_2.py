first_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for i, s in enumerate(first_list):
    if s.isdigit():
        first_list[i] = f'"{int(s):02d}"'
    elif s[1:].isdigit():
        first_list[i] = f'"{s[0]}{int(s[1:]):02d}"'
    print(first_list[i], end=' ')
print('\n', first_list)
