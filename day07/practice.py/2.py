import time

# Create a list of 100,000 fake account numbers
accounts_list = []

# Create a dictionary of 100,000 fake account numbers
accounts_dict = {}

for i in range(100000):
    account = f"CBE-{i}"
    accounts_list.append(account)
    accounts_dict[account] = i

target = "CBE-99999"

# List lookup
start = time.time()

for account in accounts_list:
    if account == target:
        break

end = time.time()

print("List lookup:", end - start, "seconds")

# Dictionary lookup
start = time.time()

accounts_dict[target]

end = time.time()

print("Dictionary lookup:", end - start, "seconds")