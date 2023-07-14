def convert(sentence):
    return sentence.replace(":)", "🙂").replace(":(", "🙁")
                         
def main():
    user_input = input()
    print(convert(user_input))

main()




