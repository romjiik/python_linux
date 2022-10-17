class calculator():
    
    
    def __init__(self, row):
        self.row = list(row.replace(' ',''))
        self.operator_list = ['-','+','*','^','/','(',')']
        self.operator_dict = {'-' : 1  ,'+' : 1 ,'*' : 2 ,'/' : 2 ,'^' : 3 ,'(': None ,')':None}
        pass
    
        
    def normalization(self):  
        row = self.row
        operator_list = self.operator_list
        norm_row = []
        save_row = []
        for i in range(len(row)):
            if row[i] in operator_list:
                try:
                    if row[i - 1] in operator_list[:-1] and row[i] == '-' :
                        save_row.append(row[i])
                    else:
                        norm_row.append(''.join(save_row))
                        norm_row.append(row[i])
                        save_row = []                
                except IndexError:
                    norm_row.append(''.join(save_row))
                    norm_row.append(row[i])
                    save_row = []
            else:
                save_row.append(row[i])
            if i == len(row) - 1:
                norm_row.append(''.join(save_row))
        norm_row = list(filter(lambda a: a != '', norm_row ))
        if norm_row[-1] == ')':
            norm_row += ['+', '0']
        return norm_row
    
    
    def operations(self, operator, a, b):
        if operator == '-':
            return float(a) - float(b)
        elif operator == '+':
            return float(a) + float(b)
        elif operator == '/':
            return float(a) / float(b)
        elif operator == '*':
             return float(a) * float(b)
        else:
             return float(a) ** float(b)

    def calculation(self):
        
        norm_row = self.normalization()
        operator_dict = self.operator_dict
        
        stack_1 = []
        stack_2_1 = []
        stack_2_2 = []

        for i in range(len(norm_row)):
            if norm_row[i] in operator_dict.keys():
                stack_2_1.append(norm_row[i])
                stack_2_2.append(operator_dict[norm_row[i]])
            else:
                stack_1.append(norm_row[i])
            try:
                if stack_2_1[-1] == ')':
                    del stack_2_1[-1], stack_2_2[-1]
                    while stack_2_1[-1] !='(':
                        operator = stack_2_1[-1]
                        number_1 = stack_1[-1]
                        number_2 = stack_1[-2]
                        del stack_2_1[-1], stack_1[-2::], stack_2_2[-1]
                        stack_1.append(self.operations(operator,number_2, number_1))
                    del stack_2_1[-1], stack_2_2[-1]
            except IndexError:
                None
            if (i == len(norm_row) - 1) & (norm_row[-1] ==')'):
                print(stack_1[0]) 
            try:    
                while stack_2_2[-1] <= stack_2_2[-2]:
                    operator = stack_2_1[-2]
                    number_1 = stack_1[-1]
                    number_2 = stack_1[-2]
                    del stack_2_1[-2], stack_1[-2::], stack_2_2[-2]
                    stack_1.append(str(self.operations(operator,number_2, number_1)))
            except IndexError:
                None  
            except TypeError:
                None
            if (i == len(norm_row) - 1) & (norm_row[-1] !=')') :
                while len(stack_2_1)>0:
                    operator = stack_2_1[-1]
                    number_1 = stack_1[-1]
                    number_2 = stack_1[-2]
                    del stack_2_1[-1], stack_1[-2::], stack_2_2[-1]
                    stack_1.append(str(self.operations(operator,number_2, number_1)))
                print(stack_1[0])


print('Введите пример') 
entry = str(input())
try:
    formula = calculator(entry)
    formula.calculation()
except DivisionByZero:
    print('Ошибка, деление на ноль')
