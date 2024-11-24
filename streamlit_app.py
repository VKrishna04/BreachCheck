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

import re
import requests
import datetime
import os
import signal
import streamlit as st
from email_apis import *
from password_apis import check_pwned_password, check_multiple_passwords
from terms_and_conditions import show_terms_and_conditions
from faq_and_contributions import show_faq_and_contributions
from dotenv import load_dotenv

load_dotenv()


def run_streamlit_app():
    st.set_page_config(
        page_title="Sagittarius",  # Set page title
        page_icon="🔒",  # Favicon emoji
        layout="centered",
    )

    # Check if running on Streamlit Cloud
    if os.getenv("STREAMLIT_SERVER_HEADLESS") == "true":
        st.set_option("server.showForkButton", False)

    # Function to stop the Streamlit server
    def stop_server():
        st.warning("Stopping the server...")
        st.markdown(
            """
            <script>
            window.close();
            </script>
            """,
            unsafe_allow_html=True,
        )
        os.kill(os.getpid(), signal.SIGTERM)

    # Function to get a random background image from Unsplash with dynamic resolution
    # def get_unsplash_background(
    #     width, height, access_key, secret_key, query=None, orientation=None
    # ):
    #     url = f"https://api.unsplash.com/photos/random?client_id={access_key}&client_secret={secret_key}&w={width}&h={height}"
    #     if query:
    #         url += f"&query={query}"
    #     if orientation:
    #         url += f"&orientation={orientation}"
    #     response = requests.get(url)
    #     if response.status_code == 200:
    #         photo_data = response.json()
    #         download_url = photo_data["links"]["download_location"]
    #         download_trigger = requests.get(
    #             download_url, headers={"Authorization": f"Client-ID {access_key}"}
    #         )
    #         if download_trigger.status_code == 200:
    #             return (
    #                 photo_data["urls"]["full"],
    #                 photo_data["user"]["name"],
    #                 photo_data["user"]["links"]["html"],
    #             )
    #         else:
    #             return None, None, None
    #     else:
    #         return None, None, None

    # Custom CSS for background
    # Get the browser window size using JavaScript
    st.markdown(
        """
        <script>
        function getWindowSize() {
            var width = window.innerWidth;
            var height = window.innerHeight;
            document.body.setAttribute('data-width', width);
            document.body.setAttribute('data-height', height);
        }
        window.onload = getWindowSize;
        window.onresize = getWindowSize;
        </script>
        """,
        unsafe_allow_html=True,
    )
    # page_bg_img = """
    #         <style>
    #         body {
    #         background-image: url("https://api.unsplash.com/photos/random?client_id={access_key}&client_secret={secret_key}&w={width}&h={height}");
    #         background-size: cover;
    #         }
    #         </style>
    #         """
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    # Sidebar navigation
    with st.sidebar:
        if st.button("Dashboard"):
            st.session_state.active_page = "Dashboard"
        if st.button("FAQs"):
            st.session_state.active_page = "FAQs"
        if st.button("Terms and Conditions"):
            st.session_state.active_page = "Terms and Conditions"
        st.markdown("---")
        # Conditionally render the stop button to stop the server
        if os.getenv("STREAMLIT_SERVER_HEADLESS") != "true":
            if st.button("Stop Server"):
                stop_server()
        st.markdown("---")

        # Unsplash API key input and filters
        # if "unsplash_access_key" not in st.session_state:
        #     st.session_state.unsplash_access_key = os.getenv("UNSPLASH_ACCESS_KEY")
        # if "unsplash_secret_key" not in st.session_state:
        #     st.session_state.unsplash_secret_key = os.getenv("UNSPLASH_SECRET_KEY")
        # if "show_api_key_input" not in st.session_state:
        #     st.session_state.show_api_key_input = not bool(
        #         st.session_state.unsplash_access_key
        #         and st.session_state.unsplash_secret_key
        #     )

        # if st.session_state.show_api_key_input:
        #     unsplash_access_key = st.text_input(
        #         "Enter Unsplash Access Key:", type="password"
        #     )
        #     unsplash_secret_key = st.text_input(
        #         "Enter Unsplash Secret Key:", type="password"
        #     )
        #     if unsplash_access_key and unsplash_secret_key:
        #         st.session_state.unsplash_access_key = unsplash_access_key
        #         st.session_state.unsplash_secret_key = unsplash_secret_key
        #         os.environ["UNSPLASH_ACCESS_KEY"] = unsplash_access_key
        #         os.environ["UNSPLASH_SECRET_KEY"] = unsplash_secret_key
        #         with open(".env", "a") as f:
        #             f.write(f"\nUNSPLASH_ACCESS_KEY={unsplash_access_key}")
        #             f.write(f"\nUNSPLASH_SECRET_KEY={unsplash_secret_key}")
        #     if st.button("Close"):
        #         st.session_state.show_api_key_input = False
        #         st.session_state.unsplash_error_shown = False
        #         st.experimental_rerun()
        #     st.markdown("---")

        # query = st.text_input("Search Term (Optional):")
        # orientation = st.selectbox(
        #     "Orientation (Optional):", [None, "landscape", "portrait", "squarish"]
        # )

    # background_url, photographer_name, photographer_link = get_unsplash_background(
    #     width,
    #     height,
    #     st.session_state.unsplash_access_key,
    #     st.session_state.unsplash_secret_key,
    #     query,
    #     orientation,
    # )
    # if background_url:
    #     st.write(f"Background URL: {background_url}")  # Debug statement
    #     st.markdown(
    #         f"""
    #         <style>
    #         body {{
    #             background-image: url('{background_url}');
    #             background-size: cover;
    #             background-repeat: no-repeat;
    #             background-attachment: fixed;
    #             background-color: black; /* Fallback color */
    #         }}
    #         .stApp {{
    #             padding: 20px;
    #             border-radius: 10px;
    #             /* background: rgba(255, 255, 255, 0.8);  White background with opacity */
    #         }}
    #         </style>
    #         """,
    #         unsafe_allow_html=True,
    #     )
    #     with st.sidebar:
    #         st.sidebar.markdown(
    #             f"Photo by [**{photographer_name}**]({photographer_link}) on [**Unsplash**](https://unsplash.com)"
    #         )
    # else:
    #     with st.sidebar:
    #         if "unsplash_error_shown" not in st.session_state:
    #             st.session_state.unsplash_error_shown = False

    #         if not st.session_state.unsplash_error_shown:
    #             st.error("Failed to load background image from Unsplash.")
    #             st.session_state.unsplash_error_shown = True
    #         else:
    #             st.error(
    #                 "Failed to load background image from Unsplash. Please enter a valid Unsplash API key."
    #             )
    #         st.markdown("---")

    # Initialize the active page and section visibility in session state
    if "active_page" not in st.session_state:
        st.session_state.active_page = "Dashboard"
    if "show_email_section" not in st.session_state:
        st.session_state.show_email_section = True
    if "show_password_section" not in st.session_state:
        st.session_state.show_password_section = True
    if "multi_check" not in st.session_state:
        st.session_state.multi_check = False

    # Function to print email breach results
    def print_email_breaches(answer, source_name):
        breaches = (
            answer.get("sources", [])
            if source_name == "LeakCheck"
            else answer.get("breaches", [])
        )
        if not breaches:
            st.warning(f"No breaches found for the email in {source_name}.")
            return

        st.warning(f"Found email in {len(breaches)} breaches from {source_name}.")

        breach_data = []
        for breach in breaches:
            # Handle cases where breach is a list (e.g., ['BigBasket'])
            if isinstance(breach, list):
                breach_name = breach[0] if len(breach) > 0 else "Unknown"
                date = "Unknown"
            elif isinstance(breach, dict):
                breach_name = breach.get("name", "Unknown")
                date = breach.get("date", "Unknown")
            elif isinstance(breach, str):
                breach_name = breach
                date = "Unknown"
            else:
                st.warning(f"Unexpected breach data format: {breach}")
                continue

            breach_data.append({"Website": breach_name, "Date": date})

        st.table(breach_data)

    # Main function to display Streamlit interface
    def main():
        # App title and description
        st.title("Password & Email Breach Checker")
        st.write(
            "This tool helps you check if your email or password has been involved in a known data breach."
        )

        # Main content rendering based on the active page
        if st.session_state.active_page == "Dashboard":
            st.title("Dashboard")

            # Email input section
            email = ""
            email_validation = None
            if st.session_state.show_email_section:
                with st.expander("Email Section", expanded=True):
                    email = st.text_input(
                        "Enter your email address:", key="email_input"
                    )
                    email_validation = re.match(r"[^@]+@[^@]+\.[^@]+", email)

            # Password input section
            if st.session_state.show_password_section:
                with st.expander("Password Section", expanded=True):
                    st.session_state.multi_check = st.checkbox(
                        "Multi-check Passwords", value=False
                    )
                    if st.session_state.multi_check:
                        passwords = st.text_area(
                            "Enter your passwords (one per line):", key="password_input"
                        )
                    else:
                        password = st.text_input(
                            "Enter your password", "", type="password"
                        )

            # Check button to trigger breach checks
            if st.button("Check for Breaches"):
                if st.session_state.show_email_section and email:
                    if not email_validation:
                        st.error("Please enter a valid email address.")

                    if email_validation:
                        # Email breach checks
                        st.subheader("Checking email breaches...")
                        leakcheck_result = req_leakcheck(email)
                        if leakcheck_result:
                            print_email_breaches(leakcheck_result, "LeakCheck")

                        xposed_result = req_xposedornot(email)
                        if xposed_result:
                            print_email_breaches(xposed_result, "XposedOrNot")

                if st.session_state.show_password_section:
                    if st.session_state.multi_check:
                        if passwords:
                            st.subheader("Checking password breaches...")
                            results = check_multiple_passwords(passwords)
                            st.table(results)
                    else:
                        if password:
                            # Password breach checks
                            st.subheader("Checking password breaches...")
                            check_pwned_password(password)

        elif st.session_state.active_page == "FAQs":
            show_faq_and_contributions()

        elif st.session_state.active_page == "Terms and Conditions":
            show_terms_and_conditions()

        # Footer rendering
        current_year = datetime.datetime.now().year
        st.markdown(
            f"""
            <style>
            .footer {{
                text-align: center;
                padding: 10px;
                background: var(--background-secondary);
                border-top: 1px solid var(--background-tertiary);
                margin-top: 20px;
                color: var(--text-color);
            }}
            </style>
            <footer class="footer">
                <p>
                    &copy;{current_year} |
                    <a href="https://github.com/VKrishna04/BreachCheck" target="_blank">GitHub</a> |
                    <a href="http://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache License 2.0</a>
                </p>
            </footer>
            """,
            unsafe_allow_html=True,
        )

    main()

    if __name__ == "__main__":
        main()
