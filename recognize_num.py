import MyException

class RecoNum():
    def __init__(self):
        self.numsWVal = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90,
    'hundred': 100,
    'thousand': 1000,
    'million': 1000000,
    'billion': 1000000000,
    'trillion': 1000000000000,
    'quadrillion': 1000000000000000,
    'quintillion': 1000000000000000000,
    'sextillion': 1000000000000000000000,
    'septillion': 1000000000000000000000000,
    'octillion': 1000000000000000000000000000,
    'nonillion': 1000000000000000000000000000000,
    'decillion': 10**33,
    'undecillion': 10**36,
    'duodecillion': 10**39,
    'tredecillion': 10**42,
    'quattuordecillion': 10**45,
    'quindecillion': 10**48,
    'sexdecillion': 10**51,
    'septendecillion': 10**54,
    'octodecillion': 10**57,
    'novemdecillion': 10**60,
    'vigintillion': 10**63,
    'unvigintillion': 10**66,
    'duovigintillion': 10**69,
    'trevigintillion': 10**72,
    'quattuorvigintillion': 10**75,
    'quinvigintillion': 10**78,
    'sexvigintillion': 10**81,
    'septenvigintillion': 10**84,
    'octovigintillion': 10**87,
    'novemvigintillion': 10**90,
    'trigintillion': 10**93,
    'untrigintillion': 10**96,
    'duotrigintillion': 10**99,
    'tretrigintillion': 10**102,
    'quattuortrigintillion': 10**105,
    'quintrigintillion': 10**108,
    'sextrigintillion': 10**111,
    'septentrigintillion': 10**114,
    'octotrigintillion': 10**117,
    'novemtrigintillion': 10**120,
    'quadragintillion': 10**123,
    'quinquagintillion': 10**153,
    'sexagintillion': 10**183,
    'septuagintillion': 10**213,
    'octogintillion': 10**243,
    'nonagintillion': 10**273,
    'centillion': 10**303,
    'googol': 10**100,
    'googolplex': 10**(10**100)
}
        self.numsWOutVal = [
    'zero','one','two','three','four','five','six','seven','eight','nine',
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


    def reco(self, text_nums):
        num = 0
        current_num = 0
        neg = 0
        nege = False
        if text_nums[0] == 'negative':
            neg = 1
            nege = True
        for x in range(len(text_nums)):
            if nege and x == len(text_nums):
                break
            word = text_nums[x + neg].lower()

            if word in self.numsWVal:
                if word in self.numsWOutVal[:28]:
                    current_num += self.numsWVal[word]

                elif word == 'hundred':
                    current_num *= 100
                
                elif word in self.numsWOutVal[29:]:
                    current_num *= self.numsWVal[word]
                    num += current_num
                    current_num = 0
        
        num += current_num
        if nege:
            num = -num
        return num