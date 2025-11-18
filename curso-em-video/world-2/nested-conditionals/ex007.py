# Exercise 007 - Nested Conditionals
# Write a program that read three numbers and informe if triangle is equilateral, isosceles or scalene.
# - Equilateral: all sides are equal
# - Isosceles: two sides are equal
# - Scalene: all sides are different

vertex1: float = float(input("Enter with first vextex: "))
vertex2: float = float(input("Enter with second vextex: "))
vertex3: float = float(input("Enter with third vextex: "))


def main() -> None:
    if has_possible_make_triangle():
        verify_triangle_type()
    else:
        print("Is not possible make a trangle")


def has_possible_make_triangle() -> bool:
    if (
        vertex1 + vertex2 <= vertex3
        or vertex1 + vertex3 <= vertex2
        or vertex2 + vertex3 <= vertex1
    ):
        return False

    return True


def verify_triangle_type() -> None:
    if vertex1 == vertex2 and vertex1 == vertex3:
        print("Equilateral")
    elif vertex1 != vertex2 and vertex1 != vertex3 and vertex3 != vertex2:
        print("Scalene")
    else:
        print("Isosceles")


main()
