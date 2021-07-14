"""
track 1
所有人都购买所有9个东西

format:
id,category
1,1 1 1 0 1 0 0 0 0

author: lzhbrian (https://lzhbrian.me)
date: 2021.7.13
"""
from tqdm import tqdm

output_filename = '../submission_track1/all_purchase_9items_track1_20210713.csv'

NUM_USERS = 206254
POP_EXPOSE_LIST = '1 1 1 1 1 1 1 1 1'

fp = open(output_filename, 'w')
print('id,category', file=fp)
for i in tqdm(range(1, NUM_USERS + 1)):
	print('%s,%s' % (i, POP_EXPOSE_LIST), file=fp)
