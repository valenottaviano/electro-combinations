import streamlit as st
import pandas as pd
import itertools


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
            
            min_val, max_val = col1.slider(f"{var}_{tab_titles[i]}", min_value=0, max_value=100, value=(0, 100))
            steps = col2.number_input(f"Steps {var}_{tab_titles[i]}", min_value=1, max_value=100, value=max_val)
            var_values[var] = list(range(min_val, max_val + 1, steps))

        # for combo in itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']]):
            # tab.write(combo)
        combinations =pd.DataFrame(
            data=list(itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']])),
            columns=variables[f'{tab_titles[i]}']
            )
        tab.dataframe(combinations)
        # st.dataframe(pd.DataFrame(list(itertools.product(*[var_values[var] for var in variables[f'{tab_titles[i]}']]))))