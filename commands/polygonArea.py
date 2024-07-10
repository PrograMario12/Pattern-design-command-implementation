from .command import Command;

class PolygonAreaCommand(Command):
    def execute(self):
        """
        Main function that executes the PolygonArea command.
        """
        print("This program calculates the area of a polygon given its vertices.")
        n = int(input("Enter the number of vertices: "))
        vertices = []
        for i in range(n):
            x, y = map(float, input(f"Enter the coordinates of vertex {i + 1}: ").split())
            vertices.append((x, y))
        area = self.calculate_area(vertices)
        print(f"The area of the polygon is {area}.")
        
    def calculate_area(self, vertices):
        """
        Function that calculates the area of a polygon given its vertices.
        """
        n = len(vertices)
        area = 0
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2
    
    def get_display_name(self):
        return "Polygon Area"
    
    