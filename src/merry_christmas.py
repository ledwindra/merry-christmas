import sys

class MerryChristmas():

    def __init__(self):
        
        self.bold = "\033[1m"
        self.unbold = "\033[0m"
        self.header = f"\t{self.bold}Merry Christmas and Happy Holidays!{self.unbold}"
        self.height = int(sys.argv[1])
        self.end = sys.argv[2]
        self.name = sys.argv[3]
        self.footer = f"\t{self.bold}{self.end},\n\n\t{self.name}{self.unbold}"
    
    def get_triangle(self):
        "Returns a triangle"

        triangle = []
        i = 0

        while i < self.height:
            if i % 2 != 0:
                triangle.append('\U0001F384' * i)
            i += 1

        return triangle
    
    def main(self):

        print(self.header, "\n")

        for i in range(len(triangle)):
            triangle[i] = ' ' * (len(triangle) - (i + 1)) + triangle[i]
            print("\t\t", triangle[i])

        trunk = triangle[0]
        i = 0
        # assume the trunk height is 1/5 of triangle height
        while i < (self.height / 5):
            print("\t\t", trunk)
            i += 1

        print("\n", self.footer)

if __name__ == '__main__':
    print("\n")
    triangle = MerryChristmas().get_triangle()
    MerryChristmas().main()
    print("\n")
