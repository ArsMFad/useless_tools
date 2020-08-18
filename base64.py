import string
letters = string.ascii_uppercase + string.ascii_lowercase + "0123456789+/"
alphabet = {}

for i in range(len(letters)):
	alphabet[letters[i]] = i


def encrypt(s):
	s_bin = ""

	for i in s:
		to_add = bin(ord(i))[2::]
		s_bin += "0" * (8 - len(to_add)) + to_add

	ravno_cnt = len(s_bin) % 3
	s_bin += (len(s_bin) % 3) * 2 * "0"


	to_ret = ""
	for i in range(0, len(s_bin), 6):
		to_ret += letters[int(s_bin[i:i + 6], 2)]

	to_ret += ravno_cnt * "="
	return to_ret


def decrypt(s):
	s_dec = []

	for i in s:
		if i == "=":
			break
		s_dec.append(alphabet[i])


	ravno_cnt = 0
	for i in range(len(s) - 1, 0, -1):
		if s[i] != "=":
			break
		ravno_cnt += 1


	s_bin = ""
	for i in s_dec:
		to_add = bin(int(i))[2::]
		s_bin += "0" * (6 - len(to_add)) + to_add

	to_ret = ""


	for i in range(0, len(s_bin), 8):
		to_ret += chr(int(s_bin[i:i + 8], 2))

	return to_ret


inp_str = input("Enter string: ")
cmd = input("Enter command [E]/[D]: ")
cmd = cmd.upper()

if cmd == "E":
	print(encrypt(inp_str))
elif cmd == "D":
	print(decrypt(inp_str))
else:
	print("[Error]: Wrong command")

