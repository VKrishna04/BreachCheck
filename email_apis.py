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

import requests
import streamlit as st


# Email Breach Check - LeakCheck
def req_leakcheck(email):
    url = f"https://leakcheck.io/api/public?check={email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"sources": []}
        else:
            st.error(
                f"LeakCheck API call failed with status code {response.status_code}"
            )
            return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False


# Email Breach Check - XposedOrNot
def req_xposedornot(email):
    url = f"https://api.xposedornot.com/v1/check-email/{email}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            return {"breaches": []}
        else:
            st.error(
                f"XposedOrNot API call failed with status code {response.status_code}"
            )
            return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False
