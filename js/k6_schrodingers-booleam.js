// Description:
// Can a value be both true and false?

// Define omniBool so that it returns true for the following:

// omniBool == true && omniBool == false

// SOLUTION
const omnibool = { n: 1, valueOf: () => this.n = !this.n }