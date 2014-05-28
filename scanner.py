def scan(input):
	if input == "fuck you fag":
		print "NO FUCK YOU"
		return
	words = input.lower().split(" ")
	return makeList(words)

def makeList(words):
	verbs = ["fight", "travel", "search", 'venture', 'rest', 'attack', 'sleep', 'run', 'check', 'leave', 'look']
	nouns = ['town', 'forest', 'night', 'potion', 'scroll', 'home', 'shop', 'yes', 'no', 'yeah', 'back', 'stats', 'opponent', 'opponents', 'my', 'mine', 'strength', 'health', 'none', 'bag']

	wordList = {}
	wordList["verbs"] = []
	wordList["nouns"] = []
	for word in words:
		if word in verbs:
			wordList['verbs'].append(word)
		elif word in nouns:
			wordList['nouns'].append(word)

	return wordList