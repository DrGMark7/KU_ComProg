""" arrow = R ,size = 3 , times = 2
*  *
** **
******
** **
*  *
"""

def print_arrow(size: int, n: int, left: bool) -> None:
  fmt_str = "{:>{}}" if left else "{:<{}}"
  for i in (*range(1, size+1),*range(size-1, 0, -1),):
    print(fmt_str.format("*"*i, size)*n)

def main() -> None:
  arrow_size = int(input())
  arrow_n = int(input())
  arrow_left = True if input().lower() == "l" else False
  print_arrow(arrow_size, arrow_n,True)  

if __name__ == "__main__":
  main()