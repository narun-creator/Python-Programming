import numpy as np

numbers_list_arrays = np.array([10, 20, 30, 40, 50])
print(numbers_list_arrays)
print(type(numbers_list_arrays))

#tuple
numbers_tuple_arrays = np.array((10, 20, 30, 40, 50))
print(numbers_tuple_arrays)

# 0-d
simple_value_array = np.array(99)
print(simple_value_array)

# 1-d
student_scores_array = np.array([80, 85, 90, 95, 100])
print(student_scores_array)
# 2-D array
matrix_table_array = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(matrix_table_array)
print(type(matrix_table_array.shape))

cube_data_array = np.array([[[1,2,3],[4, 5, 6]],
                            [[7,8,9],[10,11,12]]])
print(cube_data_array)
print(cube_data_array.shape)