from datetime import datetime

def load_bad_words(filename):
    fin = open(filename,"r")
    
    bad_words = []
    count_rows = int(fin.readline())
    
    for _ in range(count_rows):
        current_word = fin.readline()
        current_word = current_word.replace("\n","")
        bad_words.append(current_word)

    fin.close()

    return bad_words

def load_input_text(filename):
    fin = open(filename,"r")
    input_text = fin.readlines()
    input_text = "".join(input_text)
    fin.close()

    return input_text

def delete_spam(bad_words, input_text):
    for current_bad_word in bad_words:
        input_text=input_text.replace(current_bad_word,"***")
    return input_text

def save_output_text(filename, output_text):
    fin = open(filename,"w")
    fin.write(output_text)
    fin.close()

def log(message):
    print(f"LOG {datetime.now()} --- {message}")

#--------

log("prorgam started")

bad_words = load_bad_words("bad_words.txt")
log("bad_words loaded")

input_text = load_input_text("input_text.txt")
log("input_text loaded")

output_text = delete_spam(bad_words, input_text)
log("spam deleted")

save_output_text("output_text.txt", output_text)
log("output_text saved")

log("prorgam finished")
