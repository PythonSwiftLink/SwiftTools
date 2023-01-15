
#psl = "psl"
psl = "/Users/musicmaker/Library/Developer/Xcode/DerivedData/PythonSwiftLinkCLI-gurgkowxflqpxngtvigbxihgtoon/Build/Products/Debug/PythonSwiftLinkCLI"



swift_tools_standard_packages = [
    "phpicker",
    "camera",
    "notification",
    "webviews",
]

swift_tools_plyer_packages = [
    "filechooser",
    "brightness",
    "tts"
]



if __name__ == '__main__':
    from sys import argv

    from subprocess import run

    if len(argv) < 3:
        exit(0)

    project_name = argv[1]
    python_folder = argv[2]
    
    run([f"""
    . venv/bin/activate
    toolchain create {project_name} {python_folder}
    """], shell=True)

    run([f"{psl} -p {project_name}-ios project setup"], shell=True)
    # exit(0)
    # for pack in swift_tools_standard_packages:
    #     run([f"{psl} -p {project_name}-ios swift-tools install --standard {pack}"], shell=True)

    # for pack in swift_tools_plyer_packages:
    #     run([f"{psl} -p {project_name}-ios swift-tools install --plyer {pack}"], shell=True)

    run([f"""
    . venv/bin/activate
    toolchain xcode {project_name}-ios
    """], shell=True)
    # for pack in swift_tools_plyer_packages:
    #     run(["echo", f"-p {project_name}-ios swift-tools install --plyer", pack], shell=True)

