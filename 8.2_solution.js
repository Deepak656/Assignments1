// Given a number n find out if it is prime number or not
// Use javascript to find out difference between next prime number after X and X

PRIME NUMBER OR NOT

n = 17
if ( n == 1 ) {
  console.log("Neither prime nor composite");
}
else if (n > 1) {
  for (let i = 2; i < n; i++ ) {
    if (n%i == 0) {
      console.log("Not a prime number");
      break;
    }
  }
  console.log("Prime number");
}
else {
  console.log("Not a prime number");
}

