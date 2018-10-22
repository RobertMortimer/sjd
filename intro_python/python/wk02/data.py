import json
# Load out data
with open('animal-questions.json', "r") as read_file:
    data = json.load(read_file)

# Set my starting question id
q_id = '16'

# I start without an answer
ans = 'N'

# A simple Y/N validation function
def get_answer (q_text):
    good_ans = False
    while good_ans == False:
        x = str(input(q_text + '? [Y/N]: '))
        x = x.upper()
        if x == 'Y':
            return True
            good_ans = True
        elif x == 'N':
            return False
            good_ans = False
        else:
            print('Enter Y or N')

# Step into questions loop
while ans == 'N':
    q_txt = data[q_id]['Q']
    if get_answer(q_txt):
        print('YES')
        # Get next record ID
        q_id = data[q_id]['Y']
    else:
        print('No')
        # Get next record ID
        q_id = data[q_id]['N']

    # Is this an answer?
    if data[q_id]['ans'] == 'Y':
        print ('Answer is: ' + data[q_id]['Q'])
        ans ='Y'

