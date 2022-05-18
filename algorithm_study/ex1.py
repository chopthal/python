from typing import Dict
memo: Dict[int, int] = {0:0, 1:1}

def fib1(n:int) -> int:
	if n<2:
		return n
	return fib1(n-1) + fib1(n-2)


def fib3(n: int) -> int:
	if n not in memo:
		memo[n] = fib3(n-1) + fib3(n-2)
	return memo[n]


if __name__ == "__main__":
	print(fib3(5))	
	print(fib3(10))	