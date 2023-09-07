import subprocess
import re

# Execute 'localstack --help' and capture the output
help_output = subprocess.check_output(["localstack", "--help"], text=True)

# Extract the purpose and available commands from the help output
purpose_match = re.search(r"Usage:.*\n\s+(.*)\n\nOptions:", help_output, re.DOTALL)
purpose = purpose_match.group(1) if purpose_match else ""
commands_match = re.search(r"Commands:\n((?:\s{2}[^\n]*\n)+)", help_output)
commands = [cmd.strip() for cmd in commands_match.group(1).split("\n") if cmd.strip()]

# Create a dictionary to store command purposes
command_purposes = {}

# Loop through each command and subcommand
for cmd in commands:
    cmd_parts = cmd.split(None, 1)
    if len(cmd_parts) == 2:
        command_purposes[cmd_parts[0]] = cmd_parts[1].strip()

# Output file name
output_file = "content/en/references/localstack-cli-manual.md"

# Open the output file for writing
with open(output_file, "w") as f:
    # Write a header for the markdown file
    f.write("---\n")
    f.write("title: LocalStack CLI manual\n")
    f.write("weight: 3\n")
    f.write(
        "description: The reference guide for LocalStack CLI commands and how to get started on using them!\n"
    )
    f.write("---\n\n")
    f.write(
        "The LocalStack command-line interface (CLI) is a tool for starting, managing, and configuring your LocalStack container.\n"
    )
    f.write(
        "It provides convenience features that make it easier to use LocalStack, and use LocalStack tools like Cloud Pods, Extensions, and more.\n\n"
    )
    f.write("## Options\n\n")
    f.write("The following options are available for the `localstack` CLI.\n\n")

    # Loop through each command and its purpose
    for cmd, cmd_purpose in command_purposes.items():
        # Execute 'localstack [cmd] --help' and capture the output
        cmd_output = subprocess.check_output(["localstack", cmd, "--help"], text=True)

        # Write the command, its purpose, and its help output to the markdown file
        f.write(f"### `{cmd}`\n\n")
        f.write(f"{cmd_purpose}.\n\n")
        f.write("```bash\n")
        f.write(cmd_output)
        f.write("```\n\n")
