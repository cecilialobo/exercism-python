def is_bulky(width, height, length):
    bulky_volume = (width * height * length) >= 1000000
    bulky_width = width >= 150
    bulky_height = height >= 150
    bulky_length = length >= 150

    return bulky_volume or (bulky_width or bulky_height or bulky_length)

def is_heavy(mass):
    return mass >= 20

def solve(width, height, length, mass):
    bulky = is_bulky(width, height, length)
    heavy = is_heavy(mass)

    if not bulky and not heavy:
        return 'STANDARD'
    if bulky and heavy:
        return 'REJECTED'
    if bulky or heavy:
        return 'SPECIAL'    