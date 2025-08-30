# caas_jupyter_tools.py (shim locale)
from IPython.display import display

def display_dataframe_to_user(name: str, dataframe):
    print(f"## {name}")
    try:
        display(dataframe)
    except Exception:
        try:
            print(dataframe.to_string())
        except Exception:
            print(repr(dataframe))
