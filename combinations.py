import streamlit as st
import pandas as pd
import itertools

params = {
    't': {
        'min': 1,
        'max': 60,
        'step': 10,
    },
    'f': {
        'min': 1,
        'max': 200,
        'step': 30,
    },
    'V': {
        'min': 1,
        'max': 64,
        'step': 4,
    },
    'B': {
        'min': 1,
        'max': 200,
        'step': 10,
    },
    'I': {
        'min': 10,
        'max': 2000,
        'step': 10,
    },
    'P': {
        'min': 50,
        'max': 500,
        'step': 50,
    },
    'modo': {
        'min': 0,
        'max': 1,
        'step': 1,
    },
    'DC': {
        'min': 1,
        'max': 100,
        'step': 10,
    },
}

variables = {
    'AMF_ee_box': ['t', 'f', 'V'],
    'AMF_neodimio': ['t', 'B', 'f'],
    'SMF_fuente': ['t', 'I'],
    'SMF_neodimio': ['t', 'B'],
    'CMF_mfg': ['t', 'P', 'f', 'modo'],
    'CMF_ee_box': ['t', 'f', 'V', 'DC']
}



if __name__ == '__main__':

    # st.title('Combinations')

    tab_titles = list(variables.keys())
    tabs = st.tabs(tab_titles)

    for i, tab in enumerate(tabs):
        tab.header(f'{tab_titles[i]}')
        # tab.write(variables[f'{tab_titles[i]}'])

        var_values = {}
        for var in variables[f'{tab_titles[i]}']:
            col1, col2 = tab.columns(2)
            
            # min_val, max_val = col1.slider(f"{var}_{tab_titles[i]}", min_value=1, max_value=100, value=(1,100))
            min_val, max_val = col1.slider(f"{var}_{tab_titles[i]}", min_value=params[var]['min'], max_value=params[var]['max'], value=(params[var]['min'], params[var]['max']))
            steps = col2.number_input(f"Steps {var}_{tab_titles[i]}", value=params[var]['step'])
            var_values[var] = list(range(min_val, max_val + 1, steps))

            # if isinstance(var, str):
                # tab.write(f"{var}_{tab_titles[i]} is a string")

        # for combo in itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']]):
            # tab.write(combo)
        combinations =pd.DataFrame(
            data=list(itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']])),
            columns=variables[f'{tab_titles[i]}']
            )
        tab.dataframe(combinations)
        # st.dataframe(pd.DataFrame(list(itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']]))))