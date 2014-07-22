#!/usr/bin/env python
import itertools
import sys

def load_words(filename):
	ret = set()
	with open(filename) as f:
		for line in f:
			ret.add(line.strip())
	sys.stderr.write("Loaded {}\n".format(filename))
	return ret

def find_match(letters, *dicts):
	words = set()
	for d in dicts:
		words.update(load_words(d))
	sys.stderr.write("Loaded {} words.\n".format(len(words)))
	permutations = 0
	ret = set()
	for i in xrange(3, len(letters) + 1):
		for mut in itertools.permutations(letters, i):
			permutations += 1
			guess = ''.join(mut)
			if guess in words:
				ret.add(guess)
	sys.stderr.write("Found {} matches.\n".format(len(ret)))

	for match in sorted(ret, key=lambda x: '{}{}'.format(len(x), x)):
		print match

if __name__ == "__main__":
	args = sys.argv
	exe = args.pop(0)
	letters = args.pop(0)
	find_match(letters, *args)