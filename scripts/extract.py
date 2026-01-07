import pandas as pd
#pd.set_option("display.max_columns",None)
#pd.set_option("display.max_rows",None)
def load_data():
    data=pd.read_csv(r"K:\Ml Projects\Placement Predictor\career-path-pro\data\college_student_placement_dataset.csv")
    return data

    