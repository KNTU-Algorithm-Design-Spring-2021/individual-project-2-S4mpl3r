def breakTheSentence(sentence, dict, dp={}):
    if sentence in dp:
        return dp[sentence]
    if not sentence:
        return []

    result = []
    for word in dict:
        if not sentence.startswith(word):
            continue
        if len(word) == len(sentence):
            result.append(word)
        else:
            resultOfTheRest = breakTheSentence(
                sentence[len(word):], dict, dp)
            for item in resultOfTheRest:
                item = word + ' ' + item
                result.append(item)
    dp[sentence] = result
    return result


def readFile(dict, filename='./The_Oxford_3000.txt'):
    file = open(filename, 'r')
    text = file.readlines()
    for line in text:
        dict[line.strip().lower()] = line.strip().lower()
    file.close()


if __name__ == '__main__':
    dict = {}
    # CHANGE ME
    sentence = "CALLSECURITYATMIAMIAIRPORTBECAUSEITHINKTHEBOMBISABOUTTOGOOFF"
    readFile(dict)
    result = breakTheSentence(sentence.lower(), dict)
    for i in result:
        print(i)
