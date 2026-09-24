KB = 1024
MB = 1048576
GB = 1073741824

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size = (num_entries * entry_size * 60) / KB
mb_size = (num_entries * entry_size * 60 * 60) / MB
gb_size = (num_entries * entry_size * 60 * 60 * 24) / GB

print("Storage Estimates:")
print(f"Per minute: {kb_size}KB")
print(f"Per hour: {mb_size}MB")
print(f"Per day: {gb_size}GB")