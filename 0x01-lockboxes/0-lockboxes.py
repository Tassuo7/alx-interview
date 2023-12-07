#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
"""


def canUnlockAll(boxes):
	"""
	method that determines if all the boxes can be opened
	"""
	n = len(boxes)
	open_boxes = set([0])
	close_boxes = set(boxes[0]).difference(set([0]))
	while len(close_boxes) > 0:
		nbBox = close_boxes.pop()
		if not nbBox or nbBox >= n or nbBox < 0:
			continue
		if nbBox not in open_boxes:
			close_boxes = close_boxes.union(boxes[nbBox])
			open_boxes.add(nbBox)
	return n == len(open_boxes)
