first_name = input('What is your name? ').lower()
second_name = input('And what is your name? ').lower()
final_name = first_name + second_name
count1 = 0
count2 = 0
letter1 = ''
letter2 = ''
for letter1 in 'true':
    for letter2 in final_name:
        if letter2 == letter1:
            count1 += 1
for letter1 in 'love':
    for letter2 in final_name:
        if letter2 == letter1:
            count2 += 1
love_score = str(count1) + str(count2)
final_love_score = int(love_score)
if final_love_score >= 40 and final_love_score <= 50:
    print(f'Your love score is {final_love_score}, you are alright together.')    
else:
    print(f'Your love score is {final_love_score}.')