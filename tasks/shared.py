def run(context, path, command):
    print(f"cd {path} && {command}")
    with context.cd(path):
        context.run(command)