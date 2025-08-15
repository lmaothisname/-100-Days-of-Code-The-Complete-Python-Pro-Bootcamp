def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())

format_name("kiet","TRAN")

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    print(f"{formated_f_name} {formated_l_name}")

format_name("Tran","KIET")

def format_name(f_name,l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("Phuc","ANH")
print(formated_string)

def function_1(text):
    return text + text
def function_2(text):
    return text.title()
output = function_2(function_1("Cs2"))
print(output)