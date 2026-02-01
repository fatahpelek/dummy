import subprocess
import os
import sys

print("=== Python Interactive Shell (Pterodactyl) ===")
print("Ketik command seperti terminal biasa")
print("Ketik 'exit' atau 'quit' untuk keluar\n")

cwd = os.getcwd()

while True:
    try:
        cmd = input(f"{os.getenv('USER', 'container')}@panel:{cwd}$ ").strip()

        if cmd.lower() in ["exit", "quit"]:
            print("Bye 👋")
            break

        if cmd == "":
            continue

        # handle cd
        if cmd.startswith("cd "):
            path = cmd[3:].strip()
            try:
                os.chdir(path)
                cwd = os.getcwd()
            except Exception as e:
                print(f"cd: {e}")
            continue

        # execute command
        process = subprocess.Popen(
            cmd,
            shell=True,
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        out, err = process.communicate()

        if out:
            print(out, end="")
        if err:
            print(err, end="")

    except KeyboardInterrupt:
        print("\nCTRL+C (gunakan 'exit' untuk keluar)")
    except EOFError:
        break
