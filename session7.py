import math
import random
from functools import partial, reduce
# -------------------------  Question 1  ------------------------------------
def fiboacci_number_check(n):
    """
    The Fibonacci sequence is one of the most famous formulas in mathematics. 
    Each number in the sequence is the sum of the two numbers that precede it. 
    So, the sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and so on
    
    This function checks whether the given function is fibonacci or not
    
    A number is Fibonacci if and only if one or both of (5*n2 + 4) or (5*n2 – 4) is a perfect square
    
    input : number that needs to be checked
    output : Bool Value that says True for Fibonacci else False

    """
    if(isinstance(n,int)):
        result = list(filter(lambda num : int(math.sqrt(num)) * int(math.sqrt(num)) == num, [5*n*n + 4,5*n*n - 4] ))
        return bool(result) 
    else:
        raise TypeError("Input should be of type Int")


# --------------------------- Question 2  ------------------------------

def add_numbers(a, b):

    """
    input : 2 iterators say a and b
    output: A list of addition of 2 given iterators if and only if  a is even and b is odd

    """
    
    if(isinstance(a, list) and isinstance(b, list)):
        return ([x+y for x, y in zip(a, b) if ((x % 2 == 0) and (y % 2 != 0)) ])
    else:
        raise TypeError("Input should be of type list")
        
def strip_vowel(string):

    """
    input : string
    output: A stripped in which vowel are stripped

    """
    vowel = ['a', 'e', 'i', 'o', 'u']
    if(isinstance(string, str)):
         return "".join([i for i in string if i not in vowel])
    else:
        raise TypeError("Input should be of type string")
        
def relu(array):
    """
    Relu : This is one of the activation function used in ML. 
    It returns the same value for positive values, and it gives 0 for negative values

    """
    return [max(0,i) for i in array if(isinstance(i, int) or isinstance(i, float))]

def sigmoid(array):
    """
     Relu : This is one of the activation function used in ML. 
    The output is 1/1+e ^(-x)

    """
    return [1 / (1 + math.exp(-i)) for i in array if(isinstance(i, int) or isinstance(i, float))]

def shift_characters(string):

    """
    This function takes string as input and return the string which is shifted 5 times. 
    If it is at the edge it will be rounded back to first element.
    Eg . z will be shifted to e.
    """
    if(isinstance(string, str)):
        return "".join([chr(int((ord(i) + 5 - 97)%26 )+97) for i in string.lower()])

# --------------------------- Question 3  ------------------------------


