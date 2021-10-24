import binascii as b
import globalvars as gv


def main():
	# with open(f'{gv.userin}{gv.usercountry}plot.png', 'rb') as f:
	with open(f'{gv.userin}{gv.usercountry}.png', 'rb') as f:
		content = f.read()

	print(b.hexlify(content))


if __name__ == '__main__':
	main()
