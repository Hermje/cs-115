void primeFactors(int n)
{
    bool isPrime = 1;
    // Print the number of 2s that divide n
    for (int i = 2; i < number; i++)
    {
      if(number % i == 0)
      {
        isPrime = 0
      }
    }
    if(isPrime == 0)
      while (n%2 == 0)
      {
          printf("%d ", 2);
          n = n/2;
      }

      // n must be odd at this point.  So we can skip
      // one element (Note i = i +2)
      for (int i = 3; i <= sqrt(n); i = i+2)
      {
          // While i divides n, print i and divide n
          while (n%i == 0)
          {
              printf("%d ", i);
              n = n/i;
          }
      }

      // This condition is to handle the case when n
      // is a prime number greater than 2
      if (n > 2)
      {
        printf ("%d ", n);
      }
    }
    else
    {
      cout << number << " is a prime number"
    }
}
