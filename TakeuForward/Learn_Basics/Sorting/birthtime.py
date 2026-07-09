from datetime import datetime
birth_input = input("Enter birth date (YYYY-MM-DD): ")
birth = datetime.strptime(birth_input, "%Y-%m-%d")
end = datetime.now()
diff = end - birth


days = diff.days
hours = diff.total_seconds() / 3600
print(end)
print("\nCurrent Date & Time:", end.strftime("%Y-%m-%d %H:%M"))
print(f"Days: {days}")
print(f"Hours: {hours:.2f}")