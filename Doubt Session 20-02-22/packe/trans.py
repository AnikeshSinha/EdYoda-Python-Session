# Let's check first i can create my file or not

# with open('text.txt' , mode = 'w') as my_file:
#     print(my_file.write())


# Let's check first i can read my file or not
# with open('text.txt' , mode = 'r') as my_file:
#     print(my_file.read())

# Let's install the package now

# Use as a Python Module

# from translate import Translator

# translator= Translator(to_lang="hi")
# from translate import Translator

# with open('text.txt' , 'r') as my_file:
#     # print(my_file.read())
#     text = my_file.read()
#     translation = translator.translate(text)
#     print(translation)

# ---------- Translate and write in another file--------

# from translate import Translator

# translator= Translator(to_lang="hi")

# with open('text.txt' , 'r') as my_file:
#     # print(my_file.read())
#     text = my_file.read()
#     translation = translator.translate(text)
#     # print(translation)
#     with open('text-hi.txt' , 'w+',encoding="utf-8") as my_file2:
#         my_file2.write(translation)

from translate import Translator

translator= Translator(to_lang="ko")

with open('text.txt' , 'r') as my_file:
    # print(my_file.read())
    text = my_file.read()
    translation = translator.translate(text)
    # print(translation)
    with open('text-ko.txt' , 'w+',encoding="utf-8") as my_file2:
        my_file2.write(translation)