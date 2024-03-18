import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('ts-frienship-bracelets/taylor-swift-song-titles.csv')

# Take comma-separated array of letters as user input
input_str = input("Enter a comma-separated list of letters: ")

# Split the input string into an array of letters
letters_array = input_str.split(',')

# Output the array of letters
print(letters_array)

# Iterate through each value in the DataFrame and filter out values containing any letters in letters_array
filtered_values = []
for index, row in df.iterrows():
    value = row['track_title']  # Replace 'your_column_name' with the actual column name containing words or sentences
    if not any(letter in value for letter in letters_array):
        filtered_values.append(value)

# Create a new DataFrame with filtered values
new_df = pd.DataFrame(filtered_values, columns=['title'])

# Print the new DataFrame
print(new_df)