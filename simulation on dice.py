import random
dice = [1,2,3,4,5,6]

ss = []
N = 1000000
for i in range(N):
	sample = random.choice(dice)
	ss.append(sample)
	
counter = 0
for i in range(len(ss)):
	if ss[i] == 1:
		counter += 1
print(f"Probability for '1'  {(counter/N) * 100:.1f}")