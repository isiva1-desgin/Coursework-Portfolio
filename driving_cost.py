

num_MPG = float(input())
num_CostPG = float(input())
num_20Miles = 20 / num_MPG * num_CostPG
num_75Miles = 75 / num_MPG * num_CostPG
num_500Miles = 500 / num_MPG * num_CostPG
print(f"{num_20Miles:.2f} {num_75Miles:.2f} {num_500Miles:.2f}")