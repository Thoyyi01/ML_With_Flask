import pandas as pd
import numpy as np

internal_marks = [2, 4, 6,]
sleep_hrs = [1, 3, 5,]
stu_name = ["Karthi", "Dev", "Kanguva"]

M = {
    "Student Name!": stu_name,
    "Internal Marks": internal_marks,
    "Sleep Hrs": sleep_hrs
}

df = pd.DataFrame(M)
print(df)
