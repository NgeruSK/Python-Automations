catNames = []
while True:
    print('Enter the name of cat number '+str(len(catNames)+1)+'. Leave blank if done')
    catName = input()
    if catName in catNames:
        print('Already entered this pet')
        continue
    if not catName:
        break
    catNames.append(catName)
print('Done, cats count: '+str(len(catNames))+' and names are:')
for i in range(len(catNames)):
    print('cat '+str(i + 1)+' is: '+catNames[i])