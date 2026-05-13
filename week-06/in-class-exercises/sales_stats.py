import statistics

analyst_name = input("Enter your name: ")
region = input("Enter region: ")
daily_sales = []

for d in range(1, 8):
    dailysale = float(input("Enter daily sales: "))
    daily_sales.append(dailysale)

def analyze_sales(analyst, region, sales):
    mean = statistics.mean(sales)
    median = statistics.median(sales)
    mode = statistics.mode(sales)
    standard_dev = statistics.stdev(sales)
    total_sales = sum(sales)
    maximum = max(sales)
    minimum = min(sales)
    return mean, median, mode, standard_dev, total_sales, maximum, minimum

results = analyze_sales(analyst_name, region, daily_sales)

print(
    f"=== Weekly Sales Statistics Report ===\n"
    f"Analyst: {analyst_name}\n"
    f"Region: {region}\n"
    f"--- statistic calculations ---\n"
    f"mean         = {results[0]:.2f}\n"
    f"median       = {results[1]:.2f}\n"
    f"mode         = {results[2]:.2f}\n"
    f"standard dev = {results[3]:.2f}\n"
    f"total sales  = {results[4]:.2f}\n"
    f"maximum sale = {results[5]:.2f}\n"
    f"minimum sale = {results[6]:.2f}\n"
)