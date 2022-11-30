def parser(formula):
    change=[[' ',''],['||','|'],['&&','&'],['or', '|'],['and','&'],['implies','>'],['->','>'],['next','X'],['eventually','F'],['always','G']]
    operatorSimpleL=[')',']']
    operatorSimpleR=['X','F','G','(','[']
    operatorDouble=['|','&','U','R','>']
    closeoperator=[')',']']
    openoperator=['(','[']
    operator=operatorSimpleL+operatorSimpleR+operatorDouble
    for operator_change in change:
        formula=formula.replace(operator_change[0],operator_change[1])
    def cut(formula):
        new_formula=[]
        tmp=''
        for letter in formula:
            if letter in operator:
                if tmp!='':
                    new_formula.append(tmp)
                new_formula.append(letter)
                tmp=''
            else:
                tmp+=letter
        new_formula.append(tmp)
        return new_formula
    cut_formula=cut(formula)
    def verif_paranthese(formula):
        cmpt=0
        for obj in formula:
            if obj in openoperator:
                cmpt+=1
            elif obj in closeoperator:
                cmpt+=-1
        return not(cmpt)
    if not(verif_paranthese(cut_formula)):
        return False
    
    cut_class=[]
    for obj in cut_formula:
        if obj in operatorDouble:
            cut_class.append('D')
        elif obj in operatorSimpleL:
            cut_class.append('L')
        elif obj in operatorSimpleR:
            cut_class.append('R')
        else:
            cut_class.append('AP')
    def verif(list_cut):
        if not(list_cut[0]=='AP' or list_cut[0]=='L'):
            return False
        for id_obj in range(len(list_cut)-1):
            print(id_obj)
            if list_cut[id_obj]=='R':
                if (list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='D'):
                    return False
            elif list_cut[id_obj]=='D':
                if (list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='D'):
                    return False
            elif list_cut[id_obj]=='AP':
                if (list_cut[id_obj+1]=='R'  or list_cut[id_obj+1]=='AP') :
                    return False
            elif list_cut[id_obj]=='L':
                if (list_cut[id_obj+1]=='AP' or list_cut[id_obj+1]=='L' or list_cut[id_obj+1]=='R'):
                    return False
        if (list_cut[-1]=='R' or list_cut[-1]=='D'):
            return False
        return True     
    return verif(cut_class),cut_formula,cut_class

test='abcabc|| abcabc&&abcorabcandabcorimpliesnextabcoralwaysalwaysabcafe'
print(parser(test))

    
##    def find(formula,to_find):
##        all_id_find=[]
##        lenfind=len(to_find)
##        for id_formula in range(len(formula)-lenfind):
##            if formula[id_formula:id_formula+lenfind]==to_find:
##                all_id_find.append(id_formula)
##        return all_id_find
##    def reduce(formula,list_change):
##        for change_operator in change:
##            all_id_find=find(formula,change_operator).reverse()
##            if all_id_find!=[]:
##                for id_op in all_id_find:
##                    
##            
##            
            
