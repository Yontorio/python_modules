def ft_count_harvest_recursive() -> None:
    def countDays(days):
        if days == 0:
            return
        countDays(days - 1)
        print(f"Day {days}")
    countDays(int(input("Days until harvest: ")))
    print("Harvest time!")
