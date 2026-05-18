all_calculations = ['10m is 16km', '50km is 31m', '15km is 9m']

newest_first = list(reversed(all_calculations))


print("==== Oldest to Newest for File ====")
for item in all_calculations:
    print(item)

print()

print("==== Most Recent First ===")
for item in newest_first:
    print(item)