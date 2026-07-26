import sys

def run_itl_file(path):
    with open(path, 'r') as f:
        lines = f.readlines()

    # Check for ITL Numbered v1.0.0 start
    if not lines[0].strip() == 'itl-lang("start");':
        print("Error: ITL file must start with itl-lang(\"start\");")
        return

    for line in lines[1:]:
        line = line.strip()
        if line == 'itl-lang("end");' or not line or line.startswith("#"):
            continue
        if line.startswith("print"):
            # print "text";
            content = line.split("print")[1].strip().strip('";')
            print(content.strip('"').strip("'"))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py file.itl")
    else:
        run_itl_file(sys.argv[1])
