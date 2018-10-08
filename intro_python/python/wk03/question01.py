# A simple Y/N validation function
# q_text = Question text
# q_txt = 'Are we learning any python yet'

def get_answer (question):
    gotanswer = False
    while gotanswer == False:
        x = str(input(question + '? [Y/N]: '))
        if x.upper() == 'Y' or x.upper() == 'YES':
            return True
            gotanswer = True
        if x.upper() == 'N':
            return False
            gotanswer = True


# Ask question and define result
if get_answer('Are we learning any python yet'):
    print('Yes')
else:
    print('No')

