# import pafy

# url = 'https://www.youtube.com/playlist?list=PLDzeHZWIZsTr3nwuTegHLa2qlI81QweYG'
# video = pafy.new(url)
# best = video.getbest()
# best.download(filepath='/Users/kirtan/Desktop/code/python/youtube')


# import time
# import winsound

# import platform

# if platform.system() == 'Windows':
#     import winsound



# binary = input("Binary input: \n")
# for i in binary:
# 	if i == "0":
# 		winsound.Beep(2000, 100)
# 	if i == "1":
# 		winsound.Beep(4000, 100)
# 	time.sleep(0.1)
# exit()

import time
import platform

binary = input("Binary input: \n")


def play_beep(frequency, duration):
    if platform.system() == 'Windows':
        import winsound
        winsound.Beep(frequency, duration)

def validate_binary(binary_input):
    return all(bit == '0' or bit == '1' for bit in binary_input)

if validate_binary(binary):
    for bit in binary:
        if bit == '0':
            play_beep(2000, 100)
        elif bit == '1':
            play_beep(4000, 100)
        time.sleep(0.1)
else:
    print("Invalid binary input. Please enter only '0' and '1' characters.")
