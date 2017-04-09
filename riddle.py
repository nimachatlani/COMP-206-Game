print ('Hello Welcome to the riddle game')
print ('Here is your first riddle:')
answer1 = input('What has a head, a tail, is brown, and has no legs?')
print('Your answer: ' + answer1)

correctAnswer1 = 'penny'


if answer1 == correctAnswer1:
        print ('You are correct, lets go to the next riddle')
        answer2 = input('The more you take, the more you leave behind.  What am I?')
        correctAnswer2 = 'footsteps'
        if answer2 == correctAnswer2:
                print('You are correct, now onto the final riddle:')
                answer3 = input('Davids father has 3 sons: snap, crackle, and: ?')
                correctAnswer3 = 'David'
                if answer3 == correctAnswer3:
                        print ('You win!')
                else:
                        print ('You were close but you lose')
        else:
                print('thats incorrect bye')
else:
        print('incorrect smh')
