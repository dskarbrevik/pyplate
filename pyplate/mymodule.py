def say_hi():
    """_summary_
    says hi.

    """    
    return "hi there"

def say_hi_to_me(name: str):
    """_summary_
    says hi with your name.
    
    Args:
        name (str): does a thing
    """    
    print("hi {name}!")

def func(arg1, arg2):
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    return True

class Class:
    """Summary line.

    Extended description of class

    Attributes:
        attr1 (int): Description of attr1
        attr2 (str): Description of attr2
    """

def get_random_ingredients(kind=None):
    """
    Return a list of random ingredients as strings.

    :param kind: Optional "kind" of ingredients.
    :type kind: list[str] or None
    :raise lumache.InvalidKindError: If the kind is invalid.
    :return: The ingredients list.
    :rtype: list[str]

    """
    return ["shells", "gorgonzola", "parsley"]