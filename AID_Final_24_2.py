import os
import streamlit as st
import pandas as pd
import requests


# github_token = st.secrets["GITHUB_TOKEN"]
# headers = {"Authorization": f"token {github_token}"}

exam_title = "2024 Fall Artificial Intelligence Design"
fname = "AID_Midterm_Grading.xlsx"
#response = requests.get(fname, headers=headers)
solution = '''
## Solution
#### 1. (10p - 2p each)
    (a) T
    (b) F
    (c) F
    (d) F
    (e) T

#### 2. (8p - 2p each)
    (a) Active Learning
    (b) Ensemble Learning
    (c) Reinforcement Learning
    (d) Reproducibility

#### 3. (10p)
    (a) - 4p
    df_join = pd.concat([df1, df2])
    
    (b) - 3p
    "df.loc" is label-based indexing, allowing you to access rows and columns using labels or boolean arrays.
    "df.iloc", on the other hand, is integer-based indexing, where you select rows and columns by their integer position.

    (c) - 3p
    dump

#### 4. (8p - 4p each)
    (a)
    Solution1.
    def euclidean_distance(row1, row2):
        distance = math.sqrt(sum((x-y)**2 for x, y in zip(row1[:-1], row2[:-1])))
        return distance

    Solution2.
    def euclidean_distance(row1, row2):
        distance = 0.0
        for i in range(len(row1) - 1):
            distance += (row1[i] - row2[i]) ** 2
        return math.sqrt(distance)

    (b)
    k-fold cross-validation splits the dataset into k folds, trains the model on k-1 folds,
    validates on the remaining fold, and averages the results for a robust performance estimate.
    

#### 5. (10p)
    (a) - 6p
    (1)-Y, (2)-Z, (3)-X

    (b)
    def z_score_normalize_2d(array):
        column_means = np.mean(array, axis = 0)
        coulmn_stds = np.std(array, axis = 0)
        if (np.any(column_stds == 0)):
            raise ValueError("Standard deviation of zero found in one or more columns.")
        normalized_array = (array - column_means) / column_stds
        return normalized_array
     

#### 6. (14p)
    (a) - 4p
    false positive: 25 (Predicted class: yes, True class: no)
    true negative: 375 (Predicted class: no, True class: no)
    
    (b) - 6p
    precision: 1/2
    TP/TP+FP= 25/25+25
            = 25/50
            = 1/2
    
    recall = 1/4
    TP/TP+FN= 25/25+75
            = 25/100
            = 1/4
    
    F1 = 1/3
    2*(precision*recall)/(precision+recall) = (2*1/2*1/4)/(1/2+1/4)
                                            = (1/4)/(3/4)
                                            = 1/3
    
    (c) - 4p
    accurcay = 4/5
    (TP+TN)/(TP+FP+TN+FN) = (25+375)/(25+25+375+75)
                          = 400/500
                          = 4/5

    balance accuracy = 19/32
    (1/2)*(TP/(TP+FN) + TN/(TN+FP)) = (1/2)*(25/(25+75) + 375/(375+25))
                                    = (1/2)*(25/100 + 375/400)
                                    = (1/2)*(475/400)
                                    = 475/800
                                    = 19/32

#### 7. (15p)
    (a) - 11p
    product_a = df[df['Product'] == 'A']
    product_b = df[df['Product'] == 'B']

    plt.plot(product_a['Date'], product_a['Sales'], marker='o', label='Product A')
    plt.plot(product_b['Date'], product_b['Sales'], marker='o', label='Product B')

    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Daily Sales Trends for Each Product')
    plt.legend()
    
    plt.show()
    
    (b) - 4p
    Solution1.
    x_indices = np.array([0,1,2,3])
    plt.plot(x_indices, xaxis, linestyle='--', marker='o')
    plt.show()

    Solution2.
    plt.plot(xaxis, linestyle='--', marker='o')
    plt.show()

#### 8. (12p)
    (a) - 3p
    The entrypoint file in a Streamlit project (typically streamlit_app.py or app.py) is the main script that runs when the app starts,
    defining the primary interface. Additional pages are organized as separate Python files in a pages directory,
    and Streamlit automatically detects and displays them as navigation options.
    
    (b) - 9p
    (1) fruit = st.radio("What is your favorite fruit?", options = ["Apple", "Banana", "Cherry"])

    (2) name = st.text_input("Enter your name: ")

    (3) rating = st.slider("Rate your satisfaction (1-10): ", 1, 10, 5)

#### 9. (13p)
    (a) - 3p
    A virtual environment isolates a project's dependencies from the system-wide Python installation,
    ensuring that different projects can have their own specific versions of libraries without conflicts.
    This helps maintain a clean development environment and prevents dependency issues.

    (b) - 4p
    conda create --name final python=3.10

    (c) - 6p
    Solution1.
    ### Features
    - **View current weather.**
    - *Check the weekly forecast.*
    - Get weather alerts.
    ### Example Usage
    ```bash
    python weather_app.py
    ```

    Solution2.
    ### Features
    - **View current weather.**
    - _Check the weekly forecast._
    - Get weather alerts.
    ### Example Usage
    ```
    python weather_app.py
    ```

'''

# Setup Title & Wide layout
st.set_page_config(page_title=exam_title, layout="wide")
st.markdown(
    """
    <style>
    textarea {
        font-size: 2rem !important;
    }
    input {
        font-size:1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
# Load the Excel data
df = pd.read_excel(fname, dtype={'Student ID': 'Int64', '1 - 10p': 'Int64', '2 - 8p': 'Int64', '3 - 10p': 'Int64', '4 - 8p': 'Int64', '5 - 10p': 'Int64', '6 - 14p': 'Int64', '7 - 15p': 'Int64', '8 - 12p': 'Int64', '9 - 13p': 'Int64', '총점': 'Int64'})

def get_student_data(student_id):
    """
    Fetch the data for a given student ID from the Excel file.
    
    Args:
    - student_id (int): The ID of the student.
    
    Returns:
    - pd.DataFrame or None: The data for the student if found, otherwise None.
    """
    student_data = df[df["e-mail"] == student_id]
    if len(student_data) > 0:
        return student_data
    else:
        return None

# Streamlit app layout and logic
st.title(exam_title)

# Get the student ID from the user
student_id = st.text_input("Please enter your email and press the Enter key.", value='hwanheelee@cau.ac.kr')

# When the user provides a student ID, fetch and display the data
if student_id:
    data = get_student_data(student_id)
    
    if data is not None:
        to_show = data.set_index("e-mail")
        st.write("E-mail: ", to_show.index[0])
        s = to_show.style.format({"Expense": lambda x : '{:.4f}'.format(x)})
        st.dataframe(s, hide_index=True)
    else:
        st.write(f"No data found for email: {student_id}")
        
st.write(solution)