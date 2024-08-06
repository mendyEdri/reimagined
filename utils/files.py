from langchain_core.tools import tool
import os

def read_file(file_name):
    with open(file_name, 'r') as file:
        return file.read()

def write_file(input="", file_name=""):
    with open(file_name, 'w') as file:
        file.write(input)

def write_docs(input="", file_name=""):
    content = read_file(file_name)
    print("enter write file", content)
    with open(file_name, 'w') as file:
        file.writelines([f"// Description: {input}", f"\n{content}\n"])

def read_files_in_directory(input=""):
    all_content = ""
    for root, dirs, files in os.walk(input):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            with open(file_path, 'r') as file:
                content = file.read()
                print(f"Reading from: {file_path}")
                all_content += content
    return all_content


@tool
def read_file_tool(file_name):
    """Useful to when need to read single file content"""
    print("** tool-use: read_file")
    return read_file(file_name)

@tool
def write_file_tool(input="", file_name=""):
    """Useful to when need to write content into a file, get's two params, 1. input: the content you want to insert to the file. 2. file_name: the file name you want to edit."""
    print("** tool-use: write_file")
    return write_file(input, file_name)

@tool
def write_docs_tool(input="", file_name=""):
    """Useful to when need to write content into a file, get's two params, 1. input: the content you want to insert to the file. 2. file_name: the file name you want to edit."""
    print("** tool-use: write_docs")
    return write_docs(input, file_name)

@tool
def read_files_in_directory_tool(input=""):
    """Useful to when need to read folder files content"""
    print("** tool-use: read_files_in_directory")
    return read_files_in_directory(input)