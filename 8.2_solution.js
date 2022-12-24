// Given a number n find out if it is prime number or not
// Use javascript to find out difference between next prime number after X and X

//PRIME NUMBER OR NOT and NEXT PRIME NUMBER

function isprime(n) {
    if (n > 1) {
      for (let i = 2; i < n; i++ ) {
        if (n%i == 0) {
          return false;
        }
      }
      stop = true;
      return true;
    }
    else {
      return false;
    }
};

function nextprime(n){
    if (isprime(n) == false){
        return 'not a prime';
    } 
    else {
        let stop = true;
        let i = n+1;
        let ans = 0;
        while (stop) {
            if (isprime(i) == true) {
                ans = i;
                stop = false;
            }
            i +=1;
        }
        return ans;
    }
};

console.log(isprime(7));
console.log(nextprime(7));

