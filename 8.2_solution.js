// Given a number n find out if it is prime number or not
// Use javascript to find out difference between next prime number after X and X

PRIME NUMBER OR NOT

if ( n == 1 ) {
  console.log("Neither prime nor composite");
}
else if (n > 1) {
  for (let i = 2; i < number; i++ ) {
    if (number%i == 0) {
      console.log("Not a prime number");
      break;
    }
  }
}
else {
  console.log("Not a prime number");
};


