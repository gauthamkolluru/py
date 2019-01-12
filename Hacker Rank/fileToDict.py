words = [line.strip().lower()[0] for line in open('/home/gautham/zingarelli2005.txt')]

word_set = list(set(words))

word_count = {x:words.count(x) for x in word_set}

print(word_count)