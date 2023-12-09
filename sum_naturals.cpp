// Project: Sum of First n Natural Numbers
// By: Andrew Ruvinsky
// Created: December 2023
// ---------------------------------------
#include<iostream>
using namespace std;

int summation(int num) { // Sums natural numbers from 1 to input
  int result=0;
  result = num+1;
  result *= num;
  result /= 2;
  return result;
}

bool is_num(string input) { // Checks if input is a natural number
  if (input[0] == '0')
    return false;
  for (int i=0; i<input.size(); i++) {
    if (!isdigit(input[i]))
      return false;
  }
  return true;
}

int main() {
  string input="";
  int good_num=0;

  cout << "Enter a natural number: ";
  while(true) {
    cin >> input; 
    if (is_num(input)) { // If input is a natural number
      good_num = stoi(input);
      cout << "Sum of natural numbers from 1 to " << good_num << ": " << summation(good_num) << endl;
      break;
    } else {
      cout << "Invalid input, please enter a natural number: ";
    }
  }
  return 0;
}
