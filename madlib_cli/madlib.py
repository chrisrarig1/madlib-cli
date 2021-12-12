from textwrap import dedent
import re
import os

# test_path = './assets/dark_and_stormy_night_template.txt'
test_path = './assets/make_me_a_video_game_template.txt'
new_path = './saved_madlibs/new_madlibs.txt'

message = dedent("""
************Welcome to Madlibs!!***************
In this program you will be prompted to provide
words to fill in blanks to complete a story.
Once all words are provided the story will then be 
returned.""")

print(message)

def read_template(test_path):
    with open(test_path) as file:
         contents = file.read()
    return contents


results = read_template(test_path)


def parse_template(results):
  regex = r'\{[^}]*\}'
  words = tuple(re.findall(regex,results))
  text = re.sub(regex, '{}', results)
  return(text,words)

questions = parse_template(results)[1]
empty_string = parse_template(results)[0]

def answers(questions):
    responses = []
    for i in questions:
        resp = input(f'Please enter a {i} > ')
        responses.append(resp)
    return responses


responses = answers(questions)

def merge(empty_string,responses):
    return empty_string.format(*responses)




def new_file(final):
        with open(new_path, "w") as file:
            file.write(final)


       


if __name__== "__main__":
    read_template(test_path)
    parse_template(results)
    final = merge(empty_string,responses)
    print(f"""*****Your finished MadLib*******
                {final}""")
    new_file(final)

# print(contents[9:20])