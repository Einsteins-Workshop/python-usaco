0# https://projecteuler.net/problem=17

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 19
# letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters
# would be used?
#
# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters. The use of 'and' when writing out numbers is in
# compliance with British usage.

ones=['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
tens=['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
teens=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
def numberToWord(number):
    if number<10:
        return ones[number]
    elif number<20:
        return teens[number-10]
    elif number<100:
        return tens[int((number-number%10)/10)]+numberToWord(number%10)
    elif number<1000:
        if number%100==0:
            return numberToWord(int((number-number%100)/100))+'hundred'
        else:
            return numberToWord(int((number-number%100)/100))+'hundredand'+numberToWord(number%100)
    else:
        return 'onethousand'
ans=0
for i in range(1001):
    ans=ans+len(numberToWord(i))
print(ans)