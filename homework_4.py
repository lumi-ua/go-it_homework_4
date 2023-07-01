def input_error(func):
    def wrapper(*args, **kwargs):
        argc = len(args)
        result = None
        try:
            result = func(*args, **kwargs)
        except KeyError:
            print("Enter user name")
        except ValueError:
            print("Give me name and phone please")
        except IndexError:
            print("You entered incorrect data")
        except TypeError:
            print("Wrong input type")
        return result
    return wrapper     

number_phone = {}

@input_error
def hello(*args):
    return f"How can I help you?"

@input_error
def add(*args):
    name = args[0]
    phone = args[1]
    number_phone[args[0]] = args[1]
    return f"Add success {name} {phone}"

@input_error
def change(*args):
    name = args[0]
    phone = int(args[1])
    phone = args[1]
    if number_phone.get(args[0]):
        number_phone[args[0]] = args[1]
        return f"Change success {name} {phone}"
    return f"Change error {name} {phone}"

@input_error
def phone(*args):
    name = args[0]
    phone = ""
    if number_phone.get(args[0]):
        phone = number_phone[args[0]]
        return phone
    return "ERROR empty"

@input_error
def show_all():
    return number_phone

@input_error
def good_bye(*args):
    print("Good bye!")
    exit(0)
    return None

@input_error
def no_command(*args): # если нет add то мы создаем функцию которая возвращает "Unknown command"
    return "Unknown command"


def parser(text: str): -> tuple([callable, tuple([str]|None)]): 
    if text.lower().startswith("add"):
        return add, text.lower().replace("add", "").strip().split() 
    if text.lower().startswith("hello"):
        return hello, None
    if text.lower().startswith("change"):
        cmd = text.lower().replace("change", "")
        return change, cmd.strip().split()
    if text.lower().startswith("phone"):
        cmd = text.lower().replace("phone", "")
        return phone, cmd.strip().split()
    if text.lower().startswith("show all"):
        return show_all, None
    if text.lower().startswith("good bye") or text.lower().startswith("exit") or text.lower().startswith("close"):
        return good_bye, None 

    return no_command, None
    

def main():
    while True: 
        user_input = input(">>>")   
        command, args = parser(user_input) 
        if args != None:
            result = command(*args)  
        else:
            result = command()
        print(result)
    
if __name__ == "__main__":
    main()



