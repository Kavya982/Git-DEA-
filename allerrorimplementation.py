def handle_all_exceptions():
    try:
        # 1. ZeroDivisionError
        x = 10 / 0

        # # 2. ValueError
        num = int("abc")

        # 3. IndexError
        my_list = [1, 2, 3]
        print(my_list[5])

        # 4. KeyError
        my_dict = {"a": 1, "b": 2}
        print(my_dict["z"])

        # 5. FileNotFoundError
        with open("non_existent_file.txt", "r") as f:
            content = f.read()

        # 6. TypeError
        result = "5" + 5

        # 7. AttributeError
        none_obj = None
        none_obj.append(5)

        # 8. NameError
        print(undefined_variable)

    except ZeroDivisionError:
        print("ZeroDivisionError: Cannot divide by zero.")
    except ValueError:
        print("ValueError: Invalid conversion to integer.")
    except IndexError:
        print("IndexError: Index out of range.")
    except KeyError:
        print("KeyError: Key not found in dictionary.")
    except FileNotFoundError:
        print("FileNotFoundError: File not found.")
    except TypeError:
        print("TypeError: Mismatched data types.")
    except AttributeError:
        print("AttributeError: Invalid attribute used.")
    except NameError:
        print("NameError: Variable is not defined.")
    except Exception as e:
        print(f"Other Exception: {e}")
    else:
        print("No exceptions occurred.")
    finally:
        print("Execution complete.")


handle_all_exceptions()
