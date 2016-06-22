using System;

class _03CastingDemo{
	static void Main() {
		// define variables as x
		int i = 3, j = 2;
		float fraction;

		// specifying format required
		fraction = (float) i / (float) j;

		// as a float decimal place is returned
		Console.WriteLine("Fraction: " + fraction);
	}
}

