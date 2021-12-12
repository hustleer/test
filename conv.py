import json,random
with open('cleverbot_data.json','r') as file:
    conversations = json.load(file)

selected = random.randint(0, len(conversations)-1)
print('\n Title: {}'.format(conversations[selected]['title']))

for i in conversations[selected]['messages']:
    print(i['messenger'] + ' : ' + str(i['messages']))
