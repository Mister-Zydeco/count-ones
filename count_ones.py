
def count_ones(n: int) -> int:
    ones_count, power_of_ten = 0, 1
    while power_of_ten <= n:
        digit = n // power_of_ten % 10
        next_power_of_ten = 10 * power_of_ten
        n_blocks = n // next_power_of_ten
        if digit > 1:
            ones_count += (n_blocks + 1) * power_of_ten
        elif digit == 0:
            ones_count += n_blocks * power_of_ten
        else:
            ones_count += n_blocks * power_of_ten + n % power_of_ten + 1
        power_of_ten = next_power_of_ten
    return ones_count
