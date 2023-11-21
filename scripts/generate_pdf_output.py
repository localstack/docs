import os
import re
import shutil
import subprocess
import time

import PyPDF2
from pdf_list import doc_list


def run_website2pdf():
    """
    Executes the 'website2pdf' command to convert websites to PDF.
    This command uses a sitemap URL to identify the web pages to convert.
    Prints the result of the command execution or any errors encountered.
    """
    command = [
        "website2pdf",
        "--sitemap-url",
        "https://docs.localstack.cloud/sitemap.xml",
    ]
    try:
        result = subprocess.run(
            command,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        print("Command executed successfully. Output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("An error occurred while executing the command.")
        print(e.stderr)


def find_and_copy_pdfs(source_dir, target_dir):
    """
    Finds and copies PDF files from source_dir to target_dir.
    Renames the files by removing certain patterns and changing to lowercase.

    Parameters:
    source_dir (str): The directory to search for PDF files.
    target_dir (str): The directory where PDF files will be copied to.
    """
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    for root, dirs, files in os.walk(source_dir):
        # Skip the target directory to prevent copying files onto themselves
        if root == target_dir:
            continue

        for file in files:
            if file.endswith(".pdf"):
                # Construct the full file path
                file_path = os.path.join(root, file)

                # Remove "| Docs" and parenthetical expressions, then process for other replacements
                new_file_name = re.sub(r" \(.*?\)", "", file.replace(" | Docs", ""))
                new_file_name = (
                    new_file_name.lower().replace(" ", "-").replace("&", "and")
                )

                # Copy the file to the target directory with the new name
                shutil.copy(file_path, os.path.join(target_dir, new_file_name))


def merge_pdfs(file_list, output_filename):
    """
    Merges multiple PDF files into a single PDF.

    Parameters:
    file_list (list): A list of filenames of the PDFs to merge.
    output_filename (str): The filename for the merged PDF output.
    """
    merger = PyPDF2.PdfMerger()

    for pdf_file in file_list:
        with open(f"final/{pdf_file}.pdf", "rb") as f:
            merger.append(f)

    with open(output_filename, "wb") as out_file:
        merger.write(out_file)


def read_file_list(filename):
    """
    Reads a list of filenames from a given text file.

    Parameters:
    filename (str): The filename of the text file to read.

    Returns:
    list: A list of filenames read from the file.
    """
    with open(filename, "r") as file:
        return [line.strip() for line in file]


def delete_folders(folder_list):
    """
    Deletes a list of folders.

    Parameters:
    folder_list (list): A list of folder names to delete.
    """
    for folder in folder_list:
        folder_path = os.path.join("w2pdf_output", folder)
        try:
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            else:
                print(f"Folder not found: {folder_path}")
        except OSError as e:
            print(f"Error deleting folder {folder_path}: {e}")


if __name__ == "__main__":
    run_website2pdf()
    time.sleep(60)
    folders_to_delete = [
        "academy",
        "contributing",
        "developer-hub",
        "tags",
        "categories",
        "applications",
        "references/coverage",
    ]
    delete_folders(folders_to_delete)
    source_directory = "w2pdf_output"
    target_directory = "final"
    find_and_copy_pdfs(source_directory, target_directory)
    merge_pdfs(doc_list, "localstack_docs.pdf")
    print("The PDF files have been merged into a single PDF file: localstack_docs.pdf")
