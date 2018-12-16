""" Data Pre-Processing Class """
__author__ = "Kovidnath Reddy, Pyla"
__status__ = "Development/Initial"
import csv
class DataPreprocess:
    def __init__(self, matrix):
        self.matrix = matrix

    def averages(self, filepath):
        features = self.matrix
        avg_a = 0
        avg_b = 0
        sum_a = 0
        sum_b = 0
        for feature in features:
            sum_a += feature[0]
            sum_b += feature[1]
        avg_a = float(sum_a / len(features))
        avg_b = float(sum_b / len(features))
        rows = [None] * 10
        final_list = []
        for feature in features:
            # For the first feature
            if feature[0] > avg_a:
                rows[0] = 1
                rows[1] = 0
                rows[2] = 0
            elif feature[0] < avg_a:
                rows[0] = 0
                rows[1] = 0
                rows[2] = 1
            elif feature[0] == avg_a:
                rows[0] = 0
                rows[1] = 1
                rows[2] = 0

            # For the second feature
            if feature[1] > avg_b:
                rows[3] = 1
                rows[4] = 0
                rows[5] = 0
            elif feature[1] < avg_b:
                rows[3] = 0
                rows[4] = 0
                rows[5] = 1
            elif feature[1] == avg_b:
                rows[3] = 0
                rows[4] = 1
                rows[5] = 0

            # Append to the final list
            final_list.append(rows)

        # Append the header to each
        final_list.insert(0, ['above_avg_a', 'at_avg_a', 'above_avg_b', 'below_avg_a', 'at_avg_b', 'below_avg_b'])
        with open(filepath, 'w', encoding='utf-8', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(final_list)

    # method for sorting values
    def sortarr(self, x, top_y, bottom_y):
        x.sort()
        return x[:top_y], x[-bottom_y:]



## These are just test cases I run for my convinence feel free to play around
obj = DataPreprocess([[1,2], [1,3], [1,4]])
obj.averages('C:\\Users\\pylak\\Documents\\Output.csv')
templist = obj.sortarr([1,5,2,4,5], 2, 2)
print(templist)

list1, list2 = obj.sortarr([1,2,4,6,3,5],2,2)

print(list1)
print(list2)
