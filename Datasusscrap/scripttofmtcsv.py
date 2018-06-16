with open('Data2000 txt.txt', 'r') as txt:
    file = txt.read().replace(';', ',')
with open('out2000fmt.csv', 'w') as out:
    out.write(file)
    
    
