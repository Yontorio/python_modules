def ft_count_harvest_iterative() -> None:
    days = int(input("Days until harvest: "))
    count = days
    while count > 0:
        count -= 1
        print(f"Day {days - count}")
    print("Harvest time!")
