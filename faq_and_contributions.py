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
        1. [@harsha4678](https://github.com/harsha4678) - Figma Landing Page
        2. [@longhxirguy](https://github.com/longhxirguy) - Streamlit Frontend

        ### APIs Integration
        1. [@Karthikkkk123](https://github.com/Karthikkkk123)
        2. [APIs Integration Contributor 2](https://github.com/APIsIntegrationContributor2)

        ### Support / Error Testing
        1. [@Jayanth-0703](https://github.com/Jayanth-0703)
        """
    )
