def chek(vr,vv=None):
    """(x = Variable ) => Type Variable
       (x = Variable , y = Type) => bool
       => | int | float | str_fh | str_g | khali | list | bool | tuple | none |"""
    typ = str(type(vr))
    a = ["0","1","2","3","4","5","6","7","8","9"]
    a10 = ["a","b","c","d","e","f","j","h","i","g","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    t = 1
    t1 = 1
    chek = 0
    chek1 = 0
    mo = 0
    ris = "1"
    bo = 0
    boo = 0
    if vr == "" :
        akhar = "khali"
    elif typ == "<class 'tuple'>" :
        akhar = "tuple"
    elif typ == "<class 'list'>" :
        akhar = "list"
    elif typ == "<class 'int'>" :
        akhar = "int"
    elif typ == "<class 'bool'>" :
        akhar = "bool"
    elif typ == "<class 'float'>" :
        akhar = "float"
    elif typ == "<class 'NoneType'>" :
        akhar = "none"
    elif vr == True or vr == False :
        akhar = "bool"
    elif typ == "<class 'str'>" :
        vr = vr.strip()
        tol = len(vr)
        while t < tol + 1 :
            m = vr[chek]
            while t1 < len(a) + 1:
                if m == "." :
                    boo = boo + 1
                    bo = bo + 1
                if m == a[chek1] :
                    bo = bo + 1
                    if t == tol and bo == len(vr) :
                        ris = "int"
                    
                t1 = t1 + 1
                chek1 = chek1 + 1
            chek = chek + 1
            t = t + 1
            t1 = 1
            chek1 = 0


    # kar


        if ris == "int" :
            akhar = "int"
        elif boo == 10 :
            akhar = "float"
        elif bo == 0 :
            vr = vr.lower()
            tol = len(vr)
            t = 1
            t1 = 1
            chek = 0
            chek1 = 0
            mo = 0
            bo = 0
            boo = 0

            while t < tol + 1 :
                m = vr[chek]
            
                while t1 < len(a10) + 1:
                    if m == a10[chek1] :
                        bo = bo + 1
                        if t == tol and bo == len(vr) :
                            akhar = "str_fh"
                    
                    t1 = t1 + 1
                    chek1 = chek1 + 1
                chek = chek + 1
                t = t + 1
                t1 = 1
                chek1 = 0
        else :
            akhar = "str_g"

    if vv == "str_g" or vv == "str_fh" or vv == "float" or vv == "int" or vv == "bool" or vv == "list" or vv == "khali" or vv == "none" or vv == "tuple":
        if akhar == vv :return (True)
        else : return (False)
    else :return (akhar)
        
    


