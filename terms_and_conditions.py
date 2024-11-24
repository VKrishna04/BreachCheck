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


def show_terms_and_conditions():
    st.title("Terms and Conditions")
    st.markdown(
        """
    ## No Data Storage
    We declare that no data is being stored by us as no database is connected to this application. All interactions and data processing occur locally on your device.

    ## Disclaimer of Liability
    We are not responsible for any issues, damages, or losses caused by the usage of this application. The application is provided "as is" without any warranties or guarantees of any kind.

    ## Usage
    By using this application, you acknowledge and agree that you are solely responsible for any consequences that may arise from its usage. We do not take any responsibility for any actions taken based on the information provided by this application.

    ## Changes to Terms and Conditions
    We reserve the right to update or change these terms and conditions at any time without prior notice. It is your responsibility to review these terms and conditions periodically for any changes.

    ## Contact Us
    If you have any questions or concerns about these terms and conditions, please contact us at the <a href="https://github.com/VKrishna04/BreachCheck" target="_blank">GitHub page</a>.
    """,
        unsafe_allow_html=True,
    )
