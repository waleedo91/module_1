# Even or Odd Kata

def even_or_odd(number):
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
    
# Convert Number to String Kata

def number_to_string(num):
    return str(num)

# Vowel count Kata

def get_count(sentence):
    vowel_list = []
    for v in sentence:
        if v in 'aeiou':
            vowel_list.append(v)
    return len(vowel_list)