swear_words = ['4r5e',
 '5h1t',
 '5hit',
 'a55',
 'anal',
 'anus',
 'ar5e',
 'arrse',
 'arse',
 'ass',
 'ass-fucker',
 'asses',
 'assfucker',
 'assfukka',
 'asshole',
 'assholes',
 'asswhole',
 'a_s_s',
 'b!tch',
 'b00bs',
 'b17ch',
 'b1tch',
 'ballbag',
 'balls',
 'ballsack',
 'bastard',
 'beastial',
 'beastiality',
 'bellend',
 'bestial',
 'bestiality',
 'bi+ch',
 'biatch',
 'bitch',
 'bitcher',
 'bitchers',
 'bitches',
 'bitchin',
 'bitching',
 'bloody',
 'blow',
 'job',
 'blowjob',
 'blowjobs',
 'boiolas',
 'bollock',
 'bollok',
 'boner',
 'boob',
 'boobs',
 'booobs',
 'boooobs',
 'booooobs',
 'booooooobs',
 'breasts',
 'buceta',
 'bugger',
 'bum',
 'bunny',
 'fucker',
 'butt',
 'butthole',
 'buttmunch',
 'buttplug',
 'c0ck',
 'c0cksucker',
 'carpet',
 'muncher',
 'cawk',
 'chink',
 'cipa',
 'cl1t',
 'clit',
 'clitoris',
 'clits',
 'cnut',
 'cock',
 'cock-sucker',
 'cockface',
 'cockhead',
 'cockmunch',
 'cockmuncher',
 'cocks',
 'cocksuck',
 'cocksucked',
 'cocksucker',
 'cocksucking',
 'cocksucks',
 'cocksuka',
 'cocksukka',
 'cok',
 'cokmuncher',
 'coksucka',
 'coon',
 'cox',
 'crap',
 'cum',
 'cummer',
 'cumming',
 'cums',
 'cumshot',
 'cunilingus',
 'cunillingus',
 'cunnilingus',
 'cunt',
 'cuntlick',
 'cuntlicker',
 'cuntlicking',
 'cunts',
 'cyalis',
 'cyberfuc',
 'cyberfuck',
 'cyberfucked',
 'cyberfucker',
 'cyberfuckers',
 'cyberfucking',
 'd1ck',
 'damn',
 'dick',
 'dickhead',
 'dildo',
 'dildos',
 'dink',
 'dinks',
 'dirsa',
 'dlck',
 'dog-fucker',
 'doggin',
 'dogging',
 'donkeyribber',
 'doosh',
 'duche',
 'dyke',
 'ejaculate',
 'ejaculated',
 'ejaculates',
 'ejaculating',
 'ejaculatings',
 'ejaculation',
 'ejakulate',
 'fucker',
  'fuck',
 'f4nny',
 'fag',
 'fagging',
 'faggitt',
 'faggot',
 'faggs',
 'fagot',
 'fagots',
 'fags',
 'fanny',
 'fannyflaps',
 'fannyfucker',
 'fanyy',
 'fatass',
 'fcuk',
 'fcuker',
 'fcuking',
 'feck',
 'fecker',
 'felching',
 'fellate',
 'fellatio',
 'fingerfuck',
 'fingerfucked',
 'fingerfucker',
 'fingerfuckers',
 'fingerfucking',
 'fingerfucks',
 'fistfuck',
 'fistfucked',
 'fistfucker',
 'fistfuckers',
 'fistfucking',
 'fistfuckings',
 'fistfucks',
 'flange',
 'fook',
 'fooker',
 'fuck',
 'fucka',
 'fucked',
 'fucker',
 'fuckers',
 'fuckhead',
 'fuckheads',
 'fuckin',
 'fucking',
 'fuckings',
 'fuckingshitmotherfucker',
 'fuckme',
 'fucks',
 'fuckwhit',
 'fuckwit',
 'fudge',
 'packer',
 'fudgepacker',
 'fuk',
 'fuker',
 'fukker',
 'fukkin',
 'fuks',
 'fukwhit',
 'fukwit',
 'fux',
 'fux0r',
 'f_u_c_k',
 'gangbang',
 'gangbanged',
 'gangbangs',
 'gaylord',
 'gaysex',
 'goatse',
 'God',
 'god-dam',
 'god-damned',
 'goddamn',
 'goddamned',
 'hardcoresex',
 'hell',
 'heshe',
 'hoar',
 'hoare',
 'hoer',
 'homo',
 'hore',
 'horniest',
 'horny',
 'hotsex',
 'jack-off',
 'jackoff',
 'jap',
 'jerk-off',
 'jism',
 'jiz',
 'jizm',
 'jizz',
 'kawk',
 'knob',
 'knobead',
 'knobed',
 'knobend',
 'knobhead',
 'knobjocky',
 'knobjokey',
 'kock',
 'kondum',
 'kondums',
 'kum',
 'kummer',
 'kumming',
 'kums',
 'kunilingus',
 'l3i+ch',
 'l3itch',
 'labia',
 'lmfao',
 'lust',
 'lusting',
 'm0f0',
 'm0fo',
 'm45terbate',
 'ma5terb8',
 'ma5terbate',
 'masochist',
 'master-bate',
 'masterb8',
 'masterbat*',
 'masterbat3',
 'masterbate',
 'masterbation',
 'masterbations',
 'masturbate',
 'mo-fo',
 'mof0',
 'mofo',
 'mothafuck',
 'mothafucka',
 'mothafuckas',
 'mothafuckaz',
 'mothafucked',
 'mothafucker',
 'mothafuckers',
 'mothafuckin',
 'mothafucking',
 'mothafuckings',
 'mothafucks',
 'mother',
 'fucker',
 'motherfuck',
 'motherfucked',
 'motherfucker',
 'motherfuckers',
 'motherfuckin',
 'motherfucking',
 'motherfuckings',
 'motherfuckka',
 'motherfucks',
 'muff',
 'mutha',
 'muthafecker',
 'muthafuckker',
 'muther',
 'mutherfucker',
 'n1gga',
 'n1gger',
 'nazi',
 'nigg3r',
 'nigg4h',
 'nigga',
 'niggah',
 'niggas',
 'niggaz',
 'nigger',
 'niggers',
 'nob',
 'nob',
 'jokey',
 'nobhead',
 'nobjocky',
 'nobjokey',
 'numbnuts',
 'nutsack',
 'orgasim',
 'orgasims',
 'orgasm',
 'orgasms',
 'p0rn',
 'pawn',
 'pecker',
 'penis',
 'penisfucker',
 'phonesex',
 'phuck',
 'phuk',
 'phuked',
 'phuking',
 'phukked',
 'phukking',
 'phuks',
 'phuq',
 'pigfucker',
 'pimpis',
 'piss',
 'pissed',
 'pisser',
 'pissers',
 'pisses',
 'pissflaps',
 'pissin',
 'pissing',
 'pissoff',
 'poop',
 'porn',
 'porno',
 'pornography',
 'pornos',
 'prick',
 'pricks',
 'pron',
 'pube',
 'pusse',
 'pussi',
 'pussies',
 'pussy',
 'pussys',
 'rectum',
 'retard',
 'rimjaw',
 'rimming',
 'hit',
 's.o.b.',
 'sadist',
 'schlong',
 'screwing',
 'scroat',
 'scrote',
 'scrotum',
 'semen',
 'sex',
 'sh!+',
 'sh!t',
 'sh1t',
 'shag',
 'shagger',
 'shaggin',
 'shagging',
 'shemale',
 'shi+',
 'shit',
 'shitdick',
 'shite',
 'shited',
 'shitey',
 'shitfuck',
 'shitfull',
 'shithead',
 'shiting',
 'shitings',
 'shits',
 'shitted',
 'shitter',
 'shitters',
 'shitting',
 'shittings',
 'shitty',
 'skank',
 'slut',
 'sluts',
 'smegma',
 'smut',
 'snatch',
 'son-of-a-bitch',
 'spac',
 'spunk',
 's_h_i_t',
 't1tt1e5',
 't1tties',
 'teets',
 'teez',
 'testical',
 'testicle',
 'tit',
 'titfuck',
 'tits',
 'titt',
 'tittie5',
 'tittiefucker',
 'titties',
 'tittyfuck',
 'tittywank',
 'titwank',
 'tosser',
 'turd',
 'tw4t',
 'twat',
 'twathead',
 'twatty',
 'twunt',
 'twunter',
 'v14gra',
 'v1gra',
 'vagina',
 'viagra',
 'vulva',
 'w00se',
 'wang',
 'wank',
 'wanker',
 'wanky',
 'whoar',
 'whore',
 'willies',
 'willy',
 'xrated',
 'xxx']

