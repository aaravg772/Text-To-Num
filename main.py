import MyException
from recognize_num import RecoNum


def format_number(num):
    try:
        return f"{num:,}"
    except (TypeError, ValueError):
        return "Invalid number"

nums = [
    'negative', 'zero','one','two','three','four','five','six','seven','eight','nine',
    'ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen',
    'twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety',
    'hundred','thousand','million','billion','trillion','quadrillion','quintillion',
    'sextillion','septillion','octillion','nonillion',
    'decillion','undecillion','duodecillion','tredecillion','quattuordecillion',
    'quindecillion','sexdecillion','septendecillion','octodecillion','novemdecillion',
    'vigintillion','unvigintillion','duovigintillion','trevigintillion','quattuorvigintillion',
    'quinvigintillion','sexvigintillion','septenvigintillion','octovigintillion','novemvigintillion',
    'trigintillion','untrigintillion','duotrigintillion','tretrigintillion','quattuortrigintillion',
    'quintrigintillion','sextrigintillion','septentrigintillion','octotrigintillion','novemtrigintillion',
    'quadragintillion','quinquagintillion','sexagintillion','septuagintillion','octogintillion','nonagintillion',
    'centillion','googol','googolplex'
]

word_num = input("Enter a number in words: ")

try:
    word_num = word_num.lower().split(' ')
except:
    raise MyException.MyException("Invalid input, please enter a number in words")

for word in word_num:
    if word not in nums:
        raise MyException.MyException("Invalid number word: " + word)

num = RecoNum().reco(word_num)

print("The number is: ", format_number(num))