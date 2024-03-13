import streamlit as st


def stateful_multiselect(key, label, options, initial_value=[]):
    get_from_session(key=key, initial_value=initial_value)
    return st.multiselect(
        key=key,
        label=label,
        options=options,
        on_change=save_to_session,
        args=(key,),
    )


def stateful_number_input(key, label, format, step, help, label_visibility="visible", min_value=None, max_value=None, initial_value=0):
    get_from_session(key=key, initial_value=initial_value)
    return st.number_input(
        key=key,
        label=label,
        label_visibility=label_visibility,
        format=format,
        step=step,
        help=help,
        on_change=save_to_session,
        args=(key,),
        min_value=min_value,
        max_value=max_value
    )


def stateful_text_input(key, label, label_visibility="visible", initial_value=""):
    get_from_session(key=key, initial_value=initial_value)
    return st.text_input(
        key=key,
        label=label,
        label_visibility=label_visibility,
        on_change=save_to_session,
        args=(key,),
    )


def save_to_session(key):
    st.session_state[create_temporary_name_for_caching(key)] = st.session_state[key]


def get_from_session(key, initial_value):
    if key not in st.session_state:
        st.session_state[key] = initial_value
    if create_temporary_name_for_caching(key) not in st.session_state:
        st.session_state[create_temporary_name_for_caching(key)] = st.session_state[key]
    st.session_state[key] = st.session_state[create_temporary_name_for_caching(key)]
    # del st.session_state[create_temporary_name_for_caching(key)] # Must keep for state to persist between pages


def create_temporary_name_for_caching(key):
    return f"{key}_cache_helper"