def swear_word_check(paragraph):

    """
    This funtion checks whether the inputed paragraph contains swear words or not.
    Swear words are listed in swear_words list

    """
    if(isinstance(paragraph, str)):
        result = [ word for word in paragraph.split(" ") if word.lower() in swear_words]
        return bool(result) and result
    else:
        raise TypeError("Input should be of type string")


#---------------------------Question 4----------------------------------


# Using reduce function


def add_even_numbers_using_list(list_input):
    """
    This funciton add only even numbers in a list

    """
    return reduce(lambda a,b : a+b if(b%2==0) else a+0 , list_input, 0)

def biggest_printable_ascii_character(string):

    """
    this function finds the biggest character in a string (printable ascii characters)
    """

    return reduce(lambda a, b : a if ord(a)>ord(b) else b,string)
    
def add_every_third_number(list_input) :

    """
    this fuction adds every third element in a list
    It add 2nd, 5th, 8th indexed numbers
    """
    return reduce(lambda a,b : a+b if(b%3==2) else a+0 , list_input, 0)


#------------------------------- Question 6-----------------------------------


# Using randint, random.choice and list comprehensions, 
# write an expression that generates 15 random KADDAADDDD number plates, 
# where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

def number_plates():
    """
    This fuction generates 15 random KADDAADDDD number plates, 
    where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999

    """
    return ([ 'KA' + str(random.randint(10,99))+ chr(random.randint(65,90)) + chr(random.randint(65,90))+ str(random.randint(1000,9999)) for i in range(15)])


#----------------------------------- Question 7 --------------------------------------

def number_plates_arguments_accept(state, last_4_digit_start = 1000, last_4_digit_end = 9999):
    """
    This fuction generates 15 random SSDDAADDDD number plates, 
    where state(SS) is from the input  D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & DDDD range is from the input 

    """
    if(isinstance(state,str)):
        if(len(state) == 2):
            if(1000<=last_4_digit_start<=9999 and 1000<=last_4_digit_end<=9999 and last_4_digit_start < last_4_digit_end):
                 return ([ state + str(random.randint(10,99))+ chr(random.randint(65,90)) + chr(random.randint(65,90))+ str(random.randint(last_4_digit_start,last_4_digit_end)) for i in range(15)])
                
            else :
                raise ValueError("Last Four digit start and Last Four digi end should be a four digit number and last_4_digit_start < last_4_digit_end ")
        else:
            raise ValueError("state should always has 2 Characters") 


# Partial function such that state can be changed but last 4 digits range is fixed
number_plates_partial = partial(number_plates_arguments_accept,last_4_digit_start = 2000, last_4_digit_end = 9999)