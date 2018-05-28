a =raw_input("")
try:
    b=float(a)
    print("Yes")

except (ValueError, TypeError):
    print("No")
