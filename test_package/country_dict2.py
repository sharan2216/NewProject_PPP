def give_me_a_key():
    key = input("Press a key in keyboard:")
    result = ''
    try:
        num = int(key)

    except:
        if key.isalpha():
            result = key.upper()
        else:
            result = key
    else:
        result = num ** 2
    finally:
        return result

print(give_me_a_key())
