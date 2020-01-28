
# Created by inc0gnit0 #

# Please give me credit if you use it #


# MODULES #

try:

	import pytube

	import time

	import os

	import random

except ImportError:

	print("  You did not follow the instructions")

	print("\n")

	print("  I will do them for you...")

	time.sleep(3)

	os.system("chmod +x * && sudo ./install.sh")



# COLORS #

red = "\u001b[31;1m"

reset = "\u001b[0;1m"

green = "\u001b[32;1m"

cyan = "\u001b[36;1m"

yellow = "\u001b[33;1m"

magenta = "\u001b[35;1m"

blue = "\u001b[34;1m"

white = "\u001b[37;1m"

list = ["\u001b[31;1m", "\u001b[32;1m", "\u001b[36;1m", "\u001b[33;1m", "\u001b[35;1m", "\u001b[34;1m", "\u001b[37;1m"] # List of colors to chose from #

pwd = os.getcwd



# MAIN #

def main():

	os.system("clear")

	for x in range(5): # Loading Effect #

		print(random.choice(list) + "|")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "/")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "-")

		time.sleep(0.1)

		os.system("clear")

		print(random.choice(list) + "\\")

		time.sleep(0.1)

		os.system("clear")

	print(random.choice(list) + "  loader is starting")

	time.sleep(3)



	os.system("clear") # Clear the terminal #



	# DOWNLOAD #

	def download():

		print("\n")

		link = input(random.choice(list) + "  Enter the link of the Youtube video(ex: www.youtube.com): ")

		yt = pytube.YouTube(link)

		vid = yt.streams.first()

		try:

			vid.download()

		except:

			print("\n")

			print(random.choice(list) + "  Errors occured")

			time.sleep(3)

			os.system("clear")

			exit(1)

		print("\n")

		print(random.choice(list) + "  Download completed!")

		print("\n")

		print(random.choice(list) + """  The vidoe will be save to the "loader" folder""")

		time.sleep(3)

		os.system("clear")

		main()



	# MP4 to MP3 #

	def mp4mp3():

		print(random.choice(list) + "  If your file has spaces in it, make sure it is wrapped in quotes")

		print("\n")

		print(random.choice(list) + "  Example: \"this has spaces.mp4\"")

		print("\n")

		def convertion():

			mp4 = input(random.choice(list) + "  Enter the full path of the mp4 file(ex: /home/inc0gnit0/example.mp4): ")

			print("\n")

			mp3 = input(random.choice(list) + "  Enter the full name you the output to be(ex: example.mp3): ")

			os.system("ffmpeg -i" + " " + mp4 + " " + mp3) # Command to convert #

			print("\n")

			print(random.choice(list) + "                                Convertion completed!!")

			print("\n")

			print(random.choice(list) + "                            File is saved to " + random.choice(list) + os.getcwd() + "\n" + random.choice(list) + mp3)

			time.sleep(3)

			main()


		convertion()



	# MP4 to WAV #

	def mp4wav():

		print(random.choice(list) + "  If your file has spaces in it, make sure it is wrapped in quotes")

		print("\n")

		print(random.choice(list) + "  Example: \"this has spaces.mp4\"")

		print("\n")

		def convertion():

			mp4 = input(random.choice(list) + "  Enter the full path of the mp4 file(ex: /home/inc0gnit0/example.mp4): ")

			print("\n")

			wav = input(random.choice(list) + "  Enter the full name you want the output to be(ex: example.wav): ")

			os.system("ffmpeg -i" + " " + mp4 + " " + wav) # Command to convert #

			print("\n")

			print(random.choice(list) + "                                Convertion completed!!")

			print("\n")

			print(random.choice(list) + "                            File is saved to " + random.choice(list) + os.getcwd() + "\n" + random.choice(list) + wav)

			time.sleep(3)

			main()


		convertion()



	# MP3 to WAV #

	def mp3wav():

		print(random.choice(list) + "  If your file has spaces in it, make sure it is wrapped in quotes")

		print("\n")

		print(random.choice(list) + "  Example: \"this has spaces.mp3\"")

		print("\n")

		def convertion():

			mp3 = input(random.choice(list) + "  Enter the full path of the mp3 file(ex: /home/inc0gnit0/example.mp3): ")

			print("\n")

			wav = input(random.choice(list) + "  Enter the full name you want the output to be(ex: example.wav): ")

			os.system("ffmpeg -i" + " " + mp3 + " " + wav) # Command to convert #

			print("\n")

			print(random.choice(list) + "                                Convertion completed!!")

			print("\n")

			print(random.choice(list) + "                            File is saved to " + random.choice(list) + os.getcwd() + "\n" + random.choice(list) + wav)

			time.sleep(3)

			main()


		convertion()



	# BANNER #

	print("\n")
	print(random.choice(list) + "                                https://github.com/iinc0gnit0/loader")
	print("\n")
	time.sleep(0.1)
	print(random.choice(list) + "                                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                88888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888            888888888                    8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "    888888888888              888888888                  8888888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                  888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                    888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                      88888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                        888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                          888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                            888888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                              888888888")
	time.sleep(0.1)
	print(random.choice(list) + "          88                    888888                    88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                               88   888                        88   88   888")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88888888  888888  88  8 88  888888  88888888 88 888888 88  8 88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 8        88 8  88 88    88 88    88 88   88   88 8  88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88 88    88 888  888 88    88 88    88 88   88   888   88")
	time.sleep(0.1)
	print(random.choice(list) + "          88 88    88  888888   888888   8888888 88    88 88   88    888888")
	time.sleep(0.1)
	print(random.choice(list) + "                                             888")
	time.sleep(0.1)
	print(random.choice(list) + "                                         888888" + red + "                                v4.0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Created by: inc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     GitHub: iinc0gnit0")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Email: iinc0gnit0@pm.me")
	time.sleep(0.1)
	print("\n")
	print(random.choice(list) + "                                     Instagram: inc0gnit0.offical")
	time.sleep(0.1)
	print("\033[0m")

	print(random.choice(list) + "=========================================================================================================")

	print("")

	print(random.choice(list) + "                                    1. Download YouTube video")

	print("\n")

	print(random.choice(list) + "                                          2. mp4 to mp3")

	print("\n")

	print(random.choice(list) + "                                          3. mp4 to wav")

	print("\n")

	print(random.choice(list) + "                                          4, mp3 to wav")

	print("\n")

	print(random.choice(list) + "                                             0. Exit")

	print("\n")

	choice = input(random.choice(list) + "                                            loader -> ")

	if choice in "1":

		download()

	elif choice in "2":

		mp4mp3()

	elif choice in "3":

		mp4wav()

	elif choice in "4":

		mp3wav()

	elif choice in "0":

		print("\n")

		print(random.choice(list) + "  Thank you for using loader! Have a nice day")

		print("\n")

		exit(0)

	else:

		print(random.choice(list) + "  Invalid option, Quiting...")

		exit(0)



# START #

try:

	if __name__ == "__main__":

		main()

except KeyboardInterrupt: # Catch KeyboardInterruption errors #

	print("\n")

	print("  KeyboardInterrupt detected, Exiting...")

	print("\n")

	print(random.choice(list) + "  Have a nice day!! \033[0m")

	print("\n")

	time.sleep(3)

	os.system("clear")

	exit(1)
