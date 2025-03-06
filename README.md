# DC31IPR_Digital_Transformation_Tool
An all-encompassing tool designed to aid organisations in evaluating their digital maturity.

The tool is designed as an assessment and is currently in its Minimum Viable Product (MVP) stage, with some functionality still under development.

To use this tool users must create an account. Once the assessment is completed, a detailed report will be generated. The assessment consists of a series of sections designed to evaluate your company’s digital maturity. Based on your score, an algorithm generates an in-depth analysis of various areas within your business, highlighting opportunities for improvement. 

The report provides actionable solutions aimed at achieving optimal outcomes such as cost efficiency, time savings, and fostering innovation. These insights empower you to make informed decisions that will benefit your company.

# How to run

# Installation Information

This guide will help you get started.

## Prerequisites

Before you start make sure you have Python installed on your system. If not you can download it from the official Python website.

The project is also available on gitHub:
https://github.com/vfryer12/DC31IPR_Digital_Transformation_Tool

## Poetry Installation

The software is packaged and distributed using Poetry. To install the software, follow these steps:

Poetry is the dependency manager. Install it by following the instructions at Poetry's official documentation.
https://python-poetry.org/docs/?form=MG0AV3

1. Open your terminal or command prompt.

2. Navigate to the directory where you downloaded our software.

3. Run the following command to install the software and its dependencies:

    poetry install

(The poetry install command ensures Flask is available in the virtual environment)

4. After installation, confirm it’s working by running
poetry --version

## Running the Software

To run the software, use the following command in your terminal or command prompt:

    poetry run python.app

## Launching the Application Using Poetry as the Dependency Manager
This is used for demo and testing

# Activates the Poetry virtual environment (Only available in below Poetry 2.0.0)
1/ Run this command:
        poetry shell

# Runs the Python application
2/ Run this command:
        python app.py