import math
def main():
	x = 1000
	step = 2*math.pi/(x-1)
	print("  x  |  sin(x)")
	print("--------------")

	for i in range(x):
		x = i*step
		s = math.sin(x)
		print(f"  {x:.4f}  |  {s:.4f}")

if __name__ == "__main__":
	main()

