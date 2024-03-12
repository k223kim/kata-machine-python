import os
import json

def get_day(root_dir):
    day_dir = os.path.join('/'.join(root_dir.split('/')[:-1]), 'src')
    list_dir = os.listdir(day_dir)
    list_dir = [int(each_file.replace('day', '')) for each_file in list_dir if each_file.startswith('day')]
    list_dir.sort()
    max_day = 1
    if len(list_dir) > 0:
        max_day = int(list_dir[-1]) + 1
    new_day_dir = os.path.join(day_dir, f'day{max_day}')
    os.mkdir(new_day_dir)
    return new_day_dir

def update_pytest(new_day_dir, pytest_dir):
    new_day = new_day_dir.split('/')[-1]
    new_pytest_ini = f"[pytest]\ntestpaths = src/__tests__/\npythonpath = src/{new_day}\n"
    with open(pytest_dir, 'w+') as f:
        f.write(new_pytest_ini)

def generate_function_code(func_name, func_info, day_dir):
    save_path = os.path.join(day_dir, f'{func_name}.py')
    function_text = f"def {func_info['fn']}({func_info['args']}):\n    pass"
    if 'import' in func_info:
        if len(func_info['import']) > 0:
            import_txt = ""
            for each_import in func_info['import']:
                import_txt += each_import + "\n"
            function_text =  import_txt + function_text
    with open(save_path, 'w+') as f:
        f.write(function_text)

def generate_class_code(class_name, class_info, day_dir):
    save_path = os.path.join(day_dir, f'{class_name}.py')
    class_code = f"class {class_name}:\n"
    class_code += "    def __init__(self):\n"
    properties = class_info.get("properties", [])
    if len(properties) == 0:
        class_code += "        pass\n"
    for property in properties:
        class_code += f"        self.{property['name']} = None\n"
    methods = class_info.get("methods", [])
    for method in methods:
        if len(method['args']) == 0:
            class_code += f"    def {method['name']}(self):\n        pass\n"
        else:
            class_code += f"    def {method['name']}(self, {method['args']}):\n        pass\n"
    with open(save_path, 'w+') as f:
        f.write(class_code)

def main(config, day_dir):
    for key, val in config.items():
        if val["type"] == "fn":
            generate_function_code(key, val, day_dir)
        elif val["type"] == "class":
            generate_class_code(key, val, day_dir)

if __name__ == "__main__":
    root_dir = os.path.dirname(os.path.abspath(__file__))
    pytest_path = root_dir.replace('kata-machine-python/scripts', 'kata-machine-python/pytest.ini')
    day_dir = get_day(root_dir)
    update_pytest(day_dir, pytest_path)
    json_dir = os.path.join(root_dir, 'config.json')
    config = json.load(open(json_dir))
    main(config, day_dir)


