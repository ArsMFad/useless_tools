def decode(s):
	first_b = s[0]
	zero_cnter = 0

	s_bin_lens = []
	tmp = "1"

	i = 1
	while(i < len(s)):
		if s[i] == "1":
			i += 1
			while(zero_cnter != 0):
				tmp += s[i]
				i += 1
				zero_cnter -= 1
			s_bin_lens.append(tmp)
			tmp = "1"
			zero_cnter = 0
			i-=1
		elif s[i] == "0":
			zero_cnter += 1
		i += 1

	s_bin = ""
	now_b = first_b
	for i in range(len(s_bin_lens)):
		s_bin +=  int(s_bin_lens[i], 2) * now_b
		now_b = str(int(now_b) ^ 1)

	to_ret = ""
	for i in range(0, len(s_bin), 8):
		to_ret += chr(int(s_bin[i:i + 8], 2))

	return to_ret


def encode(s):
	s_bin = ""
	for i in s:
		to_add = bin(ord(i))[2::]
		s_bin += "0" * (8 - len(to_add)) + to_add

	first_b = "1" if s_bin[0] == "1" else "0"

	split_s_bin = []
	tmp = ""
	last_seen_sym = str(first_b)
	for i in s_bin:
		if i == last_seen_sym:
			tmp += i
		else:
			last_seen_sym = i
			split_s_bin.append(tmp)
			tmp = i
	split_s_bin.append(tmp)
	s_bin_lens = [len(i) for i in split_s_bin]

	to_ret = first_b
	for i in s_bin_lens:
		to_add = bin(int(i))[2::]
		to_ret += "0" * (len(to_add) - 1) + to_add

	return to_ret


inp_str = input("Enter number: ")
cmd = input("Enter command [E]/[D]: ")
cmd = cmd.upper()

if cmd == "E":
	print(encode(inp_str))
elif cmd == "D":
	print(decode(inp_str))
else:
	print("[Error]: Wrong command")
