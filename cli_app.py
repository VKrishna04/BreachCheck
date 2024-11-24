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
from email_apis import *
from password_apis import check_pwned_password, check_multiple_passwords
from tabulate import tabulate


def run_cli_app():
    print("Password & Email Breach Checker")
    print(
        "This tool helps you check if your email or password has been involved in a known data breach."
    )

    # Email input section
    email = input("Enter your email address: ")
    email_validation = re.match(r"[^@]+@[^@]+\.[^@]+", email)

    # Password input section
    multi_check = input("Multi-check Passwords (yes/no): ").lower() == "yes"
    if multi_check:
        passwords = input(
            "Enter your passwords (one per line, separated by commas): "
        ).split(",")
    else:
        password = input("Enter your password: ")

    # Check for breaches
    if email:
        if not email_validation:
            print("Please enter a valid email address.")
        else:
            # Email breach checks
            print("Checking email breaches...")
            leakcheck_result = req_leakcheck(email)
            if leakcheck_result:
                print_email_breaches(leakcheck_result, "LeakCheck")

            xposed_result = req_xposedornot(email)
            if xposed_result:
                print_email_breaches(xposed_result, "XposedOrNot")

    if multi_check:
        if passwords:
            print("Checking password breaches...")
            results = check_multiple_passwords("\n".join(passwords))
            print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        if password:
            # Password breach checks
            print("Checking password breaches...")
            check_pwned_password(password)


def print_email_breaches(answer, source_name):
    breaches = (
        answer.get("sources", [])
        if source_name == "LeakCheck"
        else answer.get("breaches", [])
    )
    if not breaches:
        print(f"No breaches found for the email in {source_name}.")
        return

    print(f"Found email in {len(breaches)} breaches from {source_name}.")

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
            print(f"Unexpected breach data format: {breach}")
            continue

        breach_data.append({"Website": breach_name, "Date": date})

    print(tabulate(breach_data, headers="keys", tablefmt="grid"))
