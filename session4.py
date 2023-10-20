import sys

class favanimal():
	def print(self):
		print("This is my favorite animal!")
		print(f"The length of the arms of the the animal is {self.arms}.")
		print(f"The length of the legs of the the animal is {self.legs}.")
		print(f"The number of eyes it has is {self.eyes}.")
		print(f"Does it have a tail? {self.tail}.")
		print(f"Is it furry? {self.fur}.")

	def __init__(self,a,b,c,d,e):
		self.arms = a
		self.legs = b 
		self.eyes = c 
		self.tail = d 
		self.fur = e 

def main():
		a = 0
		b = 0
		c = 0
		d = 0
		e = 0
		if(len(sys.argv)>=0):
			a = float(sys.argv[1])
		if(len(sys.argv)>=0):
			b = float(sys.argv[2])
		if(len(sys.argv)>=0):
			c = int(sys.argv[3])
		if(len(sys.argv)>=0):
			d = bool(sys.argv[4])
		if(len(sys.argv)>=0):
			e = bool(sys.argv[5])

		animals = favanimal(a=a,b=b,c=c,d=d,e=e)
		animals.print()
if __name__ == "__main__":
		main()


		
	