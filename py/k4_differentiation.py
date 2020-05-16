# Description:

# Create a function that differentiates a polynomial for a given value of x.

# Your function will receive 2 arguments: a polynomial as a string, and a point to evaluate the equation as an integer.

# Assumptions:
# There will be a coefficient near each x, unless the coefficient equals 1 or -1.
# There will be an exponent near each x, unless the exponent equals 0 or 1.
# All exponents will be greater or equal to zero
# Examples:
# differenatiate("12x+2", 3)      ==>   returns 12
# differenatiate("x^2+3x+2", 3)   ==>   returns 9

# SOLUTION
def differentiate(equation, point):
  terms_array = []
  index = 0
  for i in range(len(equation)):
    if equation[i] not in ['+', '-'] and i != len(equation) - 1:
      continue
    if i == len(equation) - 1:
      terms_array.append(equation[index:i+1])
    else:
      terms_array.append(equation[index:i])
    index = i
  
  terms_array = [i for i in terms_array if i != '']

  def diff_terms(terms):
    for i in range(len(terms)):
      if '^' in terms[i]:
        split_term = terms[i].split('x^')
        if split_term[0].replace('-', '').isnumeric() or split_term[0].replace('+', '').isnumeric():
          new_coefficient = int(split_term[0]) * int(split_term[1])  
        else:
          new_coefficient = int(f'{split_term[0]}{split_term[1]}')
        new_exponent = int(split_term[1]) - 1
        if new_exponent == 1:
          new_exponent = ''
        else:
          new_exponent = f"^{new_exponent}"
        new_term = f"{new_coefficient}x{new_exponent}"
        terms[i] = new_term
      elif terms[i] == 'x':
        new_term = '1'
        terms[i] = new_term
      elif terms[i][-1] == 'x':
        new_term = terms[i][:-1]
        if new_term == '+' or new_term == "-":
          new_term = {"+": '+1', '-': '-1', '': '+1'}[new_term]
        terms[i] = new_term
      else:
        terms[i] = ''
    
    return terms
  
  def substitute(term, value):
    new_term = term.replace('x', f'*{value}')
    new_term = new_term.replace('^', '**')
    return new_term
  
  diff_terms = diff_terms(terms_array.copy())
  diff_terms = [term for term in diff_terms if term != '']
  diff_terms = [f'+{term}' if term[0].isnumeric() else term for term in diff_terms]
  expression = [substitute(term, point) for term in diff_terms]
  eval_expression = [eval(term) for term in expression]
  final_value = sum(eval_expression)
  return final_value

# equation = input("Enter an equation: ")
# point = int(input("Enter a number: "))
# print(differentiate(equation, point))