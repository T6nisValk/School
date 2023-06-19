def human_to_dog_years(human_years):
    dog_years = 0

    for year in range(1, human_years + 1):
        if year < 3:
            dog_years += 10.5
        else:
            dog_years += 4
    return int(dog_years)
