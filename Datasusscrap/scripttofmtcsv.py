'''
    Data SUS do not ofers the option to download CSV, the closer is separated by ';'.
    This code simply overcome this insue.
'''
with open('Data2000 txt.txt', 'r') as txt:
    file = txt.read().replace(';', ',')
with open('out2000fmt.csv', 'w') as out:
    out.write(file)
    
    
