def draw_square(n):
    print((" " * (n-1)) + ("*" * n))
    for i in range(n - 2):
        print((" " * (n-1)) + ("*") + (" " * (n - 2)) + ("*"))
    print((" " * (n-1)) + ("*" * n))

def draw(n):
    max_space_width = n + (2 * (n - 1))
    
    # draw upper part
    for i in range(n - 1):
        space_width = max_space_width - (2 * (i + 1))
        print((" " * i) + ("*") + (" " * space_width) + ("*"))

    # # draw middle part
    draw_square(n)

    # draw lower part
    for i in range(n - 1, 0, -1):
        space_width = max_space_width - (2 * (i))
        print((" " * (i-1)) + ("*") + (" " * space_width) + ("*"))


x = int(input())
draw(x)
