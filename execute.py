import sys
import streamlit as st
from streamlit.web import cli as stcli

sys.argv = ["streamlit", "run", "main.py"]
sys.exit(stcli.main())