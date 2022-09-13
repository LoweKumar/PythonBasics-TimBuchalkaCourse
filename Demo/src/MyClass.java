public class MyClass {
    public static void main(String args[]) {
        int z = 10;
//        for(int i=0;i<=5;i++){
//            z= z+i;
//        }
//        System.out.println("Sum of no from 1 to 5 = " + z);
        int x=z;
        System.out.println(x);
        z+=20; //updating the no z
        System.out.println(x); //in python here x value would be updated as 30
        System.out.println(z);

    }
}

/* in python
i = [1,2,3,4,5]
print(sum(int(val) for val in i))
*/
