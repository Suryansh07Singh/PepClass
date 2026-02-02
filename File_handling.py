'''with open("sample.txt", "rt") as file:
    content = file.read()
    print(content)'''

f = open("file.txt", "r")
# f.write("Hello Python\n")
# f.write("File Handling")
print(f.read())
f.close()



# import json
# from pydoc import text
# # open JSON file
# with open("data.json", "rt") as file:
#     json.dump(text, file)