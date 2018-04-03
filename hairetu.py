file = open('hairetu.txt', 'r')  #読み込みモードでオープン
string = file.read()      #readですべて読み込む
list1 = string.replace('GO', '\nGO')
print(list1)
