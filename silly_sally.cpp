// Project: Silly Sally
// Started: 03/12/2023
// By: Andrew Ruvinsky

#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  bool sallyLike = false;     // 10,12 Variables initalization
  string guess = "";
  string lowercaseGuess = "";

  cout << endl << "**********************************************" << endl;
  cout << "Welcome to Silly Sally!" << endl << endl;  // Welcome paragraph 
  cout << "Can you figure out what Silly Sally likes" << endl;
  cout << "and doesn't like? Enter a single word below" << endl;
  cout << "and I'll tell you if she likes it or not!" << endl;
  cout << "Enter \"QUIT\" at any time to quit the game." << endl;
  cout << "**********************************************" << endl;

  for (int i=0; i<1;) {       // Outer loop makes it possible for user to guess as many times as they want
    sallyLike = false;        // 20,22 Resets variables after each guess
    guess = "";
    lowercaseGuess = "";

    cin >> guess;
    if (guess == "QUIT") {    // Force quit game
      break;
    }
    lowercaseGuess = guess;   // 25,26 Original guess is kept in guess, while lowercase guess is kept in lowercaseGuess
    transform(lowercaseGuess.begin(), lowercaseGuess.end(), lowercaseGuess.begin(), ::tolower); 

    /************************************************
    * NOTE: User guess is changed to all lowercase,
    * allowing program to view the user's guess
    * case insensitively!
    ************************************************/

    for (int i=0; i<guess.size()-1; i++) {  // Loop looks at the current character and the character following to see if they're the same
      if (lowercaseGuess.at(i) == lowercaseGuess.at(i+1)) { // Does this for every character besides last
        sallyLike = true;
        break;                              // As soon as double letters are found, exit loop!
      }
    }

    if (sallyLike == true) {
      cout << "Silly Sally likes " << guess << "." << endl;
    } else {
      cout << "Silly Sally doesn't like " << guess << "." << endl;
    }
  }

  return 0;
}
