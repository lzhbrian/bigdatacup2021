"""
track 2
gen a submission based on popularity
每个session购买数量最多的三个东西：'28 1 14 86 127 126 200 164 196'

format:
id,itemids
1,1 2 3 4 5 6 7 8 9

author: lzhbrian (https://lzhbrian.me)
date: 2021.7.13
"""
from tqdm import tqdm

output_filename = '../submission_track2/pop_20210713.csv'

NUM_USERS = 206096
POP_EXPOSE_LIST = '28 1 14 86 127 126 200 164 196'

fp = open(output_filename, 'w')
print('id,itemids', file=fp)
for i in tqdm(range(1, NUM_USERS + 1)):
	print('%s,%s' % (i, POP_EXPOSE_LIST), file=fp)
