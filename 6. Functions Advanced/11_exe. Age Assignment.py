def age_assignment(*args, **kwargs, ):
    for name in args:
        if name[0] in kwargs:
            kwargs[name] = kwargs.pop(name[0])
    return kwargs


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))