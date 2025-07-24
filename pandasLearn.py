import sys
import pandas as pd

class PandasWrapper():
    def __init__(self):
        pass

    def version(self):
        print("\t\t\t **PD Version** \t\t\t")
        return pd.__version__

    def csv(self):
        print("\t\t\t **Read CSV** \t\t\t")
        df = pd.read_csv("Org Users.csv")
        return df.to_string()

    def CreateSeries(self):
        print("\t\t\t **one-dimensional array** \t\t\t")
        one_Diamond_array = [1, 5 , 3, 10]
        arr_myseries = pd.Series(one_Diamond_array, index=["x","y","z","A"])
        one_Diamond_Json = {"Name": "Fai", "Age": 18}
        json_myseries = pd.Series(one_Diamond_Json)
        print(arr_myseries["y"])
        print(json_myseries)

    def createDataFram(self):
        print("\t\t\t **DataFrame** \t\t\t")
        myFram = pd.DataFrame(
            {
                'Customer Name':["Mohamed","Faiyas", "Ali"],
                'Customer Age':[20,22, 17],
                'Amount':[10000,9000, 1000]
            },index=["Sno1","Sno2","Sno3"])
        print(myFram)
        print("\t\t\t **DataFrame use Loc Atttribute** \t\t\t")
        print(myFram.loc["Sno3"])
        print(myFram.loc[["Sno1","Sno2"]])

pan_obj = PandasWrapper()
# methods = [method for method in dir(pan_obj) if callable(getattr(pan_obj, method)) and not method.startswith("__")]
# print(methods)
methods = [method for method in dir(pan_obj) if not method.startswith("__")]
methods.insert(0, 'Exit')
while True:
    print([f'{method_name} - {methods.index(method_name)}' for method_name in methods])
    filter_var = int(input('Enter the values:'))
    for methName in methods:
        if methods.index(methName) == filter_var:
            if filter_var == 0:
                sys.exit()
            callAttr = getattr(pan_obj, methName)
            if callable(callAttr):
                try:
                    print(callAttr())
                except Exception as e:
                    print(f"Error calling {methName}():", e)
                break



