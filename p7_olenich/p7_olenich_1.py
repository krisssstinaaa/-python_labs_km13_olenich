
format_tuple = ('Liverpool', 845.15, 21, 134, 358.45, 'price')
format_string = "The initial lot {5} of ${4} at the {0} auction exceeded the expected {5} by {2}%, but the lot with number {3} was neveryheless sold for ${1}."
print(format_string.format(format_tuple[0], round(format_tuple[1]), format_tuple[2], str(format_tuple[3]).zfill(4), round(format_tuple[4], 1), format_tuple[5]))