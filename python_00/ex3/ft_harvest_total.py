def ft_harvest_total() -> None:
    harvest = 0
    for day in range(1, 4):
        harvest += int(input(f"Day {day} harvest: "))
    print("Total harvest:", harvest)
