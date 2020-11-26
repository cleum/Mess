#include <stdio.h>
#include <stdlib.h>

int main(void) {

	float Height ;
	float Weight ; 

	printf("Your height (m) : ") ;
	scanf("%f",&Height) ;
       	printf("Your weight (kg) : ") ;
	scanf("%f",&Weight) ;

	printf("BMI calculation ...\n") ;

	float BMI ;
	BMI = Weight/(Height*Height) ;

	printf("Your BMI : %f\n", BMI) ;
 

	if ( BMI >= 17.5 && BMI <= 25 ) {
		printf("Your weight is considered as healthy\n") ;
	}

	if ( BMI < 17.5 ) {
		printf("According to an uncertain science you should eat more... But do whatever you want.\n") ;
	}
	
	if ( BMI > 25 ) {
		printf("According to an uncertain science you should eat less... But do whatever you want.\n") ; 
	}

}
