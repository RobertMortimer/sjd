# Ask Question from data Dictionary (hash)
# Load in data
import json
# Load out data
with open('animal-questions.json', "w") as read_file:
    data = json.load(read_file)

# Set my starting question id
q_id = '16'

# I start without an answer
ans = 'N'

# A simple Y/N validation function
# q_text = Question text
# Get question from data
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
    if data[q_id]['ans'] == 'Y':
        ans ='Y'

    # Was this answer OK?
    # IF NO
    # What was the correct answer?
    # What question do I need to ask?
