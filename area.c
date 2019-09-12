// Forms Area Calculation

#include <stdio.h>
#include <stdlib.h>

#include <math.h>

#define PI 3.14159265359


int main(void){
	
	printf("Area Calculation\n") ; 
	printf("1. Square\n2. Rectangle\n3. Triangle\n4. Disc\n") ;
	
	printf("Choose the form : ") ;
	
	int Choice ;
	scanf("%d", &Choice) ; 

	switch (Choice) {
		
		case (1) :
			{ 
				float side ;
				printf("Côté : ") ;	
				scanf("%f", &side) ;
				float result = side*side ;
				printf("Area of the square : %f\n", result) ;
				break ; 
			}

		case (2) :
			{ 
				float width ;
				float height ;
				printf("Width : ") ;
				scanf("%f", &width) ;
				printf("height : ") ;
				scanf("%f", &height) ;
				float result = width*height ;
				printf("Area of the retangle : %f\n", result) ;
				break ; 
			}

		case (3) :
			{
				float base ;
				float height ;
				printf("Base : ") ;
				scanf("%f", &base) ;
				printf("Height : ") ;
				scanf("%f", &height) ;
				float result = base*height ;
				printf("Area of the triangle : %f\n", result) ;
				break ;
			}
	
		case (4) :
			{
				float radius ;
				printf("Radius : ") ;
				scanf("%f", &radius) ;
				float result=radius*radius*PI ;
				printf("Area of the disc : %f\n", result) ;
				break ;
			}

		default :
			break ;

	}

}

			

