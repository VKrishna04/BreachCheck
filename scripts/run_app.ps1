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

Set-Location -Path (Join-Path -Path $PSScriptRoot -ChildPath "..")

Write-Output "Checking for required dependencies..."
pip install -r requirements.txt | Select-String -Pattern "Requirement already satisfied" -NotMatch

Write-Output "Starting Streamlit app..."
streamlit run app.py

Write-Output ""