import jsonlines

with open('./data/Digital_Twin_Scientific_Papers.jl', 'rb') as f:
    for item in json_lines.reader(f):
        print(item['x'])