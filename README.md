# **Session 7 - First Class Functions Part 2**
This session was all about Map, Filter & Zip, Reducing Functions, Partial Functions,The Operator Module.

## **Assignment**


1. Write a function using only list filter lambda that can tell whether a number is a Fibonacci number or not. You can use a pre-calculated list/dict to store fab numbers till 10000 
2. Using list comprehension (and zip/lambda/etc if required) write an expression that: 
add 2 iterables a and b such that a is even and b is odd
   1. strips every vowel from a string provided (tsai>>t s)
   2. acts like a ReLU function for a 1D array
   3. acts like a sigmoid function for a 1D array
   4. takes a small character string and shifts all characters by 5 (handle boundary conditions) tsai>>yxfn
3. A list comprehension expression that takes a ~200 word paragraph, and checks whether it has any of the swear words mentioned in (this repo)(https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt) 
4. Using reduce function:
    1. add only even numbers in a list
    2. find the biggest character in a string (printable ascii characters)
    3. adds every 3rd number in a list
5. Using randint, random.choice and list comprehensions, write an expression that generates 15 random KADDAADDDD number plates, where KA is fixed, D stands for a digit, and A stands for Capital alphabets. 10<<DD<<99 & 1000<<DDDD<<9999
6. Write the above again from scratch where KA can be changed to DL, and 1000/9999 ranges can be provided. Now use a partial function such that 1000/9999 are hardcoded, but KA can be provided.

### 1. **fiboacci_number_check** 

A number is Fibonacci if and only if one or both of (5 X n2 + 4) or (5 X n2 – 4) is a perfect square

### 2.1 **add_numbers**

    ```python
    ([x+y for x, y in zip(a, b) if ((x % 2 == 0) and (y % 2 != 0)) ])
    ```
### 2.2 **strip_vowel**
    ```python
    vowel = ['a', 'e', 'i', 'o', 'u']
    "".join([i for i in string if i not in vowel])
    ```

### 2.3 **relu**

    ```python
    return [max(0,i) for i in array if(isinstance(i, int) or isinstance(i, float))]
    ```
### 2.4 **sigmoid**

    ```python
   return [1 / (1 + math.exp(-i)) for i in array if(isinstance(i, int) or isinstance(i, float))]
    ```
### 2.5 **shift_characters**
    ```python
    # 1. First asci value of character is taken
    # 2. Added 5 to it
    # 3. Since they are small characters, a will start from 97. Subtracted from 97. So that we get the value which is between 0 and 26
    # 4.  Then took mod of the value. This is to handle cyclic condition. Like z should map to a again
    # 5. Again added by 97 so that it matches the ascii value of small character alphabets
   "".join([chr(int((ord(i) + 5 - 97)%26 )+97) for i in string.lower()])
    ```
### 3. **swear_word_check**
    ```python
    # list of swear words is already defined
    [word for word in paragraph.split(" ") if word.lower() in swear_words]
    ```

### 4.1 add_even_numbers_using_list
    ```python
   reduce(lambda a,b : a+b if(b%2==0) else a+0 , list_input, 0)
    ```
### 4.2  **biggest_printable_ascii_character**
    ```python
     reduce(lambda a, b : a if ord(a)>ord(b) else b,string)
    ```
### 4.3  **add_every_third_number**
    ```python
        reduce(lambda a,b : a+b if(b%3==2) else a+0 , list_input, 0)
    ```
### 5. **number_plates**
    ```python
    return [ 'KA' + str(random.randint(10,99))+ chr(random.randint(65,90)) + chr(random.randint(65,90))+ str(random.randint(1000,9999)) for i in range(15)]
    ```
### 6.  **number_plates_arguments_accept**
    ```python
     if(isinstance(state,str)):
        if(len(state) == 2):
            if(1000<=last_4_digit_start<=9999 and 1000<=last_4_digit_end<=9999 and last_4_digit_start < last_4_digit_end):
                 return ([ state + str(random.randint(10,99))+ chr(random.randint(65,90)) + chr(random.randint(65,90))+ str(random.randint(last_4_digit_start,last_4_digit_end)) for i in range(15)])
                
            else :
                raise ValueError("Last Four digit start and Last Four digi end should be a four digit number and last_4_digit_start < last_4_digit_end ")
        else:
            raise ValueError("state should always has 2 Characters") 
        
        # Convert to Partial Function
        number_plates_partial = partial(number_plates_arguments_accept,last_4_digit_start = 2000, last_4_digit_end = 9999)
    ```


