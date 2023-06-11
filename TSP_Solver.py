import math
import numpy as np
import random

class TSPSolver:
    # Khởi tạo lớp TSPSolver với phương thức khởi tạo __init__.
    def __init__(self, locations): 
        # Gán danh sách các địa điểm (locations) được truyền vào thành thuộc tính self.locations của lớp.
        self.locations = locations
        # Lưu số lượng địa điểm (num_locations)
        self.num_locations = len(locations)
        # Khởi tạo các thuộc tính self.visited, self.path, và self.distance 
        self.visited = []
        self.path = []
        self.distance = 0

    def solve_tsp(self, start):
        # Thiết lập tất cả các địa điểm chưa được đi qua
        self.visited = [False] * self.num_locations
        # Thiết lập các biến path và distance
        self.path = []
        self.distance = 0
        #Đánh dấu địa điểm ban đầu là đã được đi qua (visited) và thêm nó vào path.
        self.visited[start] = True
        self.path.append(start)
        #Gán giá trị hiện tại của start cho biến current 
        current = start
        # Bắt đầu vòng lặp để tìm kiếm địa điểm gần nhất chưa được thăm. 
        for _ in range(self.num_locations - 1):
            next_city = self.find_nearest_location(current)
            #Đánh dấu địa điểm gần nhất (next_city) là đã đi qua.
            self.visited[next_city] = True
            #Thêm địa điểm gần nhất vào đường đi (path).
            self.path.append(next_city)
            # Cập nhật khoảng cách bằng cách thêm khoảng cách từ current đến next_city vào distance.
            self.distance += self.locations[current][next_city]
            # Cập nhật current thành next_city để tiếp tục tìm kiếm địa điểm gần nhất.
            current = next_city
        # Tính khoảng cách từ địa điểm cuối cùng trở lại địa điểm ban đầu và thêm địa điểm ban đầu vào đường đi.
        self.distance += self.locations[current][start]
        self.path.append(start)
        # Trả về đường đi (path) và khoảng cách (distance).
        return self.path , self.distance

    def find_nearest_location(self, city):
        # Thiết lập nearest_location và min_distance thành giá trị khởi tạo ban đầu
        nearest_location = None
        min_distance = float('inf')
        # Duyệt qua tất cả các địa điểm. 
        for i in range(self.num_locations):
            # Nếu địa điểm đó chưa được đi qua và khoảng cách từ city đến địa điểm đó nhỏ hơn min_distance
            if not self.visited[i] and self.locations[city][i] < min_distance:
                # cập nhật nearest_location và min_distance
                nearest_location = i
                min_distance = self.locations[city][i]
        return nearest_location