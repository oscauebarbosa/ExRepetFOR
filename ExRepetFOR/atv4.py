numero = 0
for fatores in range(5, 101):
    if fatores % 7 == 0 and fatores % 5 != 0:
        print(fatores, end=" ")
        numero += 1

print("\nNo visor, possui", numero, "fatores")