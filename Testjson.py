import jsonlines

#with open('./data/Digital_Twin_Scientific_Papers.jl', 'rb') as f:
#    for item in json_lines.reader(f):
#        print(item['x'])
        
i = 0        
with jsonlines.open('./data/Digital_Twin_Scientific_Papers.jl') as reader:
    for obj in reader:
        print(obj['key'])
        i+=1
print(i)