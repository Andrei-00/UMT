def nr_of_rectangles(points):
    # Initialize the variable for counting the rectangles
    nr = 0

    # Iterate through all the points twice by using a nested for loop
    # x1, y1 will be the upper left corner and x4, y4 the bottom right corner
    for x1, y1 in points:
        for x4, y4 in points:
            # Check if the upper right and lower left corner exist in order to form a rectangle
            x2, y2 = (x1, y4)  # Upper right corner
            x3, y3 = (x4, y1)  # Lower left corner
            # Check if points are valid
            if x1 == x4 or y1 == y4 or x1 > x4 or y1 > y4:
                continue
            # Check if these points exist
            if points.get((x2, y2)) is not None and points.get((x3, y3)) is not None:
                # Increase the count
                nr = nr + 1
    return nr


def check_split(n, a_list, b_list, c_list):  # Brute force approach
    if n == 0:
        if len(b_list) > 0 and len(c_list) > 0:
            m1 = sum(b_list) / float(len(b_list))
            m2 = sum(c_list) / float(len(c_list))
            if m1 == m2:
                print(b_list)
                print(c_list)
                return True
        return False

    b = b_list.copy()
    c = c_list.copy()
    b.append(a_list[n-1])
    c.append(a_list[n-1])
    if check_split(n-1, a_list, b, c_list):
        return True
    if check_split(n-1, a_list, b_list, c):
        return True

    return False


if __name__ == '__main__':
    # Count the number of rectangles problem
    # Save the points in a dictionary
    points_dict = {(1, 1): (1, 1), (1, 3): (1, 3),
                   (2, 1): (2, 1), (3, 1): (3, 1),
                   (2, 3): (2, 3), (3, 3): (3, 3)}

    print(nr_of_rectangles(points_dict))

    # Check if list B and C exist problem
    a_list = [1, 2, 3, 4, 5, 6, 7, 8]
    b_list = []
    c_list = []

    print(check_split(len(a_list), a_list, b_list, c_list))
