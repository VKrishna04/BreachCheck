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
import hashlib
import streamlit as st


# Password Breach Check - HaveIBeenPwned (HIBP)
def check_pwned_password(password):
    sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    prefix = sha1_hash[:5]
    suffix = sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            hashes = (line.split(":") for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    st.error(f"Password has been pwned {count} times!")
                    return True
            st.success("Password is safe!")
            return False
        else:
            st.error("Error fetching data from HIBP.")
            return False
    except Exception as e:
        st.error(f"Error: {e}")
        return False


# Function to check multiple passwords
def check_multiple_passwords(passwords):
    results = []
    for idx, password in enumerate(passwords.splitlines(), start=1):
        sha1_hash = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
        prefix = sha1_hash[:5]
        suffix = sha1_hash[5:]
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                hashes = (line.split(":") for line in response.text.splitlines())
                pwned_count = 0
                for h, count in hashes:
                    if h == suffix:
                        pwned_count = int(count)
                        break
                results.append({"Password": password, "Pwned Count": pwned_count})
            else:
                results.append({"Password": password, "Pwned Count": "Error"})
        except Exception as e:
            results.append({"Password": password, "Pwned Count": f"Error: {e}"})
    return results
