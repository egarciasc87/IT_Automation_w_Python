import re

text = "25/08/2022 text error [124345]. 25/08/2022 text error [127954]."

def get_code_error(string):
    start = string.index("[")
    end = string.index("]")
    code = string[start+1:end]
    return code

def get_code_error_reg_ex(string):
    regEx = r"\[(\d+)\]"
    code = re.search(regEx, string)
    return code[1]

def search_pattern(string):
    #result = re.search(r"ck", string)
    #result = re.search(r"[a-zA-Z]son", string)
    #result = re.search(r"[^a-z]", string)
    #result = re.findall(r"cat|dog", string)
    result = re.search(r".son", string)
    print("Text: {}, Result: {}".format(string, result))

list = ["Thompson", "Peterson", "Garcia", "McAdams",
    "Anderson", "cat", "cats and dogs"]

def rearrange_name():
    name = "test"

    while name != "":
        name = input("Enter name (LastName, FirstName): ")
        result = re.search(r"^(\w*), (\w*)$", name)

        if result is None:
            print("Not a match, end of the function...")
        else:
            result = "{} {}".format(result[2], result[1])
            print("Full name: {}".format(result))

def word_search():
    text = input("Enter name (LastName, FirstName): ")
    result1 = re.findall(r"[a-zA-Z]{5}", text)
    result2 = re.findall(r"\b[a-zA-Z]{5}\b", text)
    print("Match fraction/all word: {}".format(result1))
    print("Match only words: {}".format(result2))

#print("Code error by normal search:", get_code_error(text))
#print("Code error by RegEx:", get_code_error_reg_ex(text))
#textSearch = input("Enter text:")

#for text in list:
#    search_pattern(text)

#rearrange_name()

def extract_pid(log_line):
    regex = r"\[(\d+)\]|\b[A-Z]{1,}\b"
    result = re.findall(regex, log_line)
    if result is None:
        return None
    #return "{} ({})".format(result[1], result[2])
    return result

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None

#word_search()
