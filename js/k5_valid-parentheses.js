// Description:
// Write a function called that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

// Examples
// "()"              =>  true
// ")(()))"          =>  false
// "("               =>  false
// "(())((()())())"  =>  true
// Constraints
// 0 <= input.length <= 100

// SOLUTION
function validParentheses(parens){
  const workString = parens.split('').map(item => item === ')' ? '}' : '{').join('')
  try {
    return !eval(workString)
  } catch (e) {
    return false
  }
}