number_of_inputs = int(input('Enter the  Nuber of inputs: '))

tweets_dict = {}

for each_input in range(number_of_inputs):
    no_of_tweets = int(input('Enter the number of tweets you want to register: '))
    for input_tweet in range(no_of_tweets):
        tweet = input('Enter the tweeter Name and the tweet id separated by space: ')
        if tweet.split()[0] not in tweets_dict:
            tweets_dict.update({tweet.split()[0]:1})
        else:
            tweets_dict.update({tweet.split()[0]:tweets_dict[tweet.split()[0]]+1})

output_dict = {}

for key,value in tweets_dict.items():
    if value not in output_dict.keys():
        output_dict.update({value:[key]})
    else:
        output_dict.update({value:output_dict[value]+[key]})

for key,value in output_dict.items():
    if len(value) > 1 and key is not max(output_dict.keys()):
        for each_value in sorted(value):
            print(each_value,key)
    if key == max(output_dict.keys()):
        for each_value in sorted(value):
            print(each_value,key)