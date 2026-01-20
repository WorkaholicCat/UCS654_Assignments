# UCS654_Assignments
Assignments of UCS654: Predictive Analytics using Statistics
----------------------------------------------------------------
Assignment-1 Methodology:
-We utilize the India Air Quality dataset, focusing specifically on the NO_2 feature (x)
-Then using roll no (in my case 102303941), we create non-linear mapping and calculate parameters and function:
            a = 0.05 (102303941 mod 7) 
            b = 0.3 (102303941 mod 3 + 1)
            z = x + a * np.sin(b * x)             {here x is our feature NO_2}
- We fit the transformed data z to the model p(z) = c * e^{-lambda(z-mu)^2}
- mu: We use Maximum Likelihood Estimation (MLE), which for a Gaussian is arithmetic mean of z
- lambda: This parameter represents the "precision." It is derived by calculating the variance of z
- c: This is the normalization constant. This constant is necessary to ensure that the total area under the probability density curve represented by the integral of        the function from negative infinity to positive infinity is exactly equal to 1. It is calculated by taking the reciprocal of the standard deviation ($\sigma$)         multiplied by the square root of two pi.
