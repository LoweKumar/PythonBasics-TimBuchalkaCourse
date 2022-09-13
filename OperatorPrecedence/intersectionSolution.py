text = """Education is not the learning of facts
but the training of the mind to think

– Albert Einstein"""

prepositions = {"as", "but", "by", "down", "for", "in", "of", "on", "to", "with"}

# result = list(sorted(set(text)))
# print(result)

words = text.split()
print(words)

preps_used = prepositions.intersection(words)
print(preps_used)

# Alternate Method
result = set(words) & prepositions
print(result)