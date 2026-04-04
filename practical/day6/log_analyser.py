
def analyse_log(log_file):
    counts = {
        "info": 0,
        "warning": 0,
        "error": 0
    }
    try:
        with open(log_file) as f:
            lines = f.readlines()

            for line in lines:
                if "INFO" in line:
                    counts["info"] += 1
                elif "WARNING" in line:
                    counts["warning"] += 1
                elif "ERROR" in line:
                    counts["error"] += 1

            return counts
    except FileNotFoundError:
        print("File not found")
        exit()

filename = input("Please enter the file name:")
result = analyse_log(filename)
print(result)
total_errors = sum(result.values())

for key, value in result.items():
    # print(f"{key} %: ", value/total_errors*100)
    print(f"{key}: {value} ({(value/total_errors)*100:.2f} %)")
