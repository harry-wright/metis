using System;

class _01GlazerCalc {
	// present, nil-value, method
	static void Main() {
		double width, height, woodLength, glassArea;
		string widthString, heightString;

		// gets widths value as a string from user input
		widthString = "5";

		// converts string to double
		// double.Parse is not part of 'System'
		width = double.Parse(widthString); 

		heightString = "6";
		height = double.Parse (heightString);

		// calculate length in feet
		woodLength = 2 * (width + height) * 3.25;

		// calculate area
		glassArea = 2 * (width * height);

		// console is 'public static class' within 'System'
		Console.WriteLine ("The length of the wood is " +
		woodLength + " feet");

		Console.WriteLine ("The area of the glass is " +
		glassArea + " square metres");
	}
}