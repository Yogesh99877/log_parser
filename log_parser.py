import csv

# Step 1: Read the log file
def parse_log(file_path):
    error_count = 0
    total_lines = 0
    error_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            total_lines += 1
            if "ERROR" in line:
                error_count += 1
                error_lines.append(line.strip())
    
    return total_lines, error_count, error_lines

# Step 2: Write summary to text file
def write_summary_txt(output_path, total, errors):
    with open(output_path, 'w') as f:
        f.write(f"Total lines: {total}\n")
        f.write(f"Error lines: {errors}\n")

# Step 3: Write summary to CSV
def write_summary_csv(output_path, total, errors):
    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Metric", "Value"])
        writer.writerow(["Total lines", total])
        writer.writerow(["Error lines", errors])  # ✅ Corrected this line

# Run everything
if __name__ == "__main__":
    log_file = "app.log"
    total, error_count, error_lines = parse_log(log_file)

    print("Summary:")
    print("Total lines:", total)
    print("Error lines:", error_count)

    write_summary_txt("summary.txt", total, error_count)
    write_summary_csv("summary.csv", total, error_count)

    # Optional: Save all error lines
    with open("error_lines.txt", 'w') as f:
        for line in error_lines:
            f.write(line + "\n")

