// Description:
// Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

// Examples:

// solution('abc') // should return ['ab', 'c_']
// solution('abcdef') // should return ['ab', 'cd', 'ef']

// SOLUTION
function solution(str){
  const stringArray = str.replace(/[' ']/g, '').split('')
  const returnArray = []
  if (stringArray.length % 2 !== 0) stringArray.push('_')
  for (let i = 0; i < stringArray.length - 1; i += 2) {
    const string = `${stringArray[i]}${stringArray[i + 1]}`
    returnArray.push(string)
  }
  return returnArray
}