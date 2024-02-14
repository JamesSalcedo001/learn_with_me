// STRING METHODS



// 1: System.out.println(): prints to console




// public class LearnJava {
//     public static void main(String[] args) {
//         System.out.println("Hello World");
//     }
// }







// 2: charAt ==> returns the character at the specified index of a string



// public class LearnJava {
//     public static void main(String[] args) {
//         String str = " Hello, World! ";

//         System.out.println("charAt(0): ==> " + str.charAt(0));
//         System.out.println("charAt(1): ==> " + str.charAt(1));
//         System.out.println("charAt(2): ==> " + str.charAt(2));
//         System.out.println("charAt(3): ==> " + str.charAt(3));
//     }
// }





// 3: length ==> returns the length of a string(number of characters)




// public class LearnJava {
//     public static void main(String[] args) {
//         String s = "Hello";
//         String a = "Apples";
//         String b = "Bananas";
//         String c = "Canteloupe";

//         int len = s.length();
//         int len_a = a.length();
//         int len_b = b.length();
//         int len_c = c.length();

//         System.out.println("length of string 'Apples' ==> " + len_a);
//         System.out.println("\n***\n");
//         System.out.println("length of string 'Bananas' ==> " + len_b);
//         System.out.println("\n***\n");
//         System.out.println("length of string 'Canteloupe' ==> " + len_c);
//         System.out.println("\n***\n");
//         System.out.println("length of string 'Hello' ==> " + len);
//         System.out.println("\n***\n");
//         // normally can't automatically concatenate when logging so this second approach also works when combining strings and variables
//         System.out.println(String.format("length of string 'Hello' ==> %d", len));
//     }
// }






// 4: substring(start_index, end_index): returns new string that is substring of original, starting from the beginning index(inclusive) to the end index(exclusive)




public class LearnJava {
    public static void main(String[] args) {
        String s = "Hello";
        String a = "Apples";
        String b = "Bananas";
        String c = "Cherries";


        String sub = s.substring(1, 4);
        String sub_a = a.substring(1, 3);
        String sub_b = b.substring(0, 2);
        String sub_c = c.substring(0, 4);

        System.out.println("string from index[1] - index[3](excluded) of 'Apples' ==>" + sub_a);

        System.out.println("\n***\n");

        System.out.println("string from index[0] - index[2]excl. of 'Bananas' ==> " + sub_b);
        System.out.println("\n***\n");

        System.out.println("string from index[0]-index[4]excl of 'Cherries' ==> " + sub_c);
        System.out.println("\n***\n");


        System.out.println("string from index[1] - index[4](excluded) of 'Hello' ==> " + sub);
    }
}