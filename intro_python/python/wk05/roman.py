# Roman numerals
# Symbol	I	V	X	L	C	D	M
# Value     1	5	10	50	100	500	1,000

# Three before 1 after
# I II  III VI  V   IV  IIV IIIV    XI

# Sort a hash on keys
 

roman_nbr = { 
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000
}

arabic_nbr = { 
    1    : 'I',
    5    : 'V',
    10   : 'X',
    50   : 'L',
    100  : 'C',
    500  : 'D',
    1000 : 'M'
}

x = int(input('Enter your number : '))

# Loop through our our numbers in order
for k in arabic_nbr:
  print(arabic_nbr[k])

for k in roman_nbr:
  print(roman_nbr[k])

# Find exact division with remainder
#x = divmod(1420, 500)
#print('Whole times : ' + str(x[0]))
#print('remainder   : ' + str(x[1]))
