import glob
from nbconvert import MarkdownExporter
from nbconvert.utils.exceptions import ConversionException
import os
import nbformat
import yaml
import sys
import enlighten

# Specify the directory where your Jupyter Notebook files are located
notebook_directory = "_notebooks"

# Specify the destination directory for the converted Markdown files
destination_directory = "_posts"


def error_cleanup(notebook_file):
    # Remove the destination file if it exists
    destination_path = get_relative_output_path(notebook_file)
    if os.path.exists(destination_path):
        os.remove(destination_path)


def extract_front_matter(notebook_file, cell):
    front_matter = {}
    source = cell.get("source", "")
    if source.startswith("---"):
        try:
            # Extract front matter from source
            front_matter = yaml.safe_load(source.split("---", 2)[1])
        except yaml.YAMLError as e:
            print(f"Error parsing YAML front matter in {notebook_file}: {e}")
            error_cleanup(notebook_file)
            sys.exit(1)
    return front_matter


def get_relative_output_path(notebook_file):
    # Calculate the relative path of the notebook file
    relative_path = os.path.relpath(notebook_file, notebook_directory)
    # Replace the file extension and prepend the subdirectory structure
    markdown_filename = relative_path.replace(".ipynb", ".md")
    # Construct the full path for the output file
    destination_path = os.path.join(destination_directory, markdown_filename)
    return destination_path


def ensure_directory_exists(path):
    # Ensure the directory of the given path exists
    os.makedirs(os.path.dirname(path), exist_ok=True)


def convert_notebook_to_markdown_with_front_matter(notebook_file):
    try:
        # Load the notebook file
        with open(notebook_file, "r", encoding="utf-8") as file:
            notebook = nbformat.read(file, as_version=nbformat.NO_CONVERT)

        # Extract front matter from the first cell
        front_matter = extract_front_matter(notebook_file, notebook.cells[0])

        # Remove the first cell from the notebook
        notebook.cells.pop(0)

        # Convert the notebook to Markdown
        exporter = MarkdownExporter()
        markdown, _ = exporter.from_notebook_node(notebook)

        # Prepend the front matter to the Markdown content
        front_matter_content = "---\n" + \
            "\n".join(f"{key}: {value}" for key,
                      value in front_matter.items()) + "\n---\n\n"
        markdown_with_front_matter = front_matter_content + markdown

        # Generate the destination path including subdirectories
        destination_path = get_relative_output_path(notebook_file)

        # Ensure the output directory exists
        ensure_directory_exists(destination_path)

        # Write the converted Markdown file
        with open(destination_path, "w", encoding="utf-8") as file:
            file.write(markdown_with_front_matter)

        print(f"Converted {notebook_file} → {destination_path}")

    except ConversionException as e:
        print(f"Conversion error for {notebook_file}: {str(e)}")
        error_cleanup(notebook_file)
        sys.exit(1)


def convert_notebooks(progressBar):
    # Use recursive glob pattern to find .ipynb files in all subdirectories
    notebook_files = glob.glob(
        f"{notebook_directory}/**/*.ipynb", recursive=True)
    if not notebook_files:
        print("No notebooks found for conversion.")
        return

    with progressBar:
        for notebook_file in notebook_files:
            convert_notebook_to_markdown_with_front_matter(notebook_file)
            progressBar.update()


# Call the function to perform conversions when the script is run directly
if __name__ == "__main__":
    manager = enlighten.get_manager()

    pbar = manager.counter(total=sum([len(files) for r, d, files in os.walk(
        notebook_directory)]), desc='Converting notebooks:', unit='ticks')

    convert_notebooks(pbar)
