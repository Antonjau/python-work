def main():
    fraction = input('Enter the fraction of the fuel tank that is filled (in X/Y format): ')
    try:
        percentage = convert(fraction)
        gauge_str = gauge(percentage)
        print(f'The fuel gauge reads: {gauge_str}')
    except (ValueError, ZeroDivisionError) as e:
        print(f'Error: {e}')

def convert(fraction):
    try:
        x, y = map(int, fraction.split('/'))
    except ValueError:
        raise ValueError('Invalid fraction format')
    if x > y:
        raise ValueError('X must be less than or equal to Y')
    if y == 0:
        raise ZeroDivisionError('Y cannot be zero')
    percentage = round(x / y * 100)
    if percentage < 0 or percentage > 100:
        raise ValueError('Percentage must be between 0 and 100')
    return percentage


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()