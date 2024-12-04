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
import re
import streamlit as st
import os
import datetime
import signal
from tabulate import tabulate
from dotenv import load_dotenv


# ANSI escape codes for colors (will not be used in Streamlit, just for debugging)
class colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    RESET = "\033[0m"


st.set_page_config(
    page_title="Sagittarius",  # Set page title
    page_icon="🔒",  # Favicon emoji
    layout="centered",
)

# Initialize the active page in session state
if "active_page" not in st.session_state:
    st.session_state.active_page = "Dashboard"
if "show_email_section" not in st.session_state:
    st.session_state.show_email_section = True
if "show_password_section" not in st.session_state:
    st.session_state.show_password_section = True
if "multi_check" not in st.session_state:
    st.session_state.multi_check = False

# Sidebar navigation
with st.sidebar:
    if st.button("Dashboard"):
        st.session_state.active_page = "Dashboard"
    if st.button("FAQs"):
        st.session_state.active_page = "FAQs"
    if st.button("Terms and Conditions"):
        st.session_state.active_page = "Terms and Conditions"
    st.markdown("---")
    if st.button("Stop Server"):
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
    st.markdown("---")


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

    st.success(f"Found email in {len(breaches)} breaches from {source_name}.")

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

        st.write(f"Breach: {breach_name}, Date: {date}")


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
                email = st.text_input("Enter your email address:", key="email_input")
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
                    password = st.text_input("Enter your password", "", type="password")

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


# Function to show FAQs and Contributions
def show_faq_and_contributions():
    st.title("Frequently Asked Questions")

    # FAQ Section
    faq_items = {
        "What exactly is a data breach?": "A data breach is an incident where sensitive, confidential, or protected information is accessed or disclosed without authorization.",
        "I just found out I’m in a data breach. What do I do next?": "Start by changing your passwords immediately, monitor your accounts for suspicious activity, and consider enabling multi-factor authentication.",
        "What information gets exposed in data breaches?": "Typically, breaches expose personal information like emails, passwords, financial data, or social security numbers.",
        "How can I protect myself from data breaches?": "Use strong, unique passwords for each account, enable multi-factor authentication, and regularly monitor your accounts for suspicious activity.",
        "What is multi-factor authentication?": "Multi-factor authentication (MFA) is a security process that requires more than one method of authentication to verify the user's identity.",
        "How do I know if my email has been breached?": "You can use tools like BreachCheck to check if your email has been involved in a known data breach.",
        "What should I do if my password has been pwned?": "Change your password immediately and consider using a password manager to generate and store strong, unique passwords.",
        "Is it safe to use BreachCheck?": "Yes, BreachCheck does not store any data and all interactions occur locally on your device.",
        "Can I check multiple passwords at once?": "Yes, you can enable the multi-check option in the password section to check multiple passwords at once.",
        "What is a password manager?": "A password manager is a tool that helps you generate, store, and manage your passwords securely.",
        "How often should I change my passwords?": "It's recommended to change your passwords regularly, especially if you suspect they have been compromised.",
        "What is phishing?": "Phishing is a type of cyber attack where attackers trick individuals into providing sensitive information by pretending to be a trustworthy entity.",
        "How can I recognize a phishing email?": "Look for signs like suspicious sender addresses, generic greetings, urgent language, and unexpected attachments or links.",
        "What is two-factor authentication?": "Two-factor authentication (2FA) is a type of multi-factor authentication that requires two methods of verification to access an account.",
        "Why should I use unique passwords for each account?": "Using unique passwords ensures that if one account is compromised, the others remain secure.",
    }

    for question, answer in faq_items.items():
        with st.expander(question):
            st.write(answer)

    # APIs Used Section
    st.title("APIs Used")
    st.markdown(
        """
        ### Email Breach Check APIs
        - **LeakCheck**: LeakCheck is an API that allows you to check if an email address has been involved in a data breach. It provides detailed information about the breaches.
        - **XposedOrNot**: XposedOrNot is another API that helps you determine if an email address has been compromised in a data breach.

        ### Password Breach Check API
        - **HaveIBeenPwned (HIBP)**: HaveIBeenPwned is a popular API that lets you check if a password has been exposed in a data breach. It uses a k-Anonymity model to ensure privacy while checking passwords.
        """
    )

    # Contributors Section
    st.title("Contributors")
    st.markdown(
        """
        ### Team Leader
        1. [@VKrishna04](https://github.com/VKrishna04)

        ### Frontend
        1. [@harsha4678](https://github.com/harsha4678) <- Figma Landing Page
        2. [@longhxirguy](https://github.com/longhxirguy) <- Streamlit Frontend

        ### APIs Integration
        1. [@Karthikkkk123](https://github.com/Karthikkkk123) <- Streamlit
        2. [Saisriram-88](https://github.com/Saisriram-88) <- CLI

        ### Support / Error Testing
        1. [@Jayanth-0703](https://github.com/Jayanth-0703) <- Support / Error Testing
        """
    )


# Function to show Terms and Conditions
def show_terms_and_conditions():
    st.title("Terms and Conditions")
    st.markdown(
        """
    ## No Data Storage
    We declare that no data is being stored by us as no database is connected to this application. All interactions and data processing occur locally on your device / on cloud when hosted.

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


if __name__ == "__main__":
    main()
