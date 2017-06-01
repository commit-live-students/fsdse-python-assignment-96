# Select the rows where the number of attempts in the examination is greater than 2.

Write a Python program to select the rows where the number of attempts in the examination is greater than 2.

Sample DateFrame:

        exam_data = {
                'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
                'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
                'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
                'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
            }

        labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

Sample Output:

Select specific columns and rows:


|   |attempts       |name |qualify  |score|
|----|---------|---------|----------|--------|
|b  |       3  |     Dima  |    no  |  9.0  |
|d   |      3  |    James  |    no  |  NaN  |
|f   |      3  |  Michael  |   yes  | 20.0  |