import binascii as b
import globalvars as gv


def main():
	with open(f'{gv.userin}{gv.usercountry}plot.png', 'rb') as f:
		content = f.read()
	gv.img = str(b.hexlify(content))
	gv.img = gv.img[2:len(gv.img)-1]


if __name__ == '__main__':
	main()
