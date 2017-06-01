import data
import compare 

inequality = ""

for item in compare.ratio_list:
    if not item[0] == "pallidBat":
        inequality = inequality + f" < {item[0]}"
    else:
        inequality = "pallidBat"
    print(f"{item[0]} : {item[1]}%")
    
print(f"\n {inequality}")
