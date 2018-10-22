# A simple Y/N validation function
# q_text = Question text
q_txt = 'Are we learning any python yet'

def get_answer (q_text):
    return True


# Ask question and define result
if get_answer(q_txt):
    print('Yes')
else:
    print('No')

