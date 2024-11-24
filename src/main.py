from src.utils import read_xlsx
from src.views import get_started_main
from src.reports import expenses_by_category
from src.services import analyze_cashback_categories
import pandas as pd

if __name__ == "__main__":
    print(get_started_main())

    operations = read_xlsx("../data/operations.xlsx")
    df = pd.DataFrame(operations)
    user_input = input("Enter a year and month with space")
    user_input = list(map(int, user_input.split()))
    print(analyze_cashback_categories(operations, user_input[0], user_input[1]))

    user_input = input("Enter a category and date in form YYYY-MM-DD")
    user_input = user_input.split()
    print(expenses_by_category(df, user_input[0], user_input[1]))