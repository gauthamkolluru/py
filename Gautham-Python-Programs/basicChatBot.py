user_name = input('What is your name?')
print('Hello ', user_name, ' !')
resp_list = []
resp_list.append(input(f'How are you {user_name} ?'))
random_dict = {('hw','how','Hw','HOW','hoW'):'how', ('are','ar','r',"'re"):'are'}
# something = [rand for rand in (random_dict.keys())]

for resp in resp_list:
    for rlist in resp.split(' '):
        for rand in random_dict.keys():
            if rlist in rand:
                print(rlist,random_dict[rand])
                # resp.replace(rlist,random_dict[rand])
                print(resp)
        if 'how' in resp and 'are' in resp and 'you' in resp:
            print('I\'m doing great, thanks for asking!')
            resp_list.append(input('What are you doing?'))
        elif ('what' in resp and 'doing' in resp) or ('how' in resp and 'about' in resp and 'you' in resp):
            print('i\'m just chatting with you!')
            resp_list.append(input('had a great conversation?'))
        else:
            for all_resp in resp_list:
                print(all_resp)
# for r in resp:
#     if r == rvar:
#         resp.replace(r,random_dict[rand])
#         print(resp)


# for r in resp:
#     # print(r)
#     if r == [ra for ra in [rand for rand in (random_dict.keys())]]:
#         print(random_dict[r])
    # r.replace(random_dict[rand])
# print(r)
# for resp in resp_list:
#     # print(resp)
#     # print(type(resp))
#     resp = resp.split(' ')
#     print(resp)
#     print(type(resp))

