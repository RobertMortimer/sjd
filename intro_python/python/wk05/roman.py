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
    1000 : 'M',

}

x = int(input('Enter your number : '))

if x < 4000:
  roman_number = ''
  while x > 0:
    # Loop through our our numbers in order
    bigest_int = 0
    smallest_count = 0
    for k in arabic_nbr:
      print(str(k) + ' : ' + arabic_nbr[k])
      y = divmod(x, k)
      if (y[0] != 0) and (k > bigest_int):
        print(str(k) + ' Devides ' + str(y[0]) + ' Times' )
        bigest_int = k
        smallest_count = y[0]
    while smallest_count > 0:
      roman_number = roman_number + arabic_nbr[bigest_int]
      smallest_count += -1
      x = x - bigest_int



  print('Start with ' + str(bigest_int) )
  print('Number ' + roman_number )
  




  # for k in roman_nbr:
  #   print(roman_nbr[k])

else:
  print('We only do numbers under 4000')


# Find exact division with remainder
#x = divmod(1420, 500)
#print('Whole times : ' + str(x[0]))
#print('remainder   : ' + str(x[1]))
