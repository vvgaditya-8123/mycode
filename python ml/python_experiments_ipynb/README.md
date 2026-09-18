# Python & Machine Learning Experiments — Aditya

Converted from the 10 uploaded PDF experiment files into Jupyter Notebook (`.ipynb`) format.

## Notebooks
1. `01_LIST_Operations.ipynb`
2. `02_TUPLE_Operations.ipynb`
3. `03_DICTIONARY_Operations.ipynb`
4. `04_Data_Preprocessing.ipynb`
5. `05_Linear_Regression_Salary.ipynb`
6. `06_Multilinear_Regression_Home_Price.ipynb`
7. `07_Titanic_Missing_Values.ipynb`
8. `08_Logistic_Regression_Insurance.ipynb`
9. `09_Iris_Logistic_Regression.ipynb`
10. `10_SVM_Iris.ipynb`

## Name change
Personal name values from the source experiments have been standardized to `Aditya`.

## Dataset files referenced by the original PDFs
The notebooks that read external CSV files expect:
- `insurance_data.csv`
- `home_price.csv`
- `Salary_Data.csv`
- `titanic_Data_Train.csv`
- `data_preprocessing.csv`

These CSVs were not among the uploaded PDFs, so they are referenced by the same filenames rather than fabricated.

## Note on Titanic
The source PDF reuses the same dataframe object across several missing-value demonstrations. This converted notebook uses `.copy()` for each technique so that one demonstration does not modify the dataframe used by the next technique. The techniques and columns follow the source experiment.
