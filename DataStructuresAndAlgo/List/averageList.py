total = []
# total = list()

while (True):
    inp = input('Enter a number: ')
    if inp == 'done': break
    total.append(float(inp))
    average = sum(total)/len(total)

print('Average: ', average)