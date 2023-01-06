import difflib
import subprocess


def find_processes(process_name):
    """Returns all PIDs of program processes specified by name."""
    processes = subprocess.Popen(["ps", "-A"], stdout=subprocess.PIPE)
    output, error = processes.communicate()
    pids = []
    for line in output.splitlines():
        if process_name in str(line):
            pids.append(int(line.split(None, 1)[0]))
    return pids


class Colors:
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    BLUE = "\033[94m"
    PINK = "\033[95m"
    END = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


def show_diff(before, after):
    """Show the colored difference between two strings."""
    before = before if before else ""
    after = after if after else ""
    seqm = difflib.SequenceMatcher(None, before, after)
    output = []
    for opcode, b0, b1, a0, a1 in seqm.get_opcodes():
        if opcode == "equal":
            output.append(Colors.BOLD + before[b0:b1] + Colors.END)
        elif opcode == "insert":
            output.append(Colors.GREEN + after[a0:a1] + Colors.END)
        elif opcode == "delete":
            output.append(Colors.GREY + before[b0:b1] + Colors.END)
        elif opcode == "replace":
            output.append(
                Colors.GREY
                + before[b0:b1]
                + Colors.END
                + Colors.GREEN
                + after[a0:a1]
                + Colors.END
            )
        else:
            raise RuntimeError("unexpected opcode")
    return "".join(output)


def normalize_string(string):
    """Use regular whitespaces."""
    return string.replace("\xa0", " ")
