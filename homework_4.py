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


def parser(text: str): #-> tuple([callable, tuple([str]|None)]):  #parser на вход принимает текс и возвращает tuple
    if text.lower().startswith("add"):  # здесь мы разбираем текст по запчастям для функции add
        return add, text.lower().replace("add", "").strip().split() # здесь возвращаем параметр add и реплейсим add на пустую строку
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
    while True: # бесконечный цикл
        user_input = input(">>>")  # можно сюда записать любое приглашение, здесь мы спрашиваем у пользователя запросы 
        command, args = parser(user_input) #здесь мы отправляем user_input в парсер, который всегда возвращает какую-то функцию
        if args != None:
            result = command(*args)  # например мы ожидаем здесь ввод команды, далее мы пишем функцию парсера
        else:
            result = command()
        print(result)
    
if __name__ == "__main__":
    main()

# основное в дз у нас должен быть основной цикл. Команды можно собрать в словарь, в словаре у 
# вас будет команда и список значений либо одно значение, и все эти команды нужно завернуть в 
# декоратор
# Декоратор має бути застосований до кожної командної функції.
# Також зверніть увагу, що Ви повторюєтеся в словнику COMMANDS.
# Тут не потрібно використовувати модифікатор global для доступу до словника контактів.
# Ну і рішення з пошуком по патерну - не саме вдале( При додаванні нового іункціоналу, 
# Вам доведеться це змінювати в трьох місціх - створити нову функцію, додати до словника 
# COMMANDS, а також - виправити патерн

#1 Як команда розпізнається ПЕРШЕ слово, інше ігнорується:
# Приклад:
#    Як команда "ЗАВЕРШЕННЯ роботи бота спрацює наступне:
#    "close kjdfhgkjdfhg"
# 2. Але команди можуть бути і ПОДВІЙНІ тому аналогічно:
#     "show all орплвлрыkjhskjhd"
# По этой команде бот выводит все сохраненные контакты с номерами телефонов в консоль.
# Це підкаазки Макса, але
# Якщо хтось вже консультувався з цього приводу з ментором welcome
# Поділіться своїми знаннями.