# Copyright 2025 @VKrishna04
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
import os
from streamlit_app import run_streamlit_app
from cli_app import run_cli_app

if __name__ == "__main__":
    streamlit_server = os.getenv("STREAMLIT_SERVER")
    if streamlit_server and "streamlit" in streamlit_server:
        run_streamlit_app()
    else:
        run_cli_app()
