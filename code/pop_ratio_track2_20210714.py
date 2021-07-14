"""
track 2
gen a submission based on popularity ratio
每个session购买率最高的三个东西：'28 15 14 86 126 127 196 200 234'
（去掉购买数量过少的

format:
id,itemids
1,1 2 3 4 5 6 7 8 9

author: lzhbrian (https://lzhbrian.me)
date: 2021.7.13
"""
from tqdm import tqdm

output_filename = '../submission_track2/pop_ratio_track2_20210714.csv'

NUM_USERS = 206096
POP_EXPOSE_LIST = '28 15 14 86 126 127 196 200 234'

fp = open(output_filename, 'w')
print('id,itemids', file=fp)
for i in tqdm(range(1, NUM_USERS + 1)):
	print('%s,%s' % (i, POP_EXPOSE_LIST), file=fp)
