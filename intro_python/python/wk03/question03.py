# Ask Question from data Dictionary (hash)
# Amend hash data add key pairs
#  - goto record fo YES
#  - goto record for NO 
data = {
    "1":{"Q": "Is it an aquatic animal"},
    "2":{"Q": "Is it an is it a fish"},
    "3":{"Q": "does it eat meat"},
    "4":{"A": "Goldfish"},
    "5":{"A": "Seal"},
    "6":{"A": "Dog"},
    "7":{"A": "Cow"},
}

# A simple Y/N validation function
# q_text = Question text
# Get question from data

# Set my starting question id
q_id = '1'

# I start without an answer
ans = 'N'

def get_answer (q_text):
    return True


# Ask question and define result
while ans == 'N':
    q_txt = data[q_id]['Q']
    if get_answer(q_txt):
        print('YES')
        # Get next record ID
    else:
        print('No')
        # Get next record ID

    # Is this an answer? 
    # If so print out and stop
    # If so print out and stop
    if data[q_id]['ans'] == 'Y':
        ans ='Y'
