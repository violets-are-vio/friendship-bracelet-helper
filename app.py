from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load the CSV file into a DataFrame
df = pd.read_csv('taylor-swift-song-titles.csv')

@app.route('/filter', methods=['POST'])
def filter_song_titles():
    data = request.get_json()
    input_str = data['letters']
    
    # Split the input string into an array of letters
    letters_array = input_str.split(',')
    
    # Iterate through each value in the DataFrame and filter out values containing any letters in letters_array
    filtered_values = []
    for index, row in df.iterrows():
        value = row['track_title']  # Replace 'your_column_name' with the actual column name containing words or sentences
        if not any(letter in value for letter in letters_array):
            filtered_values.append(value)
    
    # Create a new DataFrame with filtered values
    new_df = pd.DataFrame(filtered_values, columns=['title'])
    
    # Convert DataFrame to a list of titles
    filtered_titles = new_df['title'].tolist()
    
    return jsonify(filtered_titles)

if __name__ == '__main__':
    app.run(debug=True)
