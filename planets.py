def main() -> None:
    weight = float(input('What do you weigh on Earth? '))
    mercury_weight = weight*0.38
    jupiter_weight = weight*2.53
    print(
        f'\nOn Mercury you would weigh {mercury_weight:.2f} pounds.\n'
        f'On Jupiter you would weigh {jupiter_weight:.2f} pounds.'
    )
    # return (f'What do you weigh on Earth? \nOn Mercury you would weigh {mercury_weight} pounds.\nOn Jupiter you would weigh {jupiter_weight} pounds.\n')


# NOTE: This means if the code is run as `python3 planets.py`, run the
# main function.  If the code is merely imported, don't do anything.
if __name__ == "__main__":
    main()